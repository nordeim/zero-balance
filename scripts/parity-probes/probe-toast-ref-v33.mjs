// probe-toast-ref-v33.mjs — the reference's toast viewport semantics + a live
// toast trigger + focus census. Run on / (the dashboard, logged in).
(() => {
  const els = [...document.querySelectorAll('body *')].filter(e => {
    const cs = getComputedStyle(e);
    return cs.position === 'fixed' && parseInt(cs.zIndex) >= 90 && e.getBoundingClientRect().width > 200;
  });
  const viewports = els.map(e => {
    const cs = getComputedStyle(e);
    return {
      tag: e.tagName, role: e.getAttribute('role'), ariaLive: e.getAttribute('aria-live'),
      ariaLabel: e.getAttribute('aria-label'), ariaAtomic: e.getAttribute('aria-atomic'),
      ti: e.tabIndex, pe: cs.pointerEvents, h: Math.round(e.getBoundingClientRect().height),
      kids: e.children.length, cls: String(e.className).slice(0, 50)
    };
  });
  return JSON.stringify({ z90plus: els.length, viewports }, null, 1);
})()
