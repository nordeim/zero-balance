// probe-v11-rail-overlap.mjs — precise: what is the 256px fixed element, and where does main sit?
(() => {
  const out = { vw: innerWidth };
  // all fixed/sticky wide-ish elements
  out.fixedPanels = [...document.querySelectorAll('nav, aside, div, header')].filter(d => {
    const r = d.getBoundingClientRect(); const cs = getComputedStyle(d);
    return (cs.position === 'fixed' || cs.position === 'sticky') && r.width > 150 && r.width < 400 && r.height > 300;
  }).map(d => {
    const r = d.getBoundingClientRect();
    return { tag: d.tagName, w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), display: getComputedStyle(d).display, cls: (d.className || '').toString().slice(0, 90) };
  }).slice(0, 6);
  // main element detail
  const main = document.querySelector('main');
  if (main) {
    const r = main.getBoundingClientRect(); const cs = getComputedStyle(main);
    out.main = { x: Math.round(r.x), w: Math.round(r.width), ml: cs.marginLeft, cls: (main.className || '').toString().slice(0, 90) };
    // first card inside main — is it under the rail?
    const card = main.querySelector('h1, h2, [class*="card"]');
    if (card) { const cr = card.getBoundingClientRect(); out.firstContent = { txt: (card.textContent || '').trim().slice(0, 18), x: Math.round(cr.x) }; }
  }
  return JSON.stringify(out, null, 1);
})()
