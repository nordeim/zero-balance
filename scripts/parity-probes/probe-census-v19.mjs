// v19 session: items-view census on the reference — the second half of the
// drift check (per-view item counts + totals).
(() => {
  const out = {};
  for (const [path, key] of [['/income', 'income'], ['/savings', 'savings'], ['/expenses', 'expenses']]) {
    const r = window.__probe_result;
    void r;
  }
  // read the page's own summary: the items views show "N items · $X.00"
  const texts = [...document.querySelectorAll('h2,h3,p,span,div')].map((el) => (el.textContent || '').trim());
  const counts = texts.filter((t) => /^\d+ items? · \$[\d,.]+$/.test(t)).slice(0, 6);
  out.counts = counts;
  return JSON.stringify(out, null, 1);
})()
