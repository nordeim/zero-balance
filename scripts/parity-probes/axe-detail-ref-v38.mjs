import { chromium } from "@playwright/test";
import { AxeBuilder } from "@axe-core/playwright";
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
const page = await ctx.newPage();
await page.goto("https://zero-balance-4885a8f3.base44.app/login", { waitUntil: "domcontentloaded" });
await page.fill("input[type=email]", "sepnetflix2023@outlook.com");
await page.fill("input[type=password]", "$Abcd1234");
await page.locator("form").evaluate((f) => f.requestSubmit());
await page.waitForURL((u) => !u.pathname.includes("login"));
await page.waitForTimeout(2500);
for (const route of ["/", "/income", "/networth"]) {
  await page.goto("https://zero-balance-4885a8f3.base44.app" + route, { waitUntil: "domcontentloaded" });
  await page.waitForTimeout(2500);
  const r = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]).analyze();
  for (const v of r.violations) {
    console.log(`RULE ${v.id} on ${route} (${v.nodes.length} nodes)`);
    for (const n of v.nodes) {
      const sel = n.target.join(" ");
      const color = await page.evaluate((s) => {
        const el = document.querySelector(s);
        return el ? getComputedStyle(el).color : "NO-ELEMENT";
      }, sel).catch(() => "EVAL-ERR");
      console.log(`  ${sel.slice(0, 76)} :: ${color}`);
    }
  }
}
await browser.close();
