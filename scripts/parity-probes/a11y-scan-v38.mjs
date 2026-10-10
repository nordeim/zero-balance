// a11y-scan-v38.mjs — the exploratory axe-core deep scan (both sites).
// Usage: node scripts/parity-probes/a11y-scan-v38.mjs clone|ref
//   clone → http://localhost:3200 (run INSIDE with-server.sh)
//   ref   → the live reference site
// Read-only: axe injects + reads; no mutating clicks. The reference scan
// documents the superset story (which rules the reference fails that the
// clone passes); the clone scan drives the permanent tests/e2e/a11y.spec.ts
// gate + its documented allow-list.
import { chromium } from "@playwright/test";
import { AxeBuilder } from "@axe-core/playwright";

const TARGET = process.argv[2] ?? "clone";
const BASE =
  TARGET === "ref"
    ? "https://zero-balance-4885a8f3.base44.app"
    : "http://localhost:3200";
const CREDS =
  TARGET === "ref"
    ? { email: "sepnetflix2023@outlook.com", password: "$Abcd1234" }
    : { email: "demo@zerobalance.app", password: "Demo1234!" };

const ROUTES = ["/", "/dashboard", "/income", "/expenses", "/savings", "/networth"];

const summarize = (results, route) => {
  const violations = results.violations.map((v) => ({
    id: v.id,
    impact: v.impact,
    help: v.help,
    nodes: v.nodes.map((n) => ({
      target: n.target.join(" ").slice(0, 90),
      html: n.html.slice(0, 110),
      summary: (n.failureSummary || "").split("\n").slice(0, 3).join(" | ").slice(0, 140),
    })).slice(0, 6),
    nodeCount: v.nodes.length,
  }));
  return { route, violationCount: results.violations.length, violations };
};

const browser = await chromium.launch();
try {
  // ---- Logged-in routes (shared context) ----
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const page = await ctx.newPage();
  await page.goto(`${BASE}/login`, { waitUntil: "domcontentloaded" });
  await page.fill("input[type=email]", CREDS.email);
  await page.fill("input[type=password]", CREDS.password);
  await page.locator("form").evaluate((f) => f.requestSubmit());
  await page.waitForURL((u) => !u.pathname.includes("login"), { timeout: 20000 });
  await page.waitForTimeout(2500);

  for (const route of ROUTES) {
    await page.goto(`${BASE}${route}`, { waitUntil: "domcontentloaded" });
    // settle: wait for the boot data (a card heading or the h1 + content)
    await page.waitForTimeout(2500);
    const results = await new AxeBuilder({ page })
      .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
      .analyze();
    console.log(JSON.stringify(summarize(results, route)));
  }

  // ---- The 404 page (same context, unknown route) ----
  await page.goto(`${BASE}/this-route-does-not-exist`, { waitUntil: "domcontentloaded" });
  await page.waitForTimeout(1500);
  const nf = await new AxeBuilder({ page })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  console.log(JSON.stringify(summarize(nf, "/404")));

  await ctx.close();

  // ---- The login page (fresh logged-out context) ----
  const lctx = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  const lpage = await lctx.newPage();
  await lpage.goto(`${BASE}/login`, { waitUntil: "domcontentloaded" });
  await lpage.waitForTimeout(1500);
  const login = await new AxeBuilder({ page: lpage })
    .withTags(["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"])
    .analyze();
  console.log(JSON.stringify(summarize(login, "/login")));
  await lctx.close();
} finally {
  await browser.close();
}
