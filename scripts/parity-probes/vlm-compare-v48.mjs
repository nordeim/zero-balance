// vlm-compare-v48.mjs — the standing VLM pairwise (v48: the SAVINGS
// items-view at 1280x800 — the fresh DESKTOP surface; both sites' card
// chrome pinned byte-identical by the v45 items-view census family,
// /savings is the unpinned view ground. Expected flags: demo-data
// numbers + the known classes only (the reference's 1 Emergency Fund
// card vs the clone's richer seed). Every flagged diff must be
// DOM-verified before it counts — the v43 misattribution lesson).
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
            text: `You are comparing two screenshots of the same budget-planner web app's SAVINGS page (1280x800 desktop viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show the desktop sidebar navigation, the page header with its icon chip, the summary strip (Total Savings), and the list/grid of savings goal cards. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (layout, colors, fonts, spacing, card geometry, badges, buttons, icons), however small. Ignore differences in the actual DATA VALUES shown (amounts, labels, counts, number of cards). Be precise and concise.`,
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
    "PAIR: savings items-view 1280x800 (ref vs clone, v48 desktop surface)",
    "/tmp/vlm48/ref-savings.png",
    "/tmp/vlm48/clone-savings.png",
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
