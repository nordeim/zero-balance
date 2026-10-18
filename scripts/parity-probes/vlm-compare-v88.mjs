// vlm-compare-v88.mjs — the standing VLM pairwise, v88 edition: a fresh
// re-run of the v60-era pair (the re-run cadence's rotation — the oldest
// remaining standing pair: the v61-era pair covered by v83, the v60-era
// pair last re-shot v82 — now the oldest remaining [v82 < v83 < v84 < v85
// < v86 < v87]; the pair's FOURTH re-run [v60 → v67 → v76 → v82 → v88] —
// the ELEVENTH consecutive queue/ledger agreement): (1) the NETWORTH view's
// desktop 1280x800 dedicated standing pair and (2) the DASHBOARD's drill-down
// EXPANDED state pair. The chrome is expected byte-identical per the v41
// summary pins (640/390), the v46 asset-card pin (1280), the v50/v53
// tablist pins (640/390), the v60 F1 summary-card/tablist pin + the v60 F2
// drill-down sub/item pin (1280), the v63 stat-tile pin (390), the v44
// drill-height pin (1280), the v67 networth summary-card HEIGHT-family
// pin (1280), and the v82 completion-family pin (1280). The only expected
// differences are platform chrome (the reference's "Edit with Base44"
// FAB/badge) + the seed-data classes (the reference's own 1-asset data vs
// the clone's dev seed: different figures, item counts, group headers,
// ratio "∞:1" vs "0.21:1") — every flagged diff must be DOM-verified
// before it counts (the v43 misattribution lesson).
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function compare(zai, label, refPath, clonePath, prompt) {
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
  console.log(`\n===== ${label} =====`);
  console.log(text);
}

async function main() {
  const zai = await ZAI.create();
  await compare(
    zai,
    "PAIR 1: networth view desktop 1280x800 (ref vs clone — the v60-era pair's fresh re-run, v88)",
    "/tmp/vlm88/ref-networth.png",
    "/tmp/vlm88/clone-networth.png",
    `You are comparing two FULL-PAGE screenshots of the same budget-planner web app's NET WORTH view at desktop 1280x800 — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a fixed left nav rail, a page header with a gradient icon chip (trending-up arrow) + "Net Worth" title, a forest-to-lime gradient summary card (Total Net Worth figure, a round trending-up icon medallion, two glassy stat tiles Total Assets / Total Liabilities, and an "Asset to Liability Ratio" footer row), an Assets/Liabilities tab bar with circle-arrow icons, and type-grouped asset/liability cards (each with a colored dot, name, gray type badge, colored amount, institution/interest/Updated footer lines, and a vertical-ellipsis menu button). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout structure, the summary card's gradient/geometry, the tab bar, card geometry, fonts, colors, spacing, badges, buttons), however small. Be precise and concise. Note: differences in the DATA (net worth figures, asset/liability names, amounts, counts, group headers, the ratio value) are expected and should be reported separately from LAYOUT/STYLE differences.`,
  );
  await compare(
    zai,
    "PAIR 2: dashboard drill-down EXPANDED desktop 1280x800 (ref vs clone — the v60-era pair's fresh re-run, v88)",
    "/tmp/vlm88/ref-drilldown.png",
    "/tmp/vlm88/clone-drilldown.png",
    `You are comparing two FULL-PAGE screenshots of the same budget-planner web app's DASHBOARD at desktop 1280x800, with the "Net Zero Breakdown" card's drill-down EXPANDED (the Total Income section open, and its first category open showing subcategory + item rows) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a fixed left nav rail, a Net Zero Goal hero card, stat rows, an allocation donut chart with a legend, the EXPANDED breakdown card (section rows with chevrons and amounts, indented category rows with colored dots, further-indented subcategory and item rows, and a footer row counting categories), budget guidelines, and quick-action tiles. Focus your comparison on the breakdown card's expanded drill-down surfaces (row heights, indentation rhythm, fonts, colors, chevrons, dots, dividers) as well as the overall page. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot, however small. Be precise and concise. Note: differences in the DATA (category/subcategory/item names, amounts, counts, percentages) are expected and should be reported separately from LAYOUT/STYLE differences.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
