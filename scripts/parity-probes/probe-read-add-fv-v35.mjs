(async () => {
  // v35 Surface B: read the Add Item button's focus-visible chrome.
  const t = document.activeElement;
  const c = getComputedStyle(t);
  return JSON.stringify({
    name: (t.textContent || '').trim().slice(0, 14),
    tag: t.tagName,
    focus: t.matches(':focus'),
    fv: t.matches(':focus-visible'),
    hasFocus: document.hasFocus(),
    boxShadow: c.boxShadow,
    outline: c.outline,
    bg: c.backgroundColor,
  });
})()
