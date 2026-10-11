// vlm-compare-v47.mjs — the standing VLM pairwise (v47: the INCOME
// items-view at 390x844 — the fresh MOBILE surface; the reference's
// /income is overflow-free at 390 (docSW 390, verified live), both
// sites' cards pinned byte-identical at 1280 by v45, the mobile reflow
// is the new ground. Expected flags: demo-data numbers + the known
// classes only. Every flagged diff must be DOM-verified before it
// counts — the v43 misattribution lesson).
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
            text: `You are comparing two screenshots of the same budget-planner web app's INCOME page (390x844 mobile viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show the mobile top bar, the page header with its icon chip, the summary strip (Total Income), and the list/grid of income cards. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout, colors, fonts, spacing, card geometry, badges, buttons, horizontal overflow), however small. Ignore differences in the actual DATA VALUES shown (amounts, labels, counts, number of cards). Be precise and concise.`,
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
    "PAIR: income items-view 390x844 (ref vs clone, v47 mobile surface)",
    "/tmp/vlm47/ref-income.png",
    "/tmp/vlm47/clone-income.png",
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
