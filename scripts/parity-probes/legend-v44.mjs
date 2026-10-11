// v44: the donut LEGEND census — the v14 session pinned the legend's
// content contract (order/icons/amounts/percents/tinted bg) but never its
// GEOMETRY (row h/pad/radius/fonts/gap), its INTERACTION states (hover),
// or its MOBILE geometry (390). Runs at whatever viewport the driver set.
// Structure-agnostic: the rows are located via their exact-text label spans
// ("Need"/"Want"/"Savings" — the reference's textContent concatenates
// WITHOUT spaces, so text-matching the ROW fails; match the LABEL then
// climb). Read-only; a real pointer hover is dispatched on the first row.
// bash scripts/parity-probes/run-probe.sh <session> scripts/parity-probes/legend-v44.mjs
(async () => {
  const head = [...document.querySelectorAll('div,p,span,h1,h2,h3,h4')].find(
    (e) => (e.textContent || '').trim() === 'Spending Breakdown' && e.children.length === 0,
  );
  const card = head ? head.closest('div[class*="rounded"]') : null;
  if (!card) return JSON.stringify({ found: false, step: 'card' });
  const out = { vw: innerWidth, cardW: Math.round(card.getBoundingClientRect().width) };

  // The donut surface (the recharts wrapper).
  const donutWrap = card.querySelector('.recharts-wrapper, svg.recharts-surface');
  if (donutWrap) {
    const dr = donutWrap.getBoundingClientRect();
    out.donut = { w: Math.round(dr.width), h: Math.round(dr.height), mt: getComputedStyle(donutWrap).marginTop };
  }

  // The legend rows: located via the exact-text label spans, then climbing
  // to the row (label → left-cluster → row). Deduped by row identity.
  const LABELS = ['Need', 'Want', 'Savings'];
  const rowSet = new Set();
  for (const lab of LABELS) {
    const span = [...card.querySelectorAll('span,p')].find(
      (s) => (s.textContent || '').trim() === lab,
    );
    if (!span) continue;
    // climb: label span → left cluster → the ROW (the flex justify-between
    // container with 2 children). Walk up until a flex row with 2+ children
    // whose height is between 30 and 100.
    let node = span;
    for (let i = 0; i < 6 && node && node !== card; i++) {
      node = node.parentElement;
      if (!node) break;
      const cs = getComputedStyle(node);
      const h = Math.round(node.getBoundingClientRect().height);
      if (cs.display === 'flex' && h >= 30 && h <= 100) {
        rowSet.add(node);
        break;
      }
    }
  }
  const rows = [...rowSet];
  const readRow = (row) => {
    const r = row.getBoundingClientRect();
    const cs = getComputedStyle(row);
    const label = [...row.querySelectorAll('span,p')].find((s) => {
      const t = (s.textContent || '').trim();
      return LABELS.includes(t) && s.children.length === 0;
    });
    const amount = [...row.querySelectorAll('p,span')].find(
      (s) => /^\$\d/.test((s.textContent || '').trim()) && s.children.length === 0,
    );
    const pct = [...row.querySelectorAll('p,span')].find(
      (s) => /^\d+(\.\d+)?%$/.test((s.textContent || '').trim()) && s.children.length === 0,
    );
    const dot = [...row.querySelectorAll('div,span')].find((d) => {
      const w = Math.round(d.getBoundingClientRect().width);
      return !d.children.length && w > 0 && w <= 20 && getComputedStyle(d).backgroundColor !== 'rgba(0, 0, 0, 0)';
    });
    const icon = row.querySelector('svg');
    return {
      h: Math.round(r.height),
      w: Math.round(r.width),
      pad: cs.padding,
      radius: cs.borderRadius,
      bg: cs.backgroundColor,
      cursor: cs.cursor,
      transition: cs.transitionProperty,
      transitionDur: cs.transitionDuration,
      label: label
        ? {
            font: getComputedStyle(label).fontSize,
            weight: getComputedStyle(label).fontWeight,
            color: getComputedStyle(label).color,
            h: Math.round(label.getBoundingClientRect().height),
          }
        : null,
      amount: amount
        ? {
            font: getComputedStyle(amount).fontSize,
            weight: getComputedStyle(amount).fontWeight,
            color: getComputedStyle(amount).color,
          }
        : null,
      pct: pct ? { font: getComputedStyle(pct).fontSize, color: getComputedStyle(pct).color } : null,
      dot: dot
        ? {
            w: Math.round(dot.getBoundingClientRect().width),
            h: Math.round(dot.getBoundingClientRect().height),
            radius: getComputedStyle(dot).borderRadius,
            bg: getComputedStyle(dot).backgroundColor,
          }
        : null,
      icon: icon
        ? { w: Math.round(icon.getBoundingClientRect().width), h: Math.round(icon.getBoundingClientRect().height) }
        : null,
      text: (row.textContent || '').replace(/\s+/g, ' ').slice(0, 30),
    };
  };
  out.rows = { count: rows.length, list: rows.slice(0, 3).map(readRow) };

  // The inter-row gap + the legend container's margins/gap.
  if (rows.length >= 2) {
    const sorted = rows.sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);
    const r0 = sorted[0].getBoundingClientRect();
    const r1 = sorted[1].getBoundingClientRect();
    out.gap = Math.round(r1.top - r0.bottom);
    out.order = sorted.map((row) =>
      (row.textContent || '').replace(/\s+/g, ' ').slice(0, 12),
    );
    const container = sorted[0].parentElement;
    if (container) {
      const ccs = getComputedStyle(container);
      out.container = { mt: ccs.marginTop, display: ccs.display, gap: ccs.gap, spaceY: ccs.rowGap };
    }
  }

  // The REAL hover on the first row (the rows carry no mouse-following
  // tooltip — safe to hover directly, unlike the donut sectors).
  if (rows.length) {
    const row = rows[0];
    const r = row.getBoundingClientRect();
    const cx = r.x + r.width / 2;
    const cy = r.y + r.height / 2;
    const before = {
      bg: getComputedStyle(row).backgroundColor,
      shadow: getComputedStyle(row).boxShadow,
      cursor: getComputedStyle(row).cursor,
    };
    row.dispatchEvent(
      new PointerEvent('pointermove', { bubbles: true, cancelable: true, clientX: cx, clientY: cy }),
    );
    row.dispatchEvent(new MouseEvent('mouseover', { bubbles: true, cancelable: true, clientX: cx, clientY: cy }));
    row.dispatchEvent(new MouseEvent('mouseenter', { bubbles: false, cancelable: true, clientX: cx, clientY: cy }));
    await new Promise((res) => setTimeout(res, 300));
    const after = {
      bg: getComputedStyle(row).backgroundColor,
      shadow: getComputedStyle(row).boxShadow,
      cursor: getComputedStyle(row).cursor,
    };
    row.dispatchEvent(new MouseEvent('mouseout', { bubbles: true, cancelable: true, clientX: cx, clientY: cy }));
    out.hover = { before, after, changed: JSON.stringify(before) !== JSON.stringify(after) };
  }

  out.sw = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})()
