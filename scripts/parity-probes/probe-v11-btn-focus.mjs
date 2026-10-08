// probe-v11-btn-focus.mjs — focus-visible ring on the dialog's primary (Save) button
(() => {
  const out = {};
  // find the dialog PANEL (white, ~672px) — a child of the overlay on the ref,
  // a portal sibling on the clone; search whichever holds buttons
  const panel = [...document.querySelectorAll('div')].filter(d => {
    const r = d.getBoundingClientRect(); const cs = getComputedStyle(d);
    return r.width > 500 && r.width < 750 && r.height > 200 && cs.backgroundColor === 'rgb(255, 255, 255)' && d.querySelectorAll('button').length > 0;
  }).sort((a, b) => (b.textContent || '').length - (a.textContent || '').length)[0];
  if (!panel) return 'no dialog panel';
  const btn = [...panel.querySelectorAll('button')].filter(b => /save/i.test(b.textContent || '') && b.getBoundingClientRect().height > 0)[0];
  if (!btn) return 'no save button';
  btn.focus({ focusVisible: true });
  const cs = getComputedStyle(btn);
  const r = btn.getBoundingClientRect();
  out.save = {
    w: Math.round(r.width), h: Math.round(r.height),
    boxShadow: cs.boxShadow,
    outline: cs.outlineStyle + ' ' + cs.outlineWidth,
    bg: (cs.backgroundImage !== 'none' ? cs.backgroundImage : cs.backgroundColor).toString().slice(0, 60)
  };
  return JSON.stringify(out, null, 1);
})()
