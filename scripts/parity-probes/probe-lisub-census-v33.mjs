// probe-lisub-census-v33.mjs — the line-item sub-dialog focusable census (ref side)
// Run with the Add Line Item sub-dialog OPEN. Reports every focusable stop
// with geometry + the sub-dialog panel's own box (the 85vh contract).
(() => {
  // the sub-dialog panel: the fixed overlay carrying the "Add Line Item" h2
  const h2 = [...document.querySelectorAll('h2')].find(h => /Add Line Item|Edit Line Item/.test(h.textContent || ''));
  if (!h2) return JSON.stringify({ err: 'no sub-dialog heading' });
  const panel = h2.closest('div.fixed, [data-state=open], div[class*="fixed"]') || h2.parentElement;
  for (let i = 0; i < 6 && panel.parentElement; i++) {
    const cs = getComputedStyle(panel.parentElement);
    if (cs.position === 'fixed') panel = panel.parentElement;
    else break;
  }
  const pr = panel.getBoundingClientRect();
  const pcs = getComputedStyle(panel);
  const panelInfo = {
    w: Math.round(pr.width), h: Math.round(pr.height),
    maxH: pcs.maxHeight, cls: String(panel.className).slice(0, 70),
    role: panel.getAttribute('role'), ariaModal: panel.getAttribute('aria-modal'),
    zIndex: pcs.zIndex
  };
  // strict focusable census INSIDE the panel
  const stops = [...panel.querySelectorAll('*')].filter(el => {
    if (el.matches('button, a[href], input, select, textarea, [tabindex]')) {
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.display === 'none') return false;
      const r = el.getBoundingClientRect();
      if (r.width === 0 && r.height === 0) return false;
      const ti = el.tabIndex;
      return ti === 0 || ti === 1;
    }
    return false;
  }).map(el => {
    const r = el.getBoundingClientRect();
    const lbl = el.getAttribute('aria-label') || el.getAttribute('placeholder') || el.textContent?.trim().slice(0, 22) || el.name || el.id;
    return {
      tag: el.tagName.toLowerCase(), lbl: String(lbl).slice(0, 28),
      w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y),
      ti: el.tabIndex, id: el.id || null, name: el.getAttribute('name') || null,
      type: el.getAttribute('type') || null
    };
  });
  // initial focus
  const ae = document.activeElement;
  const initFocus = ae === document.body ? 'BODY' : (panel.contains(ae) ? 'in-panel: ' + (ae.tagName.toLowerCase() + '/' + (ae.getAttribute('placeholder') || ae.textContent?.trim().slice(0, 20) || ae.id)) : 'OUTSIDE-panel: ' + ae.tagName.toLowerCase());
  return JSON.stringify({ panel: panelInfo, stops: stops.length, detail: stops, initFocus }, null, 1);
})()
