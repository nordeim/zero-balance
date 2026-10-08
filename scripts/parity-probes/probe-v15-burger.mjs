// probe-v15-burger.mjs — R1: the toast-viewport hit-test on the burger's center.
// The reference's toast containers (fixed top, pe:auto) intercept the burger's
// center hit; the clone's burger hit must be DIRECT (on the svg/button).
(() => {
  const out = {};
  // find the burger: the button in the mobile top bar (28×28 at (24,16))
  const btns = [...document.querySelectorAll('button')].filter((b) => {
    const r = b.getBoundingClientRect();
    return r.width > 0 && r.height > 0 && r.width < 60 && r.height < 60;
  });
  // the burger: accessible name "Toggle Sidebar" (clone) / top-bar button (ref)
  const burger =
    btns.find((b) => /toggle sidebar/i.test(b.getAttribute('aria-label') || '')) ||
    btns.find((b) => {
      const r = b.getBoundingClientRect();
      const svg = b.querySelector('svg');
      return r.y < 100 && svg && r.width <= 32;
    });
  if (!burger) return JSON.stringify({ error: 'no burger found', btnCount: btns.length });
  const r = burger.getBoundingClientRect();
  out.burger = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
  const cx = r.x + r.width / 2, cy = r.y + r.height / 2;
  // what's at the burger's center?
  const stack = document.elementsFromPoint(cx, cy).slice(0, 5).map((el) => {
    const cs = getComputedStyle(el);
    const rr = el.getBoundingClientRect();
    return {
      tag: el.tagName.toLowerCase(),
      cls: (el.getAttribute('class') || '').slice(0, 50),
      pe: cs.pointerEvents,
      pos: cs.position,
      z: cs.zIndex,
      w: Math.round(rr.width), h: Math.round(rr.height),
    };
  });
  out.hitStack = stack;
  // the svg inside
  const svg = burger.querySelector('svg');
  if (svg) {
    const sr = svg.getBoundingClientRect();
    out.svg = { w: Math.round(sr.width), h: Math.round(sr.height) };
    out.svgDirectHit = document.elementsFromPoint(cx, cy).includes(svg);
  }
  out.buttonDirectHit = document.elementsFromPoint(cx, cy).includes(burger);
  // any fixed toast containers at top
  out.toastContainers = [...document.querySelectorAll('body *')].filter((el) => {
    if (!el.isConnected || el.children.length > 3) return false;
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed') return false;
    const rr = el.getBoundingClientRect();
    return rr.y <= 40 && rr.height <= 60 && cs.zIndex !== 'auto' && cs.pointerEvents === 'auto' && rr.width > 200;
  }).length;
  return JSON.stringify(out, null, 1);
})()
