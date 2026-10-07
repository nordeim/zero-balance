// probe-v7-dash-sweep.mjs — broad dashboard structure sweep (hero, stats, donut, guidelines)
(() => {
  const out = { url: location.pathname };
  const main = document.querySelector("main");
  if (!main) return JSON.stringify({ err: "no main" });
  // h1 + subtitle
  const h1 = main.querySelector("h1");
  out.h1 = h1 ? { text: h1.textContent?.trim().slice(0, 30), size: getComputedStyle(h1).fontSize } : null;
  // quick action buttons (top of page)
  out.actionBtns = [...main.querySelectorAll("button")].slice(0, 4).map(b => {
    const cs = getComputedStyle(b);
    return {
      text: (b.textContent || "").trim().slice(0, 26),
      h: Math.round(b.getBoundingClientRect().height),
      bg: cs.backgroundColor, grad: cs.backgroundImage !== "none" ? cs.backgroundImage.slice(0, 70) : null,
      color: cs.color,
    };
  });
  // hero card (NET ZERO GOAL)
  const hero = [...main.querySelectorAll("h3")].find(h => /NET ZERO GOAL/.test(h.textContent || ""))?.closest("div[class*='rounded']");
  if (hero) {
    const hcs = getComputedStyle(hero);
    out.hero = {
      cls: (hero.className || "").toString().slice(0, 100),
      grad: hcs.backgroundImage.slice(0, 90), radius: hcs.borderRadius,
      pad: hcs.padding,
    };
    // status badge in hero
    const status = [...hero.querySelectorAll("span, div")].find(el => el.children.length === 0 && /Budget|NET ZERO/i.test(el.textContent || ""));
    if (status) out.heroStatus = { text: status.textContent?.trim(), color: getComputedStyle(status).color };
  }
  // stat cards row
  const statCards = [...main.querySelectorAll("h3")].filter(h => /Total Income|Total Savings|Total Expenses/.test(h.textContent || ""));
  out.statCards = statCards.map(h => {
    const card = h.closest("div.bg-white, div[class*='bg-white']");
    const amount = card?.querySelector(".text-3xl, .text-2xl, [class*='text-3xl']");
    return {
      label: h.textContent?.trim(),
      amount: amount?.textContent?.trim(),
      amountSize: amount ? getComputedStyle(amount).fontSize : null,
      cardW: card ? Math.round(card.getBoundingClientRect().width) : null,
    };
  });
  // donut card + legend order
  const legendItems = [...main.querySelectorAll("span, div")].filter(el => el.children.length <= 1 && /^(Savings|Want|Need)$/.test(el.textContent?.trim() || ""));
  out.legendOrder = legendItems.map(el => el.textContent?.trim());
  // guidelines rows
  const guide = [...main.querySelectorAll("div")].find(d => /50%.*Needs|Needs.*50%|50\/30\/20/i.test(d.textContent || "") && d.children.length > 1);
  out.guidelinesPresent = !!guide;
  return JSON.stringify(out, null, 1);
})()
