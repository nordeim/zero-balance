(() => {
  const h = [...document.querySelectorAll('h2')].find((e) => /Edit Budget Item/.test(e.textContent || ''));
  if (!h) return JSON.stringify({ err: 'no heading' });
  let panel = h;
  while (panel.parentElement && getComputedStyle(panel).backgroundColor !== 'rgb(255, 255, 255)') panel = panel.parentElement;
  const cs = (el) => getComputedStyle(el);
  const btns = [...panel.querySelectorAll('button')].filter((b) => /^(Save|Cancel|Delete|Update)/.test((b.textContent || '').trim()));
  const footer = btns.map((b) => ({ text: (b.textContent || '').trim(), bg: (cs(b).backgroundImage || 'none').slice(0, 90), svg: b.querySelectorAll('svg').length }));
  const grid = panel.querySelector('.grid');
  const fields = grid ? [...grid.children].map((c) => {
    const lbl = c.querySelector('label');
    const input = c.querySelector('input, textarea, button[role="combobox"]');
    return { label: (lbl?.textContent || '').trim().slice(0, 24), span: /col-span-2/.test(c.className) ? 'span2' : '', w: Math.round(c.getBoundingClientRect().width), disabled: input ? input.disabled === true || input.getAttribute('aria-disabled') === 'true' : false };
  }) : null;
  return JSON.stringify({ footer, gridCols: grid ? cs(grid).gridTemplateColumns : null, fields }, null, 1);
})()
