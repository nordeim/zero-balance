// Session-8 (v5): dashboard fresh angles — guidelines card leaf audit,
// breakdown drill-down expanded states, page title, quick actions.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  out.title = document.title;

  // 1. Budget Guidelines card — find the card containing "Budget Guidelines"
  const cards = [...document.querySelectorAll('main div')].filter((d) => {
    const h = d.querySelector('h3, h2, div.font-semibold, p.font-semibold');
    return h && /Budget Guidelines/i.test(txt(h) || '');
  });
  const gcard = cards[cards.length - 1]; // innermost wrapper
  if (gcard) {
    // walk up to the card root (has rounded + bg)
    let root = gcard;
    for (let i = 0; i < 6; i++) {
      const p = root.parentElement;
      if (!p || p.tagName === 'MAIN') break;
      const c = cs(p, 'borderRadius');
      if (c && c !== '0px' && (p.className || '').toString().includes('rounded')) { root = p; }
    }
    out.guidelines = {
      cardBg: cs(root, 'backgroundColor'),
      cardBorder: cs(root, 'borderColor') + ' ' + cs(root, 'borderWidth'),
      radius: cs(root, 'borderRadius'),
      padding: cs(root, 'padding'),
    };
    // the 50/30/20 rows: each has a label + value + bar
    const rows = [...root.querySelectorAll('div')].filter((d) => /^(Needs|Wants|Savings)\b/.test((txt(d) || '')) && d.querySelectorAll('*').length < 12 && d.textContent.length < 80);
    out.guidelines.rows = rows.slice(0, 6).map((r) => {
      const c = (r.className || '').toString();
      return {
        text: txt(r).slice(0, 60),
        bg: cs(r, 'backgroundColor'),
        border: cs(r, 'borderColor'),
        color: cs(r, 'color'),
        cls: c.slice(0, 120),
      };
    });
  }

  // 2. Breakdown drill-down: expand first section, then first category
  const bd = [...document.querySelectorAll('main button')].filter((b) => (txt(b) || '').match(/^(Income|Savings|Expenses)\b/));
  out.breakdown = { sections: bd.map((b) => txt(b).slice(0, 50)) };
  if (bd[0]) {
    bd[0].click();
    const lvl2 = [...document.querySelectorAll('main button')].filter((b) => {
      const t = txt(b) || '';
      return b !== bd[0] && t.length > 0 && t.length < 60 && b.querySelector('svg') && !/add|calculate|edit/i.test(t);
    });
    out.breakdown.afterExpand = {
      buttons: lvl2.slice(0, 8).map((b) => txt(b).slice(0, 50)),
    };
    // click the first level-2 (category) button
    const cat = lvl2.find((b) => (txt(b) || '').includes('$'));
    if (cat) {
      cat.click();
      // level-3 rows: spans/divs with amounts
      const rows3 = [...document.querySelectorAll('main span, main div')].filter((d) => {
        const t = txt(d) || '';
        return /^\$|- \$/.test(t) && t.length < 50 && d.querySelectorAll('span,div').length === 0;
      });
      out.breakdown.level3 = rows3.slice(0, 10).map((r) => ({
        text: txt(r),
        color: cs(r, 'color'),
        fontSize: cs(r, 'fontSize'),
        weight: cs(r, 'fontWeight'),
      }));
    }
  }

  // 3. Quick action buttons (dashboard bottom card)
  const qa = [...document.querySelectorAll('main button')].filter((b) => /^(Add Income|Add Savings|Add Expense|Add Item)/i.test(txt(b) || ''));
  out.quickActions = qa.slice(0, 4).map((b) => {
    const r = b.getBoundingClientRect();
    return {
      text: txt(b),
      bg: cs(b, 'backgroundImage').slice(0, 60) || cs(b, 'backgroundColor'),
      h: Math.round(r.height),
      radius: cs(b, 'borderRadius'),
      fontSize: cs(b, 'fontSize'),
    };
  });

  return JSON.stringify(out, null, 1);
})()
