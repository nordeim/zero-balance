// diff-shots-v105.mjs — the v105 screenshot byte-compare arbitration: the
// committed (HEAD) set vs the regenerated set, per-file pixel-diff bbox +
// diff-pixel count. Expected class: the fresh-seed DATE roll (the isoDate
// offsets shift forward when the db re-seeds on a later day than the
// committed set's capture) — every delta must localize to the date
// text regions (the card date footers / the form date field / the sheet
// fact rows), never to layout or chrome.
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

fs.mkdirSync("/tmp/v105shots", { recursive: true });

for (const name of FILES) {
  const headBuf = execSync(`git show HEAD:docs/screenshots/${name}.png`, {
    maxBuffer: 40 * 1024 * 1024,
  });
  fs.writeFileSync(`/tmp/v105shots/${name}-head.png`, headBuf);
  const a = PNG.sync.read(headBuf);
  const b = PNG.sync.read(fs.readFileSync(`docs/screenshots/${name}.png`));
  if (a.width !== b.width || a.height !== b.height) {
    console.log(`${name}: SIZE MISMATCH (${a.width}x${a.height} vs ${b.width}x${b.height})`);
    continue;
  }
  let minx = 1e9, miny = 1e9, maxx = -1, maxy = -1, count = 0;
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
        count++;
        if (x < minx) minx = x;
        if (x > maxx) maxx = x;
        if (y < miny) miny = y;
        if (y > maxy) maxy = y;
      }
    }
  }
  if (count === 0) {
    console.log(`${name}: byte-identical`);
  } else {
    const w = maxx - minx + 1;
    const h = maxy - miny + 1;
    console.log(
      `${name}: ${count} diff px — bbox x=${minx} y=${miny} w=${w} h=${h} (image ${a.width}x${a.height})`,
    );
  }
}
