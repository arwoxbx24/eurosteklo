#!/usr/bin/env python3
"""Повторяемая проверка сверки встреч «Евро стекло» (spec 014).

Запуск из корня репозитория: python3 scripts/check_sverka.py
Каждый блок печатает PASS/FAIL и числа; код выхода 1, если есть FAIL.
"""
import csv
import html
import json
import re
import sys
import zipfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / 'docs/meetings/2026-10-04-dialog'
FAIL = []


def rd(p):
    return [r for r in csv.reader(open(p, encoding='utf-8'), delimiter='\t')]


def report(block, ok, msg):
    print(f"[{'PASS' if ok else 'FAIL'}] {block}: {msg}")
    if not ok:
        FAIL.append(block)


def norm(s):
    return re.sub(r'[^\w]+', ' ', s.lower().replace('ё', 'е')).strip()


def secs(t):
    h, m, s = map(int, t.split(':'))
    return h * 3600 + m * 60 + s


# расшифровки
T = {}
for rec in ('GR8', 'Hkb'):
    T[rec] = {}
    for line in open(D / f'{rec}.txt', encoding='utf-8'):
        m = re.match(r'\[(\d\d:\d\d:\d\d)\] (\w): (.*)', line.rstrip('\n'))
        T[rec][m[1]] = (m[2], m[3])


def quote_ok(rec, tc, q, window=90):
    """Цитата (возможно с … и усечением) дословно есть в окне ±window с."""
    if rec not in T or tc not in T[rec]:
        return False
    win = norm(' '.join(x[1] for k, x in T[rec].items() if abs(secs(k) - secs(tc)) <= window))
    parts = [p for p in re.split(r'\s*(?:\.\.\.|…)\s*', q) if len(norm(p)) >= 8]
    if not parts:  # короткое подтверждение («Да, да.») — ищем в самой реплике
        return bool(norm(q)) and norm(q) in norm(T[rec][tc][1])
    return all(norm(p) in win for p in parts)


def file_quote_ok(f, ln, q):
    """Цитата дословно в строке ln (±2) документа-источника."""
    cands = [ROOT / f, ROOT / 'client-materials' / f, ROOT / 'docs/process/bpmn' / f]
    p = next((c for c in cands if c.is_file()), None)
    if p is None:
        return False
    lines = open(p, encoding='utf-8').read().splitlines()
    win = norm(html.unescape(re.sub(r'<[^>]+>', ' ', ' '.join(lines[max(0, ln - 3):ln + 2]))))
    parts = [x for x in re.split(r'\s*(?:\.\.\.|…)\s*', q) if len(norm(x)) >= 4]
    return bool(parts) and all(norm(x) in win for x in parts)


# Б1. Банк вопросов = 285, id совпадают со страницами обследования
bank = set()
for P, f in (('L', 'docs/ppo/lidy/obsledovanie-lidy-podrobno.html'),
             ('S', 'docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html')):
    h = open(ROOT / f, encoding='utf-8').read()
    c = re.split(r'<article class="card" id="t(\d+)"', h)
    for i in range(1, len(c), 2):
        body = c[i + 1].split('</article>')[0]
        bank.add(f'{P}-t{c[i]}-q')
        for m in re.finditer(r'<li[^>]*data-id="(e\d+)"', body):
            bank.add(f'{P}-t{c[i]}-{m[1]}')
sv = rd(D / 'svod.tsv')
ids = [r[0] for r in sv[1:]]
report('Б1 банк', len(ids) == 285 and set(ids) == bank and len(set(ids)) == 285 and all(len(r) == 9 for r in sv),
       f'строк {len(ids)}, банк {len(bank)}, лишних {len(set(ids) - bank)}, недостающих {len(bank - set(ids))}')
st = Counter(r[1] for r in sv[1:])
print('      статусы:', dict(st))

# Б2. Каждый ответ: таймкод существует, цитата дословна, метка спикера совпадает
ans = [r for r in sv[1:] if r[1] in ('ОТВЕЧЕН', 'ЧАСТИЧНО') or (r[1] == 'ВНЕ-1С' and r[5].startswith('обсуждалось'))]
bad = []
for r in ans:
    q = re.sub(r'^обсуждалось( частично)?: ', '', r[5]).rstrip('…')
    if not quote_ok(r[2], r[3], q) or T[r[2]][r[3]][0] != r[4]:
        bad.append(r[0])
report('Б2 ответы', not bad, f'проверено {len(ans)}, ошибок {len(bad)} {bad[:5]}')

# Б3. Противоречия: источник существует
lens = {'data.md': len(open(ROOT / 'docs/process/bpmn/data.md', encoding='utf-8').read().splitlines()),
        'L': len(open(ROOT / 'docs/ppo/lidy/_parts/TOCHKI.md', encoding='utf-8').read().splitlines()),
        'S': len(open(ROOT / 'docs/ppo/sdelki/_parts/TOCHKI.md', encoding='utf-8').read().splitlines())}
nl = {k: len(v) for k, v in T.items()}
cbad = []
contr = [r for r in sv[1:] if r[6] == 'да']
for r in contr:
    for part in re.split(r'[;,]\s*(?=[A-Za-zА-Яа-я])', r[7]):
        part = part.strip()
        m = re.match(r'(data\.md|TOCHKI\.md|sct):(\d+)', part)
        m2 = re.match(r'(GR8|Hkb)[ :](\d\d:\d\d:\d\d)', part)
        m3 = re.match(r'(GR8|Hkb):(\d+)', part)
        ok = (m and (m[1] == 'sct' or int(m[2]) <= (lens['data.md'] if m[1] == 'data.md' else lens[r[0][0]]))) \
            or (m2 and m2[2] in T[m2[1]]) or (m3 and int(m3[2]) <= nl[m3[1]])
        if not ok:
            cbad.append((r[0], part))
report('Б3 противоречия', not cbad, f'строк {len(contr)}, битых источников {len(cbad)} {cbad[:3]}')

# Б4. Пробелы покрыты вопросником; в вопроснике нет 1С, DNS, кодов
vq = rd(D / 'voprosnik.tsv')
cov = {p for r in vq[1:] for p in r[1].split()}
gaps = [r[0] for r in sv[1:] if r[1] in ('НЕ-ЗАДАН', 'БЕЗ-ОТВЕТА', 'ПЛОХОЙ-ТЕКСТ')]
unc = [g for g in gaps if '-'.join(g.split('-')[:2]) not in cov]
codes = [r[2] for r in vq[1:] if re.search(r'1С|1C|DNS|[LS]-t\d|\bТЗ\b|доск', r[2])]
report('Б4 вопросник', not unc and not codes, f'пробелов {len(gaps)}, вопросов {len(vq) - 1}, не покрыто {unc}, кодов {len(codes)}')

# Б5. Word и HTML содержат все вопросы вопросника и одинаковое напоминание
x = html.unescape(re.sub(r'<[^>]+>', '', zipfile.ZipFile(D / 'Евростекло-вопросы-клиенту.docx').read('word/document.xml').decode()))
hv = html.unescape(open(D / 'voprosnik-klientu.html', encoding='utf-8').read())
miss_w = [r[2][:40] for r in vq[1:] if r[2] not in x]
miss_h = [r[2][:40] for r in vq[1:] if r[2] not in hv]
rem = 'Рекламации и отказ клиента после оплаты вы решили описать отдельно'
report('Б5 Word/HTML', not miss_w and not miss_h and rem in x and rem in hv and 'сохранил' not in x,
       f'нет в Word {len(miss_w)}, нет в HTML {len(miss_h)}')

# Б6. Корректирующий блок: каждая строка совпадает со svod, цитаты дословны
kor = rd(D / 'korrektirovka.tsv')
svd = {r[0]: r for r in sv[1:]}
kbad = [k[0] for k in kor[1:] if svd[k[0]][1] != k[2] or (k[2] in ('ОТВЕЧЕН', 'ЧАСТИЧНО') and not quote_ok(k[3], k[4], k[5]))]
report('Б6 корректировка', not kbad, f'строк {len(kor) - 1}, ошибок {kbad}')

# Б7. Блок-схема: метка, цитата дословна, строка схемы существует
K = rd(D / 'bloksxema.tsv')
kb = []
for r in K[1:]:
    if r[2] not in ('PROVEN', 'INFERRED', 'UNVERIFIED') or not quote_ok(r[3], r[4], r[6]):
        kb.append(r[0])
    m = re.match(r'(data\.md|TOCHKI\.md\((?:сделки|лиды)\)):(\d+)', r[8])
    if m:
        lim = lens['data.md'] if m[1] == 'data.md' else (lens['S'] if 'сделки' in m[1] else lens['L'])
        if int(m[2]) > lim:
            kb.append(r[0] + ':ref')
report('Б7 блок-схема', not kb, f'фактов {len(K) - 1}, метки {dict(Counter(r[2] for r in K[1:]))}, ошибок {kb}')

# Б8. Доказательства к форме ответов: id существуют, статусы совпадают со svod
F = rd(D / 'forma-otvetov-sdelki-dokazatelstva.tsv')
fb = [r[0] for r in F[1:] if r[0] not in svd or svd[r[0]][1] != r[3]]
t = open(D / 'forma-otvetov-sdelki-sanitized.md', encoding='utf-8').read()
json.loads(re.search(r'evro-answers (\{.*\}) -->', t)[1])
report('Б8 форма', not fb, f'отметок {len(F) - 1}, расхождений со svod {fb}')

# Б9. Качество расшифровки: подсчёты
g = {p: sum(open(D / f'{r}.txt', encoding='utf-8').read().count(p) for r in ('GR8', 'Hkb')) for p in ('Bittrex', '1S')}
report('Б9 расшифровка', g['Bittrex'] == 27 and g['1S'] == 6 and st['ПЛОХОЙ-ТЕКСТ'] == 4, f'{g}, ПЛОХОЙ-ТЕКСТ {st["ПЛОХОЙ-ТЕКСТ"]}')

# Б10. Персональные данные: имён участников нет в производных файлах
names = re.compile(r'Андре[йяюе]|Роман[аеу]?\b|\bДаня\b|Павел|\+7\d{10}|@\w+\.\w+')
pii = []
for p in list(D.glob('*.tsv')) + list(D.glob('*.md')) + list((D / 'kachestvo').glob('*.md')) + list((D / 'baza').glob('*.tsv')):
    if p.name in ('GR8.txt', 'Hkb.txt'):
        continue
    for i, line in enumerate(open(p, encoding='utf-8'), 1):
        if names.search(line):
            pii.append(f'{p.name}:{i}')
report('Б10 ПДн', not pii, f'совпадений {len(pii)} {pii[:5]}')

# Б11. База декомпозиции: каждая цитата с таймкодом дословна
bb = []
for p in sorted((D / 'baza').glob('D*.tsv')):
    rows = rd(p)
    hdr = rows[0]
    ci = hdr.index('цитата') if 'цитата' in hdr else None
    si = hdr.index('источник') if 'источник' in hdr else None
    ri = hdr.index('запись') if 'запись' in hdr else None
    ti = hdr.index('таймкод') if 'таймкод' in hdr else None
    n = 0
    for r in rows[1:]:
        if ci is None or len(r) != len(hdr) or r[ci] in ('—', ''):
            continue
        if ri is not None:
            refs = [(r[ri], r[ti].strip('[] '))]
            frefs = []
        else:
            refs = re.findall(r'(GR8|Hkb) (\d\d:\d\d:\d\d)', r[si])
            frefs = re.findall(r'([\w./-]+\.(?:md|html|tsv)):(\d+)', r[si])
            if not refs and not frefs:
                continue
        n += 1
        if not any(quote_ok(rec, tc, r[ci]) for rec, tc in refs) and not any(file_quote_ok(f, int(ln), r[ci]) for f, ln in frefs):
            bb.append(f'{p.name}:{r[0][:20]}')
    bad_w = [i for i, r in enumerate(rows[1:], 2) if len(r) != len(hdr)]
    print(f'      {p.name}: строк {len(rows) - 1}, цитат проверено {n}, строк с неверным числом полей {len(bad_w)}')
    bb += [f'{p.name}:строка {i} поля' for i in bad_w]
report('Б11 база', not bb, f'ошибок {len(bb)} {bb[:5]}')

# Б12. Документ подтверждения: каждая строка прослеживается к источнику; все узлы K2 и неразрешённые K1 включены; нет кодов и имён
P = rd(D / 'podtverzhdenie/podtverzhdenie.tsv')
k2 = rd(D / 'baza/K2-uzly.tsv')
k1 = [r for r in rd(D / 'baza/K1-protivorechiya.tsv')[1:] if r[6] == 'не разрешено']
brief = ' '.join(r[2] for r in rd(D / 'podtverzhdenie/1c-brief.tsv')[1:])
src = ' '.join(r[4] for r in P[1:])
miss = [r[0] for r in k2[1:] if f'K2 n{r[0]};' not in src and f'K2 n{r[0]};' not in brief] + [r[0] for r in k1 if f'K1 n{r[0]};' not in src and f'K1 n{r[0]};' not in brief]
codes = [r[1] for r in P[1:] if re.search(r'\b[LS]-t\d|\bK\d\b|\bР-\d|\bС\d{1,2}\b|DNS', r[2] + r[3]) or names.search(r[2] + r[3])]
# 1С: вопросы об интеграции — только в podtverzhdenie/1c-brief.tsv; в документе клиенту 1С допустим лишь как место создания документов в утверждениях разделов 1–2
codes += [r[1] + ':1С' for r in P[1:] if re.search(r'1С|1C', r[3]) or (re.search(r'1С|1C', r[2]) and not r[0].startswith(('1.', '2.')))]
nosrc = [r[1] for r in P[1:] if not re.match(r'(K[123] |svod )', r[4])]
hp = html.unescape(open(D / 'podtverzhdenie/podtverzhdenie-klientu.html', encoding='utf-8').read())
nohtml = [r[1] for r in P[1:] if r[2] not in hp]
report('Б12 подтверждение', not miss and not codes and not nosrc and not nohtml,
       f'пунктов {len(P) - 1}, разделы {dict(Counter(r[0][:2] for r in P[1:]))}, не включено {miss}, коды/имена {codes}, без источника {nosrc}, нет в HTML {nohtml}')

# Б13. Согласованность меток: факт, который клиент не подтвердил (UNVERIFIED в bloksxema/D2, «скорее всего», «наверное», «можно поставить»),
# не может стоять утверждением в строке PROVEN баз D1–D4 и K2 (цитаты, источники и вопросы не проверяются — там упоминание допустимо)
SKIP = {'цитата', 'источник', 'источники', 'как_у_нас', 'вопрос', 'вопрос_клиенту', 'открытый_вопрос', 'утверждение_для_клиента'}
RULES = [
    ('Max без оговорки «если подключат»', lambda t: any('если' not in t[m.start():m.start() + 40] for m in re.finditer(r'\bMax\b|\bМакс\b', t))),
    ('уведомление о доставке', lambda t: bool(re.search(r'уведомлен\w*[^;.]{0,40}доставк', t))),
    ('отказ после оплаты = рекламация', lambda t: 'после оплаты' in t and 'рекламац' in t and not re.search(r'наверное|UNVERIFIED|не подтвержд', t)),
]
un = []
for p in sorted((D / 'baza').glob('D[1-4]*.tsv')) + [D / 'baza/K2-uzly.tsv']:
    rows = rd(p)
    hdr = rows[0]
    mi = hdr.index('метка')
    for i, r in enumerate(rows[1:], 2):
        if not r[mi].startswith('PROVEN'):
            continue
        t = ' '.join(v for h, v in zip(hdr, r) if h not in SKIP)
        un += [f'{p.name}:{i} {name}' for name, f in RULES if f(t)]
report('Б13 метки', not un, f'неподтверждённых фактов в строках PROVEN {len(un)} {un[:5]}')

print('ИТОГ:', 'PASS' if not FAIL else 'FAIL ' + ', '.join(FAIL))
sys.exit(1 if FAIL else 0)
