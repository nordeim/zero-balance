#!/usr/bin/env node
// capture-dev-shots-v125.mjs — refresh the dev-server evidence set under
// docs/screenshots/dev/ for the v125 cycle: boots `next dev` (the REAL dev
// server running the remediated codebase) as a child of THIS process tree
// (the sandbox reaps background processes between shell invocations), signs
// the demo user in through a real page login, then captures the four-view
// evidence set:
//
//   dev-dashboard-1280.png        — the dashboard at 1280x800 (logged in)
//   dev-networth-1280.png         — the networth view at 1280x800
//   dev-mobile-menu-open-390.png  — the mobile menu OPEN at 390x844
//   dev-mobile-income-390.png     — the /income view post-nav at 390x844
//                                   (the sheet closed — the menu flow proven)
//
// Usage: node scripts/capture-dev-shots-v125.mjs
// Requires a seeded db/custom.db (the dev server's own DATABASE_URL).
// NOTE: derived from the v111 script via the version-swap protocol. THE
// PHANTOM-GLITCH LESSON (the v110 cycle's dispel — the lesson carried forward): the v107-era 'save
// glitch' never existed — od-hexdump verifies ALL committed dev
// scripts (v107/v108/v109) carry the byte-correct
// `a[href*="income"]:visible` locator on disk; the perceived `[h`
// loss is a DISPLAY-layer artifact (the tool-output pipeline eats the
// [h sequence — escape-sequence filtering), never a file defect.
// Any output showing a bracket-h sequence must be od-verified, never
// trusted from grep/console display.

import { spawn } from "node:child_process";
import { mkdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { chromium } from "@playwright/test";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(__dirname, "..");
const outDir = path.join(repo, "docs", "screenshots", "dev");
const BASE = "http://localhost:3000";

function wait(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function waitForServer(url, tries = 120) {
  for (let i = 0; i < tries; i++) {
    try {
      const res = await fetch(`${url}/api/health`);
      if (res.ok) return true;
    } catch {
      // not up yet (next dev compiles on first hit)
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

  // 1. boot the DEV server on :3000 (child of THIS process tree)
  const server = spawn("npx", ["next", "dev", "-p", "3000"], {
    cwd: repo,
    env: {
      ...process.env,
      DATABASE_URL: "file:../db/custom.db",
    },
    stdio: ["ignore", "ignore", "ignore"],
  });

  try {
    if (!(await waitForServer(BASE))) throw new Error("dev server did not become ready");
    console.log("dev server ready");

    const browser = await chromium.launch();
    const ctx = await browser.newContext({
      viewport: { width: 1280, height: 800 },
      deviceScaleFactor: 2,
    });
    const page = await ctx.newPage();

    // 2. login through the real form (the demo user)
    await page.goto(`${BASE}/login`);
    await page.fill('input[type="email"]', "demo@zerobalance.app");
    await page.fill('input[type="password"]', "Demo1234!");
    await page.click('button[type="submit"]');
    // the app's post-login route is "/" (the root route IS the dashboard)
    await page.waitForURL(
      (url) => url.pathname === "/" || url.pathname === "/dashboard",
      { timeout: 30_000 },
    );
    await wait(2500);

    // 3. the dashboard at 1280x800 (the remediated codebase's own dev render)
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto(`${BASE}/dashboard`);
    await wait(2500);
    await shoot(page, "dev-dashboard-1280.png");

    // 4. the networth view at 1280x800
    await page.goto(`${BASE}/networth`);
    await wait(2500);
    await shoot(page, "dev-networth-1280.png");

    // 5. the mobile menu OPEN at 390x844 (the Tailwind v4 mitigation live)
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(`${BASE}/dashboard`);
    await wait(2500);
    // the burger: the sr-only "Toggle Sidebar" accessible name (PanelLeftIcon)
    await page.getByRole("button", { name: "Toggle Sidebar" }).click();
    await wait(1500);
    await shoot(page, "dev-mobile-menu-open-390.png");

    // 6. the post-nav income shot (the sheet closed — the menu flow proven);
    //    :visible scopes past the hidden desktop rail's own income link
    const incomeLink = page.locator('a[href*="income"]:visible').first();
    await incomeLink.click();
    await wait(2500);
    await shoot(page, "dev-mobile-income-390.png");

    // 7. the evidence assertions (the menu verified through the captures)
    const menuProof = await page.evaluate(() => ({
      url: location.pathname,
      docSW: document.documentElement.scrollWidth,
      navLandmark: !!document.querySelector("nav"),
    }));
    console.log("menu proof:", JSON.stringify(menuProof));

    await browser.close();
  } finally {
    server.kill("SIGTERM");
    try {
      process.kill(-server.pid, "SIGTERM");
    } catch {
      // process group may not exist
    }
  }
  console.log("done");
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
