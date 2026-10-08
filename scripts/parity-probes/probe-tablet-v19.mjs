// v19 session: tablet breakpoint re-measurement (767/768/1024) — the
// v11-verified rail↔mobile-chrome switch, content column offset, overflow.
(() => {
  const out = {};
  const w = document.documentElement.clientWidth;
  out.viewport = w;
  // the rail: visible >=768 (md), hidden below
  const rail = [...document.querySelectorAll('div,aside')].find((d) => /fixed inset-y-0/.test((d.className || '').toString()) && /sidebar|--sidebar-width/.test((d.className || '').toString()));
  if (rail) { const r = rail.getBoundingClientRect(); out.rail = { display: getComputedStyle(rail).display, x: Math.round(r.x), w: Math.round(r.width) }; }
  else out.rail = 'NOT_FOUND';
  // the mobile top bar: hidden >=768
  const header = document.querySelector('header');
  if (header) { const r = header.getBoundingClientRect(); out.header = { display: getComputedStyle(header).display, h: Math.round(r.height) }; }
  // the main content offset
  const main = document.querySelector('main');
  if (main) { const r = main.getBoundingClientRect(); out.main = { x: Math.round(r.x), w: Math.round(r.width) }; }
  out.scrollWidth = document.documentElement.scrollWidth;
  return JSON.stringify(out, null, 1);
})()
