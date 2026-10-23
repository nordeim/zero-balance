// vlm-read-devshots-v106.mjs — one-shot VLM read of the v106 dev-server
// screenshots (the dev-server evidence set): confirms the mobile menu
// sheet renders the five nav links + brand + close, and the dashboard
// renders the reference-parity chrome.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function read(zai, path, prompt) {
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: prompt },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(path)}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  const text = res.choices[0]?.message?.content || "NO RESPONSE";
  console.log(`\n===== ${path} =====`);
  console.log(text);
}

async function main() {
  const zai = await ZAI.create();
  await read(
    zai,
    "docs/screenshots/dev/dev-mobile-menu-open-390.png",
    "This is a mobile (390px wide) screenshot of a budget-planner web app with its hamburger navigation menu OPEN (a left-anchored sheet). Answer concisely: (1) Is the navigation sheet open and readable? (2) List the nav links you can see. (3) Is there a brand/logo row at the top of the sheet? (4) Any layout problems (overflow, clipped text, overlap)?",
  );
  await read(
    zai,
    "docs/screenshots/dev/dev-dashboard-1280.png",
    "This is a desktop (1280x800) screenshot of a budget-planner dashboard. Answer concisely: (1) Is the left sidebar rail visible with nav links? (2) Is the NET ZERO GOAL hero card with a progress bar visible? (3) Are the three stat cards (Total Income / Total Savings / Total Expenses) visible? (4) Is a donut chart legend visible? (5) Any layout problems?",
  );
}

main().catch((e) => {
  console.error("VLM read failed:", e.message);
  process.exit(1);
});
