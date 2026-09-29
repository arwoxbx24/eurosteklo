#!/usr/bin/env python3
"""Общая сборка процесса ППО (лиды, сделки, …) из фрагментов _parts — механическое сведение.

Для процесса собираются три связанных HTML:
  karta-<slug>.html                  — карта процесса (BPMN), точки ведут в вопросы
  obsledovanie-<slug>.html           — сценарий встречи: ключевые вопросы, отметка ответа
  obsledovanie-<slug>-podrobno.html  — полная версия (источники, состояния, истории)

Фрагменты в <процесс>/_parts: karta.svg.html, tochki.html, sostoyaniya.html, pasport.html (необязателен).
Точки внутри — числа (title «Точка N:», id tN/pN); видимая метка — префикс + число (у сделок «С1»).
"""
import html
import re
from dataclasses import dataclass, field
from pathlib import Path

COMMON = Path(__file__).parent
CSS = (COMMON / "base.css").read_text(encoding="utf8")
ZOOM = (COMMON / "zoom.html").read_text(encoding="utf8")
# Имена окон: ссылки открывают документ во втором окне и переиспользуют его.
WIN_KARTA, WIN_OBSL = "evro-karta", "evro-obsl"
COMMON_CSS = """.docnav{margin-top:10px;font-size:15px}.docnav a{color:var(--accent);font-weight:600}"""


@dataclass
class Proc:
    slug: str                 # lidy / sdelki — имя каталога и суффикс файлов
    name: str                 # «Лиды»
    pfx: str = ""             # видимый префикс номера точки: "" у лидов, "С" у сделок
    item: str = "лид"         # «последний реальный <item>» в инструкции встречи
    item_last: str = "последний реальный лид"
    map_lead: str = ""
    short_lead: str = ""
    full_lead: str = ""
    full_intro: str = ""      # что в подробной версии
    layers: dict = field(default_factory=lambda: {"А": "Доска Романа", "Б": "По ТЗ", "В": "Портал"})
    ys: tuple = (900, 1650)   # границы слоёв А/Б/В по Y, если в svg нет <!-- layers: A<… B<… -->
    legend_src: str = ""

    @property
    def parts(self):
        return COMMON.parent / self.slug / "_parts"

    @property
    def out(self):
        return COMMON.parent / self.slug

    @property
    def files(self):
        return (f"karta-{self.slug}.html", f"obsledovanie-{self.slug}.html", f"obsledovanie-{self.slug}-podrobno.html")


def page(title, lead, body, extra_css="", nav=""):
    return f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{CSS}{extra_css}</style></head>
<body><div class="page" data-zoom><header><h1>{title}</h1><p class="lead">{lead}</p>{nav}</header>
{body}
</div>{ZOOM}</body></html>
"""


def txt(s):
    """Текст без тегов и без мелких ссылок на источники."""
    s = re.sub(r'<small class="src">.*?</small>', "", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(re.sub(r"\s+", " ", s)).strip()


def build(p: Proc):
    KARTA, SHORT, FULL = p.files
    lab = lambda n: f"{p.pfx}{n}"

    def docnav(current):
        items = [(KARTA, "Карта процесса", WIN_KARTA), (SHORT, "Вопросы к встрече", WIN_OBSL),
                 (FULL, "Подробная версия", WIN_OBSL)]
        links = [f'<b>{t}</b>' if f == current else f'<a href="{f}" target="{w}">{t}</a>' for f, t, w in items]
        return f'<nav class="docnav"><a href="../index.html">☰ Оглавление</a> · {p.name}: ' + " · ".join(links) + "</nav>"

    legend = f"""<section><h2>Как читать</h2><div class="legend">
<span><span class="st st-board">на доске</span> есть на доске Miro</span>
<span><span class="st st-said">со слов</span> запись экрана и речь интегратора</span>
<span><span class="st st-unk">не знаем</span> источника нет — спросить</span>
<span><span class="st st-conf">противоречие</span> источники расходятся</span>
<span><span class="pt">{p.pfx}N</span> конфликтная точка — вопрос в документе «Обследование»</span></div>
<p class="src">{p.legend_src}</p></section>"""

    # ---------- Карта ----------
    svg = (p.parts / "karta.svg.html").read_text(encoding="utf8")
    pf = p.parts / "pasport.html"
    pasport = pf.read_text(encoding="utf8") if pf.exists() else ""
    m = re.search(r"<!--\s*layers:\s*A<(\d+)\s+B<(\d+)\s*-->", svg)
    ya, yb = (int(m.group(1)), int(m.group(2))) if m else p.ys
    pts = []
    for m in re.finditer(r'<g class="pt"><title>Точка (\d+):\s*(.*?)</title><circle cx="([\d.]+)" cy="([\d.]+)"', svg, re.S):
        n, cy = int(m.group(1)), float(m.group(4))
        layer = "А" if cy < ya else ("Б" if cy < yb else "В")
        pts.append((layer, n, html.unescape(m.group(2))))
    # Красные точки карты — ссылки на вопрос в документе встречи; id="pN" для навигатора.
    svg = re.sub(r'<g class="pt">(<title>Точка (\d+):.*?</g>)',
                 lambda m: f'<a href="{SHORT}#t{m.group(2)}" target="{WIN_OBSL}"><g class="pt ptlink" id="p{m.group(2)}">{m.group(1)}</a>',
                 svg, flags=re.S)
    navbar = '<div class="ptnav" id="ptnav"><span class="ptnav-h">Найти точку:</span>'
    for L in "АБВ":
        items = sorted((x for x in pts if x[0] == L), key=lambda x: x[1])  # по номеру внутри слоя
        if items:
            navbar += f'<span class="ptg"><b>{L}. {p.layers[L]}</b>' + "".join(
                f'<button type="button" data-p="{n}" title="{html.escape(t)}">{lab(n)}</button>' for _, n, t in items) + "</span>"
    navbar += '<div class="ptsel" id="ptsel">Нажмите номер — карта прокрутится к точке и подсветит её.</div></div>'
    map_css = COMMON_CSS + """.mapwrap{overflow:auto;cursor:grab;border:1px solid var(--line);border-radius:8px;background:#fff}
.mapwrap.drag{cursor:grabbing;user-select:none}
.mapwrap svg{width:100%;min-width:1400px;height:auto;display:block}
.ptnav{position:sticky;top:0;z-index:20;background:var(--paper);border:1px solid var(--line);border-radius:8px;padding:8px 10px;margin-bottom:10px;display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;box-shadow:0 2px 8px rgba(0,0,0,.08)}
.ptnav-h{font-weight:700}.ptg{display:inline-flex;gap:4px;align-items:center;flex-wrap:wrap}.ptg b{font-size:14px;color:var(--muted);margin-right:2px}
.ptg button{min-width:32px;height:32px;border-radius:50%;border:0;background:var(--pt);color:#fff;font:800 15px system-ui,sans-serif;cursor:pointer}
.ptg button.on{outline:3px solid #1d2530}
.ptsel{flex:1 1 100%;font-size:15px;color:var(--ink)}.ptsel a{color:var(--accent);font-weight:700}
@keyframes ptflash{0%,100%{stroke-width:2;r:14}50%{stroke:#ffd400;stroke-width:8;r:26}}
.pt.flash circle{animation:ptflash .7s ease-in-out 4;stroke:#ffd400}
.ptlink{cursor:pointer}.ptlink:hover circle{fill:#8c1d1d}"""
    pan = """<script>(function(){var w=document.querySelector('.mapwrap');if(!w)return;var x,y,sl,st,on=false;
w.addEventListener('mousedown',function(e){if(e.target.closest('a'))return;on=true;x=e.pageX;y=e.pageY;sl=w.scrollLeft;st=w.scrollTop;w.classList.add('drag')});
addEventListener('mouseup',function(){on=false;w.classList.remove('drag')});
addEventListener('mousemove',function(e){if(!on)return;w.scrollLeft=sl-(e.pageX-x);w.scrollTop=st-(e.pageY-y)});
function go(n){var g=document.getElementById('p'+n);if(!g)return;g.scrollIntoView({behavior:'smooth',block:'center',inline:'center'});
document.querySelectorAll('.pt.flash').forEach(function(x){x.classList.remove('flash')});void g.getBBox();g.classList.add('flash');
document.querySelectorAll('.ptg button').forEach(function(b){b.classList.toggle('on',b.dataset.p==n)});
var t=g.querySelector('title');document.getElementById('ptsel').innerHTML='<b>Точка {PFX}'+n+'.</b> '+(t?t.textContent.replace(/^Точка \\d+:\\s*/,''):'')+' · <a href="{SHORT}#t'+n+'" target="{WIN_OBSL}">вопрос к встрече →</a>';}
document.getElementById('ptnav').addEventListener('click',function(e){var b=e.target.closest('button[data-p]');if(b)go(b.dataset.p)});
function fromHash(){var m=location.hash.match(/^#p(\\d+)$/);if(m)setTimeout(function(){go(m[1])},150)}
addEventListener('hashchange',fromHash);fromHash();})();</script>"""
    pan = pan.replace("{SHORT}", SHORT).replace("{WIN_OBSL}", WIN_OBSL).replace("{PFX}", p.pfx)
    (p.out / KARTA).write_text(page(
        f"Евростекло · {p.name}: карта процесса", p.map_lead,
        (f'<section><details><summary><b>Паспорт процесса: кто есть кто</b> — участники, роли (раскрыть)</summary>{pasport}</details></section>' if pasport else '')
        + legend + f'<section><h2>Карта «{p.name}»</h2><p class="src">Карту можно тянуть мышью; масштаб — кнопки справа внизу или Ctrl + колесо.</p>'
        + navbar + f'<div class="mapwrap">{svg}</div></section>' + pan,
        map_css, docnav(KARTA)), encoding="utf8")

    # ---------- Подробная версия ----------
    tochki = (p.parts / "tochki.html").read_text(encoding="utf8")
    sost = (p.parts / "sostoyaniya.html").read_text(encoding="utf8")
    m = re.search(r'<section id="top5">.*?</section>', tochki, re.S)
    top5 = m.group(0) if m else ""
    tochki_body = tochki.replace(top5, "")
    card_css = COMMON_CSS + """.card{border:1px solid var(--line);border-left:6px solid var(--pt);border-radius:8px;padding:14px 18px;margin:16px 0;background:#fff}
.card header{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
.card dl{display:grid;grid-template-columns:220px 1fr;gap:6px 16px;margin:0}
.card dt{font-weight:700;color:var(--muted)}.card dd{margin:0}
.card dd.q{font-weight:700;color:var(--accent);font-size:18px}
.card ul{margin:0;padding-left:20px}
@media (max-width:700px){.card dl{grid-template-columns:1fr}.card dt{margin-top:6px}}"""
    intro = f"""<section><h2>Как пользоваться</h2><p>Это подробная версия: {p.full_intro}. На встрече работайте по короткой версии «<a href="{SHORT}" target="{WIN_OBSL}">Вопросы к встрече</a>», сюда — за деталями.</p>
<nav class="toc"><a href="#top5">С чего начать</a> · <a href="#tochki">Конфликтные точки</a> · <a href="#sostoyaniya">Состояния</a> · <a href="#stories">Пользовательские истории</a></nav></section>"""
    full_tochki = re.sub(r'<span class="pt">' + re.escape(p.pfx) + r'?(\d+)</span>',
                         lambda m: f'<a class="pt" href="{KARTA}#p{m.group(1)}" target="{WIN_KARTA}" title="Показать на карте">{lab(m.group(1))}</a>',
                         tochki_body)
    (p.out / FULL).write_text(page(
        f"Евростекло · {p.name}: предпроектное обследование (подробно)", p.full_lead,
        intro + pasport + legend + top5 + full_tochki + sost, card_css, docnav(FULL)), encoding="utf8")

    # ---------- Короткая версия: сценарий встречи ----------
    cards = {}
    for a in re.finditer(r'<article class="card" id="t(\d+)">(.*?)</article>', tochki, re.S):
        n, body = int(a.group(1)), a.group(2)
        dd = dict((txt(k), v) for k, v in re.findall(r"<dt>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>", body, re.S))
        cards[n] = {
            "title": txt(re.search(r"<h3>(.*?)</h3>", body, re.S).group(1)),
            "type": txt(re.search(r'<span class="tp">(.*?)</span>', body, re.S).group(1)),
            "q": txt(dd.get("Главный вопрос", "")),
            "ifs": [txt(li) for li in re.findall(r"<li>(.*?)</li>", dd.get("Уточнить по состояниям", ""), re.S)],
            "gives": txt(dd.get("Что даст ответ", "")),
            "extra": [],
        }
    # Вопросы из пользовательских историй — к первой точке истории, если такого вопроса ещё нет.
    for st in re.findall(r"<h3>История.*?</table>", sost, re.S):
        q = re.search(r"<th>Вопрос клиенту</th><td>(.*?)</td>", st, re.S)
        ptsc = re.search(r"<th>Точки</th><td>(.*?)</td>", st, re.S)
        if not (q and ptsc):
            continue
        qt = txt(q.group(1))
        nums = [int(x) for x in re.findall(r">" + re.escape(p.pfx) + r"?(\d+)<", ptsc.group(1)) if int(x) in cards]
        if nums and all(qt != c["q"] for c in cards.values()):
            cards[nums[0]]["extra"].append(qt)
    order = [int(x) for x in re.findall(r'href="#t(\d+)"', top5)]
    order += [n for n in sorted(cards) if n not in order]

    def row(n, first):
        c = cards[n]
        ifs = "".join(f"<li>{html.escape(i)}</li>" for i in c["ifs"])
        extra = "".join(f'<p class="xq">Ещё: {html.escape(e)}</p>' for e in c["extra"])
        tag = '<span class="first">начать с этого</span>' if first else ""
        return f"""<article class="q" id="t{n}">
<div class="qh"><a class="pt" href="{KARTA}#p{n}" target="{WIN_KARTA}" title="Точка {lab(n)} на карте">{lab(n)}</a><h3>{html.escape(c['title'])}</h3><span class="tp">{html.escape(c['type'])}</span>{tag}</div>
<p class="ask">{html.escape(c['q'])}</p>{extra}
<details><summary>А если… ({len(c['ifs'])})</summary><ul>{ifs}</ul></details>
<div class="ans" data-n="{n}"><span class="lbl">Ответ клиента:</span>
<label><input type="radio" name="a{n}" value="Подтвердил"> подтвердил</label>
<label><input type="radio" name="a{n}" value="Иначе"> иначе</label>
<label><input type="radio" name="a{n}" value="Не знает"> не знает / уточнит</label>
<textarea rows="2" placeholder="Как на самом деле — запишите коротко"></textarea></div>
<p class="more">Ответ закроет: {html.escape(c['gives'])} · <a href="{FULL}#t{n}" target="{WIN_OBSL}">подробно</a></p>
</article>"""

    rows = "\n".join(row(n, i < 5) for i, n in enumerate(order))
    short_css = COMMON_CSS + """.q{border:1px solid var(--line);border-left:6px solid var(--pt);border-radius:8px;padding:12px 16px;margin:12px 0;background:#fff}
.q:target{box-shadow:0 0 0 3px #f2b8a8}
.qh{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.qh h3{font-size:19px}
.qh a.pt{text-decoration:none}
.first{font-size:13px;font-weight:700;color:#fff;background:var(--accent);border-radius:6px;padding:1px 8px}
.ask{font-size:20px;font-weight:700;color:var(--accent);margin:8px 0}
.xq{margin:4px 0;font-weight:600;color:#7a3a14}
details{margin:6px 0}summary{cursor:pointer;color:var(--muted);font-weight:600}
details ul{margin:6px 0;padding-left:22px}
.ans{display:flex;flex-wrap:wrap;gap:6px 16px;align-items:center;background:#f7f4ed;border-radius:8px;padding:8px 10px;margin-top:6px}
.ans .lbl{font-weight:700}.ans textarea{flex:1 1 100%;font:16px system-ui,sans-serif;border:1px solid var(--line);border-radius:6px;padding:6px}
.more{margin:6px 0 0;font-size:14px;color:var(--muted)}.more a{color:var(--accent)}
.bar{display:flex;gap:10px;flex-wrap:wrap}.bar button{font:600 15px system-ui,sans-serif;padding:8px 14px;border-radius:8px;border:1px solid var(--line);background:#fff;cursor:pointer}"""
    how = f"""<section><h2>Как вести встречу</h2><ol>
<li>Второе окно — <a href="{KARTA}" target="{WIN_KARTA}">карта процесса</a>. Красный номер на карте = карточка здесь (номер кликабелен в обе стороны).</li>
<li>Читаете крупный вопрос. Клиент показывает на экране {p.item_last}, а не рассказывает «как обычно».</li>
<li>Отмечаете: подтвердил / иначе / не знает, пишете коротко «как на самом деле». «А если…» — раскрыть, если время есть.</li>
<li>В конце — «Сохранить ответы»: скачается файл с ответами. Ответы хранятся только в этом браузере.</li></ol>
<p class="src">Порядок: первые 5 — рекомендуемое начало, дальше остальные. Все вопросы подробной версии здесь есть; источники и разбор — в «подробно».</p></section>"""
    tail = """<section><h2>Итог встречи</h2><div class="bar"><button type="button" id="save">Сохранить ответы (.md)</button><button type="button" id="clear">Очистить ответы</button></div></section>
<script>(function(){var K='evro-{SLUG}-answers';var d={};try{d=JSON.parse(localStorage.getItem(K)||'{}')}catch(e){}
function put(){try{localStorage.setItem(K,JSON.stringify(d))}catch(e){}}
document.querySelectorAll('.ans').forEach(function(b){var n=b.dataset.n,s=d[n]||{};
 b.querySelectorAll('input').forEach(function(i){if(i.value===s.v)i.checked=true;i.addEventListener('change',function(){s.v=i.value;d[n]=s;put()})});
 var t=b.querySelector('textarea');t.value=s.t||'';t.addEventListener('input',function(){s.t=t.value;d[n]=s;put()});});
document.getElementById('save').onclick=function(){var o=['# {NAME} — ответы клиента','',new Date().toLocaleString('ru-RU'),''];
 document.querySelectorAll('article.q').forEach(function(a){var n=a.id.slice(1),s=d[n]||{};
 o.push('## {PFX}'+n+'. '+a.querySelector('h3').textContent,'Вопрос: '+a.querySelector('.ask').textContent,'Ответ: '+(s.v||'—'),'Как на самом деле: '+(s.t||'—'),'')});
 var u=URL.createObjectURL(new Blob([o.join('\\n')],{type:'text/markdown'}));var l=document.createElement('a');l.href=u;l.download='evrosteklo-{SLUG}-otvety.md';l.click();};
document.getElementById('clear').onclick=function(){if(confirm('Очистить все ответы?')){d={};put();location.reload()}};})();</script>"""
    tail = tail.replace("{SLUG}", p.slug).replace("{NAME}", p.name).replace("{PFX}", p.pfx)
    (p.out / SHORT).write_text(page(
        f"Евростекло · {p.name}: вопросы к встрече",
        f"{len(cards)} {p.short_lead}",
        how + (f'<section><details><summary><b>Паспорт: кто есть кто</b> (раскрыть)</summary>{pasport}</details></section>' if pasport else '')
        + f'<section><h2>Вопросы</h2>{rows}</section>' + tail, short_css, docnav(SHORT)), encoding="utf8")
    print(p.slug, "ok:", len(cards), "точек, порядок", order)
    return {"cards": cards, "files": p.files}
