// v28 sweep: the details dialog's overlay — computed styles + the
// outside-click close behavior + the mobile bottom-sheet geometry.
(async () => {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  const cards = [...document.querySelectorAll("main div.rounded-xl")].filter((c) => c.getBoundingClientRect().width > 200);
  cards[0].click();
  await sleep(900);
  const hdr = [...document.querySelectorAll("div")].filter((d) => /Budget Item Details/.test(d.textContent || "") && d.getBoundingClientRect().width > 0 && d.getBoundingClientRect().height < 100).pop();
  if (!hdr) return JSON.stringify({ error: "no dialog" });
  let dlg = hdr;
  for (let i = 0; i < 8; i++) { dlg = dlg.parentElement; if (getComputedStyle(dlg).position === "fixed" || dlg.tagName === "BODY") break; }
  const cs = getComputedStyle(dlg);
  const out = {
    overlay: {
      cls: (dlg.className || "").toString(),
      bg: cs.backgroundColor, display: cs.display, position: cs.position,
      justify: cs.justifyContent, align: cs.alignItems, padding: cs.padding,
    },
    childCount: dlg.children.length,
    // the reference's dialogs are plain divs (no role=dialog) — v4 lesson
    role: dlg.getAttribute("role"),
  };
  // outside click (on the overlay itself, away from the panel)
  const pr = [...dlg.children].find((c) => c.getBoundingClientRect().width > 200).getBoundingClientRect();
  dlg.dispatchEvent(new MouseEvent("click", { bubbles: true, cancelable: true, clientX: 10, clientY: 10 }));
  await sleep(700);
  const stillOpen = [...document.querySelectorAll("div")].some((d) =>
    /Budget Item Details/.test(d.textContent || "") &&
    d.getBoundingClientRect().width > 0 && d.getBoundingClientRect().height < 100 &&
    getComputedStyle(d.parentElement).position === "fixed");
  out.closedOnOutsideClick = !stillOpen;
  // Escape key behavior
  if (stillOpen) {
    document.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape", bubbles: true, cancelable: true }));
    await sleep(600);
    const openAfterEsc = [...document.querySelectorAll("div")].some((d) =>
      /Budget Item Details/.test(d.textContent || "") &&
      d.getBoundingClientRect().width > 0 && d.getBoundingClientRect().height < 100 &&
      getComputedStyle(d.parentElement).position === "fixed");
    out.closedOnEscape = !openAfterEsc;
  }
  return JSON.stringify(out, null, 1);
})()
