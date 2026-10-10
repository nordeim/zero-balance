(async () => {
  // R2 step 2: click the Income link inside the open sheet, then check the trap
  const sheet = [...document.querySelectorAll('div')].filter(d => {
    const c = (d.className || '').toString();
    const r = d.getBoundingClientRect();
    return c.includes('fixed') && r.width > 150 && r.height > 300 && d.querySelectorAll('a[href]').length >= 3;
  })[0];
  if (!sheet) return JSON.stringify({error: 'sheet not open'});
  const income = [...sheet.querySelectorAll('a[href]')].find(a => /income/i.test(a.textContent));
  income.click();
  await new Promise(r => setTimeout(r, 1200));
  // after-nav trap check on /income
  const sheetAfter = [...document.querySelectorAll('div')].filter(d => {
    const c = (d.className || '').toString();
    const r = d.getBoundingClientRect();
    return c.includes('fixed') && r.width > 150 && r.height > 300 && d.querySelectorAll('a[href]').length >= 3;
  })[0];
  return JSON.stringify({
    url: location.pathname,
    sheetStillOpen: !!sheetAfter,
    bodyStillLocked: document.body.style.overflow !== '' || getComputedStyle(document.body).overflow === 'hidden',
  });
})()
