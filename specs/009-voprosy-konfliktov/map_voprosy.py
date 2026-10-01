#!/usr/bin/env python3
import argparse
import os
import re

REG = [("k1-prepost.md", "docs/ppo/konflikty/k1-prepost.md"),
       ("k2-forks.md", "docs/ppo/konflikty/k2-forks.md"),
       ("k3-conflicts.md", "docs/ppo/konflikty/k3-conflicts.md")]
BUILT = ["docs/ppo/index.html", "docs/ppo/sdelki/karta-sdelki.html",
         "docs/ppo/sdelki/obsledovanie-sdelki.html",
         "docs/ppo/sdelki/obsledovanie-sdelki-podrobno.html",
         "docs/ppo/lidy/karta-lidy.html",
         "docs/ppo/lidy/obsledovanie-lidy.html",
         "docs/ppo/lidy/obsledovanie-lidy-podrobno.html"]
TOCHKI = {"sdelki": "docs/ppo/sdelki/_parts/tochki.html",
          "lidy": "docs/ppo/lidy/_parts/tochki.html"}
OUT = "specs/009-voprosy-konfliktov/mapping.tsv"
ID_PRE = r"(?<![A-Za-zА-Яа-яЁё-])"

def clean(raw):
    q = raw.strip()
    if q.startswith("«") and q.endswith("»") and len(q) > 2:
        q = q[1:-1]
    return q.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def parse_registry(name, lines):
    items, qidx = [], None
    for ln, line in enumerate(lines, 1):
        if line.startswith("| ID |"):
            cells = [c.strip() for c in line.split("|")]
            qidx = cells.index("Вопрос клиенту")
            continue
        if not re.match(r"^\| (?:П|Р|К)-\d+ \|", line):
            continue
        cells = [c.strip() for c in line.split("|")]
        items.append({"id": cells[1], "file": name, "line": ln,
                      "stage": cells[2] if name == "k1-prepost.md" else "",
                      "raw": cells[qidx],
                      "rest": "|".join(c for j, c in enumerate(cells)
                                       if j != qidx)})
    return items

def point_keys(s):
    keys = set()
    for m in re.finditer(r"\d{9,}", s):
        keys.add(m.group()[-9:])
    for m in re.finditer(r"(?:к\.…|…|к\.|К)(\d{4})(?!\d)", s):
        keys.add(m.group(1))
    return keys

def card_keys(s):
    keys = set()
    for m in re.finditer(r"\d{9,}", s):
        d = m.group()
        keys.add(d[-9:])
        if d.startswith("3458764"):
            keys.add(d[-4:])
    for m in re.finditer(r"к\.(\d{4})(?!\d)", s):
        keys.add(m.group(1))
    return keys

def load_cards(mapname):
    text = open(TOCHKI[mapname], encoding="utf-8").read()
    cards = []
    pat = r'<article class="card" id="t(\d+)"[^>]*>(.*?)</article>'
    for m in re.finditer(pat, text, re.S):
        full = m.group(0)
        cards.append({"num": int(m.group(1)), "keys": card_keys(full),
                      "has_dt": "<dt>Уточнить по состояниям</dt>" in full,
                      "line": text.count("\n", 0, m.start()) + 1})
    return cards

def already(rec, built):
    id_re = re.compile(ID_PRE + re.escape(rec["id"]) + r"(?!\d)")
    fl_re = re.compile(re.escape(rec["file"] + ":" + str(rec["line"])) +
                       r"(?!\d)")
    for fname, text in built:
        m = id_re.search(text) or fl_re.search(text)
        if m:
            return f"{fname}:{text.count(chr(10), 0, m.start()) + 1}"
    return None

def map_order(stage):
    return ["lidy", "sdelki"] if stage.startswith("ЛИД") else ["sdelki", "lidy"]

def bind(built):
    items = []
    for name, path in REG:
        items.extend(parse_registry(name, open(path, encoding="utf-8")
                                    .read().splitlines()))
    cards = {m: load_cards(m) for m in ("sdelki", "lidy")}
    rows, cnt = [], {"уже": 0, "точка": 0, "повестка": 0, "пусто": 0}
    for rec in sorted(items, key=lambda r: (r["file"], r["line"])):
        stat, mapv, point, basis, also = "-", "-", "-", None, "-"
        got = already(rec, built)
        if got:
            stat, basis = "уже", got
        elif rec["raw"].strip() == "" or (
                rec["raw"].strip().startswith("(") and
                rec["raw"].strip().endswith(")")):
            stat, basis = "пусто", "пусто"
        else:
            pk = point_keys(rec["rest"])
            order = map_order(rec["stage"])
            chosen = None
            for m in order:
                c = [x for x in cards[m] if x["has_dt"] and (x["keys"] & pk)]
                if c:
                    chosen = (m, max(c, key=lambda x: (len(x["keys"] & pk),
                                                       -x["num"])))
                    break
            if not chosen:
                mapv = map_order(rec["stage"])[0]
                stat, basis = "повестка", "общих узлов нет"
            else:
                m2, card = chosen
                stat, mapv, point = "точка", m2, str(card["num"])
                basis = "ключ={}; {}/tochki.html:{}".format(
                    sorted(pk & card["keys"])[0], m2, card["line"])
                also = ",".join("{}:{}".format(mm, x["num"]) for mm in order
                                for x in cards[mm]
                                if x is not card and x["has_dt"]
                                and (x["keys"] & pk)) or "-"
        rows.append((rec, stat, mapv, point, basis, also))
        cnt[stat] += 1
    return rows, cnt

def write_tsv(rows, out):
    head = ["id", "reg_file", "reg_line", "status", "map", "point",
            "basis", "also", "question"]
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\t".join(head) + "\n")
        for rec, s, mapv, point, basis, also in rows:
            fh.write("\t".join([rec["id"], rec["file"], str(rec["line"]), s,
                                mapv, point, basis, also,
                                clean(rec["raw"])]) + "\n")

def selftest():
    assert clean("«Пожалуйста, уточните: что означает «ПР»?»") == \
        "Пожалуйста, уточните: что означает «ПР»?"
    k3 = parse_registry("k3-conflicts.md", [
        "| ID | Тип | Слой A | Слой B | Метка | Как поступил бы старший БА (проверка) | Вопрос клиенту |",
        "|---|---|---|---|---|---|---|",
        "| К-01 | СУЩНОСТЬ | A | B | м | старший БА текст | «Вопрос клиенту текст» |",
    ])
    assert k3[0]["raw"] == "«Вопрос клиенту текст»"
    p = "(внутренняя правка, вопрос не нужен)"
    assert p.strip() == "" or (p.strip().startswith("(") and p.strip().endswith(")"))
    assert not ("«вопрос»".strip() == "" or
                ("«вопрос»".startswith("(") and "«вопрос»".endswith(")")))
    assert point_keys("…430916255") & card_keys("3074457358430916255")
    assert point_keys("…7365") & card_keys("3458764685196477365")
    assert "2024" not in point_keys("предоплата 2024 года")
    good = [{"num": 5, "has_dt": True, "keys": {"430916255"}},
            {"num": 7, "has_dt": True, "keys": {"430916255", "7365"}}]
    c = [x for x in good if x["has_dt"] and (x["keys"] & {"430916255", "7365"})]
    assert max(c, key=lambda x: (len(x["keys"] & {"430916255", "7365"}), -x["num"]))["num"] == 7
    id_re = re.compile(ID_PRE + re.escape("П-01") + r"(?!\d)")
    assert id_re.search("текст П-01 конец")
    assert not id_re.search("П-012") and not id_re.search("ПП-01")
    built = [(os.path.basename(p), open(p, encoding="utf-8").read())
             for p in BUILT]
    for _rec, s, mapv, _pt, _b, _a in bind(built)[0]:
        if s == "точка":
            assert mapv in ("sdelki", "lidy"), (_rec["id"], mapv)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return 0
    built = [(os.path.basename(p), open(p, encoding="utf-8").read())
             for p in BUILT]
    rows, cnt = bind(built)
    write_tsv(rows, args.out)
    print("всего {} · уже {} · точка {} · повестка {} · пусто {}".format(
        sum(cnt.values()), cnt["уже"], cnt["точка"], cnt["повестка"],
        cnt["пусто"]))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
