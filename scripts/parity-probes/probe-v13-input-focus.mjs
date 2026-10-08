// probe-v13-input-focus.mjs — login input focus ring (email + password):
// the reference renders the two-layer shadcn v1 ring on plain :focus —
// border #94a3b8 + box-shadow "rgb(255,255,255) 0 0 0 2px,
// rgb(148,163,184) 0 0 0 4px" (+ v3's transparent trailing layer).
// Settle before reading: transition-colors animates the border color.
(async () => {
  const out = {};
  for (const sel of ["input#email", "input#password"]) {
    const e = document.querySelector(sel);
    if (!e) { out[sel] = "absent"; continue; }
    e.focus();
    await new Promise((r) => setTimeout(r, 350));
    const cs = getComputedStyle(e);
    out[sel] = { border: cs.borderColor, shadow: cs.boxShadow, outline: cs.outline };
    e.blur();
  }
  return JSON.stringify(out, null, 1);
})()
