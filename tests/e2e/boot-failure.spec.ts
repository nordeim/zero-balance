import { expect, test } from "@playwright/test";

// Boot data-failure parity (v16 G1 — measured live on the reference): when
// the DATA API fails during a full-page load while the session probe
// SUCCEEDS, the reference STAYS in the app rendering its silent zero-state
// (full shell, hero 0.0% / $0.00 / "✓ NET ZERO", items views "0 items ·
// $0.00" + their standard empty states, NO error surface at all). The
// clone previously bumped the user to /login — boot()'s single catch set
// user:null regardless of which stage failed.
//
// The clone's fix keeps the reference's stay-in-app zero-state (parity)
// and adds the honest error toast on top (superset — the reference's
// silent zero-state is a data-integrity illusion; the same superset class
// as the mutation-failure toast "Could not save the item"):
//
//   title:       "Could not load your data"
//   description: "Network error — check your connection and try again"
//   variant:     error (XCircle icon, the established toast chrome)
//
// A FAILED session probe (401) must still redirect to /login — the auth
// parity (spec 3 pins it).
//
// Route aborts reproduce the failure window: the specs intercept the data
// endpoints and abort them (read-only — never write). The session cookie
// comes from the storageState (the auth setup project), and /api/auth/me
// is left LIVE so the probe succeeds exactly like the measured reference
// scenario (its entity API died, its platform session lived).

/** Abort every data-API request (read-only — the handlers never write). */
async function abortDataRoutes(page: import("@playwright/test").Page) {
  for (const path of ["budget-items", "assets", "liabilities"]) {
    await page.route(`**/api/${path}`, async (route) => {
      await route.abort("failed");
    });
  }
}

test.describe("boot data-failure (v16)", () => {
  test("data-fetch failure at boot stays in-app (v16 G1)", async ({ page }) => {
    await abortDataRoutes(page);
    await page.goto("/");

    // The reference stays on its route with the full shell — the clone
    // must NOT bump to /login (the pre-fix behavior: boot()'s catch set
    // user:null and RequireSession redirected).
    await expect(page).not.toHaveURL(/\/login/);
    await expect(page).toHaveURL("/");

    // The shell renders with the session user intact (the seeded avatar
    // chip in the rail) — the user is still known, only the data failed.
    const shell = page.locator("aside, nav").first();
    await expect(shell).toBeVisible();

    // The reference's zero-state: the hero renders with zeroed figures.
    await expect(page.getByRole("heading", { name: "NET ZERO GOAL" })).toBeVisible();
    const bodyText = await page.evaluate(() => document.body.innerText);
    expect(bodyText).toContain("Budget Allocation");
    expect(bodyText).toContain("0.0%");
    expect(bodyText).toContain("$0.00");

    await page.unrouteAll({ behavior: "ignoreErrors" });
  });

  test("boot data-failure shows the error toast once (v16 G1)", async ({ page }) => {
    await abortDataRoutes(page);
    await page.goto("/");

    // The honest superset: the error toast fires while the reference's
    // zero-state renders silently. One toast, the established error chrome.
    // (exact: true — Radix mirrors the toast text into a role=status
    // live region for screen readers; the loose match double-counts it.)
    const toast = page.getByText("Could not load your data", { exact: true });
    await expect(toast).toBeVisible();
    await expect(
      page.getByText("Network error — check your connection and try again", {
        exact: true,
      })
    ).toBeVisible();

    // One-shot: no duplicates after the settle (the flag clears when
    // fired; a later successful refresh must not re-toast).
    await page.waitForTimeout(600);
    const toastCount = await page
      .getByText("Could not load your data", { exact: true })
      .count();
    expect(toastCount).toBe(1);

    await page.unrouteAll({ behavior: "ignoreErrors" });
  });

  test("session-probe 401 still redirects to login (v16 pin)", async ({ page }) => {
    // The auth parity must NOT regress: a FAILED session probe (401, not
    // a data failure) still sends the visitor to the login card with the
    // return-URL handling — the pre-v16 behavior for a logged-out boot.
    await page.route("**/api/auth/me", async (route) => {
      await route.fulfill({
        status: 401,
        contentType: "application/json",
        body: JSON.stringify({ ok: false, error: "Not authenticated" }),
      });
    });
    await page.goto("/");

    await expect(page).toHaveURL(/\/login\?from_url=%2F$/);
    await expect(
      page.getByRole("heading", { name: "Welcome to ZeroBudget" })
    ).toBeVisible();

    await page.unrouteAll({ behavior: "ignoreErrors" });
  });
});
