// vlm-compare-v92.mjs — the v92 VLM pairwise: the SAVINGS view at
// desktop 1280x800, FULL-PAGE — the fresh re-run of the re-run cycle's
// next-oldest candidate (the v86-era savings pair's FIFTH re-run — last re-shot
// v86, now the oldest remaining [v86 < v87 < v88 < v89 < v90 < v91] — agreeing with the rotation ledger, the FIFTEENTH consecutive agreement).
// Expected flag classes (each must be DOM-arbitrated per the v43 rule):
// seed-data classes (the reference's 1 savings item vs the clone's 2-item
// dev seed: names/counts/amounts/badges), user-identity (the avatar),
// platform chrome (the Base44 FAB/badge). A pair is CLEAN only when
// every flag arbitrates to a documented class.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function main() {
  const zai = await ZAI.create();
  const prompt = `You are comparing two FULL-PAGE DESKTOP screenshots (1280px wide) of the same budget-planner web app's SAVINGS view — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a dark sidebar rail with navigation links (Dashboard, Income, Expenses, Savings, Networth), a page header with a title, count subtitle and an "Add Savings Goal" gradient button, a white filter card with a search input (magnifier icon) and category/frequency dropdown selects, and a grid of savings goal cards (each card: a colored category dot, title, amount, badges, and a date footer). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons), however small — especially any horizontal overflow, clipped content, or broken alignment. Be precise and concise. Note: differences in the DATA (figures, counts, card contents, item names, badge text, dates) and in the top-left avatar area are expected — report them separately from LAYOUT/STYLE differences.`;
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: prompt },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm92/ref-savings-full.png")}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm92/clone-savings-full.png")}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log("===== PAIR: savings view full-page 1280x800 (ref vs clone — v92) =====");
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
