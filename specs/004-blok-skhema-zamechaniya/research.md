# Research: спецификация 004

## R1. Как обновить страницу без генератора `build.mjs`

- **Decision**: править `eurosteklo_process.drawio`, затем заменить XML в атрибуте `data-mxgraph` страницы `view.html` тем же XML (JSON-строка, HTML-экранирование).
- **Rationale**: `view.html` — viewer diagrams.net (`<script src="https://viewer.diagrams.net/js/viewer-static.min.js">`, атрибут `data-mxgraph`; grep 28.09); генератор не нужен.
- **Alternatives considered**: восстановить `build.mjs` из БД opencode — сорвалось (spec 003 А7) и запрещено «не пересобирать»; экспорт в SVG/PNG вместо страницы — меняет формат опубликованного объекта.

## R2. Как уместить шрифт ≥16 px

- **Decision**: увеличить ширину задач и высоту дорожек пропорционально; полотно шире экрана допустимо (горизонтальная прокрутка, spec Edge Cases). Проверка перекрытий — `drawio-ai-kit audit` + скриншот.
- **Rationale**: содержание не меняется (FR-011); переразводка маршрутов минимальна.
- **Alternatives considered**: `suggest-layout` с новой раскладкой — это пересборка (вариант C, отклонён).

## R3. Значки документов и номера вопросов

- **Decision**: документ — фигура draw.io `shape=document` в дорожке «Клиент», связь `dashed=1` к шагу; номер вопроса — круг `ellipse` с красной обводкой #D90000 и цифрой, привязанный к шагу; список «Проход с клиентом» — текстовый блок внизу полотна.
- **Rationale**: штатные фигуры draw.io, viewer их рисует без плагинов.
- **Alternatives considered**: BPMN data object (`shape=mxgraph.bpmn.data`) — допустим, если `validate` ругается на `shape=document`; выбор фиксирует атом по выводу `validate`.

## R4. Цвета

- **Decision**: `#232F3E` (15 обводок, 16 подписей) и `#5A6B7B` → `#1A1A1A`; `#D90000` — только номера 1–9; подложки фаз `#EEF2F7`/`#F5F8FB` сохраняются.
- **Rationale**: выбор владельца «Чёрный + один красный» (S2-13).
