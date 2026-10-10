(async () => {
  const btn = [...document.querySelectorAll('button')].find(x => x.textContent.includes('Toggle Sidebar'));
  if (btn) btn.click();
  await new Promise(r => setTimeout(r, 700));
  const sheet = [...document.querySelectorAll('div')].filter(d => {
    const c = (d.className || '').toString(); const r = d.getBoundingClientRect();
    return c.includes('fixed') && r.width > 150 && r.height > 300 && d.querySelectorAll('a[href]').length >= 3;
  });
  return JSON.stringify({
    toggled: !!btn,
    sheetOpen: sheet.length > 0,
    bodyLocked: document.body.style.overflow !== '' || getComputedStyle(document.body).overflow === 'hidden',
  });
})()
