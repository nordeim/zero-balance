// v46: the NET-WORTH CARD census at 1280 — the session-101 queue's first
// candidate. The v41 summary-card census pinned the hero card + the
// mobile card; the ASSET/LIABILITY card grid at 1280 (the 2-col pitch,
// the card chrome, the card's hover state, the kebab reveal) was never
// measured. The card carries an INLINE boxShadow at rest (rgba(0,0,0,0.04)
// 0px 2px 8px) AND a hover:shadow-lg class — the v29 inline-beats-class
// family, the same as the v45 items-card — so the hover is expected INERT
// on BOTH sites (verified via the driver's REAL hover step). The kebab
// (opacity-0 → group-hover:opacity-100) is tagged for the driver's click
// step (the menu → Delete → the confirm-bar census, confirm-pill-v46.mjs).
// bash scripts/parity-probes/run-probe.sh <session> scripts/parity-probes/nw-card-v46.mjs
(async () => {
  // The asset-card grid: md:grid-cols-2 lg:grid-cols-3 at 1280 (3 cols —
  // net-worth-view.tsx:459 on the clone; the reference's own asset grid
  // carries the identical utility family). NOT the summary card's inner
  // sm:grid-cols-2 stat-block grid (the v4 G4 design).
  const grid = [...document.querySelectorAll('div')].find((d) => {
    if (!d.className || typeof d.className !== 'string') return false;
    return d.className.includes('lg:grid-cols-3') && d.children.length >= 1 && getComputedStyle(d).display === 'grid';
  });
  if (!grid) return JSON.stringify({ found: false, hint: 'no lg:grid-cols-3 card grid' });

  const gr = grid.getBoundingClientRect();
  const gcs = getComputedStyle(grid);
  const out = {
    vw: innerWidth,
    grid: {
      w: Math.round(gr.width),
      cols: gcs.gridTemplateColumns,
      gap: gcs.gap,
      childCount: grid.children.length,
      y: Math.round(gr.top),
    },
  };

  // The first card census (rest state).
  const card = grid.children[0];
  const readCard = (c) => {
    const r = c.getBoundingClientRect();
    const cs = getComputedStyle(c);
    return {
      w: Math.round(r.width),
      h: Math.round(r.height),
      pad: cs.padding,
      radius: cs.borderRadius,
      border: `${cs.borderTopWidth} ${cs.borderTopStyle} ${cs.borderTopColor}`,
      boxShadow: cs.boxShadow,
      bg: cs.backgroundColor,
      transition: cs.transitionProperty,
      transitionDur: cs.transitionDuration,
    };
  };
  out.card = readCard(card);

  // The dot + title cluster (the title row).
  const titleEl = [...card.querySelectorAll('h1,h2,h3,h4')][0] || null;
  const dot = [...card.querySelectorAll('div')].find((d) => {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return !d.children.length && r.width > 0 && r.width <= 12 && cs.backgroundColor !== 'rgba(0, 0, 0, 0)';
  });
  if (titleEl) {
    const tcs = getComputedStyle(titleEl);
    out.titleRow = {
      gap: getComputedStyle(titleEl.parentElement).gap,
      dotW: dot ? Math.round(dot.getBoundingClientRect().width) : null,
      dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
      titleFont: tcs.fontSize,
      titleWeight: tcs.fontWeight,
      titleColor: tcs.color,
    };
  }

  // The type badge (the gray pill under the title: rounded-md bg-[#f3f4f6]).
  const badge = [...card.querySelectorAll('span')].find((s) => {
    const cs = getComputedStyle(s);
    return cs.backgroundColor === 'rgb(243, 244, 246)' || cs.backgroundColor === 'rgb(243,244,246)';
  });
  out.badge = badge
    ? {
        pad: getComputedStyle(badge).padding,
        radius: getComputedStyle(badge).borderRadius,
        fontSize: getComputedStyle(badge).fontSize,
        weight: getComputedStyle(badge).fontWeight,
        color: getComputedStyle(badge).color,
      }
    : null;

  // The value figure (text-2xl font-bold, the class color).
  const value = [...card.querySelectorAll('p')].find((p) => {
    const cs = getComputedStyle(p);
    return cs.fontSize === '24px' && cs.fontWeight === '700';
  });
  out.value = value
    ? { font: getComputedStyle(value).fontSize, weight: getComputedStyle(value).fontWeight, color: getComputedStyle(value).color, mb: getComputedStyle(value).marginBottom }
    : null;

  // The fact rows (space-y-2 text-xs gray: the icon rows under the figure).
  const facts = [...card.querySelectorAll('div')].find((d) => {
    if (!d.className || typeof d.className !== 'string') return false;
    return d.className.includes('space-y-2');
  });
  out.facts = facts
    ? { font: getComputedStyle(facts).fontSize, color: getComputedStyle(facts).color, gap: getComputedStyle(facts).rowGap }
    : null;

  // The kebab (opacity-0 at rest): a textless single-svg button — tagged
  // for the driver's click step (menu → Delete → the confirm bar).
  const kebab = [...card.querySelectorAll('button')].find((b) => {
    const t = (b.textContent || '').trim();
    return !t && b.querySelectorAll('svg').length === 1;
  });
  out.kebab = kebab
    ? {
        w: Math.round(kebab.getBoundingClientRect().width),
        h: Math.round(kebab.getBoundingClientRect().height),
        opacity: getComputedStyle(kebab).opacity,
      }
    : null;
  if (kebab) {
    kebab.setAttribute('data-v46-kebab', 'first');
    card.setAttribute('data-v46-card', 'first');
  }

  out.sw = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})();
