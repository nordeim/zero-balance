// crop-left-v92.mjs — extract the LEFT band (x0..130) of the
// 16-item-details crop pair for the targeted single-image VLM read (the
// wide-region localization follow-up: the within-crop column-band
// analysis showed diff clusters at the left edge beyond the date band).
import fs from "node:fs";
import { PNG } from "pngjs";

const name = "16-item-details";
const a = PNG.sync.read(fs.readFileSync(`/tmp/v92crops/${name}-committed.png`));
const b = PNG.sync.read(fs.readFileSync(`/tmp/v92crops/${name}-new.png`));
const w = 130;
const h = a.height;
const crop = (img) => {
  const out = new PNG({ width: w, height: h });
  for (let y = 0; y < h; y++) {
    for (let x = 0; x < w; x++) {
      const si = (y * img.width + x) * 4;
      const di = (y * w + x) * 4;
      out.data[di] = img.data[si];
      out.data[di + 1] = img.data[si + 1];
      out.data[di + 2] = img.data[si + 2];
      out.data[di + 3] = img.data[si + 3];
    }
  }
  return out;
};
fs.writeFileSync(`/tmp/v92crops/${name}-left-committed.png`, PNG.sync.write(crop(a)));
fs.writeFileSync(`/tmp/v92crops/${name}-left-new.png`, PNG.sync.write(crop(b)));
console.log("left bands written");
