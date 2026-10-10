// probe-data-v33.mjs — the 27th data-drift census (read-only)
(async () => {
  const txt = (sel) => document.querySelector(sel)?.textContent?.trim() ?? null;
  const alloc = document.querySelector('[data-testid="allocation-donut"], svg.recharts-surface') ? 'present' : 'absent';
  // The dashboard's key figures (the standing census fields)
  const out = {
    allocText: document.body.innerText.match(/([0-9.]+)%\s*allocated|Allocated\s*([0-9.]+)%/i)?.[0] ?? null,
    balance: document.body.innerText.match(/Balance[^$]*\$([0-9,.]+)/i)?.[1] ?? null,
    income: null, savings: null, expenses: null,
  };
  // income/savings/expenses from the breakdown rows
  const rows = [...document.querySelectorAll('button, [role="button"]')].filter(b => b.className?.includes?.('justify-between'));
  out.rowCount = rows.length;
  const bd = document.body.innerText;
  const grab = (label) => {
    const m = bd.match(new RegExp(label + '[^\\n]*?\\$([0-9,.]+)', 'i'));
    return m?.[1] ?? null;
  };
  out.income = grab('Income'); out.savings = grab('Savings'); out.expenses = grab('Expenses');
  return JSON.stringify(out);
})()
