// vlm-compare-v121.mjs — the v121 VLM pairwise: the ITEMS view (income +
// expenses) at desktop 1280x800, FULL-PAGE — the fresh re-run of the
// OLDEST re-run candidate (the v57-era items pair, last re-shot v115 —
// the TENTH re-run of the pair [v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 → v115 → v121]; every
// other pair re-ran later).
// Expected flag classes (each must be DOM-arbitrated per the v43 rule):
// seed-data classes (the reference's 1 income item / 4 expense items vs
// the clone's dev seed; the payment-method chips DATA-CONDITIONAL; the
// badge wrap), user-identity (the avatar), platform chrome (the Base44
// FAB/badge). A pair is CLEAN only when every flag arbitrates to a
// documented class.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function pair(zai, name, refPath, clonePath, prompt) {
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
  console.log(`===== PAIR ${name} (ref vs clone — v121) =====`);
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
  console.log();
}

async function main() {
  const zai = await ZAI.create();
  const base = `You are comparing two FULL-PAGE DESKTOP screenshots (1280px wide) of the same budget-planner web app — image 1 is the REFERENCE site, image 2 is the CLONE. The page shows a dark sidebar rail with navigation links (Dashboard, Income, Expenses, Savings, Networth), a page header with a title and an "Add ..." gradient button, a filter card with a search input and dropdown selects, and a grid of item cards (each card: a colored dot + title + amount + badges + footer). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons), however small — especially any horizontal overflow, clipped content, or broken alignment. Be precise and concise. Note: differences in the DATA (figures, counts, card contents, item names, badge counts) and in the top-left avatar area are expected — report them separately from LAYOUT/STYLE differences.`;
  await pair(zai, "1: income view full-page 1280x800", "/tmp/vlm121/ref-income-full.png", "/tmp/vlm121/clone-income-full.png", base + " This is the INCOME view.");
  await pair(zai, "2: expenses view full-page 1280x800", "/tmp/vlm121/ref-expenses-full.png", "/tmp/vlm121/clone-expenses-full.png", base + " This is the EXPENSES view (it also has a payment-method dropdown in the filter card, and each expense card has Edit and Calculate action buttons).");
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
