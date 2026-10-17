// vlm-arbit-v80.mjs — visually arbitrate the v80 screenshot DATE-class
// diff crops (the v66/v75 discipline: a pixel diff is DATE-class ONLY
// when the changed region is a date/text-value change with identical
// surrounding chrome — never a layout shift). Each pair image stacks the
// v79-baseline crop (top) above the fresh crop (bottom).
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");
const files = [
  "pair-03-income.png",
  "pair-05-savings.png",
  "pair-06-networth.png",
  "pair-08-calculator.png",
  "pair-16-item-details.png",
];

async function main() {
  const zai = await ZAI.create();
  for (const f of files) {
    const prompt = `This image stacks TWO crops of the same region of a budget-app screenshot: the TOP crop is the older baseline, the BOTTOM crop is the fresh capture (a magenta separator divides them). Report concisely: (1) what text/content differs between top and bottom, (2) whether the surrounding layout/chrome (fonts, spacing, alignment, borders, icons) is identical, (3) VERDICT: DATE-TEXT-ONLY or LAYOUT-CHANGE.`;
    const res = await zai.chat.completions.createVision({
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: prompt },
            { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/v80-crops/" + f)}` } },
          ],
        },
      ],
      thinking: { type: "disabled" },
    });
    console.log(`===== ${f} =====`);
    console.log(res.choices[0]?.message?.content || "NO RESPONSE");
    console.log("");
  }
}

main().catch((e) => {
  console.error("VLM arbitrate failed:", e.message);
  process.exit(1);
});
