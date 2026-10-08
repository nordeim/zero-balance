#!/usr/bin/env node
// capture-screenshots.mjs — regenerate the docs/screenshots set for
// ZeroBalance in ONE invocation: boots the production standalone server as
// a child process (the sandbox reaps background processes between shell
// invocations, so the server and the captures must share one process
// tree), signs the demo user in through a real page login, then shoots the
// catalog:
//
//   01-login · 02-dashboard · 03-income · 04-expenses · 05-savings ·
//   06-networth · 07-add-item-modal · 08-calculator ·
//   09-mobile-dashboard (390×844) · 10-mobile-menu (the open sheet) ·
//   11-breakdown-drilldown (the expandable Net Zero Breakdown) ·
//   12-mobile-networth (the responsive summary card, superset fix #6) ·
//   13-not-found (the reference's custom 404 — plan v7 G7) ·
//   14-login-error (the reference's error-banner — plan v12 G1) ·
//   15-forgot-reset (the forgot confirmation state — plan v12 G4)
//
// Usage:   node scripts/capture-screenshots.mjs
// Requires `bun run build` (the standalone server) + a seeded db/custom.db.

import { spawn } from "node:child_process";
import { mkdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "@playwright/test";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(__dirname, "..");
const outDir = path.join(repo, "docs", "screenshots");
const BASE = "http://localhost:3100";

function wait(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function waitForServer(url, tries = 60) {
  for (let i = 0; i < tries; i++) {
    try {
      const res = await fetch(`${url}/api/health`);
      if (res.ok) return true;
    } catch {
      // not up yet
    }
    await wait(1000);
  }
  return false;
}

async function shoot(page, name) {
  const file = path.join(outDir, name);
  await page.screenshot({ path: file, fullPage: false });
  console.log(`captured ${name}`);
}

async function main() {
  mkdirSync(outDir, { recursive: true });

  // 1. boot the standalone server on :3100 (child of THIS process tree)
  const server = spawn("bun", [".next/standalone/server.js"], {
    cwd: repo,
    env: {
      ...process.env,
      DATABASE_URL: "file:../db/custom.db",
      PORT: "3100",
      NODE_ENV: "production",
      HOSTNAME: "127.0.0.1",
    },
    stdio: ["ignore", "inherit", "inherit"],
  });

  try {
    if (!(await waitForServer(BASE))) throw new Error("server did not become ready");
    console.log("server ready");

    const browser = await chromium.launch();
    const ctx = await browser.newContext({
      viewport: { width: 1440, height: 900 },
      deviceScaleFactor: 2,
    });
    const page = await ctx.newPage();

    // 2. login page (logged-out state)
    await page.goto(`${BASE}/login`, { waitUntil: "networkidle" });
    await shoot(page, "01-login.png");

    // 2b. the login ERROR banner (plan v12 G1 — the reference's red-tinted
    //     bordered FormMessage banner; one failed attempt, within the
    //     rate-limit budget)
    await page.getByLabel("Email").fill("demo@zerobalance.app");
    await page.getByLabel("Password").fill("definitely-wrong");
    await page.getByRole("button", { name: "Sign in" }).click();
    await page.getByText("Invalid email or password").waitFor();
    await wait(300);
    await shoot(page, "14-login-error.png");

    // 2c. the forgot-password confirmation state (plan v12 G4 — the
    //     reference's "Check your email" layout with honest copy), then
    //     back to the clean sign-in card for the real login below.
    await page.getByRole("button", { name: "Forgot password?" }).click();
    await page.getByRole("heading", { name: "Reset your password" }).waitFor();
    await page.getByLabel("Email").fill("demo@zerobalance.app");
    await page.getByRole("button", { name: "Send reset link" }).click();
    await page.getByRole("heading", { name: "Password reset unavailable" }).waitFor();
    await wait(300);
    await shoot(page, "15-forgot-reset.png");
    await page.getByRole("button", { name: "Back to sign in" }).click();
    await page.getByRole("heading", { name: "Welcome to ZeroBudget" }).waitFor();

    // 3. real login → dashboard (the ROOT route — the reference lands on /
    //    after sign-in, plan v7 G1)
    await page.getByLabel("Email").fill("demo@zerobalance.app");
    await page.getByLabel("Password").fill("Demo1234!");
    await page.getByRole("button", { name: "Sign in" }).click();
    await page.waitForURL(/\/$/);
    await page.getByText("+$2065.00").waitFor();
    await page.locator(".recharts-sector").first().waitFor();
    await wait(600); // donut entrance animation
    await shoot(page, "02-dashboard.png");

    // 4. the four nav views
    for (const [route, name, readyText] of [
      ["income", "03-income.png", "2 items · $5550.00"],
      ["expenses", "04-expenses.png", "3 items · $2235.00"],
      ["savings", "05-savings.png", "2 items · $1250.00"],
      ["networth", "06-networth.png", "Total Net Worth"],
    ]) {
      await page.goto(`${BASE}/${route}`, { waitUntil: "networkidle" });
      await page.getByText(readyText).first().waitFor();
      await wait(250);
      await shoot(page, name);
    }

    // 5. Add Item modal (dashboard context, Expense preselected)
    await page.goto(`${BASE}/dashboard`, { waitUntil: "networkidle" });
    await page.getByText("+$2065.00").waitFor();
    await page.getByRole("button", { name: "Add Item" }).click();
    await page.getByRole("dialog").waitFor();
    await wait(350);
    await shoot(page, "07-add-item-modal.png");
    await page.getByRole("button", { name: "Cancel" }).click();

    // 5b. the breakdown drill-down (expand Income → Salary → item rows)
    const breakdown = page.locator("div.rounded-2xl").filter({ hasText: "Net Zero Breakdown" }).first();
    await breakdown.getByRole("button", { name: /Total Income/ }).click();
    await breakdown.getByRole("button", { name: /^Salary/ }).click();
    await breakdown.getByText("Net monthly salary").waitFor();
    await wait(300);
    await shoot(page, "11-breakdown-drilldown.png");

    // 6. Rent Calculator with one line item (expense cards reveal their
    // Edit/Calculate row on hover — a real hover first)
    await page.goto(`${BASE}/expenses`, { waitUntil: "networkidle" });
    await page.getByText("3 items · $2235.00").waitFor();
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    await page.getByRole("dialog").waitFor();
    await page.getByRole("button", { name: "Add Item" }).click();
    await page.getByLabel("Item Name *").fill("Contents Insurance");
    await page.getByLabel("Amount *").fill("25");
    await page.getByRole("button", { name: "Save Item" }).click();
    await page.getByText("Contents Insurance").waitFor();
    await wait(350);
    await shoot(page, "08-calculator.png");
    // clean up the line item + recalculated parent (seed hygiene): deleting
    // the line item leaves the parent at $0.00 (the recalculated line total),
    // so restore the seed's $1,850.00 through the real edit flow — the next
    // run's "3 items · $2,235.00" wait depends on it.
    await page.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await page.getByRole("button", { name: "Delete", exact: true }).click();
    await page.getByText("Based on 0 items").waitFor();
    // Close via the explicit X (Escape can race the delete's re-render and
    // leave the overlay up, blocking every later interaction).
    const calcDialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await calcDialog.getByRole("button", { name: "Close" }).click();
    await calcDialog.waitFor({ state: "hidden" });
    await page.waitForTimeout(500);
    // Expense cards carry no ellipsis (reference parity) — restore through
    // the hover-revealed Edit button.
    await rent.hover();
    await rent.getByRole("button", { name: "Edit", exact: true }).click();
    const editDialog = page.getByRole("dialog", { name: "Edit Budget Item" });
    await editDialog.getByLabel("Amount").fill("1850");
    await editDialog.getByRole("button", { name: "Save Item" }).click();
    await page.getByText("3 items · $2235.00").waitFor();

    // 7. mobile chrome (390×844) — a separate context: carry the session
    // over with a real API login (cookies live in the context).
    const mobile = await browser.newContext({
      viewport: { width: 390, height: 844 },
      deviceScaleFactor: 2,
      isMobile: true,
      hasTouch: true,
    });
    await mobile.request.post(`${BASE}/api/auth/login`, {
      data: { email: "demo@zerobalance.app", password: "Demo1234!" },
    });
    const mpage = await mobile.newPage();
    await mpage.goto(`${BASE}/dashboard`, { waitUntil: "networkidle" });
    await mpage.getByRole("heading", { name: "Budget Dashboard" }).waitFor();
    await shoot(mpage, "09-mobile-dashboard.png");

    // 8. the open mobile menu (proves the hamburger works — superset fix #1)
    await mpage.getByRole("button", { name: "Toggle Sidebar" }).click();
    await mpage.locator("[data-state='open'].fixed.inset-y-0").waitFor();
    await wait(450);
    await shoot(mpage, "10-mobile-menu.png");
    await mpage.getByRole("link", { name: "Dashboard" }).click();
    await mpage.waitForTimeout(400); // sheet closes on nav (superset fix #2)

    // 9. mobile net worth — documents superset fix #6 (the responsive
    // summary card; the reference's own /networth overflows to 464px here)
    await mpage.goto(`${BASE}/networth`, { waitUntil: "networkidle" });
    await mpage.getByText("Total Net Worth").waitFor();
    await wait(300);
    await shoot(mpage, "12-mobile-networth.png");

    // 10. the custom 404 (plan v7 G7 — the reference's branded not-found;
    // needs a logged-OUT context so the demo session is not required)
    const anon = await browser.newContext({
      viewport: { width: 1440, height: 900 },
      deviceScaleFactor: 2,
    });
    const apage = await anon.newPage();
    await apage.goto(`${BASE}/nonexistent-page-xyz`, { waitUntil: "networkidle" });
    await apage.getByRole("heading", { name: "Page Not Found" }).waitFor();
    await wait(300);
    await shoot(apage, "13-not-found.png");
    await anon.close();

    await browser.close();
    console.log("done");
  } finally {
    server.kill("SIGTERM");
  }
}

main().catch((err) => {
  console.error(err);
  process.exitCode = 1;
});
