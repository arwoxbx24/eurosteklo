# Implementation Plan: Доработка BPMN-схемы DwW по замечаниям владельца

**Branch**: `codex/8b44-eurosteklo` | **Date**: 2026-09-28 | **Spec**: [spec.md](spec.md)
**Input**: `specs/004-blok-skhema-zamechaniya/spec.md`; решение — `docs/plans/2026-09-28-1938-fix-dww-owner-remarks-plan.md` (вариант B)

## Summary

Точечная правка оформления существующей схемы `docs/process/bpmn/eurosteklo_process.drawio` (шрифт ≥16 px, чёрный + один красный, полные слова, значки документов клиента с пунктиром, красные номера 1–9 вместо заметок, список «Проход с клиентом» и строка источника внизу полотна), затем перенос того же XML в `view.html` и перезапись опубликованного объекта. Генератор не восстанавливается и не запускается.

## Technical Context

**Language/Version**: XML draw.io (mxGraphModel) + статичный HTML с viewer diagrams.net (`viewer-static.min.js`, атрибут `data-mxgraph`)
**Primary Dependencies**: `clients/tools/drawio-ai-kit` (CLI `validate`, `audit`, `render`) — установлен, spec 003 А1
**Storage**: файлы в git проекта; публикация — MinIO `b244minio/files/20260928-181501-view.html`
**Testing**: `drawio-ai-kit validate` (ok, 0 warnings), grep-счётчики по SC-001…SC-005, скриншот google-chrome headless 1920 px + `render --check`
**Target Platform**: браузер на экране владельца (показ клиенту), ширина 1920 px
**Project Type**: документ (визуальная схема процесса)
**Performance Goals**: нет
**Constraints**: не пересобирать; содержание процесса не менять (FR-011); ссылка прежняя (FR-010); код/XML правит только code-channel (конституция II)
**Scale/Scope**: 1 схема, 65 подписей, 9 проблемных мест, 6 документов клиента; contracts/ не создаётся — внешний интерфейс один (ссылка b244.ru/DwW), контракт = FR-010

## Constitution Check

| Принцип | Проверка | Итог |
|---|---|---|
| I. Только готовые решения | viewer diagrams.net и drawio-ai-kit — готовые; свой генератор не пишется | PASS |
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
├── eurosteklo_process.drawio   # правка оформления (атомы 1–4)
├── view.html                   # перенос XML в data-mxgraph (атом 5)
└── eurosteklo_process.png      # новый проверенный снимок (атом 5)
```

**Structure Decision**: правятся только три файла в `docs/process/bpmn/`; `data.md`, `tz-fix*.md`, варианты v1–v5 не трогаются.

## Complexity Tracking

| Нарушение | Зачем | Почему не проще |
|---|---|---|
| Последовательные атомы вместо ≥3 параллельных | один файл `.drawio` | параллельная правка одного XML даёт конфликт слияния; параллелятся проверки |
