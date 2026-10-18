// crop-diff-v86.mjs — crop the v86 screenshot diff bands (the committed
// vs the regenerated shots) for the single-image VLM arbitration: each
// file's pixel-diff bbox padded by 8px, written as a crop pair under
// /tmp/v86crops/. The v84 crop precedent + the v85 single-image lesson.
import fs from "node:fs";
import { PNG } from "pngjs";

const FILES = [
  "03-income",
  "04-expenses",
  "05-savings",
  "06-networth",
  "08-calculator",
  "16-item-details",
];

fs.mkdirSync("/tmp/v86crops", { recursive: true });

for (const name of FILES) {
  const a = PNG.sync.read(fs.readFileSync(`/tmp/v86-committed-${name}.png`));
  const b = PNG.sync.read(fs.readFileSync(`docs/screenshots/${name}.png`));
  if (a.width !== b.width || a.height !== b.height) {
    console.log(`${name}: SIZE MISMATCH — skipped`);
    continue;
  }
  let minx = 1e9, miny = 1e9, maxx = -1, maxy = -1;
  for (let y = 0; y < a.height; y++) {
    for (let x = 0; x < a.width; x++) {
      const i = (y * a.width + x) * 4;
      if (
        a.data[i] !== b.data[i] || a.data[i + 1] !== b.data[i + 1] ||
        a.data[i + 2] !== b.data[i + 2] || a.data[i + 3] !== b.data[i + 3]
      ) {
        if (x < minx) minx = x;
        if (x > maxx) maxx = x;
        if (y < miny) miny = y;
        if (y > maxy) maxy = y;
      }
    }
  }
  if (maxx < 0) {
    console.log(`${name}: no diff`);
    continue;
  }
  const pad = 8;
  const x0 = Math.max(0, minx - pad);
  const y0 = Math.max(0, miny - pad);
  const x1 = Math.min(a.width - 1, maxx + pad);
  const y1 = Math.min(a.height - 1, maxy + pad);
  const w = x1 - x0 + 1;
  const h = y1 - y0 + 1;
  const crop = (src) => {
    const out = new PNG({ width: w, height: h });
    for (let y = 0; y < h; y++) {
      for (let x = 0; x < w; x++) {
        const si = ((y0 + y) * src.width + (x0 + x)) * 4;
        const di = (y * w + x) * 4;
        out.data[di] = src.data[si];
        out.data[di + 1] = src.data[si + 1];
        out.data[di + 2] = src.data[si + 2];
        out.data[di + 3] = src.data[si + 3];
      }
    }
    return out;
  };
  fs.writeFileSync(`/tmp/v86crops/${name}-committed.png`, PNG.sync.write(crop(a)));
  fs.writeFileSync(`/tmp/v86crops/${name}-new.png`, PNG.sync.write(crop(b)));
  console.log(`${name}: crop ${w}x${h} at (${x0},${y0}) written`);
}
