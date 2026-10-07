(() => {
  const form = [...document.querySelectorAll('form')].find((f) => /Save Asset|Save Liability|Save Item|Save Changes/.test(f.textContent || ''));
  if (!form) return JSON.stringify({ err: 'no form' });
  const grid = form.querySelector('.grid') || form.firstElementChild;
  const gc = getComputedStyle(grid);
  const fields = [...grid.children].map((c) => {
    const lbl = c.querySelector('label');
    const input = c.querySelector('input, textarea, button[role="combobox"], select');
    const r = c.getBoundingClientRect();
    return {
      label: (lbl?.textContent || '').trim(),
      x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width),
      span: /col-span-2/.test(c.className) ? 'span2' : '',
      lblSvg: lbl ? lbl.querySelectorAll('svg').length : 0,
      inputW: input ? Math.round(input.getBoundingClientRect().width) : null,
      disabled: input ? (input.disabled === true || input.getAttribute('aria-disabled') === 'true') : null,
    };
  });
  return JSON.stringify({ gridCols: gc.gridTemplateColumns, gridDisplay: gc.display, fields }, null, 1);
})()
