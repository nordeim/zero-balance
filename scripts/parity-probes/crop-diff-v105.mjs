// crop-diff-v105.mjs — crop the 08/16 diff regions from BOTH the committed
// (HEAD) and the regenerated sets, saving side-by-side crops for the VLM
// read: what text actually changed in the flagged bands.
import { execSync } from "node:child_process";
import { createRequire } from "node:module";
import fs from "node:fs";
const require2 = createRequire("/tmp/pngtools/node_modules/");
const { PNG } = require2("pngjs");

const JOBS = [
  // [name, x0, y0, x1, y1] (device px)
  ["08-calculator", 600, 790, 2350, 920],
  ["16-item-details", 600, 790, 2350, 920],
  ["16-item-details", 1150, 990, 1300, 1050],
];

fs.mkdirSync("/tmp/v105crops", { recursive: true });
for (const [name, x0, y0, x1, y1] of JOBS) {
  const headBuf = execSync(`git show HEAD:docs/screenshots/${name}.png`, {
    maxBuffer: 40 * 1024 * 1024,
  });
  const a = PNG.sync.read(headBuf);
  const b = PNG.sync.read(fs.readFileSync(`docs/screenshots/${name}.png`));
  for (const [tag, img] of [["head", a], ["new", b]]) {
    const w = x1 - x0, h = y1 - y0;
    const out = new PNG({ width: w, height: h });
    PNG.bitblt(img, out, x0, y0, w, h, 0, 0);
    out.pack().pipe(fs.createWriteStream(`/tmp/v105crops/${name}-${y0}-${tag}.png`));
  }
  console.log(`cropped ${name} y${y0}-${y1} -> head + new`);
}
