# Tasks: Доработка BPMN-схемы DwW по замечаниям владельца

**Input**: `specs/004-blok-skhema-zamechaniya/` — spec.md, plan.md, research.md, data-model.md, quickstart.md
**Готовое решение**: drawio-ai-kit, навык `clients/tools/drawio-ai-kit/skills/drawio-bpmn/SKILL.md` (шаги 1–6 строк 53–69); CLI `K = node /root/workspaces/projects/clients/tools/drawio-ai-kit/src/cli.mjs`
**Исполнение**: каждый атом кода — одна отправка `code-channel auto` в Workflow code-atom, ТЗ после `/ce-doc-review`; разведка — repowise MCP, файл читать только перед правкой. Атомы правки идут последовательно (один файл `build.mjs`), проверки — параллельно.
**Tests**: отдельные тесты не запрошены; проверка — команды `quickstart.md`.

## Format: `[ID] [P?] [Story] Description`

## Phase 1: Setup

- [ ] T001 Снять опись содержания текущей схемы (дорожки 7, фазы 6, узлы s1, t1…t10, gw1, c1, c2, e1, e2 с подписями, дорожкой, фазой; все связи источник→цель→подпись) из `docs/process/bpmn/eurosteklo_process.drawio` в `.agent-work/tz/004-inventory.md` — `code-channel audit`, только чтение

## Phase 2: Foundational (блокирует все истории)

- [ ] T002 Скопировать шаблон набора: `K scaffold bpmn/build_bpmn.mjs -o docs/process/bpmn/build.mjs` и заменить данные шаблона описью T001 (lanes, phases, узлы `{ lane, col, label }`, `d.link` потока), `d.title` — прежний заголовок схемы; координаты руками запрещены (SKILL.md:62-63); выход `node docs/process/bpmn/build.mjs` → `docs/process/bpmn/eurosteklo_process.drawio`; критерий: `validate` ok, число узлов и связей = опись T001 (FR-011)

**Checkpoint**: схема собрана набором, содержание прежнее.

## Phase 3: User Story 1 — клиент читает схему с экрана (P1) 🎯 MVP

**Goal**: крупный шрифт, чёрный цвет, полные слова.
**Independent Test**: quickstart SC-001, SC-002, SC-003 (часть «#232F3E/#5A6B7B = 0»).

- [ ] T003 [US1] В `docs/process/bpmn/build.mjs` подписи — полными словами: «док-ты» → «документы», «14/90/270» → «через 14, 90 и 270 дней»; ₽ и коды FR/FF/P/Ф — 0 (FR-002)
- [ ] T004 [US1] В `docs/process/bpmn/build.mjs` после `d.mxfile()` — одна замена в строке XML с комментарием `ponytail:`: `fontSize` <16 → 16, у заголовков дорожек и фаз — 18; `#232F3E` и `#5A6B7B` → `#1A1A1A`; подложки фаз не трогать (FR-001, FR-003; research R2)

## Phase 4: User Story 2 — документы клиента (P2)

**Goal**: 6 значков документов в дорожке «Клиент» с пунктиром к шагу.
**Independent Test**: quickstart SC-004.

- [ ] T005 [US2] В `docs/process/bpmn/build.mjs` добавить 6 значков каталога `document` (`K search "document"` → General) в дорожке «Клиент»: счёт за замер (data.md:36), договор (:44), счёт на предоплату (:45), счёт на остаток (:55), УПД / отгрузочные документы (:58, один значок), закрывающие документы (:61); связь к шагу — `d.link(doc, step, "", { dash: true })` (FR-004, FR-005)

## Phase 5: User Story 3 — проход по 9 проблемным местам (P3)

**Goal**: номера 1–9 на шагах, список «Проход с клиентом», строка источника.
**Independent Test**: quickstart SC-005.

- [ ] T006 [US3] В `docs/process/bpmn/build.mjs` убрать 9 заметок-вопросов с полотна; на связи, входящей в проблемный шаг, — штатный `step: N`, N = P1…P9 раздела «Проблемные места» `data.md` (examples/aws/build_serverless.mjs:30) (FR-006)
- [ ] T007 [US3] В `docs/process/bpmn/build.mjs` под пулом — штатный `box` «Проход с клиентом»: 9 вопросов P1–P9 из `data.md`, номер = `step`; ниже `box` «Источник: доска Miro клиента и портал Битрикс24, 28.09.2026» (FR-007, FR-009)
- [ ] T008 [US3] В `docs/process/bpmn/build.mjs` — правки строк 1, 7, 9, 17 `docs/process/bpmn/сверка-process-mapping.md` в пределах содержания `data.md` (FR-008)

## Phase 6: Polish — страница, проверка, публикация

- [ ] T009 Перенести XML `docs/process/bpmn/eurosteklo_process.drawio` в атрибут `data-mxgraph` страницы `docs/process/bpmn/view.html` (JSON-строка, HTML-экранирование), остальное в странице не трогать (research R4)
- [ ] T010 [P] Проверка: `K validate docs/process/bpmn/eurosteklo_process.drawio` + issues `node docs/process/bpmn/build.mjs` — ok, 0 warnings, issues пусто (SC-006)
- [ ] T011 [P] Проверка: grep-счётчики quickstart SC-001…SC-005 по `docs/process/bpmn/eurosteklo_process.drawio`
- [ ] T012 [P] Снимок: chrome headless 1920×1400 `docs/process/bpmn/view.html` → `docs/process/bpmn/eurosteklo_process.png` >50 КБ; перекрытий нет (сверка по снимку — субагент sonnet, текстом)
- [ ] T013 Публикация (главный агент): `mc cp docs/process/bpmn/view.html b244minio/files/20260928-181501-view.html`; `curl https://b244.ru/DwW` = 200; `git diff --stat docs/meetings/variants/LINKS.md` пусто (FR-010, SC-007)
- [ ] T014 Обновить таблицу «Факт DwW» в `docs/research/2026-09-28-zamechaniya-skhema.md`: каждая строка — «исправлено» + доказательство (SC-007)

## Dependencies

T001 → T002 → T003 → T004 → T005 → T006 → T007 → T008 → T009 → (T010 ∥ T011 ∥ T012) → T013 → T014.
Истории независимы по смыслу, но правят один `build.mjs` — идут по очереди. MVP = T001–T004 (US1).

## Parallel

- Проверки T010, T011, T012 — одним сообщением.
- ce-doc-review ТЗ атомов US2 и US3 — параллельно с исполнением предыдущего атома.

## Implementation Strategy

1. MVP: T001–T004 → validate → снимок.
2. Добавить US2 (T005), затем US3 (T006–T008), каждый раз `node build.mjs` без issues.
3. T009–T014 — страница, проверка, публикация, контрольная точка владельца по ссылке.

## Атомы bd (код ≤100 строк, одна отправка)

| Атом | Задачи |
|---|---|
| .1 опись | T001 |
| .2 сборка + US1 | T002–T004 |
| .3 US2 | T005 |
| .4 US3 | T006–T008 |
| .5 страница | T009 |
| .6 проверка и публикация | T010–T014 |
