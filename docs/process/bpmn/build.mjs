// BPMN swimlane process — type "bpmn". GENERIC template scaffolded via drawio-ai-kit.
// Roles (7 lanes) x phases (6 milestones); canonical mxgraph.bpmn shapes; the engine lays the
// pool out automatically (no hand-written coordinates). One root wrapper (phantom) so the next
// atoms can append boxes below the pool. Sequence flow is solid + rounded across lane bands.
import { writeFileSync } from "node:fs";
import { Diagram } from "/root/workspaces/projects/clients/tools/drawio-ai-kit/src/builder.mjs";
import { renderTree, phantom } from "/root/workspaces/projects/clients/tools/drawio-ai-kit/src/layout-engine.mjs";
import { pool, start, end, gateway, userTask } from "/root/workspaces/projects/clients/tools/drawio-ai-kit/src/bpmn.mjs";

const d = new Diagram("bpmn");

// Крупный шрифт — размер задач и ширина дорожки (выбор владельца 28.09).
const TASK = { w: 170, h: 90 };

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
}, [
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
  gateway("gw1", { lane: 2, col: 13, label: "Отгрузка или монтаж?", type: "exclusive" }),
  { ...userTask("t9", { lane: 6, col: 16, label: "Вернуть документы" }), ...TASK },
  { ...userTask("t10", { lane: 4, col: 16, label: "Звонки клиенту через 14, 90 и 270 дней" }), ...TASK },
  end("e1", { lane: 3, col: 16, label: "Сделка завершена" }),
  end("e2", { lane: 1, col: 16, label: "Отказ", type: "error" }),
]);

// one root wrapper (phantom, no cell) so atom .4 can add a box below the pool
const root = phantom("sale_root", "", { dir: "col" }, [proc]);
renderTree(d, root, [40, 80]);
d.title("Евростекло: процесс продаж — BPMN swimlane");

// sequence flow (solid, rounded) — handoffs cross lane bands
d.link("s1", "t1", "", { flow: true, rounded: true }); // ed1
d.link("t1", "t2", "", { flow: true, rounded: true }); // ed2
d.link("t2", "t3", "", { flow: true, rounded: true }); // ed3
d.link("t3", "c1", "", { flow: true, rounded: true }); // ed4
d.link("c1", "t4", "", { flow: true, rounded: true }); // ed5
d.link("t4", "t5", "", { flow: true, rounded: true }); // ed6
d.link("t5", "t6", "", { flow: true, rounded: true }); // ed7
d.link("t6", "gw1", "готово", { flow: true, rounded: true }); // ed8
d.link("gw1", "t7", "Отгрузка", { flow: true, rounded: true }); // ed9
d.link("gw1", "t8", "Монтаж: уточнить", { flow: true, rounded: true }); // ed10
d.link("t7", "c2", "", { flow: true, rounded: true }); // ed11
d.link("t8", "c2", "", { flow: true, rounded: true }); // ed12
d.link("c2", "t9", "", { flow: true, rounded: true }); // ed13
d.link("t9", "t10", "", { flow: true, rounded: true }); // ed14
d.link("t10", "e1", "", { flow: true, rounded: true }); // ed15
d.link("t3", "e2", "откуда — уточнить", { flow: true, rounded: true }); // ed16

let xml = d.mxfile("Евростекло: процесс продаж (BPMN)");

// ponytail: шрифт и цвет поверх набора — выбор владельца 28.09
// (в наборе нет API шрифта/цвета; одна пост-обработка строки XML)
{
  // любой fontColor/strokeColor вне {#1A1A1A, #D90000, белый} → #1A1A1A (light-dark целиком).
  const recolor = (v) => {
    if (/light-dark\(/.test(v)) return "#1A1A1A";
    const t = v.trim();
    const u = t.toUpperCase();
    if (u === "#1A1A1A" || u === "#D90000" || u === "#FFFFFF") return t;
    if (u === "WHITE" || u === "NONE" || t === "") return v;
    return "#1A1A1A";
  };
  // fontSize <16 → 16; у дорожек sale__lane*, фаз sale__phase* и заголовка __title → 18.
  const fixCell = (_m, id, pre, style, post) => {
    const hi = id === "__title" || /^sale__lane\d+$/.test(id) || /^sale__phase\d+$/.test(id);
    style = style.replace(/fontSize=(\d+)/, (_a, n) => `fontSize=${Math.max(16, Number(n), hi ? 18 : 0)}`);
    style = style.replace(/(fontColor|strokeColor)=([^;]*)/g, (_a, k, v) => `${k}=${recolor(v)}`);
    return `<mxCell id="${id}"${pre}${style}${post}`;
  };
  xml = xml.replace(/<mxCell id="([^"]+)"([^>]*?style=")([^"]*)(")/g, fixCell);
}

writeFileSync(
  "/root/workspaces/projects/clients/eurosteklo/docs/process/bpmn/eurosteklo_process.drawio",
  xml,
);
