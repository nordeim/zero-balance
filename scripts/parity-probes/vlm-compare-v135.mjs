// vlm-compare-v135.mjs — the standing VLM pairwise (v135: a fresh standing
// sweep of the DESKTOP 1280x800 CALCULATOR dialog + the LOGIN view — the
// re-run cycle's next-oldest candidate, the v129-era LOGIN + CALCULATOR
// pair last re-shot v129 [v129 < v130 < v131 < v132]; the pair's
// TWELFTH re-run [v59 → v66 → v75 → v81 → v87 → v93 → v99 → v105 → v111 → v117 → v123 → v129 → v135] — the FIFTY-EIGHTH
// consecutive queue/ledger agreement). Existing pins on these surfaces: the
// v45 F2a pin (row census at 1280), the v49 F3 pin (panel chrome at 640),
// the v59 pin (panel/totalCard chrome at 1280), the v66 pin (the
// row-HEIGHT family at 1280), the v73 pin (the scrim + summary-text at
// 390), the v7 G2 login-slate family + the v55 glyph pin (login icons) + the
// v87 pin (the close-button chrome census at 1280).
// The only expected differences are platform chrome (the reference's
// "Edit with Base44" FAB) + the seed-data classes (the reference's own
// Rent $25.00 vs the clone's Rent $1850 — both dialogs carry ONE
// "Contents Insurance" $25.00 monthly active row for the pair, the
// clone's added through the real UI and fully restored after the shot) —
// every flagged diff must be DOM-verified before it counts (the v43
// misattribution lesson).
import ZAI from "z-ai-web-dev-sdk";
import fs from "node:fs";

const b64 = (p) => fs.readFileSync(p).toString("base64");

async function compare(zai, label, refPath, clonePath, prompt) {
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
  console.log(`\n===== ${label} =====`);
  console.log(text);
}

async function main() {
  const zai = await ZAI.create();
  await compare(
    zai,
    "PAIR: calculator dialog desktop 1280x800 (ref vs clone, panel + row — v135 re-run)",
    "/tmp/vlm135/ref-calculator.png",
    "/tmp/vlm135/clone-calculator.png",
    `You are comparing two screenshots of the same budget-planner web app's RENT CALCULATOR dialog at desktop 1280x800 — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a modal dialog over the expenses page: a header with an orange-gradient calculator chip (white icon) + "Rent Calculator" title + "Break down your rent into individual items" subtitle + an X close button; a "Total Calculated" card with an orange amount; a "Line Items" section header with an orange-gradient "Add Item" button; and one line-item row ("Contents Insurance", frequency + status badges, $25.00, hover action buttons). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (dialog panel geometry, header layout, chip, title, close button, total card chrome, section headers, the row layout, badges, amounts, fonts, colors, spacing, shadows), however small. Be precise and concise. Note: differences in the DATA (item names, amounts, badge text) are expected and should be reported separately from LAYOUT/STYLE differences.`,
  );
  await compare(
    zai,
    "PAIR: login view desktop 1280x800 (ref vs clone — v135 re-run)",
    "/tmp/vlm135/ref-login.png",
    "/tmp/vlm135/clone-login.png",
    `You are comparing two screenshots of the same budget-planner web app's LOGIN page at desktop 1280x800 — image 1 is the REFERENCE site, image 2 is the CLONE. Both show a centered login card: a brand header (logo + "Welcome to ZeroBudget" title + subtitle), an email input, a password input, a "Sign in" button, and auth-mode links (sign up / forgot password). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences you can spot (card geometry, logo shape, fonts, colors, input chrome, button chrome, spacing, shadows, icons), however small. Be precise and concise. Note: differences in the DATA (text content) are expected and should be reported separately from LAYOUT/STYLE differences.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
