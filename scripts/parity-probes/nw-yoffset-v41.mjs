// v41: attribute the 8px y-offset between the reference's and the clone's
// net-worth summary cards at 640x960 (ref y=169, clone y=161). Measures the
// vertical stack above the card: the mobile top bar (header), the page
// header row (chip + h1 + subtitle), and the header→card gap.
(() => {
  const vh = window.innerHeight;
  const header = document.querySelector('header');
  const h1 = [...document.querySelectorAll('main h1')].find(
    (h) => (h.textContent || '').trim() === 'Net Worth',
  );
  const label = [...document.querySelectorAll('p, span, h2, div')].find(
    (e) => (e.textContent || '').trim() === 'Total Net Worth' && e.children.length === 0,
  );
  const card = label ? label.closest('div.rounded-2xl') : null;
  const hr = header ? header.getBoundingClientRect() : null;
  const main = document.querySelector('main');
  const mr = main ? main.getBoundingClientRect() : null;
  // The page-header row: the chip's flex parent (gap-3 row).
  const chipRow = h1 ? h1.parentElement.parentElement : null;
  const crr = chipRow ? chipRow.getBoundingClientRect() : null;
  const h1r = h1 ? h1.getBoundingClientRect() : null;
  const subtitle = h1 ? h1.parentElement.querySelector('p') : null;
  const sr = subtitle ? subtitle.getBoundingClientRect() : null;
  const cr = card ? card.getBoundingClientRect() : null;
  const mainCs = main ? getComputedStyle(main) : null;
  return JSON.stringify(
    {
      vh,
      header: hr ? { y: Math.round(hr.y), h: Math.round(hr.height), bottom: Math.round(hr.bottom) } : null,
      main: mr ? { y: Math.round(mr.y), pad: mainCs ? mainCs.padding : null } : null,
      chipRow: crr ? { y: Math.round(crr.y), h: Math.round(crr.height), bottom: Math.round(crr.bottom) } : null,
      h1: h1r ? { y: Math.round(h1r.y), h: Math.round(h1r.height), font: getComputedStyle(h1).fontSize } : null,
      subtitle: sr ? { bottom: Math.round(sr.bottom), h: Math.round(sr.height) } : null,
      card: cr ? { y: Math.round(cr.y) } : null,
      gapHeaderToCard: crr && cr ? Math.round(cr.y - crr.bottom) : null,
    },
    null,
    1,
  );
})()
