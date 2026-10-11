(async () => {
  // v40: dump the CURRENT focused element (after the 10th Tab press done by
  // the shell) — tag/class/tabindex + the enclosing svg's tabindexed nodes
  // and text labels.
  const el = document.activeElement;
  if (!el || el === document.body) return JSON.stringify({ error: "no focused element" });
  const svg = el.closest("svg");
  const structure = svg
    ? {
        svgClass: svg.getAttribute("class"),
        svgRole: svg.getAttribute("role"),
        svgTi: svg.getAttribute("tabindex"),
        tabindexed: [...svg.querySelectorAll("[tabindex]")].map((n) => ({
          tag: n.tagName.toLowerCase(),
          cls: (n.getAttribute("class") || "").slice(0, 34),
          ti: n.getAttribute("tabindex"),
          name: n.getAttribute("name") || n.getAttribute("aria-label"),
        })),
        texts: [...svg.querySelectorAll("text")].slice(0, 8).map((t) => (t.textContent || "").trim().slice(0, 24)),
      }
    : null;
  return JSON.stringify({
    tag: el.tagName.toLowerCase(),
    cls: (el.getAttribute("class") || "").slice(0, 60),
    ti: el.getAttribute("tabindex"),
    role: el.getAttribute("role"),
    textLen: (el.textContent || "").length,
    textHead: (el.textContent || "").trim().slice(0, 50),
    structure,
  });
})()
