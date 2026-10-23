// vlm-compare-v108.mjs — the v108 standing VLM pairwise RE-RUN: BOTH mobile
// 390x844 full-page twins — (1) the /NETWORTH view (the v63-era pair's
// surface — the v108 queue item, confirmed by the rotation ledger: the
// twins last re-shot v102 = the oldest remaining candidate [v102 < v103 <
// v104 < v105 < v106 < v107]; the pair's SEVENTH re-run [v62/v63 → v69 →
// v78 → v84 → v90 → v96 → v102 → v108]) and (2) the DASHBOARD (the v62-era mobile twin's
// surface). The chrome is expected byte-identical per the v63 stat-tile
// pin + the v53 tablist-390 pin + the v41 F3 mobile superset census
// (networth), and the v62
// header-subtitle pin + the v51 F4 mobile guidelines census + the v45/v44
// pin families (dashboard); the v84/v90/v96/v102 re-runs' own verdicts were DIFFERENT
// with every flag DOM-arbitrated to a documented class — NO NEW GAP.
// Expected flag classes (each must be DOM-arbitrated per the v43 rule):
// platform chrome (the Base44 FAB/badge), seed-data classes (the
// reference's own 1-income data vs the clone's dev seed), user-identity
// (the avatar), the documented root-URL active-nav gap, the v41
// mobile-superset stacking class (the reference's 464px overflow + fixed
// 2-col tiles vs the clone's fitting 1-col), and perception artifacts.
// A pair is CLEAN only when every flag arbitrates to a documented class.
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
  const text = res.choices[0]?.message?.content || "NO RESPONSE";
  console.log(`===== PAIR: ${title} =====`);
  console.log(text);
  console.log();
}

async function main() {
  const zai = await ZAI.create();

  await pair(
    zai,
    "NETWORTH mobile 390x844 full-page (ref vs clone — the v108 re-run of the v63-era pair)",
    "/tmp/vlm108/ref-networth-mobile.png",
    "/tmp/vlm108/clone-networth-mobile.png",
    `You are comparing two FULL-PAGE MOBILE screenshots (390px wide) of the same budget-planner web app's NET WORTH page — image 1 is the REFERENCE site, image 2 is the CLONE. The page shows a top bar with a hamburger menu button and logo, a "Net Worth" header, a dark green gradient summary card (total figure, assets vs liabilities stat tiles, a ratio row, a trend icon), an Assets / Liabilities tab bar, an Assets group with cards (each card: a colored dot + title + type badge + amount + fact rows), and a Liabilities group. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons), however small — especially any horizontal overflow, clipped content, or broken alignment. Be precise and concise. Note: differences in the DATA (figures, counts, card contents, asset names) and in the top-left avatar area are expected — report them separately from LAYOUT/STYLE differences.`,
  );

  await pair(
    zai,
    "DASHBOARD mobile 390x844 full-page (ref vs clone — the v108 re-run of the v62-era mobile twin)",
    "/tmp/vlm108/ref-dashboard-mobile.png",
    "/tmp/vlm108/clone-dashboard-mobile.png",
    `You are comparing two FULL-PAGE MOBILE screenshots (390px wide) of the same budget-planner web app's DASHBOARD — image 1 is the REFERENCE site, image 2 is the CLONE. The mobile page shows a top bar with a hamburger menu button and logo, a "Budget Dashboard" header with an Add Item button, the Net Zero Goal hero card, a Net Zero Breakdown card with donut chart and drill-down rows, three stat cards stacked vertically, a Spending Breakdown card, a Budget Guidelines card, and a quick-actions stack. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons), however small — especially any horizontal overflow, clipped content, or broken alignment. Be precise and concise. Note: differences in the DATA (figures, percentages, counts, drill-down row contents) and in the top-left avatar area are expected — report them separately from LAYOUT/STYLE differences.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
