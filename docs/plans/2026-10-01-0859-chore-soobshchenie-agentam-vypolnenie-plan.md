---
title: Выполнение разового сообщения агентам - Plan
type: chore
date: 2026-10-01
artifact_contract: ce-unified-plan/v1
artifact_readiness: implementation-ready
product_contract_source: ce-plan-bootstrap
execution: code
---

# Выполнение разового сообщения агентам - Plan

## Goal Capsule

- **Objective:** владелец и любой агент откатывают `main` к утверждённым этапам e1–e6 по меткам на GitHub; в репозитории нет пустой ветки и выполненного сообщения агентам.
- **Means:** аннотированные метки по реестру `docs/CHECKPOINTS.md`, удаление ветки и файла сообщения одним PR (KTD1–KTD3).
- **Authority:** слово владельца 01.10 («да, выполнить») > `docs/SOOBSHCHENIE-AGENTAM.md` > `docs/CHECKPOINTS.md` > этот план.
- **Stop conditions:**
  - SHA метки не совпадает с реестром.
  - SHA из реестра не предок `origin/main`: эту метку не ставим, остальные ставим, факт — в bd с выводом `git merge-base --is-ancestor`.
  - Ветка `claude/wonderful-pasteur-7tzxeu` на origin не равна `575a157909476c9e55724ac1a28b78a4fb356321` или содержит коммит вне `main`.
  - Push отклонён дважды.
- **Execution profile:** только git и gh, без кода. Атом bd `eurosteklo-lq9`.

## Product Contract

### Summary

Ставим 6 меток отката e1–e6 на GitHub. Удаляем пустую ветку `claude/wonderful-pasteur-7tzxeu`. Удаляем файл сообщения `docs/SOOBSHCHENIE-AGENTAM.md` и ссылку на него в `docs/ppo/HANDOFF.md`.

### Problem Frame

Claude Web 30.09 зафиксировал этапы e1–e6 в `docs/CHECKPOINTS.md`, но метки на GitHub отправить не может: Git-прокси облака их не пропускает. Удалять удалённые ветки облаку тоже запрещено. Работу передали CLI-агенту файлом-сообщением. На 01.10 на origin есть одна метка `checkpoint/2026-09-30-lidy-sdelki`, пустая ветка на месте, файл сообщения в `main`.

### Requirements

**Метки отката**
- R1. На origin есть 6 аннотированных меток с именами и полными SHA из таблицы `docs/CHECKPOINTS.md` (e3, e1, e2, e4, e5, e6).
- R2. Существующая метка `checkpoint/2026-09-30-lidy-sdelki` не меняется.

**Ветка**
- R3. Удалённой ветки `claude/wonderful-pasteur-7tzxeu` на origin нет.

**Сообщение**
- R4. В `main` нет файла `docs/SOOBSHCHENIE-AGENTAM.md` и строки со ссылкой на него в `docs/ppo/HANDOFF.md`.
- R5. `docs/CHECKPOINTS.md` получает только новую строку-примечание внизу; строки таблицы не правятся (правило реестра «только дописывается»).

### Scope Boundaries

- PR №4 Codex не трогаем: слияние ждёт отдельного «да» владельца.
- Ветки `claude-web/*` (12 шт., слиты) не удаляем: удаление чужих веток — только словом владельца.
- Локальная ветка `codex/8b44-eurosteklo` с 21 коммитом от 28.09 не пушится (П9).

---

## Planning Contract

### Key Technical Decisions

- KTD1. **Метки по реестру, а не по файлу сообщения.** Сообщение даёт команды для 4 меток; реестр — для 6 (добавлены e5, e6). Реестр — источник истины по SHA (правило в шапке `docs/CHECKPOINTS.md`). (session-settled: user-approved — выбрано вместо «только 4 метки из сообщения»: в отчёте 01.10 предложено 6, владелец ответил «да»)
- KTD2. **Push меток по одной** (`git push origin <метка>`), не `--tags`. Закон репозиториев запрещает массовый push больше 3 ref.
- KTD3. **Удаление файла сообщения — через ветку и PR** `claude/lq9-soobshchenie-vypolneno` → `main`, merge с `--match-head-commit`. Прямой push в `main` запрещён законом веток.

### Assumptions

- Строка `HANDOFF.md:5` — единственная ссылка на файл сообщения в `main` (проверено `git grep SOOBSHCHENIE origin/main` 01.10: 1 совпадение).

---

## Implementation Units

### U1. Метки отката e1–e6

- **Goal:** 6 аннотированных меток на origin.
- **Requirements:** R1, R2. KTD1, KTD2.
- **Dependencies:** нет.
- **Files:** нет (только refs).
- **Approach:**
  1. Для каждой строки e3, e1, e2, e4, e5, e6 таблицы `docs/CHECKPOINTS.md` проверить, что SHA — предок `origin/main`.
  2. Создать аннотированную метку. Имя — текст в обратных кавычках из столбца «Метка», без приписки. Сообщение — `e<N>: ` + начало столбца «Что зафиксировано».
  3. Отправить каждую метку отдельным push.
- **Test scenarios:**
  - `git ls-remote --tags origin 'checkpoint/*'` показывает 7 меток.
  - Разыменованный SHA (`^{}`) каждой метки равен полному SHA из реестра.
  - Метка `lidy-sdelki` указывает на `575a157` как и до работы.
- **Verification:** 7 меток, 6 новых SHA совпадают с реестром.

### U2. Удаление пустой ветки

- **Goal:** ветки `claude/wonderful-pasteur-7tzxeu` нет на origin.
- **Requirements:** R3.
- **Dependencies:** нет.
- **Files:** нет.
- **Approach:**
  1. `git fetch --prune origin` непосредственно перед удалением.
  2. SHA ветки из `git ls-remote --heads origin` равен `575a157909476c9e55724ac1a28b78a4fb356321`; иначе стоп.
  3. `git log origin/main..origin/claude/wonderful-pasteur-7tzxeu` пуст; иначе стоп.
  4. Удалить удалённую ветку одним push.
- **Test scenarios:**
  - До удаления, после fetch: SHA ветки = `575a157…`, коммитов вне `main` — 0.
  - После: `git ls-remote --heads origin claude/wonderful-pasteur-7tzxeu` — 0 строк.
  - Коммит `575a157` по-прежнему достижим из `main` и метки `lidy-sdelki`.
- **Verification:** 0 строк в `ls-remote`.

### U3. Удаление файла сообщения через PR

- **Goal:** выполненное сообщение убрано из `main`.
- **Requirements:** R4, R5. KTD3.
- **Dependencies:** U1, U2 (сообщение удаляется после выполнения его поручений).
- **Files:** `docs/SOOBSHCHENIE-AGENTAM.md` (удалить), `docs/ppo/HANDOFF.md` (удалить строку 5), `docs/CHECKPOINTS.md` (дописать примечание о 6 метках).
- **Approach:**
  1. Удалить файл сообщения и строку-ссылку в `HANDOFF.md`.
  2. Дописать в конец `CHECKPOINTS.md` абзац: 6 имён меток поставлены CLI-агентом 01.10; `git ls-remote --tags origin 'checkpoint/*'` показывает 7; приписки «метку ставит CLI-агент» в строках таблицы и абзац о недоступности меток утратили силу. Строки таблицы не править.
  3. gitleaks, коммит, push ветки, PR, merge.
- **Test scenarios:**
  - `git grep -n SOOBSHCHENIE origin/main` после merge — 0 строк.
  - `git diff 21125b3 <merge-SHA> -- docs/CHECKPOINTS.md` — только добавленные строки (база — `main` на старте работы).
  - `gitleaks` — 0 находок.
- **Verification:** PR в статусе MERGED, 0 совпадений `SOOBSHCHENIE`.

---

## Verification Contract

| Проверка | Команда | Ожидание |
|---|---|---|
| Метки | `git ls-remote --tags origin 'checkpoint/*'` | 7 меток, SHA `^{}` = реестр |
| Ветка | `git ls-remote --heads origin claude/wonderful-pasteur-7tzxeu` | 0 строк |
| Сообщение | `git grep -n SOOBSHCHENIE origin/main` | 0 строк |
| Реестр | `git diff 21125b3 <merge-SHA> -- docs/CHECKPOINTS.md` | только `+` строки |
| Секреты | `gitleaks detect` на ветке | 0 находок |

## Definition of Done

- U1–U3 прошли свои Verification.
- PR слит, рабочая ветка и worktree `.worktrees/claude/lq9` удалены.
- Атом `eurosteklo-lq9` закрыт с командами и цифрами в reason.
