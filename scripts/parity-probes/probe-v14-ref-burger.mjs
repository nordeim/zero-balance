// probe-v14-ref-burger.mjs — the reference burger via the sr-only span finder
// (v13 gotcha: no aria-label, textContent NOT empty — 'Toggle Sidebar' sr-only
// span inside). Then the R1 hit-test at its center.
(() => {
  const out = { url: location.pathname };
  const burger = [...document.querySelectorAll("button")].find(b =>
    b.textContent.includes("Toggle Sidebar") || (b.getAttribute("aria-label") || "").toLowerCase().includes("sidebar"));
  if (burger) {
    const r = burger.getBoundingClientRect();
    out.burger = { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), label: burger.getAttribute("aria-label"), text: burger.textContent.trim().slice(0, 40) };
    const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
    const hit = document.elementFromPoint(cx, cy);
    out.hitCenter = { tag: hit ? hit.tagName : null, cls: hit ? (hit.className || "").toString().slice(0, 70) : null, isBurger: hit === burger || burger.contains(hit) };
    // also probe the exposed bottom half (y = r.y + r.height - 4)
    const hitB = document.elementFromPoint(cx, r.y + r.height - 4);
    out.hitBottom = { tag: hitB ? hitB.tagName : null, isBurger: hitB === burger || burger.contains(hitB) };
  } else out.burger = "NOT FOUND";
  return JSON.stringify(out, null, 1);
})()
