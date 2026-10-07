// probe-v7-railgeom.mjs — rail computed geometry: border, padding chain, label offset
(() => {
  const out = {};
  const rail = document.querySelector("aside") || [...document.querySelectorAll("div")].find(d => /fixed/.test(d.className?.toString?.() || "") && d.querySelector('a[href="/dashboard"]'));
  if (!rail) return JSON.stringify({ err: "no rail" });
  const rcs = getComputedStyle(rail);
  out.rail = {
    borderRight: rcs.borderRightWidth + " " + rcs.borderRightColor,
    w: rail.getBoundingClientRect().width, display: rcs.display,
    bg: rcs.backgroundColor,
  };
  // scroll container (flex-1 overflow-auto)
  const scroll = [...rail.querySelectorAll("div")].find(d => /overflow-auto/.test(d.className?.toString?.() || ""));
  if (scroll) {
    const scs = getComputedStyle(scroll);
    out.scroll = { padding: scs.padding, cls: (scroll.className || "").toString().slice(0, 110) };
  }
  // the Navigation label + its x-position relative to the rail
  const label = [...rail.querySelectorAll("div")].find(d => d.children.length === 0 && /Navigation/i.test(d.textContent || ""));
  if (label) {
    const lr = label.getBoundingClientRect();
    const rr = rail.getBoundingClientRect();
    out.label = {
      x: Math.round(lr.left - rr.left), y: Math.round(lr.top - rr.top),
      w: Math.round(lr.width), h: Math.round(lr.height),
      cls: (label.className || "").toString(),
      size: getComputedStyle(label).fontSize, color: getComputedStyle(label).color,
      tracking: getComputedStyle(label).letterSpacing,
    };
  }
  // first nav link x-position
  const link = rail.querySelector('a[href="/dashboard"]');
  if (link) {
    const lr = link.getBoundingClientRect();
    const rr = rail.getBoundingClientRect();
    out.firstLink = { x: Math.round(lr.left - rr.left), y: Math.round(lr.top - rr.top), w: Math.round(lr.width), h: Math.round(lr.height) };
  }
  // ul wrapper text-sm div
  const ul = rail.querySelector("ul");
  out.ulParentCls = (ul?.parentElement?.className || "").toString().slice(0, 90);
  // brand block y-offset
  const brand = [...rail.querySelectorAll("h2")].find(h => h.textContent?.trim() === "ZeroBalance");
  if (brand) {
    const br = brand.getBoundingClientRect();
    const rr = rail.getBoundingClientRect();
    out.brand = { x: Math.round(br.left - rr.left), y: Math.round(br.top - rr.top) };
  }
  return JSON.stringify(out, null, 1);
})()
