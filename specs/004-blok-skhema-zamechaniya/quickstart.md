# Quickstart: проверка спецификации 004

Каталог: `/root/workspaces/projects/clients/eurosteklo`. Файл схемы: `docs/process/bpmn/eurosteklo_process.drawio` (далее `D`).

| SC | Команда | Ожидание |
|---|---|---|
| SC-001 | `grep -o "fontSize=[0-9]*" D \| sort \| uniq -c` | нет значений <16 |
| SC-002 | `grep -cE "док-ты\|14/90/270\|₽\|FR-\|FF[0-9]" D` | 0 |
| SC-003 | `grep -cE "#232F3E\|#5A6B7B" D`; `grep -o "#D90000" D \| wc -l` | 0; только у 9 номеров |
| SC-004 | `grep -c "shape=document" D` | 6 |
| SC-005 | `grep -c "shape=note" D`; `grep -c "Проход с клиентом" D` | 0; 1 |
| SC-006 | `node /root/workspaces/projects/clients/tools/drawio-ai-kit/src/cli.mjs validate D` | `"ok":true`, warnings `[]` |
| SC-006 | `timeout 90 google-chrome --headless=new --no-sandbox --disable-gpu --virtual-time-budget=15000 --window-size=1920,1400 --screenshot=/tmp/dww-004.png docs/process/bpmn/view.html` | PNG >50 КБ, перекрытий нет (проверка агентом по снимку) |
| SC-007 | `curl -s -o /dev/null -w "%{http_code}" https://b244.ru/DwW`; `git diff --stat docs/meetings/variants/LINKS.md` | 200 (после редиректа); LINKS.md без изменений |

Сохранность содержания (FR-011): список `value="…"` шагов, дорожек и фаз до и после совпадает, кроме FR-002.
