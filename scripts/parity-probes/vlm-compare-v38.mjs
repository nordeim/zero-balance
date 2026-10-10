// vlm-compare-v38.mjs — the standing VLM pairwise (v38: the /savings view —
// Surface B, first-time measured). Sends the pair to the vision model.
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
            text: `You are comparing two screenshots of the same budget-planner web page — image 1 is the REFERENCE site, image 2 is the CLONE. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout, colors, fonts, spacing, component chrome), however small. Ignore differences in the actual DATA VALUES shown (demo data differs between the accounts) and any text-content differences. Be precise and concise.`,
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
    "PAIR: /savings view (ref vs clone)",
    "/tmp/vlm38/ref-savings.png",
    "/tmp/vlm38/clone-savings.png",
  );
}

main().catch((e) => {
  console.error("VLM ERROR:", e.message || e);
  process.exit(1);
});
