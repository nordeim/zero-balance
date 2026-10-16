// vlm-compare-v73.mjs — the v73 NEW-pair program's VLM pairwise
// comparison: the LAST never-shot mobile 390x844 twins — (1) the LOGIN
// page (the simplest never-shot pair — the fresh logged-out surface;
// the v59/v66 login pairs were desktop 1280 only), and (2) the
// CALCULATOR dialog (the dialog-state surface — the v66 desktop pair's
// mobile twin; the reference's OWN Rent calculator carries its single
// Contents Insurance $25.00 line item, the clone's added through the
// real UI and fully restored after the shot — the v66 discipline).
// The login chrome is expected byte-identical per the v59/v66 pairs
// (the centered login card: the brand header [logo + "Welcome to
// ZeroBudget" title + subtitle], the email + password inputs, the
// "Sign in" button, the auth-mode links). The calculator chrome is
// expected byte-identical per the v66 census (the 48rem/85vh panel,
// the border-b header with the gradient chip + title/description +
// the 36x36 X close, the #fff7f5 Total Calculated block, the row
// inventory). Expected flag classes (each must be DOM-arbitrated per
// the v43 rule): platform chrome (the Base44 FAB), seed-data classes
// (the reference's Rent $25.00 vs the clone's Rent $1850, the
// "Will update category total" span's DATA-CONDITIONAL class), and
// perception artifacts. A pair is CLEAN only when every flag
// arbitrates to a documented class — otherwise it becomes a v73
// finding.
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function pair(zai, title, refPath, clonePath, prompt) {
  const res = await zai.chat.completions.createVision({
    messages: [
      {
        role: "user",
        content: [
          { type: "text", text: prompt },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(refPath)}` } },
          { type: "image_url", image_url: { url: `data:image/png;base64,${b64(clonePath)}` } },
        ],
      },
    ],
    thinking: { type: "disabled" },
  });
  const text = res.choices[0]?.message?.content || "NO RESPONSE";
  console.log(`===== PAIR: ${title} =====`);
  console.log(text);
  console.log();
}

async function main() {
  const zai = await ZAI.create();

  await pair(
    zai,
    "LOGIN page mobile 390x844 (ref vs clone — the v73 NEW-pair program)",
    "/tmp/vlm73/ref-login-mobile.png",
    "/tmp/vlm73/clone-login-mobile.png",
    `You are comparing two MOBILE VIEWPORT screenshots (390x844) of the same budget-planner web app's LOGIN page — a centered login card on a plain background. Image 1 is the REFERENCE site, image 2 is the CLONE. Both show: a brand header (a logo mark + "Welcome to ZeroBudget" title + a subtitle line), an email input, a password input, a "Sign in" button, and auth-mode links (sign up / forgot password). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (card geometry and width, logo shape, fonts, colors, input chrome, button chrome, spacing, shadows, icons, any corner floating button), however small. Be precise and concise. Note: differences in the DATA (text content) are expected and should be reported separately from LAYOUT/STYLE differences.`,
  );

  await pair(
    zai,
    "CALCULATOR dialog mobile 390x844 (ref vs clone — the v73 NEW-pair program)",
    "/tmp/vlm73/ref-calculator-mobile.png",
    "/tmp/vlm73/clone-calculator-mobile.png",
    `You are comparing two MOBILE VIEWPORT screenshots (390x844) of the same budget-planner web app's RENT CALCULATOR modal dialog over a dark scrim. Image 1 is the REFERENCE site, image 2 is the CLONE. Both show: a dialog header row with an orange gradient calculator icon chip, the title "Rent Calculator" and a gray description line, an X close button at the right; a tinted "Total Calculated" summary block showing a large orange amount and a small "Based on N items" line; a "Line Items" section with ONE row (a name like "Contents Insurance", an amount, badges, action buttons) and an "Add Item" button; and a footer or lower section. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (dialog geometry/width/corners, fonts, colors, spacing, borders, icons, the row's internal layout, any clipped or overflowing content at the mobile width), however small. Be precise and concise. Note: differences in DATA VALUES (the parent Rent amount context, dates) are expected — report them separately from LAYOUT/STYLE differences.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
