(async () => {
  // v40: the dashboard focusable-element census — DOM order of every
  // focusable element (a[href], button, [tabindex]>=0, input) with rects,
  // NO Tab scrolling artifacts. Mirrors the tabwalk ground truth.
  const els = [...document.querySelectorAll("a[href], button, input, [tabindex]")].filter((el) => {
    if (el.closest("script, style, [aria-hidden='true']")) return false;
    if (el.getAttribute("tabindex") === "-1") return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 || r.height > 0;
  });
  return JSON.stringify(
    els.map((el) => {
      const r = el.getBoundingClientRect();
      return {
        tag: el.tagName.toLowerCase(),
        role: el.getAttribute("role"),
        name: (
          el.getAttribute("aria-label") ||
          (el.textContent || "").trim().replace(/\s+/g, " ")
        ).slice(0, 26),
        rect: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
      };
    }),
  );
})()
