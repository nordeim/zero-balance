// probe-v10-hero2.mjs — hero figures via body text regex (established drift-check approach)
(() => {
  const txt = document.body.innerText.replace(/\s+/g, " ");
  const out = { url: location.pathname };
  const m = (re) => { const x = txt.match(re); return x ? x[0] : null; };
  out.income = m(/Total Income \$[\d,]+\.\d{2}(?: \d+ items?)?/);
  out.savings = m(/Total Savings \$[\d,]+\.\d{2}(?: \d+ items?)?/);
  out.expenses = m(/Total Expenses \$[\d,]+\.\d{2}(?: \d+ items?)?/);
  out.net = m(/Net Balance [+\-]? ?\$[\d,]+\.\d{2}/);
  out.alloc = m(/Budget Allocation \d+(?:\.\d+)?%/);
  out.heroStatus = m(/Under Budget|NET ZERO|Over Budget/);
  // legend amounts (donut)
  out.need = m(/Need \$[\d,]+\.\d{2} \d+(?:\.\d+)?%/);
  out.save = m(/Savings \$[\d,]+\.\d{2} \d+(?:\.\d+)?%/);
  out.want = m(/Want \$[\d,]+\.\d{2} \d+(?:\.\d+)?%/);
  // income statement row before Total Expenses (for item counts)
  out.itemCounts = (txt.match(/\d+ items?/g) || []).slice(0, 6);
  return JSON.stringify(out, null, 1);
})()
