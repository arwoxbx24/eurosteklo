# Удалённые файлы Codex — проверка 2026-10-13

Статус: **PROVEN** для вызова удаления и числа 86; **INFERRED** для полного поимённого состава, восстановленного из команд создания и совпавшего с числом 86; **UNVERIFIED** для существования копий с другими именами. Этот документ не подтверждает смысл клиентского процесса.

## Основание и границы

- Журнал собственной сессии Codex: `/root/.codex/sessions/2026/10/13/rollout-2026-10-13T13-53-55-01a134e5-c247-7790-86a1-1801d5768d1e.jsonl`, записи 1859/1861 (отказ `rm -f`), 1869/1872 (`Path.unlink`, вывод `GOAL_FILES_REMOVED=86`, `GOAL_FILES_REMAIN=0`). Удалялись только файлы по шаблону `codex-01a134e5-*` в двух каталогах ниже; исходный вызов не записал перечень имён перед удалением.
- Имена восстановлены по записям создания и открытия в том же журнале: основные файлы — 121, 304, 434, 1111, 1737; страницы обзора — 1036, 1127, 1148, 1175; видео/материалы — 1064, 1092, 1242, 1263, 1279, 1305, 1403, 1473. Диапазоны имён формируются циклами в этих командах. Это реконструкция, а не сохранённый до удаления `find`.
- Поиск `find /root -type f -name "codex-01a134e5-*"` 2026-10-13 не нашёл файлов с исходными именами. **Копия с известным путём: не найдена** для всех 86. Поиск по имени не исключает копию с иным именем или вне `/root`; контрольных хешей удалённых файлов нет. JSONL сохраняет команды и отдельные текстовые фрагменты, но не является байтовой копией JSON, лога или изображений.

## Список удалённых имён

Каталог `.goal/` — 5 файлов:
- `codex-01a134e5-brief.md`
- `codex-01a134e5-passport.json`
- `codex-01a134e5-claims.json`
- `codex-01a134e5-evidence.log`
- `codex-01a134e5-lead-top.png`

Каталог `client-materials/private/.goal/` — 81 файл:
- `codex-01a134e5-review-C016.html`
- `codex-01a134e5-review-C016.png`
- `codex-01a134e5-review-001-004.html`
- `codex-01a134e5-review-001-004.png`
- `codex-01a134e5-review-005-008.html`
- `codex-01a134e5-review-005-008.png`
- `codex-01a134e5-review-009-012.html`
- `codex-01a134e5-review-009-012.png`
- `codex-01a134e5-review-013-016.html`
- `codex-01a134e5-review-013-016.png`
- `codex-01a134e5-review-017-020.html`
- `codex-01a134e5-review-017-020.png`
- `codex-01a134e5-review-021-023.html`
- `codex-01a134e5-review-021-023.png`
- `codex-01a134e5-review-024-028.html`
- `codex-01a134e5-review-024-028.png`
- `codex-01a134e5-review-029-033.html`
- `codex-01a134e5-review-029-033.png`
- `codex-01a134e5-review-034-038.html`
- `codex-01a134e5-review-034-038.png`
- `codex-01a134e5-review-039-043.html`
- `codex-01a134e5-review-039-043.png`
- `codex-01a134e5-review-044-048.html`
- `codex-01a134e5-review-044-048.png`
- `codex-01a134e5-review-049-053.html`
- `codex-01a134e5-review-049-053.png`
- `codex-01a134e5-review-054-058.html`
- `codex-01a134e5-review-054-058.png`
- `codex-01a134e5-review-059-063.html`
- `codex-01a134e5-review-059-063.png`
- `codex-01a134e5-review-064-068.html`
- `codex-01a134e5-review-064-068.png`
- `codex-01a134e5-review-069-073.html`
- `codex-01a134e5-review-069-073.png`
- `codex-01a134e5-review-074-078.html`
- `codex-01a134e5-review-074-078.png`
- `codex-01a134e5-review-079-083.html`
- `codex-01a134e5-review-079-083.png`
- `codex-01a134e5-review-084-088.html`
- `codex-01a134e5-review-084-088.png`
- `codex-01a134e5-review-089-093.html`
- `codex-01a134e5-review-089-093.png`
- `codex-01a134e5-review-094-098.html`
- `codex-01a134e5-review-094-098.png`
- `codex-01a134e5-review-099-103.html`
- `codex-01a134e5-review-099-103.png`
- `codex-01a134e5-review-104-108.html`
- `codex-01a134e5-review-104-108.png`
- `codex-01a134e5-review-109-113.html`
- `codex-01a134e5-review-109-113.png`
- `codex-01a134e5-review-114-114.html`
- `codex-01a134e5-review-114-114.png`
- `codex-01a134e5-miro-01-04.html`
- `codex-01a134e5-miro-01-04.png`
- `codex-01a134e5-miro-05-08.html`
- `codex-01a134e5-miro-05-08.png`
- `codex-01a134e5-miro-09-12.html`
- `codex-01a134e5-miro-09-12.png`
- `codex-01a134e5-miro-13-16.html`
- `codex-01a134e5-miro-13-16.png`
- `codex-01a134e5-miro-17-20.html`
- `codex-01a134e5-miro-17-20.png`
- `codex-01a134e5-miro-21-21.html`
- `codex-01a134e5-miro-21-21.png`
- `codex-01a134e5-csv-001-025.html`
- `codex-01a134e5-csv-001-025.png`
- `codex-01a134e5-csv-026-050.html`
- `codex-01a134e5-csv-026-050.png`
- `codex-01a134e5-csv-051-075.html`
- `codex-01a134e5-csv-051-075.png`
- `codex-01a134e5-csv-076-085.html`
- `codex-01a134e5-csv-076-085.png`
- `codex-01a134e5-answer-01.html`
- `codex-01a134e5-answer-01.png`
- `codex-01a134e5-source-status-preview.html`
- `codex-01a134e5-source-status-preview.png`
- `codex-01a134e5-transcript-format.html`
- `codex-01a134e5-transcript-format.png`
- `codex-01a134e5-GR8-004050.png`
- `codex-01a134e5-Hkb-000206.png`
- `codex-01a134e5-jpg-contact.png`

## Восстановление 20 решений

- **PROVEN:** в `/root/workspaces/projects/.worktrees/codex/eurosteklo-l07/docs/ppo/source-status.md` есть 20 отдельных строк паспортов `L1–L8` и `S1–S12` с решением, локаторами источников и ограничением решения: 1 `PROVEN`, 1 `CONTRADICTED`, 18 `UNVERIFIED` (строки 26–45; генерация из удалённого JSON видна в журнале, запись 1489). Эти **20 итоговых решений по строкам можно восстановить** из этой версии документа.
- **UNVERIFIED:** эта таблица не восстанавливает исходный 114-блочный `codex-01a134e5-claims.json`, полный ход проверки и точные байты `codex-01a134e5-evidence.log`. Для них нет известной полной копии.
- **CONTRADICTED для текущего `main`:** `/root/workspaces/projects/clients/eurosteklo/docs/ppo/source-status.md` на момент проверки содержит 12 сгруппированных строк паспортов (строки 26–37), а не 20 отдельных итоговых решений; из этой версии их восстановить нельзя. При использовании результата нужен именно файл из указанного рабочего дерева `eurosteklo-l07`, а не одноимённый файл в `main`.

Источник: собственный JSONL Codex и две локально проверенные версии `docs/ppo/source-status.md`; дата проверки: 2026-10-13. Конфиденциально; в Git не добавлять.
