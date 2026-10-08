// probe-v11-viewport2.mjs — breakpoint boundary: main content offset + topbar at current viewport
(() => {
  const out = { url: location.pathname, vw: innerWidth };
  const main = document.querySelector('main') || [...document.querySelectorAll('div')].find(d => d.getBoundingClientRect().width > 300 && d.getBoundingClientRect().width < innerWidth && d.querySelector && d.querySelector('h1'));
  if (main) { const r = main.getBoundingClientRect(); out.main = { x: Math.round(r.x), w: Math.round(r.width) }; }
  const h1 = document.querySelector('h1');
  if (h1) { const r = h1.getBoundingClientRect(); const cs = getComputedStyle(h1); out.h1 = { txt: (h1.textContent || '').trim().slice(0, 24), x: Math.round(r.x), y: Math.round(r.y), fs: cs.fontSize, fw: cs.fontWeight }; }
  out.sw = document.documentElement.scrollWidth;
  return JSON.stringify(out, null, 1);
})()
