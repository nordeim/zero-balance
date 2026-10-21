// diff-shots-v103-bands.mjs — the row-band decomposition of the v103
// screenshot deltas: for each modified shot, group the diff pixels into
// horizontal bands (rows containing diff pixels, merged across <=4px
// gaps). The DATE-class expectation: each band is a TEXT-row band
// (~19px tall at 2x — one glyph row), never a full-width structural band.
import { execSync } from "node:child_process";
import { createRequire } from "node:module";
import fs from "node:fs";
const require2 = createRequire("/tmp/pngtools/node_modules/");
const { PNG } = require2("pngjs");

const FILES = [
  "03-income",
  "04-expenses",
  "05-savings",
  "06-networth",
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
  const rows = [];
  for (let y = 0; y < a.height; y++) {
    let cnt = 0;
    for (let x = 0; x < a.width; x++) {
      const ia = (a.width * y + x) << 2;
      const ib = (b.width * y + x) << 2;
      if (
        a.data[ia] !== b.data[ib] ||
        a.data[ia + 1] !== b.data[ib + 1] ||
        a.data[ia + 2] !== b.data[ib + 2] ||
        a.data[ia + 3] !== b.data[ib + 3]
      )
        cnt++;
    }
    if (cnt > 0) rows.push({ y, cnt });
  }
  // merge rows into bands across <=4px gaps
  const bands = [];
  for (const r of rows) {
    const last = bands[bands.length - 1];
    if (last && r.y - last.yEnd <= 4) {
      last.yEnd = r.y;
      last.px += r.cnt;
    } else {
      bands.push({ yStart: r.y, yEnd: r.y, px: r.cnt });
    }
  }
  console.log(`${name}: ${bands.length} band(s)`);
  for (const bd of bands) {
    console.log(`  y ${bd.yStart}-${bd.yEnd} (h ${bd.yEnd - bd.yStart + 1}) — ${bd.px} px`);
  }
}
