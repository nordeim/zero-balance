// vlm-diff-read-v145.mjs — read the two diff-row crops and confirm the
// 07-add-item-modal.png difference is the date-input digit (the
// wall-clock class — todayIso() crossed midnight between the committed
// shot and this cycle's capture).
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
            text: "These are two crops of the same region of a budget-app dialog form (Image 1 = the older committed screenshot, Image 2 = the fresh capture). Report exactly what text differs between them — especially any date value. Be concise: state the field label(s) visible and the exact text values in each image.",
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/row-head.png")}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/row-fresh.png")}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
}

main().catch((e) => {
  console.error("VLM read failed:", e.message);
  process.exit(1);
});
