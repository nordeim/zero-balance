// vlm-compare-v71.mjs — the v71 NEW-pair program's VLM pairwise
// comparison: the ITEMS views' MOBILE 390x844 full-page twins —
// (1) /INCOME, (2) /EXPENSES and (3) /SAVINGS — the below-the-fold 390
// surfaces never individually shot (the standing-pair matrix extension;
// the desktop items pairs were covered by v57/v64/v70). The chrome is
// expected byte-identical per the v52 F2/F3 mobile censuses (the header
// row, the filter card, the search, the item grid at 390) + the v57/v58
// footer + badge-row pins. Expected flag classes (each must be
// DOM-arbitrated per the v43 rule): platform chrome (the Base44
// FAB/badge), seed-data classes (the reference's own 1-income data vs
// the clone's dev seed), user-identity (the avatar), the v57 badge-wrap
// class (the clone's 4th Recurring superset badge), the v57
// DATA-CONDITIONAL footer class (paymentMethod), and perception
// artifacts. A pair is CLEAN only when every flag arbitrates to a
// documented class — otherwise it becomes a v71 finding.
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
    "INCOME mobile 390x844 full-page (ref vs clone — the v71 NEW-pair program)",
    "/tmp/vlm71/ref-income-mobile.png",
    "/tmp/vlm71/clone-income-mobile.png",
    `You are comparing two FULL-PAGE MOBILE screenshots (390px wide) of the same budget-planner web app's INCOME page — image 1 is the REFERENCE site, image 2 is the CLONE. The page shows a top bar with a hamburger menu button and logo, an "Income" header with a chip icon and Add button, a white filter card (search input + comboboxes), and income item cards (each card: a title with a colored dot, a subtitle, an amount, badge chips like frequency/classification, a footer with dates). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons), however small — especially any horizontal overflow, clipped content, or broken alignment. Be precise and concise. Note: differences in the DATA (figures, card counts, card contents, subcategory texts) and in the top-left avatar area are expected — report them separately from LAYOUT/STYLE differences.`,
  );

  await pair(
    zai,
    "EXPENSES mobile 390x844 full-page (ref vs clone — the v71 NEW-pair program)",
    "/tmp/vlm71/ref-expenses-mobile.png",
    "/tmp/vlm71/clone-expenses-mobile.png",
    `You are comparing two FULL-PAGE MOBILE screenshots (390px wide) of the same budget-planner web app's EXPENSES page — image 1 is the REFERENCE site, image 2 is the CLONE. The page shows a top bar with a hamburger menu button and logo, an "Expenses" header with a chip icon and Add button, a white filter card (search input + three comboboxes), and expense item cards (each card: a title with a colored dot, a subtitle, an amount, badge chips, a footer with dates, Edit/Calculate action buttons). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons), however small — especially any horizontal overflow, clipped content, or broken alignment. Be precise and concise. Note: differences in the DATA (figures, card counts, card contents, subcategory texts) and in the top-left avatar area are expected — report them separately from LAYOUT/STYLE differences.`,
  );

  await pair(
    zai,
    "SAVINGS mobile 390x844 full-page (ref vs clone — the v71 NEW-pair program)",
    "/tmp/vlm71/ref-savings-mobile.png",
    "/tmp/vlm71/clone-savings-mobile.png",
    `You are comparing two FULL-PAGE MOBILE screenshots (390px wide) of the same budget-planner web app's SAVINGS page — image 1 is the REFERENCE site, image 2 is the CLONE. The page shows a top bar with a hamburger menu button and logo, a "Savings" header with a chip icon and Add button, a white filter card (search input + comboboxes), and savings goal cards (each card: a title with a colored dot, a subtitle, an amount, badge chips, a footer with a date). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons), however small — especially any horizontal overflow, clipped content, or broken alignment. Be precise and concise. Note: differences in the DATA (figures, card counts, card contents, subcategory texts) and in the top-left avatar area are expected — report them separately from LAYOUT/STYLE differences.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
