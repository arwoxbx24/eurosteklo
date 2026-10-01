#!/usr/bin/env python3
"""Блок B spec 009: вставка вопросов по конфликтам в tochki.html из mapping.tsv."""

import os
import re
import sys

TSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mapping.tsv")
SDELKI = "docs/ppo/sdelki/_parts/tochki.html"
LIDY = "docs/ppo/lidy/_parts/tochki.html"
COLS = ["id", "reg_file", "reg_line", "status", "map", "point",
        "basis", "also", "question"]

def read_tsv(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not (line := line.rstrip("\n")) or line.startswith("id\t"):
                continue
            cells = (line.split("\t") + [""] * len(COLS))[:len(COLS)]
            rows.append(dict(zip(COLS, cells)))
    return rows

def find_region(text, first, tags, close):
    """Вернуть (позиция последнего из tags, позиция close) или None."""
    pos = text.find(first)
    if pos < 0:
        return None
    for t in tags:
        pos = text.find(t, pos)
        if pos < 0:
            return None
    c = text.find(close, pos)
    if c < 0:
        return None
    return pos, c

def max_e(text, ul_start, ul_end):
    nums = [int(n) for n in re.findall(r'data-id="e(\d+)"', text[ul_start:ul_end])]
    return max(nums) if nums else 0

def li_indent(text, start, end):
    m = re.search(r'\n([ \t]*)(?=<li)', text[start:end])
    return m.group(1) if m else ""

def insert_card(text, point, items):
    ul, end = find_region(text, 'id="t%s"' % point,
                          ["<dt>Уточнить по состояниям</dt>", "<dd>", "<ul>"], "</ul>")
    base = max_e(text, ul, end)
    ind = li_indent(text, ul, end)
    block = "".join('%s<li data-id="e%d" data-src="доска">🟣 %s '
                    '<small class="src">%s:%s</small></li>\n'
                    % (ind, base + 1 + i, q, f, ln)
                    for i, (pid, f, ln, q) in enumerate(items))
    return text[:end] + block + text[end:]

def insert_sec(text, sec_id, items):
    ol, end = find_region(text, '<section id="%s"' % sec_id, ["<ol>"], "</ol>")
    ind = li_indent(text, ol, end)
    block = "".join('%s<li>🟣 %s <small class="src">%s:%s</small></li>\n'
                    % (ind, q, f, ln) for _, f, ln, q in items)
    return text[:end] + block + text[end:]

def plan(rows, texts):
    skipped = 0
    no_place = []
    card = {}
    sec = {}
    for r in rows:
        if r["status"] not in ("точка", "повестка"):
            continue
        text = texts[r["map"]]
        src = '<small class="src">%s:%s</small>' % (r["reg_file"], r["reg_line"])
        if src in text:
            skipped += 1
            continue
        item = (r["id"], r["reg_file"], r["reg_line"], r["question"])
        if r["status"] == "точка":
            place = find_region(text, 'id="t%s"' % r["point"],
                                ["<dt>Уточнить по состояниям</dt>", "<dd>", "<ul>"], "</ul>")
            if place is None:
                no_place.append("%s %s %s" % (r["id"], r["map"], r["point"]))
            else:
                card.setdefault((r["map"], r["point"]), []).append(item)
        else:
            sec_id = "top5" if r["map"] == "sdelki" else "povestka"
            if find_region(text, '<section id="%s"' % sec_id, ["<ol>"], "</ol>") is None:
                no_place.append("%s %s -" % (r["id"], r["map"]))
            else:
                sec.setdefault((r["map"], sec_id), []).append(item)
    return skipped, no_place, card, sec

def selftest():
    card = ('<article class="card" id="t9"><dl>\n'
            '<dt>Уточнить по состояниям</dt>\n<dd><ul>\n'
            '<li data-id="e1" data-src="доска">б <small class="src">доска</small></li>\n'
            '<li data-id="e2" data-src="ТЗ">б <small class="src">ТЗ</small></li>\n'
            '<li data-id="e5" data-see="х">б</li>\n</ul></dd></dl></article>\n')
    a = insert_card(card, 9, [("П-01", "k1-prepost.md", "57", "Вопрос первый?")])
    assert 'data-id="e6"' in a
    assert 'data-src="доска">🟣 Вопрос первый? <small class="src">k1-prepost.md:57' in a
    b = insert_card(a, 9, [("П-02", "k1-prepost.md", "58", "Вопрос второй?")])
    assert 'data-id="e7"' in b
    rows = [dict(id="П-01", status="точка", map="sdelki", point="9",
                 reg_file="k1-prepost.md", reg_line="57", question="Вопрос первый?"),
            dict(id="П-02", status="точка", map="sdelki", point="9",
                 reg_file="k1-prepost.md", reg_line="58", question="Вопрос второй?")]
    skip, no, ce, se = plan(rows, {"sdelki": b, "lidy": b})
    assert skip == 2 and not no and not ce and not se
    rows.append(dict(id="П-99", status="уже", map="-", point="-",
                     reg_file="k1-prepost.md", reg_line="61", question="Уже на карте?"))
    rows.append(dict(id="К-99", status="пусто", map="-", point="-",
                     reg_file="k3-conflicts.md", reg_line="82", question="Пусто"))
    skip2, no2, ce2, se2 = plan(rows, {"sdelki": b, "lidy": b})
    assert skip2 == skip and not no2 and not ce2 and not se2
    src = ('<section id="top5"><h2>Темы</h2><ol>\n'
           '<li>а <small class="src">доска</small></li>\n</ol></section>\n')
    st = insert_sec(src, "top5", [("Р-01", "k2-forks.md", "30", "Вопрос?")])
    assert '<li>🟣 Вопрос? <small class="src">k2-forks.md:30</small></li>' in st
    assert st.rindex("🟣 Вопрос?") < st.index("</ol>")
    assert find_region(src, '<section id="povestka">', ["<ol>"], "</ol>") is None
    print("selftest: ok")

def main(argv):
    if "--selftest" in argv:
        selftest()
        return 0
    path = TSV
    if "--tsv" in argv:
        path = argv[argv.index("--tsv") + 1]
    paths = {"sdelki": SDELKI, "lidy": LIDY}
    texts = {m: open(p, encoding="utf-8").read() for m, p in paths.items()}
    skipped, no_place, card, sec = plan(rows := read_tsv(path), texts)
    if no_place:
        for n in no_place:
            print("НЕТ МЕСТА:", n)
        return 1
    for (m, point), items in card.items():
        texts[m] = insert_card(texts[m], point, items)
    for (m, sec_id), items in sec.items():
        texts[m] = insert_sec(texts[m], sec_id, items)
    for m, p in paths.items():
        with open(p, "w", encoding="utf-8") as f:
            f.write(texts[m])
    print("вставлено в карточки %d · в повестку %d · пропущено %d"
          % (sum(len(v) for v in card.values()),
             sum(len(v) for v in sec.values()), skipped))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
