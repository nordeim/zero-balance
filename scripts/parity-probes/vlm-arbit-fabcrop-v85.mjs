// vlm-arbit-fabcrop-v85.mjs — single-image VLM reads of the bottom-right
// corner crops (one image per call — no image-order confusion possible).
// The v85 income pair's NEW flag claimed the "Edit with Base44" FAB is in
// the CLONE; the pixel census says the dark FAB pixels are in the REFERENCE
// shot only. This read confirms the crop contents.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function readOne(zai, label, path) {
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "This is a cropped corner of a web page screenshot (the bottom-right 340x100 pixels). Describe exactly what UI elements are visible in this crop. Is there a dark/black floating action button with text like 'Edit with Base44'? Answer concisely.",
          },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(path)}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(`===== ${label} =====`);
  console.log(res.choices[0]?.message?.content || "NO RESPONSE");
  console.log();
}

async function main() {
  const zai = await ZAI.create();
  await readOne(zai, "REFERENCE income bottom-right crop", "/tmp/vlm85/ref-income-br.png");
  await readOne(zai, "CLONE income bottom-right crop", "/tmp/vlm85/clone-income-br.png");
}

main().catch((e) => {
  console.error("VLM crop read failed:", e.message);
  process.exit(1);
});
