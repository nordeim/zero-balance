// probe-v8-page.mjs — per-page mobile geometry sweep (overflow, header, first content row)
(() => {
  const out = { url: location.pathname, sw: document.documentElement.scrollWidth, vw: innerWidth };
  const main = document.querySelector("main");
  if (!main) return JSON.stringify({ err: "no main" });
  // page h1 (inside main content)
  const h1 = main.querySelector("h1");
  out.h1 = h1 ? { text: h1.textContent?.trim().slice(0, 30), size: getComputedStyle(h1).fontSize, weight: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color } : null;
  // item cards count (seeded cards)
  const cards = [...main.querySelectorAll("h3")].map(h => h.textContent?.trim().slice(0, 24)).filter(t => t && !/NET ZERO|Total|SPENDING|GUIDELINE/i.test(t));
  out.cardHeadings = cards.slice(0, 10);
  // count chips ("N items")
  out.countTexts = [...main.querySelectorAll("span,div")].filter(el => el.children.length === 0 && /^\d+\s+items?$/.test(el.textContent?.trim() || "")).map(el => el.textContent?.trim());
  return JSON.stringify(out, null, 1);
})()
