// probe-menu-hover-v36.mjs — v36 Surface A: the action-menu HOVER-highlight family.
// Opens the card action menu via CLICK (pointerdown family — focus lands on the
// container), then dispatches a REAL hover (mousemove + mouseenter) on the Delete
// item and reads the highlight: which element holds activeElement, whether the
// hovered item matches :focus, its data-highlighted state, and its computed
// bg/text colors (the accent tint family — the v35 G1 cascade pinned for FOCUS,
// the HOVER path measured here for the first time).
(async () => {
  const trig = [...document.querySelectorAll('button')].find(b => b.getAttribute('aria-haspopup') === 'menu');
  if (!trig) return JSON.stringify({ error: 'no trigger' });
  // fresh-open via CLICK (pointerdown is what opens Radix's trigger)
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
    return {
      bg: c.backgroundColor, color: c.color,
      focusMatch: el.matches(':focus'),
      highlighted: el.getAttribute('data-highlighted'),
    };
  };
  const before = {
    active: document.activeElement === m ? 'CONTAINER' : (document.activeElement.textContent || '').trim().slice(0, 10),
    hasFocus: document.hasFocus(),
    item0: read(items[0]), item1: read(items[1]),
  };
  // HOVER the Delete item (items[1]) with a real pointer event family
  const target = items[1];
  const r = target.getBoundingClientRect();
  const mx = r.x + r.width / 2, my = r.y + r.height / 2;
  target.dispatchEvent(new MouseEvent('mousemove', { bubbles: true, clientX: mx, clientY: my }));
  document.dispatchEvent(new MouseEvent('mousemove', { bubbles: true, clientX: mx, clientY: my }));
  target.dispatchEvent(new MouseEvent('mouseenter', { bubbles: false, clientX: mx, clientY: my }));
  target.dispatchEvent(new MouseEvent('mouseover', { bubbles: true, clientX: mx, clientY: my }));
  await new Promise(res => setTimeout(res, 500));
  const after = {
    active: document.activeElement === m ? 'CONTAINER' : (document.activeElement === target ? 'DELETE' : (document.activeElement.textContent || document.activeElement.tagName).toString().trim().slice(0, 10)),
    activeIsDelete: document.activeElement === target,
    activeMatchesFocus: document.activeElement.matches(':focus'),
    hovered: read(target), resting: read(items[0]),
  };
  return JSON.stringify({ menuOpen: true, before, after });
})()
