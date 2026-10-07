// probe-v8-mobile-nav2.mjs — targeted mobile topbar (inside main) + fixed overlays
(() => {
  const out = { url: location.pathname, vw: innerWidth, sw: document.documentElement.scrollWidth };
  const main = document.querySelector("main");
  if (!main) return JSON.stringify({ err: "no main" });
  // topbar = first visible child block of main (the stacked header row)
  const firstRow = main.querySelector(":scope > div");
  if (firstRow) {
    const r = firstRow.getBoundingClientRect();
    const cs = getComputedStyle(firstRow);
    out.mainFirstRow = { w: Math.round(r.width), h: Math.round(r.height), display: cs.display, pad: cs.padding, cls: (firstRow.className || "").toString().slice(0, 80) };
    // toggle button inside it
    const tgl = [...firstRow.querySelectorAll("button")].find(b => b.querySelector("svg"));
    if (tgl) {
      const tr = tgl.getBoundingClientRect();
      const tcs = getComputedStyle(tgl);
      const svg = tgl.querySelector("svg");
      const sr = svg ? svg.getBoundingClientRect() : null;
      out.toggle = {
        w: Math.round(tr.width), h: Math.round(tr.height),
        svgW: sr ? Math.round(sr.width) : null, color: tcs.color,
        pe: tcs.pointerEvents, z: tcs.zIndex,
        svgShrink: svg ? getComputedStyle(svg).flexShrink : null,
      };
      // hit-test: is the toggle actually clickable (elementFromPoint)?
      const cx = tr.x + tr.width / 2, cy = tr.y + tr.height / 2;
      const hit = document.elementFromPoint(cx, cy);
      out.toggleHit = hit === tgl || tgl.contains(hit) ? "DIRECT" : (hit ? `BLOCKED by ${hit.tagName}.${(hit.className || "").toString().slice(0, 50)}` : "NONE");
    }
    // page title h1 in the topbar row
    const h1 = firstRow.querySelector("h1");
    if (h1) out.h1 = { text: h1.textContent?.trim().slice(0, 30), size: getComputedStyle(h1).fontSize, w: Math.round(h1.getBoundingClientRect().width) };
  }
  // ALL fixed-position elements (toast container / overlay detection)
  out.fixedEls = [...document.querySelectorAll("body *")].filter(el => {
    const cs = getComputedStyle(el);
    if (cs.position !== "fixed" || cs.display === "none") return false;
    const r = el.getBoundingClientRect();
    return r.width > 300 && r.height <= 60; // full-width short strips at top
  }).map(el => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return { tag: el.tagName, h: Math.round(r.height), y: Math.round(r.y), pe: cs.pointerEvents, z: cs.zIndex, cls: (el.className || "").toString().slice(0, 60) };
  });
  return JSON.stringify(out, null, 1);
})()
