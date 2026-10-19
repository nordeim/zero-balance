// vlm-arbit-crop-v92.mjs — the SINGLE-IMAGE VLM reads of the v92 crop
// pairs (the v85 image-attribution lesson: one image per call — no
// image-order confusion possible). Each crop read independently and
// asked for its own text content; the arbitration then compares the two
// reads OFFLINE: a DATE-TEXT-ONLY delta (the day number shifting by one)
// with identical chrome confirms the v80/v86 fresh-seed DATE class.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const FILES = [
  "03-income",
  "04-expenses",
  "05-savings",
  "06-networth",
  "07-add-item-modal",
  "08-calculator",
  "16-item-details",
];

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function readCrop(path, label) {
  const zai = await ZAI.create();
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text:
              "This is a small cropped region of a budget-planner web app screenshot. " +
              "Report EXACTLY the text you can read in this crop (especially any dates), " +
              "and briefly describe any icons/chrome. Be concise and literal.",
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(path)}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  const text = res.choices[0]?.message?.content || "NO RESPONSE";
  console.log(`--- ${label} ---`);
  console.log(text);
  return text;
}

async function main() {
  for (const name of FILES) {
    console.log(`===== ${name} =====`);
    await readCrop(`/tmp/v92crops/${name}-committed.png`, `${name} COMMITTED crop`);
    await readCrop(`/tmp/v92crops/${name}-new.png`, `${name} NEW crop`);
    console.log("");
  }
}

main().catch((e) => {
  console.error("VLM crop arbitration failed:", e.message);
  process.exit(1);
});
