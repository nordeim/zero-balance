// v28 sweep: real-Tab walk stop reader — reports the focused element's
// tag/text/geometry + FULL focus-visible shadow (box-shadow layers + outline).
(() => {
  const el = document.activeElement;
  if (!el || el === document.body) return JSON.stringify({ stop: "body" });
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  return JSON.stringify({
    tag: el.tagName,
    txt: (el.textContent || el.getAttribute("aria-label") || "").trim().replace(/\s+/g, " ").slice(0, 20),
    w: Math.round(r.width), h: Math.round(r.height),
    cls: ((el.className || "").toString()).slice(0, 200),
    boxShadow: cs.boxShadow,
    outline: cs.outlineStyle + " " + cs.outlineWidth + " " + cs.outlineColor,
  });
})()
