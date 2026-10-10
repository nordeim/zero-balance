// probe-tabwalk-v36.mjs — v36 Surface C: the full Tab-order census of the items
// view (/income). Walks REAL Tab presses from the page start, recording each
// focusable stop's tag, role, accessible name, geometry, and (for the
// hover-revealed triggers) visibility. The v33 census covered the sub-dialog;
// the PAGE-level walk was never measured. Run at 1280x800.
(async () => {
  const stops = [];
  const nameOf = (el) => {
    const lab = el.getAttribute('aria-label');
    if (lab) return lab.slice(0, 24);
    const id = el.closest('[aria-labelledby]');
    if (id) { const src = document.getElementById(id.getAttribute('aria-labelledby')); if (src) return src.textContent.trim().slice(0, 24); }
    return (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 24);
  };
  // reset focus to the document start
  if (document.activeElement && document.activeElement !== document.body) document.activeElement.blur();
  // NOTE: a synthetic Tab keydown does not MOVE focus — the walk needs REAL
  // Tab presses via agent-browser press (tabwalk-v36.sh drives those and
  // reads document.activeElement after each).
  const read = () => {
    const el = document.activeElement;
    if (!el || el === document.body) return null;
    const r = el.getBoundingClientRect();
    const c = getComputedStyle(el);
    return {
      tag: el.tagName.toLowerCase(),
      role: el.getAttribute('role'),
      name: nameOf(el),
      rect: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
      opacity: c.opacity,
      cursor: c.cursor,
    };
  };
  return JSON.stringify({ active: read(), hasFocus: document.hasFocus() });
})()
