// Session-8 (v5): calculator Add Item button gradient + line-item dialog footer buttons.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const h = [...document.querySelectorAll('h2')].find((x) => /Calculator/.test(x.textContent || ''));
  if (!h) return JSON.stringify({ error: 'no calc' });
  let panel = h;
  for (let i = 0; i < 10; i++) { const p = panel.parentElement; if (!p || p === document.body) break; if ((panel.className || '').toString().includes('fixed')) break; panel = p; }
  const addBtn = [...panel.querySelectorAll('button')].find((b) => txt(b) === 'Add Item');
  if (addBtn) out.addItemGradient = (cs(addBtn, 'backgroundImage') || 'none').slice(0, 100);
  return JSON.stringify(out, null, 1);
})()
