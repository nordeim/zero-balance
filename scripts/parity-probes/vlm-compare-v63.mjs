// vlm-compare-v63.mjs — the v63 VLM pairwise: the /NETWORTH view
// full-page at mobile 390x844 — the standing-pair program's LAST
// un-paired viewport × view combination (v56 PAIR 2 covered the desktop
// 1280 networth; v62's mobile twin covered the dashboard; this closes
// the viewport × view matrix: {dashboard, items, savings, calculator,
// networth} × {1280, 390} all now paired).
// Expected flag classes (each must be DOM-arbitrated per the v43 rule):
// the documented reference OVERFLOW (its /networth page renders 464px
// wide at 390 — R-bug-4, superset fix #4; its summary card 432 wide,
// its tablist 432 with fractional tracks, its trend icon clipped at the
// page edge), platform chrome (the Base44 FAB/badge/tooltip), seed-data
// classes (its 1 asset vs the clone's 3 + 2 liabilities), user-identity
// (the avatar). A pair is CLEAN only when every flag arbitrates to a
// documented class.
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
          {
            type: "text",
            text: `You are comparing two FULL-PAGE MOBILE screenshots (390px wide) of the same budget-planner web app's NET WORTH page — image 1 is the REFERENCE site, image 2 is the CLONE. The page shows a top bar with a hamburger menu button and logo, a "Net Worth" header, a dark green gradient summary card (total figure, assets vs liabilities stat tiles, a ratio row, a trend icon), an Assets / Liabilities tab bar, an Assets group with cards (each card: a colored dot + title + type badge + amount + fact rows), and a Liabilities group. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons), however small — especially any horizontal overflow, clipped content, or broken alignment. Be precise and concise. Note: differences in the DATA (figures, counts, card contents, asset names) and in the top-left avatar area are expected — report them separately from LAYOUT/STYLE differences.`,
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm63/ref-networth-mobile.png")}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm63/clone-networth-mobile.png")}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log("===== PAIR: networth full-page mobile 390x844 (ref vs clone — v63) =====");
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
