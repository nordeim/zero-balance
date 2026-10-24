// VLM-read the v110 screenshot delta crops: what actually changed in the
// flagged bands (head vs new side by side per crop pair).
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");
const PAIRS = [
  ["08-calculator-y790", "the calculator dialog band"],
  ["16-item-details-y790", "the item-details band 1"],
  ["16-item-details-y990", "the item-details band 2"],
  ["03-income-y790", "the income card band"],
];

const zai = await ZAI.create();
for (const [name, label] of PAIRS) {
  const completion = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text:
              "Two crops of the SAME region of a screenshot, taken a day apart " +
              "(Image 1 = the older committed set, Image 2 = the regenerated set). " +
              "Report EXACTLY what text or visual element differs between them. " +
              "Be precise about any dates, numbers, or labels you can read in each.",
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(`/tmp/v110crops/${name}-head.png`)}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(`/tmp/v110crops/${name}-new.png`)}` } },
        ],
      },
    ],
  });
  console.log(`\n===== ${name} (${label}) =====`);
  console.log(completion.choices[0].message.content);
}
