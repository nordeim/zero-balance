// pixel-diff-v84.mjs — pixel-level arbitration for the v84 screenshot
// diff on 07-add-item-modal.png (the committed set vs the regenerated
// shot). Locates the differing pixels' bounding box + row distribution
// so the diff class can be determined (DATE-text vs hover-state vs
// other). No dependencies beyond pngjs installed ad hoc.
import fs from "node:fs";
import { PNG } from "pngjs";

const a = PNG.sync.read(fs.readFileSync("/tmp/07-committed.png"));
const b = PNG.sync.read(fs.readFileSync(process.argv[2] || "docs/screenshots/07-add-item-modal.png"));
console.log("committed:", a.width + "x" + a.height, "new:", b.width + "x" + b.height);
if (a.width !== b.width || a.height !== b.height) {
  console.log("SIZE MISMATCH — different capture geometry");
  process.exit(0);
}
let minx = 1e9, miny = 1e9, maxx = -1, maxy = -1, count = 0;
const rows = new Map();
for (let y = 0; y < a.height; y++) {
  for (let x = 0; x < a.width; x++) {
    const i = (y * a.width + x) * 4;
    if (
      a.data[i] !== b.data[i] || a.data[i + 1] !== b.data[i + 1] ||
      a.data[i + 2] !== b.data[i + 2] || a.data[i + 3] !== b.data[i + 3]
    ) {
      count++;
      rows.set(y, (rows.get(y) || 0) + 1);
      if (x < minx) minx = x;
      if (x > maxx) maxx = x;
      if (y < miny) miny = y;
      if (y > maxy) maxy = y;
    }
  }
}
console.log("diff pixels:", count, "bbox:", `${minx},${miny} -> ${maxx},${maxy}`);
const sorted = [...rows.entries()].sort((p, q) => p[0] - q[0]);
console.log("diff rows (y:count):", sorted.slice(0, 40).map(([y, c]) => `${y}:${c}`).join(" "));
if (sorted.length > 40) console.log(`... ${sorted.length - 40} more rows`);
