# Задачи: выполнение разового сообщения агентам

**Вход**: `specs/007-soobshchenie-vypolnenie/spec.md`, план `docs/plans/2026-10-01-0859-chore-soobshchenie-agentam-vypolnenie-plan.md` (роль plan.md)
**Рабочее дерево**: `.worktrees/claude/lq9`, ветка `claude/lq9-soobshchenie-vypolneno` от `origin/main` `21125b3`
**Правило**: спецификация и задачи в процессе не меняются; расхождение с фактом — стоп + bd.
**Тесты**: отдельные тестовые задачи не заказаны; проверка — командой с числом в каждой задаче.

## Формат: `[ID] [P?] [Story] Описание`

## Фаза 1: Подготовка

- [ ] T001 Сверить состояние перед работой: `git -C .worktrees/claude/lq9 fetch --prune origin --tags`, `git ls-remote --tags origin 'checkpoint/*'` → ровно 2 строки (`lidy-sdelki` и `^{}` → `575a157…`). Иначе стоп.

## Фаза 2: Основа (блокирует истории)

- [ ] T002 Проверить, что 6 SHA из `docs/CHECKPOINTS.md` — предки `origin/main`: `git merge-base --is-ancestor <SHA> origin/main` по каждому → 6 из 6 код 0. Не предок → эту метку исключить, факт в bd (spec Clarifications Q2).

## Фаза 3: История 1 — метки отката (P1) 🎯 MVP

**Цель**: 6 аннотированных меток на GitHub.
**Независимая проверка**: `git ls-remote --tags origin 'checkpoint/*'` → 7 меток, `^{}` новых = SHA реестра.

- [ ] T003 [US1] Создать 6 аннотированных меток по таблице `docs/CHECKPOINTS.md` (имя — текст в обратных кавычках, сообщение — `e<N>: ` + начало столбца «Что зафиксировано»):
  - `checkpoint/2026-09-30-e3-dvizhok` → `09437d4f530d9d4e8c54305ef23a0ee556a268f9`
  - `checkpoint/2026-09-30-e1-sdelki` → `3898d95a76402934b64529d3a44ddec7293f0a3e`
  - `checkpoint/2026-09-30-e2-lidy-sdelki` → `71ea516d915f5d6f0e4a4765531a5410722d89c0`
  - `checkpoint/2026-09-30-e4-karta` → `97bc3cba6a14a6d131bd181f84e3c58a5364b6ef`
  - `checkpoint/2026-09-30-e5-roli` → `b6ce7435781584d5b95523bb4d4ab301f2a76dd7`
  - `checkpoint/2026-09-30-e6-pokaz` → `16df6eb18517450946326ff8008fe6a6016d0a4b`
  Проверка: `git rev-parse <метка>^{}` = SHA для 6 из 6.
- [ ] T004 [US1] Отправить каждую метку отдельным `git push origin <метка>` (6 вызовов, не `--tags`). Отказ дважды — стоп.
- [ ] T005 [US1] Проверить: `git ls-remote --tags origin 'checkpoint/*'` → 7 меток; `^{}` 6 новых = SHA T003; `lidy-sdelki^{}` = `575a157909476c9e55724ac1a28b78a4fb356321`.

**Контрольная точка**: история 1 выполнена и проверена отдельно.

## Фаза 4: История 2 — пустая ветка (P2)

**Цель**: ветки `claude/wonderful-pasteur-7tzxeu` нет на GitHub.
**Независимая проверка**: `git ls-remote --heads origin claude/wonderful-pasteur-7tzxeu` → 0 строк.

- [ ] T006 [P] [US2] Непосредственно перед удалением: `git fetch --prune origin`; `git ls-remote --heads origin claude/wonderful-pasteur-7tzxeu` → SHA = `575a157909476c9e55724ac1a28b78a4fb356321`; `git log --oneline origin/main..origin/claude/wonderful-pasteur-7tzxeu` → 0 строк. Иначе стоп.
- [ ] T007 [US2] Удалить: `git push origin --delete claude/wonderful-pasteur-7tzxeu`. Проверка: `ls-remote --heads` → 0 строк; `git merge-base --is-ancestor 575a157 origin/main` → код 0.

## Фаза 5: История 3 — сообщение снято (P3)

**Цель**: в `main` нет файла сообщения и ссылки на него; реестр дописан.
**Зависимость**: T005 и T007 выполнены.
**Независимая проверка**: `git grep -n SOOBSHCHENIE origin/main` → 0 строк после merge.

- [ ] T008 [US3] Удалить `docs/SOOBSHCHENIE-AGENTAM.md` (`git rm`).
- [ ] T009 [US3] Удалить строку 5 в `docs/ppo/HANDOFF.md` (ссылка «Разовое сообщение агентам…»). Проверка: `git grep -n SOOBSHCHENIE` в дереве → 0.
- [ ] T010 [US3] Дописать в конец `docs/CHECKPOINTS.md` абзац: метки e3, e1, e2, e4, e5, e6 (6 имён) поставлены CLI-агентом 01.10.2026; `git ls-remote --tags origin 'checkpoint/*'` показывает 7; приписки «(метку ставит CLI-агент)» в таблице и абзац о недоступности меток утратили силу. Строки таблицы не трогать. Проверка: `git diff -- docs/CHECKPOINTS.md` → 0 строк с `-`.
- [ ] T011 [US3] `gitleaks` по ветке → 0 находок; коммит (автор по `git config`), push ветки `claude/lq9-soobshchenie-vypolneno`.
- [ ] T012 [US3] PR в `main`; слияние `gh pr merge <N> --merge --match-head-commit <полный sha>`. Проверка: `gh pr view <N> --json state` → MERGED.
- [ ] T013 [US3] После merge: `git fetch origin`; `git grep -n SOOBSHCHENIE origin/main` → 0; `git diff 21125b3 origin/main -- docs/CHECKPOINTS.md | grep -c '^-[^-]'` → 0.

## Фаза 6: Завершение

- [ ] T014 Убрать своё: `git worktree remove .worktrees/claude/lq9`; локальная ветка — `git branch -d` (после squash не применимо — merge-коммит); удалённая ветка `claude/lq9-soobshchenie-vypolneno` — `git push origin --delete` после MERGED.
- [ ] T015 Закрыть атом `eurosteklo-lq9`: в reason — выводы T005 (7 меток), T007 (0 строк), T013 (0 строк), номер PR.

## Зависимости

- T001 → T002 → US1 (T003 → T004 → T005).
- US2 (T006 → T007) не зависит от US1; T006 можно выполнять параллельно с T003–T005.
- US3 (T008–T013) — после T005 и T007.
- T014, T015 — после T013.

## Параллельно

- T006 [P] идёт одновременно с US1: разные ссылки GitHub, общих файлов нет.

## Стратегия

MVP — история 1 (метки): даёт откат по метке сразу. Затем история 2, затем история 3 одним PR. Каждая история проверяется своей командой до перехода к следующей.
