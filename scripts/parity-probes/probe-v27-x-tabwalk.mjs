// v27 sweep: walk the clone dialog's tab stops and report which element is focused,
// flagging the 36px X-close button when it lands.
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  // state check: is the dialog open?
  const dlg = document.querySelector("[role=dialog][data-state=open], [data-state=open][role=dialog]");
  if (!dlg) return JSON.stringify({ error: "no open dialog", active: document.activeElement.tagName });
  const x = [...dlg.querySelectorAll("button")].find((b) => {
    const r = b.getBoundingClientRect();
    return Math.round(r.width) === 36 && b.querySelector("svg") && b.querySelector(".sr-only");
  });
  if (!x) return JSON.stringify({ error: "no 36px X in dialog", dlgW: Math.round(dlg.getBoundingClientRect().width) });
  // dispatch REAL keydown Tab events from the document — these engage Chromium's
  // actual focus navigation including :focus-visible heuristics.
  const stops = [];
  const seenX = { hit: false, shadow: null, outline: null };
  for (let i = 0; i < 14 && !seenX.hit; i++) {
    document.dispatchEvent(new KeyboardEvent("keydown", { key: "Tab", bubbles: true, cancelable: true }));
    await sleep(120);
    const el = document.activeElement;
    if (el === x) {
      const cs = getComputedStyle(el);
      seenX.hit = true;
      seenX.shadow = cs.boxShadow;
      seenX.outline = cs.outlineStyle + " " + cs.outlineWidth + " " + cs.outlineColor;
    } else {
      stops.push(el.tagName + ":" + (el.textContent || el.getAttribute("aria-label") || "").trim().slice(0, 8));
    }
  }
  return JSON.stringify({ xFound: seenX.hit, fullShadow: seenX.shadow, outline: seenX.outline, walked: stops.slice(0, 12) }, null, 1);
})()
