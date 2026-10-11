// axe-detail-v39.mjs — the MOBILE color-provenance enumeration (the v39
// GATE 2 evidence for the mobile a11y-gate extension). Enumerates every
// color-contrast node on the clone's mobile routes (390×844, isMobile,
// hasTouch — the same emulation as the mobile-navigation spec) with its
// computed color, so the mobile gate's palette provenance is verified the
// same way the v38 desktop gate was.
// Usage (INSIDE with-server.sh): node scripts/parity-probes/axe-detail-v39.mjs
import { chromium } from "@playwright/test";
import { AxeBuilder } from "@axe-core/playwright";

const ROUTES = ["/", "/dashboard", "/income", "/expenses", "/savings", "/networth"];
const browser = await chromium.launch();
const ctx = await browser.newContext({
  viewport: { width: 390, height: 844 },
  hasTouch: true,
  isMobile: true,
});
const page = await ctx.newPage();
await page.goto("https://zero-balance-4885a8f3.base44.app/login", { waitUntil: "domcontentloaded" });
await page.fill("input[type=email]", "sepnetflix2023@outlook.com");
await page.fill("input[type=password]", "$Abcd1234");
await page.locator("form").evaluate((f) => f.requestSubmit());
await page.waitForURL((u) => !u.pathname.includes("login"));
await page.waitForTimeout(2500);
for (const route of ROUTES) {
  await page.goto(`https://zero-balance-4885a8f3.base44.app${route}`, { waitUntil: "domcontentloaded" });
  await page.waitForTimeout(2500);
  const r = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]).analyze();
  for (const v of r.violations) {
    console.log(`ROUTE ${route} RULE ${v.id} (${v.nodes.length} nodes)`);
    for (const n of v.nodes) {
      const sel = n.target.join(" ");
      const color = await page
        .evaluate((s) => {
          const el = document.querySelector(s);
          return el ? getComputedStyle(el).color : "NO-ELEMENT";
        }, sel)
        .catch(() => "EVAL-ERR");
      console.log(`  ${sel.slice(0, 80)} :: ${color}`);
    }
  }
}
await browser.close();
