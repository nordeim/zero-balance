// vlm-compare-v50.mjs — the standing VLM pairwise (v50: the LOGIN
// page's SIGN-UP state at 390x844 mobile — THE FIXED SURFACE: the v50
// F1 restore lifted the clone's sign-up panel from 406 to the
// reference's 422 — the heading no longer overlaps the back button).
// The sign-up form is data-free (a static form) — the only expected
// differences are platform chrome (the reference's "Edit with Base44"
// FAB). Every flagged diff must be DOM-verified before it counts —
// the v43 misattribution lesson.
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
            text: `You are comparing two screenshots of the same budget-planner web app's SIGN-UP page (390x844 mobile viewport) — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a centered card (logo, "Create your account" heading, a "Back to sign in" link above it, email/password/confirm-password form, "Create account" button) on a light gradient page. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (card position in the viewport, layout, colors, fonts, spacing, buttons, icons), however small — especially the spacing between the "Back to sign in" link and the heading. Be precise and concise.`,
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
    "PAIR: login sign-up state 390x844 (ref vs clone, v50 fixed surface)",
    "/tmp/vlm50/ref-signup.png",
    "/tmp/vlm50/clone-signup.png",
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
