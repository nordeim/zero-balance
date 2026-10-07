(() => {
  const btn = [...document.querySelectorAll('button')].find((b) => /^Save Item$/.test((b.textContent || '').trim()));
  if (!btn) return JSON.stringify({ err: 'no save btn' });
  let panel = btn;
  while (panel.parentElement && !/rounded-2xl/.test(panel.className || '')) panel = panel.parentElement;
  const cs = (el) => getComputedStyle(el);
  const grids = [...panel.querySelectorAll('.grid')].map((g) => ({
    cols: cs(g).gridTemplateColumns,
    children: [...g.children].map((c) => {
      const lbl = c.querySelector('label');
      const input = c.querySelector('input, textarea, button[role="combobox"], [role="radiogroup"], [role="switch"]');
      return {
        label: (lbl?.textContent || c.textContent || '').trim().slice(0, 22),
        span: /col-span-2/.test(c.className) ? '2' : '',
        disabled: input ? input.disabled === true || input.getAttribute('aria-disabled') === 'true' : false,
      };
    }),
  }));
  return JSON.stringify({ grids }, null, 1);
})()
