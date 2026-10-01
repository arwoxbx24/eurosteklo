# Блок D1, часть 1б — k1-prepost.md, строки П-06…П-10 (вопросы)
Срез: 0de477d. Источник: docs/ppo/konflikty/k1-prepost.md. Пунктов: 5.
Итог: НА КАРТЕ 5 · ТОЛЬКО ТЕХДОК 0 · ПРОТИВОРЕЧИТ 0 · НЕТ 0 · НЕПРИМЕНИМО 0 (5+0+0+0+0 = 5)

| ID | Тип | Источник файл:строка | Согласовано (цитата) | Подстрока проверки | Точка карты | T1–T7 grep (число; Tn:строка) | Повтор (е/ядро) | Статус |
|---|---|---|---|---|---|---|---|---|
| П-06 | вопрос | k1-prepost.md:59 | Что делает менеджер, если нужной позиции нет в номенклатуре, и сколько это обычно занимает? | Что делает менеджер | — | 0 | «позиции нет в номенклатуре»: T1:1 (1065), T3:1 (491), T4:1 (804) | НА КАРТЕ |
| П-07 | вопрос | k1-prepost.md:60 | Что такое понижающие коэффициенты, кто вправе их применять и почему согласует именно служба сервиса? | Что такое понижающие коэффициенты | — | 0 | «понижающие коэффициенты»: T1:3 (103, 748, 1065), T3:1 (242), T4:2 (216, 863) | НА КАРТЕ |
| П-08 | вопрос | k1-prepost.md:61 | Когда вы считаете, что клиент согласился на расчёт и можно ехать на замер? Кто это отмечает? | Когда вы считаете | — | 0 | «КП согласовано»: T1:4 (103, 363, 366, 748), T4:5 (196, 206, 246, 871, 1041) | НА КАРТЕ |
| П-09 | вопрос | k1-prepost.md:62 | Меняется ли состав заказа после замера и проектирования? Если да, как это попадает в договор? | Меняется ли состав заказа | — | 0 | «А если после замера состав»: T1:1 (1065), T3:1 (478), T4:1 (782) | НА КАРТЕ |
| П-10 | вопрос | k1-prepost.md:63 | Что должно произойти, чтобы сделка перешла в «Заявку», и что должно быть готово, чтобы перейти дальше? | Что должно произойти | С29, С1 | 0 | «начинается сделка»: T4:1 (С1 о Предв. расчёте и Заявке); «С29»: T1:1 (62), T3:2 (91, 164), T4:4 (59, 107, 813) | НА КАРТЕ |

## Команды

### П-06. Первичная
```
grep -c -F "Что делает менеджер" docs/ppo/sdelki/karta-sdelki.html docs/ppo/lidy/karta-lidy.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html docs/ppo/lidy/obsledovanie-lidy.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html docs/ppo/index.html
docs/ppo/sdelki/karta-sdelki.html:0
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:0
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0
```

### П-06. Повтор (ё→е — нет «ё»; ядро: «позиции нет в номенклатуре»)
```
grep -c -F "позиции нет в номенклатуре" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1
docs/ppo/sdelki/obsledovanie-sdelki.html:1
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:1
```
```
grep -n -o -F "позиции нет в номенклатуре" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:позиции нет в номенклатуре
docs/ppo/sdelki/obsledovanie-sdelki.html:491:позиции нет в номенклатуре
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:804:позиции нет в номенклатуре
```

### П-07. Первичная
```
grep -c -F "Что такое понижающие коэффициенты" docs/ppo/sdelki/karta-sdelki.html docs/ppo/lidy/karta-lidy.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html docs/ppo/lidy/obsledovanie-lidy.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html docs/ppo/index.html
docs/ppo/sdelki/karta-sdelki.html:0
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:0
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0
```

### П-07. Повтор (ё→е — нет; ядро: «понижающие коэффициенты»)
```
grep -c -F "понижающие коэффициенты" docs/ppo/sdelki/karta-sdelki.html docs/ppo/lidy/karta-lidy.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html docs/ppo/lidy/obsledovanie-lidy.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html docs/ppo/index.html
docs/ppo/sdelki/karta-sdelki.html:3
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:1
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:2
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0
```
```
grep -n -o -F "понижающие коэффициенты" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:103:понижающие коэффициенты
docs/ppo/sdelki/karta-sdelki.html:748:понижающие коэффициенты
docs/ppo/sdelki/karta-sdelki.html:1065:понижающие коэффициенты
docs/ppo/sdelki/obsledovanie-sdelki.html:242:понижающие коэффициенты
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:216:понижающие коэффициенты
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:863:понижающие коэффициенты
```

### П-08. Первичная
```
grep -c -F "Когда вы считаете" docs/ppo/sdelki/karta-sdelki.html docs/ppo/lidy/karta-lidy.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html docs/ppo/lidy/obsledovanie-lidy.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html docs/ppo/index.html
docs/ppo/sdelki/karta-sdelki.html:0
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:0
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0
```

### П-08. Повтор (ё→е — нет; ядро: «КП согласовано»)
```
grep -c -F "КП согласовано" docs/ppo/sdelki/karta-sdelki.html docs/ppo/lidy/karta-lidy.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html docs/ppo/lidy/obsledovanie-lidy.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html docs/ppo/index.html
docs/ppo/sdelki/karta-sdelki.html:4
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:5
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0
```
```
grep -n -o -F "КП согласовано" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:103:КП согласовано
docs/ppo/sdelki/karta-sdelki.html:363:КП согласовано
docs/ppo/sdelki/karta-sdelki.html:366:КП согласовано
docs/ppo/sdelki/karta-sdelki.html:748:КП согласовано
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:196:КП согласовано
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:206:КП согласовано
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:246:КП согласовано
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:871:КП согласовано
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:1041:КП согласовано
```

### П-09. Первичная
```
grep -c -F "Меняется ли состав заказа" docs/ppo/sdelki/karta-sdelki.html docs/ppo/lidy/karta-lidy.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html docs/ppo/lidy/obsledovanie-lidy.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html docs/ppo/index.html
docs/ppo/sdelki/karta-sdelki.html:0
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:0
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0
```

### П-09. Повтор (ё→е — нет; ядро: «А если после замера состав»)
```
grep -c -F "А если после замера состав" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1
docs/ppo/sdelki/obsledovanie-sdelki.html:1
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:1
```
```
grep -n -o -F "А если после замера состав" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:А если после замера состав
docs/ppo/sdelki/obsledovanie-sdelki.html:478:А если после замера состав
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:782:А если после замера состав
```

### П-10. Первичная
```
grep -c -F "Что должно произойти" docs/ppo/sdelki/karta-sdelki.html docs/ppo/lidy/karta-lidy.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html docs/ppo/lidy/obsledovanie-lidy.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html docs/ppo/index.html
docs/ppo/sdelki/karta-sdelki.html:0
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:0
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0
```

### П-10. Повтор (ё→е — нет; ядро: «начинается сделка» — C1; «С29» — точка карты)
```
grep -c -F "начинается сделка" docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:1
```
```
grep -c -F "С29" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1
docs/ppo/sdelki/obsledovanie-sdelki.html:2
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:4
```
```
grep -n -o -F "С29" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:62:С29
docs/ppo/sdelki/karta-sdelki.html:62:С29
docs/ppo/sdelki/karta-sdelki.html:103:С29
docs/ppo/sdelki/karta-sdelki.html:748:С29
docs/ppo/sdelki/obsledovanie-sdelki.html:91:С29
docs/ppo/sdelki/obsledovanie-sdelki.html:91:С29
docs/ppo/sdelki/obsledovanie-sdelki.html:164:С29
docs/ppo/sdelki/obsledovanie-sdelki.html:164:С29
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:59:С29
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:59:С29
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:107:С29
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:813:С29
```