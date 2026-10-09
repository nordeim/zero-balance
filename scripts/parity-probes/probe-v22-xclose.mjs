(() => {
  const out = { vw: innerWidth };
  let dlg = document.querySelector("[role=dialog]");
  if (!dlg) {
    const h2 = [...document.querySelectorAll("h2")].find(h => /Calculator/i.test(h.textContent || ""));
    if (h2) dlg = h2.closest("[class*=fixed]");
  }
  if (!dlg) return JSON.stringify({ ...out, error: "no dialog" });
  const btns = [...dlg.querySelectorAll("button")];
  const xbtn = btns.find(b => {
    const r = b.getBoundingClientRect();
    return r.y < 120 && r.x > innerWidth - 120 && !b.textContent.trim();
  }) || btns[0];
  const r = xbtn.getBoundingClientRect();
  const cs = getComputedStyle(xbtn);
  const svg = xbtn.querySelector("svg");
  return JSON.stringify({
    vw: innerWidth,
    box: { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y) },
    border: cs.border, bg: cs.backgroundColor, radius: cs.borderRadius, shadow: cs.boxShadow.slice(0, 60),
    svg: svg ? { w: Math.round(svg.getBoundingClientRect().width), color: getComputedStyle(svg).color } : null,
  }, null, 1);
})()
