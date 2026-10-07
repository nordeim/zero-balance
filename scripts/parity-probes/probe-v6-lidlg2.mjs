(() => {
  const btn = [...document.querySelectorAll('button')].find((b) => /Save Liability/.test(b.textContent || ''));
  if (!btn) return JSON.stringify({ err: 'no dialog' });
  let panel = btn;
  while (panel.parentElement && !/rounded-2xl/.test(panel.className || '')) panel = panel.parentElement;
  const grid = panel.querySelector('.grid');
  const fields = grid ? [...grid.children].map((c) => {
    const lbl = c.querySelector('label');
    const input = c.querySelector('input, textarea, button[role="combobox"]');
    return { label: (lbl?.textContent || '').trim().slice(0, 26), span: /col-span-2/.test(c.className) ? '2' : '', w: Math.round(c.getBoundingClientRect().width), ph: input?.getAttribute('placeholder') };
  }) : [];
  const save = { text: 'Save Liability', bg: getComputedStyle(btn).backgroundImage.slice(0, 90), svg: btn.querySelectorAll('svg').length };
  const title = panel.querySelector('h2, h3, h4');
  return JSON.stringify({ title: title?.textContent?.trim(), gridCols: grid ? getComputedStyle(grid).gridTemplateColumns : null, fields, save }, null, 1);
})()
