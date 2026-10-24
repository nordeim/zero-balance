// VLM read of the 07 delta band: identify the exact text that changed
// between the committed HEAD crop and the regenerated crop.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function main() {
  const zai = await ZAI.create();
  const completion = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          {
            type: "text",
            text: "Two crops of the same region of an add-item modal from a budget app. Image 1 is the older capture (HEAD), Image 2 the newer. Report EXACTLY what text differs between them — quote the differing text in each image verbatim. If the only difference is a date or number, say so plainly.",
          },
          {
            type: "image_url",
            image_url: { url: `data:image/png;base64,${b64("/tmp/v109crops/07-band-head.png")}` },
          },
          {
            type: "image_url",
            image_url: { url: `data:image/png;base64,${b64("/tmp/v109crops/07-band-new.png")}` },
          },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  console.log(completion.choices[0]?.message?.content ?? "no content");
}

main().catch((e) => { console.error(e.message); process.exit(1); });
