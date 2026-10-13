// vlm-compare-v56.mjs — the standing VLM pairwise (v56: the DESKTOP
// 1280x800 state of (1) the DASHBOARD — the v55 F1 surfaces post-swap:
// the stat rows carrying the legacy piggy-bank/trending-up glyphs, the
// donut, and its legend; (2) the NETWORTH view — the trending-up
// hero/summary swap surfaces). The session-131 v56 queue's own
// standing-check suggestion. The chrome is byte-identical per the v55
// glyph-parity pin + the dashboard/networth spec pins. The only
// expected differences are platform chrome (the reference's "Edit with
// Base44" FAB) + the seed-data classes (the reference's own 1-item seed
// vs the clone's dev seed: different item names/counts/amounts) — every
// flagged diff must be DOM-verified before it counts (the v43
// misattribution lesson).
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
    "PAIR 1: dashboard desktop 1280x800 (ref vs clone, v55 F1 surfaces post-swap — v56 standing check)",
    "/tmp/vlm56/ref-dashboard.png",
    "/tmp/vlm56/clone-dashboard.png",
    `You are comparing two screenshots of the same budget-planner web app's DASHBOARD at desktop 1280x800 — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a fixed left nav rail, a Net Zero Goal hero card, stat rows (Total Income / Total Savings / Total Expenses with icons), an allocation donut chart with a legend, a breakdown card, and quick-action tiles. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout structure, card geometry, icon shapes — especially the piggy-bank and trending-up icons — fonts, colors, spacing, buttons), however small. Be precise and concise. Note: differences in the DATA (item names, amounts, counts) are expected and should be reported separately from LAYOUT/STYLE differences.`,
  );
  await compare(
    zai,
    "PAIR 2: networth desktop 1280x800 (ref vs clone, trending-up swap surfaces — v56 standing check)",
    "/tmp/vlm56/ref-networth.png",
    "/tmp/vlm56/clone-networth.png",
    `You are comparing two screenshots of the same budget-planner web app's NET WORTH view at desktop 1280x800 — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a forest-gradient hero card with a trending-up icon and total net worth, a summary card, asset and liability tables/cards. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout structure, card geometry, the trending-up icon shape, fonts, colors, spacing, buttons), however small. Be precise and concise. Note: differences in the DATA (asset/liability names, amounts, counts) are expected and should be reported separately from LAYOUT/STYLE differences.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
