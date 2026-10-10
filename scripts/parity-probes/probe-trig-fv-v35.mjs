(async () => {
  const t = document.activeElement;
  const c = getComputedStyle(t);
  return JSON.stringify({
    active: t.tagName + ':' + (t.textContent || '').trim().slice(0, 12),
    matches: t.matches(':focus'),
    matchesFV: t.matches(':focus-visible'),
    boxShadow: c.boxShadow,
    outline: c.outline,
    hasFocus: document.hasFocus(),
  });
})()
