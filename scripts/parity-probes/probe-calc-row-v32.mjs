// v32: the populated calculator's focusable census (the strict tabindex-
// property discipline; the row actions are focusable inside their opacity-0
// hover-reveal container on BOTH sites — the reveal is hover-only).
// Prereq: the calculator open on an expense WITH at least one line item,
// pointer parked far from the row. bash scripts/parity-probes/run-probe.sh <session> probe-calc-row-v32.mjs
(() => {
  const calc = document.querySelector('[role=dialog]') ||
    [...document.querySelectorAll('div')].find(d => d.className && /fixed inset-0 z-50/.test(d.className) && d.textContent.includes('Calculator'));
  if (!calc) return 'no calculator open';
  const stop = (el) => {
    if (el.tagName === 'A' || el.tagName === 'BUTTON') return el.tabIndex !== -1;
    if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA' || el.tagName === 'SELECT') return !el.disabled;
    return el.tabIndex === 0;
  };
  const vis = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const focusables = [...calc.querySelectorAll('a, button, input, textarea, select, [tabindex]')].filter(el => stop(el) && vis(el) && !el.closest('[aria-hidden=true]'));
  return JSON.stringify({ count: focusables.length, stops: focusables.map(el => ({
    tag: el.tagName.toLowerCase(),
    name: (el.getAttribute('aria-label') || (el.textContent || '').trim().slice(0, 20) || '').slice(0, 24),
    tabindex: el.tabIndex, w: Math.round(el.getBoundingClientRect().width),
    op: getComputedStyle(el).opacity, contOp: getComputedStyle(el.parentElement).opacity
  })) });
})()
