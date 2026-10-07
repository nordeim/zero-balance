// Session-7 follow-up: hero status badge, donut legend, sidebar structure.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. Hero status badge — the small chip showing Under Budget / NET ZERO / Over Budget
  const badge = [...document.querySelectorAll('span,div,p')].find((x) => {
    const t = txt(x);
    return x.children.length === 0 && /^(Under Budget|NET ZERO|Over Budget|✓ NET ZERO)/.test(t || '');
  });
  out.heroBadge = badge ? { text: txt(badge), color: cs(badge, 'color'), bg: cs(badge, 'backgroundColor'), border: cs(badge, 'borderColor'), cls: badge.className.toString().slice(0, 120) } : null;

  // 2. Donut legend — find the card containing piggy-bank-ish svg + "$" amounts near "Savings"/"Want"/"Need"
  const allSvgs = [...document.querySelectorAll('svg.lucide, svg[class*="lucide"]')];
  const piggy = allSvgs.find((s) => (s.getAttribute('class') || '').includes('piggy-bank'));
  if (piggy) {
    let card = piggy.closest('div');
    for (let i = 0; i < 4 && card && card.parentElement; i++) {
      if ((card.textContent || '').includes('$') && card.querySelectorAll('svg').length >= 2) break;
      card = card.parentElement;
    }
    out.legendCard = { bg: cs(card, 'backgroundColor'), border: cs(card, 'borderColor'), radius: cs(card, 'borderRadius'), padding: cs(card, 'padding') };
    out.legendRows = [...card.children].map((ch) => ({ text: txt(ch).slice(0, 44) })).slice(0, 5);
    // legend icon names in order
    out.legendIcons = [...card.querySelectorAll('svg')].map((s) => {
      const c = s.getAttribute('class') || '';
      const m = c.match(/lucide-([a-z-]+)/);
      return m ? m[1] : (c.split(' ').find((x) => x.startsWith('lucide-')) || c.slice(0, 30));
    }).slice(0, 6);
  }

  // 3. Sidebar structure: element types + nav presence
  const rail = [...document.querySelectorAll('div')].find((d) => (d.className || '').toString().includes('w-64') || /width.*256/.test(cs(d, 'width') || ''));
  out.sidebar = {
    usesNavElement: !!document.querySelector('nav'),
    railFound: !!rail,
    railW: rail ? cs(rail, 'width') : null,
  };

  // 4. Donut center text (if any)
  const surface = document.querySelector('svg.recharts-surface');
  if (surface) {
    const centerTexts = [...surface.querySelectorAll('text')].filter((t) => !/%/.test(txt(t) || ''));
    out.donutCenter = centerTexts.map((t) => txt(t)).slice(0, 3);
  }

  // 5. Breakdown card footer (border-t row) — try card-level
  const bdH = [...document.querySelectorAll('h3')].find((h) => /Net Zero Breakdown/i.test(txt(h) || ''));
  if (bdH) {
    const card = bdH.closest('div[class*="rounded"]');
    const footer = [...card.querySelectorAll('div')].filter((d) => (d.className || '').includes('border-t')).pop();
    out.bdFooter = footer ? txt(footer).slice(0, 70) : null;
    // sections list
    out.bdSections = [...card.querySelectorAll('button')].slice(0, 4).map((b) => txt(b).slice(0, 40));
  }

  // 6. Stat card count row (first stat) — "N items" + separator + trend
  const ti = [...document.querySelectorAll('h3')].find((h) => txt(h) === 'Total Income');
  if (ti) {
    const card = ti.closest('div[class*="rounded"]') || ti.parentElement.parentElement;
    const rows = [...card.querySelectorAll('div')].filter((d) => /item/.test(txt(d) || '') && d.children.length >= 2);
    const row = rows[0];
    if (row) {
      out.statCountRow = { text: txt(row).slice(0, 50), cls: row.className.toString().slice(0, 80) };
      const sep = row.querySelector('div[class*="h-px"], hr');
      out.statSep = sep ? { h: cs(sep, 'height'), bg: cs(sep, 'backgroundColor') } : null;
    }
  }

  return JSON.stringify(out, null, 1);
})()
