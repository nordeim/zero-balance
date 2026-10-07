(() => {
  const form = [...document.querySelectorAll('form')].find((f) => /Edit Budget Item/.test(f.textContent || ''));
  if (!form) return JSON.stringify({ err: 'no form' });
  const cs = (el) => getComputedStyle(el);
  // footer buttons
  const btns = [...form.querySelectorAll('button')].filter((b) => /^(Save|Cancel|Delete|Update)/.test((b.textContent || '').trim()));
  const footer = btns.map((b) => ({ text: (b.textContent || '').trim(), bg: (cs(b).backgroundImage || 'none').slice(0, 90), svg: b.querySelectorAll('svg').length, color: cs(b).color, border: cs(b).borderColor, bw: cs(b).borderWidth }));
  // grid layout of form fields
  const grid = form.querySelector('.grid');
  const fields = grid ? [...grid.children].map((c) => {
    const lbl = c.querySelector('label');
    const input = c.querySelector('input, textarea, button[role="combobox"]');
    return { label: (lbl?.textContent || '').trim().slice(0, 24), span: /col-span-2/.test(c.className) ? 'span2' : '', w: Math.round(c.getBoundingClientRect().width), disabled: input ? input.disabled === true || input.getAttribute('aria-disabled') === 'true' : false };
  }) : null;
  // any delete row?
  const delText = /Delete/.test(form.textContent || '') ? 'HAS-DELETE' : 'NO-DELETE';
  return JSON.stringify({ footer, gridCols: grid ? cs(grid).gridTemplateColumns : null, fields, delText }, null, 1);
})()
