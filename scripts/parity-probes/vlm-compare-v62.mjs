// vlm-compare-v62.mjs — the v62 VLM pairwise: TWO pairs — (1) the
// DASHBOARD full-page at desktop 1280x800 (the standing pair, re-verifying
// the post-v61 state: the F1 guidelines-wrapper fix + the v60/v61 pinned
// surfaces) and (2) the DASHBOARD full-page at mobile 390x844 (the v62
// addition — the user directive's mobile emphasis; the standing checks
// verify mobile functionally, this pair adds the visual confirmation).
// Expected flag classes (each must be DOM-arbitrated per the v43 rule):
// platform chrome (the Base44 FAB/badge), seed-data classes (the
// reference's 1-income data vs the clone's dev seed), user-identity (the
// avatar), the documented root-URL active-nav gap, and perception
// artifacts (the donut labels). A pair is CLEAN only when every flag
// arbitrates to a documented class.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function pair(zai, title, refPath, clonePath, prompt) {
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: prompt },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(refPath)}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(clonePath)}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(`===== PAIR: ${title} =====`);
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
  console.log();
}

async function main() {
  const zai = await ZAI.create();
  await pair(
    zai,
    "dashboard full-page desktop 1280x800 (ref vs clone — v62)",
    "/tmp/vlm62/ref-dashboard.png",
    "/tmp/vlm62/clone-dashboard.png",
    `You are comparing two FULL-PAGE screenshots of the same budget-planner web app's DASHBOARD at desktop 1280x800 — image 1 is the REFERENCE site, image 2 is the CLONE. The page shows a fixed left nav rail, a "Budget Dashboard" header with an Add Item button, the Net Zero Goal hero card (gradient), a Net Zero Breakdown card with a donut chart and drill-down rows, three stat cards, a Spending Breakdown card, a BUDGET GUIDELINES card (three tinted bordered rows: Needs/Wants/Savings), and a QUICK ACTIONS row of three card buttons (Add Income / Add Savings / Add Expense). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons), however small. Be precise and concise. Note: differences in the DATA (figures, percentages, counts, drill-down row contents) and in the top-left user avatar are expected — report them separately from LAYOUT/STYLE differences.`,
  );
  await pair(
    zai,
    "dashboard full-page mobile 390x844 (ref vs clone — v62)",
    "/tmp/vlm62/ref-dashboard-mobile.png",
    "/tmp/vlm62/clone-dashboard-mobile.png",
    `You are comparing two FULL-PAGE MOBILE screenshots (390px wide) of the same budget-planner web app's DASHBOARD — image 1 is the REFERENCE site, image 2 is the CLONE. The mobile page shows a top bar with a hamburger menu button and logo, a "Budget Dashboard" header with an Add Item button, the Net Zero Goal hero card, a Net Zero Breakdown card with donut chart and drill-down rows, three stat cards stacked vertically, a Spending Breakdown card, a Budget Guidelines card, and a quick-actions stack. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons), however small — especially any horizontal overflow, clipped content, or broken alignment. Be precise and concise. Note: differences in the DATA (figures, percentages, counts, drill-down row contents) and in the top-left avatar area are expected — report them separately from LAYOUT/STYLE differences.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
