// Session-7: donut legend card + sidebar brand icon, precisely scoped.
(() => {
  const out = {};
  const cs = (el, p) => (el ? getComputedStyle(el)[p] : null);
  const txt = (el) => (el ? el.textContent.replace(/\s+/g, ' ').trim() : null);

  // 1. Donut legend: the piggy-bank svg lives in the legend; scope = closest common card with bg
  const allSvgs = [...document.querySelectorAll('svg')];
  const piggy = allSvgs.find((s) => (s.getAttribute('class') || '').includes('piggy-bank'));
  if (piggy) {
    // climb until we find a container with 2+ svgs AND $ text AND a white/tinted bg
    let node = piggy.parentElement;
    const trail = [];
    for (let i = 0; i < 8 && node && node !== document.body; i++) {
      trail.push({ tag: node.tagName, cls: (node.className || '').toString().slice(0, 60), svgs: node.querySelectorAll('svg').length, hasDollar: /\$/.test(node.textContent || ''), bg: cs(node, 'backgroundColor') });
      node = node.parentElement;
    }
    out.piggyTrail = trail;
  }

  // 2. Sidebar brand icon (first svg in the sidebar)
  const rail = [...document.querySelectorAll('aside, div')].find((d) => (d.className || '').toString().includes('w-64'));
  if (rail) {
    const brandSvg = rail.querySelector('svg');
    out.brandIcon = {
      cls: brandSvg ? (brandSvg.getAttribute('class') || '') : null,
      color: brandSvg ? cs(brandSvg, 'color') : null,
      size: brandSvg ? cs(brandSvg, 'width') : null,
    };
    const brandText = rail.querySelector('h1, h2, span, div');
    out.brandText = brandText ? txt(brandText) : null;
  }

  // 3. Sidebar bottom: avatar + user info
  if (rail) {
    const av = [...rail.querySelectorAll('div,span')].filter((x) => (x.className || '').includes('rounded-full')).pop();
    out.railAvatar = av ? { text: txt(av), bg: cs(av, 'backgroundColor'), size: cs(av, 'width') } : null;
  }

  // 4. Donut legend rows — via the recharts container's sibling card
  const rechartsContainer = document.querySelector('svg.recharts-surface');
  if (rechartsContainer) {
    // the donut card = closest div with rounded + border; legend = the rows with $ inside that card
    let card = rechartsContainer.closest('div');
    while (card && !(card.className || '').toString().match(/rounded-2xl|border/)) card = card.parentElement;
    if (card) {
      out.donutCard = { cls: card.className.toString().slice(0, 80), bg: cs(card, 'backgroundColor') };
      // legend rows: rows containing an svg + a $ amount
      const rows = [...card.querySelectorAll('div')].filter((d) => {
        const t = txt(d) || '';
        return /\$/.test(t) && d.querySelector('svg') && (d.className || '').includes('flex') && (d.textContent || '').length < 60;
      });
      out.legendRows = rows.map((r) => {
        const svgs = r.querySelectorAll('svg');
        const spans = [...r.querySelectorAll('span, p, div')].filter((x) => x.children.length === 0);
        return {
          iconClass: svgs[0] ? (svgs[0].getAttribute('class') || '').replace(/^.*?lucide/, 'lucide').slice(0, 40) : null,
          iconColor: svgs[0] ? cs(svgs[0], 'color') : null,
          text: txt(r).slice(0, 50),
          lastSpanColor: spans.length ? cs(spans[spans.length - 1], 'color') : null,
        };
      });
    }
  }

  return JSON.stringify(out, null, 1);
})()
