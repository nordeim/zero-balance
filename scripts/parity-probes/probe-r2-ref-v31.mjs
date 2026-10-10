(async () => {
  window.scrollTo(0, 0);
  await new Promise(r => setTimeout(r, 300));
  const btn = [...document.querySelectorAll('button')].find(b => {
    const r = b.getBoundingClientRect();
    return r.width > 20 && r.width < 45 && r.top < 60 && b.querySelector('svg');
  });
  if (!btn) return 'no burger';
  const r = btn.getBoundingClientRect();
  btn.querySelector('svg').dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, clientX: r.x + 5, clientY: r.y + 5 }));
  await new Promise(res => setTimeout(res, 1200));
  const overlay = [...document.querySelectorAll('div')].find(d => d.className && /fixed/.test(d.className) && /inset-0|black/.test(d.className + ' ' + (d.getAttribute('style') || '')));
  const sheetVisible = !!([ ...document.querySelectorAll('div') ].find(d => {
    const cs = getComputedStyle(d);
    return cs.position === 'fixed' && cs.backgroundColor === 'rgb(255, 255, 255)' && d.getBoundingClientRect().width > 200;
  }));
  const link = [...document.querySelectorAll('a')].find(a => /income/i.test(a.textContent) && a.getBoundingClientRect().left < 300);
  let afterNav = 'no-link';
  let sheetAfter = null;
  if (link) {
    const lr = link.getBoundingClientRect();
    link.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, clientX: lr.x + lr.width / 2, clientY: lr.y + 10 }));
    await new Promise(res => setTimeout(res, 2000));
    const sheetStill = [...document.querySelectorAll('div')].find(d => {
      const cs = getComputedStyle(d);
      return cs.position === 'fixed' && cs.backgroundColor === 'rgb(255, 255, 255)' && d.getBoundingClientRect().width > 200;
    });
    sheetAfter = sheetStill ? 'SHEET STILL OPEN (trapped)' : 'sheet closed';
  }
  return JSON.stringify({ sheetOpened: sheetVisible, afterNavClick: afterNav, sheetAfter, url: location.pathname });
})()
