// probe-v9-dash.mjs — dashboard hero/stat-card/donut/guideline internals at computed depth (desktop 1280)
(() => {
  const out = { url: location.pathname, vw: innerWidth };
  const main = document.querySelector("main");
  if (!main) return JSON.stringify({ err: "no main" });
  // hero card
  const hero = [...main.querySelectorAll("h3")].find(h => /NET ZERO GOAL/.test(h.textContent || ""))?.closest("div[class*='rounded']");
  if (hero) {
    const hr = hero.getBoundingClientRect();
    const hcs = getComputedStyle(hero);
    out.hero = { w: Math.round(hr.width), h: Math.round(hr.height), bg: hcs.backgroundImage || hcs.backgroundColor, radius: hcs.borderRadius, pad: hcs.padding, color: hcs.color };
    // allocation row: look for the progress/percentage label
    const labels = [...hero.querySelectorAll("*")].filter(el => el.children.length === 0);
    out.heroLabels = labels.map(l => ({ t: (l.textContent || "").trim().slice(0, 42), fs: getComputedStyle(l).fontSize, fw: getComputedStyle(l).fontWeight, c: getComputedStyle(l).color })).filter(x => x.t).slice(0, 12);
    // progress bar?
    const bars = [...hero.querySelectorAll("div")].filter(d => { const g = getComputedStyle(d).backgroundImage; return g && g !== "none" && /linear|conic/.test(g) && d.getBoundingClientRect().height < 20; });
    out.heroBars = bars.map(b => { const br = b.getBoundingClientRect(); const bcs = getComputedStyle(b); return { w: Math.round(br.width), h: Math.round(br.height), bg: bcs.backgroundImage.slice(0, 90), radius: bcs.borderRadius }; }).slice(0, 4);
  }
  // stat cards
  out.statCards = [...main.querySelectorAll("h3")].filter(h => /Total Income|Total Savings|Total Expenses/.test(h.textContent || "")).map(h => {
    const card = h.closest("div.bg-white, div[class*='bg-white']");
    if (!card) return null;
    const cr = card.getBoundingClientRect();
    const ccs = getComputedStyle(card);
    const amt = card.querySelector(".text-3xl, .text-2xl, [class*='text-3xl']");
    const acs = amt ? getComputedStyle(amt) : null;
    return {
      title: (h.textContent || "").trim(),
      w: Math.round(cr.width), h: Math.round(cr.height), radius: ccs.borderRadius, border: ccs.borderColor, pad: ccs.padding,
      amount: amt ? { t: (amt.textContent || "").trim(), fs: acs.fontSize, fw: acs.fontWeight, c: acs.color } : null,
    };
  });
  // donut (recharts sector paths + center label + legend)
  const paths = [...main.querySelectorAll("path.recharts-pie-arc, .recharts-pie-sector path")];
  out.donutSectors = paths.slice(0, 4).map(p => {
    const pcs = getComputedStyle(p);
    const pr = p.getBoundingClientRect();
    return { fill: pcs.fill || p.getAttribute("fill"), stroke: pcs.stroke || p.getAttribute("stroke"), sw: pcs.strokeWidth || p.getAttribute("stroke-width"), w: Math.round(pr.width), h: Math.round(pr.height) };
  });
  // donut center label
  const donutWrap = document.querySelector(".recharts-wrapper")?.parentElement;
  if (donutWrap) {
    const centerTexts = [...donutWrap.querySelectorAll("*")].filter(el => el.children.length === 0 && (el.textContent || "").trim().match(/%|\$/));
    out.donutCenter = centerTexts.slice(0, 3).map(el => ({ t: (el.textContent || "").trim().slice(0, 20), fs: getComputedStyle(el).fontSize, fw: getComputedStyle(el).fontWeight, c: getComputedStyle(el).color }));
  }
  // guideline rows (50/30/20)
  const guide = [...main.querySelectorAll("*")].filter(el => el.children.length === 0 && /^50%|^30%|^20%/.test((el.textContent || "").trim()));
  out.guidelines = guide.slice(0, 3).map(el => {
    const row = el.closest("div");
    const rcs = row ? getComputedStyle(row) : null;
    return { t: (el.textContent || "").trim().slice(0, 30), rowText: (row?.textContent || "").replace(/\s+/g, " ").slice(0, 80), fs: getComputedStyle(el).fs, color: getComputedStyle(el).color, rowBorder: rcs?.borderBottomColor, rowPad: rcs?.padding };
  });
  return JSON.stringify(out, null, 1);
})()
