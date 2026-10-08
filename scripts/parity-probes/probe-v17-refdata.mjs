// Data drift check: reference figures on the dashboard (v17 re-verification)
(async () => {
  const hero = document.querySelector("main") || document.body;
  const text = hero.innerText;
  const grab = (re) => { const m = text.match(re); return m ? m[1] : null; };
  const out = {
    url: location.pathname,
    allocation: grab(/Budget Allocation\s*([\d.]+%)/i) || grab(/([\d.]+%)/),
    balance: grab(/Balance\s*(-?\$[\d,.]+)/i),
    netBalance: grab(/Net Balance\s*(-?\$[\d,.]+)/i),
    incomeRow: grab(/Income\s*\$?([\d,.]+)/i),
    savingsRow: grab(/Savings\s*\$?([\d,.]+)/i),
    expensesRow: grab(/Expenses\s*\$?([\d,.]+)/i),
    statusBadge: grab(/\u2713\s*(NET ZERO|Under Budget|Over Budget)/) || null,
  };
  return JSON.stringify(out);
})()
