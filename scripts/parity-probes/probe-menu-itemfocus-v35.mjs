(async () => {
  // v35 Surface A: the menu ITEM focus chrome after a REAL ArrowDown.
  const menu = document.querySelector('[role="menu"]');
  if (!menu) return JSON.stringify({menuOpen: false});
  const items = [...menu.querySelectorAll('[role="menuitem"]')];
  const ae = document.activeElement;
  const cs = ae ? getComputedStyle(ae) : null;
  const read = (el) => {
    if (!el) return null;
    const c = getComputedStyle(el);
    return {
      bg: c.backgroundColor, color: c.color,
      boxShadow: c.boxShadow, outline: c.outline,
      focusMatch: el.matches(':focus'),
    };
  };
  return JSON.stringify({
    menuOpen: true,
    hasFocus: document.hasFocus(),
    active: ae ? (ae.tagName + ':' + (ae.getAttribute('role') || '') + ':' + (ae.textContent || '').trim().slice(0, 12)) : 'none',
    activeMatchesFocus: ae ? ae.matches(':focus') : false,
    hovered0: read(items[0]), hovered1: read(items[1]),
    itemRects: items.map(i => { const r = i.getBoundingClientRect(); return [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)]; }),
  });
})()
