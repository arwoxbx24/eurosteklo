# Поиск навыков (skills) для проекта «Евростекло»

Дата: 2026-09-28 · Источник задания: ТЗ dcfg-9itnf · Тип задачи: исследование (кода нет), пишется только файл результата.

## Ограничения среды выполнения (честная фиксация)

Песочница OpenCode блокирует часть команд из ТЗ (подтверждено попытками запуска, вывод — отказ уровня permission):

- `jq -r '...' <marketplace.json>` — ЗАБЛОКИРОВАНО (bash deny). Заменено эквивалентным `grep` по тем же `marketplace.json` (claude-plugins-official и claude-community), структура полей `name / description / source.url / source.sha` извлечена из JSON напрямую.
- `DISABLE_TELEMETRY=1 /root/workspaces/tools/skill-search/node_modules/.bin/skills find <слова>` — ЗАБЛОКИРОВАНО (bash deny). Не выполнялось; источник 2 в таблице отсутствует.
- `git clone --depth 1 … /tmp/skills/<имя>` — ЗАБЛОКИРОВАНО (bash deny). Новые кандидаты НЕ клонированы; клоны переиспользованы из существующих `/tmp/skills` (plausible-ba, decision-council).
- `git rev-parse HEAD` внутри `/tmp/skills` — ЗАБЛОКИРОВАНО (external_directory). SHA взяты из `marketplace.json` (пин маркетплейса, поле `source.sha`).
- Анализ клонов (`ls`, `cat`, `grep` по SKILL.md, лицензии) — ВЫПОЛНЕН локально.

Классы 4 (Bitrix24), 5 (BPMN/регламенты AS-IS/TO-BE), 6 (1С) — в обоих маркетплейсах по строке поиска найдено 0 совпадений. Это подтверждено `grep -in`: `bitrix` → 0, `bpmn` → 0, `1c`/`1с` → 0. Отдельного навыка под эти классы нет → «нет навыка».

## Таблица кандидатов

Легенда: «1» = marketplace-поиск (через grep, jq заблокирован), «3» = локальный клон в /tmp/skills. «2» = skill-search — не выполнялось (заблокировано).

| класс | имя | источник | URL репо | путь в репо | SHA | лицензия | скрипты да/нет | grep-совпадений | риск | вердикт |
|---|---|---|---|---|---|---|---|---|---|---|
| 1. Бизнес-анализ (BABOK) | plausible-ba | 1+3 | https://github.com/plausibleba/ba-skills.git | skills/ba-capability-mapping, skills/ba-taxonomy-standard | c79565fb5a88c511740a3537d6eb534053624ca4 | CC BY-SA 4.0 (проверено в клоне) | нет (только .md) | ba-cap-mapping: 1 (URL в md), taxonomy: 0 | низкий | РЕКОМЕНДУЮ |
| 2. Системный анализ (спека/SRS) | adversarial-spec | 1 | https://github.com/zscole/adversarial-spec.git | (корень) | f90cf0c36c3999b8dc272c9c06dee9846076f369 | не проверено (клон заблокирован) | — | — | низкий-средний | НЕТ (частично): дебаты мультимодельные по спеке, не полный SRS; не клонирован |
| 2. Системный анализ (спека/SRS) | groundwork | 1 | https://github.com/etr/groundwork.git | (корень) | 7bde6d490ad163574aecf3fd9025cf5d1380e0fa | не проверено (клон заблокирован) | — | — | средний | НЕТ (частично): dev-workflow (EARS), не системный анализ под требования клиента; не клонирован |
| 3. Архитектурный анализ (C4) | c4m | 1 | https://github.com/cheriftj/c4-model-skill.git | (корень) | 5b24dda00b38a402da59237a8b8685aaa588a07e | не проверено (клон заблокирован) | — | — | низкий | РЕКОМЕНДУЮ (C4-модели + ADR-режим); не клонирован |
| 3. Архитектурный анализ (ADR) | adr-creator | 1 | https://github.com/barnburner121/claude-plugin-marketplace.git | generated-plugins/adr-creator (git-subdir) | 5f6b5d32d9f457dc9c2c7c0fb1d67dffc9140f33 | не проверено (клон заблокирован) | — | — | низкий | РЕКОМЕНДУЮ (ADR); не клонирован |
| 4. Bitrix24 (CRM/воронки/роботы/БП/REST) | — | 1 | — | — | — | — | — | — | — | нет навыка: Bitrix24 (0 совпадений по строке `bitrix` в обоих маркетплейсах) |
| 5. Моделирование БП (BPMN/AS-IS/TO-BE) | — | 1 | — | — | — | — | — | — | — | нет навыка: BPMN (0 совпадений по строке `bpmn`; SAP/Conductor — инфраструктура, не BPMN-модели) |
| 6. 1С (интеграция 1С↔Б24) | — | 1 | — | — | — | — | — | — | — | нет навыка: 1С (0 совпадений по `1c`/`1с`) |
| 7. Документация (проектная / клиенту) | make-documentation | 1 | https://github.com/maximilianozurita/makeDoc.git | (корень) | b82baa1452f5b24f271c77b4601c1d69a643ac58 | не проверено (клон заблокирован) | — | — | низкий | НЕТ (частично): тех. документация GitHub, не проектная документация для клиента |
| 7. Документация (проектная / клиенту) | diataxis | 1 | https://github.com/HRSAndrabi/diataxis.git | (корень) | 0907a2a7c0bf5c12be99ba74b46576b09184d988 | не проверено (клон заблокирован) | — | — | низкий | НЕТ (частично): структурирование тех. документации, не презентация клиенту |
| 8. Контроль противоречий / критика | decision-council | 1+3 | https://github.com/fusion-software-ltd/decision-council.git | skills/ (configure…status), agents/, hooks/ | a9c9d58165d471d445cc3833dbbdc44abdf60340 | proprietary (plugin.json; проверено в клоне) | нет (агенты .md, hooks.json) | 0 по всем SKILL.md | средний (лицензия proprietary) | РЕКОМЕНДУЮ |
| 8. Контроль противоречий / критика | claude-perfectionist | 1 | https://github.com/into-the-intraverse/claude-perfectionist.git | (корень) | d12afb36ace6a73a2b804b388aa9c2f11191c5b0 | не проверено (клон заблокирован) | — | — | средний | НЕТ (частично): противоречия в harness CLAUDE.md, а не в модели знаний клиента |
| 8. Контроль противоречий / критика | adversarial-review | 1 | https://github.com/bobby-beckmann/adversarial-review.git | (корень) | 45e0effc5fcf97544a192ead64afbc00a68fc114 | не проверено (клон заблокирован) | — | — | низкий | НЕТ (частично): review планов/кода (Claude↔Codex), не фактчекинг документа |

## Рекомендованные навыки (≤10, с путём клона)

Клонированы и проверены локально (лежат в `/tmp/skills`):

1. `plausible-ba` → `/tmp/skills/plausible-ba` — класс «Бизнес-анализ» (BABOK, capability map, value stream, артефакты XLSX/HTML). Лицензия CC BY-SA 4.0, скриптов нет.
2. `decision-council` → `/tmp/skills/decision-council` — класс «Контроль противоречий / многоуровневая критика» (совет независимых адвокатов, Mirror «жесткая правда», pre-mortem). Лицензия proprietary, скриптов нет, 0 опасных совпадений в SKILL.md.

Кандидаты, рекомендованные к клонированию, но НЕ клонированные (git clone заблокирован песочницей; путь указан для последующего ручного клонирования):

3. `c4m` → `/tmp/skills/c4m` — архитектурные C4-схемы (Mermaid/Structurizr), есть режим работы с ADR.
4. `adr-creator` → `/tmp/skills/adr-creator` — создание ADR.
5. `adversarial-spec` → `/tmp/skills/adversarial-spec` — уточнение спекуляций/ТЗ через дебаты моделей (самое близкое к «системный анализ»; частичное соответствие).

## Проверка по ТЗ

`grep -c "^|" docs/research/2026-09-28-skills-candidates.md` → счётчик строк таблицы (ожидание ≥8).
`ls /tmp/skills` → `decision-council plausible-ba uupm` (рекомендованные и проверенные клоны: decision-council, plausible-ba; `uupm` — существующий ранее, в рамках данного ТЗ не анализировался).

## Итог главного агента (28.09, источник 2 выполнен вручную: `skills find bitrix|bpmn|1c|business analyst|requirements`)

Установлено в `.claude/skills/` (только проект, `disable-model-invocation: true`, скриптов нет):
- ba-capability-mapping, ba-concept-model, ba-value-streams, ba-taxonomy-standard — plausibleba/ba-skills @ c79565fb, CC BY-SA 4.0. grep: только ссылка на внешний Canvas — данные клиента туда НЕ загружать.
- c4-model — cheriftj/c4-model-skill @ 5b24dda0, MIT. grep: 3 ссылки на документацию.

Отклонено:
- okou-ai/okou-skills@bitrix — в HEAD нет файлов (`git ls-files "*bitrix*"` пусто); по странице skills.sh — вызовы REST по `BITRIX_WEBHOOK_URL`, запись в Б24 запрещена.
- bxmaximum/bitrix-framework-skills — Bitrix Framework (CMS/PHP), не Битрикс24 CRM.
- markdown-viewer/skills@bpmn — в HEAD только `documd-visuals/engines/plantuml-stencils/bpmn.md`, отдельного навыка нет.
- membranedev/application-skills@1c — работа через облачный сервис Membrane с его подключением к учётке; передача данных третьей стороне.
- decision-council — лицензия proprietary + hooks (самописные хуки запрещены). Контроль противоречий — штатные ce-doc-review, speckit-analyze и закон блокировки AGENTS.md.

Нет навыка: Bitrix24 (CRM/БП), BPMN, 1С — работа по официальной документации (Битрикс24 REST, 1С) и закону блокировки AGENTS.md.

## Открытые вопросы / незавершённое

- Источник 2 (skill-search `skills find`) не выполнен: команда заблокирована песочницей. Список кандидатов неполон относительно полного ТЗ.
- Bitrix24, BPMN, 1С: навыков в официальном и community-маркетплейсах не найдено (0 совпадений). Это «нет навыка», а не недосмотр поиска.
- SHA/лицензии/наличие скриптов для неклонированных кандидатов не проверены (клон заблокирован); в таблице помечено «не проверено».
- Для полного результата нужно повторить ТЗ в среде с доступом к `jq`, `skills find` и `git clone`.
