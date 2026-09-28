# Implementation Plan: Доработка BPMN-схемы DwW по замечаниям владельца

**Branch**: `codex/8b44-eurosteklo` | **Date**: 2026-09-28 | **Spec**: [spec.md](spec.md)
**Input**: `specs/004-blok-skhema-zamechaniya/spec.md`; решение — `docs/plans/2026-09-28-1938-fix-dww-owner-remarks-plan.md` (вариант B)

## Summary

Схема строится готовым решением drawio-ai-kit по его навыку `drawio-bpmn`: `scaffold bpmn/build_bpmn.mjs` → `build.mjs` (только разница: содержание текущей схемы и `data.md`) → `node build.mjs` → `validate`. Штатно: полные слова, значки `document` в дорожке «Клиент» с пунктиром, номера 1–9 (`step`), список «Проход с клиентом» и строка источника. Единственная правка поверх набора — шрифт ≥16 px и чёрный цвет (выбор владельца 28.09 «Набор + шрифт и цвет»). Затем XML переносится в `view.html` и объект перезаписывается.

## Technical Context

**Language/Version**: скрипт сборки набора `build.mjs` (Node, API `builder.mjs`/`bpmn.mjs`/`layout-engine.mjs`) → XML draw.io; страница — viewer diagrams.net (`data-mxgraph`)
**Primary Dependencies**: `clients/tools/drawio-ai-kit` (CLI `node …/src/cli.mjs`: `scaffold`, `search`, `principles`, `validate`) — установлен, spec 003 А1; `drawio-ai` не в PATH, draw.io desktop нет → `render` недоступен
**Storage**: файлы в git проекта; публикация — MinIO `b244minio/files/20260928-181501-view.html`
**Testing**: `validate` (ok, 0 warnings), issues из `node build.mjs` = пусто, grep-счётчики SC-001…SC-005, скриншот google-chrome headless 1920 px
**Target Platform**: браузер на экране владельца (показ клиенту), ширина 1920 px
**Project Type**: документ (визуальная схема процесса)
**Performance Goals**: нет
**Constraints**: не пересобирать; содержание процесса не менять (FR-011); ссылка прежняя (FR-010); код/XML правит только code-channel (конституция II)
**Scale/Scope**: 1 схема, 65 подписей, 9 проблемных мест, 6 документов клиента; contracts/ не создаётся — внешний интерфейс один (ссылка b244.ru/DwW), контракт = FR-010

## Constitution Check

| Принцип | Проверка | Итог |
|---|---|---|
| I. Только готовые решения | сборка — штатный порядок drawio-ai-kit (scaffold → build.mjs → validate); одна правка поверх — шрифт и цвет, выбор владельца 28.09 | PASS |
| II. Код пишут только внешние каналы | правка XML/HTML — только `code-channel auto` в Workflow code-atom, ТЗ после ce-doc-review | PASS |
| III. Docs-first и детерминизм | spec → plan → tasks → ТЗ; проверки — фиксированные команды quickstart | PASS |
| IV. Тестирование, вердикт цитатой | каждый SC — команда + вывод в `bd close` | PASS |
| V. Фиксация: память + документ + git | коммит на атом, push в `arwoxbx24/eurosteklo` | PASS |
| Закон дробления (`CLAUDE.md` проекта) | правки одного файла `.drawio` нельзя вести параллельно без конфликта | ОТКЛОНЕНИЕ, обосновано: атомы правки идут последовательно по одному файлу; параллельно — проверки (validate, grep, скриншот) и ревью |

Повторная проверка после дизайна: без изменений.

## Project Structure

### Documentation (this feature)

```text
specs/004-blok-skhema-zamechaniya/
├── spec.md
├── plan.md          # этот файл
├── research.md
├── data-model.md
├── quickstart.md
├── checklists/requirements.md
└── tasks.md         # speckit-tasks
```

### Source (правимые файлы)

```text
docs/process/bpmn/
├── build.mjs                   # новый: scaffold набора + разница (атомы 1–3)
├── eurosteklo_process.drawio   # вывод build.mjs (перезапись)
├── view.html                   # перенос XML в data-mxgraph (атом 4)
└── eurosteklo_process.png      # снимок chrome (атом 4)
```

**Structure Decision**: правятся только файлы в `docs/process/bpmn/`; `data.md`, `tz-fix*.md`, варианты v1–v5 не трогаются.

## Complexity Tracking

| Нарушение | Зачем | Почему не проще |
|---|---|---|
| Последовательные атомы вместо ≥3 параллельных | один файл `build.mjs` | параллельная правка одного скрипта даёт конфликт слияния; параллелятся проверки |
| Правка шрифта и цвета поверх набора | замечания S2-01, S2-13; в API набора нет опции | выбор владельца 28.09 «Набор + шрифт и цвет» |
