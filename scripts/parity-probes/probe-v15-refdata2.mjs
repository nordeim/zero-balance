// probe-v15-refdata2.mjs — precise reference data state: hero net figure,
// allocation %, the three stat-card totals, and the net balance row.
(() => {
  const out = {};
  const vis = (el) => el && el.getBoundingClientRect().height > 0;
  const main = document.querySelector('main');
  if (!main) return JSON.stringify({ error: 'no main' });
  // The hero net figure is the largest text in the hero card (text-4xl/5xl)
  const big = [...main.querySelectorAll('h1,h2,p,div,span')].filter(vis).filter((el) => {
    const fs = parseFloat(getComputedStyle(el).fontSize);
    return fs >= 32 && el.children.length <= 3;
  });
  out.bigTexts = big.map((el) => ({
    text: el.textContent.trim().replace(/\s+/g, ' ').slice(0, 40),
    fs: Math.round(parseFloat(getComputedStyle(el).fontSize)),
  }));
  // allocation line
  const pct = [...main.querySelectorAll('*')].filter(vis).find((el) => {
    const t = el.textContent.trim();
    return /^\d+(\.\d+)?% of income|allocated/i.test(t) || /^Income\s*[-–]\s*/.test(t) && t.length < 80;
  });
  const pctAll = [...main.querySelectorAll('p,span,div')].filter(vis).filter((el) => {
    const t = el.textContent.replace(/\s+/g, ' ').trim();
    return /\d+(\.\d+)?%/.test(t) && t.length < 70;
  });
  out.pctLines = pctAll.slice(0, 6).map((el) => el.textContent.replace(/\s+/g, ' ').trim().slice(0, 70));
  // stat totals: find the labels then their sibling money text
  const grab = (label) => {
    const els = [...main.querySelectorAll('h2,h3,p,span,div')].filter(vis);
    const lab = els.find((el) => el.textContent.trim() === label);
    if (!lab) return null;
    let n = lab;
    for (let i = 0; i < 4 && n; i++) {
      const t = n.textContent.replace(/\s+/g, ' ');
      const m = t.match(/\$[\d,]+\.\d{2}/);
      if (m && t.trim() !== label) return { total: m[0], ctx: t.trim().slice(0, 40) };
      n = n.parentElement;
    }
    return null;
  };
  out.income = grab('Income');
  out.savings = grab('Savings');
  out.expenses = grab('Expenses');
  // Net Balance row (sign-prefixed)
  const nbEl = [...main.querySelectorAll('p,span,div')].filter(vis).find((el) => /^Net Balance$/i.test(el.textContent.trim()));
  if (nbEl) {
    out.netBalance = nbEl.parentElement.textContent.replace(/\s+/g, ' ').trim().slice(0, 40);
  }
  // income/savings/expenses item counts from their sections
  out.sectionHeads = [...main.querySelectorAll('h3')].filter(vis).map((h) => h.textContent.trim().slice(0, 30));
  return JSON.stringify(out, null, 1);
})()
