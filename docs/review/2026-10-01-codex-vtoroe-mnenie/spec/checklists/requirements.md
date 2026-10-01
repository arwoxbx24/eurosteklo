# Чеклист качества спецификации критики

Дата: 2026-10-01. Основание: [spec.md](../spec.md); единственный канонический паспорт — [неизменное ТЗ](../../../../plans/2026-10-01-0929-codex-vtoroe-mnenie-plan.md).
skills: speckit-checklist → этот файл; speckit-specify → ../spec.md.
skip-step: speckit-checklist — check-prerequisites.sh и разрешение проектного шаблона через .specify вне заданного объёма.
skip-step: speckit-checklist — чтение проектной constitution и метаданных .specify, запись feature.json, extension hooks и любые файлы вне каталога результата.
skip-step: speckit-checklist — операции Git (ветка, коммит, push, PR, метки) и bd.
Контекст явно задан владельцем: спецификация критики сводки; дополнительных уточнений не требуется. Использован разрешённый навыком запасной формат (H1, назначение, дата, разделы, CHK-номера и примечания). Штатный prerequisite/resolver не объявляется исполненным.

Назначение: вопросы о полноте, ясности, согласованности и проверяемости требований, а не сценарии тестирования интеграции. Владелец оценки — будущий рецензент. Отметки в первой части относятся только к форме документа при speckit-specify; CHK ниже оставлены без отметок до независимой оценки. Ни одна отметка не означает исправление процесса клиента или приёмку Claude.

## Авторская проверка формы при speckit-specify — 16 пунктов

### Качество содержания

- [x] Спецификация не предлагает технологии и детали реализации новой интеграции.
- [x] Цель связана с решением владельца о встрече и воспроизводимостью критики.
- [x] Сценарии описаны со стороны владельца, рецензента и следующего участника.
- [x] Обязательные разделы сценариев, требований и критериев успеха заполнены.

### Полнота требований

- [x] Нет незавершённых маркеров NEEDS CLARIFICATION; неизвестность клиента обозначена отдельно.
- [x] FR-001–FR-015 имеют предмет и наблюдаемый приёмочный признак.
- [x] SC-001–SC-008 измеримы по числам, ID и границам результата.
- [x] Критерии не зависят от будущего выбора технологии интеграции.
- [x] У трёх пользовательских историй есть самостоятельная приёмка.
- [x] Пограничные случаи цитаты/отношения, истории/актуальности и разных областей счёта описаны.
- [x] Объём и исключения ограничены неизменным ТЗ.
- [x] Зависимости и отсутствие доступа к оригиналам отражены без выдуманных ответов.

### Готовность спецификации критики

- [x] Для каждого FR есть явный приёмочный признак.
- [x] Основные сценарии покрывают решение о встрече, воспроизведение и продолжение.
- [x] Критерии успеха оценивают документ критики, сохраняя неготовность клиентского пакета.
- [x] Спецификация не создаёт план реализации или новую каноническую задачу.

Эта оценка относится к тексту требований. Доказательства количества, структуры и сохранения ограничений — командный вывод ниже; содержательная оценка выполнена автором документа, не названа независимой.

## Полнота и происхождение требований

- [ ] CHK001 Описаны ли пользовательская цель и смысл второго мнения без добавления новой клиентской функции? [Полнота; Spec §Цель и основание]
- [ ] CHK002 Определён ли неизменный канонический паспорт, чтобы производная спецификация не конкурировала с ТЗ? [Полнота; Spec §Объём; FR-001]
- [ ] CHK003 Требуется ли сохранить каждый из 34 ID, включая ошибки самого аудитора? [Полнота; FR-002/015; SC-001]
- [ ] CHK004 Требуется ли раскрыть все 11 НЕ ПРОВЕРЕНО с причинами и без выдуманных ответов? [Полнота; FR-007; SC-004]
- [ ] CHK005 Описано ли полное покрытие B/C/D с конкретными числами, без подмены матрицы выборкой? [Полнота; FR-008/009; SC-005]
- [ ] CHK006 Сохранены ли все пять измерений E и ограничения условного выбора метода? [Полнота; FR-011; SC-007]

## Ясность и согласованность

- [ ] CHK007 Различимы ли существование цитаты и доказательство отношения между цитатами? [Ясность; FR-004; Spec §Пограничные случаи]
- [ ] CHK008 Объяснено ли, почему ЛОЖЬ-ВЫВОД остаётся видимым, но не служит доказанным препятствием? [Ясность; FR-005/006; SC-002]
- [ ] CHK009 Различаются ли исходные классы и S1/S2/S3, а также четыре исходных S1 и два после критики, без скрытой смены основания? [Согласованность; FR-003/015; SC-003]
- [ ] CHK010 Ограничено ли положительное подтверждение файловым покрытием или историческим пересказом? [Ясность; FR-010; SC-006]
- [ ] CHK011 Исключён ли вывод об автоматизации только из указания системы, управляющей статусом? [Ясность; Spec §Пограничные случаи; FR-005]
- [ ] CHK012 Различены ли области счёта рамок «вся доска» и «только сделка»? [Ясность; Spec §Пограничные случаи; FR-005]

## Проверяемость и приёмка

- [ ] CHK013 Есть ли у каждого FR наблюдаемый признак оценки требований? [Проверяемость; Spec §Функциональные требования]
- [ ] CHK014 Измеримы ли все SC без утверждения об исправлении клиента? [Проверяемость; Spec §Критерии успеха]
- [ ] CHK015 Требуют ли свидетельства команду, фактический вывод, источник и SHA, а E — дату и ограничение версии? [Проверяемость; FR-012; Spec §Сущности результата]
- [ ] CHK016 Разделены ли авторская проверка и будущая независимая приёмка Claude по §9? [Приёмка; FR-014; SC-008]
- [ ] CHK017 Обозначены ли запретные шаги навыков без ложного заявления об исполнении resolver/hooks? [Приёмка; FR-013; шапка Spec]
- [ ] CHK018 Выводится ли итог из доказанных S1, сохраняя формулу трёх состояний и исходные записи? [Проверяемость; FR-006/015; История 1]

## Границы, зависимости и восстановление

- [ ] CHK019 Прямо ли исключены CRM-изменения, правки источников, Git-публикация, bd и приватные материалы? [Границы; Spec §Объём]
- [ ] CHK020 Отделены ли неизвестные процессы клиента от отсутствующих уточнений текущей задачи? [Зависимости; Spec §Объём]
- [ ] CHK021 Не превращается ли закрытый оригинал Miro или схемы в обвинение в фальсификации? [Границы; FR-007; История 2]
- [ ] CHK022 Сохранён ли фактический предел параллельности без заявления о недоступном запуске? [Границы; Spec §Пограничные случаи]
- [ ] CHK023 Определён ли путь продолжения с тем же паспортом и SHA без новой реализации? [Восстановление; Spec §Восстановление]
- [ ] CHK024 Не трактуется ли готовность спецификации критики как готовность документов клиента к встрече? [Границы; Spec §Критерии успеха]

## Примечания и командное свидетельство

24 вопроса CHK относятся к требованиям; все снабжены ссылкой на раздел или FR/SC. Они не отмечены как пройденные. Архитектура реализации неприменима в текущем объёме. Независимая приёмка ещё не наблюдалась.

Навык `/root/.codex/skills/speckit-checklist/SKILL.md` прочитан целиком. Выполнены применимые шаги: зафиксированы предмет, глубина и будущий рецензент; прочитана производная спецификация; вопросы распределены по полноте, ясности, согласованности, проверяемости и границам; уточнены ссылки на FR-003 и SC-002. 24 CHK сохранены пустыми. Отдельные 16 отметок формы — оценка автора спецификации, не результат независимого рецензента. Запрещённые prerequisite, метаданные, hooks, Git и bd не запускались; причина каждого пропуска указана выше.

Первый вызов `repowise search 'спецификация критики' /root/workspaces/projects/clients/eurosteklo/.worktrees/claude/cuw --no-workspace --limit 5` не дал доступного вывода результатов. Успех индексного поиска не заявляется; полнота индекса, включая незакоммиченные отчёты, не установлена. Использован адресный поиск строк и чтение диапазонов только `spec.md` и этого чеклиста. Повторного исследования A–D нет.

Ниже проверяются только структура и явные признаки качества формулировок. Команды не устанавливают истинность исходных выводов, не подтверждают процессы клиента и не заменяют независимую оценку CHK.

### Адресная проверка структуры

Команда (из корня указанного worktree):

```bash
grep -n -E '^#|^skip-step:' docs/review/2026-10-01-codex-vtoroe-mnenie/spec/checklists/requirements.md
```

Фактический вывод; код завершения 0:

```text
1:# Чеклист качества спецификации критики
5:skip-step: speckit-checklist — check-prerequisites.sh и разрешение проектного шаблона через .specify вне заданного объёма.
6:skip-step: speckit-checklist — чтение проектной constitution и метаданных .specify, запись feature.json, extension hooks и любые файлы вне каталога результата.
7:skip-step: speckit-checklist — операции Git (ветка, коммит, push, PR, метки) и bd.
12:## Авторская проверка формы при speckit-specify — 16 пунктов
14:### Качество содержания
21:### Полнота требований
32:### Готовность спецификации критики
41:## Полнота и происхождение требований
50:## Ясность и согласованность
59:## Проверяемость и приёмка
68:## Границы, зависимости и восстановление
77:## Примечания и командное свидетельство
```

### Проверка вопросов, ссылок и владельца оценки

Команда читает только этот чеклист и уже существующую спецификацию; проверка ссылок не открывает паспорт. SHA256 обозначает снимок прочитанного `spec.md` в момент запуска.

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
import re

checklist = Path('docs/review/2026-10-01-codex-vtoroe-mnenie/spec/checklists/requirements.md')
spec = checklist.parent.parent / 'spec.md'
text = checklist.read_text(encoding='utf-8')
body = text.split('## Примечания и командное свидетельство', 1)[0]
spec_bytes = spec.read_bytes()
spec_text = spec_bytes.decode('utf-8')
items = re.findall(r'^- \[([ xX])\] (CHK\d{3}) (.+)$', body, re.M)
ids = [item[1] for item in items]
expected = [f'CHK{i:03d}' for i in range(1, 25)]
assert ids == expected, ids
assert all(mark == ' ' for mark, _, _ in items)
author = re.findall(r'^- \[x\] (?!CHK)(.+)$', body, re.M)
assert len(author) == 16, len(author)
assert 'Авторская проверка формы при speckit-specify — 16 пунктов' in body
assert 'содержательная оценка выполнена автором документа, не названа независимой' in body
assert all(re.search(r'\?\s*\[[^\]\n]+\]$', question) for _, _, question in items)
traceable = sum(bool(re.search(r'Spec §|FR-\d{3}|SC-\d{3}', question)) for _, _, question in items)
assert traceable == 24, traceable
fr = set(re.findall(r'^\| (FR-\d{3}) \|', spec_text, re.M))
sc = set(re.findall(r'^\| (SC-\d{3}) \|', spec_text, re.M))
assert fr == {f'FR-{i:03d}' for i in range(1, 16)}
assert sc == {f'SC-{i:03d}' for i in range(1, 9)}
refs = {'FR': set(), 'SC': set()}
for _, _, question in items:
    for kind, first, second in re.findall(r'(FR|SC)-(\d{3})(?:/(\d{3}))?', question):
        refs[kind].add(f'{kind}-{first}')
        if second:
            refs[kind].add(f'{kind}-{second}')
assert refs['FR'] == fr, (refs['FR'], fr)
assert refs['SC'] == sc, (refs['SC'], sc)
headings = re.findall(r'^#{1,6} (.+)$', spec_text, re.M)
section_refs = re.findall(r'Spec §([^;\]\n]+)', body)
assert all(any(heading.startswith(section.strip()) for heading in headings) for section in section_refs)
links = re.findall(r'\[[^\]]+\]\(([^)]+)\)', body)
assert len(links) == 2, links
assert all((checklist.parent / target).is_file() for target in links)
for token in ('check-prerequisites.sh', 'constitution', 'feature.json', 'extension hooks', 'Git', 'bd'):
    assert any(token in line for line in body.splitlines() if line.startswith('skip-step:')), token
categories = re.findall(r'^## (.+)$', body, re.M)
assert len(categories) == 5, categories
print('CHK: 24; IDs: CHK001–CHK024, unique and consecutive')
print('CHK unchecked: 24; checked: 0')
print('Author form assessment: 16 checked; explicitly not independent')
print('Requirement-quality questions: 24/24 have question form and dimension labels')
print(f'Traceable CHK: {traceable}/24 (100%)')
print(f'Referenced FR: {len(refs["FR"])}/15; SC: {len(refs["SC"])}/8; missing references: 0')
print(f'Spec section references: {len(section_refs)}; unresolved: 0')
print('Document links: 2; existing: 2')
print('Explicit skip-step groups: 3; required forbidden operations named: 6/6')
print('Sections: 1 author assessment + 4 custom checklist categories')
print('Spec snapshot SHA256: ' + hashlib.sha256(spec_bytes).hexdigest())
print('STRUCTURE: PASS; semantic acceptance and independent CHK review: NOT CLAIMED')
PY
```

Первый запуск той же команды завершился кодом 1: в строке `skip-step` операции были перечислены, но слово `Git` не было написано явно. Исправлена только эта поясняющая строка.

```text
Traceback (most recent call last):
  File "<stdin>", line 42, in <module>
AssertionError: Git
```

Повторный запуск после этой ограниченной правки; фактический вывод, код завершения 0:

```text
CHK: 24; IDs: CHK001–CHK024, unique and consecutive
CHK unchecked: 24; checked: 0
Author form assessment: 16 checked; explicitly not independent
Requirement-quality questions: 24/24 have question form and dimension labels
Traceable CHK: 24/24 (100%)
Referenced FR: 15/15; SC: 8/8; missing references: 0
Spec section references: 13; unresolved: 0
Document links: 2; existing: 2
Explicit skip-step groups: 3; required forbidden operations named: 6/6
Sections: 1 author assessment + 4 custom checklist categories
Spec snapshot SHA256: d48ca6f6f97a8fefecd2b41f9d4394827d8bae947017af7deabc12e85d62bab1
STRUCTURE: PASS; semantic acceptance and independent CHK review: NOT CLAIMED
```

PASS выше относится только к перечисленным структурным признакам. Содержательные 16 отметок остаются авторской оценкой; 24 CHK ждут независимого рецензента.
