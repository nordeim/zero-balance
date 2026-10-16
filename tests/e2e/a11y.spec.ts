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

// ---------------------------------------------------------------------------
// v39 F1 — the a11y gate's MOBILE extension (docs/remediation-plan-v39.md).
// The session-80/81 queue's third item: the desktop gate extended to the
// mobile viewport (390×844, isMobile + hasTouch — the mobile-navigation
// spec's emulation). Measured live on BOTH sites (a11y-scan-v39.mjs):
//
//  - The reference at mobile fails button-name (critical) on the four item
//    views (its unlabeled Select triggers + kebabs) and svg-img-alt on
//    / + /dashboard (its donut sectors) — the same families as desktop.
//  - The clone passes both everywhere at mobile; its only failures are
//    color-contrast, every flagged color enumerated in the reference's own
//    7-color palette (axe-detail-v39.mjs / axe-detail-ref-v39.mjs — the
//    mobile node counts differ from desktop only by the demo card counts).
//  - The sheet-OPEN superset: the reference's mobile sheet is a plain
//    fixed div (no role, no aria-labelledby, no nav landmark, no title);
//    the clone's is a Radix Dialog — role=dialog + aria-labelledby → the
//    sr-only "Navigation" DialogTitle + nav aria-label="Primary" + the
//    named burger — pinned structurally by the sheet-open test below.
// ---------------------------------------------------------------------------
test.describe("a11y gate MOBILE (v39 F1 — the 390×844 sheet-state scan)", () => {
  test.use({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true });

  const authed: Array<[route: string, marker: string]> = [
    ["/", "Total Income"],
    ["/dashboard", "Total Income"],
    ["/income", "Salary"],
    ["/expenses", "Rent"],
    ["/savings", "Emergency Fund"],
    ["/networth", "Assets"],
  ];

  for (const [route, marker] of authed) {
    test(`axe scan (authed, mobile 390×844): ${route} — structural rules clean, contrast failures carry only the reference's palette`, async ({ page }) => {
      await page.goto(route);
      await expect(page.getByText(marker).first()).toBeVisible();
      await assertParityClean(page, `${route} (mobile 390×844)`);
    });
  }

  test("the sheet-OPEN state: the accessible mobile navigation menu + both gates", async ({ page }) => {
    await page.goto("/");
    await expect(page.getByText("Total Income").first()).toBeVisible();

    // A REAL click on the named burger — the clone's toast viewport never
    // blocks it (superset fix #1; the reference's does — its probe needs
    // the JS-click workaround, an e2e here does not).
    await page.getByRole("button", { name: "Toggle Sidebar" }).click();
    const sheet = page.locator("[data-state='open'][role='dialog']");
    await expect(sheet).toBeVisible();
    await page.waitForTimeout(1200); // the sheet-open settle (probe-measured)

    // The structural pins — the reference's sheet has NONE of these:
    // role=dialog, an aria-labelledby resolving to a titled element, a
    // nav landmark with its label, the five links.
    const structure = await sheet.evaluate((el) => {
      const labelledBy = el.getAttribute("aria-labelledby");
      const titleEl = labelledBy ? (el.querySelector(`#${CSS.escape(labelledBy)}`) || document.getElementById(labelledBy)) : null;
      const nav = el.querySelector("nav");
      return {
        role: el.getAttribute("role"),
        labelledBy,
        titleText: titleEl ? titleEl.textContent?.trim() : null,
        navPresent: !!nav,
        navLabel: nav ? nav.getAttribute("aria-label") : null,
        links: [...el.querySelectorAll("nav a")].map((a) => (a.textContent || "").trim()),
      };
    });
    expect(structure.role, "the sheet must be a dialog (the reference's is a plain div)").toBe("dialog");
    expect(structure.labelledBy, "the sheet must be labelled (aria-labelledby)").toBeTruthy();
    expect(structure.titleText, "the labelledby must resolve to the sr-only Navigation title").toBe("Navigation");
    expect(structure.navPresent, "the sheet must contain a nav landmark (the reference has none)").toBe(true);
    expect(structure.navLabel).toBe("Primary");
    expect(structure.links).toEqual(["Dashboard", "Income", "Expenses", "Savings", "Net Worth"]);

    // Both gates against the sheet-open DOM (measured: the sheet adds no
    // violations beyond the page's 14 color-contrast baseline nodes).
    await assertParityClean(page, "/ (mobile, sheet open)");

    // The sheet closes (the reference's traps — superset fix #2) — Escape.
    await page.keyboard.press("Escape");
    await expect(sheet).not.toBeVisible();
  });
});

// The logged-out mobile login — its own describe (the v38 hoisting
// lesson: test.use is hoisted PER describe; the opt-out never leaks).
test.describe("a11y gate MOBILE — the login page (logged out, 390×844)", () => {
  test.use({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true });
  test.use({ storageState: { cookies: [], origins: [] } });
  test("axe scan: the mobile login page — zero violations", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    await page.waitForTimeout(2500);
    const results = await new AxeBuilder({ page }).withTags(TAGS).analyze();
    expect(
      results.violations,
      `mobile login page a11y violations: ${JSON.stringify(results.violations.map((v) => ({ id: v.id, nodes: v.nodes.length })))}`,
    ).toHaveLength(0);
  });
});

// ---------------------------------------------------------------------------
// v41 F4 (docs/remediation-plan-v41.md) — the sheet-open structural pins
// extended to the REMAINING five authed routes. The v39 test pins the full
// structure (dialog role, labelledby → Navigation, the nav landmark, the
// five links, the axe gates) on `/` only; the sheet is a GLOBAL app-shell
// component, but each route's page mounts its own header burger — this
// extension pins that every route's sheet opens with the SAME structure
// and closes on Escape. The full axe scan stays on `/` (the sheet's DOM
// contribution is route-independent; each route's page baseline is
// already scanned sheet-CLOSED by the v39 mobile gate above).
// ---------------------------------------------------------------------------
test.describe("a11y gate MOBILE — the sheet-open structure on EVERY route (v41 F4)", () => {
  test.use({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true });

  const routes: Array<[route: string, marker: string]> = [
    ["/dashboard", "Total Income"],
    ["/income", "Salary"],
    ["/expenses", "Rent"],
    ["/savings", "Emergency Fund"],
    ["/networth", "Assets"],
  ];

  for (const [route, marker] of routes) {
    test(`the sheet-OPEN structure on ${route}: the accessible menu + Escape close (v41 F4)`, async ({ page }) => {
      await page.goto(route);
      await expect(page.getByText(marker).first()).toBeVisible();

      // The REAL burger click (the clone's toast viewport never blocks it).
      await page.getByRole("button", { name: "Toggle Sidebar" }).click();
      const sheet = page.locator("[data-state='open'][role='dialog']");
      await expect(sheet).toBeVisible();
      await page.waitForTimeout(1200); // the sheet-open settle

      // The structural pins — the same contract as the v39 `/` test.
      const structure = await sheet.evaluate((el) => {
        const labelledBy = el.getAttribute("aria-labelledby");
        const titleEl = labelledBy ? (el.querySelector(`#${CSS.escape(labelledBy)}`) || document.getElementById(labelledBy)) : null;
        const nav = el.querySelector("nav");
        return {
          role: el.getAttribute("role"),
          titleText: titleEl ? titleEl.textContent?.trim() : null,
          navPresent: !!nav,
          navLabel: nav ? nav.getAttribute("aria-label") : null,
          links: [...el.querySelectorAll("nav a")].map((a) => (a.textContent || "").trim()),
        };
      });
      expect(structure.role, "the sheet must be a dialog (the reference's is a plain div)").toBe("dialog");
      expect(structure.titleText, "the labelledby must resolve to the sr-only Navigation title").toBe("Navigation");
      expect(structure.navPresent, "the sheet must contain a nav landmark (the reference has none)").toBe(true);
      expect(structure.navLabel).toBe("Primary");
      expect(structure.links).toEqual(["Dashboard", "Income", "Expenses", "Savings", "Net Worth"]);

      // The sheet closes on Escape (superset fix #2 — the reference's traps).
      await page.keyboard.press("Escape");
      await expect(sheet).not.toBeVisible();
    });
  }
});

// ---------------------------------------------------------------------------
// v68 F3 — the a11y gate's ENGINE-CONTRACT pin (docs/remediation-plan-v68.md).
// The dedicated axe-core upgrade iteration's own invariant: the engine the
// AxeBuilder executes under is axe-core 4.14.x — the DELIBERATELY-PINNED
// toolchain state (package.json `@axe-core/playwright` `^4.14.0`), never a
// silent drift. Every AxeResults object carries `testEngine:
// { name, version }` — the identity of the engine that actually executed
// the scan — so a REAL scan's testEngine is the ground truth, not the
// lockfile's promise.
//
// The upgrade's verification chain (all measured this iteration): the
// registry 4.14.0 (no 5.x exists), the activated rule sets at the gate's
// TAGS byte-identical 4.13.0 → 4.14.0 (69 of 105 rules each, zero added,
// zero removed — the axe-rule-census-v68.mjs re-audit), and the full gate
// green under 4.14.0. This pin makes the state executable: any future
// engine change without a conscious re-verification (a lockfile drift, a
// dedupe flip, a wrapper downgrade, a 4.15/5.x bump) FAILS here — the
// "never a drift" discipline. When a deliberate future upgrade changes
// this expectation, it changes WITH its own full re-verification chain
// (the v68 precedent).
// ---------------------------------------------------------------------------
test.describe("a11y gate — the engine contract (v68 — the dedicated axe-core upgrade)", () => {
  test.use({ storageState: { cookies: [], origins: [] } });
  test("the gate executes under axe-core 4.14.x (the deliberately-pinned engine — never a drift)", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    await page.waitForTimeout(1000);

    // A real scan — the testEngine field reports the engine that ran it.
    const results = await new AxeBuilder({ page }).withTags(TAGS).analyze();
    expect(results.testEngine.name).toBe("axe-core");
    expect(
      results.testEngine.version,
      `the a11y gate executed under axe-core ${results.testEngine.version} — the v68 upgrade pinned the engine at 4.14.x (package.json ^4.14.0); an unintended engine change (a lockfile drift, a dedupe flip, a wrapper downgrade) must fail here, never silently pass`,
    ).toMatch(/^4\.14\./);
  });
});
