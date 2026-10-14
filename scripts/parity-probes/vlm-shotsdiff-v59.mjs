// vlm-shotsdiff-v59.mjs — the screenshot-diff arbitration (v59): the
// regenerated 04-expenses vs HEAD's — expected class: the seed's
// RELATIVE-DATE drift (isoDate(-N) anchors to the seed-run date; the
// fresh checkout's db seeded 2 days after v58's capture), NOT chrome.
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
          { type: "text", text: `You are comparing TWO screenshots of the SAME app's expenses view at the same viewport — image 1 captured 2026-10-13, image 2 captured 2026-10-15 (same code, same seed structure, the only expected difference is the item-card FOOTER DATES which are seed-run-relative). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) list EVERY difference you can spot, however small, and classify each as either a DATE-TEXT difference (e.g. "Oct 4, 2026" vs "Oct 6, 2026") or a LAYOUT/STYLE difference (geometry, colors, fonts, spacing).` },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/vlm59/head-04-expenses.png")}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("docs/screenshots/04-expenses.png")}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
}

main().catch((e) => { console.error("VLM failed:", e.message); process.exit(1); });
