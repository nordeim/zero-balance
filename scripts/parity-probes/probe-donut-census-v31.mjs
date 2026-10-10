(() => {
  // find the recharts pie sectors
  const sectors = [...document.querySelectorAll('.recharts-pie-sector, path.recharts-pie-sector')];
  const pie = document.querySelector('.recharts-pie');
  const details = sectors.slice(0, 4).map(s => {
    const cs = getComputedStyle(s);
    const attrs = {};
    ['tabindex', 'tabIndex', 'role', 'aria-label', 'focusable'].forEach(a => { const v = s.getAttribute(a); if (v !== null) attrs[a] = v; });
    return { tag: s.tagName, attrs, cursor: cs.cursor, pointerEvents: cs.pointerEvents };
  });
  const pieSvg = document.querySelector('.recharts-surface');
  return JSON.stringify({
    sectorCount: sectors.length,
    sectors: details,
    pieExists: !!pie,
    svgTabIndex: pieSvg ? pieSvg.getAttribute('tabindex') : null,
    svgRole: pieSvg ? pieSvg.getAttribute('role') : null,
    svgFocusable: pieSvg ? pieSvg.getAttribute('focusable') : null
  }, null, 1);
})()
