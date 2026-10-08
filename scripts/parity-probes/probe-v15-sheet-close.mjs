// probe-v15-sheet-close.mjs — R2 clone side: after tapping a nav link in the
// sheet, the sheet must CLOSE (the reference traps instead).
(() => {
  const links = [...document.querySelectorAll('a, button')].filter(
    (el) => /^Income$/.test(el.textContent.trim()) && el.getBoundingClientRect().height > 0 && el.closest('[data-state]')
  );
  return JSON.stringify({
    sheetOpen: !!document.querySelector('[data-state="open"]'),
    incomeLinks: links.map((el) => {
      const r = el.getBoundingClientRect();
      return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    }),
  });
})()
