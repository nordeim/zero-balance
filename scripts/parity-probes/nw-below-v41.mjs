// v41: the vertical gaps BELOW the net-worth summary card — the card→tabs
// gap and the tabs→grid gap, measured against the card's bottom on both
// sites. Completes the vertical-rhythm census for the mb-* parity audit.
(() => {
  const label = [...document.querySelectorAll('p, span, h2, div')].find(
    (e) => (e.textContent || '').trim() === 'Total Net Worth' && e.children.length === 0,
  );
  const card = label ? label.closest('div.rounded-2xl') : null;
  if (!card) return JSON.stringify({ error: 'NO CARD' });
  const cr = card.getBoundingClientRect();
  const cardCs = getComputedStyle(card);
  // The tabs list: the [role=tablist] (or the 2-col trigger grid).
  const tablist = document.querySelector('[role="tablist"]');
  const tl = tablist ? tablist.getBoundingClientRect() : null;
  // The first tab panel's card grid.
  const panel = document.querySelector('[role="tabpanel"]');
  const firstGrid = panel ? panel.querySelector('[class*="grid"]') : null;
  const fg = firstGrid ? firstGrid.getBoundingClientRect() : null;
  // The tablist's own margin context: its parent.
  return JSON.stringify(
    {
      cardBottom: Math.round(cr.bottom),
      cardMB: cardCs.marginBottom,
      tablist: tl
        ? {
            y: Math.round(tl.y),
            gapFromCard: Math.round(tl.y - cr.bottom),
            h: Math.round(tl.height),
            w: Math.round(tl.width),
          }
        : null,
      firstGrid: fg ? { y: Math.round(fg.y), gapFromTablist: tl ? Math.round(fg.y - tl.bottom) : null } : null,
    },
    null,
    1,
  );
})()
