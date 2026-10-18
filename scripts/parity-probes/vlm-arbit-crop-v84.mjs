// vlm-arbit-crop-v84.mjs — the v84 screenshot diff-crop arbitration (the
// v80 discipline: pixel-locate the diff, then VLM-read ONLY the crop).
// The 07-add-item-modal.png diff: 229 pixels in a 14x22 box — read both
// crops and classify the delta (DATE-text vs hover-state vs other).
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
            text:
              "These are two CROPS of the same region of a budget-app Add Item dialog screenshot (image 1 = the originally committed version, image 2 = a freshly regenerated version). The crops are centered on the only pixel-level difference between the two full screenshots: a small ~7x11 CSS-pixel region. Describe precisely what text or glyph each crop shows in that differing region and what changed between the two versions (e.g. a date digit, a placeholder character, a hover tint). Be concise and literal — read the exact characters you can see.",
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm84/crop-committed.png")}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm84/crop-regenerated.png")}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
}

main().catch((e) => {
  console.error("VLM arbitration failed:", e.message);
  process.exit(1);
});
