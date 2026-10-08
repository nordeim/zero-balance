// probe-v16-sheet-close.mjs — R2 sheet trap test on the clone: after tapping
// a nav link in the sheet, the sheet + overlay must be GONE (the reference's
// trap bug is superset-fixed). Run with the sheet OPEN.
(() => {
  const links = [...document.querySelectorAll("a")].filter((a) => /income/i.test(a.textContent));
  const l = links.find((a) => a.getBoundingClientRect().width > 100);
  if (!l) return JSON.stringify({ error: "no income link" });
  const r = l.getBoundingClientRect();
  const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
  l.click();
  return JSON.stringify({
    incomeLink: { x: r.x, y: r.y, w: r.width, h: r.height },
    center: [cx, cy],
    clicked: true,
  });
})()
