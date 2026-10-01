# C — процесс «Лиды»: независимое второе мнение

Срез: `git rev-parse HEAD` → `9690df60bfecfdd5839946f0ca12d9392a2359f3`.
Паспорт: `docs/plans/2026-10-01-0929-codex-vtoroe-mnenie-plan.md`, прочитан целиком до проверки.
skills: csb → `csb-log.md` (координатор; дочерняя сессия загрузила SKILL.md и alignment.md); superpowers:dispatching-parallel-agents → `csb-log.md` (запуск блока координатором); compound-engineering:ce-doc-review → `ce-doc-review-log.md` (фактическое выполнение последующей CE-рецензии отражается в этом журнале).
skip-step: csb — журнал bd; по §8 паспорта не вызывается, доступность и выполнение требования журнала здесь не подтверждены.

Первичный проход и эта матрица зафиксированы до чтения `FACTCHECK-karta.md` и `audit-lidy.md`. Время независимой проверки: `date -u '+%Y-%m-%dT%H:%M:%SZ'` → `2026-10-01T06:54:36Z`. Матрица подтверждает наличие и внутреннее отражение вопросов, а не достоверность внешней доски.

## Прочитано

Перечень: `git ls-files docs/ppo/lidy`; числа строк: `git ls-files docs/ppo/lidy | xargs wc -l`. Для больших HTML применены поиск и диапазоны, затем сравнение фрагментов без сборки и записи исходников.

| Файл | Строк (`wc -l`) | Прочитан | Способ / причина |
|---|---:|---|---|
| docs/ppo/lidy/_parts/FACTCHECK-karta.md | 192 | да | После фиксации первичной матрицы; целиком, с дополнительным диапазоном 83–163 |
| docs/ppo/lidy/_parts/TOCHKI.md | 43 | да | Целиком |
| docs/ppo/lidy/_parts/audit-lidy.md | 56 | да | После фиксации первичной матрицы, целиком |
| docs/ppo/lidy/_parts/build.py | 6 | да | Целиком; не запускался |
| docs/ppo/lidy/_parts/karta.svg.html | 418 | да | Разметка и диапазоны всех слоёв, связей и точек; сравнение SVG |
| docs/ppo/lidy/_parts/pasport.html | 40 | да | Целиком |
| docs/ppo/lidy/_parts/povestka-vladeltsu.md | 68 | да | Целиком, двумя диапазонами |
| docs/ppo/lidy/_parts/sostoyaniya.html | 305 | да | Состояния, переходы и все семь историй, диапазонами |
| docs/ppo/lidy/_parts/tochki.html | 419 | да | Все 16 карточек и повестка, диапазонами |
| docs/ppo/lidy/karta-lidy.html | 915 | да | Все маркеры, SVG, mapdata, подписи слоёв и используемые ссылки; остальные участки — структурное сравнение |
| docs/ppo/lidy/obsledovanie-lidy-podrobno.html | 852 | да | Паспорт, все карточки, состояния, истории и повестка; структурное сравнение |
| docs/ppo/lidy/obsledovanie-lidy.html | 496 | да | Повестка, паспорт, все короткие карточки; сопоставление главных вопросов |
| client-materials/sanitized-tz.md | 45 | да | Дополнительный разрешённый источник: ФТ-1, следующий ФТ-2 и развитие; метаданные изображений |
| client-materials/sanitized-statusy.md | 48 | да | Дополнительный разрешённый источник: таблицы статусов; схема «Создание лида → Новый» в этом тексте не представлена |

## Матрица покрытия

Команда подсчёта: `rg -c '^\| [0-9]+ \|' docs/ppo/lidy/_parts/TOCHKI.md` → `16`.
Проверка номеров: `rg -n '^\| [0-9]+ \|' docs/ppo/lidy/_parts/TOCHKI.md` → строки 7–22, номера 1–16.
В матрице **16 строк**. Карта — готовый `karta-lidy.html`; состояния — первичный `sostoyaniya.html`. Маркеры готовой карты — строки 499–514, в SVG-источнике — 402–417. Ссылки частей проверены также в готовой подробной странице.

| Точка / TOCHKI.md | Место на карте | Место в состояниях | Класс внутреннего покрытия |
|---|---|---|---|
| 1 / :7 | karta-lidy.html:499, `id="p1"`; связи :182, :206 | _parts/sostoyaniya.html:14, :16, :96 | НЕСООТВЕТСТВИЕ C-01: стрелки / линии без наконечника; точка присутствует |
| 2 / :8 | karta-lidy.html:500, `id="p2"` | _parts/sostoyaniya.html:16, :166, :221 | ПОДТВЕРЖДЕНО: вопрос об источниках присутствует |
| 3 / :9 | karta-lidy.html:501, `id="p3"` | _parts/sostoyaniya.html:21, :97, :139 | ПОДТВЕРЖДЕНО: неизвестная роль отражена; оговорка о таймере — C-03 |
| 4 / :10 | karta-lidy.html:502, `id="p4"` | _parts/sostoyaniya.html:21, :222 | ПОДТВЕРЖДЕНО: B2B/B2C и общий путь отражены |
| 5 / :11 | karta-lidy.html:503, `id="p5"` | _parts/sostoyaniya.html:4, :23, :28, :103 | НЕСООТВЕТСТВИЕ C-02: прямой ход / связи нет; точка присутствует |
| 6 / :12 | karta-lidy.html:504, `id="p6"` | _parts/sostoyaniya.html:35, :36, :37, :110 | ПОДТВЕРЖДЕНО: недозвон сохранён открытым вопросом |
| 7 / :13 | karta-lidy.html:505, `id="p7"` | _parts/sostoyaniya.html:42, :43, :44, :117 | ПОДТВЕРЖДЕНО: повтор / дубль отражён |
| 8 / :14 | karta-lidy.html:506, `id="p8"` | _parts/sostoyaniya.html:56, :57, :58, :140, :235 | ПОДТВЕРЖДЕНО: реквизиты и частное лицо отражены; гипотеза не подтверждена клиентом |
| 9 / :15 | karta-lidy.html:507, `id="p9"` | _parts/sostoyaniya.html:63, :64, :65, :145, :194 | ПОДТВЕРЖДЕНО: выход лида и первая стадия сделки сохранены вопросами |
| 10 / :16 | karta-lidy.html:508, `id="p10"` | _parts/sostoyaniya.html:140, :247, :250 | ПОДТВЕРЖДЕНО: отсутствие структуры карточек отражено |
| 11 / :17 | karta-lidy.html:509, `id="p11"` | _parts/sostoyaniya.html:49, :50, :51, :70, :71, :72 | ПОДТВЕРЖДЕНО: отказ и отличие от исхода задачи отражены |
| 12 / :18 | karta-lidy.html:510, `id="p12"` | _parts/sostoyaniya.html:77, :78, :79, :159 | ПОДТВЕРЖДЕНО: отказ / перенос не выбран за клиента |
| 13 / :19 | karta-lidy.html:511, `id="p13"` | _parts/sostoyaniya.html:22, :167, :285 | ПОДТВЕРЖДЕНО: Распорядитель сохранён отдельной неизвестной ролью |
| 14 / :20 | karta-lidy.html:512, `id="p14"` | _parts/sostoyaniya.html:15, :43, :168, :298 | ПОДТВЕРЖДЕНО: конфликт слоя ТЗ с пересказом владельца не разрешён самовольно |
| 15 / :21 | karta-lidy.html:513, `id="p15"` | _parts/sostoyaniya.html:64, :194, :196 | ПОДТВЕРЖДЕНО: граница лид / заявка сохранена вопросом; схема — C-11 |
| 16 / :22 | karta-lidy.html:514, `id="p16"` | _parts/sostoyaniya.html:29, :186, :187, :188, :189, :201 | НЕСООТВЕТСТВИЕ C-03: таймер ожидающей задачи / отсутствие ответа; точка присутствует |

## Первичные находки

Идентификаторы и классификация получены до прежних проверок. Для ПОДТВЕРЖДЕНО серьёзность не назначается (—), поскольку дефект не установлен. S2 у НЕ ПРОВЕРЕНО обозначает значимость проверяемого тезиса, а не наличие установленной ошибки.

| ID | Класс | S | Файл:строка | Дословная цитата | Противоречит / с чем сверено | Что сломается на встрече | Предложение |
|---|---|---|---|---|---|---|---|
| C-01 | НЕСООТВЕТСТВИЕ | S2 | docs/ppo/lidy/_parts/TOCHKI.md:7 | `Каналов 8, со стрелкой в «ЛИД» только 2` | docs/ppo/lidy/_parts/karta.svg.html:85, коннектор `3458764681641805249`: `Челнокова — ЛИД (линия есть на доске, без наконечника; направление не нарисовано)` | Список точек приписывает двум связям направление, которого карта не заявляет | В списке точек заменить «стрелкой» на «связью»; направление оставить неизвестным |
| C-02 | НЕСООТВЕТСТВИЕ | S2 | docs/ppo/lidy/_parts/TOCHKI.md:11 | `лид сразу идёт к конвертации` | docs/ppo/lidy/_parts/karta.svg.html:121: `ЛИД → Конвертация: связи на доске нет, выведено по расположению` | Точка описывает прямой переход как содержание доски; карта и состояния называют его выводом по расположению | Согласовать TOCHKI с оговоркой карты: связи нет, последовательность предположена |
| C-03 | НЕСООТВЕТСТВИЕ | S1 | docs/ppo/lidy/obsledovanie-lidy.html:77, повестка, `<a href="#t16">16</a>` | `В прежнем плане: 30 минут без ответа — лид передаётся Распорядителю.` | client-materials/sanitized-tz.md:14, автоматизация задачи, условие `Ожидает исполнения`: `Если “Ожидает исполнения” >30 мин, тогда смена Исполнителя = Распорядитель + Уведомление`; также docs/ppo/lidy/_parts/sostoyaniya.html:186: `По ТЗ: задача «Ожидает исполнения» → исполнитель Распорядитель` | Клиенту предлагают другое правило: отсутствие ответа клиенту вместо пребывания задачи в статусе ожидания, передачу лида вместо смены исполнителя задачи. Взятая в работу задача без ответа не соответствует исходному условию | В повестке назвать объект и условие из ТЗ; исправить источник _parts/tochki.html:408, затем пересобрать штатно. Сейчас исходник и результат одинаково неточны, это не ошибка сборки |
| C-04 | ПОДТВЕРЖДЕНО | — | docs/ppo/lidy/_parts/TOCHKI.md:1 | `номера фиксированы, 1–16` | docs/ppo/lidy/_parts/karta.svg.html:1, `aria-label`: `конфликтные точки 1–16` | Потери точки не выявлено: список, готовая карта, короткие и подробные карточки содержат каждый номер; состояния отражены в матрице | Сохранить 16 номеров; достоверность Miro отдельно ограничена C-08 |
| C-05 | ПОДТВЕРЖДЕНО | — | client-materials/sanitized-tz.md:9 | `Исполнитель = роль Распорядитель` | docs/ppo/lidy/_parts/sostoyaniya.html:22, `ТЗ ФТ-1 Л8`: `Исполнитель = роль Распорядитель` | Историческое назначение нового клиента не заменено выдуманной должностью; роль остаётся вопросом | Различать точность передачи текста старого ТЗ и его применение сегодня |
| C-06 | ПОДТВЕРЖДЕНО | — | client-materials/sanitized-tz.md:6, предусловие | `наличия существующей карточки клиента в 1С` | docs/ppo/lidy/_parts/karta.svg.html:267, `ТЗ ФТ-1 Л2`: `наличия существующей карточки клиента в 1С` | Наличие поиска клиента в 1С в историческом слое ТЗ воспроизведено, а рядом на карте оставлена оговорка об уточнении | Не считать этот слой доказательством действующей интеграции |
| C-07 | ПОДТВЕРЖДЕНО | — | client-materials/sanitized-tz.md:14, статусы задачи | `Результирующий статус: Создать заявку /  Отменено` | docs/ppo/lidy/_parts/karta.svg.html:346, `ТЗ ФТ-1 Л12`: `Результирующий статус: Создать заявку /  Отменено` | Результаты задачи сохранены отдельно от статуса лида; «Отменено» не объявлено причиной отказа | Сохранить разделение объектов при исправлении C-03 |
| C-08 | НЕ ПРОВЕРЕНО | S2 | docs/ppo/lidy/_parts/sostoyaniya.html:4, `<b>Доска</b>` | `<b>Доска</b> — клон доски клиента «Copy of Евростекло», на ней нарисовано, как клиент хочет работать` | Внешний источник: доска Miro `Copy of Евростекло`, её объекты и комментарии; доступ запрещён объёмом C. Внутренняя оговорка docs/ppo/lidy/_parts/pasport.html:8: `Доска Романа — его представление о процессе, а не утверждённый целевой процесс.` | Внутренняя согласованность производных документов не доказывает желание клиента, количество и направление линий, отсутствие состояний, ролей или документов на реальной доске | На встрече называть это представлением автора доски. Проверку Miro здесь не выдавать за выполненную; не квалифицировать недоступность как фальсификацию |
| C-09 | НЕ ПРОВЕРЕНО | S2 | docs/ppo/lidy/karta-lidy.html:483, слой портала, `frame_0001 / frame_0021` | `портал: стадия лида «Не обработан 982» (frame_0001 / frame_0021)` | Внешний / исключённый источник: запись портала и кадры; портал, private и docs/as-is вне объёма C | Проверка текста карты не подтверждает числа, стадии и состояние портала; справочный слой уже обозначен «не как факт» | Сохранять справочную оговорку; не заявлять актуальную CRM проверенной |
| C-10 | НЕ ПРОВЕРЕНО | S2 | docs/ppo/lidy/_parts/pasport.html:30, строка `Руководитель отдела продаж, руководитель направления` | `руководитель ОП — 1 (последний лист), руководители направлений — от 3 (11.02) до 1` | Исключённая прежняя таблица сотрудников (§2 и §8 ТЗ); не открывалась | Исторические числа ролей и сравнение салонов нельзя независимо подтвердить этим объёмом; текущий состав в паспорте уже не заявлен подтверждённым | Сохранить датировку и неизвестность текущего состава; не подменять проверку запрещённого источника |
| C-11 | НЕ ПРОВЕРЕНО | S2 | docs/ppo/lidy/_parts/tochki.html:360, `ТЗ ФТ-1 Л14` / схема заявки | `Схема «Статусная модель Заявки» при этом начинается с «Создание лида» → «Новый».` | Исключённый визуальный источник: схема клиента в ТЗ. client-materials/sanitized-tz.md:1: `7 схем не включены`; в двух разрешённых текстовых выгрузках этой цепочки нет | Начало графической модели заявки не проверяется по доступным текстам. Отсутствие цепочки в текстовой выгрузке не доказывает отсутствие в оригинальной картинке | Считать графическую схему непроверенной; вопрос о границе лида сохранять открытым |

## Проверка сборки без записи исходников

Нормализация была ограниченной: у SVG сняты сгенерированные ссылки и `id` маркеров; у подробных карточек сняты дополнительные пояснения ссылок `small.see` и автоматически добавленная метка «наш вопрос (проверка полноты)». Иная разница не исключалась.

Фактический вывод read-only Python-сравнения:

```text
obsledovanie-lidy.html points= ['1', '2', '3', '13', '16', '4', '8', '15', '9', '7', '11', '12', '6', '5', '10', '14'] markers= []
karta-lidy.html points= [] markers= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
obsledovanie-lidy-podrobno.html points= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'] markers= []
map svg equals _parts after stripping generated links and marker IDs: True
detail text pasport = True
detail text sostoyaniya = True
detail text stories = True
detail text povestka = True
mapdata point keys: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
detail article 1 equal normalized _parts: True
detail article 2 equal normalized _parts: True
detail article 3 equal normalized _parts: True
detail article 4 equal normalized _parts: True
detail article 5 equal normalized _parts: True
detail article 6 equal normalized _parts: True
detail article 7 equal normalized _parts: True
detail article 8 equal normalized _parts: True
detail article 9 equal normalized _parts: True
detail article 10 equal normalized _parts: True
detail article 11 equal normalized _parts: True
detail article 12 equal normalized _parts: True
detail article 13 equal normalized _parts: True
detail article 14 equal normalized _parts: True
detail article 15 equal normalized _parts: True
detail article 16 equal normalized _parts: True
```

Дополнительно read-only сопоставление всех 16 карточек дало для каждого номера: `short_title=True`, `short_question=True`, `mapdata_title=True`, `mapdata_question=True`, `states_marker=True`. Полная выполняемая команда и все 16 строк фактического вывода — в `C-grep.log`, раздел «Структурное сравнение». Ниже приведена та же команда и её сводный фактический вывод.

```bash
python3 - <<'PY'
from pathlib import Path
import re, html, json
p = Path('docs/ppo/lidy')
source = (p/'_parts/tochki.html').read_text()
short = (p/'obsledovanie-lidy.html').read_text()
detail = (p/'obsledovanie-lidy-podrobno.html').read_text()
mp = (p/'karta-lidy.html').read_text()
states = (p/'_parts/sostoyaniya.html').read_text()
def txt(x):
    x = re.sub(r'<small class="see">.*?</small>', '', x, flags=re.S)
    x = re.sub(r'<small class="src">наш вопрос \(проверка полноты\)</small>', '', x)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip()
svg = re.search(r'<svg class="map".*?</svg>', mp, re.S).group()
svg = re.sub(r'<a href="obsledovanie-lidy.html#t\d+" target="evro-obsl">(<g class="pt ptlink" id="p\d+">.*?</g>)</a>', r'\1', svg, flags=re.S)
svg = re.sub(r'<g class="pt ptlink" id="p\d+">', '<g class="pt">', svg)
print('svg_equal:', svg == (p/'_parts/karta.svg.html').read_text().strip())
for file, ids in [('pasport.html', ['pasport']), ('sostoyaniya.html', ['sostoyaniya', 'stories']), ('tochki.html', ['povestka'])]:
    for identity in ids:
        rx = r'<section id="'+identity+r'">.*?</section>'
        print(identity+'_text_equal:', txt(re.search(rx, (p/'_parts'/file).read_text(), re.S).group()) == txt(re.search(rx, detail, re.S).group()))
data = json.loads(re.search(r'<script type="application/json" id="mapdata">(.*?)</script>', mp, re.S).group(1))
nums = list(range(1, 17))
point_sets = [re.findall(r'^\| (\d+) \|', (p/'_parts/TOCHKI.md').read_text(), re.M)]
point_sets += [re.findall(rx, text) for rx, text in [(r'<g\b[^>]*\bid="p(\d+)"', mp), (r'<article\b[^>]*\bid="t(\d+)"', short), (r'<article\b[^>]*\bid="t(\d+)"', detail)]]
print('point_sets_equal:', all(sorted(map(int, x)) == nums for x in point_sets))
ok = []
for n in nums:
    rx = r'<article[^>]*id="t'+str(n)+r'">.*?</article>'
    a, b, d = [re.search(rx, x, re.S).group() for x in [source, short, detail]]
    q = txt(re.search(r'<dd class="q">(.*?)</dd>', a, re.S).group(1))
    title = txt(re.search(r'<h3>(.*?)</h3>', a, re.S).group(1))
    row = [txt(a) == txt(d), q == txt(re.search(r'<p class="ask">(.*?)</p>', b, re.S).group(1)), title == txt(re.search(r'<h3>(.*?)</h3>', b, re.S).group(1)), q == data['cards'][str(n)]['q'], title == data['cards'][str(n)]['title'], f'<span class="pt">{n}</span>' in states]
    ok.append(all(row))
    print('point', n, 'detail_text,short_q,short_title,map_q,map_title,state:', row)
print('all_point_checks:', sum(ok), '/', len(ok))
PY
```

```text
svg_equal: True
pasport_text_equal: True
sostoyaniya_text_equal: True
stories_text_equal: True
povestka_text_equal: True
point_sets_equal: True
point 1–16: каждая строка [True, True, True, True, True, True] (полные строки в C-grep.log)
all_point_checks: 16 / 16
```

Сборка не запускалась. Это проверка конкретных фрагментов, не проверка браузерного поведения всех управляющих элементов. По этой проверке самостоятельного расхождения сборки с первичными фрагментами не обнаружено.

## Расхождения с прежней проверкой

Только после первичной фиксации прочитаны все 192 строки FACTCHECK и 56 строк audit. Даты различаются: FACTCHECK относится к 28.09 и 12 точкам, нынешний список — к 16. Его старые номера K/Q не перенесены как номера нынешних строк.

| Прежняя проверка / точная цитата | Свежая сверка / точная цитата | Отношение к независимому выводу |
|---|---|---|
| docs/ppo/lidy/_parts/FACTCHECK-karta.md:87: `лучше «связь» вместо «стрелки»: наконечников на доске нет` (при вердикте ИСТИНА) | docs/ppo/lidy/_parts/TOCHKI.md:7: `Каналов 8, со стрелкой в «ЛИД» только 2` | C-01: прежняя рекомендация реализована в карте и карточке, но осталась невыполненной в общем списке. Внутреннее расхождение сохранено |
| docs/ppo/lidy/_parts/FACTCHECK-karta.md:184: `**Точка 5:** «лид сразу идёт к конвертации» — на доске связи нет.` | docs/ppo/lidy/_parts/TOCHKI.md:11: `лид сразу идёт к конвертации` | C-02: совпадение независимых выводов. Карта и состояния исправлены, общий список сохранил старое утверждение |
| docs/ppo/lidy/_parts/FACTCHECK-karta.md:136: `## 3. Проверка 12 вопросов` | docs/ppo/lidy/_parts/TOCHKI.md:1: `номера фиксированы, 1–16` | C-04: прежняя проверка не покрывает четыре добавленные точки 13–16; это различие срезов, а не фальсификация старого отчёта |
| docs/ppo/lidy/_parts/FACTCHECK-karta.md:106: `**(в) 982 / 291 / 1552 и 5 стадий: ИСТИНА.**` | docs/ppo/lidy/karta-lidy.html:483: `портал: стадия лида «Не обработан 982» (frame_0001 / frame_0021)` | C-09: нынешний вердикт НЕ ПРОВЕРЕНО относится к недоступности записи/портала в этом объёме. Пересказ прежнего вердикта не является повторной независимой проверкой |
| docs/ppo/lidy/_parts/audit-lidy.md:5: `На карте лидов слой «В. Портал» (справочно) пока оставлен` | docs/ppo/lidy/_parts/karta.svg.html:368: `В. Портал — справочно, для аудита интегратора` | Наличие портального слоя сознательно сохранено; C-09 не объявляет его запрещённой или ложной вставкой. Маркеры 2 и 5 также сознательно оставлены в его полосе |

Старый FACTCHECK не проверял нынешнюю повестку и условие C-03: он ограничен 12 вопросами и датой 28.09. audit-lidy.md — перечень снятого и будущих вопросов, а не доказательство текущей настройки CRM.

## Самопроверка и ограничения

**Перепроверено 33 из 33 цитатных вхождений**: 21 из 21 в таблице находок, 10 из 10 в сравнении с прежней проверкой и 2 из 2 в снятом кандидате B2C. Для каждого реально выполнен `grep -n -F -e`; найден ожидаемый номер строки. Команды и полный исходный вывод — `C-grep.log`. Структурная проверка — 16 из 16 точек.

Итог блока: НЕСООТВЕТСТВИЕ — C-01, C-02 (S2), C-03 (S1); ПОДТВЕРЖДЕНО — C-04–C-07 (—); НЕ ПРОВЕРЕНО — C-08–C-11 (S2). РАЗРЫВ ДАННЫХ и ФАЛЬСИФИКАЦИЯ по этому проходу не установлены. S1 = 1, S2 = 6, S3 = 0; подтверждений без серьёзности = 4; это 11 записей, из них 3 установленных расхождения.
Запрещённые источники, сеть, bd, Git-запись, исполнители и дополнительные субагенты не использовались. Реестры конфликтов и журнал решений вне блока C самостоятельно не проверялись: сквозная сверка принадлежит A/D.
Предварительный кандидат B2C «у него нет карточки компании» не включён в ошибки: в полном контексте это исключение внутри строки с чипом «не знаем» (_parts/sostoyaniya.html:235), а карта помечает применимость как наш вывод. Без проверки источника К-26 установленного противоречия нет.

## Фактические команды цитатной проверки

```text
C — actual command evidence; source SHA follows.
$ git rev-parse HEAD
9690df60bfecfdd5839946f0ca12d9392a2359f3
[exit=0]
$ git diff --stat d68c37f HEAD -- docs/ppo docs/CHECKPOINTS.md client-materials
[exit=0]
$ git ls-files docs/ppo/lidy
docs/ppo/lidy/_parts/FACTCHECK-karta.md
docs/ppo/lidy/_parts/TOCHKI.md
docs/ppo/lidy/_parts/audit-lidy.md
docs/ppo/lidy/_parts/build.py
docs/ppo/lidy/_parts/karta.svg.html
docs/ppo/lidy/_parts/pasport.html
docs/ppo/lidy/_parts/povestka-vladeltsu.md
docs/ppo/lidy/_parts/sostoyaniya.html
docs/ppo/lidy/_parts/tochki.html
docs/ppo/lidy/karta-lidy.html
docs/ppo/lidy/obsledovanie-lidy-podrobno.html
docs/ppo/lidy/obsledovanie-lidy.html
[exit=0]
$ wc -l docs/ppo/lidy/_parts/FACTCHECK-karta.md docs/ppo/lidy/_parts/TOCHKI.md docs/ppo/lidy/_parts/audit-lidy.md docs/ppo/lidy/_parts/build.py docs/ppo/lidy/_parts/karta.svg.html docs/ppo/lidy/_parts/pasport.html docs/ppo/lidy/_parts/povestka-vladeltsu.md docs/ppo/lidy/_parts/sostoyaniya.html docs/ppo/lidy/_parts/tochki.html docs/ppo/lidy/karta-lidy.html docs/ppo/lidy/obsledovanie-lidy-podrobno.html docs/ppo/lidy/obsledovanie-lidy.html client-materials/sanitized-tz.md client-materials/sanitized-statusy.md
   192 docs/ppo/lidy/_parts/FACTCHECK-karta.md
    43 docs/ppo/lidy/_parts/TOCHKI.md
    56 docs/ppo/lidy/_parts/audit-lidy.md
     6 docs/ppo/lidy/_parts/build.py
   418 docs/ppo/lidy/_parts/karta.svg.html
    40 docs/ppo/lidy/_parts/pasport.html
    68 docs/ppo/lidy/_parts/povestka-vladeltsu.md
   305 docs/ppo/lidy/_parts/sostoyaniya.html
   419 docs/ppo/lidy/_parts/tochki.html
   915 docs/ppo/lidy/karta-lidy.html
   852 docs/ppo/lidy/obsledovanie-lidy-podrobno.html
   496 docs/ppo/lidy/obsledovanie-lidy.html
    45 client-materials/sanitized-tz.md
    48 client-materials/sanitized-statusy.md
  3903 total
[exit=0]
$ rg -c '^\| [0-9]+ \|' docs/ppo/lidy/_parts/TOCHKI.md
16
[exit=0]
$ rg -n '^\| [0-9]+ \|' docs/ppo/lidy/_parts/TOCHKI.md
7:| 1 | Каналов 8, со стрелкой в «ЛИД» только 2 (Челнокова, Авито) — как попадают остальные | предусловие (вход) | дорожка «Каналы» | П-03, Р-07, К-28; коннекторы 3458764681641805249, 3458764681641922880 |
8:| 2 | Источники лида: на доске — каналы (салоны, сарафан, vk.ru, Telegram, Авито), в ТЗ — «АТС», «Почта», «Восстановление»; общего справочника нет | разный уровень (доска ↔ ТЗ) | полоса «Портал» (маркер пока там) | К-28; ТЗ ФТ-1 Л4, Л5 |
9:| 3 | Кто разбирает лид и за какой срок — роль не названа | роль | дорожка «? кто разбирает» | П-02, Р-07; RACI s1 «A?» |
10:| 4 | В названии рамки «B2B, B2C», а путь один | развилка | рамка «ЛИД» | Р-07, К-26 |
11:| 5 | Состояния лида: на доске их нет (лид сразу идёт к конвертации), в ТЗ — один статус «Новый», движется задача | состояние | полоса «Портал» (маркер пока там) | Р-06; ТЗ ФТ-1 Л7, Л12 |
12:| 6 | Недозвон — на доске нет: сколько попыток, куда уходит лид | развилка / сценарий | после «ЛИД» | Р-06 |
13:| 7 | Повторная заявка / клиент уже есть в базе — не описано | сценарий | перед конвертацией | Р-08; prosto/2-voprosy РОП в.5 |
14:| 8 | «Обязательно все реквизиты в карточку компании» — состава нет; у B2C-физлица компании нет | предусловие (готовность к конвертации) | узел «Конвертация» 3074457358430916255 | П-01, К-26, к.7365 |
15:| 9 | Что есть после конвертации: сделка на какой стадии; «Предв. расчёт» левее «Заявки», стрелок между стадиями нет | постусловие | выход в «Предварительный расчёт» 3074457358430445405 | К-02, П-44 |
16:| 10 | «Единый формат контрагента» и «структура карточек (от Л.А., М.А.)» — самих документов нет; «от» ≠ «одобрено» | документ / user story | рамка «Битрикс24» 3074457358429708946 | К-32; к.7350, к.7365 |
17:| 11 | Отказ: «Воронка отказников» и 4 причины без связей на доске; в ТЗ у лида только «Отменено» без причины | развилка | ромб 3074457358431590461 | П-05, Р-01, Р-02, К-13; ТЗ ФТ-1 Л12 |
18:| 12 | «Закупка отложена» лежит среди причин отказа, но по смыслу это перенос | состояние | причина 3074457358431099077 | Р-03 |
19:| 13 | «Распорядитель» — кто это: по ТЗ исполнитель нового лида, в ТЗ не расшифрован, на доске нет | роль | дорожка «по ТЗ» | ТЗ ФТ-1 Л8, Л13 (`client-materials/sanitized-tz.md`); владелец 28.09: неизвестно |
20:| 14 | 1С в лидах: по ТЗ поиск клиента в 1С по телефону/почте и исполнитель из 1С; владелец: 1С только в сделках (воронка «Активные») | противоречие (ТЗ ↔ владелец) | дорожка «по ТЗ», блок «1С — уточнить» | ТЗ ФТ-1 предусловие, альт. сценарий 1; `docs/ppo/00-resheniya-vladeltsa.md` |
21:| 15 | Лид или заявка: по ТЗ статус «Новый», задача «Созвониться с клиентом» → «Создать заявку» / «Отменено»; модель заявки начинается с «Создание лида → Новый» — где кончается лид | постусловие / состояние | дорожка «по ТЗ» | ТЗ ФТ-1 Л7, Л12; схема «Статусная модель Заявки»; r-tz В1 |
22:| 16 | Задача не взята 30 минут → передаётся Распорядителю; что с лидом при «Отменено» — не сказано | развилка | дорожка «по ТЗ» | ТЗ ФТ-1 Л13, Л12 |
[exit=0]

Citation checks; grep command prints complete actual source line.

## C-01a; expected docs/ppo/lidy/_parts/TOCHKI.md:7; quote_length=39
$ grep -n -F -e 'Каналов 8, со стрелкой в «ЛИД» только 2' docs/ppo/lidy/_parts/TOCHKI.md
7:| 1 | Каналов 8, со стрелкой в «ЛИД» только 2 (Челнокова, Авито) — как попадают остальные | предусловие (вход) | дорожка «Каналы» | П-03, Р-07, К-28; коннекторы 3458764681641805249, 3458764681641922880 |
[exit=0; expected_line_found=True]

## C-01b; expected docs/ppo/lidy/_parts/karta.svg.html:85; quote_length=81
$ grep -n -F -e 'Челнокова — ЛИД (линия есть на доске, без наконечника; направление не нарисовано)' docs/ppo/lidy/_parts/karta.svg.html
85:<g><title>коннектор Miro 3458764681641805249: Челнокова — ЛИД (линия есть на доске, без наконечника; направление не нарисовано)</title>
[exit=0; expected_line_found=True]

## C-02a; expected docs/ppo/lidy/_parts/TOCHKI.md:11; quote_length=28
$ grep -n -F -e 'лид сразу идёт к конвертации' docs/ppo/lidy/_parts/TOCHKI.md
11:| 5 | Состояния лида: на доске их нет (лид сразу идёт к конвертации), в ТЗ — один статус «Новый», движется задача | состояние | полоса «Портал» (маркер пока там) | Р-06; ТЗ ФТ-1 Л7, Л12 |
[exit=0; expected_line_found=True]

## C-02b; expected docs/ppo/lidy/_parts/karta.svg.html:121; quote_length=63
$ grep -n -F -e 'ЛИД → Конвертация: связи на доске нет, выведено по расположению' docs/ppo/lidy/_parts/karta.svg.html
121:<g><title>ЛИД → Конвертация: связи на доске нет, выведено по расположению</title>
[exit=0; expected_line_found=True]

## C-03a; expected docs/ppo/lidy/obsledovanie-lidy.html:77; quote_length=68
$ grep -n -F -e 'В прежнем плане: 30 минут без ответа — лид передаётся Распорядителю.' docs/ppo/lidy/obsledovanie-lidy.html
77:<li><a href="#t3">Точки 3</a>, <a href="#t13">13</a> и <a href="#t16">16</a> — кто первым взял последний лид и через сколько ответил клиенту; кто такой «Распорядитель». В прежнем плане: 30 минут без ответа — лид передаётся Распорядителю. Это нужно? Вечер, выходные, отпуск — одно правило для лидов и сделок?</li>
[exit=0; expected_line_found=True]

## C-03b; expected client-materials/sanitized-tz.md:14; quote_length=88
$ grep -n -F -e 'Если “Ожидает исполнения” >30 мин, тогда смена Исполнителя = Распорядитель + Уведомление' client-materials/sanitized-tz.md
14:– Статус: "Новый"– Исполнитель = ID менеджера (указывается вручную) – Заполняются базовые поля = значения из полей 1САвтоматизация: При событии “Создан лид” формируется задача на менеджера “Созвонится с клиентом” Статусы задачи - Ожидает исполнения / В работе /  → Результирующий статус: Создать заявку /  ОтмененоЕсли “Ожидает исполнения” >30 мин, тогда смена Исполнителя = Распорядитель + УведомлениеПостусловия: Заявка созданасхема регистрация и маршрутизация нового обращения
[exit=0; expected_line_found=True]

## C-03c; expected docs/ppo/lidy/_parts/sostoyaniya.html:186; quote_length=62
$ grep -n -F -e 'По ТЗ: задача «Ожидает исполнения» → исполнитель Распорядитель' docs/ppo/lidy/_parts/sostoyaniya.html
186:<td>По ТЗ: задача «Ожидает исполнения» → исполнитель Распорядитель</td>
[exit=0; expected_line_found=True]

## C-04a; expected docs/ppo/lidy/_parts/TOCHKI.md:1; quote_length=24
$ grep -n -F -e 'номера фиксированы, 1–16' docs/ppo/lidy/_parts/TOCHKI.md
1:# Конфликтные точки процесса «Лиды» — общий список (номера фиксированы, 1–16)
[exit=0; expected_line_found=True]

## C-04b; expected docs/ppo/lidy/_parts/karta.svg.html:1; quote_length=22
$ grep -n -F -e 'конфликтные точки 1–16' docs/ppo/lidy/_parts/karta.svg.html
1:<svg class="map" viewBox="0 0 2300 1880" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Карта процесса «Лиды» Евростекла в упрощённом BPMN, три слоя: доска Романа (предположение), ТЗ ФТ-1 (как задумано), портал (справочно); конфликтные точки 1–16">
[exit=0; expected_line_found=True]

## C-05a; expected client-materials/sanitized-tz.md:9; quote_length=32
$ grep -n -F -e 'Исполнитель = роль Распорядитель' client-materials/sanitized-tz.md
9:– Статус: "Новый"– Исполнитель = роль Распорядитель– Уведомление на ИсполнительАльтернативный сценарий №1: Определена существующая карточка клиента в 1с.Система создает лид с полями: – Источник (автоподстановка: "АТС", "Почта")
[exit=0; expected_line_found=True]

## C-05b; expected docs/ppo/lidy/_parts/sostoyaniya.html:22; quote_length=32
$ grep -n -F -e 'Исполнитель = роль Распорядитель' docs/ppo/lidy/_parts/sostoyaniya.html
22:<td>«Статус: "Новый"» <small class="src">ТЗ ФТ-1 Л7</small>. Исполнитель: новый клиент — «Исполнитель = роль Распорядитель» <small class="src">ТЗ ФТ-1 Л8</small>, клиент найден в 1С — «Исполнитель = ID менеджера (1с)» <small class="src">ТЗ ФТ-1 Л9</small>; уведомление исполнителю. Сразу создаётся задача «Созвонится с клиентом» <small class="src">ТЗ ФТ-1 Л11</small> <span class="pt">3</span> <span class="pt">13</span> <span class="pt">15</span></td>
284:<tr><th>Взято из ТЗ</th><td>«Исполнитель = роль Распорядитель– Уведомление на Исполнитель» <small class="src">ТЗ ФТ-1 Л8</small>; «Если “Ожидает исполнения” &gt;30 мин, тогда смена Исполнителя = Распорядитель + Уведомление» <small class="src">ТЗ ФТ-1 Л13</small></td></tr>
[exit=0; expected_line_found=True]

## C-06a; expected client-materials/sanitized-tz.md:6; quote_length=42
$ grep -n -F -e 'наличия существующей карточки клиента в 1С' client-materials/sanitized-tz.md
6:Функциональное требование “Регистрация и маршрутизация нового обращения”Предусловия: Поступило входящее обращение от нового клиента. Битрикс24 далее (Система) синхронизирована с 1с. Запущена валидация наличия существующей карточки клиента в 1С по номеру телефона ( 3 цифра с начала и далее)  / почты Основной сценарий: Поступила заявка на заказ посредством звонка ( виртуальная АТС) или корпоративной почты. Система автоматически создает лид с полями:
[exit=0; expected_line_found=True]

## C-06b; expected docs/ppo/lidy/_parts/karta.svg.html:267; quote_length=42
$ grep -n -F -e 'наличия существующей карточки клиента в 1С' docs/ppo/lidy/_parts/karta.svg.html
267:<g><title>ТЗ ФТ-1 Л2: «Запущена валидация наличия существующей карточки клиента в 1С по номеру телефона ( 3 цифра с начала и далее)  / почты»</title>
[exit=0; expected_line_found=True]

## C-07a; expected client-materials/sanitized-tz.md:14; quote_length=49
$ grep -n -F -e 'Результирующий статус: Создать заявку /  Отменено' client-materials/sanitized-tz.md
14:– Статус: "Новый"– Исполнитель = ID менеджера (указывается вручную) – Заполняются базовые поля = значения из полей 1САвтоматизация: При событии “Создан лид” формируется задача на менеджера “Созвонится с клиентом” Статусы задачи - Ожидает исполнения / В работе /  → Результирующий статус: Создать заявку /  ОтмененоЕсли “Ожидает исполнения” >30 мин, тогда смена Исполнителя = Распорядитель + УведомлениеПостусловия: Заявка созданасхема регистрация и маршрутизация нового обращения
[exit=0; expected_line_found=True]

## C-07b; expected docs/ppo/lidy/_parts/karta.svg.html:346; quote_length=49
$ grep -n -F -e 'Результирующий статус: Создать заявку /  Отменено' docs/ppo/lidy/_parts/karta.svg.html
346:<g><title>ТЗ ФТ-1 Л12: «→ Результирующий статус: Создать заявку /  Отменено»</title>
[exit=0; expected_line_found=True]

## C-08a; expected docs/ppo/lidy/_parts/sostoyaniya.html:4; quote_length=100
$ grep -n -F -e '<b>Доска</b> — клон доски клиента «Copy of Евростекло», на ней нарисовано, как клиент хочет работать' docs/ppo/lidy/_parts/sostoyaniya.html
4:<p>Сравниваем два источника. <b>Доска</b> — клон доски клиента «Copy of Евростекло», на ней нарисовано, как клиент хочет работать <small class="src">TOCHKI.md:3</small>. <b>ТЗ 2024–2025</b> — старое ТЗ клиента, раздел ФТ-1 «Регистрация и маршрутизация нового обращения»: как было задумано, базовая линия; клиентом не подтверждено <small class="src">client-materials/sanitized-tz.md; 00-resheniya-vladeltsa.md; Л1–Л15 — номера правил из разбора ТЗ</small>. Главное расхождение: на доске у лида нет промежуточных состояний и нет связи с «Конвертацией» (они только стоят рядом), по ТЗ у лида один статус «Новый», а движется задача «Созвонится с клиентом»: «Ожидает исполнения / В работе / Создать заявку / Отменено» <small class="src">TOCHKI.md:11; фактчек, точка 5; ТЗ ФТ-1 Л7, Л12</small>.</p>
[exit=0; expected_line_found=True]

## C-08b; expected docs/ppo/lidy/_parts/pasport.html:8; quote_length=79
$ grep -n -F -e 'Доска Романа — его представление о процессе, а не утверждённый целевой процесс.' docs/ppo/lidy/_parts/pasport.html
8:<tr><td>Доска Романа — его представление о процессе, а не утверждённый целевой процесс. Расхождения доски и ТЗ выносим клиенту вопросом «какой вариант верный сейчас» <small class="src">решение владельца 28.09</small></td><td><span class="st st-own">решение владельца</span></td></tr>
[exit=0; expected_line_found=True]

## C-09a; expected docs/ppo/lidy/karta-lidy.html:483; quote_length=64
$ grep -n -F -e 'портал: стадия лида «Не обработан 982» (frame_0001 / frame_0021)' docs/ppo/lidy/karta-lidy.html
483:<g><title>портал: стадия лида «Не обработан 982» (frame_0001 / frame_0021)</title><rect x="620" y="1716" width="170" height="30" rx="6" class="chip"/>
[exit=0; expected_line_found=True]

## C-10a; expected docs/ppo/lidy/_parts/pasport.html:30; quote_length=82
$ grep -n -F -e 'руководитель ОП — 1 (последний лист), руководители направлений — от 3 (11.02) до 1' docs/ppo/lidy/_parts/pasport.html
30:<tr><td>Руководитель отдела продаж, руководитель направления</td><td>список сотрудников 2024–2025: руководитель ОП — 1 (последний лист), руководители направлений — от 3 (11.02) до 1</td><td>Роль в лидах не описана <small class="src">sanitized-sotrudniki.md; разбор оргструктуры</small></td><td><span class="st st-unk">не знаем</span></td></tr>
[exit=0; expected_line_found=True]

## C-11a; expected docs/ppo/lidy/_parts/tochki.html:360; quote_length=80
$ grep -n -F -e 'Схема «Статусная модель Заявки» при этом начинается с «Создание лида» → «Новый».' docs/ppo/lidy/_parts/tochki.html
360:<dd>У лида «Статус: "Новый"» <small class="src">ТЗ ФТ-1 Л7</small>; задача заканчивается статусом «Создать заявку / Отменено» <small class="src">ТЗ ФТ-1 Л12</small>; «Постусловия: Заявка создана» <small class="src">ТЗ ФТ-1 Л14</small>. Схема «Статусная модель Заявки» при этом начинается с «Создание лида» → «Новый». Где кончается лид и начинается заявка, и заявка — это сделка или что-то другое, в ТЗ не сказано. <span class="st st-conf">противоречие</span> <small class="src">разбор ТЗ В1</small></dd>
[exit=0; expected_line_found=True]

## C-11b; expected client-materials/sanitized-tz.md:1; quote_length=18
$ grep -n -F -e '7 схем не включены' client-materials/sanitized-tz.md
1:# Старое ТЗ (текст из docx клиента, 7 схем не включены)
[exit=0; expected_line_found=True]

## PREV-1a; expected docs/ppo/lidy/_parts/FACTCHECK-karta.md:87; quote_length=57
$ grep -n -F -e 'лучше «связь» вместо «стрелки»: наконечников на доске нет' docs/ppo/lidy/_parts/FACTCHECK-karta.md
87:| 1 | 8 каналов, «со стрелкой» в ЛИД только 2 (Челнокова, Авито) | коннекторы `…805249`, `…922880`; k1 П-03 | ИСТИНА | лучше «связь» вместо «стрелки»: наконечников на доске нет |
[exit=0; expected_line_found=True]

## PREV-1b; expected docs/ppo/lidy/_parts/TOCHKI.md:7; quote_length=39
$ grep -n -F -e 'Каналов 8, со стрелкой в «ЛИД» только 2' docs/ppo/lidy/_parts/TOCHKI.md
7:| 1 | Каналов 8, со стрелкой в «ЛИД» только 2 (Челнокова, Авито) — как попадают остальные | предусловие (вход) | дорожка «Каналы» | П-03, Р-07, К-28; коннекторы 3458764681641805249, 3458764681641922880 |
[exit=0; expected_line_found=True]

## PREV-2a; expected docs/ppo/lidy/_parts/FACTCHECK-karta.md:184; quote_length=65
$ grep -n -F -e '**Точка 5:** «лид сразу идёт к конвертации» — на доске связи нет.' docs/ppo/lidy/_parts/FACTCHECK-karta.md
184:9. **Точка 5:** «лид сразу идёт к конвертации» — на доске связи нет.
[exit=0; expected_line_found=True]

## PREV-2b; expected docs/ppo/lidy/_parts/TOCHKI.md:11; quote_length=28
$ grep -n -F -e 'лид сразу идёт к конвертации' docs/ppo/lidy/_parts/TOCHKI.md
11:| 5 | Состояния лида: на доске их нет (лид сразу идёт к конвертации), в ТЗ — один статус «Новый», движется задача | состояние | полоса «Портал» (маркер пока там) | Р-06; ТЗ ФТ-1 Л7, Л12 |
[exit=0; expected_line_found=True]

## PREV-3a; expected docs/ppo/lidy/_parts/FACTCHECK-karta.md:136; quote_length=26
$ grep -n -F -e '## 3. Проверка 12 вопросов' docs/ppo/lidy/_parts/FACTCHECK-karta.md
136:## 3. Проверка 12 вопросов (`dd.q` в tochki.html)
[exit=0; expected_line_found=True]

## PREV-3b; expected docs/ppo/lidy/_parts/TOCHKI.md:1; quote_length=24
$ grep -n -F -e 'номера фиксированы, 1–16' docs/ppo/lidy/_parts/TOCHKI.md
1:# Конфликтные точки процесса «Лиды» — общий список (номера фиксированы, 1–16)
[exit=0; expected_line_found=True]

## PREV-4a; expected docs/ppo/lidy/_parts/FACTCHECK-karta.md:106; quote_length=44
$ grep -n -F -e '**(в) 982 / 291 / 1552 и 5 стадий: ИСТИНА.**' docs/ppo/lidy/_parts/FACTCHECK-karta.md
106:**(в) 982 / 291 / 1552 и 5 стадий: ИСТИНА.** ASIS:19–20 (frame_0001: «Не обработан 982», «В работе 291», «Обработан 1552»; frame_0021: «Некачественный лид», «Качественный лид»). Ошибка есть только в переходах между стадиями на карте (строки 63–64): развилка «Обработан → Кач/Некач» источника не имеет.
[exit=0; expected_line_found=True]

## PREV-4b; expected docs/ppo/lidy/karta-lidy.html:483; quote_length=64
$ grep -n -F -e 'портал: стадия лида «Не обработан 982» (frame_0001 / frame_0021)' docs/ppo/lidy/karta-lidy.html
483:<g><title>портал: стадия лида «Не обработан 982» (frame_0001 / frame_0021)</title><rect x="620" y="1716" width="170" height="30" rx="6" class="chip"/>
[exit=0; expected_line_found=True]

## PREV-5a; expected docs/ppo/lidy/_parts/audit-lidy.md:5; quote_length=57
$ grep -n -F -e 'На карте лидов слой «В. Портал» (справочно) пока оставлен' docs/ppo/lidy/_parts/audit-lidy.md
5:Это **список**, а не документ для интегратора: документ пишем только по команде владельца «Дай мне специальный документ для интегратора» (журнал 28.09). Всё ниже снято с клиентских фрагментов лидов (`tochki.html`, `pasport.html`, `sostoyaniya.html`, подсказки маркеров `karta.svg.html`). Источник всех строк — `docs/as-is/2026-09-28-portal-as-is.md` (as-is стр. N = номер строки; запись экрана и речь прежнего интегратора, метка «со слов», портал мы не открывали). На карте лидов слой «В. Портал» (справочно) пока оставлен — снимается при проверке карты по методике А после встречи.
[exit=0; expected_line_found=True]

## PREV-5b; expected docs/ppo/lidy/_parts/karta.svg.html:368; quote_length=45
$ grep -n -F -e 'В. Портал — справочно, для аудита интегратора' docs/ppo/lidy/_parts/karta.svg.html
368:<text x="40" y="1670" class="pgb" text-anchor="start">В. Портал — справочно, для аудита интегратора</text>
[exit=0; expected_line_found=True]

## CTX-B2C-1; expected docs/ppo/lidy/_parts/sostoyaniya.html:235; quote_length=112
$ grep -n -F -e '<th>Нет исключений</th><td><span class="st st-unk">не знаем</span> Частное лицо — у него нет «карточки компании»' docs/ppo/lidy/_parts/sostoyaniya.html
235:<tr><th>Нет исключений</th><td><span class="st st-unk">не знаем</span> Частное лицо — у него нет «карточки компании»; клиент пока не даёт реквизиты; компания уже есть в базе <span class="pt">7</span> <span class="pt">8</span> <small class="src">k3-conflicts.md:66; k2-forks.md:32</small></td></tr>
[exit=0; expected_line_found=True]

## CTX-B2C-2; expected docs/ppo/lidy/_parts/tochki.html:189; quote_length=101
$ grep -n -F -e 'Есть ли у частного лица карточка компании и реквизиты вроде ИНН — не знаем (наш вывод: может не быть;' docs/ppo/lidy/_parts/tochki.html
189:<dd>Состав «всех реквизитов» нигде не дан. Есть ли у частного лица карточка компании и реквизиты вроде ИНН — не знаем (наш вывод: может не быть; применимость к частным лицам в К-26 записана как «не знаем»). <small class="src">k1 П-01; k3 К-26</small></dd>
[exit=0; expected_line_found=True]

Structural comparison — read-only source text, no build.
$ python3 - <<'PY'
from pathlib import Path
import re, html, json
p = Path('docs/ppo/lidy')
source = (p/'_parts/tochki.html').read_text()
short = (p/'obsledovanie-lidy.html').read_text()
detail = (p/'obsledovanie-lidy-podrobno.html').read_text()
mp = (p/'karta-lidy.html').read_text()
states = (p/'_parts/sostoyaniya.html').read_text()
def txt(x):
    x = re.sub(r'<small class="see">.*?</small>', '', x, flags=re.S)
    x = re.sub(r'<small class="src">наш вопрос \(проверка полноты\)</small>', '', x)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip()
svg = re.search(r'<svg class="map".*?</svg>', mp, re.S).group()
svg = re.sub(r'<a href="obsledovanie-lidy.html#t\d+" target="evro-obsl">(<g class="pt ptlink" id="p\d+">.*?</g>)</a>', r'\1', svg, flags=re.S)
svg = re.sub(r'<g class="pt ptlink" id="p\d+">', '<g class="pt">', svg)
print('svg_equal:', svg == (p/'_parts/karta.svg.html').read_text().strip())
for file, ids in [('pasport.html', ['pasport']), ('sostoyaniya.html', ['sostoyaniya', 'stories']), ('tochki.html', ['povestka'])]:
    for identity in ids:
        rx = r'<section id="'+identity+r'">.*?</section>'
        print(identity+'_text_equal:', txt(re.search(rx, (p/'_parts'/file).read_text(), re.S).group()) == txt(re.search(rx, detail, re.S).group()))
data = json.loads(re.search(r'<script type="application/json" id="mapdata">(.*?)</script>', mp, re.S).group(1))
nums = list(range(1, 17))
point_sets = [re.findall(r'^\| (\d+) \|', (p/'_parts/TOCHKI.md').read_text(), re.M)]
point_sets += [re.findall(rx, text) for rx, text in [(r'<g\b[^>]*\bid="p(\d+)"', mp), (r'<article\b[^>]*\bid="t(\d+)"', short), (r'<article\b[^>]*\bid="t(\d+)"', detail)]]
print('point_sets_equal:', all(sorted(map(int, x)) == nums for x in point_sets))
ok = []
for n in nums:
    rx = r'<article[^>]*id="t'+str(n)+r'">.*?</article>'
    a, b, d = [re.search(rx, x, re.S).group() for x in [source, short, detail]]
    q = txt(re.search(r'<dd class="q">(.*?)</dd>', a, re.S).group(1))
    title = txt(re.search(r'<h3>(.*?)</h3>', a, re.S).group(1))
    row = [txt(a) == txt(d), q == txt(re.search(r'<p class="ask">(.*?)</p>', b, re.S).group(1)), title == txt(re.search(r'<h3>(.*?)</h3>', b, re.S).group(1)), q == data['cards'][str(n)]['q'], title == data['cards'][str(n)]['title'], f'<span class="pt">{n}</span>' in states]
    ok.append(all(row))
    print('point', n, 'detail_text,short_q,short_title,map_q,map_title,state:', row)
print('all_point_checks:', sum(ok), '/', len(ok))
PY
svg_equal: True
pasport_text_equal: True
sostoyaniya_text_equal: True
stories_text_equal: True
povestka_text_equal: True
point_sets_equal: True
point 1 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 2 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 3 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 4 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 5 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 6 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 7 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 8 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 9 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 10 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 11 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 12 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 13 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 14 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 15 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
point 16 detail_text,short_q,short_title,map_q,map_title,state: [True, True, True, True, True, True]
all_point_checks: 16 / 16
[exit=0]
$ rg -n 'Создание лида|Статусная модель Заявки' client-materials/sanitized-tz.md client-materials/sanitized-statusy.md
[exit=1]

SUMMARY: citation_checks=33/33; primary_findings=21/21; previous=10/10; context=2/2; structural=16/16.
```
