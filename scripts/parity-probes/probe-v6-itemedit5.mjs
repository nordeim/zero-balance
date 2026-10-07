(() => {
  const dlg = document.querySelector('[role="dialog"]');
  if (!dlg) return JSON.stringify({ err: 'no radix dialog' });
  const cs = (el) => getComputedStyle(el);
  const grids = [...dlg.querySelectorAll('.grid')].map((g) => ({
    cols: cs(g).gridTemplateColumns,
    children: [...g.children].map((c) => ({
      label: (c.querySelector('label')?.textContent || c.textContent || '').trim().slice(0, 24),
      span: /col-span-2/.test(c.className) ? '2' : '',
    })),
  }));
  const cls = dlg.querySelector('[role="radiogroup"]');
  return JSON.stringify({
    grids,
    classification: cls ? { w: Math.round(cls.closest('.grid > div, [class*="col-span-2"]')?.getBoundingClientRect().width || cls.getBoundingClientRect().width), inSpan2: !!cls.closest('[class*="col-span-2"]') } : 'MISSING',
  }, null, 1);
})()
