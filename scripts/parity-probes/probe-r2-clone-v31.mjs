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
  const sheetOpen = !!document.querySelector('[role=dialog]');
  const link = sheetOpen ? [...document.querySelectorAll('[role=dialog] a')].find(a => /income/i.test(a.textContent)) : null;
  let afterNav = 'no-link';
  if (link) {
    const lr = link.getBoundingClientRect();
    link.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true, clientX: lr.x + lr.width / 2, clientY: lr.y + 10 }));
    await new Promise(res => setTimeout(res, 2000));
    afterNav = document.querySelector('[role=dialog]') ? 'SHEET STILL OPEN' : 'sheet closed';
  }
  return JSON.stringify({ sheetOpened: sheetOpen, afterNavClick: afterNav, url: location.pathname, scrollWidth: document.documentElement.scrollWidth });
})()
