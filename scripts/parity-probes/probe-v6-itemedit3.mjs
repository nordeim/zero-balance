(() => {
  const btn = [...document.querySelectorAll('button')].find((b) => /^Save Item$/.test((b.textContent || '').trim()));
  if (!btn) return JSON.stringify({ err: 'no save btn' });
  let panel = btn;
  while (panel.parentElement && !/rounded-2xl/.test(panel.className || '')) panel = panel.parentElement;
  const cs = (el) => getComputedStyle(el);
  const grid = panel.querySelector('.grid');
  const fields = grid ? [...grid.children].map((c) => {
    const lbl = c.querySelector('label');
    const input = c.querySelector('input, textarea, button[role="combobox"]');
    return { label: (lbl?.textContent || '').trim().slice(0, 26), span: /col-span-2/.test(c.className) ? 'span2' : '', w: Math.round(c.getBoundingClientRect().width), disabled: input ? input.disabled === true || input.getAttribute('aria-disabled') === 'true' : false };
  }) : [];
  const save = { text: 'Save Item', bg: cs(btn).backgroundImage.slice(0, 95), svg: btn.querySelectorAll('svg').length };
  return JSON.stringify({ gridCols: grid ? cs(grid).gridTemplateColumns : null, save, fields }, null, 1);
})()
