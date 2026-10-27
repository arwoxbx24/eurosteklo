---
artifact_contract: "ce-handoff/v1"
created_at: "2026-10-06T09:13:50.200946+00:00"
title: "Спецификация передачи: таймауты native Codex Hooks"
summary: "Диагностика не воспроизвела таймаут; передача атрибуции и исправления другому Codex без вмешательства в клиентский проект."
keywords: ["codex", "hooks", "context-guard", "timeout", "eurosteklo"]
cwd: "/root/workspaces/projects/clients/eurosteklo"
resume_focus: "Установить фактический callback, вызывающий timeout, и выполнить доказанное штатное исправление."
---

# Техническая спецификация и контрольная точка

## 1. Решение владельца и разделение ответственности

Владелец в текущей сессии передаёт проблему Codex Hooks другому агенту Codex. Этот координатор прекращает исследования хуков и остаётся в проекте Евростекло. Документ — передача фактов и требований, не разрешение на изменение защищённых настроек.

Исходный запрос: устранить повторяющиеся сообщения `Hook failed` / `hook timed out after 10s`, каскад ошибок чтения навыков и задержки работы. Подтверждённого общего первопричинного объяснения пока нет. Нельзя приписывать все задержки одному плагину или утверждать, что весь Codex сломан.

Цель принимающего агента: установить конкретный ошибочный callback и причину, выполнить минимальное штатное исправление в своём разрешённом контуре, проверить реальное выполнение и сохранность защиты. Цель-финиш: ошибочный сценарий исправлен, проверен измеряемым native runtime результатом и не повреждает клиентские материалы.

Передача документа не означает, что ошибка исправлена, новый агент запущен или задача им принята. Владелец сам передаёт этот файл.

## 2. Идентификаторы и авторитетные источники

- Исходная сессия: `01a10c0c-746d-7c51-9a85-9046d5bbbf17`.
- Канонический клиентский корень: `/root/workspaces/projects/clients/eurosteklo`.
- Открытый исходный Beads-атом: `eurosteklo-37m`.
- Точное имя: `[CODEX-eurosteklo-hooks-01a10c0c-746d-7c51-9a85-9046d5bbbf17]`.
- Статус при передаче: `in_progress`; ремонт не принят. Чужой атом не переименовывать и не переназначать автоматически.
- Регламент: ближайшие действующие `AGENTS.md`, `/root/workspaces/projects/AGENTS.md`, `/root/.codex/rules/owner-operations.md` (только применимые разделы), `/root/.codex/skills/csb/references/alignment.md`.
- Официальная документация: https://learn.chatgpt.com/docs/hooks — схема Hooks, timeout, trust и синхронное исполнение.
- Поставщик Context Guard: https://github.com/GreenLv/codex-context-guard/releases/tag/v0.15.1 — установленная версия совпала с последним опубликованным релизом при проверке.

Все пути ниже к Codex runtime — машинно-локальные. Файл остаётся в закрытой производной зоне клиента; не отправлять клиенту и не публиковать. Секретов и текста консультаций в нём нет. Пути транскрипта и runtime не являются переносимой резервной копией; на другом сервере они могут отсутствовать.

## 3. Подтверждённые данные и предел доказательства

| Утверждение | Наблюдение | Статус и предел |
|---|---|---|
| Владелец видит таймауты | В переписке повторяется `Hook failed` / `hook timed out after 10s` | PROVEN: сообщение получено; конкретный handler не указан |
| Два Stop-handler имеют лимит 10 секунд | Global goal guard и плагин Context Guard настроены на timeout 10 | PROVEN: конфигурация; не доказательство причины |
| Goal guard выполнился на сохранённом реальном ответе | 0.180 с, exit 0, пустой stdout | PROVEN: один replay; не гарантия всех native вызовов |
| Context Guard Stop выполнился на сохранённом реальном ответе | 1.123 с, exit 0, response keys [], stderr 0 bytes | PROVEN: один replay; timeout не воспроизведён |
| Native diagnose с правильной директорией runtime выполнился | 2.131 с, exit 0 | PROVEN: diagnose; это не Stop |
| Profiling diagnose нашёл дорогую проекцию | wall 4.578 с, `current_core_projections` cumulative 3.441 с | PROVEN: профилированный diagnose; нельзя подменять им Stop timing |
| Исправление внесено | Нет изменений hook config/source/vendor | PROVEN: исправления в этом исследовании не выполнялись |
| Точный источник native timeout | Callback trace с именем failed handler не получен | UNVERIFIED |
| Задержки 5–10 минут вызваны только Hooks | Нет данных с разложением host/model/tool времени | UNVERIFIED |

Последний replay — исторический настоящий ответ против текущего состояния. Это диагностическая проверка, не полноценная приёмка актуального host lifecycle. Не объявлять FAIL/PASS всей системы по одному replay.

## 4. Native архитектура и конфигурация

### 4.1 Global goal guard

Машинно-локальная конфигурация: `/root/.codex/hooks.json`.

- `SessionStart` и `Stop`: `/usr/bin/python3 /root/.codex/hooks/codex-goal-guard.py`, timeout 10.
- `PreToolUse` RepoWise rewrite: timeout 5.
- Другие Hooks Beads существуют; полной атрибуции сбоя по ним нет.
- Зафиксированный mtime_ns hooks.json: `1791215788238732445`; это не доказательство автора изменений.

Источник goal guard: `/root/.codex/hooks/codex-goal-guard.py`, около 99 строк.

- Проверка открытых задач: `bd list --status in_progress --assignee Codex --limit 0 --json`.
- Дочерний процесс: env `BEADS_ACTOR=Codex`, timeout 3 секунды.
- Hardcoded `ROOT=/root/workspaces/projects` вместо корня выбранного клиента — отдельный найденный риск выбора ledger, но причина timeout не доказана.
- Есть обработка `stop_hook_active`, исключений и счётчика через flock; управление счётчиком не трогали.
- Replay этого источника завершился за 0.180 секунды, без решения о блокировке.

### 4.2 Context Guard

Установленный vendor root:
`/root/.codex/plugins/cache/codex-context-guard/context-guard/0.15.1`.

- Stop и большинство hook событий: timeout 10; PreCompact 15; SessionEnd 3.
- Native bootstrap: `scripts/run_context_guard.sh hook` → `cg_hook.py` → `context_guard.py`.
- Bootstrap выбирает доступный Python; hook router использует облегчённый запуск, тяжёлый core выполняет рабочую логику.
- В router fallback subprocess timeout 120 не отменяет host timeout 10.
- Сессионная блокировка core: обычно до 5 секунд; SessionEnd имеет меньший предел. Конкуренция за lock в момент реального сбоя не измерена.
- Директория data определяется `CONTEXT_GUARD_DATA_DIR`, затем plugin env; без них возможен другой default `~/.codex/context-guard`.

Машинно-локальная фактическая база:
`/root/.codex/plugins/data/context-guard-codex-context-guard`.

Состояние исходной сессии:
`/root/.codex/plugins/data/context-guard-codex-context-guard/sessions-v2/01a10c0c-746d-7c51-9a85-9046d5bbbf17/`.

Размер state.json при одном измерении около 896478 bytes; состояние меняется при native событиях. Это снимок, не текущий размер и не порог отказа.

Источник heavy core: `scripts/context_guard.py`.

Ориентиры установленных исходников (номера могут меняться с версией):
- `handle_stop` ~20439: active/integrity checks, EvaluationContext, копия состояния, классификация решения, проекции, сохранение.
- `finish` ~20681; save state ~20735 и отдельная ранняя ветка ~20668.
- `current_feedback_view` ~16244.
- `current_core_projections` ~12010.
- `_current_action_basis` ~11045.
- `diagnose` ~22197.

Профиль diagnose:

| Функция | Calls | Cumulative seconds |
|---|---:|---:|
| current_feedback_view | — | 3.540 |
| current_core_projections | — | 3.441 |
| _current_action_basis | 1408 | 3.372 |
| cg_instruction.fragments | 15275 | 2.015 |
| _action_source_clauses | 1408 | 1.240 |
| _action_source_filter | 1408 | 1.010 |
| action_search | 9670 | 0.860 |
| action_matches | 9730 | 0.854 |

Cumulative значения вложены друг в друга: не складывать их как независимое время. Profiler добавляет overhead. Это кандидат для проверки, не доказанный дефект.

## 5. Входные данные replay и уже сделанные ошибки

Машинно-локальный transcript:
`/root/.codex/sessions/2026/10/05/rollout-2026-10-05T15-31-45-01a10c0c-746d-7c51-9a85-9046d5bbbf17.jsonl`.

Размер на момент чтения: 40472032 bytes; текущий размер может отличаться. Не загружать весь transcript в модель. Для новой проверки сначала использовать narrow native сведения; никакой повторной полной индексации клиентских консультаций.

Правильная схема сохранённого ответа:
- событие `response_item`;
- `payload.type=message`, `payload.role=assistant`;
- **`payload.phase=final_answer`**, не `final`;
- `payload.content[].type=output_text`;
- turn_id — из ближайшего соответствующего `turn_context.payload.turn_id`.

Два первых preflight прекращены из-за ошибочных предположений о схеме: `phase=final`, затем поиск отсутствующего `event_msg agent_message`. Callback в этих двух попытках НЕ исполнялся. Не считать их двумя reproduced timeout и не повторять эти selectors.

Успешный Stop replay передавал настоящий сохранённый ответ и настоящий turn_id:

```json
{
  "hook_event_name": "Stop",
  "session_id": "01a10c0c-746d-7c51-9a85-9046d5bbbf17",
  "cwd": "/root/workspaces/projects/clients/eurosteklo",
  "transcript_path": "<фактический локальный transcript>",
  "turn_id": "<turn_id сохранённого реального ответа>",
  "stop_hook_active": false,
  "last_assistant_message": "<реальный ответ; не выдумывать completion>"
}
```

Context Guard env: `PLUGIN_ROOT` = установленный vendor root; `PLUGIN_DATA` и `CONTEXT_GUARD_DATA_DIR` = фактическая база выше. Запускался штатный `sh <vendor-root>/scripts/run_context_guard.sh hook`; stdin JSON; stdout/stderr удерживались локально. Предел диагностического subprocess — 15 секунд. Исполнение: 1.123 секунды, exit 0, пустой ответ. Обычный native handler мог сохранить своё runtime состояние. Vendor/config не изменялись.

Первый diagnose без явной фактической data-dir прочитал другой default: 0.46 с и пустые decisions. Эта попытка НЕ является доказательством состояния живой сессии. Использовать правильную env/data-dir.

## 6. Логи и проверенные источники

- `/root/.codex/log` был пуст; usable codex-tui.log не найден.
- `/root/.codex/logs_2.sqlite` читалась в режиме SQLite `mode=ro` / `query_only`; релевантного failed-hook callback trace не найдено.
- Таблица `logs`: id, ts, ts_nanos, level, target, feedback_log_body, module_path, file, line, thread_id, process_uuid, estimated_bytes.
- Broad поиск `hook timeout` возвращал чужие исторические/diff записи. Не повторять широкое чтение базы и не принимать чужие ошибки за эту сессию.
- В state_5.sqlite / thread_history_1.sqlite hook tables не обнаружены.
- Последняя видимая до replay Stop decision: `2026-10-06T08:09:08.334479Z`; это только snapshot.
- Отдельный clipboard/X11 warning не доказывает причину зависания Hooks.

Журнал исходной работы и результаты читать в `env BEADS_ACTOR=Codex bd show eurosteklo-37m --json` из клиентского корня. Старый HANDOFF-CLAUDE был записью в notes, не реально выполненной передачей Claude и не вторым мнением по hook incident.

## 7. Отдельная ошибка каталогов навыков

Два чтения CE `ce-plan` / `ce-brainstorm` по пути версии 3.30.3 завершились exit 1. Реальный cache содержал 3.30.4; соответствующие SKILL.md затем прочитаны успешно.

Актуальный найденный каталог:
`/root/.codex/plugins/cache/compound-engineering-plugin/compound-engineering/3.30.4/skills`.

Это доказанное несовпадение старого пути каталога с установленным пакетом. Кто обновил пакет и связано ли это с Hook timeout — не установлено. Координатор пакет не обновлял. Не смешивать path-read failure и runtime timeout как одну доказанную причину.

## 8. Рабочие гипотезы для принимающего агента

1. INFERRED: реальное событие имеет другой вход/объём/состояние, чем replay; нужен конкретный failed callback.
2. UNVERIFIED: lock contention или конкурентные native handlers иногда расходуют бюджет.
3. UNVERIFIED: projection hot path длинной сессии создаёт worst-case задержку; профиль diagnose даёт направление, но успешный Stop replay не подтвердил timeout.
4. UNVERIFIED: сбой связан с иным handler/event или host scheduling.
5. UNVERIFIED: часть воспринимаемых 5–10 минут — время модельного рассуждения, не hook execution.

Не выбирать гипотезу как факт до атрибуции. Не обещать, что увеличение timeout устранит первопричину.

## 9. Ограничения и штатный путь

- CE — единственный оркестратор; для подтверждённого ремонта нужен CE/CSB passport: цель, архитектура, scope, шаги, acceptance, rollback.
- Другой агент имеет собственную сессию/атом; не присваивает исходный atom без разрешённого handover. Владелец передаёт саму работу этим документом, техническая процедура actor/handover остаётся регламентной.
- Исходный координатор не создаёт новый paid Codex process ради доказательства. Новую сессию запускает/разрешает владелец; в этой передаче другой агент не был запущен.
- Все Codex `bd` вызовы: `env BEADS_ACTOR=Codex`.
- Код меняется только поддерживаемым `code-channel auto` в разрешённом контуре; этот файл не разрешает vendor source edit.
- Перед конфигурационными правками: rule-author, актуальная официальная документация, собственная зона изменений и native trust.
- Нельзя отключать guards, ставить async для защитного Stop, удалять state/evidence, править immutable installed caches, обходить host gates, менять чужие настройки Claude, массово удалять версии или клонировать вкладки.
- Нельзя тратить деньги, запускать model eval/paid verification, менять права/production без действующего явного разрешения.
- Не делать blind reinstall: installed 0.15.1 совпала с vendor latest. Native installer не доказывает trust/runtime acceptance; активные старые cache могут требоваться другим задачам.
- Runtime/private state не публикуется и не включается в Git. Оригиналы клиента, общая evidence DB, Word и карты не изменяются ради ремонта Hooks.
- Конфигурация — не исполнение; replay — не актуальный host lifecycle; source-only benchmark — не приёмка установки.

Согласно официальной Hooks документации совпадающие hooks из нескольких источников могут выполняться одновременно. Добавление user hook не является override vendor handler. Async hook не подходит для поведения, которое должно блокировать/управлять завершением.

## 10. Порядок выполнения и приёмка

### Шаг 1. Атрибуция

Принимающий агент сверяет свои полномочия и native hook/trust listing. Получает фактическое имя event, matcher, command, plugin/config source, начало/окончание/elapsed, exit и timeout для конкретного сбоя. Использует доступную штатную поверхность `/hooks` и narrowly scoped журналы, не запускает новую модель исключительно ради проверки. Если такой trace недоступен — фиксирует точный пробел вместо выдуманного root cause.

### Шаг 2. Причина

Сопоставляет failed input с уже успешным replay. Проверяет только названный callback, его lock, data-dir, workload и путь. Одного наблюдения diagnose недостаточно. Не повторяет обзор всех проектов, skills и клиентских записей.

### Шаг 3. Решение

Выбирает минимальную документированную корректировку, только после cause evidence. Формирует точный diff/версию/официальный путь и rollback. При vendor дефекте следует штатному vendor source/issue/release процессу в разрешённой зоне, не патчит установленный immutable cache. При wrong root ledger проверяет правильность выбора Beads отдельно от performance.

### Шаг 4. Приёмка

| ID | Требование | Проверка | Ожидаемый результат |
|---|---|---|---|
| H1 | Назван фактически failed handler | Native event/trace с command, event и elapsed | Атрибуция подтверждена |
| H2 | Причина связана с этим handler | Сравнение failed input/path и cause evidence | Нет подмены диагнозом другого event |
| H3 | Исправление внесено штатно | Scoped diff или native vendor install receipt | Изменение существует, разрешено и обратимо |
| H4 | Ошибочный сценарий отработал | Реальный native callback текущего host, elapsed и exit | Укладывается в действующий budget, без timeout |
| H5 | Защита сохранена | Штатная проверка ветвей разрешённого и запрещённого завершения в разрешённой тестовой зоне | Недопустимое завершение не пропускается; допустимое не блокируется |
| H6 | Проект не повреждён | Scoped readback/hash клиентских артефактов только при затрагивании | Word/evidence/источники сохранены |
| H7 | Нет неподтверждённой сдачи | Requirement→command→output→status | Done только по применимым successful evidence |

Одно изменение — одна затронутая проверка; не повторять полный аудит ради пересказа результата. При неуспехе не закрывать bug как fixed.

### Rollback

До изменения: записать exact old/new field или source version и native restoration method. Откат только своего изменения штатным способом; никакого wipe runtime, удаления guard state, переписывания main или чужого revert. После rollback проверить тот же callback и защитные условия. В исходном исследовании rollback не требуется: hook/config/vendor изменений нет.

## 11. Евростекло — независимая работа координатора

Клиентская форма уже находится непосредственно в каноническом корне:
`/root/workspaces/projects/clients/eurosteklo/Евростекло-уточнение-процесса.docx`.

Рабочий документ:
`docs/review/2026-10-05-consistency/Евростекло-уточнение-процесса.docx`.

Ранее проверенный размер 39707 bytes; SHA-256 `1d6e32b0e7612e986370770feba82d11cbdfd8624f4cfe00c5c39ed8b8db4547`.

Форма содержит 18 уточнений. Ответы клиента ещё не получены; разработка клиентского ТЗ требует отдельного одобрения. Полную гарантию неизвестного будущего ТЗ из успешного replay Hooks вывести нельзя.

Общая база: `client-materials/private/analysis/evidence-crv8.sqlite3`; при prior acceptance integrity ok, foreign-key errors 0. Не редактировать и не читать содержимое для диагностики Hooks.

Delivery receipt: `client-materials/private/analysis/delivery-crv10/receipt.json` — источник prior delivery проверки. Исходный клиентский атом `eurosteklo-a58` закрыт; это не закрытие `eurosteklo-37m`.

## 12. Контрольная точка передачи

На момент составления: успешные replay за 0.180 и 1.123 секунды; фактический timeout не атрибутирован; hooks не исправлялись; закрытые клиентские материалы не менялись. Новых агентов, вкладок, worktrees и платных проверок координатор не запускает. Ремонт отделён от передачи спецификации. Дальнейшее исполнение этого incident — принимающим агентом по указанию владельца.
