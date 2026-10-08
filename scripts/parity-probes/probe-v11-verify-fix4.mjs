// probe-v11-verify-fix4.mjs — calculator Add Item + Add First Item shadows + Add button hover
(() => {
  const out = {};
  // close any open dialog first
  document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
  return new Promise(resolve => setTimeout(async () => {
    // go to expenses
    const links = [...document.querySelectorAll('a')].filter(a => (a.textContent || '').trim() === 'Expenses' && a.getBoundingClientRect().height > 0);
    if (links.length) { links[0].click(); await new Promise(r => setTimeout(r, 1500)); }
    const h4 = [...document.querySelectorAll('h4')].find(el => /Rent/.test((el.textContent || '').trim()));
    if (!h4) { resolve('no rent h4: ' + location.pathname); return; }
    let target = h4; let opened = false;
    for (let i = 0; i < 8 && target; i++) {
      const btns = [...target.querySelectorAll('button')].filter(b => /Calculate/i.test(b.textContent || '') && b.getBoundingClientRect().height > 0);
      if (btns.length) { btns[0].click(); opened = true; break; }
      target = target.parentElement;
    }
    if (!opened) { resolve('no calculate btn'); return; }
    await new Promise(r => setTimeout(r, 1200));
    const panel = [...document.querySelectorAll('div')].filter(d => {
      const r = d.getBoundingClientRect(); const cs = getComputedStyle(d);
      return cs.position === 'fixed' && r.width > 400 && r.width < 900 && r.height > 150 && d.querySelectorAll('button').length > 0;
    }).find(d => /Calculator/i.test(d.textContent || ''));
    if (!panel) { resolve('no calc panel'); return; }
    const grab = (label) => {
      const b = [...panel.querySelectorAll('button')].filter(x => (x.textContent || '').trim() === label && x.getBoundingClientRect().height > 0)[0];
      if (!b) return null;
      return { shadow: getComputedStyle(b).boxShadow };
    };
    out.calcAddItem = grab('Add Item');
    out.calcAddFirst = grab('Add First Item');
    resolve(JSON.stringify(out, null, 1));
  }, 600));
})()
