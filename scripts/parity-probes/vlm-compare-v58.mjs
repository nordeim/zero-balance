// vlm-compare-v58.mjs — the standing VLM pairwise (v58: the DESKTOP
// 1280x800 state of the SAVINGS view — the items family's remaining view;
// the v57 pair covered income + expenses). The savings goal-card's 1280
// state is unpinned at the pair viewport; its internals are pinned at 390
// only (v54 F1). The chrome is expected byte-identical per the v45
// grid-census pin + the v57 footer/badge pins (the same item-card family).
// The only expected differences are platform chrome (the reference's
// "Edit with Base44" FAB) + the seed-data classes (the reference's own
// 1-item seed vs the clone's dev seed: different item names/counts/
// amounts) — every flagged diff must be DOM-verified before it counts
// (the v43 misattribution lesson).
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
    "PAIR: savings view desktop 1280x800 (ref vs clone, goal-card grid — v58 standing check)",
    "/tmp/vlm58/ref-savings.png",
    "/tmp/vlm58/clone-savings.png",
    `You are comparing two screenshots of the same budget-planner web app's SAVINGS view at desktop 1280x800 — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a fixed left nav rail, a page header with a count subtitle, a white filter card with a search input (with a magnifier icon) and category/frequency select filters and classification tiles, and a grid of savings goal cards (each with a colored category dot or icon, title, amount, badges, and a date footer). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout structure, card geometry, the search icon shape, filter controls, fonts, colors, spacing, badges, buttons), however small. Be precise and concise. Note: differences in the DATA (item names, amounts, counts, badge text, dates) are expected and should be reported separately from LAYOUT/STYLE differences.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
