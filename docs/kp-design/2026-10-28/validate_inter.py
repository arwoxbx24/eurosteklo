"""Проверка вёрстки холста Claude Design (артборды .dc.html) перед выдачей ППО.

Что делает: открывает каждый артборд из canvas.json в Chromium (Playwright) в размере $preview,
подключает Montserrat локально (рантайм редактора support.js вне Claude недоступен — рендер приближённый),
ищет текст за краем слайда, обрезанный текст в блоках, наложения абсолютно позиционированных подписей,
проверяет теги и нумерацию «N / M», сохраняет снимки render/NN.png. Снимки ОБЯЗАТЕЛЬНО смотреть глазами:
скрипт не видит текст, срезанный clip-path (ромбы).

Запуск:
  pip install playwright && npm i @fontsource/montserrat   (Chromium уже есть в среде агента)
  python3 tools/validate_canvas.py <папка с canvas.json> --fonts <путь>/node_modules/@fontsource/montserrat/files
Итог: «TOTAL ISSUES 0» + просмотр снимков = вёрстка проверена.
"""
import argparse, json, re, pathlib
from html.parser import HTMLParser
from playwright.sync_api import sync_playwright

VOID = {'meta', 'link', 'br', 'img', 'input', 'hr'}

CHECK = r"""
() => {
  const s = document.querySelector('.slide') || document.body.firstElementChild; const sr = s.getBoundingClientRect();
  const res = {overflow: [], clipped: [], overlaps: []};
  const txt = e => (e.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60);
  for (const e of s.querySelectorAll('*')) {
    const r = e.getBoundingClientRect(); if (!r.width || !r.height) continue;
    if (e.children.length === 0 || e.matches('td,li,p,h1,h2,h3,.box,.lbl,.rl,.pl,.mb,.dia,.md,.chip')) {
      if (r.right > sr.right + 1 || r.bottom > sr.bottom - 20 || r.left < sr.left - 1)
        res.overflow.push([e.tagName + '.' + e.className, Math.round(r.right - sr.left), Math.round(r.bottom - sr.top), txt(e)]);
    }
    if (e.matches('.card,.box,.mb,.dia,.md,td') && (e.scrollHeight > e.clientHeight + 2 || e.scrollWidth > e.clientWidth + 2))
      res.clipped.push([e.className || e.tagName, e.scrollWidth - e.clientWidth, e.scrollHeight - e.clientHeight, txt(e)]);
  }
  const abs = [...s.querySelectorAll('.box,.lbl,.rl,.dia,span.pl,div.card')].filter(e => getComputedStyle(e).position === 'absolute');
  for (let i = 0; i < abs.length; i++) for (let j = i + 1; j < abs.length; j++) {
    const a = abs[i], b = abs[j]; if (a.contains(b) || b.contains(a)) continue;
    const r1 = a.getBoundingClientRect(), r2 = b.getBoundingClientRect();
    const w = Math.min(r1.right, r2.right) - Math.max(r1.left, r2.left), h = Math.min(r1.bottom, r2.bottom) - Math.max(r1.top, r2.top);
    if (w > 2 && h > 2) res.overlaps.push([txt(a), txt(b), Math.round(w), Math.round(h)]);
  }
  return res;
}
"""


def tags_ok(src):
    class P(HTMLParser):
        def __init__(self):
            super().__init__(); self.st = []; self.err = 0
        def handle_starttag(self, t, a):
            if t not in VOID: self.st.append(t)
        def handle_endtag(self, t):
            if t in VOID: return
            if self.st and self.st[-1] == t: self.st.pop()
            else: self.err += 1
    p = P(); p.feed(src)
    return not p.st and not p.err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('project', help='папка с canvas.json и артбордами')
    ap.add_argument('--fonts', required=True, help='папка с montserrat-*-normal.woff2 (@fontsource/montserrat/files)')
    a = ap.parse_args()
    proj = pathlib.Path(a.project).resolve(); fonts = pathlib.Path(a.fonts).resolve()
    out = proj / 'render'; out.mkdir(exist_ok=True)
    ff = ''
    for w in (400, 500, 600, 700, 800):
        for sub, rng in (('cyrillic', 'U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116'),
                         ('latin', 'U+0000-00FF,U+2000-206F,U+20BD,U+2190-21FF')):
            ff += f"@font-face{{font-family:Inter;font-weight:{w};src:url('file://{fonts}/inter-{sub}-{w}-normal.woff2') format('woff2');unicode-range:{rng}}}\n"
    order = json.load(open(proj / 'canvas.json', encoding='utf-8'))['order']
    total = len(order); problems = 0
    with sync_playwright() as p:
        br = p.chromium.launch()
        for i, f in enumerate(order, 1):
            src = (proj / f).read_text(encoding='utf-8')
            m = re.search(r'"\$preview":\{"width":(\d+),"height":(\d+)\}', src)
            w, h = (int(m.group(1)), int(m.group(2))) if m else (1280, 720)
            issues = []
            if not tags_ok(src): issues.append('незакрытые теги')
            pg_m = re.search(r'>(\d+) / (\d+)<', src)
            if pg_m and (int(pg_m.group(1)) != i or int(pg_m.group(2)) != total):
                issues.append(f'нумерация {pg_m.group(0)} вместо {i} / {total}')
            if 'data:' in src: issues.append('data:-URI запрещён')
            src = src.replace('<script src="./support.js"></script>', '')
            src = re.sub(r'<link rel="stylesheet" href="https://fonts.googleapis.com[^>]*>', '', src)
            src = re.sub(r'href="\./([^"]+\.css)"', lambda mm: f'href="file://{proj}/{mm.group(1)}"', src)
            src = re.sub(r'/_blob/([0-9a-f]{32})', lambda mm: 'file:///tmp/claude-0/-home-claude/db59aa0e-48c1-5941-808f-853353ca79b2/scratchpad/logo/' + {'2d13f70378f3606a62bea08f50f6129b':'logo0.png','a3fe85a8f3531a642a989f06e9a121ac':'logo1.png'}.get(mm.group(1),'x'), src); src = src.replace('</head>', f'<style>{ff}</style></head>')
            tmp = out / f'_{f}.html'; tmp.write_text(src, encoding='utf-8')
            page = br.new_page(viewport={'width': w, 'height': h})
            page.goto(f'file://{tmp}'); page.evaluate('document.fonts.ready'); page.wait_for_timeout(150)
            r = page.evaluate(CHECK)
            page.screenshot(path=str(out / f'{i:02d}.png'), clip={'x': 0, 'y': 0, 'width': w, 'height': h})
            page.close(); tmp.unlink()
            for k in ('overflow', 'clipped', 'overlaps'):
                issues += [f'{k}: {it}' for it in r[k]]
            problems += len(issues)
            print(f'{i:2} {f:24} issues={len(issues)}')
            for it in issues: print('     ', it)
        br.close()
    print('TOTAL ISSUES', problems, '| снимки:', out)


if __name__ == '__main__':
    main()
