#!/usr/bin/env python3
"""Проверки ППО K1–K9 (только чтение рабочего дерева; сборка — во временной копии).

Запуск: python3 docs/ppo/check_ppo.py [--base=SHA] [--lidy]
  --base=SHA  база для K2 (номера точек) и K9 (шлюз лидов); по умолчанию 575a157 (лиды 28.09, сделки 29.09)
  --lidy      разрешить изменение собранных страниц лидов (только с «да» владельца на лиды)
Код выхода: 0 — ошибок нет, 1 — есть. Предупреждения (K3, слой А в K5, недоступная база) код не меняют.
Основа — прототип SRE (specs/006-ispravlenie-kart/kritika/c2-6-sre.md), регэксп ПДн — свой (c2-5, п.36).
"""
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
ARGS = sys.argv[1:]
BASE = next((a.split("=", 1)[1] for a in ARGS if a.startswith("--base=")), "575a157909476c9e55724ac1a28b78a4fb356321")
PROCS = ("lidy", "sdelki")
KS = [f"K{i}" for i in range(1, 10)]
ERR, WARN = {k: [] for k in KS}, {k: [] for k in KS}
INFO = {}


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

    bad = tot = 0
    for n, body in re.findall(CARD + r"(.*?)</article>", rd(parts / "tochki.html"), re.S):
        m = re.search(r"<dt>Уточнить по состояниям</dt>\s*<dd>(.*?)</dd>", body, re.S)
        for li in re.findall(r"<li>(.*?)</li>", m.group(1) if m else "", re.S):
            tot += 1
            if 'class="src"' not in li and "наш вариант" not in li:
                bad += 1
    if bad:
        warn("K3", f"{slug}: {bad} из {tot} вариантов «А если…» без источника/пометки «наш вариант (гипотеза)»")

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

NAMES = {"K1": "связность точек", "K2": "номера не пропали", "K3": "источник у вариантов",
         "K4": "нет «(вопрос N)» на картах", "K5": "пометка 1С", "K6": "ПДн", "K7": "stitch вызван",
         "K8": "идемпотентность сборки", "K9": "шлюз лидов"}
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
