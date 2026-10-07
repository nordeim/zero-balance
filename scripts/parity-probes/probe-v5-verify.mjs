// Session-8 (v5): post-fix live verification — select trigger, nav hover, tabs, hero labels.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. select trigger chrome
  const trig = [...document.querySelectorAll('button')].find((b) => /^All Categories/.test(txt(b) || ''));
  if (trig) out.trigger = { color: cs(trig.querySelector('span') || trig, 'color'), border: cs(trig, 'borderColor') };

  // 2. hero white-alpha labels
  const grab = (t) => { const el = [...document.querySelectorAll('main span, main p')].find((x) => txt(x) === t && x.querySelectorAll('*').length === 0); return el ? cs(el, 'color') : null; };
  if (document.querySelector('main svg.recharts-surface') || grab('Budget Allocation')) {
    out.heroAlloc = grab('Budget Allocation');
  }

  return JSON.stringify(out, null, 1);
})()
