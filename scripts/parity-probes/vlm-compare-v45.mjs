// vlm-compare-v45.mjs — the standing VLM pairwise (v45: the ITEMS-VIEW
// card grid at 1280x800 — the session's new surface; the grid + card
// chrome is pinned byte-identical, so expected flags: demo-data numbers
// + the known classes only. Every flagged diff must be DOM-verified
// before it counts — the v43 misattribution lesson).
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function compare(zai, label, refPath, clonePath) {
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: `You are comparing two screenshots of the same budget-planner web app's INCOME items page (1280x800 desktop viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show the page header with its icon chip, the search + filter card, and the grid of income item cards. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout, colors, fonts, spacing, card geometry, grid columns, badges, buttons), however small. Ignore differences in the actual DATA VALUES shown (amounts, labels, counts, number of cards). Be precise and concise.`,
          },
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
    "PAIR: income items-view 1280x800 (ref vs clone, v45 surface)",
    "/tmp/vlm45/ref-items.png",
    "/tmp/vlm45/clone-items.png",
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
