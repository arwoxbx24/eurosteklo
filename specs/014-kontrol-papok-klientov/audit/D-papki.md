# Блок D: инвентарь папок clients/* (H9, H11)

Дата: 2026-10-09. Только чтение. Содержимое клиентских материалов не читалось.

## Таблица по папкам

Колонки: репо = `git -C <папка> rev-parse --show-toplevel` (СВОЙ или родительский `/root/workspaces/projects`). Файлы = записи верхнего уровня включая скрытые (`find -maxdepth 1`).

| Папка | Репо | remote origin | .beads | CLAUDE.md / AGENTS.md (строк) | README | private/ и защита | dev/prod | Файлов верхн. ур. | Ignore в родителе (`check-ignore`) |
|---|---|---|---|---|---|---|---|---|---|
| Savinsname | родитель | нет | нет | нет / нет | нет | нет | нет | 5 (все служебные: .repowise, .tmp, .claude-downloads, .cbmignore, .pytest_cache) | не игнорируется, `??` untracked |
| agida-bream-tech | родитель | нет | нет | нет / нет | нет | нет | нет | 4 (все служебные) | untracked |
| agramak | родитель | нет | нет | нет / нет | нет | нет | нет | 4 (serverless/ игнорируется + служебные) | untracked |
| asense.store | родитель | нет | нет | нет / нет | нет | нет | нет | 4 (все служебные) | untracked |
| docs | родитель | нет | нет | нет / нет | нет | нет | нет | 1 (infographic-styles.md) | tracked |
| eurosteklo | СВОЙ | git@github.com:arwoxbx24/eurosteklo.git | да (локальная) | 17 / 72 | да | `client-materials/private/` есть; `.gitignore:4:client-materials/private/` | нет (есть `.worktrees/`) | 20 | в родителе untracked как вложенный репо |
| mikhail-travel | родитель | нет | нет | нет / нет | нет | нет | нет | 3 (все служебные) | untracked |
| okna-plus | СВОЙ | git@github.com:arwoxbx24/clients-okna-plus.git | нет | 0 (пустой файл) / нет | нет | нет `private/`; есть `secrets` (файл) и `.env` (симлинк) | нет | 28 (13 скриптов .py в корне) | `.gitignore:214:clients/okna-plus/` (полностью игнорируется) |
| planeta-autostekla | родитель | нет | нет | нет / нет | нет | нет | нет | 3 (все служебные) | untracked |
| sanatory-avto | СВОЙ | git@github.com:arwoxbx24/agent-contour.git | да (локальная, в ignore родителя) | нет / нет | нет | `private/` нет; `data/` игнорируется (`.gitignore:147:data/`) | нет | 13 | untracked |
| techsplav | родитель (tracked) | нет (нет своего .git) | нет | 11 / 58 | да | `private/` нет; `inbox/` и `correspondence/attachments/` в `techsplav/.gitignore:2-3` | нет | 14 | tracked, часть ignore |
| tools | родитель | нет | нет | нет / нет | нет | нет | нет | 1 (drawio-ai-kit/) | `!! clients/tools/` игнорируется (в `clients/CLAUDE.md` описан) |

Общее: `ls -d clients/*-dev clients/*-prod clients/*/dev clients/*/prod` — совпадений нет (ошибка "No such file" по всем четырём). Папка `clients/CLAUDE.md` (общий файл) tracked в родителе.

## Итоговые числа

- Папок: 12 (11 клиентских + `docs` + `tools` = 12 каталогов; клиентских проектов 10).
- Свой `.git`: 3 (eurosteklo, okna-plus, sanatory-avto). Родительский: 9.
- remote origin: 3 из 3 своих репо; три разных имени (eurosteklo, clients-okna-plus, agent-contour). Имя репо sanatory-avto не совпадает с папкой.
- `.beads`: 2 (eurosteklo, sanatory-avto).
- `CLAUDE.md`: 3 (eurosteklo 17, techsplav 11, okna-plus 0). `AGENTS.md`: 2 (eurosteklo 72, techsplav 58). 7 папок без обоих.
- README: 2 (eurosteklo, techsplav).
- `private/` (по имени): 1 (`eurosteklo/client-materials/private`), защищён строкой `.gitignore:4` своего репо.
- dev/prod: 0 папок.
- Служебные файлы во всех папках: `.repowise` — 10 из 10 клиентских; `.cbmignore` — 8 из 10 (нет у eurosteklo, okna-plus); `.tmp`/`.claude-downloads`/`.pytest_cache` — в большинстве. Это следы индексации и хуков, не проверки конвенции.
- Родительский `git status --ignored clients`: 8 папок `??` untracked целиком, okna-plus и tools `!!` ignored.

## Вердикты

| ID | Вердикт | Доказательство |
|---|---|---|
| H9 | НЕТ | Единой конвенции по факту нет: репо свой/родительский/игнорируемый (3/9, из них okna-plus ignored, tools ignored); `.beads` 2 из 10; `CLAUDE.md` 3 из 10 (один пустой, 0 строк); `private/` 1 из 10 и только как `client-materials/private/`; dev/prod 0; имена папок разных стилей (Savinsname, asense.store, agida-bream-tech). `clients/CLAUDE.md` задаёт только инструмент `tools/drawio-ai-kit`, индексы и стиль инфографики; конвенции папок (компания, dev/prod, private) в нём нет (команда: `wc -l clients/*/CLAUDE.md`, `ls -d` выше). Текстовый поиск по законам — блок A. |
| H11 | НЕТ | Следов регулярной проверки папок нет: нет одинаковых служебных файлов проверки/отчёта ни в одной папке. Одинаковы только артефакты индексации (`.repowise`, `.cbmignore`), создаваемые `code-memory-enable`/git-хуком. Наличие pm2/cron/CI проверяет блок B. |
