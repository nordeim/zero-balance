// Session-7: dialog inner panel + classification tile markup.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const h2 = [...document.querySelectorAll('h2')].find((h) => /Add Budget Item/.test((h.textContent || '')));
  if (h2) {
    // the dialog panel: ancestor with a white bg + rounded + max-w
    let panel = h2;
    while (panel.parentElement) {
      panel = panel.parentElement;
      const c = (panel.className || '').toString();
      const st = getComputedStyle(panel);
      if (st.backgroundColor === 'rgb(255, 255, 255)' && c.includes('rounded') && st.position !== 'fixed') break;
      if (st.position === 'fixed' && !c.includes('inset-0')) break;
    }
    const r = panel.getBoundingClientRect();
    out.panel = { x: Math.round(r.x), w: Math.round(r.width), right: Math.round(r.right), maxW: cs(panel, 'maxWidth'), cls: (panel.className || '').toString().slice(0, 90) };
    out.docScrollW = document.documentElement.scrollWidth;
    // tile row: the container of the Need/Want/Savings radios
    const rg = panel.querySelector('[role="radiogroup"]') || panel;
    const row = rg.querySelector('div[class*="flex"], div[class*="grid"]') || rg;
    out.tileRowCls = (row.className || '').toString().slice(0, 80);
    out.tileRowHTML = row.outerHTML.replace(/\s+/g, ' ').slice(0, 1000);
  }
  return JSON.stringify(out, null, 1);
})()
