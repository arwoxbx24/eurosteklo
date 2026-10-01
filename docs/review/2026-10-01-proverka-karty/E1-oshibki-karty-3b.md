# Блок E1/3б — проверка карты: ошибки карты (О-05…О-08)
Срез: 0de477d. Источник: docs/ppo/sdelki/_parts/proverka-2026-09-30/A-oshibki-karty.md. Пунктов: 4.
Итог: НА КАРТЕ 3 · ТОЛЬКО ТЕХДОК 0 · ПРОТИВОРЕЧИТ 0 · НЕТ 0 · НЕПРИМЕНИМО 1 (3+0+0+0+1 = 4)

| ID | Тип | Источник файл:строка | Согласовано (цитата) | Подстрока проверки | Точка карты | T1–T7 grep (число; Tn:строка) | Повтор (е/ядро) | Статус |
|---|---|---|---|---|---|---|---|---|
| О-05 | замена | A-oshibki-karty.md:27 | Паспорт: «Звонки … нарисованы после закрытия» | нарисованы после закрытия | — | 3; T1:56, T3:85, T4:53 | — | НА КАРТЕ |
| О-06 | удаление | A-oshibki-karty.md:28 | «частичное совпадение, авто-задачи по звонкам есть» — НЕТ (снято с карты) | частичное совпадение | — | 0 во всех T1–T7 | — | НА КАРТЕ |
| О-07 | удаление | A-oshibki-karty.md:29 | «RACI на карте нет» (не для карты) | RACI | — | 0 во всех T1–T7 | — | НЕПРИМЕНИМО |
| О-08 | удаление | A-oshibki-karty.md:30 | «роли "Соб", "Бух"; ссылки inventory.md» — НЕТ (снято с карты) | inventory | — | 0 во всех T1–T7 | — | НА КАРТЕ |

## Команды
```
$ grep -c -F "нарисованы после закрытия" T1 T2 T3 T4 T5 T6 T7
docs/ppo/sdelki/karta-sdelki.html:1
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:1
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:1
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0

$ grep -n -o -F "нарисованы после закрытия" T1 T3 T4
docs/ppo/sdelki/karta-sdelki.html:56:нарисованы после закрытия
docs/ppo/sdelki/obsledovanie-sdelki.html:85:нарисованы после закрытия
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:53:нарисованы после закрытия

$ grep -c -F "частичное совпадение" T1 T2 T3 T4 T5 T6 T7
docs/ppo/sdelki/karta-sdelki.html:0
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:0
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0

$ grep -c -F "inventory" T1 T2 T3 T4 T5 T6 T7
docs/ppo/sdelki/karta-sdelki.html:0
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:0
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0

$ grep -c -F "RACI" T1 T2 T3 T4 T5 T6 T7
docs/ppo/sdelki/karta-sdelki.html:0
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:0
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0
```
