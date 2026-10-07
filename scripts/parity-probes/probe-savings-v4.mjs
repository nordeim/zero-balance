// Session-7: view header + add button gradient (savings).
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);
  const main = document.querySelector('main');
  const addBtn = main ? [...main.querySelectorAll('button')].find((b) => /Add (Savings|Income|Expense)/.test(txt(b) || '')) : null;
  if (addBtn) out.addBtn = { text: txt(addBtn), bg: cs(addBtn, 'backgroundImage').slice(0, 100), color: cs(addBtn, 'color') };
  const h1 = main ? main.querySelector('h1') : null;
  if (h1) out.h1 = { text: txt(h1), sub: h1.nextElementSibling ? txt(h1.nextElementSibling).slice(0, 40) : null };
  return JSON.stringify(out, null, 1);
})()
