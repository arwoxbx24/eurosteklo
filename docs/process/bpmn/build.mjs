// BPMN swimlane process — type "bpmn". GENERIC template scaffolded via drawio-ai-kit.
// Roles (7 lanes) x phases (6 milestones); canonical mxgraph.bpmn shapes; the engine lays the
// pool out automatically (no hand-written coordinates). One root wrapper (phantom) so the next
// atoms can append boxes below the pool. Sequence flow is solid + rounded across lane bands.
import { writeFileSync } from "node:fs";
import { Diagram } from "/root/workspaces/projects/clients/tools/drawio-ai-kit/src/builder.mjs";
import { renderTree, phantom, box as engBox } from "/root/workspaces/projects/clients/tools/drawio-ai-kit/src/layout-engine.mjs";
import { pool, start, end, gateway, userTask } from "/root/workspaces/projects/clients/tools/drawio-ai-kit/src/bpmn.mjs";

const d = new Diagram("bpmn");

// Крупный шрифт — размер задач и ширина дорожки (выбор владельца 28.09).
const TASK = { w: 170, h: 90 };

// Широкий шаг колонок пула (90 px) — даёт место подписям связей и документов (TZ 004.6).
const GAP = 90;

// Compute pool width from children before creating anything
const poolChildren = [
  start("s1", { lane: 0, col: 1, label: "Заявка клиента" }),
  { ...userTask("t1", { lane: 1, col: 4, label: "Счёт за замер + задание" }), ...TASK },
  { ...userTask("t2", { lane: 2, col: 4, label: "Контроль замера" }), ...TASK },
  { ...userTask("c1", { lane: 0, col: 7, label: "КП, подпись, оплата" }), ...TASK },
  { ...userTask("t3", { lane: 1, col: 7, label: "Договор, предоплата" }), ...TASK },
  { ...userTask("t4", { lane: 1, col: 10, label: "Заказ в производство" }), ...TASK },
  { ...userTask("t5", { lane: 3, col: 10, label: "Запуск в производство" }), ...TASK },
  { ...userTask("t6", { lane: 4, col: 10, label: "Фурнитура, поставки" }), ...TASK },
  { ...userTask("c2", { lane: 0, col: 13, label: "Изделие или монтаж" }), ...TASK },
  { ...userTask("t7", { lane: 1, col: 13, label: "Отгрузка: оплата" }), ...TASK },
  { ...userTask("t8", { lane: 5, col: 13, label: "Монтаж: дата, фото" }), ...TASK },
  { ...gateway("gw1", { lane: 2, col: 13, label: "Отгрузка или монтаж?", type: "exclusive" }), w: 90, h: 90 },
  { ...userTask("t9", { lane: 6, col: 16, label: "Вернуть документы" }), ...TASK },
  { ...userTask("t10", { lane: 4, col: 16, label: "Звонки клиенту через 14, 90 и 270 дней" }), ...TASK },
  { ...end("e1", { lane: 3, col: 16, label: "Сделка завершена" }), w: 80, h: 80 },
  { ...end("e2", { lane: 1, col: 16, label: "Отказ", type: "error" }), w: 80, h: 80 },

  // T005: 6 document icons in lane 0 (Клиент) — kind:box with document shape style
  { kind: "box", id: "doc_inv", lane: 0, col: 4, label: "Счёт за замер", w: 120, h: 70, style: "shape=document;whiteSpace=wrap;html=1;fillColor=#F5F8FB;strokeColor=#1A1A1A;fontColor=#1A1A1A;fontSize=10;" },
  { kind: "box", id: "doc_agr", lane: 0, col: 6, label: "Договор", w: 120, h: 70, style: "shape=document;whiteSpace=wrap;html=1;fillColor=#F5F8FB;strokeColor=#1A1A1A;fontColor=#1A1A1A;fontSize=10;" },
  { kind: "box", id: "doc_prep", lane: 0, col: 8, label: "Счёт на предоплату", w: 140, h: 70, style: "shape=document;whiteSpace=wrap;html=1;fillColor=#F5F8FB;strokeColor=#1A1A1A;fontColor=#1A1A1A;fontSize=10;" },
  { kind: "box", id: "doc_bal", lane: 0, col: 12, label: "Счёт на оплату остатка", w: 160, h: 70, style: "shape=document;whiteSpace=wrap;html=1;fillColor=#F5F8FB;strokeColor=#1A1A1A;fontColor=#1A1A1A;fontSize=10;" },
  { kind: "box", id: "doc_upd", lane: 0, col: 14, label: "УПД и отгрузочные документы", w: 170, h: 70, style: "shape=document;whiteSpace=wrap;html=1;fillColor=#F5F8FB;strokeColor=#1A1A1A;fontColor=#1A1A1A;fontSize=10;" },
  { kind: "box", id: "doc_close", lane: 0, col: 16, label: "Закрывающие документы", w: 160, h: 70, style: "shape=document;whiteSpace=wrap;html=1;fillColor=#F5F8FB;strokeColor=#1A1A1A;fontColor=#1A1A1A;fontSize=10;" },
];

// Compute pool dimensions for box width
const maxCol = Math.max(1, ...poolChildren.map(c => (c.col ?? 0) + 1));
const pCellW = Math.max(...poolChildren.map(c => c.w || 0), 80);
const contentW = maxCol * pCellW + GAP * (maxCol - 1);
const poolW = 2 * 16 + 170 + contentW;

// T007: checklist box below the pool
const checkLines = [
  "Проход с клиентом",
  "1. кто разбирает новые заявки и за какой срок?",
  "2. что мешает дойти до замера?",
  "3. где это фиксируется сейчас?",
  "4. кто и когда переводит сделку дальше?",
  "5. монтаж — после отгрузки или вместо неё?",
  "6. звоните ли клиенту после сделки?",
  "7. куда уходит сделка при отказе?",
  "8. кто отвечает на каждом этапе?",
  "9. какая воронка рабочая?",
  "Уточнить: Монтаж: уточнить",
  "Уточнить: откуда — уточнить",
];
const checkH = checkLines.length * 20 + 12;
const chkBox = engBox("chk_list", checkLines.join("\n"), { w: poolW, h: checkH });

// T008: source box below checklist
const srcBox = engBox("src_box", "Источник: доска Miro клиента и портал Битрикс24, 28.09.2026", { w: poolW, h: 40 });

const proc = pool("sale", "Евростекло: процесс продаж", {
  lanes: [
    "Клиент",
    "Менеджер ОП",
    "Руководитель ПО",
    "Руководитель ПТО",
    "Руководитель ОС",
    "Руководитель службы сервиса",
    "Ассистент ОП",
  ],
  phases: [
    "1. Заявка",
    "2. Расчёт и замер",
    "3. Договор и оплата",
    "4. Производство",
    "5. Отгрузка или монтаж",
    "6. Завершение и сервис",
  ],
  laneLabel: 170,
  gap: GAP,
}, poolChildren);

// Root phantom stacks pool + boxes vertically (dir: "col" default)
const root = phantom("sale_root", "", { dir: "col", gap: 40 }, [proc, chkBox, srcBox]);
renderTree(d, root, [40, 80]);
d.title("Евростекло: процесс продаж — BPMN swimlane");

// sequence flow (solid, rounded) — FR-005: no flow:true
// T006: badges on ed1, ed2, ed3, ed6, ed8, ed14, ed16
d.link("s1", "t1", "", { rounded: true, badge: 1, badgePos: -0.6 }); // ed1
d.link("t1", "t2", "", { rounded: true, badge: 2, badgePos: -0.6 }); // ed2
d.link("t2", "t3", "", { rounded: true, badge: 3, badgePos: 0 }); // ed3
d.link("t3", "c1", "", { rounded: true }); // ed4
d.link("c1", "t4", "", { rounded: true }); // ed5
d.link("t4", "t5", "", { rounded: true, badge: 4, badgePos: 0 }); // ed6
d.link("t5", "t6", "", { rounded: true }); // ed7
d.link("t6", "gw1", "готово", { rounded: true, badge: 5, badgePos: 0.6 }); // ed8
d.link("gw1", "t7", "Отгрузка", { rounded: true }); // ed9
d.link("gw1", "t8", "Монтаж: уточнить", { rounded: true }); // ed10
d.link("t7", "c2", "", { rounded: true }); // ed11
d.link("t8", "c2", "", { rounded: true }); // ed12
d.link("c2", "t9", "", { rounded: true }); // ed13
d.link("t9", "t10", "", { rounded: true, badge: 6, badgePos: 0 }); // ed14
d.link("t10", "e1", "", { rounded: true }); // ed15
d.link("t3", "e2", "откуда — уточнить", { rounded: true, badge: 7, badgePos: 0.6 }); // ed16

// T005: dashed links from document icons to steps
d.link("doc_inv", "t1", "", { dash: true });
d.link("doc_agr", "t3", "", { dash: true });
d.link("doc_prep", "t3", "", { dash: true });
d.link("doc_bal", "t7", "", { dash: true });
d.link("doc_upd", "t7", "", { dash: true });
d.link("doc_close", "t9", "", { dash: true });

let xml = d.mxfile("Евростекло: процесс продаж (BPMN)");

// ponytail: шрифт и цвет поверх набора — выбор владельца 28.09
{
  const recolor = (v) => {
    if (/light-dark\(/.test(v)) return "#1A1A1A";
    const t = v.trim();
    const u = t.toUpperCase();
    if (u === "#1A1A1A" || u === "#D90000" || u === "#FFFFFF") return t;
    if (u === "#3F7D20") return "#D90000"; // badge green → problem red
    if (u === "WHITE" || u === "NONE" || t === "") return v;
    return "#1A1A1A";
  };
  const fixCell = (_m, id, pre, style, post) => {
    const hi = id === "__title" || /^sale__lane\d+$/.test(id) || /^sale__phase\d+$/.test(id);
    style = style.replace(/fontSize=(\d+)/, (_a, n) => `fontSize=${Math.max(16, Number(n), hi ? 18 : 0)}`);
    style = style.replace(/(fontColor|strokeColor|fillColor)=([^;]*)/g, (_a, k, v) => `${k}=${recolor(v)}`);
    return `<mxCell id="${id}"${pre}${style}${post}`;
  };
  xml = xml.replace(/<mxCell id="([^"]+)"([^>]*?style=")([^"]*)(")/g, fixCell);
}

writeFileSync(
  "/root/workspaces/projects/clients/eurosteklo/docs/process/bpmn/eurosteklo_process.drawio",
  xml,
);

// TZ 004.6: перенос нового D в V (атрибут data-mxgraph, как в ТЗ 004.5) + zoom:1 / auto-fit:false.
// Строка-страница остаётся неизменной, меняется только JSON в атрибуте (кодировка: & -> &amp;, ' -> &#39;).
{
  const viewPath = "/root/workspaces/projects/clients/eurosteklo/docs/process/bpmn/view.html";
  const head =
    '<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Евростекло — процесс продаж (BPMN)</title></head><body style="margin:0"><div class="mxgraph" data-mxgraph=\'';
  const tail =
    "'></div><script src=\"https://viewer.diagrams.net/js/viewer-static.min.js\"></script></body></html>";
  const escapeAttr = (s) => s.replace(/&/g, "&amp;").replace(/'/g, "&#39;");
  const graphConfig = JSON.stringify({
    xml,
    toolbar: "zoom layers",
    nav: true,
    zoom: 1,
    "auto-fit": false,
  });
  writeFileSync(viewPath, head + escapeAttr(graphConfig) + tail);
}
