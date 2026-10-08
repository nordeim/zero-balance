// probe-v9-stat-cards.mjs — stat cards + guideline rows at computed depth
(() => {
  const out = { url: location.pathname, vw: innerWidth };
  const main = document.querySelector("main");
  if (!main) return JSON.stringify({ err: "no main" });
  // stat cards: climb from the "Total Income" h3
  out.stats = ["Total Income", "Total Savings", "Total Expenses"].map((title) => {
    const h = [...main.querySelectorAll("h3")].find(x => (x.textContent || "").trim() === title);
    if (!h) return { title, err: "no h3" };
    // card = the ancestor with border + rounded (the clickable stat card)
    let card = h.parentElement;
    for (let i = 0; i < 6 && card; i++) {
      const cs = getComputedStyle(card);
      if (parseInt(cs.borderRadius) >= 8 && cs.backgroundColor !== "rgba(0, 0, 0, 0)" && card !== main) break;
      card = card.parentElement;
    }
    if (!card) return { title, err: "no card" };
    const cr = card.getBoundingClientRect();
    const ccs = getComputedStyle(card);
    const amt = [...card.querySelectorAll("*")].find(el => el.children.length === 0 && /^\$[\d,]+\.\d\d$/.test((el.textContent || "").trim()));
    const acs = amt ? getComputedStyle(amt) : null;
    const label = [...card.querySelectorAll("p, span")].find(el => el.children.length === 0 && /per month|monthly/i.test(el.textContent || ""));
    const chev = card.querySelector("svg[class*=chevron], svg.lucide-chevron-right");
    return {
      title,
      w: Math.round(cr.width), h: Math.round(cr.height),
      bg: ccs.backgroundColor, border: ccs.borderColor, radius: ccs.borderRadius, pad: ccs.padding, shadow: (ccs.boxShadow || "").slice(0, 50),
      amount: amt ? { t: amt.textContent?.trim(), fs: acs.fontSize, fw: acs.fontWeight, c: acs.color } : null,
      sub: label ? { t: label.textContent?.trim(), fs: getComputedStyle(label).fontSize, c: getComputedStyle(label).color } : null,
      chevron: chev ? { w: Math.round(chev.getBoundingClientRect().width), c: getComputedStyle(chev).color } : null,
      text: (card.textContent || "").replace(/\s+/g, " ").slice(0, 60),
    };
  });
  // guideline rows (50/30/20)
  const guide = [...main.querySelectorAll("*")].filter(el => el.children.length === 0 && /^(50|30|20)%/.test((el.textContent || "").trim()));
  out.guidelines = guide.slice(0, 3).map(el => {
    const row = el.closest("div");
    const rcs = row ? getComputedStyle(row) : null;
    return {
      pct: (el.textContent || "").trim(),
      rowText: (row?.textContent || "").replace(/\s+/g, " ").slice(0, 90),
      pctFs: getComputedStyle(el).fontSize, pctFw: getComputedStyle(el).fontWeight, pctColor: getComputedStyle(el).color,
      rowBorderB: rcs ? rcs.borderBottomColor + " " + rcs.borderBottomWidth : null, rowPad: rcs ? rcs.padding : null,
    };
  });
  return JSON.stringify(out, null, 1);
})()
