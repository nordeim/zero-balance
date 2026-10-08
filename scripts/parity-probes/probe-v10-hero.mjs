// probe-v10-hero.mjs — hero card figures, precisely targeted
(() => {
  const out = { url: location.pathname };
  // hero card: the card containing "NET ZERO GOAL"
  const cards = [...document.querySelectorAll("div")].filter(d => {
    const t = (d.textContent || "");
    return t.includes("NET ZERO GOAL") && d.querySelectorAll("div").length < 60;
  });
  const hero = cards.sort((a, b) => a.querySelectorAll("div").length - b.querySelectorAll("div").length)[0];
  if (hero) {
    const leaves = [...hero.querySelectorAll("*")].filter(el => el.children.length === 0 && (el.textContent || "").trim());
    out.heroLeaves = leaves.map(el => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return { t: (el.textContent || "").replace(/\s+/g, " ").trim().slice(0, 45), fs: cs.fontSize, fw: cs.fontWeight, color: cs.color, w: Math.round(r.width), h: Math.round(r.height) };
    }).filter(x => x.t).slice(0, 22);
    // status pill (Under Budget / NET ZERO / Over Budget)
    const status = leaves.find(el => /Under Budget|NET ZERO|Over Budget/i.test(el.textContent || ""));
    out.status = status ? { t: status.textContent.trim(), color: getComputedStyle(status).color, bg: getComputedStyle(status).backgroundColor, fs: getComputedStyle(status).fontSize, fw: getComputedStyle(status).fontWeight } : null;
  }
  // stat cards: Total Income / Total Savings / Total Expenses values
  const statVals = {};
  for (const name of ["Total Income", "Total Savings", "Total Expenses"]) {
    const h = [...document.querySelectorAll("h3, h2, p, span")].find(el => (el.textContent || "").trim() === name);
    if (h) {
      const card = h.closest("div");
      const val = [...(card || document).querySelectorAll("p, span, div")].filter(el => el.children.length === 0 && /^\$[\d,]+\.\d{2}$/.test((el.textContent || "").trim()))[0];
      const items = (card || document).textContent.match(/(\d+) items?/);
      statVals[name] = { val: val ? val.textContent.trim() : null, items: items ? items[1] : null };
    }
  }
  out.stats = statVals;
  return JSON.stringify(out, null, 1);
})()
