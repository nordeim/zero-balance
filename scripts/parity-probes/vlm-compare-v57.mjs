// vlm-compare-v57.mjs — the standing VLM pairwise (v57: the DESKTOP
// 1280x800 state of (1) the INCOME view — the v55 search-input glyph swap
// surface + the item-card grid; (2) the EXPENSES view — the same grid
// family + the payment-method filter row). The session-134 v57 queue's
// own standing-check suggestion. The chrome is byte-identical per the v45
// grid-census pin + the v55 glyph-parity pin + the v57 footer/badge pins.
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
    "PAIR 1: income view desktop 1280x800 (ref vs clone, search-glyph + item-card grid — v57 standing check)",
    "/tmp/vlm57/ref-income.png",
    "/tmp/vlm57/clone-income.png",
    `You are comparing two screenshots of the same budget-planner web app's INCOME view at desktop 1280x800 — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a fixed left nav rail, a page header with a count subtitle, a white filter card with a search input (with a magnifier icon) and category/frequency select filters and classification tiles, and a grid of income item cards (each with a colored category dot, title, amount, badges, and a date footer). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout structure, card geometry, the search icon shape, filter controls, fonts, colors, spacing, badges, buttons), however small. Be precise and concise. Note: differences in the DATA (item names, amounts, counts, badge text, dates) are expected and should be reported separately from LAYOUT/STYLE differences.`,
  );
  await compare(
    zai,
    "PAIR 2: expenses view desktop 1280x800 (ref vs clone, item-card grid + payment filter — v57 standing check)",
    "/tmp/vlm57/ref-expenses.png",
    "/tmp/vlm57/clone-expenses.png",
    `You are comparing two screenshots of the same budget-planner web app's EXPENSES view at desktop 1280x800 — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a fixed left nav rail, a page header with a count subtitle, a white filter card with a search input, category/frequency/payment-method filters and classification tiles, and a grid of expense item cards (each with a colored category dot, title, amount, badges, and a date + payment-method footer). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout structure, card geometry, filter controls, fonts, colors, spacing, badges, buttons), however small. Be precise and concise. Note: differences in the DATA (item names, amounts, counts, badge text, dates, payment methods) are expected and should be reported separately from LAYOUT/STYLE differences.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
