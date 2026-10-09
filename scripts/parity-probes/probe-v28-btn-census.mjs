// v28 sweep: one-pass BUTTON class census — every <button> on the page with
// its full class attribute (the family arbiter), geometry, and rest color.
// The session-55 suggestion: diff ALL button variants between the sites in
// one sweep to surface any remaining family drifts. No truncation — the
// class string IS the evidence.
(() => {
  const out = { path: location.pathname, buttons: [] };
  [...document.querySelectorAll("button")].forEach((b) => {
    if (!b.isConnected || b.getBoundingClientRect().width === 0) return;
    const cls = (b.className || "").toString().trim();
    if (!cls) return;
    const r = b.getBoundingClientRect();
    const cs = getComputedStyle(b);
    out.buttons.push({
      txt: (b.textContent || b.getAttribute("aria-label") || "").trim().replace(/\s+/g, " ").slice(0, 24),
      w: Math.round(r.width),
      h: Math.round(r.height),
      cls,
    });
  });
  out.count = out.buttons.length;
  return JSON.stringify(out);
})()
