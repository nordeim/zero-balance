// crop-diff-v84.mjs — crop both versions of 07-add-item-modal.png around
// the diff bbox (plus margin) and save the pair for VLM arbitration of
// the DIFF CROP ONLY (the v80 discipline — never a full-page verdict).
import fs from "node:fs";
import { PNG } from "pngjs";

const a = PNG.sync.read(fs.readFileSync("/tmp/07-committed.png")); // committed
const b = PNG.sync.read(fs.readFileSync("docs/screenshots/07-add-item-modal.png")); // regenerated
const M = 80; // margin around the diff bbox (device px)
const bbox = { x1: 1552, y1: 931, x2: 1566, y2: 952 };
const x1 = Math.max(0, bbox.x1 - M), y1 = Math.max(0, bbox.y1 - M);
const x2 = Math.min(a.width, bbox.x2 + M), y2 = Math.min(a.height, bbox.y2 + M);
const w = x2 - x1, h = y2 - y1;

function crop(src) {
  const out = new PNG({ width: w, height: h });
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      const si = ((y1 + y) * src.width + (x1 + x)) * 4;
      const di = (y * w + x) * 4;
      out.data[di] = src.data[si];
      out.data[di + 1] = src.data[si + 1];
      out.data[di + 2] = src.data[si + 2];
      out.data[di + 3] = src.data[si + 3];
    }
  }
  return out;
}
crop(a).pack().pipe(fs.createWriteStream("/tmp/vlm84/crop-committed.png"));
crop(b).pack().pipe(fs.createWriteStream("/tmp/vlm84/crop-regenerated.png"));
console.log(`crops saved: ${w}x${h} @ (${x1},${y1}) -> /tmp/vlm84/crop-committed.png + crop-regenerated.png`);
