// v26 session: the verify-email state's INPUTS audit (the session-51 log's
// suggestion 2 — the state's inputs were never swept as an aria/landmark/
// focus surface). Registers are rate-capped on the reference (the
// "Security verification" gate) — run this AFTER landing on the verify
// state by whatever means. Reads the six code inputs' attributes, the
// state's landmark structure, and (with `act` query flags) the live
// keyboard behaviors.
(() => {
  const out = { path: location.pathname };
  const h2 = document.querySelector("h2");
  out.h2 = h2 ? h2.textContent.trim() : null;
  out.landmarks = ["main", "nav", "form"].map((t) => ({
    tag: t,
    count: document.querySelectorAll(t).length,
  }));
  const ins = [...document.querySelectorAll('input[inputmode="numeric"]')];
  out.inputs = ins.map((i) => ({
    type: i.type,
    inputmode: i.getAttribute("inputmode"),
    ac: i.getAttribute("autocomplete"),
    ariaLabel: i.getAttribute("aria-label"),
    pattern: i.getAttribute("pattern"),
    maxLength: i.getAttribute("maxlength"),
    w: Math.round(i.getBoundingClientRect().width),
    h: Math.round(i.getBoundingClientRect().height),
  }));
  out.focusIdx = ins.indexOf(document.activeElement);
  return JSON.stringify(out, null, 1);
})()
