// probe-v11-viewport.mjs — intermediate breakpoint audit: what chrome renders at this viewport?
(() => {
  const out = { url: location.pathname, vw: innerWidth, vh: innerHeight };
  // rail (desktop sidebar) present?
  const rail = [...document.querySelectorAll('nav, aside, div')].find(d => {
    const r = d.getBoundingClientRect(); const cs = getComputedStyle(d);
    return r.width >= 200 && r.width <= 270 && (cs.position === 'fixed' || cs.position === 'sticky') && r.height > 500;
  });
  // mobile topbar (burger) present?
  const burger = [...document.querySelectorAll('button')].find(x =>
    (x.textContent || '').trim() === 'Toggle Sidebar' ||
    (x.getAttribute('aria-label') || '').match(/enu|avigation|toggle/i));
  out.hasRail = !!rail; out.hasBurger = !!burger;
  if (rail) { const r = rail.getBoundingClientRect(); out.rail = { w: Math.round(r.width), x: Math.round(r.x), position: getComputedStyle(rail).position }; }
  if (burger) { const r = burger.getBoundingClientRect(); out.burger = { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y) }; }
  // horizontal overflow
  out.sw = document.documentElement.scrollWidth;
  // the topbar brand (mobile header) visible?
  const brand = [...document.querySelectorAll('h1, span, div')].filter(el => {
    const r = el.getBoundingClientRect(); const t = (el.textContent || '').trim();
    return /ZeroBalance|ZeroBudget/.test(t) && t.length < 20 && r.height > 0 && r.height < 40 && r.top < 80;
  })[0];
  if (brand) { const r = brand.getBoundingClientRect(); const cs = getComputedStyle(brand); out.mobileBrand = { txt: (brand.textContent || '').trim().slice(0, 12), fs: cs.fontSize, fw: cs.fontWeight, x: Math.round(r.x), y: Math.round(r.y) }; }
  return JSON.stringify(out, null, 1);
})()
