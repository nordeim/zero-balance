// v25: walk ALL keyboard focusables on /login via REAL Tab presses handled
// by the caller (agent-browser press Tab); this eval reads the CURRENT
// focused element's full focus chrome. Called in a loop by kb-login-walk-v25.sh.
(() => {
  const el = document.activeElement;
  if (!el || el === document.body) return JSON.stringify({ stop: "body" });
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  return JSON.stringify({
    stop: el.tagName,
    label: (el.textContent || el.placeholder || el.getAttribute("aria-label") || "").trim().replace(/\s+/g, " ").slice(0, 26),
    boxShadow: cs.boxShadow,
    outline: (cs.outlineStyle + " " + cs.outlineWidth + " " + cs.outlineColor).slice(0, 50),
    color: cs.color,
    bg: cs.backgroundColor,
    y: Math.round(r.y)
  });
})()
