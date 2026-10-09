(() => {
  const el = document.activeElement;
  const cs = getComputedStyle(el);
  return JSON.stringify({
    label: (el.textContent || '').trim().slice(0, 16),
    boxShadow: cs.boxShadow,
    outline: cs.outlineStyle + ' ' + cs.outlineWidth + ' ' + cs.outlineColor,
  });
})()
