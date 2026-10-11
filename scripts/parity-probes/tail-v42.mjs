// v42: the tail-band check — the last content band's margin-bottom and the
// total document scrollHeight (the trailing-space class: the reference
// applies mb-8 to EVERY band including the last; the clone uses mt-8 on
// subsequent bands — the trailing 32px is the visible difference at the
// page bottom).
(() => {
  const h1 = [...document.querySelectorAll('h1')]
    .filter((h) => !h.closest('header'))
    .find((h) => h.getBoundingClientRect().height > 0);
  const cap = h1 ? h1.closest('div[class*="max-w"]') : null;
  if (!cap) return JSON.stringify({ found: false });
  const kids = [...cap.children];
  const last = kids[kids.length - 1];
  const cs = getComputedStyle(last);
  const doc = document.documentElement;
  return JSON.stringify({
    path: location.pathname,
    bands: kids.length,
    lastBand: {
      text: (last.textContent || '').trim().slice(0, 20),
      mb: cs.marginBottom,
      h: Math.round(last.getBoundingClientRect().height),
    },
    scrollH: doc.scrollHeight,
    vw: window.innerWidth,
  });
})()
