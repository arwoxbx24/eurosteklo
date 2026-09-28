#!/usr/bin/env python3
"""Сборка двух HTML «Лиды» из фрагментов _parts (механическое сведение)."""
from pathlib import Path
P = Path(__file__).parent
css = (P / "base.css").read_text(encoding="utf8")
def page(title, lead, body, extra_css=""):
    return f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{css}{extra_css}</style></head>
<body><div class="page"><header><h1>{title}</h1><p class="lead">{lead}</p></header>
{body}
</div></body></html>
"""
legend = """<section><h2>Как читать</h2><div class="legend">
<span><span class="st st-board">на доске</span> есть на доске Miro</span>
<span><span class="st st-said">со слов</span> запись экрана и речь интегратора</span>
<span><span class="st st-unk">не знаем</span> источника нет — спросить</span>
<span><span class="st st-conf">противоречие</span> источники расходятся</span>
<span><span class="pt">N</span> конфликтная точка — вопрос в документе «Обследование»</span></div>
<p class="src">Источник: доска клиента «Copy of Евростекло» (Miro, только чтение, 28.09.2026) и запись портала. Доска не изменялась. Это взгляд на схему клиента, а не утверждённый процесс.</p></section>"""
svg = (P / "karta.svg.html").read_text(encoding="utf8")
map_css = ".mapwrap{overflow-x:auto}.mapwrap svg{width:100%;min-width:1100px;height:auto;display:block}"
(P.parent / "karta-lidy.html").write_text(page(
    "Евростекло · Лиды: карта процесса",
    "Схема клиента, перенесённая в BPMN: кто что делает, где стрелки есть и где их нет. Красные номера — места, которые обсуждаем на встрече.",
    legend + f'<section><h2>Карта «Лиды»</h2><div class="mapwrap">{svg}</div></section>', map_css), encoding="utf8")
card_css = """.card{border:1px solid var(--line);border-left:6px solid var(--pt);border-radius:8px;padding:14px 18px;margin:16px 0;background:#fff}
.card header{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin-bottom:8px}
.card dl{display:grid;grid-template-columns:220px 1fr;gap:6px 16px;margin:0}
.card dt{font-weight:700;color:var(--muted)}.card dd{margin:0}
.card dd.q{font-weight:700;color:var(--accent);font-size:18px}
.card ul{margin:0;padding-left:20px}
@media (max-width:700px){.card dl{grid-template-columns:1fr}.card dt{margin-top:6px}}"""
intro = """<section><h2>Как пользоваться</h2><p>Откройте рядом «Карту процесса». Каждый красный номер на карте — карточка ниже. В карточке: что нарисовано на доске, где это не сходится, какой вопрос задать и что уточнить «а если…». Вопросы задаём на примере последнего реального лида: клиент показывает на экране, а не рассказывает «как обычно».</p>
<nav class="toc"><a href="#top5">С чего начать</a> · <a href="#tochki">12 конфликтных точек</a> · <a href="#sostoyaniya">Состояния лида</a> · <a href="#stories">Пользовательские истории</a></nav></section>"""
body = intro + legend
tochki = (P / "tochki.html").read_text(encoding="utf8")
sost = (P / "sostoyaniya.html").read_text(encoding="utf8")
import re
m = re.search(r'<section id="top5">.*?</section>', tochki, re.S)
top5 = m.group(0) if m else ""
tochki = tochki.replace(top5, "")
(P.parent / "obsledovanie-lidy.html").write_text(page(
    "Евростекло · Лиды: предпроектное обследование",
    "Вопросы к клиенту по конфликтным точкам схемы «Лиды»: что спросить, как спросить, что уточнить по каждому состоянию.",
    body + top5 + tochki + sost, card_css), encoding="utf8")
print("ok")
