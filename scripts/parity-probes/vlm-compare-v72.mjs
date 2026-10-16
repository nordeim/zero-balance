// vlm-compare-v72.mjs — the v72 NEW-pair program's VLM pairwise
// comparison: the DETAILS-SHEET + DRILL-DOWN mobile 390x844 twins —
// (1) the WITH-subtitle details sheet (the Rent card), (2) the
// EMPTY-subcategory details sheet (the v71 fix's sibling surface — the
// v52 sheet conditional's empty side, never shot against the reference's
// own empty-side sheet), and (3) the dashboard's drill-down EXPANDED
// state at 390 (the v67 pair's mobile twin). The sheet chrome is expected
// byte-identical per the v28 G3 census (the bottom-sheet panel, the
// scrim, the sticky header + X close, the summary block, the tinted
// classification block, the fact rows) + the v52 F1 pin (the subtitle
// P.text-lg 18/400/gray between the H3 name and the amount). Expected
// flag classes (each must be DOM-arbitrated per the v43 rule): platform
// chrome (the Base44 FAB/badge), seed/fixture-data classes (the probe
// card's own name/amount vs the reference's Miscellaneous values),
// user-identity (the avatar), and perception artifacts. A pair is CLEAN
// only when every flag arbitrates to a documented class — otherwise it
// becomes a v72 finding.
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
    "DETAILS SHEET with-subtitle (Rent) mobile 390x844 (ref vs clone — the v72 NEW-pair program)",
    "/tmp/vlm72/ref-sheet-withsub.png",
    "/tmp/vlm72/clone-sheet-withsub.png",
    `You are comparing two MOBILE VIEWPORT screenshots (390x844) of the same budget-planner web app's ITEM DETAILS SHEET — a bottom-anchored modal sheet over a dark blurred scrim. Image 1 is the REFERENCE site, image 2 is the CLONE. The sheet shows: a header row titled "Budget Item Details" with an X close button at the right, then a centered summary (an EXPENSE pill badge and a NEED pill badge, the item name "Rent" in large bold text, a gray subtitle line "Apartment", a large amount figure), a tinted classification block with an icon and description text, and fact rows (Date, Frequency, Recurring, Status) with small icons. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons, the sheet's top corners/width/position, the scrim), however small — especially clipped content or misalignment. Be precise and concise. Note: differences in DATA VALUES (dates, figures) are expected — report them separately from LAYOUT/STYLE differences.`,
  );

  await pair(
    zai,
    "DETAILS SHEET empty-subcategory mobile 390x844 (ref vs clone — the v72 NEW-pair program)",
    "/tmp/vlm72/ref-sheet-nosub.png",
    "/tmp/vlm72/clone-sheet-nosub.png",
    `You are comparing two MOBILE VIEWPORT screenshots (390x844) of the same budget-planner web app's ITEM DETAILS SHEET — a bottom-anchored modal sheet over a dark blurred scrim. Image 1 is the REFERENCE site (the "Miscellaneous" expense item), image 2 is the CLONE (a user-created "Probe NoSub" expense item). Both items carry NO subcategory — the sheet should show the name directly followed by the amount with NO subtitle line between them. The sheet shows: a header row titled "Budget Item Details" with an X close, a centered summary (EXPENSE + NEED pill badges, the item name in large bold text, NO subtitle line, a large amount figure), a tinted classification block, and fact rows (Date, Frequency, Recurring, Status). Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons, the sheet's corners/width/position, the scrim, the vertical rhythm between the name and the amount), however small. Be precise and concise. Note: differences in DATA VALUES (the item name, the amount figure, dates) are expected — report them separately from LAYOUT/STYLE differences.`,
  );

  await pair(
    zai,
    "DASHBOARD drill-down EXPANDED mobile 390x844 full-page (ref vs clone — the v72 NEW-pair program)",
    "/tmp/vlm72/ref-drilldown-mobile.png",
    "/tmp/vlm72/clone-drilldown-mobile.png",
    `You are comparing two FULL-PAGE MOBILE screenshots (390px wide) of the same budget-planner web app's DASHBOARD with the "Net Zero Breakdown" drill-down card in its EXPANDED state — the Total Income section expanded, and within it the first category row expanded showing its drill-down detail rows. Image 1 is the REFERENCE site, image 2 is the CLONE. The page shows a top bar with a hamburger menu button and logo, stat tiles, the drill-down card (Total Income / Total Expenses / Net Balance sections with amounts and chevrons; the expanded category's child rows with names, amounts, progress/frequency indicators), quick-action buttons, and other dashboard cards. Report: (1) VERDICT: IDENTICAL or DIFFERENT, (2) a list of any visual differences (layout structure, geometry, fonts, colors, spacing, borders, icons, the expanded rows' indentation and alignment), however small — especially any horizontal overflow, clipped content, or broken alignment. Be precise and concise. Note: differences in DATA (figures, section values, category names) and in the top-left avatar area are expected — report them separately from LAYOUT/STYLE differences.`,
  );
}

main().catch((e) => {
  console.error("VLM compare failed:", e.message);
  process.exit(1);
});
