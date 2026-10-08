// probe-v14-accordion-hover.mjs — the Net Zero Breakdown section buttons
// (aria-expanded accordions): rest + hover computed styles. Plus a user-select
// sweep on money figures and badges.
(() => {
  const out = {};
  const btns = [...document.querySelectorAll('button')].filter(b => /^Total (Income|Savings|Expenses)/.test(b.textContent.trim()) && b.closest('main') && b.getBoundingClientRect().height > 0);
  out.btnCount = btns.length;
  if (btns.length) {
    const b = btns[0];
    const cs = getComputedStyle(b);
    const rest = { bg: cs.backgroundColor, color: cs.color, cursor: cs.cursor, fw: cs.fontWeight, border: cs.borderTopColor, w: Math.round(b.getBoundingClientRect().width), h: Math.round(b.getBoundingClientRect().height) };
    b.dispatchEvent(new MouseEvent('mouseover', { bubbles: true }));
    const cs2 = getComputedStyle(b);
    const hover = { bg: cs2.backgroundColor, color: cs2.color, cursor: cs2.cursor, fw: cs2.fontWeight };
    b.dispatchEvent(new MouseEvent('mouseout', { bubbles: true }));
    out.sectionBtn = { text: b.textContent.trim().replace(/\s+/g, ' ').slice(0, 30), rest, hover, expanded: b.getAttribute('aria-expanded') };
  }
  // chevron icon in the button
  if (btns.length) {
    const svg = btns[0].querySelector('svg');
    if (svg) { const r = svg.getBoundingClientRect(); out.chevron = { w: Math.round(r.width), h: Math.round(r.height), transform: getComputedStyle(svg).transform }; }
  }
  // user-select sweep: h1, money spans, badges
  const probes = {};
  const h1 = [...document.querySelectorAll('main h1')].find(h => h.getBoundingClientRect().height > 0);
  if (h1) probes.h1 = getComputedStyle(h1).userSelect;
  const money = [...document.querySelectorAll('main span, main div')].filter(e => /^\$[\d,]+\.\d{2}$/.test(e.textContent.trim()) && e.children.length === 0).slice(0, 1);
  if (money.length) probes.money = getComputedStyle(money[0]).userSelect;
  out.userSelect = probes;
  return JSON.stringify(out, null, 1);
})()
