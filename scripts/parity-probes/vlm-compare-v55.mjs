// vlm-compare-v55.mjs — the standing VLM pairwise (v55: (1) the
// CALCULATOR DIALOG's WITH-ROW state at 390x844 — the v53 F2 surface,
// the session-128 standing-check suggestion; (2) the SAVINGS view's
// goal card at 390x844 — THE v55 F1 surface, now carrying the
// legacy-glyph swap: the piggy-bank chip icon renders the reference's
// OLD lucide shape data). The chrome is byte-identical per the v55 F1
// pin + the v53/v54 calculator + goal-card pins. The only expected
// differences are platform chrome (the reference's "Edit with Base44"
// FAB) + the seed-data classes (the reference's need-classified 3-chip
// goal vs the clone's savings-classified 4-chip goal; the line-item
// rows' own values) — every flagged diff must be DOM-verified before
// it counts (the v43 misattribution lesson).
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
    "PAIR 1: calculator dialog with-row 390x844 (ref vs clone, v53 F2 surface — v55 standing check)",
    "/tmp/vlm55/ref-calculator.png",
    "/tmp/vlm55/clone-calculator.png",
    `You are comparing two screenshots of the same budget-planner web app's category calculator dialog (390x844 mobile viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a modal dialog with a title, a total-calculated summary, a list of line-item rows (name, frequency, amount, edit/delete actions), and an add-item row. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (dialog chrome, row layout, fonts, colors, spacing, buttons), however small. Be precise and concise.`,
  );
  await compare(
    zai,
    "PAIR 2: savings goal card 390x844 (ref vs clone, v55 F1 surface — post legacy-glyph swap)",
    "/tmp/vlm55/ref-savings.png",
    "/tmp/vlm55/clone-savings.png",
    `You are comparing two screenshots of the same budget-planner web app's Savings page (390x844 mobile viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a mobile page with a title, a filter card, and item cards carrying a colored dot + name header, a dollar amount, small badge chips (with tiny icons), and a date footer. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (card chrome, badge chips and their icons, colors, fonts, spacing, footer), however small. Be precise and concise.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
