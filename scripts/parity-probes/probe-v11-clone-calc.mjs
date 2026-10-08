// probe-v11-clone-calc.mjs — open the calculator on the clone's expenses page, measure panel + buttons
(() => {
  const out = {};
  const h4 = [...document.querySelectorAll('h4')].find(el => /Rent|Mortgage|Groceries|Utilities|Fuel|Insurance/i.test((el.textContent || '').trim()));
  if (!h4) return 'no expense h4 found';
  let target = h4;
  let opened = false;
  for (let i = 0; i < 8 && target; i++) {
    const btns = [...target.querySelectorAll('button')].filter(b => /Calculate/i.test(b.textContent || '') && b.getBoundingClientRect().height > 0);
    if (btns.length) { btns[0].click(); opened = true; break; }
    target = target.parentElement;
  }
  if (!opened) return 'no calculate button found for ' + (h4.textContent || '').trim();
  return new Promise(resolve => setTimeout(() => {
    const panels = [...document.querySelectorAll('div')].filter(d => {
      const r = d.getBoundingClientRect(); const cs = getComputedStyle(d);
      return cs.position === 'fixed' && r.width > 400 && r.width < 900 && r.height > 150 && d.querySelectorAll('button').length > 0;
    });
    const calc = panels.find(d => /Calculator/i.test(d.textContent || ''));
    if (!calc) { resolve('no calc panel after open'); return; }
    const grab = (label) => {
      const b = [...calc.querySelectorAll('button')].filter(x => (x.textContent || '').trim() === label && x.getBoundingClientRect().height > 0)[0];
      if (!b) return null;
      const cs = getComputedStyle(b); const r = b.getBoundingClientRect();
      return { w: Math.round(r.width), h: Math.round(r.height), shadow: cs.boxShadow, bg: (cs.backgroundImage !== 'none' ? 'grad' : cs.backgroundColor), fs: cs.fontSize };
    };
    const cr = calc.getBoundingClientRect(); const ccs = getComputedStyle(calc);
    resolve(JSON.stringify({
      item: (h4.textContent || '').trim(),
      panel: { w: Math.round(cr.width), h: Math.round(cr.height), radius: ccs.borderRadius, shadow: ccs.boxShadow },
      addItem: grab('Add Item'),
      addFirst: grab('Add First Item')
    }));
  }, 1200));
})()
