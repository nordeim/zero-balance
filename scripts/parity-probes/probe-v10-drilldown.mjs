// probe-v10-drilldown.mjs — expand Total Expenses section, measure drill-down rows
(() => {
  const out = {};
  // find the "Total Expenses" row button in the Net Zero Breakdown card
  const row = [...document.querySelectorAll("button")].find(b => (b.textContent || "").includes("Total Expenses"));
  if (!row) return JSON.stringify({ err: "no row" });
  const rr = row.getBoundingClientRect();
  out.collapsedRow = { w: Math.round(rr.width), h: Math.round(rr.height), fs: getComputedStyle(row).fontSize, fw: getComputedStyle(row).fontWeight, txt: (row.textContent || "").replace(/\s+/g, " ").slice(0, 40) };
  row.click();
  return JSON.stringify({ expanded: true, collapsedRow: out.collapsedRow });
})()
