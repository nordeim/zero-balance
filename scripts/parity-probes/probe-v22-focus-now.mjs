(() => {
  const el = document.activeElement;
  if (!el || el === document.body) return JSON.stringify({ body: true });
  const r = el.getBoundingClientRect();
  const cs = getComputedStyle(el);
  return JSON.stringify({
    t: el.tagName,
    label: (el.getAttribute("aria-label") || el.textContent || "").trim().slice(0, 24),
    x: Math.round(r.x), y: Math.round(r.y),
    ring: (cs.boxShadow || "").slice(0, 70),
    outline: (cs.outlineStyle + " " + cs.outlineWidth + " " + (cs.outlineColor || "")).slice(0, 44),
  });
})()
