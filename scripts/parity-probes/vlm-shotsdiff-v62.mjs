// vlm-shotsdiff-v62.mjs — the v62 screenshot-regeneration arbitration (the
// v59/v60 pattern): SIX of the 16 regenerated screenshots diffed
// (03-income, 04-expenses, 05-savings, 06-networth, 08-calculator,
// 16-item-details — the six date-bearing surfaces). Hypothesis: the
// SEED-DATE class (the seed's isoDate(-N) dates are relative to the
// seed-run day; the dev DB was re-seeded this session) — the diffs must
// be DATE-TEXT-only per the v43 rule before the regeneration is accepted.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");
const PREV = "/home/z/my-project/tool-results/shots-prev";
const NEW = "docs/screenshots";
const pairs = [
  ["03-income.png", "the Income items view"],
  ["04-expenses.png", "the Expenses items view"],
  ["05-savings.png", "the Savings items view"],
  ["06-networth.png", "the Net Worth view"],
  ["08-calculator.png", "the expense calculator dialog"],
  ["16-item-details.png", "the item details sheet"],
];

async function main() {
  const zai = await ZAI.create();
  for (const [file, label] of pairs) {
    const res = await zai.chat.completions.createVision({
      messages: [
        {
          role: "user",
          content: [
            {
              type: "text",
              text: `You are comparing two screenshots of the SAME app's ${label} (image 1 = the previous capture, image 2 = the fresh capture of the same build). They should be identical. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) if DIFFERENT, list every visible difference precisely (text content, position, color), however small. Pay special attention to whether the ONLY differences are date texts (e.g. calendar dates in card footers or detail rows).`,
            },
            { type: "image_url", image_url: { url: `data:image/png;base64,${b64(`${PREV}/${file}`)}` } },
            { type: "image_url", image_url: { url: `data:image/png;base64,${b64(`${NEW}/${file}`)}` } },
          ],
        },
      ],
      thinking: { type: "disabled" },
    });
    console.log(`=== ${file} (${label}) ===`);
    console.log(res.choices[0]?.message?.content || "NO RESPONSE");
    console.log();
  }
}

main().catch((e) => {
  console.error("VLM shotsdiff failed:", e.message);
  process.exit(1);
});
