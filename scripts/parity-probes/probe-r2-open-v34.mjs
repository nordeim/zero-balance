(async () => {
  // R2 step 1: open the sheet (structure detector)
  const b = [...document.querySelectorAll('button')].find(x =>
    x.textContent.includes('Toggle Sidebar') ||
    (x.getAttribute('aria-label') || '').includes('Toggle Sidebar'));
  if (b) b.click();
  await new Promise(r => setTimeout(r, 800));
  // structure-based sheet detector: fixed side panel + nav links + body lock
  const fixed = [...document.querySelectorAll('div')].filter(d => {
    const c = (d.className || '').toString();
    const r = d.getBoundingClientRect();
    return c.includes('fixed') && r.width > 150 && r.height > 300 &&
      d.querySelectorAll('a[href]').length >= 3;
  });
  const sheet = fixed[0];
  return JSON.stringify({
    sheetOpen: !!sheet,
    bodyLocked: document.body.style.overflow !== '' || getComputedStyle(document.body).overflow === 'hidden',
    fixedPanels: fixed.length,
    overlayCount: [...document.querySelectorAll('div')].filter(d => {
      const c = (d.className || '').toString();
      const r = d.getBoundingClientRect();
      return c.includes('fixed') && c.includes('inset-0') && r.width >= 380;
    }).length,
  });
})()
