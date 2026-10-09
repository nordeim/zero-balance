// v29: reference data census (23rd drift check) — the standing five-metric set
// (allocation %, Balance, income/savings/expenses totals + counts).
(() => {
  const t = document.body.innerText;
  const grab = (re) => { const m = t.match(re); return m ? m[1] : null; };
  const pct = grab(/(\d+(?:\.\d+)?)%\s*allocated/i) || grab(/(\d+(?:\.\d+)?)%/);
  const balance = grab(/Balance\s*\$?([\d,]+\.\d{2})/) || grab(/Net Zero Balance\s*\$?([\d,]+\.\d{2})/);
  const income = grab(/Income\s*\$?([\d,]+\.\d{2})/);
  const savings = grab(/Savings\s*\$?([\d,]+\.\d{2})/);
  const expenses = grab(/Expenses\s*\$?([\d,]+\.\d{2})/);
  // view counts: click-free — read the quick-action card descriptions
  const incomeDesc = grab(/Income\s*[\d.]+[^$]*?\$?[\d,]+\.\d{2}\s*\n?([^$]{0,40})/);
  return JSON.stringify({
    url: location.pathname,
    pct,
    balance,
    income, savings, expenses,
    hasNetZero: /NET ZERO|Net Zero/i.test(t),
    heroSnippet: (document.querySelector('h1') || {}).textContent,
  });
})()
