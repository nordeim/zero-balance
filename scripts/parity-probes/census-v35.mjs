// Standing data-drift census (v35) — reference read-only.
// Reports the dashboard's hero numbers + the three summary rows.
(() => {
  const out = {};
  out.url = location.pathname;
  const txt = (sel) => { const el = document.querySelector(sel); return el ? el.textContent.trim() : null; };
  const all = document.body.innerText;
  const grab = (re) => { const m = all.match(re); return m ? m[1] : null; };
  out.allocation = grab(/([\d.]+)%/);
  out.balance = grab(/-?\$[\d,]+\.\d\d/);
  out.incomeRow = grab(/Total Income\s*\$([\d,.]+)\s*(\d+)\s*item/);
  out.savingsRow = grab(/Total Savings\s*-?\s*\$([\d,.]+)\s*(\d+)\s*item/);
  out.expensesRow = grab(/Total Expenses\s*-?\s*\$([\d,.]+)\s*(\d+)\s*items/);
  out.hasFocus = document.hasFocus();
  return JSON.stringify(out);
})()
