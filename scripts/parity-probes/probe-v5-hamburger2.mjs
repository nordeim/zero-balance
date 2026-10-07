// Session-8 (v5): mobile hamburger hit-test — find by accessible-name-ish (first small button in top bar).
(() => {
  const out = {};
  const btns = [...document.querySelectorAll('button')];
  // the hamburger: small square button near the top-left at mobile
  const b = btns.find((x) => {
    const r = x.getBoundingClientRect();
    return r.top < 80 && r.left < 80 && r.width > 20 && r.width < 60 && !/Add/i.test(x.textContent || '');
  });
  if (!b) return JSON.stringify({ error: 'no burger', btnCount: btns.length });
  const r = b.getBoundingClientRect();
  const top = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2);
  out.hit = { tag: top.tagName, cls: (top.className || '').toString().slice(0, 70) };
  out.isButtonChild = b.contains(top);
  out.burgerBox = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
  return JSON.stringify(out, null, 1);
})()
