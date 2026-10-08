// probe-v9-donut-bbox.mjs — sector path bounding boxes + svg rect (true screen positions)
(() => {
  const out = { url: location.pathname };
  const wrap = document.querySelector(".recharts-wrapper");
  if (!wrap) return JSON.stringify({ err: "no wrapper" });
  const svg = wrap.querySelector("svg");
  const sr = svg.getBoundingClientRect();
  out.svgRect = { x: Math.round(sr.x), y: Math.round(sr.y), w: Math.round(sr.width), h: Math.round(sr.height) };
  const arcs = [...wrap.querySelectorAll(".recharts-pie-sector path, path.recharts-pie-arc")];
  out.sectorBoxes = arcs.map(p => {
    const r = p.getBoundingClientRect();
    return {
      fill: p.getAttribute("fill"),
      x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height),
      // bbox quadrant hints relative to svg rect
      relX: r.x - sr.x < sr.width / 2 ? "left" : "right",
      relY: r.y - sr.y < sr.height / 2 ? "top" : "bottom",
    };
  });
  // label text positions (real screen)
  out.labels = [...wrap.querySelectorAll("text")].slice(0, 4).map(t => {
    const r = t.getBoundingClientRect();
    return { t: (t.textContent || "").trim(), fill: t.getAttribute("fill"), x: Math.round(r.x), y: Math.round(r.y), relX: r.x - sr.x < sr.width / 2 ? "left" : "right", relY: r.y - sr.y < sr.height / 2 ? "top" : "bottom" };
  });
  // center via the path's L command in svg coords, converted with the viewBox if present
  out.viewBox = svg.getAttribute("viewBox");
  const firstPath = arcs[0];
  const d = (firstPath?.getAttribute("d") || "");
  const cz = d.match(/L\s*([\d.]+),([\d.]+)/);
  out.centerSvgCoords = cz ? [parseFloat(cz[1]), parseFloat(cz[2])] : null;
  return JSON.stringify(out, null, 1);
})()
