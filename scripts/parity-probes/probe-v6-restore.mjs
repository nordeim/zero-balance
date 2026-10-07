(() => {
  const t = (document.body.textContent || '').replace(/\s+/g, ' ');
  return JSON.stringify({
    hasCard: t.includes('Savings Account'),
    hasInst: t.includes('Commonwealth Bank'),
    summary: (t.match(/\$25,000\.00/g) || []).length,
    ratio: t.includes('Asset to Liability Ratio'),
    items1: t.includes('1 items'),
  }, null, 1);
})()
