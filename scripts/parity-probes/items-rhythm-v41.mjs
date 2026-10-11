// v41: the items-view page's vertical rhythm (measured on /income) — the
// page header row→filter card gap (the v20 G1 mb-8 pin) and the filter
// card→grid gap (the mb-6 at items-view.tsx:167). Checks the same
// vertical-rhythm drift class the net-worth audit found (ref 32 vs clone
// 24 on the net-worth header→card gap).
(() => {
  const h1 = [...document.querySelectorAll('main h1')].find(
    (h) => (h.textContent || '').trim() === 'Income',
  );
  if (!h1) return JSON.stringify({ error: 'NO H1' });
  // The page header row: the flex row containing the h1 block + the Add button.
  const headerRow = h1.closest('div.mb-\\8, div[class*="mb-8"]') || h1.parentElement.parentElement;
  const hrr = headerRow ? headerRow.getBoundingClientRect() : null;
  // The filter card: the white rounded-2xl card with the search input.
  const search = document.querySelector('input[type="search"], input[placeholder*="earch" i]');
  const filterCard = search ? search.closest('div.rounded-2xl') : null;
  const fcr = filterCard ? filterCard.getBoundingClientRect() : null;
  // The card grid: the first grid below the filter card.
  const grid = [...document.querySelectorAll('main [class*="grid"]')].find(
    (g) => fcr && g.getBoundingClientRect().y > fcr.bottom + 4 && (g.className || '').toString().match(/grid-cols/),
  );
  const gr = grid ? grid.getBoundingClientRect() : null;
  return JSON.stringify(
    {
      headerRow: hrr ? { bottom: Math.round(hrr.bottom), mb: getComputedStyle(headerRow).marginBottom } : null,
      filterCard: fcr
        ? {
            y: Math.round(fcr.y),
            gapFromHeader: hrr ? Math.round(fcr.y - hrr.bottom) : null,
            mb: getComputedStyle(filterCard).marginBottom,
            h: Math.round(fcr.height),
          }
        : 'NOT FOUND',
      grid: gr ? { y: Math.round(gr.y), gapFromFilter: fcr ? Math.round(gr.y - fcr.bottom) : null } : null,
    },
    null,
    1,
  );
})()
