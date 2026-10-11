// a11y-scan-v39.mjs — the MOBILE extension of the v38 a11y gate (v39's
// headline surface). Usage: node scripts/parity-probes/a11y-scan-v39.mjs clone|ref
//   clone → http://localhost:3200 (run INSIDE with-server.sh)
//   ref   → the live reference site
// What it measures, at the reference's own mobile viewport (390×844,
// isMobile + hasTouch, the mobile-navigation.spec.ts emulation):
//   1. every authed route, sheet-closed booted state (mobile chrome census)
//   2. the sheet-OPEN state on / (dashboard) — the mobile navigation menu
//      itself, the user's standing task focus
// Read-only EXCEPT the sheet-open click (a navigation toggle, no data
// mutation; the sheet is Escape-closed after the scan). The reference's
// burger is clicked via JS el.click() — its toast viewport intercepts the
// REAL pointer hit at the burger's center (the R1 bug), so a hit-tested
// click would open nothing on the reference.
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
const TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"];

const summarize = (results, route) => {
  const violations = results.violations.map((v) => ({
    id: v.id,
    impact: v.impact,
    nodeCount: v.nodes.length,
    nodes: v.nodes.map((n) => ({
      target: n.target.join(" ").slice(0, 90),
      html: n.html.slice(0, 110),
    })).slice(0, 8),
  }));
  return { target: TARGET, route, viewport: "390x844", violationCount: results.violations.length, violations };
};

const browser = await chromium.launch();
try {
  const ctx = await browser.newContext({
    viewport: { width: 390, height: 844 },
    hasTouch: true,
    isMobile: true,
  });
  const page = await ctx.newPage();
  await page.goto(`${BASE}/login`, { waitUntil: "domcontentloaded" });
  await page.fill("input[type=email]", CREDS.email);
  await page.fill("input[type=password]", CREDS.password);
  await page.locator("form").evaluate((f) => f.requestSubmit());
  await page.waitForURL((u) => !u.pathname.includes("login"), { timeout: 20000 });
  await page.waitForTimeout(2500);

  // ---- 1. every authed route, sheet closed ----
  for (const route of ROUTES) {
    await page.goto(`${BASE}${route}`, { waitUntil: "domcontentloaded" });
    await page.waitForTimeout(2500);
    const results = await new AxeBuilder({ page }).withTags(TAGS).analyze();
    console.log(JSON.stringify(summarize(results, route)));
  }

  // ---- 2. the sheet-OPEN state on / ----
  await page.goto(`${BASE}/`, { waitUntil: "domcontentloaded" });
  await page.waitForTimeout(2500);
  // JS click: bypasses the reference's toast-viewport hit interception (R1).
  const opened = await page.evaluate(() => {
    const named = [...document.querySelectorAll("button")].find((x) => {
      const al = x.getAttribute("aria-label") || "";
      return al.includes("Toggle Sidebar") || al.includes("menu") || al.toLowerCase().includes("menu");
    });
    const btn =
      named ||
      [...document.querySelectorAll("button")].find((x) => {
        const r = x.getBoundingClientRect();
        const c = (x.className || "").toString();
        return r.top < 80 && r.left < 60 && r.width < 60;
      });
    if (!btn) return "NO BURGER FOUND";
    btn.click();
    return `clicked: ${btn.getAttribute("aria-label") || btn.className}`;
  });
  await page.waitForTimeout(1200);
  const sheetInfo = await page.evaluate(() => {
    const nav = document.querySelector("nav");
    const sheet = document.querySelector("[data-state='open']");
    const sheetLinks = [...document.querySelectorAll("a")].filter((a) => {
      const r = a.getBoundingClientRect();
      return r.width > 0 && r.height > 0 && ["Dashboard", "Income", "Expenses", "Savings", "Net Worth"].some(
        (t) => (a.textContent || "").trim().includes(t),
      );
    });
    return JSON.stringify({
      hasNavLandmark: !!nav,
      navInSheet: !!(nav && sheet && sheet.contains(nav)),
      visibleNavLinks: sheetLinks.length,
      bodyOverflow: getComputedStyle(document.body).overflow,
    });
  });
  console.log(JSON.stringify({ target: TARGET, phase: "sheet-open-structure", opened, sheetInfo }));
  const openResults = await new AxeBuilder({ page }).withTags(TAGS).analyze();
  console.log(JSON.stringify(summarize(openResults, "/ (sheet open)")));
  // close the sheet (restore state): Escape
  await page.keyboard.press("Escape");
  await page.waitForTimeout(600);

  await ctx.close();
} finally {
  await browser.close();
}
