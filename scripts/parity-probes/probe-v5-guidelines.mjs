// Session-8 (v5): guidelines card LEAF text colors + breakdown drill-down real structure.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. Guidelines leaves: find the "Needs ~50%" label + description spans
  const g = [...document.querySelectorAll('main h3, main h2, main div')].filter((d) => /^Budget Guidelines$/.test(txt(d) || '') && d.querySelectorAll('*').length === 0);
  if (g.length) {
    // climb to card root
    let root = g[0];
    for (let i = 0; i < 8; i++) { const p = root.parentElement; if (!p || p.tagName === 'MAIN' || p.tagName === 'BODY') break; root = p; }
    const leaves = [...root.querySelectorAll('span, p, h4, div')].filter((d) => d.querySelectorAll('*').length === 0 && (txt(d) || '').length > 0);
    out.guidelineLeaves = leaves.slice(0, 22).map((l) => ({
      t: txt(l).slice(0, 42),
      color: cs(l, 'color'),
      size: cs(l, 'fontSize'),
      weight: cs(l, 'fontWeight'),
    }));
  }

  // 2. Breakdown structure: find the Net Zero Breakdown heading, dump its card's buttons
  const bh = [...document.querySelectorAll('main h3, main h2, main div')].filter((d) => /^Net Zero Breakdown$/.test(txt(d) || '') && d.querySelectorAll('*').length === 0);
  if (bh.length) {
    let root = bh[0];
    for (let i = 0; i < 8; i++) { const p = root.parentElement; if (!p || p.tagName === 'MAIN' || p.tagName === 'BODY') break; root = p; }
    out.breakdownCard = {
      headingSize: cs(bh[0], 'fontSize'),
      headingWeight: cs(bh[0], 'fontWeight'),
      headingColor: cs(bh[0], 'color'),
    };
    const btns = [...root.querySelectorAll('button')];
    out.breakdownButtons = btns.slice(0, 10).map((b) => ({
      t: txt(b).slice(0, 46),
      tag: b.tagName,
      cls: (b.className || '').toString().replace(/\s+/g, ' ').slice(0, 110),
    }));
    // rows that look like sections (div with font-medium etc.)
    const secs = [...root.querySelectorAll('div')].filter((d) => {
      const t = txt(d) || '';
      return /^(Income|Savings|Expenses)/.test(t) && t.includes('$') && d.querySelectorAll('button').length === 0 && t.length < 70;
    });
    out.sections = secs.slice(0, 5).map((s) => ({
      t: txt(s).slice(0, 60),
      cls: (s.className || '').toString().replace(/\s+/g, ' ').slice(0, 110),
      color: cs(s, 'color'),
      weight: cs(s, 'fontWeight'),
    }));
  }

  return JSON.stringify(out, null, 1);
})()
