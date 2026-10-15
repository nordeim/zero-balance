// vlm-glcol-v61.mjs — the Budget Guidelines COLUMN arbitration crop
// (the right column of the lg:grid-cols-2 row: x 770-1258, y 764-1472 on
// the 1280-wide full-page shots). The v61 census found the reference's
// card h 348 inside a STRETCHED space-y-4 wrapper (h 656) vs the clone's
// card itself stretched to 656 — the VLM pair called the page IDENTICAL,
// so this crop comparison arbitrates whether the height difference is
// visually real (the white card area below the last tile) or below the
// perception threshold.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function main() {
  const zai = await ZAI.create();
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: `These are two cropped screenshots of the SAME region (the right-hand column of a two-column card row on a budget-planner dashboard at desktop 1280) — image 1 is the REFERENCE site, image 2 is the CLONE. Each image should show a "Budget Guidelines" card: a white rounded card with a header and three tinted rows (Needs ~50%, Wants ~30%, Savings ~20%). Question: does the card's WHITE BODY (with its border and shadow) end at the same vertical position in both images — right after the third tinted row — or does one card's white body extend FURTHER DOWN with extra empty white space below the last row? Report: (1) where the white card body ends in image 1 (immediately after the Savings row / extends further down), (2) same for image 2, (3) VERDICT: SAME or DIFFERENT. Be precise.` },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm61/crops/ref-gl-col.png")}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm61/crops/clone-gl-col.png")}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
}

main().catch((e) => {
  console.error("VLM arbitration failed:", e.message);
  process.exit(1);
});
