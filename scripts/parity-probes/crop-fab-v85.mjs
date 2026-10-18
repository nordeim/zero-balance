// crop-fab-v85.mjs — crop the bottom-right corner regions of the v85
// income full-page pair (ref vs clone) so the "Edit with Base44" FAB claim
// can be pixel-arbitrated: the FAB (if present) is a dark rounded button
// pinned at the viewport's bottom-right. Full-page screenshots pin fixed
// elements at the FIRST screenful's bottom-right (the capture window's
// viewport height = 800), so crop BOTH the first-viewport bottom-right AND
// the document-bottom right of each image.
import fs from "node:fs";
import { PNG } from "pngjs";

function cropRightBottom(src, dst, vw = 1280, vh = 800) {
  const buf = fs.readFileSync(src);
  const png = PNG.sync.read(buf);
  const { width, height } = png;
  const cropW = Math.min(340, width);
  // first-viewport bottom-right (fixed chrome renders here in full-page shots)
  const y1 = Math.min(vh, height) - 100;
  const x1 = width - cropW;
  const out = new PNG({ width: cropW, height: 100 });
  for (let y = 0; y < 100; y++) {
    for (let x = 0; x < cropW; x++) {
      const si = (y1 + y) * width + (x1 + x);
      const di = y * cropW + x;
      out.data[di * 4] = png.data[si * 4];
      out.data[di * 4 + 1] = png.data[si * 4 + 1];
      out.data[di * 4 + 2] = png.data[si * 4 + 2];
      out.data[di * 4 + 3] = png.data[si * 4 + 3];
    }
  }
  fs.writeFileSync(dst, PNG.sync.write(out));
  // also report whether ANY near-black pixel cluster exists in the crop
  let dark = 0;
  for (let i = 0; i < out.data.length; i += 4) {
    const [r, g, b] = [out.data[i], out.data[i + 1], out.data[i + 2]];
    if (r < 40 && g < 40 && b < 40) dark++;
  }
  console.log(`${dst}: doc ${width}x${height}, dark-px in corner crop: ${dark}`);
}

cropRightBottom("/tmp/vlm85/ref-income-full.png", "/tmp/vlm85/ref-income-br.png");
cropRightBottom("/tmp/vlm85/clone-income-full.png", "/tmp/vlm85/clone-income-br.png");
