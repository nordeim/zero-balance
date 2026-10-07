// probe-v8-hamburger.mjs — find the real hamburger toggle (small svg button near top-left)
(() => {
  const out = { url: location.pathname };
  const btns = [...document.querySelectorAll("button")].filter(b => {
    const r = b.getBoundingClientRect();
    if (r.width === 0 || r.y > 120 || r.x > 80) return false;
    return r.width <= 36 && r.height <= 36 && !!b.querySelector("svg");
  });
  out.topLeftButtons = btns.map(b => {
    const r = b.getBoundingClientRect();
    const cs = getComputedStyle(b);
    const svg = b.querySelector("svg");
    const sr = svg ? svg.getBoundingClientRect() : null;
    // hit test at button center
    const hit = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2);
    return {
      aria: b.getAttribute("aria-label"),
      w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y),
      svgW: sr ? Math.round(sr.width) : null, color: cs.color, pad: cs.padding, radius: cs.borderRadius,
      svgFlexShrink: svg ? getComputedStyle(svg).flexShrink : null,
      hit: hit === b || b.contains(hit) ? "DIRECT" : `BLOCKED(${hit ? hit.tagName + "." + (hit.className || "").toString().slice(0, 40) : "none"})`,
      parent: b.parentElement?.tagName + "." + (b.parentElement?.className || "").toString().slice(0, 50),
    };
  });
  // mobile topbar row: the row containing the hamburger
  if (btns[0]) {
    let row = btns[0].closest("div");
    for (let i = 0; i < 3 && row; i++) {
      const rr = row.getBoundingClientRect();
      if (rr.height > 40 && rr.height < 90 && rr.width > 200) break;
      row = row.parentElement;
    }
    if (row) {
      const rr = row.getBoundingClientRect();
      const rc = getComputedStyle(row);
      out.topbarRow = { w: Math.round(rr.width), h: Math.round(rr.height), display: rc.display, pad: rc.padding, gap: rc.gap, bg: rc.backgroundColor, cls: (row.className || "").toString().slice(0, 90) };
      const h1 = row.querySelector("h1, h2");
      if (h1) out.rowTitle = { tag: h1.tagName, text: h1.textContent?.trim().slice(0, 28), size: getComputedStyle(h1).fontSize, weight: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color };
    }
  }
  return JSON.stringify(out, null, 1);
})()
