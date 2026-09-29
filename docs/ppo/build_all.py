#!/usr/bin/env python3
"""Сборка всех процессов ППО и оглавления docs/ppo/index.html.

Запуск: python3 docs/ppo/build_all.py
Процесс собирается, только если в его _parts есть все обязательные фрагменты.
"""
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE / "_common"))
from build_proc import COMMON_CSS, WIN_KARTA, WIN_OBSL, Proc, build, page  # noqa: E402

SRC_BOARD = "Источник: доска клиента «Copy of Евростекло» (Miro, только чтение, 28.09.2026)"

PROCS = [
    Proc(
        slug="lidy", name="Лиды", pfx="", item_last="последний реальный лид",
        map_lead="Схема клиента, перенесённая в BPMN: кто что делает, где связи есть и где их нет. Красный номер — нажмите, откроется вопрос к встрече.",
        short_lead="ключевых вопросов по красным точкам карты. Спрашиваете — клиент подтверждает или поправляет — вы отмечаете.",
        full_lead="Полная версия: что на доске, что в портале, почему противоречие, все вопросы и уточнения, состояния и истории.",
        full_intro="источники, состояния лида, пользовательские истории",
        legend_src=f"{SRC_BOARD} и запись портала. Доска не изменялась. Это взгляд на схему клиента, а не утверждённый процесс.",
    ),
    Proc(
        slug="sdelki", name="Сделки", pfx="С", item_last="последнюю реальную сделку",
        layers={"А": "Доска Романа", "Б": "ТЗ и статусы Б24/1С", "В": "Портал"},
        map_lead="Сделка от «Предв. расчёта» до закрытия в трёх слоях: доска Романа, ТЗ 2024–2025 со статусной моделью Б24 ↔ 1С, портал справочно. Красный номер — нажмите, откроется вопрос к встрече.",
        short_lead="ключевых вопросов по красным точкам карты сделок. Спрашиваете — клиент подтверждает или поправляет — вы отмечаете.",
        full_lead="Полная версия: доска, ТЗ, статусная модель Б24 ↔ 1С, почему противоречие, все вопросы и уточнения, состояния и истории.",
        full_intro="источники, модель состояний сделки (Б24 ↔ 1С), пользовательские истории",
        legend_src=f"{SRC_BOARD}, ТЗ 2024–2025 и статусная модель Б24 ↔ 1С (обезличенные тексты в client-materials/sanitized-*.md). 1С — «неизвестно, уточнить». Доска не изменялась.",
    ),
]
REQUIRED = ("karta.svg.html", "tochki.html", "sostoyaniya.html")

built = {}
for p in PROCS:
    missing = [f for f in REQUIRED if not (p.parts / f).exists()]
    if missing:
        print(p.slug, "пропущен — нет фрагментов:", ", ".join(missing))
        continue
    built[p.slug] = build(p)

# ---------- Оглавление ----------
INDEX_CSS = COMMON_CSS + """.blocks{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:16px}
.blockc{border:1px solid var(--line);border-radius:10px;padding:16px 18px;background:#fff}
.blockc h3{margin:0 0 8px}.blockc ul{margin:6px 0 0;padding-left:20px}.blockc li{margin:4px 0}.blockc a{color:var(--accent);font-weight:600}
.soon{color:var(--muted)}.badge{font-size:13px;font-weight:700;border-radius:6px;padding:1px 8px;background:#e5f3e9;color:#1f6b3a;border:1px solid #1f6b3a}
.badge.wip{background:#fbf1d9;color:#8a5a00;border-color:#8a5a00}"""
BLOCKS = {
    "lidy": ("1. Лиды", '<span class="badge">утверждено 28.09</span>', "От обращения клиента до сделки."),
    "sdelki": ("2. Сделки", '<span class="badge wip">на согласовании</span>',
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
<section><h2>Основания и правила</h2><ul>
<li><b>Доска Романа</b> — его предположение о процессе, не истина; расхождения выносим клиенту.</li>
<li><b>Базовая линия</b> — ТЗ 2024–2025 (UNVERIFIED до подтверждения клиентом).</li>
<li><b>Портал</b> — справочно; проверит интегратор отдельным аудитом (по команде владельца).</li>
<li>Журнал решений владельца: <code>docs/ppo/00-resheniya-vladeltsa.md</code>. Обезличенные исходники: <code>client-materials/sanitized-*.md</code>.</li></ul></section>"""
(HERE / "index.html").write_text(page("Евростекло · предпроектное обследование",
    "Управляющий файл: процессы, карты, вопросы к встрече. Всё связано ссылками.", index_body, INDEX_CSS,
    '<nav class="docnav"><b>☰ Оглавление</b></nav>'), encoding="utf8")
print("index ok")
