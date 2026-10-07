// probe-v8-rail-ref.mjs — find the reference's rail by geometry (no <aside> element)
(() => {
  const out = { url: location.pathname };
  // the rail: a tall narrow column on the left (fixed or first flex child)
  const candidates = [...document.querySelectorAll("div, nav, section")].filter(el => {
    const cs = getComputedStyle(el);
    if (cs.display === "none" || cs.position === "static") return false;
    const r = el.getBoundingClientRect();
    return r.width >= 250 && r.width <= 270 && r.height > 600;
  });
  const rail = candidates[0];
  if (!rail) return JSON.stringify({ err: "no rail found", bodyChildren: [...document.body.children].map(c => c.tagName + "." + (c.className || "").toString().slice(0, 40)) });
  const rr = rail.getBoundingClientRect();
  const rcs = getComputedStyle(rail);
  out.rail = { tag: rail.tagName, w: Math.round(rr.width), h: Math.round(rr.height), borderRight: rcs.borderRightWidth + " " + rcs.borderRightColor, cls: (rail.className || "").toString().slice(0, 90) };
  // brand block
  const brand = rail.querySelector("h2, h1");
  if (brand) {
    const br = brand.getBoundingClientRect();
    out.brand = { text: brand.textContent?.trim().slice(0, 16), size: getComputedStyle(brand).fontSize, weight: getComputedStyle(brand).fontWeight, x: Math.round(br.x), y: Math.round(br.y), h: Math.round(br.height) };
    const brandRow = brand.closest("div");
    if (brandRow) out.brandRow = { h: Math.round(brandRow.getBoundingClientRect().height) };
    const tile = brand.parentElement?.querySelector("div") || brand.previousElementSibling;
    if (tile) {
      const tr = tile.getBoundingClientRect();
      const tcs = getComputedStyle(tile);
      out.brandTile = { w: Math.round(tr.width), h: Math.round(tr.height), radius: tcs.borderRadius, grad: tcs.backgroundImage !== "none" ? tcs.backgroundImage.slice(0, 60) : tcs.backgroundColor };
      const tsvg = tile.querySelector("svg");
      if (tsvg) { const sr = tsvg.getBoundingClientRect(); out.brandTileSvg = { w: Math.round(sr.width), color: getComputedStyle(tsvg).color }; }
    }
  }
  // nav label
  const label = [...rail.querySelectorAll("*")].find(el => el.children.length === 0 && /^navigation$/i.test(el.textContent?.trim() || ""));
  if (label) out.navLabel = { y: Math.round(label.getBoundingClientRect().y), size: getComputedStyle(label).fontSize, weight: getComputedStyle(label).fontWeight, color: getComputedStyle(label).color, letterSpacing: getComputedStyle(label).letterSpacing };
  // nav links
  out.navLinks = [...rail.querySelectorAll("a")].map(a => {
    const ar = a.getBoundingClientRect();
    const acs = getComputedStyle(a);
    return { text: a.textContent?.trim().slice(0, 18), href: a.getAttribute("href"), h: Math.round(ar.height), y: Math.round(ar.y), x: Math.round(ar.x), size: acs.fontSize, weight: acs.fontWeight, color: acs.color, bg: acs.backgroundColor, radius: acs.borderRadius, pad: acs.padding };
  });
  return JSON.stringify(out, null, 1);
})()
