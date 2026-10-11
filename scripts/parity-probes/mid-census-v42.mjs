// v42: the MID viewport (640x960) census of the five non-networth routes
// (/, /dashboard, /income, /expenses, /savings) — the v41 lesson applied:
// an unmeasured VIEWPORT CLASS is as dangerous as an unmeasured surface.
// Measures the vertical stack (header -> main -> page-header row -> first
// section) + the section rhythm + the grid columns + the overflow.
// The h1: NOT inside the mobile top bar (header) — the PAGE title
// ("Budget Dashboard" / "Income" / ...). The content cap: the h1's
// max-w-* wrapper (the reference and the clone share the structure:
// cap.children = [page-header row, first band, second band, ...]).
(() => {
  const vw = window.innerWidth;
  const vh = window.innerHeight;
  const header = document.querySelector('header');
  const main = document.querySelector('main');
  const h1 = [...document.querySelectorAll('h1')]
    .filter((h) => !h.closest('header'))
    .find((h) => h.getBoundingClientRect().height > 0);
  const cap = h1 ? h1.closest('div[class*="max-w"]') : null;
  const capRow = h1 ? h1.closest('div.flex, div[class*="flex"]') : null;
  const headerRow =
    cap && cap.children.length > 0 ? cap.children[0] : capRow || null;
  const kids = cap ? [...cap.children] : [];
  const firstSection = kids[1] || null;
  const secondBand = kids[2] || null;
  const thirdBand = kids[3] || null;
  const hr = header ? header.getBoundingClientRect() : null;
  const mr = main ? main.getBoundingClientRect() : null;
  const hrr = headerRow ? headerRow.getBoundingClientRect() : null;
  const fsr = firstSection ? firstSection.getBoundingClientRect() : null;
  const mainCs = main ? getComputedStyle(main) : null;
  const rowCs = headerRow ? getComputedStyle(headerRow) : null;
  const fsCs = firstSection ? getComputedStyle(firstSection) : null;
  const band = (el) => {
    if (!el) return null;
    const r = el.getBoundingClientRect();
    const cs = getComputedStyle(el);
    return {
      y: Math.round(r.y),
      h: Math.round(r.height),
      mt: cs.marginTop,
      mb: cs.marginBottom,
      display: cs.display,
      cols: cs.display === 'grid' ? cs.gridTemplateColumns.split(' ').length : null,
      gap: cs.display === 'grid' ? cs.gap : null,
    };
  };
  return JSON.stringify({
    path: location.pathname,
    vw,
    vh,
    sw: document.documentElement.scrollWidth,
    header: hr ? { y: Math.round(hr.y), h: Math.round(hr.height) } : null,
    main: mr ? { y: Math.round(mr.y), pad: mainCs ? mainCs.padding : null } : null,
    h1: h1
      ? {
          text: (h1.textContent || '').trim().slice(0, 20),
          font: getComputedStyle(h1).fontSize,
          h: Math.round(h1.getBoundingClientRect().height),
        }
      : null,
    headerRow: hrr
      ? {
          y: Math.round(hrr.y),
          h: Math.round(hrr.height),
          bottom: Math.round(hrr.bottom),
          mb: rowCs ? rowCs.marginBottom : null,
          dir: rowCs ? rowCs.flexDirection : null,
        }
      : null,
    firstSection: band(firstSection),
    secondBand: band(secondBand),
    thirdBand: band(thirdBand),
    gapRowToFirst: hrr && fsr ? Math.round(fsr.y - hrr.bottom) : null,
    capW: cap ? Math.round(cap.getBoundingClientRect().width) : null,
  });
})()
