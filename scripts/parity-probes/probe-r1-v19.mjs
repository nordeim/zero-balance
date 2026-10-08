// v19 session: R1 — the burger hit test. Returns the burger geometry and
// what elementFromPoint reports at its center (the reference's toast
// containers intercept it; the clone's hit is the svg itself).
(() => {
  const out = {};
  const header = document.querySelector('header');
  const btn = header ? header.querySelector('button') : null;
  if (btn) {
    const r = btn.getBoundingClientRect();
    out.burger = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    const cx = Math.round(r.x + r.width / 2), cy = Math.round(r.y + r.height / 2);
    const hit = document.elementFromPoint(cx, cy);
    out.center = { x: cx, y: cy, tag: hit ? hit.tagName : null, cls: hit ? (hit.className || '').toString().slice(0, 80) : null };
    // walk up to see which fixed container owns the hit
    let el = hit, chain = [];
    while (el && chain.length < 6) { chain.push(el.tagName + (el.id ? '#' + el.id : '')); el = el.parentElement; }
    out.chain = chain;
  }
  // count fixed top-0 containers (the reference's toast viewport family)
  out.fixedTop = [...document.querySelectorAll('body *')].filter((el) => {
    const cs = getComputedStyle(el);
    return cs.position === 'fixed' && cs.top === '0px' && cs.display !== 'none' && el.getBoundingClientRect().width > 0;
  }).map((el) => ({ tag: el.tagName, cls: (el.className || '').toString().slice(0, 60), pe: getComputedStyle(el).pointerEvents, w: Math.round(el.getBoundingClientRect().width), h: Math.round(el.getBoundingClientRect().height), z: getComputedStyle(el).zIndex })).slice(0, 6);
  out.scrollWidth = document.documentElement.scrollWidth;
  out.title = document.title;
  return JSON.stringify(out, null, 1);
})()
