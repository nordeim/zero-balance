import { expect, test } from "@playwright/test";

// Net-worth asset/liability error tier (v18 G1 — measured live on both
// sites): with the entity API dead, the REFERENCE is silent on every
// path — its asset-card Delete fires with NO confirmation and the failed
// delete leaves the card with no feedback; its failed Edit Asset Save
// leaves the (plain-div) dialog open with no feedback. The clone keeps
// the reference's SURFACES (parity — the card stays, the confirm bar
// stays, the dialog stays open; the store mutates state only after the
// awaited API resolves) and adds the honest error toasts on top
// (superset — the same class as the v16 boot toast, the budget-item
// catches, and the v17 calculator tier):
//
//   asset save:     "Could not save the asset"       (in place since the
//   liability save:  "Could not save the liability"    dialogs' catch blocks)
//   asset delete:   "Could not delete the asset"     (v18 G1 fix)
//   liability delete:"Could not delete the liability" (v18 G1 fix)
//
// This file pins all four. The save specs guard REGRESSIONS of the
// existing superset (nothing pinned them before v18 — a dropped catch
// block would ship silently); the delete specs drive the v18 fix — the
// pre-fix confirm bars called `void deleteAsset(asset.id)` /
// `void deleteLiability(liability.id)` and the rejections were
// unhandled with no toast (the same `void` accident as v17's
// calculator load).
//
// Route aborts reproduce the failure window; the DELETE/PUT bodies never
// reach the server, so NO fixture restore is needed (the rows survive by
// construction — that IS the parity pin). Toast assertions use
// exact:true — Radix mirrors toast text into a role=status live region
// whose concatenated text double-matches loose locators (the v16 lesson
// 34). Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("net-worth asset/liability error tier (v18)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
  });

  test("asset delete failure keeps the card + confirm bar + error toast (v18 G1)", async ({ page }) => {
    // Kill the assets API BEFORE the delete attempt (the DELETE dies; the
    // failed request leaves the server state untouched — no restore).
    await page.route("**/api/assets**", async (route) => {
      await route.abort("failed");
    });

    const card = page.locator("div.rounded-xl").filter({ hasText: "Share Portfolio" }).first();
    await expect(card).toBeVisible();
    await card.getByRole("button", { name: "Actions for Share Portfolio" }).click();
    await page.getByRole("menuitem", { name: "Delete" }).click();
    await expect(card.getByText("Delete this asset?")).toBeVisible();
    await card.getByRole("button", { name: "Delete", exact: true }).click();

    // PARITY: the reference's failed delete leaves the card in place
    // (measured live — no confirmation, card stays, zero feedback); the
    // clone keeps the card AND its inline confirm bar (superset #6
    // chrome, still up — the failure leaves the user mid-action).
    await expect(card.getByRole("heading", { name: "Share Portfolio" })).toBeVisible();
    await expect(card.getByText("Delete this asset?")).toBeVisible();

    // SUPERSET: the honest error toast fires (the reference stays silent —
    // its card-stay is a data-integrity illusion). exact:true per the
    // live-region lesson.
    await expect(
      page.getByText("Could not delete the asset", { exact: true })
    ).toBeVisible();
    await expect(
      page.getByText("Network error — check your connection and try again", {
        exact: true,
      })
    ).toBeVisible();

    // Per-click semantics: after the settle there is exactly ONE toast
    // for this delete click.
    await page.waitForTimeout(600);
    const toastCount = await page
      .getByText("Could not delete the asset", { exact: true })
      .count();
    expect(toastCount).toBe(1);

    // Leave the card clean for any later probe (the API is still dead,
    // so this only clears the UI state).
    await card.getByRole("button", { name: "Cancel" }).click();
    await expect(card.getByText("Delete this asset?")).toHaveCount(0);

    await page.unrouteAll({ behavior: "ignoreErrors" });
  });

  test("liability delete failure keeps the card + error toast (v18 G1)", async ({ page }) => {
    await page.route("**/api/liabilities**", async (route) => {
      await route.abort("failed");
    });

    await page.getByRole("tab", { name: "Liabilities" }).click();
    const card = page.locator("div.rounded-xl").filter({ hasText: "Credit Card" }).first();
    await expect(card).toBeVisible();
    await card.getByRole("button", { name: "Actions for Credit Card" }).click();
    await page.getByRole("menuitem", { name: "Delete" }).click();
    await expect(card.getByText("Delete this liability?")).toBeVisible();
    await card.getByRole("button", { name: "Delete", exact: true }).click();

    // PARITY: the card stays (measured live on the reference's family —
    // the failed delete is a silent no-op there; the clone keeps the row
    // by construction — the store filters only after the API resolves).
    await expect(card.getByRole("heading", { name: "Credit Card" })).toBeVisible();
    await expect(card.getByText("Delete this liability?")).toBeVisible();

    // SUPERSET: the honest error toast.
    await expect(
      page.getByText("Could not delete the liability", { exact: true })
    ).toBeVisible();
    await expect(
      page.getByText("Network error — check your connection and try again", {
        exact: true,
      })
    ).toBeVisible();

    await page.waitForTimeout(600);
    const toastCount = await page
      .getByText("Could not delete the liability", { exact: true })
      .count();
    expect(toastCount).toBe(1);

    await card.getByRole("button", { name: "Cancel" }).click();
    await expect(card.getByText("Delete this liability?")).toHaveCount(0);

    await page.unrouteAll({ behavior: "ignoreErrors" });
  });

  test("asset save failure keeps the dialog open + error toast (v18 pin)", async ({ page }) => {
    const card = page.locator("div.rounded-xl").filter({ hasText: "Share Portfolio" }).first();
    await card.getByRole("button", { name: "Actions for Share Portfolio" }).click();
    await page.getByRole("menuitem", { name: "Edit" }).click();
    const dialog = page.getByRole("dialog", { name: "Edit Asset" });
    await expect(dialog).toBeVisible();

    // Kill the assets API before the Save (the PATCH dies — the edit is
    // unchanged values, so even a success would be a no-op write).
    await page.route("**/api/assets**", async (route) => {
      await route.abort("failed");
    });
    await dialog.getByRole("button", { name: "Save Asset" }).click();

    // The reference's failed Save leaves its dialog open with NO
    // feedback (measured live); the clone matches the open dialog and
    // adds the honest toast (the superset, unpinned until now).
    await expect(dialog).toBeVisible();
    await expect(
      page.getByText("Could not save the asset", { exact: true })
    ).toBeVisible();
    await expect(
      page.getByText("Network error — check your connection and try again", {
        exact: true,
      })
    ).toBeVisible();

    // Clean exit: Cancel the still-open dialog (the API stays dead; the
    // form was never written anywhere).
    await dialog.getByRole("button", { name: "Cancel" }).click();
    await expect(dialog).toBeHidden();

    await page.unrouteAll({ behavior: "ignoreErrors" });
  });

  test("liability save failure keeps the dialog open + error toast (v18 pin)", async ({ page }) => {
    await page.getByRole("tab", { name: "Liabilities" }).click();
    const card = page.locator("div.rounded-xl").filter({ hasText: "Credit Card" }).first();
    await card.getByRole("button", { name: "Actions for Credit Card" }).click();
    await page.getByRole("menuitem", { name: "Edit" }).click();
    const dialog = page.getByRole("dialog", { name: "Edit Liability" });
    await expect(dialog).toBeVisible();

    await page.route("**/api/liabilities**", async (route) => {
      await route.abort("failed");
    });
    await dialog.getByRole("button", { name: "Save Liability" }).click();

    await expect(dialog).toBeVisible();
    await expect(
      page.getByText("Could not save the liability", { exact: true })
    ).toBeVisible();
    await expect(
      page.getByText("Network error — check your connection and try again", {
        exact: true,
      })
    ).toBeVisible();

    await dialog.getByRole("button", { name: "Cancel" }).click();
    await expect(dialog).toBeHidden();

    await page.unrouteAll({ behavior: "ignoreErrors" });
  });
});
