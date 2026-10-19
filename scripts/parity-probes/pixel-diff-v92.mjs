// pixel-diff-v92.mjs — pixel-level arbitration for the v92 screenshot
// diffs (the committed set vs the regenerated shots, the fresh-seed
// DATE-class candidates: 03-income / 04-expenses / 05-savings /
// 06-networth / 07-add-item-modal / 08-calculator / 16-item-details —
// the v80/v86 fresh-seed pattern's six files + 07). Locates each
// differing file's pixel count + bounding box + row distribution so the
// diff class can be determined (DATE-text vs hover-state vs other).
// pngjs installed ad hoc.
import fs from "node:fs";
import { PNG } from "pngjs";

const FILES = [
  "03-income",
  "04-expenses",
  "05-savings",
  "06-networth",
  "07-add-item-modal",
  "08-calculator",
  "16-item-details",
];

for (const name of FILES) {
  const a = PNG.sync.read(fs.readFileSync(`/tmp/shots-ref/${name}.png`));
  const b = PNG.sync.read(fs.readFileSync(`docs/screenshots/${name}.png`));
  if (a.width !== b.width || a.height !== b.height) {
    console.log(`${name}: SIZE MISMATCH ${a.width}x${a.height} vs ${b.width}x${b.height}`);
    continue;
  }
  let minx = 1e9, miny = 1e9, maxx = -1, maxy = -1, count = 0;
  const rows = new Map();
  const cols = new Map();
  for (let y = 0; y < a.height; y++) {
    for (let x = 0; x < a.width; x++) {
      const i = (y * a.width + x) * 4;
      if (
        a.data[i] !== b.data[i] || a.data[i + 1] !== b.data[i + 1] ||
        a.data[i + 2] !== b.data[i + 2] || a.data[i + 3] !== b.data[i + 3]
      ) {
        count++;
        rows.set(y, (rows.get(y) || 0) + 1);
        cols.set(x, (cols.get(x) || 0) + 1);
        if (x < minx) minx = x;
        if (x > maxx) maxx = x;
        if (y < miny) miny = y;
        if (y > maxy) maxy = y;
      }
    }
  }
  if (count === 0) {
    console.log(`${name}: IDENTICAL`);
    continue;
  }
  const rowDist = [...rows.entries()]
    .sort((r1, r2) => r1[0] - r2[0])
    .map(([y, c]) => `y${y}:${c}`)
    .join(" ");
  const colDist = [...cols.entries()]
    .sort((c1, c2) => c1[0] - c2[0])
    .map(([x, c]) => `x${x}:${c}`)
    .join(" ");
  console.log(`${name}: ${count} px differ, bbox x[${minx}..${maxx}] y[${miny}..${maxy}]`);
  console.log(`  rows: ${rowDist.slice(0, 400)}`);
  console.log(`  cols: ${colDist.slice(0, 400)}`);
}
