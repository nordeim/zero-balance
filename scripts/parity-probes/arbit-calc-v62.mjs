// arbit-calc-v62.mjs — the 08-calculator diff arbitration, phase 2: the
// byte-diff bbox is x 2208-2265 / y 829-902 (1,596 of 5.18M pixels — a
// 57x73 region on the right edge of the dialog). The full-shot VLM said
// IDENTICAL (sub-perceptual at full scale); this crop-pair (3x upscaled)
// arbitrates the region per the v61 REGION-CROP pattern.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function main() {
  const zai = await ZAI.create();
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: `You are comparing two 3x-upscaled crops of the SAME region (the right edge of an expense-calculator dialog, around a line-item row's action area). Image 1 = the previous capture, image 2 = the fresh capture. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) if DIFFERENT, describe exactly what changed (text, icon, hover state, caret, antialiasing).`,
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/calc-prev-crop.png")}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/calc-new-crop.png")}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
}

main().catch((e) => {
  console.error("VLM crop arbitration failed:", e.message);
  process.exit(1);
});
