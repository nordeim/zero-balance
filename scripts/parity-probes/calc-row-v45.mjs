// v45: the CALCULATOR LINE-ITEM ROW census + hover — the v6/v32 pins
// covered the row chrome at rest (p-4, border, 32px actions) and the
// focus-visible rings, but never the ROW's own hover state (the
// transition-all hover:shadow-md family — the clone's row carries NO
// inline boxShadow so its hover is LIVE, unlike the item cards whose
// inline shadow makes them inert). The reference's row hover is
// UNMEASURED. A REAL pointer hover is dispatched on the row.
// Assumes the calculator dialog is OPEN (the driver clicked Calculate).
// bash scripts/parity-probes/run-probe.sh <session> scripts/parity-probes/calc-row-v45.mjs
(async () => {
  // The calculator dialog: the fixed overlay's panel. Located via its
  // distinctive content (the "#total" orange total or the Add First Item /
  // line rows). Structure-agnostic climb.
  const dlg = [...document.querySelectorAll('div[role="dialog"], div.fixed')]
    .filter((d) => {
      const r = d.getBoundingClientRect();
      return r.width > 0 && (d.textContent || '').length > 50;
    })
    .pop();
  if (!dlg) return JSON.stringify({ found: false, hint: 'no dialog' });
  const panel = dlg.matches('[role="dialog"]') ? dlg : (dlg.querySelector('[role="dialog"]') || dlg);
  const pr = panel.getBoundingClientRect();
  const out = {
    vw: innerWidth,
    panel: { w: Math.round(pr.width), h: Math.round(pr.height) },
  };

  // The line-item row: a white rounded-xl bordered block inside the
  // dialog. Found via the rows' common parent (the space-y-3 stack).
  let row = null;
  const stackCandidates = [...panel.querySelectorAll('div')].filter((d) => {
    const cs = getComputedStyle(d);
    return (cs.display === 'flex' || cs.display === 'block') && d.children.length >= 1;
  });
  // Locate a row: a div whose computed borderRadius is ~12px, bg white,
  // has a border, and contains an h4 (the row's name heading).
  for (const d of [...panel.querySelectorAll('div')]) {
    const cs = getComputedStyle(d);
    const r = d.getBoundingClientRect();
    const hasH4 = d.querySelector('h4');
    const isRowItself = [...d.children].some((c) => c.querySelector && c.querySelector('h4'));
    if (hasH4 && r.width > 100 && cs.backgroundColor === 'rgb(255, 255, 255)' && parseFloat(cs.borderTopWidth) > 0) {
      // walk: prefer the node that directly contains the h4 AND carries the border
      row = d;
      if (cs.borderTopStyle !== 'none' && d.querySelector(':scope > div > h4, :scope > h4, :scope > div > div > h4')) break;
    }
  }
  if (!row) return JSON.stringify({ ...out, found: false, hint: 'no row — empty calculator?' });

  const readRow = (r) => {
    const cs = getComputedStyle(r);
    const rect = r.getBoundingClientRect();
    return {
      w: Math.round(rect.width),
      h: Math.round(rect.height),
      pad: cs.padding,
      radius: cs.borderRadius,
      border: `${cs.borderTopWidth} ${cs.borderTopStyle} ${cs.borderTopColor}`,
      boxShadow: cs.boxShadow,
      bg: cs.backgroundColor,
      transition: cs.transitionProperty,
      transitionDur: cs.transitionDuration,
    };
  };
  out.row = readRow(row);

  // The row's hover-revealed action pair: opacity-0 group-hover:opacity-100.
  const actions = [...row.querySelectorAll('div')].find((d) => {
    const cs = getComputedStyle(d);
    return cs.display === 'flex' && cs.opacity === '0' && d.querySelectorAll('button').length >= 1;
  });
  out.actionPair = actions
    ? {
        opacity: getComputedStyle(actions).opacity,
        btnW: Math.round(actions.querySelector('button').getBoundingClientRect().width),
        btnH: Math.round(actions.querySelector('button').getBoundingClientRect().height),
        gap: getComputedStyle(actions).gap,
      }
    : null;

  // REAL pointer hover on the row (the hover-v43 idiom).
  const rr = row.getBoundingClientRect();
  const rx = rr.left + Math.min(120, rr.width / 4);
  const ry = rr.top + rr.height / 2;
  for (const type of ['pointermove', 'mouseover', 'pointerover']) {
    row.dispatchEvent(new MouseEvent(type, { bubbles: true, clientX: rx, clientY: ry, composed: true }));
  }
  await new Promise((r) => setTimeout(r, 400));
  const after = readRow(row);
  out.hover = {
    boxShadow: after.boxShadow,
    changed: after.boxShadow !== out.row.boxShadow,
  };
  if (actions) out.hover.actionOpacity = getComputedStyle(actions).opacity;

  // The row count + the total card (context).
  out.rowCount = [...panel.querySelectorAll('h4')].filter((h) => h.closest('div[class*="rounded"]')).length;
  out.sw = document.documentElement.scrollWidth;
  return JSON.stringify(out);
})();
