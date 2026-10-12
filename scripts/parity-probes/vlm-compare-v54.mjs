// vlm-compare-v54.mjs — the standing VLM pairwise (v54: (1) the
// /networth TABLIST at 390x844 mobile — the v53 F1 surface, the
// session-125 standing-check suggestion; (2) the SAVINGS view's goal
// card at 390x844 — THE v54 F1 surface, a data-divergent surface: the
// reference's own Emergency Fund goal (need-classified, 3 chips, no
// payment method) vs the clone's dev seed's Emergency Fund
// (savings-classified, 4 chips incl. Recurring, Bank Account payment).
// The chrome is byte-identical per the v54 F1 pin. The only expected
// differences are platform chrome (the reference's "Edit with Base44"
// FAB) + the seed-data classes — every flagged diff must be
// DOM-verified before it counts (the v43 misattribution lesson).
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function compare(zai, label, refPath, clonePath, prompt) {
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: prompt,
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(refPath)}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(clonePath)}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  const text = res.choices[0]?.message?.content || "NO RESPONSE";
  console.log(`\n===== ${label} =====`);
  console.log(text);
}

async function main() {
  const zai = await ZAI.create();
  await compare(
    zai,
    "PAIR 1: /networth tablist 390x844 (ref vs clone, v53 F1 surface — v54 standing check)",
    "/tmp/vlm54/ref-networth.png",
    "/tmp/vlm54/clone-networth.png",
    `You are comparing two screenshots of the same budget-planner web app's Net Worth page (390x844 mobile viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a mobile page with a title, a summary area, and a segmented tab control ("Assets" / "Liabilities"). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (tab control chrome, colors, fonts, spacing, layout, card content), however small. Be precise and concise.`,
  );
  await compare(
    zai,
    "PAIR 2: savings goal card 390x844 (ref vs clone, v54 F1 surface)",
    "/tmp/vlm54/ref-savings.png",
    "/tmp/vlm54/clone-savings.png",
    `You are comparing two screenshots of the same budget-planner web app's Savings page (390x844 mobile viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a mobile page with a title, a filter card, and item cards carrying a colored dot + name header, a dollar amount, small badge chips, and a date footer. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (card chrome, badge chips, colors, fonts, spacing, footer), however small. Be precise and concise.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
