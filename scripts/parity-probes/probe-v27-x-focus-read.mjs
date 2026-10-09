// v27 sweep: read the FULL focus-visible shadow of the dialog's X-close button.
(() => {
  const el = document.activeElement;
  const cs = getComputedStyle(el);
  return JSON.stringify({
    tag: el.tagName,
    txt: (el.textContent || el.getAttribute("aria-label") || "").trim().slice(0, 12),
    w: Math.round(el.getBoundingClientRect().width),
    fullBoxShadow: cs.boxShadow,
    outline: cs.outlineStyle + " " + cs.outlineWidth,
  });
})()
