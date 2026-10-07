// probe-v7-mobile-items.mjs — mobile items-view geometry (header, filter, cards)
(() => {
  const out = { vw: innerWidth, url: location.pathname };
  out.scrollWidth = document.documentElement.scrollWidth;
  const main = document.querySelector("main");
  if (main) {
    const mcs = getComputedStyle(main);
    out.main = { w: Math.round(main.getBoundingClientRect().width), overflowX: mcs.overflowX, minW: mcs.minWidth };
  }
  // page header (h1 + count + Add button)
  const h1 = document.querySelector("h1");
  if (h1) {
    const hcs = getComputedStyle(h1);
    out.h1 = { text: h1.textContent?.trim().slice(0, 30), size: hcs.fontSize, w: Math.round(h1.getBoundingClientRect().width) };
  }
  // header row: h1 + add button side by side?
  const headerRow = h1?.parentElement;
  if (headerRow) out.headerRow = { cls: (headerRow.className || "").toString().slice(0, 70), kids: headerRow.children.length };
  // filter card geometry
  const search = document.querySelector('input[type="text"], input[placeholder*="Search" i], input[placeholder*="search" i]');
  if (search) {
    const scs = getComputedStyle(search);
    out.search = { placeholder: search.placeholder, w: Math.round(search.getBoundingClientRect().width), h: Math.round(search.getBoundingClientRect().height) };
  }
  // first item card
  const cards = [...document.querySelectorAll("main .bg-white.rounded-xl, main .bg-white.rounded-lg, main [class*='rounded-2xl'].bg-white")];
  const card = cards.find(c => c.querySelector("h3"));
  if (card) {
    out.firstCard = {
      cls: (card.className || "").toString().slice(0, 80),
      w: Math.round(card.getBoundingClientRect().width),
      heading: card.querySelector("h3")?.textContent?.trim().slice(0, 24),
    };
  }
  return JSON.stringify(out, null, 1);
})()
