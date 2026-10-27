// verify-modal-shot-v124.mjs — the one-shot VLM verification of the
// 07-add-item-modal.png day-rollover diff (the capture-day-dependent
// class: the dialog's date input defaults to todayIso() — the CAPTURE
// day, not the seed day; the committed shot same-day with the Oct 26
// v123 capture, the re-capture same-day with today's Oct 27 v124 run).
// The pixel pre-analysis: 234/5,184,000 pixels in a 16×22 bbox — the
// date digits alone; the VLM read confirms date-only, zero chrome drift.
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
          {
            type: "text",
            text: `You are comparing two screenshots of the same "Add Item" modal dialog from a budget-planner web app. Image 1 is the OLDER capture, image 2 is the NEWER capture. A pixel-diff pre-analysis found only 234 differing pixels in a single tiny 16x22 region. Report: (1) What exactly differs between the two images? (2) Is the difference confined to a date value inside a date input field, or is there ANY other visual difference (layout, fonts, colors, spacing, buttons, labels)? Be precise and concise.`,
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("/tmp/07-old.png")}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64("docs/screenshots/07-add-item-modal.png")}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
}

main().catch((e) => {
  console.error("VLM verify failed:", e.message);
  process.exit(1);
});
