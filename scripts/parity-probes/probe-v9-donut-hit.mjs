// probe-v9-donut-hit.mjs — empirically sample sector colors at clock positions around the donut
(() => {
  const out = { url: location.pathname };
  const wrap = document.querySelector(".recharts-wrapper");
  if (!wrap) return JSON.stringify({ err: "no wrapper" });
  const svg = wrap.querySelector("svg");
  const sr = svg.getBoundingClientRect();
  // pie center in svg coords (from the L x,y Z in sector paths) — read it live
  const firstPath = wrap.querySelector(".recharts-pie-sector path, path.recharts-pie-arc");
  const d = (firstPath?.getAttribute("d") || "");
  const cz = d.match(/L\s*([\d.]+),([\d.]+)/);
  const cx = cz ? parseFloat(cz[1]) : 209, cy = cz ? parseFloat(cz[2]) : 150;
  out.svgRect = { x: Math.round(sr.x), y: Math.round(sr.y), w: Math.round(sr.width), h: Math.round(sr.height) };
  out.centerSvg = { cx, cy };
  // page coords center
  const px = sr.x + (cx / 418) * sr.width, py = sr.y + (cy / 300) * sr.height;
  const R = (80 / 418) * sr.width; // 80px radius inside 100px pie
  // sample at clock hours: 12, 1:30, 3, 4:30, 6, 7:30, 9, 10:30 (screen-clockwise angle from 3 o'clock)
  const hours = { "12": 270, "1:30": 315, "3": 0, "4:30": 45, "6": 90, "7:30": 135, "9": 180, "10:30": 225 };
  out.samples = {};
  for (const [h, ang] of Object.entries(hours)) {
    const a = ang * Math.PI / 180;
    const x = px + R * Math.cos(a), y = py + R * Math.sin(a);
    const el = document.elementFromPoint(x, y);
    let fill = null;
    if (el && el.tagName === "path") fill = el.getAttribute("fill");
    else if (el) fill = `${el.tagName}:${(el.getAttribute("class") || "").slice(0, 30)}`;
    // fallback: check elementFromPoint at slightly different radius
    if (!fill || fill.startsWith("path") === false && !/^#/.test(fill || "")) {
      const x2 = px + (R - 15) * Math.cos(a), y2 = py + (R - 15) * Math.sin(a);
      const el2 = document.elementFromPoint(x2, y2);
      if (el2 && el2.tagName === "path" && /^#/.test(el2.getAttribute("fill") || "")) fill = el2.getAttribute("fill");
    }
    out.samples[h] = fill;
  }
  // map colors to names
  const names = { "#e07a3b": "Need(orange)", "#8fbc3f": "Savings(lime)", "#3b7ea1": "Want(blue)" };
  out.reading = Object.fromEntries(Object.entries(out.samples).map(([h, f]) => [h, names[f] || f]));
  return JSON.stringify(out, null, 1);
})()
