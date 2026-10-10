// Data-drift census (28th) — the reference must stay read-only throughout.
(() => {
  const txt = document.body.innerText;
  const grab = (re) => { const m = txt.match(re); return m ? m[0] : null; };
  return JSON.stringify({
    url: location.pathname,
    balance: grab(/Balance\s*\$[\d,.]+/),
    income: grab(/Income\s*\$[\d,.]+/),
    savings: grab(/Savings\s*\$[\d,.]+/),
    expenses: grab(/Expenses\s*\$[\d,.]+/),
    allocation: grab(/[\d.]+%\s*of\s*(Income|your)/) || txt.match(/allocated|allocation/i)?.[0] || null,
    heroLine: txt.split('\n').find(l => /Income|Savings|Expenses|NET ZERO|Under Budget|Over Budget/i.test(l)) || null,
  });
})()
