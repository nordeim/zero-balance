// probe-v8-data.mjs — reference data state sweep (items/amounts per section)
(() => {
  const out = { url: location.pathname };
  const main = document.querySelector("main");
  if (!main) return JSON.stringify({ err: "no main" });
  // hero net figure + allocation
  const hero = [...main.querySelectorAll("h3")].find(h => /NET ZERO GOAL/.test(h.textContent || ""))?.closest("div[class*='rounded']");
  if (hero) {
    const big = hero.querySelector("[class*='text-4xl'], [class*='text-3xl']");
    out.heroFigure = big ? { text: big.textContent?.trim() } : null;
    const pct = [...hero.querySelectorAll("*")].find(el => el.children.length === 0 && /\d+(\.\d+)?%/.test(el.textContent || "") && /alloc|Income/i.test(hero.textContent || ""));
    out.heroPct = pct ? pct.textContent?.trim() : null;
    out.heroText = hero.textContent?.replace(/\s+/g, " ").slice(0, 220);
  }
  // stat cards
  out.stats = [...main.querySelectorAll("h3")].filter(h => /Total Income|Total Savings|Total Expenses/.test(h.textContent || "")).map(h => {
    const card = h.closest("div.bg-white, div[class*='bg-white']");
    const amount = card?.querySelector(".text-3xl, .text-2xl, [class*='text-3xl']");
    return `${h.textContent?.trim()}: ${amount?.textContent?.trim()}`;
  });
  // donut legend
  out.legend = [...main.querySelectorAll("span, div")].filter(el => el.children.length <= 1 && /^(Savings|Want|Need)$/.test(el.textContent?.trim() || "")).map(el => el.textContent?.trim());
  return JSON.stringify(out, null, 1);
})()
