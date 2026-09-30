#!/usr/bin/env python3
"""Проверки ППО K1–K10 (только чтение рабочего дерева; сборка — во временной копии).

Запуск: python3 docs/ppo/check_ppo.py [--base=SHA] [--lidy]
  --base=SHA  база для K2 (номера точек) и K9 (шлюз лидов); по умолчанию — последний полный SHA
              в таблице docs/CHECKPOINTS.md (нет файла/строки — 575a157 с предупреждением)
  --lidy      разрешить изменение собранных страниц лидов (только с «да» владельца на лиды)
K3 и K10 разбирают пункты «А если…» той же функцией, что и сборка (build_proc.ifs_of): <li> с атрибутами не теряются.
Код выхода: 0 — ошибок нет, 1 — есть. Предупреждения (слой А в K5, похожие пункты в K10, недоступная база) код не меняют.
Основа — прототип SRE (specs/006-ispravlenie-kart/kritika/c2-6-sre.md), регэксп ПДн — свой (c2-5, п.36).
"""
import difflib
import hashlib
import html
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

PPO = Path(__file__).resolve().parent
ROOT = PPO.parent.parent
sys.path.insert(0, str(PPO / "_common"))
from build_proc import SRC_OK, cards_of, dd_of, ifs_of, parse_see, pov_lines, povestka_of, txt  # noqa: E402

ARGS = sys.argv[1:]
PROCS = ("lidy", "sdelki")
KS = [f"K{i}" for i in range(1, 11)]
ERR, WARN = {k: [] for k in KS}, {k: [] for k in KS}
INFO = {}
FALLBACK = "575a157909476c9e55724ac1a28b78a4fb356321"


def default_base():
    """Последний полный SHA из таблицы docs/CHECKPOINTS.md; нет — FALLBACK."""
    f = ROOT / "docs" / "CHECKPOINTS.md"
    shas = re.findall(r"\|\s*`([0-9a-f]{40})`", f.read_text(encoding="utf8")) if f.exists() else []
    return (shas[-1], None) if shas else (FALLBACK, "в docs/CHECKPOINTS.md нет полного SHA — база 575a157")


BASE, BASE_NOTE = next(((a.split("=", 1)[1], None) for a in ARGS if a.startswith("--base=")), None) or default_base()


def err(k, m): ERR[k].append(m)
def warn(k, m): WARN[k].append(m)
def rd(p): return p.read_text(encoding="utf8")
def nums(rx, s): return {int(x) for x in re.findall(rx, s)}


def git_show(path):
    r = subprocess.run(["git", "-C", str(ROOT), "show", f"{BASE}:{path}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


CARD = r'<article class="card" id="t(\d+)">'

# K1 связность: точки svg = карточки _parts = pN карты = data-p навигатора = tN короткой = tN подробной
# K2 номера не пропадают относительно базы; K3 источник у варианта «А если…» (предупреждение)
for slug in PROCS:
    parts, out = PPO / slug / "_parts", PPO / slug
    try:
        k = rd(out / f"karta-{slug}.html")
        sets = {
            "svg": nums(r'<g class="pt"><title>Точка (\d+):', rd(parts / "karta.svg.html")),
            "карточки": nums(CARD, rd(parts / "tochki.html")),
            "карта pN": nums(r'id="p(\d+)"', k),
            "навигатор": nums(r'data-p="(\d+)"', k),
            "короткая": nums(r'<article class="q" id="t(\d+)">', rd(out / f"obsledovanie-{slug}.html")),
            "подробная": nums(CARD, rd(out / f"obsledovanie-{slug}-podrobno.html")),
        }
    except FileNotFoundError as e:
        err("K1", f"{slug}: нет файла {Path(e.filename).name}")
        continue
    ref = sets["svg"]
    if len({frozenset(s) for s in sets.values()}) != 1:
        err("K1", f"{slug}: расхождение с svg — " + ", ".join(f"{n} {sorted(s ^ ref)}" for n, s in sets.items() if s != ref))
    else:
        INFO.setdefault("K1", []).append(f"{slug} {len(ref)} точек")

    old = git_show(f"docs/ppo/{slug}/_parts/tochki.html")
    if old is None:
        warn("K2", f"{slug}: база {BASE[:7]} недоступна — не подтверждено")
    else:
        oldset = nums(CARD, old.decode("utf8"))
        if not oldset <= sets["карточки"]:
            err("K2", f"{slug}: пропали номера {sorted(oldset - sets['карточки'])}")

    # K3 (ошибка): у каждого своего пункта (без data-see) data-src из SRC_OK; кроме «наш» — есть <small class="src">
    tot, probs = 0, {}
    for n, body in sorted(cards_of(rd(parts / "tochki.html")).items()):
        for x in ifs_of(dd_of(body, "Уточнить по состояниям")):
            tot += 1
            if x["see"]:
                continue
            if x["src"] is None:
                why = "нет data-src"
            elif x["src"] == "портал":
                why = "data-src=\"портал\" запрещён (в аудит интегратора)"
            elif x["src"] not in SRC_OK:
                why = f"data-src=\"{x['src']}\" не из {{{', '.join(SRC_OK)}}}"
            elif x["src"] != "наш" and 'class="src"' not in x["html"]:
                why = f"data-src=\"{x['src']}\" без <small class=\"src\">"
            else:
                continue
            probs.setdefault(why, []).append(f"т{n}:{x['id']}")
    for why, where in probs.items():
        err("K3", f"{slug}: {why} — {len(where)} из {tot}: " + ", ".join(where[:12]) + (" …" if len(where) > 12 else ""))
    if not probs:
        INFO.setdefault("K3", []).append(f"{slug} {tot} пунктов")

# K10 владение вопроса: (а) цель data-see существует, сама не ссылка и не своя карточка; (б) data-id вида eN,
# уникален в карточке; (в) нет точных дублей текста среди своих пунктов обоих процессов; (г) точки повестки существуют;
# (д) похожие свои пункты (difflib ≥ 0,80) без ссылки — предупреждение
ITEMS, CARDS = {}, {}
for slug in PROCS:
    f = PPO / slug / "_parts" / "tochki.html"
    if not f.exists():
        continue
    CARDS[slug] = cards_of(rd(f))
    for n, body in CARDS[slug].items():
        ITEMS[(slug, n)] = ifs_of(dd_of(body, "Уточнить по состояниям"))
for (slug, n), items in sorted(ITEMS.items()):
    ids = [x["id"] for x in items]
    for i in sorted({i for i in ids if ids.count(i) > 1}):
        err("K10", f"{slug} т{n}: data-id «{i}» повторяется в карточке")
    for x in items:
        if not re.fullmatch(r"e\d+", x["id"]):
            err("K10", f"{slug} т{n}: data-id «{x['id']}» не вида eN")
        if not x["see"]:
            continue
        t = parse_see(x["see"])
        if not t or not t[2]:
            err("K10", f"{slug} т{n} {x['id']}: data-see «{x['see']}» не вида slug:N:eK")
            continue
        if (t[0], t[1]) == (slug, n):
            err("K10", f"{slug} т{n} {x['id']}: data-see ведёт в свою же карточку")
            continue
        tgt = next((y for y in ITEMS.get((t[0], t[1]), []) if y["id"] == t[2]), None)
        if tgt is None:
            err("K10", f"{slug} т{n} {x['id']}: цель data-see «{x['see']}» не найдена")
        elif tgt["see"]:
            err("K10", f"{slug} т{n} {x['id']}: цель «{x['see']}» сама ссылка (цепочки запрещены)")
        if x["src"]:
            warn("K10", f"{slug} т{n} {x['id']}: у пункта-ссылки лишний data-src")


def norm(s):
    s = re.sub(r"[^\w\s]", " ", s.lower().replace("ё", "е"))
    return re.sub(r"\s+", " ", re.sub(r"^\s*а если\s+", "", s)).strip()


own = [(slug, n, x["id"], norm(x["text"])) for (slug, n), items in sorted(ITEMS.items()) for x in items if not x["see"]]
seen = {}
for slug, n, i, t in own:
    if t in seen:
        err("K10", f"точный дубль без ссылки: {seen[t]} = {slug} т{n} {i} «{t[:60]}»")
    else:
        seen[t] = f"{slug} т{n} {i}"
sim = 0
for a in range(len(own)):
    for b in range(a + 1, len(own)):
        if own[a][3] != own[b][3] and difflib.SequenceMatcher(None, own[a][3], own[b][3]).ratio() >= 0.80:
            sim += 1
            if sim <= 15:
                warn("K10", f"похожи (≥0,80), проверить ссылку: {own[a][0]} т{own[a][1]} {own[a][2]} ↔ {own[b][0]} т{own[b][1]} {own[b][2]}")
if sim > 15:
    warn("K10", f"… и ещё {sim - 15} похожих пар")
for slug in CARDS:
    pov = povestka_of(rd(PPO / slug / "_parts" / "tochki.html"))
    for a, body, ns in pov_lines(pov):
        for n in ns:
            if n not in CARDS[slug]:
                err("K10", f"{slug} повестка: точки {n} нет среди карточек")
        t = parse_see(a.get("data-see"))
        if a.get("data-see") and not (t and t[1] in CARDS.get(t[0], {})):
            err("K10", f"{slug} повестка: data-see «{a['data-see']}» — нет такой точки")
        if not ns and "cut" not in a.get("class", "").split():
            warn("K10", f"{slug} повестка: строка без номера точки «{txt(body)[:50]}»")
    if pov:
        INFO.setdefault("K10", []).append(f"{slug}: повестка {sum(1 for _, _, ns in pov_lines(pov) if ns)} строк")
INFO.setdefault("K10", []).append(f"своих пунктов {len(own)}, ссылок {sum(1 for v in ITEMS.values() for x in v if x['see'])}")

# K4 нет ссылок на портальные вопросы клиенту: «(вопрос N)», «ASIS §» везде; на картах — любое «вопрос N»
KARTY = sorted(PPO.glob("*/_parts/karta*.svg.html")) + sorted(PPO.glob("*/karta-*.html"))
for f in sorted(set(PPO.glob("*/*.html")) | set(KARTY)):
    rx = r"вопрос[а-яё]*\s*№?\s*\d+|ASIS §" if f in KARTY else r"\(вопрос \d+\)|ASIS §"
    for m in re.finditer(rx, rd(f), re.I):
        err("K4", f"{f.relative_to(PPO)}: «{m.group(0)}»")

# K5 пометка «1С — неизвестно, уточнить»: каждый <g> слоя Б (ошибка) и слоя А (предупреждение: цитата доски,
# решает владелец) с «1С» в видимом тексте несёт «неизвестно» или data-1c="unk"
for layer, lvl in (("B", err), ("A", warn)):
    f = PPO / f"sdelki/_parts/karta-{layer}.svg.html"
    if not f.exists():
        continue
    src = rd(f)
    for m in re.finditer(r'<g( data-1c="unk")?>(<title>.*?)</g>', src, re.S):
        g = m.group(0)
        title = re.search(r"<title>(.*?)</title>", g, re.S).group(1)
        text = " ".join(re.findall(r"<text[^>]*>(.*?)</text>", g, re.S))
        after = src[m.end():m.end() + 900].split("<g", 1)[0]  # подписи сразу за группой, до следующей <g>
        if re.search(r"Б24 «[^»]*» — из 1С", title):
            text += " [подпись вне <g>: из 1С]" + (" неизвестно" if "неизвестно, уточнить" in after else "")
        if "1С" in text and "неизвестно" not in text and 'data-1c="unk"' not in g:
            if re.match(r"Статусная модель, ячейка [^:]*: 1С «", title) or re.match(r"Статусная модель, ячейка I\d+:", title):
                continue  # строка 1С статусной модели / направление обмена — дословная цитата ячейки
            lvl("K5", f"слой {layer}: «{html.unescape(text)[:70]}»")

# K6 ПДн: сначала вырезать белый список id Miro (19 цифр, префиксы 3074457/3458764, включая маски «…хх»),
# затем телефонов РФ, e-mail и чисел ≥ 15 цифр должно быть 0 (эталон — 0)
MIRO = re.compile(r"(?<!\d)(?:3074457|3458764)\d{8,12}(?:хх|xx)?")
SEP = r"[\s()\-‐–—.]*"
PHONE = re.compile(r"(?<![\d\w])(?:\+7|8|7)" + SEP + r"\d{3}" + SEP + r"\d{3}" + SEP + r"\d{2}" + SEP + r"\d{2}(?!\d)")
MAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)*\.[A-Za-zА-Яа-я]{2,}")
LONG = re.compile(r"(?<!\d)\d{15,}(?!\d)")
naive = 0
for f in sorted(PPO.rglob("*.html")):
    s = rd(f)
    naive += len(PHONE.findall(s))
    s2 = MIRO.sub("", s)
    for kind, rx in (("телефон", PHONE), ("e-mail", MAIL), ("число ≥15 цифр", LONG)):
        for m in rx.findall(s2):
            err("K6", f"{f.relative_to(PPO)}: {kind} «{m}»")
INFO["K6"] = [f"без белого списка телефонов {naive}, после — {len(ERR['K6'])}"]

# K9 шлюз лидов: собранные lidy/*.html байт в байт как на базе (иначе нужен --lidy с «да» владельца)
INFO["K9"] = [f"база {BASE[:7]}" + (" (--lidy)" if "--lidy" in ARGS else "")]
if BASE_NOTE:
    warn("K9", BASE_NOTE)
if "--lidy" not in ARGS:
    for f in sorted((PPO / "lidy").glob("*.html")):
        old = git_show(f"docs/ppo/lidy/{f.name}")
        if old is None:
            warn("K9", f"lidy/{f.name}: нет в базе {BASE[:7]}")
        elif old != f.read_bytes():
            err("K9", f"lidy/{f.name} изменён относительно {BASE[:7]} без --lidy")

# K7 stitch вызван: karta.svg.html сделок = склейка слоёв; K8 идемпотентность: две пересборки в копии = текущее
if "stitch" not in rd(PPO / "build_all.py"):
    warn("K7", "build_all.py не вызывает stitch.py")
tmp = Path(tempfile.mkdtemp(prefix="check_ppo_"))
try:
    cp = tmp / "ppo"
    shutil.copytree(PPO, cp, ignore=shutil.ignore_patterns("__pycache__"))

    def snap(d): return {str(p.relative_to(d)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(d.rglob("*.html"))}

    s0 = snap(cp)
    st = cp / "sdelki/_parts/stitch.py"
    if st.exists():
        r = subprocess.run([sys.executable, str(st)], capture_output=True, text=True)
        if r.returncode:
            err("K7", "stitch.py упал: " + (r.stderr.strip().splitlines() or ["?"])[-1][:120])
        elif snap(cp) != s0:
            err("K7", "karta.svg.html сделок ≠ склейка слоёв A/B/C: stitch.py не вызван после правки слоя")

    def build():
        r = subprocess.run([sys.executable, str(cp / "build_all.py")], capture_output=True, text=True)
        if r.returncode or "пропущен" in r.stdout:
            tail = (r.stderr.strip() or r.stdout.strip()).splitlines() or ["?"]
            err("K8", f"сборка: код {r.returncode}, {tail[-1][:120]}")
        return snap(cp)

    s1, s2 = build(), build()
    if s1 != s2:
        err("K8", "две сборки подряд дают разные файлы: " + ", ".join(k for k in s1 if s1[k] != s2.get(k)))
    changed = [k for k in s1 if s1[k] != s0.get(k)] + [k for k in s0 if k not in s1]
    if changed:
        err("K8", "пересборка не совпадает с текущими файлами: " + ", ".join(changed))
finally:
    shutil.rmtree(tmp, ignore_errors=True)

NAMES = {"K1": "связность точек", "K2": "номера не пропали", "K3": "источник у вариантов (data-src)",
         "K4": "нет «(вопрос N)» на картах", "K5": "пометка 1С", "K6": "ПДн", "K7": "stitch вызван",
         "K8": "идемпотентность сборки", "K9": "шлюз лидов",
         "K10": "владение вопроса (data-see, data-id, дубли, повестка)"}
for k in KS:
    e, w = ERR[k], WARN[k]
    st = f"ОШИБОК {len(e)}" if e else ("ПРЕДУПР " + str(len(w)) if w else "ок")
    info = "; ".join(INFO.get(k, []))
    print(f"{k} {NAMES[k]}: {st}" + (f" ({info})" if info else ""))
    for m in e:
        print(f"   ОШИБКА {m}")
    for m in w:
        print(f"   предупр {m}")
ne, nw = sum(map(len, ERR.values())), sum(map(len, WARN.values()))
print(f"итого: ошибок {ne}, предупреждений {nw}")
sys.exit(1 if ne else 0)
