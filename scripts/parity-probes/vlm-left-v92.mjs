// vlm-left-v92.mjs — the targeted single-image VLM reads of the
// 16-item-details LEFT band pair (the wide-region localization
// follow-up).
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function readCrop(path, label) {
  const zai = await ZAI.create();
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text:
              "This is a narrow vertical strip cropped from the LEFT EDGE of a dialog in a budget-planner app screenshot. " +
              "Report EXACTLY any text, borders, or chrome you can read. Be concise and literal.",
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(path)}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(`--- ${label} ---`);
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
}

await readCrop("/tmp/v92crops/16-item-details-left-committed.png", "LEFT COMMITTED");
await readCrop("/tmp/v92crops/16-item-details-left-new.png", "LEFT NEW");
