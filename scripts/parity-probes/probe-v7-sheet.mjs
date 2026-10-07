// probe-v7-sheet.mjs — mobile sheet geometry + structure
(() => {
  const out = {};
  const link = document.querySelector('a[href="/dashboard"]');
  // find the sheet panel: walk up from a nav link to the fixed/transform panel
  let sheet = link;
  while (sheet && sheet !== document.body) {
    const c = sheet.className?.toString?.() || "";
    if (/fixed/.test(c) && sheet.getBoundingClientRect().width < 500) break;
    sheet = sheet.parentElement;
  }
  if (!sheet || sheet === document.body) return JSON.stringify({ err: "no sheet panel" });
  const scs = getComputedStyle(sheet);
  out.sheet = {
    cls: (sheet.className || "").toString().slice(0, 130),
    w: Math.round(sheet.getBoundingClientRect().width),
    h: Math.round(sheet.getBoundingClientRect().height),
    x: Math.round(sheet.getBoundingClientRect().left),
    bg: scs.backgroundColor, z: scs.zIndex,
    transform: scs.transform !== "none" ? scs.transform : "none",
    borderR: scs.borderRightWidth + " " + scs.borderRightColor,
    shadow: scs.boxShadow.slice(0, 60),
  };
  // overlay
  const ov = [...document.querySelectorAll("div")].find(d => {
    const c = d.className?.toString?.() || "";
    return /fixed/.test(c) && /inset-0/.test(c) && d !== sheet && !sheet.contains(d);
  });
  out.overlay = ov ? { cls: ov.className.toString().slice(0, 90), bg: getComputedStyle(ov).backgroundColor, z: getComputedStyle(ov).zIndex } : null;
  // sheet content skeleton (top 14 lines)
  const lines = [];
  const walk = (el, depth) => {
    if (depth > 4 || lines.length > 16) return;
    const cls = (el.className?.toString?.() || "").replace(/\s+/g, " ").slice(0, 70);
    const txt = el.children.length === 0 ? (el.textContent || "").trim().slice(0, 24) : "";
    lines.push("  ".repeat(depth) + el.tagName.toLowerCase() + (cls ? " ." + cls.split(" ").join(".") : "") + (txt ? ` "${txt}"` : ""));
    [...el.children].forEach((c) => walk(c, depth + 1));
  };
  walk(sheet, 0);
  out.skeleton = lines.join("\n");
  return JSON.stringify(out, null, 1);
})()
