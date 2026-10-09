(async () => {
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  const out = { vw: innerWidth, path: location.pathname, order: [] };
  // keyboard: Tab 12 times from the start, recording each focus target
  const synth = (key) => document.dispatchEvent(new KeyboardEvent("keydown", { key, bubbles: true }));
  // focus body first (reset)
  (document.activeElement || document.body).blur();
  document.body.focus();
  for (let i = 0; i < 12; i++) {
    synth("Tab");
    await sleep(60);
    const el = document.activeElement;
    if (!el || el === document.body) { out.order.push("(body-end)"); break; }
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    out.order.push({
      t: el.tagName,
      label: (el.getAttribute("aria-label") || el.textContent || "").trim().slice(0, 24),
      x: Math.round(r.x), y: Math.round(r.y),
      focusRing: (cs.boxShadow || "").slice(0, 60),
      outline: (cs.outlineStyle + " " + cs.outlineWidth).slice(0, 30),
    });
  }
  return JSON.stringify(out, null, 1);
})()
