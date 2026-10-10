import { expect, test } from "@playwright/test";
import { AxeBuilder } from "@axe-core/playwright";

// A11y gate (v38 — the session-72 tooling pass, F1 in
// docs/remediation-plan-v38.md). There is no hosted CI, so this spec IS
// the "a11y CI step": the local clean-check gate runs it with the rest of
// the e2e suite on every change.
//
// The contract, measured live on BOTH sites this session (a11y-scan-v38
// .mjs + axe-detail-v38.mjs / axe-detail-ref-v38.mjs, axe-core 4.13):
//
//  1. GATE 1 (structural): the clone must show NO axe violation other
//     than color-contrast. The reference FAILS two structural families
//     the clone passes — `button-name` (critical: its unlabeled Select
//     triggers + card kebabs) and `svg-img-alt` (its recharts donut
//     sectors path[name=…]). A regression here (a lost aria-label, an
//     accessible-name bug, a stray img) fails the gate.
//
//  2. GATE 2 (provenance): every color-contrast node the clone flags
//     must carry one of the reference's OWN measured palette colors —
//     the 1:1 node enumeration matched both sites color-for-color. The
//     contrast failures are the reference's parity-pinned design (its
//     lime/blue/orange type accents, its hero status color, its 404
//     slate); a NEW low-contrast color (outside the palette) fails the
//     gate even though the rule id is allow-listed.
//
// The login page scans ZERO-violation clean on both sites — no allow-list
// needed there.

// The reference's own axe-flagged colors, measured on the live reference
// this session (axe-detail-ref-v38.mjs):
const PARITY_PALETTE = new Set([
  "rgb(143, 188, 63)", // limeGreen — income accents (breakdown rows, card amounts, guidelines)
  "rgb(59, 126, 161)", // blueMedium — savings accents
  "rgb(224, 122, 59)", // orangeDark — expense accents
  "rgb(245, 169, 98)", // orangeLight — the hero's Under Budget status label
  "rgb(107, 114, 128)", // gray-500 — a stat-card sublabel on its tinted card
  "rgb(203, 213, 225)", // #cbd5e1 — the 404 h1
  "rgb(115, 115, 115)", // zinc-500 — the net-worth inactive Liabilities tab
]);

const TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"];

async function assertParityClean(page: import("@playwright/test").Page, route: string) {
  // Let transitions settle (the repo's ~300ms discipline) before the scan.
  await page.waitForTimeout(2500);
  const results = await new AxeBuilder({ page }).withTags(TAGS).analyze();

  // GATE 1 — structural: only color-contrast may appear.
  for (const v of results.violations) {
    expect(
      v.id,
      `non-parity a11y violation on ${route} — ${v.help} (${v.nodes.length} nodes, first: ${v.nodes[0]?.target.join(" ")})`,
    ).toBe("color-contrast");
  }

  // GATE 2 — provenance: every flagged color is the reference's own.
  for (const v of results.violations) {
    for (const node of v.nodes) {
      const selector = node.target.join(" ");
      const color = await page.evaluate((sel) => {
        const el = document.querySelector(sel);
        return el ? getComputedStyle(el).color : null;
      }, selector);
      expect(color, `flagged node did not resolve on ${route}: ${selector}`).toBeTruthy();
      expect(
        PARITY_PALETTE.has(color as string),
        `${route}: color-contrast flagged a color OUTSIDE the reference's pinned palette (${color}) on ${selector} — a new low-contrast color crept in`,
      ).toBe(true);
    }
  }
}

test.describe("a11y gate (v38 F1 — the session-72 tooling pass)", () => {
  // The authed routes: the shared storageState replays the demo session.
  // Each test waits for a seeded content marker first — since v15 the
  // item-view pages prerender the full-screen loading overlay, and the
  // scan must run against the BOOTED DOM.
  const authed: Array<[route: string, marker: string]> = [
    ["/", "Total Income"],
    ["/dashboard", "Total Income"],
    ["/income", "Salary"],
    ["/expenses", "Rent"],
    ["/savings", "Emergency Fund"],
    ["/networth", "Assets"],
  ];

  for (const [route, marker] of authed) {
    test(`axe scan (authed): ${route} — structural rules clean, contrast failures carry only the reference's palette`, async ({ page }) => {
      await page.goto(route);
      await expect(page.getByText(marker).first()).toBeVisible();
      await assertParityClean(page, route);
    });
  }

  test("axe scan: the custom 404 — structural rules clean, the h1's slate is the reference's", async ({ page }) => {
    await page.goto("/this-route-does-not-exist");
    await expect(page.getByRole("heading", { name: "404" })).toBeVisible();
    await assertParityClean(page, "/404");
  });
});

// The login surface opts OUT of the shared storageState (the auth.spec
// idiom) — a separate describe so the opt-out never leaks into the
// authed-route tests. It must scan ZERO-violation clean (no allow-list).
test.describe("a11y gate — the login page (logged out)", () => {
  test.use({ storageState: { cookies: [], origins: [] } });
  test("axe scan: the login page — zero violations", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    await page.waitForTimeout(2500);
    const results = await new AxeBuilder({ page }).withTags(TAGS).analyze();
    expect(
      results.violations,
      `login page a11y violations: ${JSON.stringify(results.violations.map((v) => ({ id: v.id, nodes: v.nodes.length })))}`,
    ).toHaveLength(0);
  });
});
