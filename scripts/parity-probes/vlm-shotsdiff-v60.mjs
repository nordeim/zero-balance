// vlm-shotsdiff-v60.mjs — the v60 screenshot-regeneration arbitration (the
// v59 vlm-shotsdiff pattern): ONE of the 16 regenerated screenshots diffed
// (07-add-item-modal.png, +48 bytes — NOT the seed-date class). This VLM
// pairwise old-vs-new identifies the diff class; per the v43 rule the
// verdict must be a DOM/perception class before the diff is accepted.
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
            text: "You are comparing two screenshots of the SAME app's 'Add Item' modal (image 1 = the previous capture, image 2 = the fresh capture of the same build). They should be identical. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) if DIFFERENT, list every visible difference precisely (text, position, color, focus rings, dropdowns, shadows, caret position), however small.",
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/old-07.png")}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("docs/screenshots/07-add-item-modal.png")}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
}

main().catch((e) => {
  console.error("VLM shotsdiff failed:", e.message);
  process.exit(1);
});
