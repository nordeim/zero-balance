// vlm-compare-v43.mjs — the standing VLM pairwise (v43: the EXPANDED
// drill-down at 1280x800 — the surface the F1/F2 fixes touched; expected
// flags: demo-data numbers, both data-level).
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
            text: `You are comparing two screenshots of the same budget-planner web app's dashboard page (1280x800 desktop viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show the Net Zero Breakdown card with its drill-down EXPANDED (the Total Income section open, its category and item rows visible). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout, colors, fonts, spacing, card geometry, chevron icons, hover backgrounds), however small. Ignore differences in the actual DATA VALUES shown (amounts, labels, counts). Be precise and concise.`,
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
    "PAIR: expanded drill-down 1280x800 (ref vs clone)",
    "/tmp/vlm43/ref-drill.png",
    "/tmp/vlm43/clone-drill.png",
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
