// v46: the CONFIRM-BAR white-pill census — the session-101 queue's third
// candidate (the five pill badges' rest shadows, the shadow-scale
// regression net, unpinned). The delete-confirm bar renders after the
// card menu's Delete click (kebab → Delete): the red-tinted bar
// (rgb(254,242,242), rounded-lg, p-3) with the white Cancel pill
// (rounded-md bg-white px-3 py-1 text-xs shadow-sm) + the red Delete
// button (bg-red-600). The five sites (item-card / budget-item-dialog /
// calculator-dialog / net-worth asset / net-worth liability) share the
// identical class family — this census pins the visible layer of the
// pill's shadow-sm (the --shadow-sm theme pin's regression net, the
// reference's v3 `0 1px 2px 0 rgb(0 0 0 / 0.05)`).
// Run AFTER the driver's kebab→Delete step. Read-only: NEVER click the
// confirm Delete (the driver clicks Cancel to restore).
// bash scripts/parity-probes/run-probe.sh <session> scripts/parity-probes/confirm-pill-v46.mjs
(async () => {
  // The confirm bar: the red-tinted flex row with the Cancel/Delete pair.
  const bar = [...document.querySelectorAll('div')].find((d) => {
    const cs = getComputedStyle(d);
    if (cs.backgroundColor !== 'rgb(254, 242, 242)') return false;
    const btns = [...d.querySelectorAll('button')];
    return btns.length === 2 && btns[0].textContent.trim() === 'Cancel' && btns[1].textContent.trim() === 'Delete';
  });
  if (!bar) return JSON.stringify({ found: false, hint: 'no confirm bar' });

  const barCs = getComputedStyle(bar);
  const barR = bar.getBoundingClientRect();
  const out = {
    found: true,
    bar: {
      mt: barCs.marginTop,
      radius: barCs.borderRadius,
      pad: barCs.padding,
      bg: barCs.backgroundColor,
      w: Math.round(barR.width),
      h: Math.round(barR.height),
      justify: barCs.justifyContent,
    },
    gap: barCs.gap,
  };

  // The text label (text-sm text-red-700).
  const label = bar.querySelector('p');
  if (label) {
    const lcs = getComputedStyle(label);
    out.label = { font: lcs.fontSize, weight: lcs.fontWeight, color: lcs.color };
  }

  // The Cancel pill (the white shadow-sm site — the census's target).
  const cancel = [...bar.querySelectorAll('button')].find((b) => b.textContent.trim() === 'Cancel');
  if (cancel) {
    const ccs = getComputedStyle(cancel);
    const cr = cancel.getBoundingClientRect();
    out.cancelPill = {
      bg: ccs.backgroundColor,
      color: ccs.color,
      pad: ccs.padding,
      radius: ccs.borderRadius,
      font: ccs.fontSize,
      weight: ccs.fontWeight,
      boxShadow: ccs.boxShadow,
      h: Math.round(cr.height),
      gap: barCs.gap,
    };
  }

  // The Delete button (bg-red-600 — the destructive twin).
  const del = [...bar.querySelectorAll('button')].find((b) => b.textContent.trim() === 'Delete');
  if (del) {
    const dcs = getComputedStyle(del);
    out.deleteBtn = {
      bg: dcs.backgroundColor,
      color: dcs.color,
      pad: dcs.padding,
      radius: dcs.borderRadius,
      font: dcs.fontSize,
      weight: dcs.fontWeight,
      boxShadow: dcs.boxShadow,
    };
  }

  return JSON.stringify(out);
})();
