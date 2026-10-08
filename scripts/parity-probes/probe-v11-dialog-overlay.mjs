// probe-v11-dialog-overlay.mjs — the modal overlay (backdrop) computed state
(() => {
  const out = {};
  // the overlay: fixed full-screen element with a dark bg, behind the dialog
  const overlays = [...document.querySelectorAll('div')].filter(d => {
    const r = d.getBoundingClientRect(); const cs = getComputedStyle(d);
    return cs.position === 'fixed' && r.width >= innerWidth - 2 && r.height >= innerHeight - 2 && cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && r.top <= 1;
  });
  out.overlays = overlays.map(d => {
    const cs = getComputedStyle(d); const r = d.getBoundingClientRect();
    return { bg: cs.backgroundColor, w: Math.round(r.width), h: Math.round(r.height), z: cs.zIndex, pe: cs.pointerEvents, opacity: cs.opacity, childCount: d.children.length };
  });
  // the dialog panel itself
  const panel = [...document.querySelectorAll('div')].filter(d => {
    const r = d.getBoundingClientRect(); const cs = getComputedStyle(d);
    return r.width > 500 && r.width < 750 && cs.position === 'fixed' && r.height > 300;
  })[0];
  if (panel) {
    const r = panel.getBoundingClientRect(); const cs = getComputedStyle(panel);
    out.panel = { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), y: Math.round(r.y), bg: cs.backgroundColor, radius: cs.borderRadius, shadow: cs.boxShadow.slice(0, 70), z: cs.zIndex };
  }
  return JSON.stringify(out, null, 1);
})()
