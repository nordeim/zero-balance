// vlm-compare-v39.mjs — the standing VLM pairwise (v39: the MOBILE
// sheet-open state at 390×844 — the mobile navigation menu itself, both
// sites freshly opened, the superset differences expected: the clone's
// Dashboard link carries the active highlight the reference's `/` lacks
// [R3, superset fix #3]).
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
            text: `You are comparing two screenshots of the same budget-planner web app's MOBILE navigation sheet (390x844 viewport, sheet just opened from the hamburger) — image 1 is the REFERENCE site, image 2 is the CLONE. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout, colors, fonts, spacing, sheet geometry, link styling), however small. Ignore differences in the actual DATA VALUES shown. Be precise and concise.`,
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
    "PAIR: mobile sheet-open state 390x844 (ref vs clone)",
    "/tmp/vlm39/ref-mobile-sheet.png",
    "/tmp/vlm39/clone-mobile-sheet.png",
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
