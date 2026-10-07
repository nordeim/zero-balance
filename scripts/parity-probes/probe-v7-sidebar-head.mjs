// probe-v7-sidebar-head.mjs — sidebar top block geometry (logo + icon + container)
(() => {
  const out = {};
  const logo = [...document.querySelectorAll("h2")].find(h => h.textContent?.trim() === "ZeroBalance");
  if (!logo) return JSON.stringify({ err: "no logo h2" });
  // walk up to the flex row that holds icon + logo
  let row = logo.parentElement;
  for (let i = 0; i < 4 && row && row !== document.body; i++) {
    if (row.className && /flex/.test(row.className) && row.querySelectorAll("svg").length > 0) break;
    row = row.parentElement;
  }
  const rowCs = getComputedStyle(row);
  out.row = {
    cls: (row.className || "").toString().slice(0, 100),
    display: rowCs.display, gap: rowCs.gap, padding: rowCs.padding,
    height: row.getBoundingClientRect().height,
    svgCount: row.querySelectorAll("svg").length,
  };
  const svg = row.querySelector("svg");
  if (svg) {
    const scs = getComputedStyle(svg);
    out.icon = { w: scs.width, h: scs.height, color: scs.color, tag: svg.getAttribute("class")?.slice(0, 60) };
  }
  const lcs = getComputedStyle(logo);
  out.logo = { size: lcs.fontSize, weight: lcs.fontWeight, color: lcs.color, lineH: lcs.lineHeight, letterSpacing: lcs.letterSpacing };
  // the container holding that row (the header cell of the rail)
  const cont = row.parentElement;
  const ccs = getComputedStyle(cont);
  out.container = {
    cls: (cont.className || "").toString().slice(0, 100),
    padding: ccs.padding, height: cont.getBoundingClientRect().height,
    borderBottom: ccs.borderBottomWidth + " " + ccs.borderBottomColor,
    display: ccs.display,
  };
  return JSON.stringify(out, null, 1);
})()
