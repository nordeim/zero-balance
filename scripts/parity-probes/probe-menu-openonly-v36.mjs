// probe-menu-openonly-v36.mjs — opens the card action menu via CLICK and returns
// the pre-hover state (container focus + both items at rest). The REAL hover then
// runs via the agent-browser hover command (separate step).
(async () => {
  const trig = [...document.querySelectorAll('button')].find(b => b.getAttribute('aria-haspopup') === 'menu');
  if (!trig) return JSON.stringify({ error: 'no trigger' });
  trig.dispatchEvent(new PointerEvent('pointerdown', { bubbles: true, pointerId: 1 }));
  trig.dispatchEvent(new MouseEvent('mousedown', { bubbles: true }));
  trig.click();
  await new Promise(r => setTimeout(r, 700));
  const m = document.querySelector('[role="menu"]');
  if (!m) return JSON.stringify({ menuOpen: false });
  const items = [...m.querySelectorAll('[role="menuitem"]')];
  const read = (el) => {
    if (!el) return null;
    const c = getComputedStyle(el);
    return { bg: c.backgroundColor, color: c.color, focusMatch: el.matches(':focus'), hl: el.getAttribute('data-highlighted') };
  };
  return JSON.stringify({
    menuOpen: true,
    hasFocus: document.hasFocus(),
    active: document.activeElement === m ? 'CONTAINER' : (document.activeElement.textContent || '').trim().slice(0, 10),
    activeMatchesFocus: document.activeElement.matches(':focus'),
    item0: read(items[0]), item1: read(items[1]),
  });
})()
