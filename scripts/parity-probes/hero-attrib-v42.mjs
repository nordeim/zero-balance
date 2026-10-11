// v42: attribute the +13px hero-grid height drift on the dashboard at
// 640x960 (ref firstSection h=664 vs clone 677). Robust selection: the
// leaf h3/h2/p/span whose exact text is the marker, then walk up to the
// rounded card. The donut: the largest svg in main (the recharts surface).
(() => {
  const leaf = (txt) =>
    [...document.querySelectorAll('h1,h2,h3,h4,p,span,div')].find(
      (e) => (e.textContent || '').trim() === txt && e.children.length === 0,
    );
  const cardOf = (el) => (el ? el.closest('div.rounded-2xl, [class*="rounded-2xl"]') : null);
  const goalH = leaf('NET ZERO GOAL');
  const goalCard = cardOf(goalH);
  const goalGrid = goalCard ? goalCard.parentElement : null;
  const bdH = [...document.querySelectorAll('h3,h2,p,span')].find(
    (e) => /Breakdown/i.test((e.textContent || '').trim()) && e.children.length === 0,
  );
  const bdCard = cardOf(bdH);
  const rect = (el) =>
    el ? { y: Math.round(el.getBoundingClientRect().y), h: Math.round(el.getBoundingClientRect().height) } : null;
  // The goal card's internal bands: the chip row (the h3's flex parent),
  // the allocation block, the balance row.
  const chipRow = goalH ? goalH.closest('div.flex') : null;
  const balanceP = leaf('Balance');
  const balanceRow = balanceP ? balanceP.parentElement : null;
  const figure = balanceP
    ? [...balanceP.parentElement.querySelectorAll('p')].find((p) => /-?\$/.test(p.textContent || ''))
    : null;
  // All svgs in main, sorted by area — the donut is the biggest.
  const svgs = [...document.querySelectorAll('main svg')].map((s) => {
    const r = s.getBoundingClientRect();
    return { w: Math.round(r.width), h: Math.round(r.height) };
  });
  const donut = svgs.sort((a, b) => b.w * b.h - a.w * a.h)[0] || null;
  // The goal card's direct children bands (the chip row / allocation /
  // balance rows) with their margins, for the internal rhythm.
  const bands = goalCard
    ? [...goalCard.querySelectorAll(':scope > div > div')].slice(0, 6).map((b) => {
        const r = b.getBoundingClientRect();
        const cs = getComputedStyle(b);
        return {
          h: Math.round(r.height),
          mb: cs.marginBottom,
          pb: cs.paddingBottom,
          pt: cs.paddingTop,
        };
      })
    : [];
  return JSON.stringify({
    path: location.pathname,
    goalCard: rect(goalCard),
    goalGrid: goalGrid
      ? {
          gap: getComputedStyle(goalGrid).gap,
          h: Math.round(goalGrid.getBoundingClientRect().height),
          cols: getComputedStyle(goalGrid).gridTemplateColumns,
        }
      : null,
    breakdownCard: rect(bdCard),
    chipRow: rect(chipRow),
    balanceRow: rect(balanceRow),
    figure: figure
      ? { font: getComputedStyle(figure).fontSize, h: Math.round(figure.getBoundingClientRect().height) }
      : null,
    donut,
    goalBands: bands,
  });
})()
