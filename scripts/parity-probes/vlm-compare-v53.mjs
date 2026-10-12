// vlm-compare-v53.mjs — the standing VLM pairwise (v53: the CALCULATOR
// dialog at 390x844 mobile — THE F2 SURFACE: the panel + header + total
// card family, a data-divergent surface — the reference's own Rent data
// carries 1 line-item row where the clone's dev seed carries none (the
// empty state); the chrome is byte-identical per the v53 F2 pin). The
// only expected differences are platform chrome (the reference's
// "Edit with Base44" FAB) + the seed-data classes (the v47/v48/v52
// precedents). Every flagged diff must be DOM-verified before it
// counts — the v43 misattribution lesson.
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
            text: `You are comparing two screenshots of the same budget-planner web app's category Calculator dialog (390x844 mobile viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a modal dialog over a dimmed page: a white panel with a rounded top, a header with an orange calculator icon chip + a title like "Rent Calculator" + a close X, an orange-tinted "Total Calculated" card, a line-items list area, and an "Add Item"-style button. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (panel chrome, colors, fonts, spacing, buttons, list content), however small. Be precise and concise.`,
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
    "PAIR: calculator dialog 390x844 (ref vs clone, v53 F2 surface)",
    "/tmp/vlm53/ref-calculator.png",
    "/tmp/vlm53/clone-calculator.png",
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
