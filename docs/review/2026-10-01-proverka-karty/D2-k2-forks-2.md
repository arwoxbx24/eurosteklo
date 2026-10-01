# Блок D2 — K2 развилки и события, строки Р-14…Р-26 (вопросы клиенту)

Срез: 0de477d. Источник: `docs/ppo/konflikty/k2-forks.md`. Пунктов: 13 (Р-14…Р-26).

Итог: НА КАРТЕ 13 · ТОЛЬКО ТЕХДОК 0 · ПРОТИВОРЕЧИТ 0 · НЕТ 0 · НЕПРИМЕНИМО 0 (13 = 13)

Проверяемая ячейка — «Вопрос клиенту» (правило D). Подстрока — отрывок 3–8 слов из вопроса, найденный на карте (карта перефразирует вопросы); первичная подстрока из исходника и повтор (е/ядро) указаны в графах grep/повтор. Пропущенных ID Р-14…Р-26 в реестре нет.

| ID | Тип | Источник файл:строка | Согласовано (цитата) | Подстрока проверки | Точка карты | T1–T7 grep (число; Tn:строка) | Повтор (е/ядро) | Статус |
|---|---|---|---|---|---|---|---|---|
| Р-14 | вопрос | k2-forks.md:38 | «Покажите: сделку, у которой стадия сменилась сама. А если клиент просто не отвечает — сделка после смены идёт дальше или возвращается менеджеру, и от какого действия считаются 3 дня?» | «3 рабочих дня, а оплаты нет» | С26 | 3 («3 рабочих дня, а оплаты нет»: T1:1065, T3:465, T4:757) | первичная подстрока «сделку, у которой стадия сменилась» = 0;; ядро «сменилась сама» = 0 — нашли по формулировке точки С26 | НА КАРТЕ |
| Р-15 | вопрос | k2-forks.md:39 | «Покажите: сделку, где предоплата была меньше 35 % — кто разрешил и где это записано.» | «пришло меньше 35» | — | 3 («пришло меньше 35»: T1:1065, T3:153, T4:331) | ядро «меньше 35» = T1:1, T3:2, T4:3 | НА КАРТЕ |
| Р-16 | вопрос | k2-forks.md:40 | «Покажите: заказ, по которому фурнитура частично была на складе. А если нужной нет и поставка 3 недели — заказ всё равно запускается…» | «откуда взялась фурнитура» | С11 | 3 («откуда взялась фурнитура»: T1:1065, T3:295, T4:380) | ядро «фурнитуры нет на складе» = T1:1065, T3:296, T4:383 | НА КАРТЕ |
| Р-17 | вопрос | k2-forks.md:41 | «Покажите: как менеджер сейчас добавляет позицию, которой нет в списке. А если РОС не внёс за неделю…» | «позиции нет в номенклатуре» | С5 | 3 («позиции нет в номенклатуре»: T1:1065, T3:491, T4:804) | первичная подстрока «как менеджер сейчас добавляет позицию» = 0 | НА КАРТЕ |
| Р-18 | вопрос | k2-forks.md:42 | «Покажите: сделку с понижающим коэффициентом — кто ставил и как получал визу.» | «понижающим коэффициентом» | С5 | 3 («понижающим коэффициентом»: T1:1065, T3:243, T4:227) | первичная подстрока «сделку с понижающим коэффициентом» = 0 | НА КАРТЕ |
| Р-19 | вопрос | k2-forks.md:43 | «Покажите: две последние сделки — с монтажом и без. На каком шаге менеджер узнаёт, что монтаж нужен, и кто это решил.» | «две последние сделки» | С14 | 3 («две последние сделки»: T1:1065, T3:334, T4:455) | — | НА КАРТЕ |
| Р-20 | вопрос | k2-forks.md:44 | «Покажите: сделку, где было и то и другое — в каком порядке шли документы и кто закрывал каждую часть.» | «заказ оплачен, а монтаж не сделан» | — | 3 («заказ оплачен, а монтаж не сделан»: T1:1065, T3:179, T4:558) | ядро «и то и другое» = 0; тема дубля блоков МОП = T1:217 «дублирует часть блока» | НА КАРТЕ |
| Р-21 | вопрос | k2-forks.md:45 | «Покажите: сделку, где изделие готово, а остаток не оплачен — сколько оно стоит и кто звонит.» | «остаток не оплачен» | С13 | 3 («остаток не оплачен»: T1:1065, T3:348, T4:484) | первичная подстрока «сделку, где изделие готово» = 0 | НА КАРТЕ |
| Р-22 | вопрос | k2-forks.md:46 | «Покажите: доставку и самовывоз последних двух сделок — какие документы у каждой.» | «заказ забран самовывозом» | С13 | 3 («заказ забран самовывозом»: T1:1065, T3:374, T4:534) | ядро «самовывоз» = T1:3, T3:1, T4:3 | НА КАРТЕ |
| Р-23 | вопрос | k2-forks.md:47 | «Покажите: пример сделки, отгруженной в два приёма — какие документы и оплата на каждый приём.» | «заказ состоит из нескольких частей» | С18 | 3 («заказ состоит из нескольких частей»: T1:1065, T3:127, T4:710) | ядро «отгруженной» = 0; вариант «…два приема» = 0 | НА КАРТЕ |
| Р-24 | вопрос | k2-forks.md:48 | «Покажите: последнюю рекламацию от начала до конца — кто принял, кто решал, чем закончилась.» | «Покажите последнюю рекламацию» | — | 3 («Покажите последнюю рекламацию»: T1:1065, T3:399, T4:605) | первичная подстрока «последнюю рекламацию от начала до конца» = 0 | НА КАРТЕ |
| Р-25 | вопрос | k2-forks.md:49 | «Покажите: закрытый монтаж — какие фото и документы нужны, чтобы считать его сделанным.» | «Покажите на последнем монтаже» | С16 | 3 («Покажите на последнем монтаже»: T1:1065, T3:360, T4:505) | первичная подстрока «закрытый монтаж какие фото и документы» = 0; ядро «закрытый монтаж» = 0 | НА КАРТЕ |
| Р-26 | вопрос | k2-forks.md:50 | «Покажите: чек-лист, о котором идёт речь, — какие пункты и кто отмечает.» | «внесение информации по чек-листу» | — | 1 («внесение информации по чек-листу»: T1:215) | вариант е «чек-лист, о котором идет речь» = 0; тема чек-листа отражена у рамки ОТГРУЗКА | НА КАРТЕ |

## Команды

Первичные подстроки из исходника — `grep -c -F` по T1–T7, итог 0 по всем кроме Р-19:

```
$ grep -c -F "сделку, у которой стадия сменилась" docs/ppo/sdelki/karta-sdelki.html docs/ppo/lidy/karta-lidy.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html docs/ppo/lidy/obsledovanie-lidy.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html docs/ppo/index.html
docs/ppo/sdelki/karta-sdelki.html:0
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:0
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:0
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0
```
Аналогично 0 для: «сделку, где предоплата была меньше», «заказ, по которому фурнитура частично», «как менеджер сейчас добавляет позицию», «сделку с понижающим коэффициентом», «сделку, где было и то и другое», «сделку, где изделие готово», «доставку и самовывоз последних двух сделок», «сделки, отгруженной в два приёма», «последнюю рекламацию от начала до конца», «закрытый монтаж какие фото и документы», «чек-лист, о котором идёт речь».

Единственная первичная подстрока, найденная сразу:
```
$ grep -c -F "две последние сделки" docs/ppo/sdelki/karta-sdelki.html docs/ppo/lidy/karta-lidy.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html docs/ppo/lidy/obsledovanie-lidy.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html docs/ppo/index.html
docs/ppo/sdelki/karta-sdelki.html:1
docs/ppo/lidy/karta-lidy.html:0
docs/ppo/sdelki/obsledovanie-sdelki.html:1
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:1
docs/ppo/lidy/obsledovanie-lidy.html:0
docs/ppo/lidy/obsledovanie-lidy-podrobno.html:0
docs/ppo/index.html:0
$ grep -n -o -F "две последние сделки" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:две последние сделки
docs/ppo/sdelki/obsledovanie-sdelki.html:334:две последние сделки
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:455:две последние сделки
```

Повтор (е/ядро) по карте — найденные фрагменты (T1 — karta-sdelki.html, T3 — obsledovanie-sdelki.html, T4 — obsledovanie-sdelki-podrobno.html):

```
$ grep -n -o -F "3 рабочих дня, а оплаты нет" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:3 рабочих дня, а оплаты нет
docs/ppo/sdelki/obsledovanie-sdelki.html:465:3 рабочих дня, а оплаты нет
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:757:3 рабочих дня, а оплаты нет
```
```
$ grep -c -F "меньше 35" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html   →   T1:1, T3:2, T4:3
$ grep -n -o -F "пришло меньше 35" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:пришло меньше 35
docs/ppo/sdelki/obsledovanie-sdelki.html:153:пришло меньше 35
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:331:пришло меньше 35
```
```
$ grep -n -o -F "откуда взялась фурнитура" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:откуда взялась фурнитура
docs/ppo/sdelki/obsledovanie-sdelki.html:295:откуда взялась фурнитура
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:380:откуда взялась фурнитура
$ grep -n -o -F "фурнитуры нет на складе" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:фурнитуры нет на складе
docs/ppo/sdelki/obsledovanie-sdelki.html:296:фурнитуры нет на складе
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:383:фурнитуры нет на складе
```
```
$ grep -n -o -F "позиции нет в номенклатуре" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:позиции нет в номенклатуре
docs/ppo/sdelki/obsledovanie-sdelki.html:491:позиции нет в номенклатуре
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:804:позиции нет в номенклатуре
```
```
$ grep -n -o -F "понижающим коэффициентом" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:понижающим коэффициентом
docs/ppo/sdelki/obsledovanie-sdelki.html:243:понижающим коэффициентом
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:227:понижающим коэффициентом
```
```
$ grep -n -o -F "заказ оплачен, а монтаж не сделан" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:заказ оплачен, а монтаж не сделан
docs/ppo/sdelki/obsledovanie-sdelki.html:179:заказ оплачен, а монтаж не сделан
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:558:заказ оплачен, а монтаж не сделан
docs/ppo/sdelki/karta-sdelki.html:217:дублирует часть блока
```
```
$ grep -n -o -F "остаток не оплачен" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:остаток не оплачен
docs/ppo/sdelki/obsledovanie-sdelki.html:348:остаток не оплачен
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:484:остаток не оплачен
```
```
$ grep -n -o -F "заказ забран самовывозом" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:заказ забран самовывозом
docs/ppo/sdelki/obsledovanie-sdelki.html:374:заказ забран самовывозом
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:534:заказ забран самовывозом
```
```
$ grep -n -o -F "заказ состоит из нескольких частей" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:заказ состоит из нескольких частей
docs/ppo/sdelki/obsledovanie-sdelki.html:127:заказ состоит из нескольких частей
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:710:заказ состоит из нескольких частей
```
```
$ grep -n -o -F "Покажите последнюю рекламацию" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:Покажите последнюю рекламацию
docs/ppo/sdelki/obsledovanie-sdelki.html:399:Покажите последнюю рекламацию
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:605:Покажите последнюю рекламацию
```
```
$ grep -n -o -F "Покажите на последнем монтаже" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:1065:Покажите на последнем монтаже
docs/ppo/sdelki/obsledovanie-sdelki.html:360:Покажите на последнем монтаже
docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html:505:Покажите на последнем монтаже
```
```
$ grep -n -o -F "внесение информации по чек-листу" docs/ppo/sdelki/karta-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki.html docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html
docs/ppo/sdelki/karta-sdelki.html:215:внесение информации по чек-листу
```
