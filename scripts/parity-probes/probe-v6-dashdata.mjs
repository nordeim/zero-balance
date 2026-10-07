(() => {
  const t = (document.querySelector('main')?.textContent || '').replace(/\s+/g, ' ');
  const grab = (re) => { const m = t.match(re); return m ? m[0] : null; };
  return JSON.stringify({
    hero: grab(/NET ZERO GOAL.{0,160}/),
    stats: grab(/Income.{0,60}Savings.{0,60}/),
    breakdown: grab(/Net Zero Breakdown.{0,200}/),
  }, null, 1);
})()
