// Session-7 (v4) dashboard probe — structural + computed-style evidence.
// Run via: agent-browser eval "$(cat scripts/parity-probes/probe-dashboard-v4.mjs)"
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. Hero card: title, computed amount, status badge, allocation bar
  const h3s = [...document.querySelectorAll('h3')];
  const heroH = h3s.find((h) => /NET ZERO GOAL/i.test(txt(h) || ''));
  if (heroH) {
    const card = heroH.closest('div[class*="rounded"]');
    out.hero = {
      title: txt(heroH),
      cardBg: cs(card, 'backgroundImage').slice(0, 100) || cs(card, 'backgroundColor'),
      texts: [...card.querySelectorAll('h1,span,p,div')].slice(0, 4).map(txt).filter(Boolean).slice(0, 3),
    };
    const status = [...card.querySelectorAll('*')].find((x) => /NET ZERO|Over Budget|Under Budget/.test(txt(x) || '') && x.children.length === 0);
    out.heroStatus = status ? { text: txt(status), color: cs(status, 'color'), bg: cs(status, 'backgroundColor') } : null;
    const fill = card.querySelector('[class*="bg-"][style*="width"], div[style*="width:"]');
    out.heroFill = fill ? { style: (fill.getAttribute('style') || '').slice(0, 80), bg: cs(fill, 'backgroundImage').slice(0, 90) || cs(fill, 'backgroundColor') } : null;
  }

  // 2. Stat cards: heading, amount format, count row
  out.stats = h3s.filter((h) => /Total (Income|Savings|Expenses)/i.test(txt(h) || '')).map((h) => {
    const card = h.closest('div[class*="rounded"]') || h.parentElement;
    const amount = [...card.querySelectorAll('*')].find((x) => /^\$[\d,.]+$/.test(txt(x) || '') && x.children.length === 0);
    return {
      head: txt(h),
      amount: amount ? { text: txt(amount), size: cs(amount, 'fontSize'), weight: cs(amount, 'fontWeight'), color: cs(amount, 'color') } : null,
    };
  });

  // 3. Net balance row (breakdown footer or hero)
  const nb = [...document.querySelectorAll('*')].find((x) => /Net Balance/i.test(txt(x) || '') && x.children.length <= 2 && (x.textContent || '').includes('$'));
  out.netBalance = nb ? txt(nb).slice(0, 60) : null;

  // 4. Donut: svg sectors + legend order + icons + center label
  const donutSvg = document.querySelector('svg.recharts-surface, svg[class*="recharts"]');
  if (donutSvg) {
    const sectors = [...donutSvg.querySelectorAll('path.recharts-pie-sector path, .recharts-pie-sector path')];
    out.donutSectors = sectors.map((s) => cs(s, 'fill'));
    const labels = [...donutSvg.querySelectorAll('.recharts-pie-label-text, text')].map((t) => txt(t)).filter(Boolean).slice(0, 6);
    out.donutLabels = labels;
  }
  const legend = [...document.querySelectorAll('div')].find((d) => (d.className || '').toString().includes('space-y') && /piggy|Savings/.test(d.textContent || '') && d.querySelectorAll('svg').length >= 2);
  if (legend) {
    out.legend = [...legend.querySelectorAll(':scope > div')].map((row) => {
      const svg = row.querySelector('svg');
      const amt = [...row.querySelectorAll('span,div,p')].find((x) => /^\$/.test(txt(x) || ''));
      return { icon: svg ? cs(svg, 'color') : null, label: txt(row).slice(0, 40), amt: amt ? txt(amt) : null, pct: (row.textContent.match(/\d+%/) || [null])[0] };
    });
    out.legendBg = cs(legend, 'backgroundColor');
  }

  // 5. Guidelines rows
  const gl = [...document.querySelectorAll('h3')].find((h) => /Budget Guidelines/i.test(txt(h) || ''));
  if (gl) {
    const card = gl.closest('div[class*="rounded"]');
    out.guidelines = [...card.querySelectorAll('div[class*="justify-between"], div.flex')].filter((d) => /\$\d/.test(txt(d) || '')).slice(0, 3).map((d) => {
      const row = d.closest('div[class*="bg-"]') || d;
      return { bg: cs(row, 'backgroundColor'), border: cs(row, 'borderColor'), text: txt(row).slice(0, 50) };
    });
  }

  // 6. Quick actions (first)
  const qa = [...document.querySelectorAll('button')].find((b) => /Add Income/.test(txt(b) || ''));
  if (qa) out.quickAction = { text: txt(qa).slice(0, 30), cls: qa.className.slice(0, 120), border: cs(qa, 'borderColor') };

  // 7. Breakdown: first section + footer
  const bdH = h3s.find((h) => /Net Zero Breakdown/i.test(txt(h) || ''));
  if (bdH) {
    const card = bdH.closest('div[class*="rounded"]');
    const firstBtn = card.querySelector('button');
    out.breakdown = {
      firstBtnText: txt(firstBtn).slice(0, 60),
      firstBtnCls: firstBtn.className.slice(0, 100),
      footer: txt(card.querySelector('div[class*="border-t"], div[class*="pt-4"]')).slice(0, 60) || null,
    };
  }

  // 8. Nav links + active state
  out.nav = [...document.querySelectorAll('nav a')].map((a) => ({
    text: txt(a),
    bg: (cs(a, 'backgroundImage') !== 'none' ? cs(a, 'backgroundImage').slice(0, 60) : cs(a, 'backgroundColor')),
    color: cs(a, 'color'),
  }));

  // 9. Avatar
  const av = [...document.querySelectorAll('div,span')].find((x) => /^D[A-Z]?$|^Demo|DU$/.test(txt(x) || '') && (x.className || '').includes('rounded-full'));
  out.avatar = av ? { text: txt(av), bg: cs(av, 'backgroundColor'), color: cs(av, 'color'), size: cs(av, 'width') } : null;

  // 10. Add Item button (header)
  const addBtn = [...document.querySelectorAll('button')].find((b) => txt(b) === 'Add Item');
  out.addBtn = addBtn ? { cls: addBtn.className.slice(0, 140), bg: cs(addBtn, 'backgroundImage').slice(0, 100) } : null;

  return JSON.stringify(out, null, 1);
})()
