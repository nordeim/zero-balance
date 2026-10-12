// vlm-compare-v52.mjs — the standing VLM pairwise (v52: the EXPENSES
// view at 390x844 mobile — THE F3 SURFACE: the filter + card family, a
// data-divergent surface — the clone's richer seed renders 3 expense
// cards (with a 4-badge Rent row + a Notes-carrying card) where the
// reference's 4 cards carry 3-badge rows; the chrome is byte-identical
// per the v52 pins). The only expected differences are platform chrome
// (the reference's "Edit with Base44" FAB) + the seed-data classes (the
// v47/v48 precedents). Every flagged diff must be DOM-verified before
// it counts — the v43 misattribution lesson.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function compare(zai, label, refPath, clonePath) {
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: `You are comparing two screenshots of the same budget-planner web app's EXPENSES page (390x844 mobile viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show an "Expenses" page: a mobile top bar with a hamburger and the ZeroBalance brand, an "Expenses" heading with an items-count subtitle and an "Add Expense" button, a white filter card (search + category/frequency/payment-method selects), and white expense cards with a title, an amount, and colored badge chips. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (card chrome, colors, fonts, spacing, badges, layout), however small. Be precise and concise.`,
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
    "PAIR: expenses view 390x844 (ref vs clone, v52 F3 surface)",
    "/tmp/vlm52/ref-expenses.png",
    "/tmp/vlm52/clone-expenses.png",
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
