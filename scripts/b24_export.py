#!/usr/bin/env python3
"""b24_export.py — выгрузка Битрикс24 CRM «Евростекло / АНДА» в агентский формат.

Только чтение Б24. Все данные берутся через готовый CLI /root/workspaces/tools/b24
(subprocess). Вебхук читает сам CLI из /root/workspaces/secrets/services/b24.env —
этот скрипт секрет не читает и не печатает, ничего не передаёт в аргументах.

Используются только методы чтения: *.list, *.get, *.fields, *.items.get.
Запись в Б24 (add/update/delete/set) запрещена и здесь не вызывается.

Результат: client-materials/private/b24-export/ (каталог в .gitignore).
"""

import json
import os
import subprocess
from datetime import datetime, timezone


PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(PROJ, "client-materials", "private", "b24-export")
B24 = "/root/workspaces/tools/b24"

DEAL_IDS = [4844, 6778]
COMPANY_IDS = [2372, 2398, 3218]
OWNER_TYPE = {"deal": 2, "company": 4, "contact": 3}
DEAL_STATUS_ENTITIES = ["DEAL_STAGE_24", "DEAL_STAGE_26"]

DEAL_LIST_SELECT = ["ID", "TITLE", "STAGE_ID", "CATEGORY_ID", "OPPORTUNITY", "DATE_CREATE"]

# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------


def _f(key, value):
    return "%s=%s" % (key, value)


def _filt(key, value):
    return "filter[%s]=%s" % (key, value)


def _sel(*cols):
    return ["select[%d]=%s" % (i, c) for i, c in enumerate(cols)]


def b24(method, keyvals, mode):
    """Запуск CLI. mode='pick' -> `--pick ''`, mode='all' -> `--all`."""
    cmd = [B24, method] + list(keyvals)
    if mode == "pick":
        cmd += ["--pick", ""]
    else:
        cmd += ["--all"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout or "").strip() or "rc=%s" % proc.returncode)
    out = proc.stdout.strip()
    if not out:
        return None
    try:
        return json.loads(out)
    except ValueError:
        raise RuntimeError("не-JSON вывод от CLI: %r" % out[:200])


def safe(errors, method, keyvals, mode, ctx):
    """Обёртка: ошибка метода не роняет выгрузку."""
    try:
        return b24(method, keyvals, mode)
    except Exception as e:  # noqa: BLE001 - любая ошибка одного метода
        errors.append("%s: %s" % (ctx, e))
        return {"error": str(e)}


def as_list(value):
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        res = value.get("result")
        if isinstance(res, list):
            return res
    return []


def write_json(rel_path, data):
    path = os.path.join(OUT, rel_path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    return path


def is_blank(value):
    return value is None or value == "" or value == [] or value == {}


# --------------------------------------------------------------------------
# справочники
# --------------------------------------------------------------------------


def collect_meta(errors, index):
    labels = {}
    fields = {}
    for kind, method in (("deal", "crm.deal.fields"), ("company", "crm.company.fields"), ("contact", "crm.contact.fields")):
        res = safe(errors, method, [], "pick", method)
        fields[kind] = res
        write_json("meta/fields_%s.json" % kind, res)
        if isinstance(res, dict):
            for fname, fdef in res.items():
                if not isinstance(fdef, dict):
                    continue
                label = fdef.get("title") or fdef.get("formLabel") or fdef.get("listLabel") or fname
                labels[fname] = label
            fields[kind] = res
    index["labels"] = labels

    stage_rows = []
    stage_map = {}
    for entity in DEAL_STATUS_ENTITIES:
        res = safe(errors, "crm.status.list", [_filt("ENTITY_ID", entity)], "all", "crm.status.list %s" % entity)
        for row in as_list(res):
            if isinstance(row, dict):
                stage_rows.append(row)
                sid = row.get("STATUS_ID")
                name = row.get("NAME")
                if sid:
                    stage_map[(entity, sid)] = name
    write_json("meta/stages.json", stage_rows)
    index["stage_map"] = {("%s:%s" % k): v for k, v in stage_map.items() if v}
    return labels, stage_map


def stage_name(stage_map, stage_id):
    if not stage_id:
        return None
    parts = str(stage_id).split(":")
    if len(parts) >= 3:
        status = parts[-1]
        cat = int(parts[1]) if parts[1].isdigit() else 0
    elif len(parts) == 2:
        status = parts[1]
        cat = 0
    else:
        return None
    entity = "DEAL_STAGE_26" if cat else "DEAL_STAGE_24"
    return stage_map.get((entity, status))


# --------------------------------------------------------------------------
# дела
# --------------------------------------------------------------------------


def export_deal(errors, index, labels, did):
    entity = safe(errors, "crm.deal.get", [_f("id", did)], "pick", "crm.deal.get id=%s" % did)
    contacts = safe(errors, "crm.deal.contact.items.get", [_f("id", did)], "pick",
                    "crm.deal.contact.items.get id=%s" % did)
    productrows = safe(errors, "crm.deal.productrows.get", [_f("id", did)], "pick",
                       "crm.deal.productrows.get id=%s" % did)
    activities = safe(errors, "crm.activity.list",
                      [_filt("OWNER_TYPE_ID", OWNER_TYPE["deal"]), _filt("OWNER_ID", did)] + _sel("*"),
                      "all", "crm.activity.list deal=%s" % did)
    comments = safe(errors, "crm.timeline.comment.list",
                    [_filt("ENTITY_TYPE", "deal"), _filt("ENTITY_ID", did)],
                    "all", "crm.timeline.comment.list deal=%s" % did)
    payload = {
        "entity": entity,
        "contacts": contacts,
        "productrows": productrows,
        "activities": activities,
        "comments": comments,
    }
    rel = "deals/%s.json" % did
    write_json(rel, payload)
    title = ""
    if isinstance(entity, dict):
        title = entity.get("TITLE") or ""
    index["deals"].append({"id": did, "title": title, "file": rel})
    return entity, contacts, payload


# --------------------------------------------------------------------------
# компании
# --------------------------------------------------------------------------


def export_company(errors, index, labels, stage_map, cid):
    entity = safe(errors, "crm.company.get", [_f("id", cid)], "pick", "crm.company.get id=%s" % cid)
    contacts = safe(errors, "crm.company.contact.items.get", [_f("id", cid)], "pick",
                    "crm.company.contact.items.get id=%s" % cid)
    requisites = safe(errors, "crm.requisite.list",
                      [_filt("ENTITY_TYPE_ID", OWNER_TYPE["company"]), _filt("ENTITY_ID", cid)],
                      "all", "crm.requisite.list company=%s" % cid)
    deals = safe(errors, "crm.deal.list",
                 [_filt("COMPANY_ID", cid)] + _sel(*DEAL_LIST_SELECT),
                 "all", "crm.deal.list COMPANY_ID=%s" % cid)
    activities = safe(errors, "crm.activity.list",
                      [_filt("OWNER_TYPE_ID", OWNER_TYPE["company"]), _filt("OWNER_ID", cid)] + _sel("*"),
                      "all", "crm.activity.list company=%s" % cid)
    comments = safe(errors, "crm.timeline.comment.list",
                    [_filt("ENTITY_TYPE", "company"), _filt("ENTITY_ID", cid)],
                    "all", "crm.timeline.comment.list company=%s" % cid)
    payload = {
        "entity": entity,
        "contacts": contacts,
        "requisites": requisites,
        "deals": deals,
        "activities": activities,
        "comments": comments,
    }
    rel = "companies/%s.json" % cid
    write_json(rel, payload)
    title = ""
    if isinstance(entity, dict):
        title = entity.get("TITLE") or ""
    index["companies"].append({"id": cid, "title": title, "file": rel})
    return entity, contacts, payload


# --------------------------------------------------------------------------
# контакты
# --------------------------------------------------------------------------


def collect_contact_ids(deal_items, company_items):
    ids = set()

    def walk(v):
        if isinstance(v, dict):
            cid = v.get("CONTACT_ID")
            if cid not in (None, "", "0"):
                try:
                    ids.add(int(cid))
                except (TypeError, ValueError):
                    pass
        elif isinstance(v, list):
            for x in v:
                walk(x)

    for _, contacts, _ in deal_items:
        walk(contacts)
    for _, contacts, _ in company_items:
        walk(contacts)
    return sorted(ids)


def export_contact(errors, index, labels, cid):
    entity = safe(errors, "crm.contact.get", [_f("id", cid)], "pick", "crm.contact.get id=%s" % cid)
    activities = safe(errors, "crm.activity.list",
                      [_filt("OWNER_TYPE_ID", OWNER_TYPE["contact"]), _filt("OWNER_ID", cid)] + _sel("*"),
                      "all", "crm.activity.list contact=%s" % cid)
    comments = safe(errors, "crm.timeline.comment.list",
                    [_filt("ENTITY_TYPE", "contact"), _filt("ENTITY_ID", cid)],
                    "all", "crm.timeline.comment.list contact=%s" % cid)
    payload = {"entity": entity, "activities": activities, "comments": comments}
    rel = "contacts/%s.json" % cid
    write_json(rel, payload)
    name = ""
    if isinstance(entity, dict):
        name = " ".join(str(x) for x in (entity.get("NAME"), entity.get("LAST_NAME")) if x).strip()
    index["contacts"].append({"id": cid, "title": name or ("Contact %s" % cid), "file": rel})
    return entity, payload


# --------------------------------------------------------------------------
# README
# --------------------------------------------------------------------------


def _fmt_label(field, labels):
    return labels.get(field, field)


def _scalar_lines(d, keys, labels):
    lines = []
    for k in keys:
        v = d.get(k)
        if is_blank(v):
            continue
        lines.append("- %s: %s" % (_fmt_label(k, labels), v))
    return lines


def _uf_lines(d, labels):
    lines = []
    for k, v in d.items():
        if k.startswith("UF_") and not is_blank(v):
            lines.append("- %s: %s" % (_fmt_label(k, labels), v))
    return lines


def build_readme(index, labels, stage_map, deal_items, company_items, contact_items):
    L = []
    L.append("# Выгрузка Битрикс24 — «Евростекло / АНДА»")
    L.append("")
    L.append("- Источник: B24 REST (методы чтения), экспортировано %s" % index["exported_at"])
    L.append("")
    L.append("Только факты из CRM, без интерпретаций.")
    L.append("")

    L.append("## Сделки")
    for did, entity, payload in deal_items:
        L.append("")
        if not isinstance(entity, dict):
            L.append("### Сделка %s (ошибка)" % did)
            continue
        L.append("### %s" % (entity.get("TITLE") or "Сделка %s" % did))
        L.extend(_scalar_lines(entity, ["ID", "STAGE_ID", "COMPANY_ID", "CONTACT_ID", "OPPORTUNITY",
                                        "CURRENCY_ID", "DATE_CREATE", "DATE_MODIFY", "ASSIGNED_BY_ID",
                                        "BEGINDATE", "CLOSEDATE"], labels))
        st = stage_name(stage_map, entity.get("STAGE_ID"))
        if st:
            L.append("- Стадия: %s" % st)
        L.extend(_uf_lines(entity, labels))
        L.append("- Деятельность (activity): %d" % len(as_list(payload["activities"])))
        L.append("- Комментарии (timeline): %d" % len(as_list(payload["comments"])))
        L.append("- Позиции (productrows): %d" % len(as_list(payload["productrows"])))
        L.append("- JSON: `deals/%s.json`" % did)

    L.append("")
    L.append("## Компании")
    for cid, entity, payload in company_items:
        L.append("")
        if not isinstance(entity, dict):
            L.append("### Компания %s (ошибка)" % cid)
            continue
        L.append("### %s" % (entity.get("TITLE") or "Компания %s" % cid))
        L.extend(_scalar_lines(entity, ["ID", "COMPANY_TYPE", "INDUSTRY", "ASSIGNED_BY_ID", "DATE_CREATE",
                                        "DATE_MODIFY"], labels))
        L.extend(_uf_lines(entity, labels))
        L.append("- Сделки компании: %d" % len(as_list(payload["deals"])))
        for d in as_list(payload["deals"]):
            if not isinstance(d, dict):
                continue
            t = d.get("TITLE") or d.get("ID")
            s = stage_name(stage_map, d.get("STAGE_ID"))
            L.append("  - %s (%s)%s" % (t, d.get("STAGE_ID"), " — %s" % s if s else ""))
        L.append("- Реквизиты: %d" % len(as_list(payload["requisites"])))
        L.append("- Деятельность (activity): %d" % len(as_list(payload["activities"])))
        L.append("- Комментарии (timeline): %d" % len(as_list(payload["comments"])))
        L.append("- JSON: `companies/%s.json`" % cid)

    L.append("")
    L.append("## Контакты")
    for cid, entity, payload in contact_items:
        L.append("")
        if not isinstance(entity, dict):
            L.append("### Контакт %s (ошибка)" % cid)
            continue
        name = " ".join(str(x) for x in (entity.get("NAME"), entity.get("LAST_NAME")) if x).strip()
        L.append("### %s" % (name or "Контакт %s" % cid))
        L.extend(_scalar_lines(entity, ["ID", "POST", "PHONE", "EMAIL", "COMPANY_ID", "ASSIGNED_BY_ID",
                                        "DATE_CREATE"], labels))
        L.extend(_uf_lines(entity, labels))
        L.append("- Деятельность (activity): %d" % len(as_list(payload["activities"])))
        L.append("- Комментарии (timeline): %d" % len(as_list(payload["comments"])))
        L.append("- JSON: `contacts/%s.json`" % cid)

    L.append("")
    L.append("## Ошибки отдельных методов")
    if index["errors"]:
        for e in index["errors"]:
            L.append("- %s" % e)
    else:
        L.append("- нет")

    with open(os.path.join(OUT, "README.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


# --------------------------------------------------------------------------
# главная
# --------------------------------------------------------------------------


def main():
    errors = []
    index = {
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "source": "b24",
        "deals": [],
        "companies": [],
        "contacts": [],
        "errors": errors,
    }
    os.makedirs(OUT, exist_ok=True)

    labels, stage_map = collect_meta(errors, index)

    deal_items = []
    for did in DEAL_IDS:
        entity, contacts, payload = export_deal(errors, index, labels, did)
        deal_items.append((did, entity, payload))

    company_items = []
    for cid in COMPANY_IDS:
        entity, contacts, payload = export_company(errors, index, labels, stage_map, cid)
        company_items.append((cid, entity, payload))

    contact_ids = collect_contact_ids(deal_items, company_items)
    contact_items = []
    for cid in contact_ids:
        entity, payload = export_contact(errors, index, labels, cid)
        contact_items.append((cid, entity, payload))

    # чистим служебные key/value, если хотим оставить index чистым — сохраняем как есть
    index.pop("labels", None)
    index.pop("stage_map", None)

    write_json("index.json", index)
    build_readme(index, labels, stage_map, deal_items, company_items, contact_items)

    print("exported deals=%d companies=%d contacts=%d errors=%d -> %s"
          % (len(index["deals"]), len(index["companies"]), len(index["contacts"]), len(errors), OUT))
    return 0


if __name__ == "__main__":
    sys = __import__("sys")
    sys.exit(main())
