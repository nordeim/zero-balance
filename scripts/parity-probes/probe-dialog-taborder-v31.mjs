(() => {
  const overlays = [...document.querySelectorAll('div')].filter(d => {
    const cs = getComputedStyle(d);
    return cs.position === 'fixed' && d.querySelector('input, select, textarea, form');
  });
  const o = overlays[overlays.length - 1];
  const focusables = [...o.querySelectorAll('button, input, select, textarea, a[href], [tabindex]')].filter(e => {
    if (e.getClientRects().length === 0 && e.type !== 'radio') return false;
    if (e.tabIndex === -1 && e.getAttribute('tabindex') !== null) return false; // explicitly -1
    if (e.getAttribute('aria-hidden') === 'true') return false;
    const cs = getComputedStyle(e);
    if (cs.display === 'none' || cs.visibility === 'hidden') return false;
    // truly invisible 1x1?
    const r = e.getBoundingClientRect();
    if (r.width <= 1 && r.height <= 1) return false;
    return e.tabIndex >= 0;
  });
  return focusables.map(e => {
    let label = '';
    if (/^(INPUT|SELECT|TEXTAREA)$/.test(e.tagName)) {
      label = (e.labels && e.labels[0]) ? e.labels[0].textContent.trim() : (e.getAttribute('aria-label') || e.getAttribute('name') || e.type || '');
    } else {
      label = (e.getAttribute('aria-label') || e.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 25);
    }
    return e.tagName + (label ? ':' + label : '') + (e.getAttribute('role') ? '(' + e.getAttribute('role') + ')' : '') + ' [tabindex=' + e.tabIndex + ']';
  }).join('\n');
})()
