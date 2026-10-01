# Проверка блока D спецификации 009

Статус: IN_PROGRESS

Итог: всего 121 · были на карте 120 · добавлено в карточки 0 · добавлено в повестку 0 · пусто 1 · после сборки не на карте 0

## Ход выполнения

### Шаг 1

Команда: `python3 docs/ppo/check_ppo.py --lidy`

Вывод:

```text
K1 связность точек: ок (lidy 16 точек; sdelki 29 точек)
K2 номера не пропали: ок
K3 источник у вариантов (data-src): ок (lidy 60 пунктов; sdelki 180 пунктов)
K4 нет «(вопрос N)» на картах: ок
K5 пометка 1С: ПРЕДУПР 1
   предупр слой A: ««уведомление Руководителя ОС для внесения номенклатуры» (к.7368); «инт»
K6 ПДн: ок (без белого списка телефонов 0, после — 0)
K7 stitch вызван: ок
K8 идемпотентность сборки: ок
K9 шлюз лидов: ок (база 21125b3 (--lidy))
K10 владение вопроса (data-see, data-id, дубли, повестка): ок (lidy: повестка 9 строк; своих пунктов 207, ссылок 33)
итого: ошибок 0, предупреждений 1
```

### Шаг 6

Команда: `python3 specs/009-voprosy-konfliktov/map_voprosy.py --out specs/009-voprosy-konfliktov/mapping-posle.tsv`

Вывод:

```text
всего 121 · уже 120 · точка 0 · повестка 0 · пусто 1
```

### Шаг 7

Команда: `grep -c -F "замер платный" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html`

Код завершения: 1 (для `grep -c` при отсутствии совпадений; ожидаемый результат шага — три нуля).

Вывод:

```text
docs/ppo/sdelki/karta-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:0
```

### Шаг 8

Команда: `grep -c -F "🟣" docs/ppo/sdelki/karta-sdelki.html docs/ppo/lidy/karta-lidy.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html`

Вывод:

```text
docs/ppo/sdelki/karta-sdelki.html:1
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:76
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
```

### Шаг 9

Команда: `git status --porcelain`

Вывод:

```text
 M docs/ppo/ppo-evrosteklo.zip
 M docs/ppo/sdelki/_parts/tochki.html
 M docs/ppo/sdelki/karta-sdelki.html
 M docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
 M docs/ppo/sdelki/obsledovanie-sdelki.html
?? docs/review/2026-10-01-voprosy-konfliktov/
?? specs/009-voprosy-konfliktov/apply_voprosy.py
?? specs/009-voprosy-konfliktov/blocks/A-fix.md
?? specs/009-voprosy-konfliktov/blocks/B-fix.md
?? specs/009-voprosy-konfliktov/map_voprosy.py
?? specs/009-voprosy-konfliktov/mapping-posle.tsv
?? specs/009-voprosy-konfliktov/mapping.tsv
?? test_block_d.py
```

## Строки привязки со статусом «точка» или «повестка»

Нет: оба счётчика шага 2 и шага 6 равны 0.

Лиды: новые вопросы в точках: нет; в повестке лидов: 0

Пусто: К-37 — вопрос в круглых скобках; на карту не выводится.

Статус: PROVEN — все девять команд выполнены; шаги 5–7 соответствуют критериям блока D. Git-операции публикации не выполнялись.

### Шаг 2

Команда: `python3 specs/009-voprosy-konfliktov/map_voprosy.py`

Вывод:

```text
всего 121 · уже 120 · точка 0 · повестка 0 · пусто 1
```

### Шаг 3

Команда: `python3 specs/009-voprosy-konfliktov/apply_voprosy.py`

Вывод:

```text
вставлено в карточки 0 · в повестку 0 · пропущено 0
```

### Шаг 4

Команда: `python3 docs/ppo/build_all.py`

Вывод:

```text
ok 2600 3770 точек 29
lidy ok: 16 точек, порядок [1, 2, 3, 13, 16, 4, 8, 15, 9, 7, 11, 12, 6, 5, 10, 14]
sdelki ok: 29 точек, порядок [24, 6, 9, 29, 18, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 25, 26, 27, 28]
index ok
zip ok: ppo-evrosteklo.zip 7 файлов
```

### Шаг 5

Команда: `python3 docs/ppo/check_ppo.py --lidy`

Вывод:

```text
K1 связность точек: ок (lidy 16 точек; sdelki 29 точек)
K2 номера не пропали: ок
K3 источник у вариантов (data-src): ок (lidy 60 пунктов; sdelki 180 пунктов)
K4 нет «(вопрос N)» на картах: ок
K5 пометка 1С: ПРЕДУПР 1
   предупр слой A: ««уведомление Руководителя ОС для внесения номенклатуры» (к.7368); «инт»
K6 ПДн: ок (без белого списка телефонов 0, после — 0)
K7 stitch вызван: ок
K8 идемпотентность сборки: ок
K9 шлюз лидов: ок (база 21125b3 (--lidy))
K10 владение вопроса (data-see, data-id, дубли, повестка): ок (lidy: повестка 9 строк; своих пунктов 207, ссылок 33)
итого: ошибок 0, предупреждений 1
```
