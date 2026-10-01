# Поручение: исправление дефекта скрипта блока B спецификации 009

Рабочий каталог: `/root/workspaces/projects/clients/eurosteklo/.worktrees/claude/0e3`.

Дефект кода (спецификация не меняется): `python3 specs/009-voprosy-konfliktov/apply_voprosy.py` падает —
`apply_voprosy.py line 72, in plan: text = texts[r["map"]]` → `KeyError: '-'`.
По `specs/009-voprosy-konfliktov/spec.md`, раздел 6 и раздел 7 блок B: строки со статусом `уже` и `пусто` имеют `map=-` и скрипт для них ничего не делает.

Что сделать (только файл `specs/009-voprosy-konfliktov/apply_voprosy.py`):
1. `grep -n` по `texts[` и по `status` в скрипте; прочитать только нужный диапазон.
2. Строки TSV со статусом `уже` и `пусто` пропускать до любого обращения к `map` / `point` (ни проверки места, ни вставки).
3. В `--selftest` добавить случай: TSV-строки `уже` и `пусто` с `map=-`, `point=-` не вызывают ошибку и ничего не вставляют.
4. Больше ничего в скрипте не менять. На рабочих `tochki.html` скрипт не запускать.

Запреты: `git commit`/`push`, `rm -rf`, секреты, `~/.ssh`; одна команда на вызов, без `;`, `&&`, `|`, циклов; новых файлов не создавать (временные тесты — нет).

Приёмка: `python3 specs/009-voprosy-konfliktov/apply_voprosy.py --selftest` → код 0. Ответ: эта команда с выводом и `grep -n` изменённых строк.
