// probe-v14-data-drift.mjs — dashboard data state on both sites (drift check).
// Reads: allocation %, income/savings/expenses visible figures, net balance,
// stat-card count, breakdown section headers, guideline rows.
(() => {
  const out = {};
  const txt = (sel) => { const el = document.querySelector(sel); return el ? el.textContent.trim() : null; };
  // hero
  const hero = document.querySelector('main h1')?.closest('div');
  if (hero) out.heroText = hero.textContent.slice(0, 200);
  // stat cards
  const statCards = [...document.querySelectorAll('main [class*="rounded"]')].filter(el => /\$/.test(el.textContent) && el.querySelectorAll('*').length < 30).slice(0, 8);
  out.statCardTexts = statCards.map(c => c.textContent.trim().replace(/\s+/g, ' ').slice(0, 80));
  // allocation percentage
  const pct = document.body.textContent.match(/(\d+(?:\.\d+)?)\s*%/);
  out.firstPct = pct ? pct[1] : null;
  // breakdown sections (Income/Savings/Expenses rows)
  const body = document.body.textContent.replace(/\s+/g, ' ');
  for (const key of ['Income', 'Savings', 'Expenses', 'Net Balance', 'NET ZERO']) {
    const i = body.indexOf(key);
    if (i >= 0) out['ctx_' + key.replace(/\s/g, '_')] = body.slice(Math.max(0, i - 10), i + 60).trim();
  }
  return JSON.stringify(out);
})()
