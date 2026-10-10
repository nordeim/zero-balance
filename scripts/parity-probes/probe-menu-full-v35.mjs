(async () => {
  // v35: open the card action menu via the trigger and read the full item classes.
  const trig = [...document.querySelectorAll('button')].find(b => b.getAttribute('aria-haspopup') === 'menu');
  if (!trig) return JSON.stringify({error: 'no trigger'});
  trig.dispatchEvent(new PointerEvent('pointerdown', {bubbles: true, pointerId: 1}));
  trig.dispatchEvent(new MouseEvent('mousedown', {bubbles: true}));
  trig.click();
  await new Promise(r => setTimeout(r, 900));
  const m = document.querySelector('[role="menu"]');
  if (!m) return JSON.stringify({menuOpen: false});
  const items = [...m.querySelectorAll('[role="menuitem"]')];
  return JSON.stringify({
    menuOpen: true,
    wrapperTag: m.parentElement ? m.parentElement.tagName + (m.parentElement.hasAttribute('data-radix-popper-content-wrapper') ? '+popper' : '') : null,
    menuCls: (m.className || '').toString(),
    itemClasses: items.map(i => (i.className || '').toString()),
    initialActive: document.activeElement.tagName + ':' + (document.activeElement.getAttribute('role') || document.activeElement.textContent || '').toString().slice(0, 10),
  });
})()
