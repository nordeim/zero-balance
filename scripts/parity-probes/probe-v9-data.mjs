// probe-v9-data.mjs — reference data state sweep (drift check vs session-15 pins)
(() => {
  const out = { url: location.pathname };
  const main = document.querySelector("main");
  if (!main) return JSON.stringify({ err: "no main" });
  const hero = [...main.querySelectorAll("h3")].find(h => /NET ZERO GOAL/.test(h.textContent || ""))?.closest("div[class*='rounded']");
  if (hero) {
    const big = hero.querySelector("[class*='text-4xl'], [class*='text-3xl']");
    out.heroFigure = big ? big.textContent?.trim() : null;
    out.heroText = hero.textContent?.replace(/\s+/g, " ").slice(0, 260);
  }
  out.stats = [...main.querySelectorAll("h3")].filter(h => /Total Income|Total Savings|Total Expenses/.test(h.textContent || "")).map(h => {
    const card = h.closest("div.bg-white, div[class*='bg-white']");
    const amount = card?.querySelector(".text-3xl, .text-2xl, [class*='text-3xl']");
    return `${h.textContent?.trim()}: ${amount?.textContent?.trim()}`;
  });
  return JSON.stringify(out, null, 1);
})()
