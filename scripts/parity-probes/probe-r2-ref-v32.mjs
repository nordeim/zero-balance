// v32: the ROBUST reference sheet detector for R2 (the trap check). The v31
// probe's white-background matcher missed the reference's sheet this session
// (sheetOpened:false while the sheet was open) — this detector matches the
// STRUCTURE instead: a fixed panel wider than 200px carrying ≥4 nav links,
// plus the body-lock + dark-overlay census. Run with the sheet OPEN.
// bash scripts/parity-probes/run-probe.sh <session> probe-r2-ref-v32.mjs
(() => {
  const fixedPanels = [...document.querySelectorAll('div')].filter(d => {
    const cs = getComputedStyle(d);
    return cs.position === 'fixed' && d.getBoundingClientRect().width > 200 && d.querySelectorAll('a').length >= 4;
  });
  const bodyLock = document.body.style.overflow === 'hidden' || getComputedStyle(document.body).overflow === 'hidden';
  const darkOverlays = [...document.querySelectorAll('div')].filter(d => {
    const cs = getComputedStyle(d);
    return cs.position === 'fixed' && cs.backgroundColor.includes('rgba(0, 0, 0');
  }).length;
  return JSON.stringify({ sheetOpen: fixedPanels.length > 0, bodyLocked: bodyLock, darkOverlays, panelClass: fixedPanels.length ? String(fixedPanels[0].className).slice(0, 60) : null });
})()
