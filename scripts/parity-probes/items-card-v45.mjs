// v45: the ITEMS-VIEW CARD census at 1280 — the v42 mid-viewport census
// pinned the five-route rhythm at 640 (header→filter gapRowToFirst 32) but
// never the CARD GRID geometry at 1280 (the 3-col grid pitch, the card
// chrome, the card's hover shadow state). The card carries an INLINE
// boxShadow at rest (rgba(0,0,0,0.04) 0px 2px 8px 0px on the reference —
// 4-value with the explicit 0px spread) AND a hover:shadow-lg class —
// an inline style beats the class, so the card hover is expected INERT on
// BOTH sites (the v29 category-row family) — verified via the tag+hover
// steps in the driver (synthetic dispatchEvent cannot engage :hover).
// bash scripts/parity-probes/run-probe.sh <session> scripts/parity-probes/items-card-v45.mjs
(async () => {
  // The items grid: located by its grid-cols-3 class (both sites run the
  // same utility family — 'grid gap-4 md:grid-cols-2 lg:grid-cols-3').
  const grid = [...document.querySelectorAll('div')].find((d) => {
    if (!d.className || typeof d.className !== 'string') return false;
    return d.className.includes('grid-cols-3') && d.children.length >= 1;
  });
  if (!grid) return JSON.stringify({ found: false, hint: 'no grid' });

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
      cursor: cs.cursor,
      transition: cs.transitionProperty,
      transitionDur: cs.transitionDuration,
    };
  };
  out.card = readCard(card);

  // The card's inner first rows: the dot + title cluster.
  const dot = [...card.querySelectorAll('div,span')].find((d) => {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    return !d.children.length && r.width > 0 && r.width <= 12 && cs.backgroundColor !== 'rgba(0, 0, 0, 0)';
  });
  const titleEl = [...card.querySelectorAll('h1,h2,h3,h4')][0] || null;
  if (titleEl) {
    out.titleRow = {
      gap: getComputedStyle(titleEl.parentElement).gap,
      dotW: dot ? Math.round(dot.getBoundingClientRect().width) : null,
      dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
      titleFont: getComputedStyle(titleEl).fontSize,
      titleWeight: getComputedStyle(titleEl).fontWeight,
    };
  }

  // Tag the first card for the driver's REAL hover step.
  card.setAttribute('data-v45-card', 'first');

  // The hover-revealed action row (expense cards): absolute top-3 right-3
  // opacity-0 → group-hover:opacity-100. Read its geometry at rest.
  const actionRow = [...card.querySelectorAll('div')].find((d) => {
    const cs = getComputedStyle(d);
    return cs.position === 'absolute' && cs.opacity === '0' && d.children.length > 0;
  });
  out.actionRow = actionRow
    ? {
        top: getComputedStyle(actionRow).top,
        right: getComputedStyle(actionRow).right,
        gap: getComputedStyle(actionRow).gap,
        btnH: Math.round(actionRow.querySelector('button').getBoundingClientRect().height),
        btnPadX: getComputedStyle(actionRow.querySelector('button')).paddingLeft,
        fontSize: getComputedStyle(actionRow.querySelector('button')).fontSize,
      }
    : null;

  // The kebab (v36 focus-reveal): a textless single-svg button.
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

  out.sw = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})();
