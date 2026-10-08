// probe-v9-donut-angles.mjs — exact sector angular spans + label-line presence
(() => {
  const out = { url: location.pathname };
  const wrap = document.querySelector(".recharts-wrapper");
  if (!wrap) return JSON.stringify({ err: "no wrapper" });
  const svg = wrap.querySelector("svg");
  const svgr = svg ? svg.getBoundingClientRect() : null;
  out.svg = svgr ? { w: Math.round(svgr.width), h: Math.round(svgr.height) } : null;
  // pie group transform (cx/cy)
  const pie = wrap.querySelector(".recharts-pie");
  if (pie) out.pieTransform = pie.getAttribute("transform");
  // sectors with FULL d
  const arcs = [...wrap.querySelectorAll(".recharts-pie-sector path, path.recharts-pie-arc")];
  const center = { cx: 209, cy: 150 }; // will refine from transform
  out.sectors = arcs.map(p => {
    const d = (p.getAttribute("d") || "").replace(/\s+/g, " ");
    // parse "M x,y A rx,ry,rot,laf,sf, x,y"
    const m = d.match(/^M\s*([\d.]+),([\d.]+)\s*A\s*([\d.]+),([\d.]+),[\d.]+,([01]),([01]),\s*([\d.]+),([\d.]+)/);
    let start = null, end = null, laf = null, sf = null;
    if (m) {
      start = [parseFloat(m[1]), parseFloat(m[2])];
      laf = m[5]; sf = m[6];
      // end point = last coordinate pair in the d
      const nums = d.match(/[\d.]+/g);
      end = [parseFloat(nums[nums.length - 2]), parseFloat(nums[nums.length - 1])];
    }
    const ang = (pt) => {
      const dx = pt[0] - center.cx, dy = pt[1] - center.cy;
      let a = Math.atan2(dy, dx) * 180 / Math.PI; // screen coords, y down
      return a;
    };
    return {
      fill: p.getAttribute("fill"),
      d: d.slice(0, 110),
      startPt: start, endPt: end,
      startAng: start ? Math.round(ang(start) * 10) / 10 : null,
      endAng: end ? Math.round(ang(end) * 10) / 10 : null,
      laf, sf,
    };
  });
  // label lines (recharts labelLine)
  const ll = [...wrap.querySelectorAll(".recharts-pie-label-line, line.recharts-pie-label-line")];
  out.labelLineCount = ll.length;
  out.labelLines = ll.slice(0, 4).map(l => ({ stroke: l.getAttribute("stroke"), cls: (l.getAttribute("class") || "").slice(0, 50), d: (l.getAttribute("d") || (l.getAttribute("x1") || "") + "," + (l.getAttribute("y1") || "")).slice(0, 60) }));
  // any line at all
  const anyLine = [...wrap.querySelectorAll("line")];
  out.allLines = anyLine.map(l => ({ stroke: l.getAttribute("stroke"), cls: (l.getAttribute("class") || "").slice(0, 40) })).slice(0, 5);
  // legend order (spending breakdown)
  const legendRegion = [...document.querySelectorAll("main h3")].find(h => /Spending Breakdown|Breakdown/i.test(h.textContent || ""))?.closest("div");
  if (legendRegion) {
    out.legendText = (legendRegion.textContent || "").replace(/\s+/g, " ").slice(0, 200);
  }
  return JSON.stringify(out, null, 1);
})()
