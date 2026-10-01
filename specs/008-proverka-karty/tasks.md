# Задачи: спецификация 008 — точечная проверка карты владельца

Источник: `specs/008-proverka-karty/spec.md` (заморожен, коммит 2e01bce; роль plan.md — его разделы 3–6). Атом: `eurosteklo-4ub`.
Составлено 01.10 после запуска блоков: отметка `[x]` — только там, где файл отчёта существует (по отчёту исполнителя OpenCode).
Каталог отчётов: `docs/review/2026-10-01-proverka-karty/`. Исполнение каждой задачи — `code-channel auto` (Workflow code-atom), поручение — `specs/008-proverka-karty/blocks/<блок>.md`.

## Фаза 1. Подготовка

- [x] T001 Спецификация и поручения блоков в `specs/008-proverka-karty/spec.md`, `blocks/*.md`; ce-doc-review (coherence, feasibility) — 14 находок применены до отправки

## Фаза 2. История US1 — «по каждому согласованному пункту виден статус на карте» (блоки независимы, свой файл у каждого)

- [x] T002 [P] [US1] Блок A: правки S1 и S2 → `docs/review/2026-10-01-proverka-karty/A-pravki-s1-s2.md`
- [x] T003 [P] [US1] Блок B: находки Codex → `docs/review/2026-10-01-proverka-karty/B-codex-nakhodki.md`
- [x] T004 [P] [US1] Блок C: чекпойнты e1–e7 → `docs/review/2026-10-01-proverka-karty/C-checkpoints-e1-e7.md`
- [ ] T005 [P] [US1] Блок D1, часть 1 (П-01…П-15) → `docs/review/2026-10-01-proverka-karty/D1-k1-prepost-1.md`
- [ ] T006 [P] [US1] Блок D1, часть 2 (П-16…П-30) → `docs/review/2026-10-01-proverka-karty/D1-k1-prepost-2.md`
- [ ] T007 [P] [US1] Блок D1, часть 3 (П-31…конец) → `docs/review/2026-10-01-proverka-karty/D1-k1-prepost-3.md`
- [ ] T008 [P] [US1] Блок D2, часть 1 (Р-01…Р-13) → `docs/review/2026-10-01-proverka-karty/D2-k2-forks-1.md`
- [ ] T009 [P] [US1] Блок D2, часть 2 (Р-14…Р-26) → `docs/review/2026-10-01-proverka-karty/D2-k2-forks-2.md`
- [ ] T010 [P] [US1] Блок D2, часть 3 (Р-27…конец) → `docs/review/2026-10-01-proverka-karty/D2-k2-forks-3.md`
- [x] T011 [P] [US1] Блок D3: К-01…К-37 → `docs/review/2026-10-01-proverka-karty/D3-k3-conflicts.md`
- [ ] T012 [P] [US1] Блок E1: ошибки карты Е-xx, О-xx → `docs/review/2026-10-01-proverka-karty/E1-oshibki-karty.md`
- [x] T013 [P] [US1] Блок E2: ТЗ ↔ доска → `docs/review/2026-10-01-proverka-karty/E2-tz-vs-doska.md`
- [ ] T014 [P] [US1] Блок E3: фактчек сделок → `docs/review/2026-10-01-proverka-karty/E3-factcheck-sdelki.md`
- [ ] T015 [P] [US1] Блок E4: фактчек лидов → `docs/review/2026-10-01-proverka-karty/E4-factcheck-lidy.md`

Независимая проверка истории: в каждом файле строка «Итог», сумма статусов = N = числу строк таблицы (spec §9 п.1–2).

## Фаза 3. Сведение и приёмка

- [ ] T016 Блок F (после T002–T015): `docs/review/2026-10-01-proverka-karty/svodka.md` по spec §6
- [ ] T017 Приёмка по spec §9 (4 критерия), таблица пункт → факт
- [ ] T018 Коммит, PR в main, закрытие `eurosteklo-4ub`

## Зависимости

T001 → T002…T015 (параллельно, до 5 одновременно) → T016 → T017 → T018.

## Отклонения от spec §3 (исполнение, не содержание)

- D1 и D2 не уложились в лимит 590 с одним прогоном → разделены на 3 части каждый; файлов отчёта у D1 и D2 по три (`-1`, `-2`, `-3`) вместо одного. Строки источника, метод и статусы — по spec без изменений.
