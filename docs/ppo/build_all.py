#!/usr/bin/env python3
"""Сборка всех процессов ППО и оглавления docs/ppo/index.html.

Запуск: python3 docs/ppo/build_all.py
Перед сборкой процесса вызывается его _parts/stitch.py (склейка слоёв карты), если он есть.
Процесс собирается, только если в его _parts есть все обязательные фрагменты.
Код выхода 1, если процесс пропущен или stitch.py упал (остальное при этом собирается).
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE / "_common"))
from build_proc import COMMON_CSS, WIN_KARTA, WIN_OBSL, Proc, build, page  # noqa: E402

SRC_BOARD = "Источник: доска клиента «Copy of Евростекло» (Miro, только чтение, 28.09.2026)"

PROCS = [
    Proc(
        slug="lidy", name="Лиды", name_in="«Лидах»", pfx="", item_last="последний реальный лид",
        legend_said="запись экрана и речь интегратора",
        map_lead="Схема клиента, перенесённая в BPMN: кто что делает, где связи есть и где их нет. Красный номер — нажмите, откроется вопрос к встрече.",
        short_lead="ключевых вопросов по красным точкам карты. Спрашиваете — клиент подтверждает или поправляет — вы отмечаете.",
        full_lead="Полная версия: что на доске, что в портале, почему противоречие, все вопросы и уточнения, состояния и истории.",
        full_intro="источники, состояния лида, пользовательские истории",
        legend_src=f"{SRC_BOARD} и запись портала. Доска не изменялась. Это взгляд на схему клиента, а не утверждённый процесс.",
    ),
    Proc(
        slug="sdelki", name="Сделки", name_in="«Сделках»", pfx="С", item_last="последнюю реальную сделку",
        legend_said="запись экрана портала и речь интегратора — только слой «Портал», справочно; документы клиента — метка «документ клиента»",
        layers={"А": "Доска Романа", "Б": "ТЗ и статусы Б24/1С", "В": "Портал"},
        map_lead="Сделка от «Предв. расчёта» до закрытия в трёх слоях: доска Романа, ТЗ 2024–2025 со статусной моделью Б24 ↔ 1С, портал справочно. Красный номер — нажмите, откроется вопрос к встрече.",
        short_lead="ключевых вопросов по красным точкам карты сделок. Спрашиваете — клиент подтверждает или поправляет — вы отмечаете.",
        full_lead="Полная версия: доска, ТЗ, статусная модель Б24 ↔ 1С, почему противоречие, все вопросы и уточнения, состояния и истории.",
        full_intro="источники, модель состояний сделки (Б24 ↔ 1С), пользовательские истории",
        legend_src=f"{SRC_BOARD}, ТЗ 2024–2025 и статусная модель Б24 ↔ 1С (обезличенные тексты в client-materials/sanitized-*.md). 1С — «неизвестно, уточнить». Доска не изменялась.",
    ),
]
REQUIRED = ("karta.svg.html", "tochki.html", "sostoyaniya.html")

ALLP = {p.slug: p for p in PROCS}  # для ссылок «этот вопрос задаём в …» между процессами
built = {}
failed = False
for p in PROCS:
    stitch = p.parts / "stitch.py"
    if stitch.exists():
        r = subprocess.run([sys.executable, str(stitch)])
        if r.returncode:
            print(p.slug, "пропущен — stitch.py упал, код", r.returncode)
            failed = True
            continue
    missing = [f for f in REQUIRED if not (p.parts / f).exists()]
    if missing:
        print(p.slug, "пропущен — нет фрагментов:", ", ".join(missing))
        failed = True
        continue
    built[p.slug] = build(p, ALLP)

# ---------- Оглавление ----------
INDEX_CSS = COMMON_CSS + """.blocks{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.blockc{border:1px solid var(--line);border-radius:10px;padding:16px 18px;background:#fff}
.blockc h3{margin:0 0 8px}.blockc ul{margin:6px 0 0;padding-left:20px}.blockc li{margin:4px 0}.blockc a{color:var(--accent);font-weight:600}
.soon{color:var(--muted)}.badge{font-size:13px;font-weight:700;border-radius:6px;padding:1px 8px;background:#e5f3e9;color:#1f6b3a;border:1px solid #1f6b3a}
.badge.wip{background:#fbf1d9;color:#8a5a00;border-color:#8a5a00}"""
BLOCKS = {
    "lidy": ("1. Лиды", '<span class="badge">предварительно утверждено 28.09</span>', "От обращения клиента до сделки."),
    "sdelki": ("2. Сделки", '<span class="badge">исправлено 30.09</span>',
               "Расчёт и замер → договор и оплата → производство → отгрузка / монтаж → закрытие. Слои: доска Романа, ТЗ 2024–2025 и статусная модель Б24 ↔ 1С (1С — «неизвестно, уточнить»), портал справочно."),
}
blocks = ""
for p in PROCS:
    title, badge, desc = BLOCKS[p.slug]
    if p.slug in built:
        k, s, f = p.files
        n = len(built[p.slug]["cards"])
        blocks += f"""<div class="blockc"><h3>{title} {badge}</h3><p>{desc} {n} конфликтных точек.</p><ul>
<li><a href="{p.slug}/{k}" target="{WIN_KARTA}">Карта процесса (BPMN, 3 слоя)</a></li>
<li><a href="{p.slug}/{s}" target="{WIN_OBSL}">Вопросы к встрече</a></li>
<li><a href="{p.slug}/{f}" target="{WIN_OBSL}">Подробная версия обследования</a></li></ul></div>"""
    else:
        blocks += f"""<div class="blockc"><h3>{title} <span class="badge wip">в работе</span></h3><p class="soon">{desc}</p><ul class="soon"><li>Карта процесса — готовится</li><li>Вопросы к встрече — готовится</li></ul></div>"""
index_body = f"""<section><h2>Как пользоваться</h2><p>Скачайте папку <code>docs/ppo</code> целиком — все файлы связаны ссылками. На встрече два окна: <b>карта процесса</b> и <b>вопросы к встрече</b>. Красный номер на карте открывает вопрос; номер в вопросе открывает карту и подсвечивает точку. Масштаб — кнопки справа внизу, Ctrl + колесо.</p></section>
<section><h2>Процессы</h2><div class="blocks">{blocks}</div></section>
<section><h2>Лид и сделка — где граница</h2><ul>
<li><b>Лид</b> — первичное обращение потенциального клиента из любого канала или рекламного источника, до квалификации.</li>
<li><b>Сделка</b> — работа с квалифицированным клиентом после конвертации лида.</li>
<li>Вопрос живёт в одном процессе; во втором — строка «↪ этот вопрос задаём в …» со ссылкой на карточку.</li>
<li>Квалифицированный, но не конвертированный клиент — ещё лид.</li>
<li>Повторный клиент — новый лид, привязанный к прежнему контакту.</li>
<li>Сделка из 1С без лида — исключение, помечается.</li>
<li>Общие правила для лида и сделки — точка С23.</li></ul>
<p class="soon">Определения лида и сделки — владельца 30.09.2026. Правила границы лид/сделка — решение архитектора по поручению владельца 30.09 (В1–В3), противоречие с ТЗ ФТ-2 — вопрос клиенту.</p></section>
<section><h2>Основания и правила</h2><ul>
<li><b>Доска Романа</b> — его предположение о процессе, не истина; расхождения выносим клиенту.</li>
<li><b>Базовая линия</b> — ТЗ 2024–2025 (UNVERIFIED до подтверждения клиентом).</li>
<li><b>Портал</b> — справочно; проверит интегратор отдельным аудитом (по команде владельца).</li>
<li>Журнал решений владельца <span class="badge">предварительно утверждено 28.09</span>: <code>docs/ppo/00-resheniya-vladeltsa.md</code>. Обезличенные исходники: <code>client-materials/sanitized-*.md</code>.</li></ul></section>"""
(HERE / "index.html").write_text(page("Евростекло · предпроектное обследование",
    "Управляющий файл: процессы, карты, вопросы к встрече. Всё связано ссылками.", index_body, INDEX_CSS,
    '<nav class="docnav"><b>☰ Оглавление</b></nav>'), encoding="utf8")
print("index ok")
if failed:
    sys.exit(1)
