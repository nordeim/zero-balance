(() => {
  // the DIALOG's X: inside the topmost fixed overlay, in the sticky header row
  const overlays = [...document.querySelectorAll('div')].filter(d => getComputedStyle(d).position === 'fixed' && d.querySelector('input, select, textarea, form'));
  if (!overlays.length) return 'no dialog open';
  const o = overlays[overlays.length - 1];
  const x = [...o.querySelectorAll('button')].find(b => {
    const r = b.getBoundingClientRect();
    const svg = b.querySelector('svg');
    const srText = /close/i.test((b.textContent || '').trim());
    return r.width <= 40 && r.height <= 40 && svg && (r.y < 400) && (srText || !b.textContent.trim().length);
  });
  if (!x) return 'no X in dialog';
  const cs = getComputedStyle(x);
  return JSON.stringify({
    box: (r => ({ w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y) }))(x.getBoundingClientRect()),
    border: cs.border, radius: cs.borderRadius, bg: cs.backgroundColor,
    outline: cs.outline, boxShadow: cs.boxShadow, color: cs.color,
    focused: document.activeElement === x
  });
})()
