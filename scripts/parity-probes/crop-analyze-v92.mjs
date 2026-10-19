// crop-analyze-v92.mjs — within-crop diff localization for the two
// wide-region files (08-calculator, 16-item-details): splits each crop
// pair's diff by column band so the DATE-TEXT-ONLY vs NOISE vs LAYOUT
// classes can be read off the horizontal distribution.
import fs from "node:fs";
import { PNG } from "pngjs";

const FILES = ["08-calculator", "16-item-details"];

for (const name of FILES) {
  const a = PNG.sync.read(fs.readFileSync(`/tmp/v92crops/${name}-committed.png`));
  const b = PNG.sync.read(fs.readFileSync(`/tmp/v92crops/${name}-new.png`));
  const diffs = [];
  for (let y = 0; y < a.height; y++) {
    for (let x = 0; x < a.width; x++) {
      const i = (y * a.width + x) * 4;
      if (
        a.data[i] !== b.data[i] || a.data[i + 1] !== b.data[i + 1] ||
        a.data[i + 2] !== b.data[i + 2] || a.data[i + 3] !== b.data[i + 3]
      ) {
        diffs.push({ x, y, d: [a.data[i], a.data[i + 1], a.data[i + 2]] });
      }
    }
  }
  console.log(`===== ${name}: ${diffs.length} diff px in crop ${a.width}x${a.height} =====`);
  // column bands of 50px
  const bands = new Map();
  for (const p of diffs) {
    const band = Math.floor(p.x / 50) * 50;
    bands.set(band, (bands.get(band) || 0) + 1);
  }
  console.log(
    "col-bands(50px): " +
      [...bands.entries()].sort((u, v) => u[0] - v[0]).map(([k, v]) => `x${k}:${v}`).join(" "),
  );
  // the max channel delta across all diff pixels (the noise class check)
  let maxDelta = 0;
  let deltaCounts = new Map();
  for (const p of diffs) {
    const bIdx = (p.y * b.width + p.x) * 4;
    for (let c = 0; c < 3; c++) {
      const d = Math.abs(p.d[c] - b.data[bIdx + c]);
      if (d > 0) {
        maxDelta = Math.max(maxDelta, d);
        deltaCounts.set(d, (deltaCounts.get(d) || 0) + 1);
      }
    }
  }
  console.log(
    "channel deltas: " +
      [...deltaCounts.entries()].sort((u, v) => u[0] - v[0]).map(([k, v]) => `d${k}:${v}`).join(" ") +
      ` (max ${maxDelta})`,
  );
}
