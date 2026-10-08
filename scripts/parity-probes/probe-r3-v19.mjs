// v19 session: R3 — root-route nav highlighting. The reference marks nothing
// active at `/`; the clone highlights Dashboard (white + gradient + 500).
(() => {
  const out = {};
  const nav = document.querySelector('nav');
  out.hasNavLandmark = !!nav;
  const links = [...document.querySelectorAll('a')].filter((a) => /Dashboard|Income|Expenses|Savings|Net Worth/.test((a.textContent || '').trim()) && a.getBoundingClientRect().width > 0);
  out.links = links.slice(0, 6).map((a) => {
    const cs = getComputedStyle(a);
    return { text: (a.textContent || '').trim(), color: cs.color, fontWeight: cs.fontWeight, bg: cs.backgroundColor };
  });
  out.path = location.pathname;
  return JSON.stringify(out, null, 1);
})()
