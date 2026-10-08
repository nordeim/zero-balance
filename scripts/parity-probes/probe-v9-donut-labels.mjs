// probe-v9-donut-labels.mjs — donut percentage label styling at element depth
(() => {
  const out = { url: location.pathname };
  const wrap = document.querySelector(".recharts-wrapper");
  if (!wrap) return JSON.stringify({ err: "no recharts wrapper", hasSvg: !!document.querySelector("svg.recharts-surface") });
  out.wrap = { w: Math.round(wrap.getBoundingClientRect().width), h: Math.round(wrap.getBoundingClientRect().height) };
  // label texts — recharts renders <text> elements for labels
  const texts = [...wrap.querySelectorAll("text")];
  out.texts = texts.slice(0, 8).map(t => {
    const tcs = getComputedStyle(t);
    return {
      t: (t.textContent || "").trim().slice(0, 12),
      fill: t.getAttribute("fill") || tcs.fill,
      fs: tcs.fontSize, fw: tcs.fontWeight, ff: tcs.fontFamily.slice(0, 30),
      x: t.getAttribute("x"), y: t.getAttribute("y"),
      textAnchor: t.getAttribute("text-anchor"),
      opacity: tcs.opacity,
    };
  });
  // label lines (the little connector lines)?
  out.lines = [...wrap.querySelectorAll("line, .recharts-pie-label-line")].slice(0, 4).map(l => ({ stroke: l.getAttribute("stroke") || getComputedStyle(l).stroke, sw: l.getAttribute("stroke-width") }));
  // sectors with geometry
  const arcs = [...wrap.querySelectorAll(".recharts-pie-sector path, path.recharts-pie-arc")];
  out.sectors = arcs.slice(0, 5).map(p => ({
    fill: p.getAttribute("fill"),
    d: (p.getAttribute("d") || "").slice(0, 60),
    stroke: p.getAttribute("stroke"), sw: p.getAttribute("stroke-width"),
    opacity: getComputedStyle(p).opacity,
    transform: p.getAttribute("transform") || getComputedStyle(p).transform,
  }));
  return JSON.stringify(out, null, 1);
})()
