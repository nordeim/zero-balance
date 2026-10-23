// diff-shots-v105-rows.mjs — the fine-grained per-row histogram of the
// v105 screenshot deltas (NO band merging): for each flagged file, print
// every diff row's y + diff-pixel count, to decompose the wide bands into
// their constituent text rows.
import { execSync } from "node:child_process";
import { createRequire } from "node:module";
import fs from "node:fs";
const require2 = createRequire("/tmp/pngtools/node_modules/");
const { PNG } = require2("pngjs");

const FILES = [
  "08-calculator",
  "16-item-details",
];

for (const name of FILES) {
  const headBuf = execSync(`git show HEAD:docs/screenshots/${name}.png`, {
    maxBuffer: 40 * 1024 * 1024,
  });
  const a = PNG.sync.read(headBuf);
  const b = PNG.sync.read(fs.readFileSync(`docs/screenshots/${name}.png`));
  if (a.width !== b.width || a.height !== b.height) {
    console.log(`${name}: SIZE MISMATCH — skipped`);
    continue;
  }
  console.log(`\n=== ${name} (${a.width}x${a.height}) per-row diff counts ===`);
  for (let y = 0; y < a.height; y++) {
    let count = 0;
    let minx = 1e9, maxx = -1;
    for (let x = 0; x < a.width; x++) {
      const ia = (a.width * y + x) << 2;
      const ib = (b.width * y + x) << 2;
      if (
        a.data[ia] !== b.data[ib] ||
        a.data[ia + 1] !== b.data[ib + 1] ||
        a.data[ia + 2] !== b.data[ib + 2] ||
        a.data[ia + 3] !== b.data[ib + 3]
      ) {
        count++;
        if (x < minx) minx = x;
        if (x > maxx) maxx = x;
      }
    }
    if (count > 0) {
      console.log(`  y=${y} count=${count} x=[${minx}..${maxx}]`);
    }
  }
}
