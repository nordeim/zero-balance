// diff-shots-v105-bands.mjs — the row-band decomposition of the v105
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
  "07-add-item-modal",
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
  const rows = new Set();
  for (let y = 0; y < a.height; y++) {
    for (let x = 0; x < a.width; x++) {
      const ia = (a.width * y + x) << 2;
      const ib = (b.width * y + x) << 2;
      if (
        a.data[ia] !== b.data[ib] ||
        a.data[ia + 1] !== b.data[ib + 1] ||
        a.data[ia + 2] !== b.data[ib + 2] ||
        a.data[ia + 3] !== b.data[ib + 3]
      ) {
        rows.add(y);
      }
    }
  }
  if (rows.size === 0) {
    console.log(`${name}: byte-identical`);
    continue;
  }
  // merge rows into bands across <=4px gaps
  const sorted = [...rows].sort((p, q) => p - q);
  const bands = [];
  let start = sorted[0], prev = sorted[0];
  for (const y of sorted.slice(1)) {
    if (y - prev <= 4) {
      prev = y;
    } else {
      bands.push([start, prev]);
      start = y;
      prev = y;
    }
  }
  bands.push([start, prev]);
  const bandSummary = bands
    .map(([y0, y1]) => `y${y0}-${y1}(${y1 - y0 + 1}px)`)
    .join(" ");
  const maxBandH = Math.max(...bands.map(([y0, y1]) => y1 - y0 + 1));
  const verdict = maxBandH <= 24 ? "TEXT-ROW BANDS (the DATE class)" : "STRUCTURAL BAND — INVESTIGATE";
  console.log(`${name}: ${bands.length} band(s) — ${bandSummary} — maxBandH ${maxBandH}px — ${verdict}`);
}
