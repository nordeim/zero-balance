(async () => {
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  const out = { vw: innerWidth };
  // find the calculator's row edit button and click it
  let dlg = document.querySelector("[role=dialog]");
  if (!dlg) {
    const h2 = [...document.querySelectorAll("h2")].find(h => /Calculator/i.test(h.textContent || ""));
    if (h2) dlg = h2.closest("[class*=fixed]");
  }
  if (!dlg) return JSON.stringify({ ...out, error: "no calculator" });
  const h4 = dlg.querySelector("h4");
  const row = h4.closest("div").parentElement;
  const btns = [...row.querySelectorAll("button")];
  out.rowBtnCount = btns.length;
  const edit = btns.find(b => {
    const svg = b.querySelector("svg");
    return svg && getComputedStyle(svg).color === "rgb(10, 10, 10)";
  });
  if (!edit) return JSON.stringify({ ...out, error: "no edit button" });
  edit.click();
  await sleep(800);
  // the sub-dialog: the topmost dialog/panel
  const panels = [...document.querySelectorAll("[role=dialog]")];
  let sub = panels[panels.length - 1];
  if (!sub || sub === dlg) {
    // reference: plain div panels — find by the Edit Item heading
    const h2s = [...document.querySelectorAll("h2")].map(h => h.textContent.trim());
    out.allH2 = h2s;
    sub = [...document.querySelectorAll("h2")].find(h => /Edit/i.test(h.textContent || ""))?.closest("[class*=fixed]") || null;
  }
  if (!sub) return JSON.stringify({ ...out, error: "no sub-dialog" });
  const r = sub.getBoundingClientRect();
  const cs = getComputedStyle(sub);
  const title = sub.querySelector("h2");
  const inputs = [...sub.querySelectorAll("input")].map(i => ({ label: i.getAttribute("aria-label") || i.name || i.placeholder, w: Math.round(i.getBoundingClientRect().width), h: Math.round(i.getBoundingClientRect().height), val: i.value }));
  const buttons = [...sub.querySelectorAll("footer button, button")].map(b => ({ t: b.textContent.trim().slice(0, 24), w: Math.round(b.getBoundingClientRect().width), h: Math.round(b.getBoundingClientRect().height) })).slice(0, 6);
  return JSON.stringify({
    ...out,
    subTitle: title ? title.textContent.trim() : null,
    panel: { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), bg: cs.backgroundColor, radius: cs.borderRadius },
    inputs,
    buttons,
  }, null, 1);
})()
