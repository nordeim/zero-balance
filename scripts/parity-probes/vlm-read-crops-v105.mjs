// vlm-read-crops-v105.mjs — the VLM read of the 08/16 diff crops: what
// text actually changed between the committed (HEAD) and regenerated
// sets, to arbitrate the DATE-class expectation for the blur-smeared
// bands.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function main() {
  const zai = await ZAI.create();
  const jobs = [
    ["08-calculator y790-920 (the dialog's lower region + scrim edges)", "/tmp/v105crops/08-calculator-790-head.png", "/tmp/v105crops/08-calculator-790-new.png"],
    ["16-item-details y790-920 (the sheet's mid region + scrim edges)", "/tmp/v105crops/16-item-details-790-head.png", "/tmp/v105crops/16-item-details-790-new.png"],
    ["16-item-details y990-1050 (the meta footer region)", "/tmp/v105crops/16-item-details-990-head.png", "/tmp/v105crops/16-item-details-990-new.png"],
  ];
  for (const [label, hp, np] of jobs) {
    const res = await zai.chat.completions.createVision({
      messages: [
        {
          role: "user",
          content: [
            { type: "text", text: "These are two crops from the SAME region of two screenshots of the same app, taken one day apart (image 1 = day 1, image 2 = day 2). Report EXACTLY which text strings differ between the two images (quote the day-1 text and the day-2 text for each difference). If the region is blurred (behind a dialog scrim), read the blurred text as best you can. Be concise: list ONLY the textual differences, or say 'no readable text difference'." },
            { type: "image_url", image_url: { url: `data:image/png;base64,${b64(hp)}` } },
            { type: "image_url", image_url: { url: `data:image/png;base64,${b64(np)}` } },
          ],
        },
      ],
      thinking: { type: "disabled" },
    });
    console.log(`\n===== ${label} =====`);
    console.log(res.choices[0]?.message?.content || "NO RESPONSE");
  }
}

main().catch((e) => { console.error("VLM read failed:", e.message); process.exit(1); });
