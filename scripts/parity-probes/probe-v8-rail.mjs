// probe-v8-rail.mjs — desktop sidebar rail audit (brand block, nav links, active state, footer)
(() => {
  const out = { url: location.pathname };
  const aside = document.querySelector("aside");
  if (!aside) return JSON.stringify({ err: "no aside" });
  const r = aside.getBoundingClientRect();
  const cs = getComputedStyle(aside);
  out.rail = { w: Math.round(r.width), h: Math.round(r.height), borderRight: cs.borderRightWidth + " " + cs.borderRightColor, bg: cs.backgroundColor };
  // brand block: the 40x40 tile + logo text
  const brand = aside.querySelector("h2");
  if (brand) {
    const br = brand.getBoundingClientRect();
    const bcs = getComputedStyle(brand);
    out.brand = { text: brand.textContent?.trim().slice(0, 16), size: bcs.fontSize, weight: bcs.fontWeight, x: Math.round(br.x), y: Math.round(br.y), h: Math.round(br.height) };
    const brandRow = brand.closest("div");
    if (brandRow) out.brandRow = { h: Math.round(brandRow.getBoundingClientRect().height), gap: getComputedStyle(brandRow).gap };
    const tile = brand.parentElement?.querySelector("div");
    if (tile) {
      const tr = tile.getBoundingClientRect();
      const tcs = getComputedStyle(tile);
      out.brandTile = { w: Math.round(tr.width), h: Math.round(tr.height), radius: tcs.borderRadius, grad: tcs.backgroundImage !== "none" ? tcs.backgroundImage.slice(0, 60) : tcs.backgroundColor };
      const tsvg = tile.querySelector("svg");
      if (tsvg) { const sr = tsvg.getBoundingClientRect(); out.brandTileSvg = { w: Math.round(sr.width), color: getComputedStyle(tsvg).color }; }
    }
  }
  // nav label ("Navigation")
  const label = [...aside.querySelectorAll("*")].find(el => el.children.length === 0 && /^navigation$/i.test(el.textContent?.trim() || ""));
  if (label) out.navLabel = { text: label.textContent?.trim(), y: Math.round(label.getBoundingClientRect().y), size: getComputedStyle(label).fontSize, weight: getComputedStyle(label).fontWeight, color: getComputedStyle(label).color, letterSpacing: getComputedStyle(label).letterSpacing };
  // nav links
  out.navLinks = [...aside.querySelectorAll("a")].map(a => {
    const ar = a.getBoundingClientRect();
    const acs = getComputedStyle(a);
    return {
      text: a.textContent?.trim().slice(0, 18), href: a.getAttribute("href"),
      h: Math.round(ar.height), y: Math.round(ar.y), x: Math.round(ar.x),
      size: acs.fontSize, weight: acs.fontWeight, color: acs.color,
      bg: acs.backgroundColor, radius: acs.borderRadius, pad: acs.padding,
    };
  });
  // footer of rail
  const railFoot = aside.lastElementChild;
  if (railFoot) {
    const fr = railFoot.getBoundingClientRect();
    out.railFooter = { h: Math.round(fr.height), y: Math.round(fr.y), text: railFoot.textContent?.trim().slice(0, 60) };
  }
  return JSON.stringify(out, null, 1);
})()
