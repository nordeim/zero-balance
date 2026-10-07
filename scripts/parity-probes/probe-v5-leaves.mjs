// Session-8 (v5): leaf-level audit — donut legend rows, guidelines rows, quick-action card chrome.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. Donut legend rows: "Savings $X Y%" style rows with p-3 rounded-lg
  const legendRows = [...document.querySelectorAll('main div')].filter((d) => {
    const c = (d.className || '').toString();
    return /items-center justify-between/.test(c) && /p-3/.test(c) && (txt(d) || '').includes('%') && (txt(d) || '').length < 40 && d.querySelectorAll('div').length === 0;
  });
  out.legend = legendRows.slice(0, 3).map((r) => {
    const spans = [...r.querySelectorAll('span')].map((s) => ({ t: txt(s), color: cs(s, 'color'), size: cs(s, 'fontSize'), weight: cs(s, 'fontWeight') }));
    return { rowColor: cs(r, 'color'), spans };
  });

  // 2. Guidelines rows: p-4 rounded-lg tinted
  const grows = [...document.querySelectorAll('main div')].filter((d) => {
    const c = (d.className || '').toString();
    return /rounded-lg/.test(c) && /p-4/.test(c) && /^(Needs|Wants|Savings)~/.test(txt(d) || '') && d.querySelectorAll('div').length > 0 && d.querySelectorAll('div').length < 8;
  });
  out.guidelines = grows.slice(0, 3).map((r) => {
    const leaves = [...r.querySelectorAll('span, p, h4')].filter((d) => d.querySelectorAll('*').length === 0);
    return leaves.slice(0, 6).map((l) => ({ t: txt(l).slice(0, 46), color: cs(l, 'color'), size: cs(l, 'fontSize'), weight: cs(l, 'fontWeight') }));
  });

  // 3. Quick-action cards: computed chrome
  const qa = [...document.querySelectorAll('main button')].filter((b) => /^(Add Income|Add Savings|Add Expense)$/.test(txt(b) || ''));
  out.quickActions = qa.slice(0, 3).map((b) => ({
    t: txt(b),
    border: cs(b, 'borderWidth') + ' ' + cs(b, 'borderStyle') + ' ' + cs(b, 'borderColor'),
    bg: cs(b, 'backgroundColor'),
    shadow: cs(b, 'boxShadow').slice(0, 60),
    radius: cs(b, 'borderRadius'),
    padding: cs(b, 'padding'),
  }));

  // 4. Hero white-alpha texts (computed)
  const heroLeaves = [...document.querySelectorAll('main span, main div')].filter((d) => {
    const t = txt(d) || '';
    return d.querySelectorAll('*').length === 0 && /^(Income = Savings \+ Expenses|Budget Allocation|Balance)$/.test(t);
  });
  out.heroLabels = heroLeaves.slice(0, 4).map((l) => ({ t: txt(l), color: cs(l, 'color'), size: cs(l, 'fontSize') }));

  return JSON.stringify(out, null, 1);
})()
