// vlm-compare-v131.mjs — the standing VLM pairwise RE-RUN (v131, the v125-era pair ELEVENTH re-run
// [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131] — the FIFTY-FOURTH consecutive queue/ledger
// agreement: the DASHBOARD's
// below-the-fold surfaces at desktop 1280x800 — (1) the BUDGET GUIDELINES
// card (the tinted, bordered 50/30/20 rows — the v51 F4 mobile census's
// desktop twin, never VLM-paired) and (2) the QUICK-ACTION card row (the
// three card buttons — the v45 F3 pin covers the hover:shadow-lg layers
// only; the resting chrome at the pair viewport unpaired)). The chrome is
// expected byte-identical per the v51 F4 pin (the card/tiles at 390), the
// v45 F3b pin (the hover shadow), and the v44 hero/stat pins at 1280. The
// only expected differences are platform chrome (the reference's "Edit
// with Base44" FAB/badge) + the seed-data classes (the reference's own
// 1-income data vs the clone's dev seed: different figures/counts/labels
// in the hero, donut, and drill-down) + the documented root-URL active-nav
// gap — every flagged diff must be DOM-verified before it counts (the v43
// misattribution lesson).
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
          { type: "text", text: `You are comparing two FULL-PAGE screenshots of the same budget-planner web app's DASHBOARD at desktop 1280x800 — image 1 is the REFERENCE site, image 2 is the CLONE. The page shows a fixed left nav rail, a "Budget Dashboard" header with an Add Item button, the Net Zero Goal hero card (gradient), a Net Zero Breakdown card with a donut chart and drill-down rows, three stat cards (Total Income / Total Savings / Total Expenses), then BELOW THE FOLD a Spending Breakdown card and a BUDGET GUIDELINES card (the header "Budget Guidelines" plus three tinted, bordered rows: Needs ~50%, Wants ~30%, Savings ~20% — each with a colored label, a percent, and a gray description), and finally a QUICK ACTIONS row of three large card buttons (Add Income, Add Savings, Add Expense — each a bordered rounded card with a tinted icon tile, a label, and a plus icon at the right). Focus your comparison on the BUDGET GUIDELINES card (card geometry, border, header typography, row tints, row padding, label/percent/description typography and colors) and the QUICK ACTION cards (card geometry, radius, padding, border, icon tile size/radius/tint, icon size, label typography, plus icon size/opacity). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout structure, geometry, fonts, colors, spacing, borders, icons), however small. Be precise and concise. Note: differences in the DATA (net zero figures, donut percentages, drill-down rows, item counts, stat amounts) are expected and should be reported separately from LAYOUT/STYLE differences.` },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm131/ref-dashboard.png")}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm131/clone-dashboard.png")}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  const text = res.choices[0]?.message?.content || "NO RESPONSE";
  console.log("===== PAIR: dashboard below-the-fold (Budget Guidelines + Quick Actions) desktop 1280x800 (ref vs clone — the v131 ELEVENTH re-run of the v125-era pair [v61 → v68 → v77 → v83 → v89 → v95 → v101 → v107 → v113 → v119 → v125 → v131]) =====");
  console.log(text);
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
