// v27 sweep: the dialog X-close button's HOVER family — bg + text color under a
// parked pointer (parked at the X's center; the v22 parked-pointer discipline).
(async () => {
  const save = [...document.querySelectorAll("button")].find((b) => /save/i.test((b.textContent || "").trim()) && (b.closest("[role=dialog]") || /save item/i.test(b.textContent || "")));
  let dlg = null;
  if (save) {
    dlg = save.closest("[role=dialog]") || save.parentElement;
    while (dlg && dlg !== document.body && !/(auto|scroll)/.test(getComputedStyle(dlg).overflowY)) dlg = dlg.parentElement;
  }
  if (!dlg) return "NO DIALOG";
  const x = [...dlg.querySelectorAll("button")].find((b) => {
    const r = b.getBoundingClientRect();
    return Math.round(r.width) === 36 && b.querySelector("svg");
  });
  if (!x) return "NO X";
  const cs = getComputedStyle(x);
  const out = {
    w: Math.round(x.getBoundingClientRect().width),
    restColor: cs.color,
    restBg: cs.backgroundColor,
    clsHover: (x.className || "").toString().match(/hover:[^ ]+/g) ?? [],
  };
  return JSON.stringify(out, null, 1);
})()
