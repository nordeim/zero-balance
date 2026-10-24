// Crop the 07 delta band (rows 931-952) from BOTH the committed HEAD set
// and the regenerated set — side-by-side crops for the VLM read: what text
// actually changed in the flagged band.
import { execSync } from "node:child_process";
import { createRequire } from "node:module";
import fs from "node:fs";
const require2 = createRequire("/tmp/pngtools/node_modules/");
const { PNG } = require2("pngjs");

fs.mkdirSync("/tmp/v109crops", { recursive: true });
const y0 = 900, y1 = 980, x0 = 900, x1 = 2000; // generous context around 931-952
const headBuf = execSync("git show HEAD:docs/screenshots/07-add-item-modal.png", {
  maxBuffer: 40 * 1024 * 1024,
});
const a = PNG.sync.read(headBuf);
const b = PNG.sync.read(fs.readFileSync("docs/screenshots/07-add-item-modal.png"));
for (const [tag, img] of [["head", a], ["new", b]]) {
  const w = x1 - x0, h = y1 - y0;
  const out = new PNG({ width: w, height: h });
  PNG.bitblt(img, out, x0, y0, w, h, 0, 0);
  out.pack().pipe(fs.createWriteStream(`/tmp/v109crops/07-band-${tag}.png`));
  console.log(`cropped 07 band -> ${tag}`);
}
