// probe-securecookie-v136.mjs — the conclusive mechanism probe.
// Boots nothing: uses playwright.chromium directly with the saved storageState,
// then makes the same page.request GET against BOTH host forms to show the
// cookie-attach asymmetry (secure cookie + http://127.0.0.1 vs http://localhost).
import { chromium } from "@playwright/test";
import { spawn } from "node:child_process";
import { readFileSync } from "node:fs";

const PORT = 3101;
const server = spawn("bun", [".next/standalone/server.js"], {
  env: {
    ...process.env,
    PORT: String(PORT),
    NODE_ENV: "production",
    DATABASE_URL: "file:../db/e2e.db",
    AUTH_SECRET: "playwright-e2e-session-secret",
  },
  stdio: ["ignore", "pipe", "pipe"],
});

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function waitHealthy() {
  for (let i = 0; i < 60; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${PORT}/api/health`);
      if (res.ok) return true;
    } catch {}
    await sleep(500);
  }
  return false;
}

try {
  const healthy = await waitHealthy();
  console.log("server healthy:", healthy);
  if (!healthy) process.exit(1);

  // Login via a raw fetch to capture the Set-Cookie EXACTLY as the server sends it.
  const loginRes = await fetch(`http://127.0.0.1:${PORT}/api/auth/login`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ email: "demo@zerobalance.app", password: "Demo1234!" }),
  });
  console.log("login status:", loginRes.status);
  const setCookie = loginRes.headers.get("set-cookie");
  console.log("set-cookie (first 160):", (setCookie || "").slice(0, 160));

  // Now the playwright-side check: storageState cookie + page.request to both hosts.
  const state = JSON.parse(readFileSync("tests/e2e/.auth/user.json", "utf8"));
  console.log("storageState cookie: domain=%s secure=%s", state.cookies[0].domain, state.cookies[0].secure);

  const browser = await chromium.launch();
  const context = await browser.newContext({ storageState: "tests/e2e/.auth/user.json" });
  const page = await context.newPage();

  for (const host of ["127.0.0.1", "localhost"]) {
    // Log in through the APIRequestContext bound to this context so the cookie
    // lands in the context jar with the domain matching THIS host.
    const login = await page.request.post(`http://${host}:${PORT}/api/auth/login`, {
      data: { email: "demo@zerobalance.app", password: "Demo1234!" },
    });
    const res = await page.request.get(`http://${host}:${PORT}/api/liabilities`);
    console.log(
      `host=${host}: login=${login.status()} GET /api/liabilities -> ${res.status()} ${res.status() === 200 ? "(cookie attached)" : "(NO cookie)"}`,
    );
  }
  await browser.close();
} finally {
  server.kill("SIGKILL");
}
