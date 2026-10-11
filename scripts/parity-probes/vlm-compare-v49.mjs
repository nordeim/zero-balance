// vlm-compare-v49.mjs — the standing VLM pairwise (v49: the LOGIN page
// at 390x844 mobile — THE FIXED SURFACE: the v49 F1 spacer lifted the
// clone's card stack to the reference's y 57; the pre-fix clone sat
// 24px lower). The login page is data-free (a static form) — the only
// expected differences are platform chrome (the reference's
// "Edit with Base44" FAB). Every flagged diff must be DOM-verified
// before it counts — the v43 misattribution lesson.
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
            text: `You are comparing two screenshots of the same budget-planner web app's LOGIN page (390x844 mobile viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a centered login card (logo, "Welcome to ZeroBudget" heading, Continue with Google button, email/password sign-in form) on a light gradient page. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (card position in the viewport, layout, colors, fonts, spacing, buttons, icons), however small — especially the vertical position of the card. Be precise and concise.`,
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
    "PAIR: login page 390x844 (ref vs clone, v49 fixed surface)",
    "/tmp/vlm49/ref-login.png",
    "/tmp/vlm49/clone-login.png",
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
