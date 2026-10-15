import { chromium } from "@playwright/test";
import { AxeBuilder } from "@axe-core/playwright";

// axe-detail-ref-v62.mjs — the v62 a11y re-audit (the v62 queue's top
// item, deferred from v61): re-scan the LIVE REFERENCE's axe tree and
// compare it against the v38 contract pinned in tests/e2e/a11y.spec.ts:
//
//   GATE 1 (structural): the reference fails `button-name` (its unlabeled
//   Select triggers + card kebabs) and `svg-img-alt` (its recharts donut
//   sectors) — the two structural families the clone deliberately fixes.
//
//   GATE 2 (provenance): the reference's contrast-flagged colors are the
//   7-color PARITY_PALETTE (lime/blue/orange/orangeLight/gray-500/
//   #cbd5e1/zinc-500).
//
//   The login page scans ZERO-violation clean.
//
// Drift classes to arbitrate if anything changed:
//   - a NEW structural family on the reference (the reference changed its
//     DOM/a11y tree) — the clone's superset contract may need a new pin;
//   - a NEW contrast color on the reference — if the clone mirrors the
//     design, the clone's a11y.spec.ts GATE 2 palette needs it added
//     (with this scan as the provenance evidence);
//   - a MISSING family (the reference FIXED one of its bugs) — the
//     superset contrast shrinks; document, no clone change needed.
//
// READ-ONLY discipline: login + read-only navigations only (v46 rule).
const BASE = "https://zero-balance-4885a8f3.base44.app";
const TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"];

// The a11y.spec.ts surface: six authed routes at desktop 1280x800, the
// 404, the login page (logged out), and the mobile 390x844 sheet state.
const authedRoutes = ["/", "/dashboard", "/income", "/expenses", "/savings", "/networth"];

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
const page = await ctx.newPage();

// ---- login (the zero-violation surface) ----
await page.goto(BASE + "/login", { waitUntil: "domcontentloaded" });
await page.waitForTimeout(2500);
const loginScan = await new AxeBuilder({ page }).withTags(TAGS).analyze();
console.log(`LOGIN (logged out): ${loginScan.violations.length} violations`);
for (const v of loginScan.violations) {
  console.log(`  RULE ${v.id} (${v.nodes.length} nodes)`);
}

// ---- authed scan (desktop) ----
await page.fill("input[type=email]", "sepnetflix2023@outlook.com");
await page.fill("input[type=password]", "$Abcd1234");
await page.locator("form").evaluate((f) => f.requestSubmit());
await page.waitForURL((u) => !u.pathname.includes("login"));
await page.waitForTimeout(2500);

const structural = new Map(); // rule id -> total nodes
const palette = new Set(); // contrast-flagged colors
for (const route of authedRoutes) {
  await page.goto(BASE + route, { waitUntil: "domcontentloaded" });
  await page.waitForTimeout(2500);
  const r = await new AxeBuilder({ page }).withTags(TAGS).analyze();
  const families = r.violations.map((v) => `${v.id}(${v.nodes.length})`).join(", ") || "CLEAN";
  console.log(`${route} @1280: ${families}`);
  for (const v of r.violations) {
    structural.set(v.id, (structural.get(v.id) || 0) + v.nodes.length);
    if (v.id === "color-contrast") {
      for (const n of v.nodes) {
        const sel = n.target.join(" ");
        const color = await page
          .evaluate((s) => {
            const el = document.querySelector(s);
            return el ? getComputedStyle(el).color : "NO-ELEMENT";
          }, sel)
          .catch(() => "EVAL-ERR");
        palette.add(color);
        console.log(`  cc ${sel.slice(0, 64)} :: ${color}`);
      }
    }
  }
}

// ---- the 404 (unknown path) ----
await page.goto(BASE + "/definitely-not-a-route-v62", { waitUntil: "domcontentloaded" });
await page.waitForTimeout(2500);
const nf = await new AxeBuilder({ page }).withTags(TAGS).analyze();
console.log(`404 @1280: ${nf.violations.map((v) => `${v.id}(${v.nodes.length})`).join(", ") || "CLEAN"}`);
for (const v of nf.violations) {
  if (v.id === "color-contrast") {
    for (const n of v.nodes) {
      const sel = n.target.join(" ");
      const color = await page
        .evaluate((s) => {
          const el = document.querySelector(s);
          return el ? getComputedStyle(el).color : "NO-ELEMENT";
        }, sel)
        .catch(() => "EVAL-ERR");
      palette.add(color);
      console.log(`  cc(404) ${sel.slice(0, 64)} :: ${color}`);
    }
  }
}

// ---- mobile 390x844 (the sheet-open state carries its own tree) ----
const mctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
const mpage = await mctx.newPage();
await mpage.goto(BASE + "/login", { waitUntil: "domcontentloaded" });
await mpage.fill("input[type=email]", "sepnetflix2023@outlook.com");
await mpage.fill("input[type=password]", "$Abcd1234");
await mpage.locator("form").evaluate((f) => f.requestSubmit());
await mpage.waitForURL((u) => !u.pathname.includes("login"));
await mpage.waitForTimeout(2500);

// open the mobile sheet (the reference's own burger) before scanning:
// mirror the ref-standing finder — aria-label/text "menu", else the
// top-left positional fallback.
await mpage
  .evaluate(() => {
    const b =
      [...document.querySelectorAll("button")].find(
        (x) => (x.getAttribute("aria-label") || "").includes("menu") || (x.textContent || "").includes("menu"),
      ) ||
      [...document.querySelectorAll("button")].find(
        (x) => x.getBoundingClientRect().top < 80 && x.getBoundingClientRect().left < 80 && x.getBoundingClientRect().width < 60,
      );
    if (b) b.click();
    return b ? "burger clicked" : "no burger";
  })
  .catch(() => "eval-err");
await mpage.waitForTimeout(1500);
const ms = await new AxeBuilder({ page: mpage }).withTags(TAGS).analyze();
console.log(`MOBILE / @390 sheet-open: ${ms.violations.map((v) => `${v.id}(${v.nodes.length})`).join(", ") || "CLEAN"}`);
await mctx.close();

// ---- the v38-contract verdict ----
console.log("\n=== THE v38 CONTRACT VERDICT ===");
console.log("structural families:", JSON.stringify([...structural.entries()]));
console.log("contrast palette:", JSON.stringify([...palette]));
const v38Palette = [
  "rgb(143, 188, 63)",
  "rgb(59, 126, 161)",
  "rgb(224, 122, 59)",
  "rgb(245, 169, 98)",
  "rgb(107, 114, 128)",
  "rgb(203, 213, 225)",
  "rgb(115, 115, 115)",
];
const newColors = [...palette].filter((c) => !v38Palette.includes(c));
console.log(
  newColors.length === 0
    ? "PALETTE: IDENTICAL to v38 (no new reference contrast colors)"
    : `PALETTE DRIFT — colors outside the v38 set: ${JSON.stringify(newColors)}`,
);
const structuralIds = [...structural.keys()].filter((id) => id !== "color-contrast");
console.log(
  structuralIds.length === 0
    ? "STRUCTURAL: reference now CLEAN (a family was FIXED — the superset contrast shrinks)"
    : `STRUCTURAL families on the reference: ${JSON.stringify(structuralIds)} (v38 record: button-name + svg-img-alt)`,
);

await browser.close();
