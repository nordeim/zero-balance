// v30 reference probe: the "Needs vs Wants vs Savings" guideline rows (class + computed, rest state)
(() => {
  const out = {};
  // find the rows by their tinted backgrounds — the row contains a % + description
  const head = [...document.querySelectorAll('main p, main h3, main h4')].find(h => /Needs vs Wants vs Savings/i.test(h.textContent || ''));
  out.found = !!head;
  if (!head) return JSON.stringify(out);
  // the rows live in a sibling container; find all rounded containers with a % inside
  const scope = head.closest('div');
  const rows = [...scope.querySelectorAll('div')].filter(d => {
    const txt = d.textContent || '';
    return /%$|^\d+\.\d+%/.test(d.textContent || '') === false && /\d+\.\d+%/.test(txt) && d.querySelectorAll('p').length >= 1 && d.className && typeof d.className === 'string' && /rounded/.test(d.className) && (d.textContent.match(/%/g) || []).length <= 2 && d.querySelectorAll('div').length <= 3;
  });
  out.rows = rows.map(r => {
    const cs = getComputedStyle(r);
    return {
      tag: r.tagName,
      cls: r.className.slice(0, 250),
      bg: cs.backgroundColor,
      border: cs.border,
      radius: cs.borderRadius,
      pad: cs.padding,
      transition: cs.transition,
      cursor: cs.cursor,
      hasHoverClass: /hover/i.test(r.className || '')
    };
  });
  return JSON.stringify(out);
})()
