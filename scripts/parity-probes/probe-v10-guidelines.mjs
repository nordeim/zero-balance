// probe-v10-guidelines.mjs — Budget Guidelines card: row structure + any bars/indicators
(() => {
  const out = {};
  const card = [...document.querySelectorAll("div")].find(d => {
    const t = (d.textContent || "");
    return t.includes("Budget Guidelines") && t.includes("Needs ~50%") && d.querySelectorAll("div").length < 80;
  });
  if (!card) return JSON.stringify({ err: "no card" });
  // rows: the three guideline groups
  const groups = ["Needs", "Wants", "Savings"].map(name => {
    const h = [...card.querySelectorAll("h4, h3, p, span, div")].find(el => (el.textContent || "").trim().startsWith(name) && (el.textContent || "").includes("~"));
    if (!h) return { name, err: "not found" };
    const row = h.parentElement;
    const r = row.getBoundingClientRect();
    const cs = getComputedStyle(row);
    return { name, rowH: Math.round(r.height), pad: cs.padding, gap: cs.gap, flexDir: cs.flexDirection };
  });
  out.groups = groups;
  // any bar/track/indicator elements
  const bars = [...card.querySelectorAll("div")].filter(el => { const cs = getComputedStyle(el); const r = el.getBoundingClientRect(); return (r.height >= 4 && r.height <= 16 && r.width > 40) && (cs.backgroundColor !== "rgba(0, 0, 0, 0)" || cs.backgroundImage !== "none"); });
  out.bars = bars.slice(0, 5).map(el => { const cs = getComputedStyle(el); const r = el.getBoundingClientRect(); return { w: Math.round(r.width), h: Math.round(r.height), bg: cs.backgroundColor.slice(0, 25), bgImg: cs.backgroundImage.slice(0, 30), radius: cs.borderRadius }; });
  // guideline value typography
  const leaf = [...card.querySelectorAll("span, p, div")].filter(el => el.children.length === 0 && /~(50|30|20)%/.test(el.textContent || ""));
  out.percLeaves = leaf.map(el => { const cs = getComputedStyle(el); return { t: (el.textContent || "").trim(), fs: cs.fontSize, fw: cs.fontWeight, color: cs.color }; });
  return JSON.stringify(out, null, 1);
})()
