import { chromium } from "@playwright/test";
import { AxeBuilder } from "@axe-core/playwright";
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
const page = await ctx.newPage();
await page.goto("http://localhost:3200/login", { waitUntil: "domcontentloaded" });
await page.fill("input[type=email]", "demo@zerobalance.app");
await page.fill("input[type=password]", "Demo1234!");
await page.locator("form").evaluate((f) => f.requestSubmit());
await page.waitForURL((u) => !u.pathname.includes("login"));
await page.waitForTimeout(2500);
await page.goto("http://localhost:3200/", { waitUntil: "domcontentloaded" });
await page.waitForTimeout(2500);
const r = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"]).analyze();
for (const v of r.violations) {
  console.log(`RULE ${v.id} (${v.nodes.length} nodes)`);
  for (const n of v.nodes) {
    const sel = n.target.join(" ");
    const color = await page.evaluate((s) => {
      const el = document.querySelector(s);
      return el ? getComputedStyle(el).color : "NO-ELEMENT";
    }, sel).catch(() => "EVAL-ERR");
    console.log(`  ${sel.slice(0, 80)} :: ${color}`);
  }
}
await browser.close();
