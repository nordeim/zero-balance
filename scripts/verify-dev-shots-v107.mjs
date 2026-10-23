// verify-dev-shots-v107.mjs — VLM-verify the dev-server evidence set:
// (1) the mobile menu OPEN shot (all 5 links + the brand row visible),
// (2) the dashboard shot (clean render, the guidelines + quick-action pair).
import ZAI from "z-ai-web-dev-sdk";
import { readFileSync } from "node:fs";

const b64 = (p) => readFileSync(p).toString("base64");

async function main() {
  const zai = await ZAI.create();
  const shots = [
    ["docs/screenshots/dev/dev-mobile-menu-open-390.png",
     "This is a screenshot of a mobile navigation menu (390px wide). Answer: (1) Is a navigation menu/sheet OPEN and visible? (2) List the navigation link texts you can read. (3) Is the ZeroBalance brand visible? Answer briefly."],
    ["docs/screenshots/dev/dev-dashboard-1280.png",
     "This is a desktop dashboard screenshot (1280px). Answer: (1) Does it show a left sidebar and a main dashboard? (2) Are the Budget Guidelines card (Needs/Wants/Savings rows) and the three Add Income / Add Savings / Add Expense buttons visible? (3) Any visual glitch, overlap, or broken layout? Answer briefly."],
  ];
  for (const [file, q] of shots) {
    const res = await zai.chat.completions.createVision({
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: q },
            { type: "image_url", image_url: { url: `data:image/png;base64,${b64(file)}` } },
          ],
        },
      ],
      thinking: { type: "disabled" },
    });
    console.log(`=== ${file} ===`);
    console.log(res.choices[0]?.message?.content);
  }
}

main().catch((e) => { console.error(e.message); process.exit(1); });
