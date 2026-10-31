import { defineConfig, devices } from "@playwright/test";

// E2E layer (v2.3): boots the PRODUCTION standalone server on an isolated
// port with its own scratch database (db/e2e.db, schema-pushed + seeded by
// the global setup), then drives the real UI in Chromium.
//
// Prerequisites: `bun run build` (the standalone server must exist).
// Run with: `bun run test:e2e`.
//
// Auth strategy: the "setup" project signs the demo user in ONCE and saves
// the session cookie to tests/e2e/.auth/user.json; every spec in the main
// project starts with that storageState. This is not just speed — the auth
// endpoints are rate-limited (10 attempts/IP/15 min), so per-test logins
// would trip the limiter mid-suite. tests/e2e/auth.spec.ts opts back out
// with an empty storageState because it tests the logged-out surface.
//
// The unit layer stays in Vitest (see vitest.config.ts — it matches
// *.test.ts only, so these *.spec.ts / *.setup.ts files are never picked
// up twice).

const PORT = Number(process.env.E2E_PORT ?? 3100);
// v136: back to the "localhost" NAME, with the server bound DUAL-STACK
// (HOSTNAME="::" in webServer.env below). The v135 IPv4-literal pin fixed
// the not-found:111 resolver race ([::1] → REFUSED under the IPv4-only bind)
// but introduced a second-order defect: Playwright's Node-side cookie store
// (coreBundle Cookie.matches → isLocalHostname) grants the Secure-cookie
// exemption ONLY to the string "localhost" — NOT the 127.0.0.1 literal —
// so every authenticated page.request call (the empty-states G6 fixture)
// went out with NO Cookie header → 401 (the v135 "empty-states:85
// intermittent", deterministically reproduced + root-caused this cycle —
// see docs/remediation-plan-v136.md F0). With HOSTNAME="::" the standalone
// server accepts BOTH stacks (verified live: 127.0.0.1 → 200 AND [::1] →
// 200), so the ::1-vs-IPv4 race class is dead outright and the name can
// safely return to localhost — where the Secure cookie attaches. No spec
// references any host literal (verified by grep).
const BASE_URL = `http://localhost:${PORT}`;
const E2E_DATABASE_URL = "file:../db/e2e.db";
const AUTH_STATE = "tests/e2e/.auth/user.json";

export default defineConfig({
  testDir: "./tests/e2e",
  timeout: 45_000,
  expect: { timeout: 10_000 },
  fullyParallel: false,
  workers: 1, // one worker: the specs share a single seeded SQLite file
  retries: 0,
  reporter: [["list"]],
  use: {
    baseURL: BASE_URL,
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
  },
  projects: [
    {
      name: "setup",
      testMatch: /auth\.setup\.ts/,
    },
    {
      name: "chromium",
      dependencies: ["setup"],
      testIgnore: /auth\.setup\.ts/,
      use: {
        ...devices["Desktop Chrome"],
        storageState: AUTH_STATE,
      },
    },
  ],
  globalSetup: "./tests/e2e/global-setup.ts",
  webServer: {
    command: "bun .next/standalone/server.js",
    url: `${BASE_URL}/api/health`,
    timeout: 60_000,
    reuseExistingServer: !process.env.CI,
    env: {
      ...process.env,
      PORT: String(PORT),
      // v136: bind [::] — dual-stack (IPv6 + IPv4-mapped), so "localhost"
      // connects whichever stack the resolver picks (kills the not-found:111
      // race class) and the Secure session cookie attaches to page.request
      // calls (Playwright's isLocalHostname honors "localhost" only). The
      // sandbox shell's HOSTNAME is bash-local (never exported), so this
      // override is deterministic; smoke-test.sh uses the same explicit-bind
      // pattern.
      HOSTNAME: "::",
      NODE_ENV: "production",
      DATABASE_URL: E2E_DATABASE_URL,
      AUTH_SECRET: "playwright-e2e-session-secret",
    } as Record<string, string>,
  },
});
