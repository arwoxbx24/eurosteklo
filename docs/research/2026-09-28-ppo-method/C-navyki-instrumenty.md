# Блок C — навыки и инструменты для цикла ППО → спецификация → Б24

Атом: eurosteklo-k5d | исполнитель: субагент analyst (sonnet), read-only, 28.09.2026; перепроверка главным агентом — помечено «проверено».

## Этап цикла → что есть → пробел
| этап | есть (`.claude/skills/` проекта, `disable-model-invocation: true`) | пробел |
|---|---|---|
| сбор требований, интервью | requirements-elicitation, meeting-facilitation | — |
| роли, RACI | stakeholder-analysis | — |
| AS-IS | process-mapping, process-states, ba-value-streams | — |
| TO-BE | process-optimization, process-mapping | — |
| модель понятий, возможности | ba-concept-model, ba-capability-mapping, ba-taxonomy-standard (PlausibleBA, CC BY-SA 4.0) | — |
| разрывы | gap-analysis | — |
| валидация требований | requirements-validation | — |
| архитектура (C4) | c4-model (MIT) | — |
| схемы | `clients/tools/drawio-ai-kit` | — |
| **архитектура под облачный Б24** | нет навыка | **пробел** |
| **чтение конфигурации портала** (воронки, стадии, поля, смарт-процессы, роботы, БП, права) | выгрузка `client-materials/private/b24-export/` (companies, contacts, deals, meta, index.json — проверено `ls`); MCP `claude.ai B24` (сделки, задачи, воронки, стадии) | **пробел**: роботы, БП, смарт-процессы, права — нет инструмента чтения |

## Битрикс24
- Подключён `claude.ai B24` (`https://mcp.bitrix24.tech/mcp`, `claude mcp list` → Connected): CRM/задачи/структура; методов чтения роботов, БП, прав нет (по списку инструментов сессии).
- Официальный dev-MCP (apidocs.bitrix24.ru/ai-tools/mcp.html, цитата субагента): «Сервер отдаёт только документацию: доступа к данным Битрикс24 у него нет» — адрес `https://mcp-dev.bitrix24.tech/mcp`. Годится как справочник REST, не как источник данных портала.
- Ранее отклонены (`docs/research/2026-09-28-skills-candidates.md`): okou-ai bitrix (пустой HEAD, запись в Б24), bitrix-framework-skills (CMS, не CRM), membranedev 1c (данные третьей стороне).

## Кандидаты (не установлены, лицензии не проверены)
1. takusaotome/claude-skills-library `skills/business-analyst` — BABOK v3, 6 областей. Дублирует установленное.
2. GiangGiangTran/ba-skills — BABOK+PMBOK+IEEE 830. Дублирует.
3. GSkuza/BABOK_ANALYST — 8 стадий BABOK до бизнес-кейса. Частично новое (бизнес-кейс/ROI).
4. vrtalex/bitrix24-skill — webhook/OAuth/события REST Б24; инфраструктура, не архитектура CRM.
5. soajv/bitrix24-openlines-skill — только открытые линии.

## Размещение навыков
- Факт (проверено): `git -C eurosteklo rev-parse --show-toplevel` → `/root/workspaces/projects/clients/eurosteklo` (свой репозиторий); `git -C clients rev-parse --show-toplevel` → `/root/workspaces/projects` (другой репозиторий).
- Документация (code.claude.com/docs/en/skills): «Claude Code loads project skills from `.claude/skills/` in the directory where you start it and in every parent directory up to the repository root».
- Вывод: навыки — только в `.claude/skills` этой директории, никуда не выносить (закон жёсткого контура, `CLAUDE.md`).
