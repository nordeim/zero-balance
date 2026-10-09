// v28 sweep: details dialog — Escape close + mobile bottom-sheet geometry
// (run at 390x844 for the mobile read; reopens the first card's dialog).
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const isOpen = () => [...document.querySelectorAll("div")].some((d) =>
    /Budget Item Details/.test(d.textContent || "") &&
    d.getBoundingClientRect().width > 0 && d.getBoundingClientRect().height < 100 &&
    getComputedStyle(d.parentElement).position === "fixed");
  const cards = [...document.querySelectorAll("main div.rounded-xl")].filter((c) => c.getBoundingClientRect().width > 200);
  cards[0].click();
  await sleep(900);
  if (!isOpen()) return JSON.stringify({ error: "dialog did not open" });
  // geometry at the CURRENT viewport
  const panel = [...document.querySelectorAll("div")].find((d) => /max-h-\[85vh\]|max-h-\[90vh\]/.test((d.className || "").toString()) && d.getBoundingClientRect().width > 100);
  const pr = panel.getBoundingClientRect();
  const pcs = getComputedStyle(panel);
  const out = {
    viewport: { w: innerWidth, h: innerHeight },
    panel: { x: Math.round(pr.x), y: Math.round(pr.y), w: Math.round(pr.width), h: Math.round(pr.height), radius: pcs.borderRadius, maxH: pcs.maxHeight, overflowY: pcs.overflowY },
  };
  // Escape
  document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape", bubbles: true, cancelable: true }));
  await sleep(600);
  out.closedOnEscape = !isOpen();
  return JSON.stringify(out, null, 1);
})()
