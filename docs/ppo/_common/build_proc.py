#!/usr/bin/env python3
"""Общая сборка процесса ППО (лиды, сделки, …) из фрагментов _parts — механическое сведение.

Для процесса собираются три связанных HTML:
  karta-<slug>.html                  — карта процесса (BPMN), точки ведут в вопросы
  obsledovanie-<slug>.html           — сценарий встречи: ключевые вопросы, отметка ответа
  obsledovanie-<slug>-podrobno.html  — полная версия (источники, состояния, истории)

Фрагменты в <процесс>/_parts: karta.svg.html, tochki.html, sostoyaniya.html, pasport.html (необязателен).
Точки внутри — числа (title «Точка N:», id tN/pN); видимая метка — префикс + число (у сделок «С1»).

Разметка пункта «А если…» (контракт e2, specs/006-ispravlenie-kart/kritika/e2-c2-3-dizajner.md §1):
  <li data-id="e2" data-src="ТЗ">А если …? <small class="src">ТЗ ФТ-1 Л13</small></li>
  <li data-id="e1" data-see="sdelki:23:e1">А если …?</li>   — вопрос задаётся в другой точке
Пункт без атрибутов (переходное) получает неявный id e<позиция>. Разбор — ifs_of(); check_ppo.py его импортирует.
Повестка: <section id="povestka"> в tochki.html заменяет section#top5 (строки <li data-p="1 2">, <li class="cut">).
"""
import html
import re
from dataclasses import dataclass, field
from pathlib import Path

COMMON = Path(__file__).parent
CSS = (COMMON / "base.css").read_text(encoding="utf8")
ZOOM = (COMMON / "zoom.html").read_text(encoding="utf8")
LANES = (COMMON / "lanes.html").read_text(encoding="utf8") if (COMMON / "lanes.html").exists() else ""  # роли слева закреплены (Т5)
# Имена окон: ссылки открывают документ во втором окне и переиспользуют его.
WIN_KARTA, WIN_OBSL = "evro-karta", "evro-obsl"
WIN_SEE = "evro-see"  # ссылка «этот вопрос задаём в …» на другой процесс — третье окно, встреча не теряется
SRC_OK = ("доска", "ТЗ", "СМ", "журнал", "наш")  # допустимые data-src; «портал» запрещён (аудит интегратора)
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
    legend_said: str = "запись экрана и речь интегратора"  # что значит метка «со слов» в этом процессе
    name_in: str = ""         # «в «Лидах»» — имя процесса в предложном падеже для ссылок из другого процесса

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


LI_RX = re.compile(r"<li\b([^>]*)>(.*?)</li>", re.S)
ATTR_RX = re.compile(r'([a-z][a-z-]*)="([^"]*)"')
CARD_RX = re.compile(r'<article class="card" id="t(\d+)">(.*?)</article>', re.S)


def attrs_of(s):
    return dict(ATTR_RX.findall(s))


def dd_of(body, name):
    """Содержимое <dd> (с атрибутами или без) сразу за <dt>name</dt>."""
    m = re.search(r"<dt>\s*" + re.escape(name) + r"\s*</dt>\s*<dd\b[^>]*>(.*?)</dd>", body, re.S)
    return m.group(1) if m else ""


def ifs_of(dd):
    """Пункты «А если…» из <dd>: <li> с data-id/data-src/data-see и без них (неявный id e<позиция>)."""
    out = []
    for pos, (at, body) in enumerate(LI_RX.findall(dd), 1):
        a = attrs_of(at)
        out.append({"id": a.get("data-id") or f"e{pos}", "id_set": "data-id" in a, "pos": pos,
                    "src": a.get("data-src"), "see": a.get("data-see"), "text": txt(body), "html": body})
    return out


def cards_of(tochki):
    """{N: тело карточки} из tochki.html."""
    return {int(n): body for n, body in CARD_RX.findall(tochki)}


def parse_see(see):
    """«sdelki:23:e1» → ("sdelki", 23, "e1"); «sdelki:1» (строка повестки) → ("sdelki", 1, None); иначе None."""
    m = re.fullmatch(r"\s*([a-z]+):(\d+)(?::(e\d+))?\s*", see or "")
    return (m.group(1), int(m.group(2)), m.group(3)) if m else None


def povestka_of(tochki):
    m = re.search(r'<section id="povestka">.*?</section>', tochki, re.S)
    return m.group(0) if m else ""


def pov_lines(sec):
    """Строки повестки: [(attrs, html, [N…])]; N — из data-p, иначе из href="#tN"; строка отреза — class="cut"."""
    out = []
    for at, body in LI_RX.findall(sec):
        a = attrs_of(at)
        ns = [int(x) for x in a["data-p"].split()] if a.get("data-p") else [int(x) for x in re.findall(r'href="#t(\d+)"', body)]
        out.append((a, body, ns))
    return out


def see_of(see, p, allp):
    """Куда ведёт data-see: метка, «где» для текста, ссылки на короткую и подробную версии (или None)."""
    t = parse_see(see)
    if not t or t[0] not in allp:
        return None
    q = allp[t[0]]
    lab, n = f"{q.pfx}{t[1]}", t[1]
    if q.slug == p.slug:
        return {"lab": lab, "where": f"в точке {lab}", "short": f"#t{n}", "full": f"#t{n}", "other": False}
    return {"lab": lab, "where": f"в {q.name_in or '«' + q.name + '»'} — {lab}", "other": True,
            "short": f"../{q.slug}/obsledovanie-{q.slug}.html#t{n}", "full": f"../{q.slug}/obsledovanie-{q.slug}-podrobno.html#t{n}"}


def build(p: Proc, allp=None):
    allp = allp or {p.slug: p}
    KARTA, SHORT, FULL = p.files
    lab = lambda n: f"{p.pfx}{n}"

    def docnav(current):
        items = [(KARTA, "Карта процесса", WIN_KARTA), (SHORT, "Вопросы к встрече", WIN_OBSL),
                 (FULL, "Подробная версия", WIN_OBSL)]
        links = [f'<b>{t}</b>' if f == current else f'<a href="{f}" target="{w}">{t}</a>' for f, t, w in items]
        return f'<nav class="docnav"><a href="../index.html">☰ Оглавление</a> · {p.name}: ' + " · ".join(links) + "</nav>"

    legend = f"""<section><h2>Как читать</h2><div class="legend">
<span><span class="st st-board">на доске</span> есть на доске Miro</span>
<span><span class="st st-doc">документ клиента</span> ТЗ и статусная модель 2024–2025 (UNVERIFIED)</span>
<span><span class="st st-own">решение владельца</span> журнал решений владельца</span>
<span><span class="st st-said">со слов</span> {p.legend_said}</span>
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
.ptnav{position:static;background:var(--paper);border:1px solid var(--line);border-radius:8px;padding:6px 10px;margin-bottom:10px;display:flex;flex-wrap:wrap;gap:4px 14px;align-items:center;box-shadow:0 2px 8px rgba(0,0,0,.08);font-size:15px}
.ptnav-h{font-weight:700;font-size:15px}.ptg{display:inline-flex;gap:4px;align-items:center;flex-wrap:wrap}.ptg b{font-size:14px;font-weight:700;color:var(--muted);margin-right:2px}
.ptg button{min-width:28px;height:26px;padding:0 7px;border-radius:13px;border:0;background:var(--pt);color:#fff;font-weight:700;font-size:13px;line-height:26px;font-family:inherit;cursor:pointer}
.ptg button.on{outline:3px solid #1d2530}
.ptsel{flex:1 1 100%;font-size:14px;color:var(--ink)}.ptsel a{color:var(--accent);font-weight:700}
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
        + legend + f'<section><h2>Карта «{p.name}»</h2><p class="src">Карту можно тянуть мышью; масштаб схемы — кнопки справа внизу, клавиши + и − или Ctrl + колесо над схемой (меняется только схема).</p>'
        + navbar + f'<div class="mapwrap">{svg}</div></section>' + pan + LANES,
        map_css, docnav(KARTA)), encoding="utf8")

    # ---------- Подробная версия ----------
    tochki = (p.parts / "tochki.html").read_text(encoding="utf8")
    sost = (p.parts / "sostoyaniya.html").read_text(encoding="utf8")
    m = re.search(r'<section id="top5">.*?</section>', tochki, re.S)
    top5 = m.group(0) if m else ""
    pov = povestka_of(tochki)  # повестка встречи заменяет top5 (порядок карточек и блок вверху короткой версии)
    tochki_body = tochki.replace(top5, "").replace(pov, "") if pov else tochki.replace(top5, "")

    def see_link(see, kind):
        s_ = see_of(see, p, allp)
        if not s_:
            return f'<span class="see-bad">ссылка «{html.escape(see)}» не найдена</span>'
        tgt = f' target="{WIN_SEE}"' if s_["other"] else ""
        return f'этот вопрос задаём <a href="{s_[kind]}"{tgt}>{html.escape(s_["where"])}</a>'

    def pov_render(sec, kind):
        """Строки повестки: номера точек — ссылки на карточки этой страницы, data-see — ссылка на другой процесс."""
        def li(m):
            a = attrs_of(m.group(1))
            ns = [int(x) for x in a["data-p"].split()] if a.get("data-p") else []
            pts = "".join(f'<a class="pt" data-p="{n}" href="#t{n}">{lab(n)}</a> ' for n in ns)
            see = f' <small class="see">↪ {see_link(a["data-see"], kind)}</small>' if a.get("data-see") else ""
            return f"<li{m.group(1)}>{pts}{m.group(2)}{see}</li>"
        return LI_RX.sub(li, sec)

    def full_li(m):
        """Подробная версия: у пункта-ссылки — «↪ задаём в …», у data-src="наш" без адреса — «наш вопрос»."""
        a = attrs_of(m.group(1))
        if a.get("data-see"):
            return f'<li{m.group(1)}>{m.group(2)} <small class="see">↪ {see_link(a["data-see"], "full")}</small></li>'
        if a.get("data-src") == "наш" and 'class="src"' not in m.group(2):
            return f'<li{m.group(1)}>{m.group(2)} <small class="src">наш вопрос (проверка полноты)</small></li>'
        return m.group(0)
    card_css = COMMON_CSS + """.card{border:1px solid var(--line);border-left:6px solid var(--pt);border-radius:8px;padding:14px 18px;margin:16px 0;background:#fff}
.card header{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
.card dl{display:grid;grid-template-columns:220px 1fr;gap:6px 16px;margin:0}
.card dt{font-weight:700;color:var(--muted)}.card dd{margin:0}
.card dd.q{font-weight:700;color:var(--accent);font-size:18px}
.card ul{margin:0;padding-left:20px}
@media (max-width:700px){.card dl{grid-template-columns:1fr}.card dt{margin-top:6px}}"""
    toc0 = '<a href="#povestka">Повестка</a>' if pov else '<a href="#top5">С чего начать</a>'
    intro = f"""<section><h2>Как пользоваться</h2><p>Это подробная версия: {p.full_intro}. На встрече работайте по короткой версии «<a href="{SHORT}" target="{WIN_OBSL}">Вопросы к встрече</a>», сюда — за деталями.</p>
<nav class="toc">{toc0} · <a href="#tochki">Конфликтные точки</a> · <a href="#sostoyaniya">Состояния</a> · <a href="#stories">Пользовательские истории</a></nav></section>"""
    full_tochki = re.sub(r'<span class="pt">' + re.escape(p.pfx) + r'?(\d+)</span>',
                         lambda m: f'<a class="pt" href="{KARTA}#p{m.group(1)}" target="{WIN_KARTA}" title="Показать на карте">{lab(m.group(1))}</a>',
                         tochki_body)
    full_tochki = re.sub(r'<dt>Уточнить по состояниям</dt>\s*<dd\b[^>]*>.*?</dd>',
                         lambda m: LI_RX.sub(full_li, m.group(0)), full_tochki, flags=re.S)
    (p.out / FULL).write_text(page(
        f"Евростекло · {p.name}: предпроектное обследование (подробно)", p.full_lead,
        intro + pasport + legend + (pov_render(pov, "full") if pov else top5) + full_tochki + sost, card_css, docnav(FULL)), encoding="utf8")

    # ---------- Короткая версия: сценарий встречи ----------
    cards = {}
    for n, body in cards_of(tochki).items():
        dd = dict((txt(k), v) for k, v in re.findall(r"<dt>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>", body, re.S))
        cards[n] = {
            "title": txt(re.search(r"<h3>(.*?)</h3>", body, re.S).group(1)),
            "type": txt(re.search(r'<span class="tp">(.*?)</span>', body, re.S).group(1)),
            "q": txt(dd.get("Главный вопрос", "")),
            "ifs": ifs_of(dd.get("Уточнить по состояниям", "")),
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
    # Порядок: повестка (строки по порядку, без повторов), иначе top5; дальше остальные по номеру.
    povn = {}  # N → номер строки повестки
    if pov:
        k = 0
        for a_, _, ns in pov_lines(pov):
            if "cut" in a_.get("class", "").split() or not ns:
                continue
            k += 1
            for n in ns:
                if n in cards:
                    povn.setdefault(n, k)
        order = list(povn)
    else:
        order = [int(x) for x in re.findall(r'href="#t(\d+)"', top5)]
    order += [n for n in sorted(cards) if n not in order]

    def row(n, first):
        c = cards[n]
        # «А если…»: флажок только у своих пунктов (ключ — data-id); пункт с data-see — строка-ссылка без флажка.
        own = [x for x in c["ifs"] if not x["see"]]
        ifs = "".join(f'<label><input type="checkbox" data-if="{html.escape(x["id"])}"> {html.escape(x["text"])}</label>' for x in own)
        sees = "".join(f'<p class="see">↪ {html.escape(x["text"])} — {see_link(x["see"], "short")}</p>' for x in c["ifs"] if x["see"])
        summ = f"А если… ({len(own)})" if own else f"А если… — задаём в других точках ({len(c['ifs'])})"
        ifblock = (f'<details class="ifs"{" open" if len(own) <= 4 else ""}><summary>{summ}</summary>'
                   f'<div class="ifl">{ifs}{sees}'
                   + ('<input type="text" class="ifc" placeholder="комментарий к отмеченному">' if own else "")
                   + '</div></details>' if c["ifs"] else "")
        extra = "".join(f'<p class="xq"><label><input type="checkbox" data-ex="{j}"> спросили</label> <span>Ещё: {html.escape(e)}</span></p>'
                        for j, e in enumerate(c["extra"], 1))
        if pov:
            tag = f'<span class="first">повестка · {povn[n]}</span>' if n in povn else ""
        else:
            tag = '<span class="first">начать с этого</span>' if first else ""
        return f"""<article class="q" id="t{n}">
<div class="qh"><a class="pt" href="{KARTA}#p{n}" target="{WIN_KARTA}" title="Точка {lab(n)} на карте">{lab(n)}</a><h3>{html.escape(c['title'])}</h3><span class="tp">{html.escape(c['type'])}</span>{tag}</div>
<p class="ask">{html.escape(c['q'])}</p>{extra}
{ifblock}
<div class="ans" data-n="{n}"><span class="lbl">Статус точки:</span>
<label><input type="radio" name="a{n}" value="Подтвердил"> подтвердил</label>
<label><input type="radio" name="a{n}" value="Иначе"> иначе</label>
<label><input type="radio" name="a{n}" value="Не знает"> не знает</label>
<label><input type="radio" name="a{n}" value="Знает другой"> знает другой человек</label>
<input type="text" class="who" placeholder="кто знает (роль или имя)" hidden>
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
.ifl{display:flex;flex-direction:column;gap:4px;margin:6px 0 0 4px}.ifl label{display:flex;gap:8px;align-items:flex-start;cursor:pointer}
.ifl input[type=checkbox],.xq input{width:18px;height:18px;flex:0 0 auto;margin-top:3px}
.ifl .ifc,.ans .who{font:15px system-ui,sans-serif;border:1px solid var(--line);border-radius:6px;padding:4px 6px;max-width:420px}
.xq label{font-weight:600;color:var(--muted);margin-right:4px;cursor:pointer}
.meet{display:flex;gap:10px;align-items:center;flex-wrap:wrap;font-weight:700}.meet input{font:16px system-ui,sans-serif;padding:4px 8px;border:1px solid var(--line);border-radius:6px}
.ans{display:flex;flex-wrap:wrap;gap:6px 16px;align-items:center;background:#f7f4ed;border-radius:8px;padding:8px 10px;margin-top:6px}
.ans .lbl{font-weight:700}.ans textarea{flex:1 1 100%;font:16px system-ui,sans-serif;border:1px solid var(--line);border-radius:6px;padding:6px}
.more{margin:6px 0 0;font-size:14px;color:var(--muted)}.more a{color:var(--accent)}
.bar{display:flex;gap:10px;flex-wrap:wrap}.bar button,#povblk button{font:600 15px system-ui,sans-serif;padding:8px 14px;border-radius:8px;border:1px solid var(--line);background:#fff;cursor:pointer}
.ifl p.see{margin:2px 0 0;color:var(--muted);font-size:15px}.ifl p.see a{color:var(--accent);font-weight:600}
#povblk ol{margin:6px 0 10px;padding-left:24px}#povblk li{margin:4px 0}#povblk a{color:var(--accent)}#povblk a.pt{color:#fff;text-decoration:none;min-width:26px;height:26px;font-size:13px}
#povblk li.cut{list-style:none;margin:10px 0 10px -24px;border-top:2px dashed var(--muted);padding-top:4px;color:var(--muted);font-size:14px}
#povblk button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
body.onlypov article.q.nopov{display:none}"""
    order_note = ("Порядок: сначала точки повестки (блок вверху), дальше остальные; «Только повестка» скрывает остальные карточки."
                  if pov else "Порядок: первые 5 — рекомендуемое начало, дальше остальные.")
    how = f"""<section><h2>Как вести встречу</h2><ol>
<li>Второе окно — <a href="{KARTA}" target="{WIN_KARTA}">карта процесса</a>. Красный номер на карте = карточка здесь (номер кликабелен в обе стороны). Вверху поставьте дату встречи.</li>
<li>Читаете крупный вопрос. Клиент показывает на экране {p.item_last}, а не рассказывает «как обычно».</li>
<li>Статус точки: подтвердил / иначе / не знает / знает другой человек (впишите, кто). «Как на самом деле» — коротко.</li>
<li>«А если…» и «Ещё:» — галочка у того, что обсудили; уточнение — в поле «комментарий».</li>
<li>В конце — «Сохранить ответы»: скачается .md с датой, статусами, отмеченными и не обсуждёнными пунктами. Ответы хранятся только в этом браузере; это черновик, источник — транскрипт видео.</li></ol>
<p class="src">{order_note} Все вопросы подробной версии здесь есть; источники и разбор — в «подробно».</p></section>"""
    meet = '<section><label class="meet">Дата встречи: <input type="date" id="meet"></label></section>'
    povblk = povjs = ""
    if pov:
        inner = re.sub(r'^<section id="povestka">|</section>$', "", pov_render(pov, "short").strip())
        povblk = (f'<section id="povblk">{inner}<div class="bar"><button type="button" id="onlypov" aria-pressed="false">Только повестка</button></div></section>')
        povjs = ("""<script>(function(){var K='evro-{SLUG}-onlypov',b=document.getElementById('onlypov'),ns={};
document.querySelectorAll('#povblk a[data-p],#povblk a[href^="#t"]').forEach(function(a){if(a.closest('.see'))return;var n=a.getAttribute('data-p')||a.getAttribute('href').slice(2);ns[n]=1});
document.querySelectorAll('article.q').forEach(function(a){if(!ns[a.id.slice(1)])a.classList.add('nopov')});
function set(on){document.body.classList.toggle('onlypov',on);b.classList.toggle('on',on);b.setAttribute('aria-pressed',on?'true':'false');
 b.textContent=on?'Показать все вопросы':'Только повестка';try{on?localStorage.setItem(K,'1'):localStorage.removeItem(K)}catch(e){}}
var on=false;try{on=localStorage.getItem(K)==='1'}catch(e){}set(on);
b.addEventListener('click',function(){set(!document.body.classList.contains('onlypov'))});})();</script>""".replace("{SLUG}", p.slug))
    tail = """<section><h2>Итог встречи</h2><div class="bar"><button type="button" id="save">Сохранить ответы (.md)</button><button type="button" id="clear">Очистить ответы</button></div></section>
<script>(function(){var K='evro-{SLUG}-answers.v3',K2='evro-{SLUG}-answers.v2',K1='evro-{SLUG}-answers';
function get(k){try{return localStorage.getItem(k)}catch(e){return null}}
function jp(k){try{return JSON.parse(get(k)||'null')}catch(e){return null}}
function put(){try{localStorage.setItem(K,JSON.stringify(d))}catch(e){}}
function blank(){return {v:3,meeting:'',items:{}}}
var d=jp(K);
if(!d||typeof d!=='object'||d.v!==3){d=blank();var o2=jp(K2),o=jp(K1);
 /* v2 и старый ключ только читаются и не стираются; v2: ifs["N"] (позиция) → ifs["eN"] (data-id) */
 if(o2&&typeof o2==='object'&&o2.items&&typeof o2.items==='object'){d.meeting=o2.meeting||'';
  Object.keys(o2.items).forEach(function(n){var r=o2.items[n];if(!r||typeof r!=='object')return;var x={};
   Object.keys(r).forEach(function(k){x[k]=r[k]});
   if(r.ifs&&typeof r.ifs==='object'){x.ifs={};Object.keys(r.ifs).forEach(function(k){if(r.ifs[k])x.ifs[/^\\d+$/.test(k)?'e'+k:k]=true})}
   d.items[n]=x});put()}
 /* перенос старого формата {N:{v,t}} */
 else if(o&&typeof o==='object'){var any=false;Object.keys(o).forEach(function(n){var r=o[n];if(r&&(r.v||r.t)){d.items[n]={s:r.v||'',t:r.t||''};any=true}});if(any)put()}}
if(!d.items||typeof d.items!=='object')d.items={};
function it(n){return d.items[n]||(d.items[n]={})}
function rd(n){return d.items[n]||{}}
var mt=document.getElementById('meet');mt.value=d.meeting||'';mt.addEventListener('change',function(){d.meeting=mt.value;put()});
document.querySelectorAll('article.q').forEach(function(a){var n=a.id.slice(1),s=rd(n),b=a.querySelector('.ans'),w=b.querySelector('.who');
 function sw(){w.hidden=(rd(n).s!=='Знает другой')}
 b.querySelectorAll('input[type=radio]').forEach(function(i){if(i.value===s.s)i.checked=true;i.addEventListener('change',function(){it(n).s=i.value;sw();put()})});
 w.value=s.who||'';sw();w.addEventListener('input',function(){it(n).who=w.value;put()});
 var t=b.querySelector('textarea');t.value=s.t||'';t.addEventListener('input',function(){it(n).t=t.value;put()});
 [['if','ifs'],['ex','ex']].forEach(function(p){a.querySelectorAll('input[data-'+p[0]+']').forEach(function(c){var k=c.getAttribute('data-'+p[0]);
  c.checked=!!(s[p[1]]&&s[p[1]][k]);c.addEventListener('change',function(){var x=it(n),m=x[p[1]]||(x[p[1]]={});if(c.checked)m[k]=true;else delete m[k];put()})})});
 var f=a.querySelector('.ifc');if(f){f.value=s.ifc||'';f.addEventListener('input',function(){it(n).ifc=f.value;put()})}});
function lt(c){return c.closest('label').textContent.trim()}
document.getElementById('save').onclick=function(){var o=['# {NAME} — ответы клиента','','Дата встречи: '+(d.meeting||'—'),'Выгружено: '+new Date().toLocaleString('ru-RU'),''],seen={};
 document.querySelectorAll('article.q').forEach(function(a){var n=a.id.slice(1),s=rd(n),yes=[],no=[];seen[n]=1;
 o.push('## {PFX}'+n+'. '+a.querySelector('h3').textContent,'Вопрос: '+a.querySelector('.ask').textContent,'Статус: '+(s.s||'—'));
 if(s.s==='Знает другой'||s.who)o.push('Кто знает: '+(s.who||'—'));
 o.push('Как на самом деле: '+(s.t||'—'));
 var here={};a.querySelectorAll('input[data-if]').forEach(function(c){var k=c.getAttribute('data-if');here[k]=1;(s.ifs&&s.ifs[k]?yes:no).push('- '+lt(c))});
 var gone=Object.keys(s.ifs||{}).filter(function(k){return s.ifs[k]&&!here[k]});
 if(yes.length||no.length||gone.length){o.push('','А если… — обсудили:');o.push.apply(o,yes.length?yes:['- —']);if(s.ifc)o.push('Комментарий: '+s.ifc);
  if(no.length){o.push('','Не обсуждали:');o.push.apply(o,no)}
  gone.forEach(function(k){o.push('- Отмечено раньше, пункт снят: '+k)})}
 var sees=a.querySelectorAll('.ifl p.see');if(sees.length){o.push('','Задаём в другой точке:');sees.forEach(function(x){o.push('- '+x.textContent.replace(/^↪\\s*/,''))})}
 var ex=a.querySelectorAll('input[data-ex]');if(ex.length){o.push('','Ещё:');ex.forEach(function(c){var q=c.closest('.xq').querySelector('span').textContent.replace(/^Ещё:\\s*/,'');
  o.push('- '+(s.ex&&s.ex[c.getAttribute('data-ex')]?'[спросили] ':'[не спросили] ')+q)})}
 o.push('')});
 Object.keys(d.items).forEach(function(n){if(seen[n])return;var s=d.items[n]||{};if(!(s.s||s.t||s.who))return;
  o.push('## {PFX}'+n+' (карточки на странице нет)','Статус: '+(s.s||'—'),'Кто знает: '+(s.who||'—'),'Как на самом деле: '+(s.t||'—'),'')});
 o.push('Ответы — рабочий черновик; источник для разблокировки точки — транскрипт видео');
 var u=URL.createObjectURL(new Blob([o.join('\\n')],{type:'text/markdown'}));var l=document.createElement('a');l.href=u;l.download='evrosteklo-{SLUG}-otvety.md';l.click();};
document.getElementById('clear').onclick=function(){if(confirm('Очистить все ответы?')){d=blank();put();location.reload()}};})();</script>"""
    tail = tail.replace("{SLUG}", p.slug).replace("{NAME}", p.name).replace("{PFX}", p.pfx)
    (p.out / SHORT).write_text(page(
        f"Евростекло · {p.name}: вопросы к встрече",
        f"{len(cards)} {p.short_lead}",
        meet + povblk + how + (f'<section><details><summary><b>Паспорт: кто есть кто</b> (раскрыть)</summary>{pasport}</details></section>' if pasport else '')
        + f'<section><h2>Вопросы</h2>{rows}</section>' + tail + povjs, short_css, docnav(SHORT)), encoding="utf8")
    print(p.slug, "ok:", len(cards), "точек, порядок", order)
    return {"cards": cards, "files": p.files}
