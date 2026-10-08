import { expect, test } from "@playwright/test";

// Calculator line-item error tier (v17 G1 — measured live on both sites):
// with the line-items API dead, the REFERENCE is silent on every path —
// the load renders the empty-state ("Total Calculated $0.00 / Based on 0
// items / No line items yet. / Add First Item"), the create leaves the
// sub-dialog open with no feedback, the delete leaves the row with no
// feedback. The clone keeps the reference's SURFACES (parity) and adds
// the honest error toasts on top (superset — the same class as the v16
// boot toast and the mutation-failure toasts "Could not save the item"):
//
//   load:    "Could not load the line items"      (v17 G1 fix)
//   create:  "Could not save the line item"       (in place since the
//   delete:  "Could not remove the line item"      dialogs' catch blocks)
//
// This file pins all three. The create/delete specs guard REGRESSIONS of
// the existing superset (nothing pinned them before v17 — a dropped catch
// block would ship silently); the load spec drives the v17 fix (the
// pre-fix calculator-dialog effect called `void loadLineItems(item.id)`
// — the rejection was unhandled and no toast fired).
//
// Route aborts reproduce the failure window (read-only for the load spec;
// the create/delete specs abort only the mutations they fail). Toast
// assertions use exact:true — Radix mirrors toast text into a role=status
// live region whose concatenated text double-matches loose locators (the
// v16 lesson 34).
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("calculator line-item error tier (v17)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
  });

  test("calculator load failure renders the reference empty-state + the error toast (v17 G1)", async ({ page }) => {
    // Abort the line-items API BEFORE the calculator opens — its mount
    // effect's loadLineItems fetch dies, exactly like the measured
    // reference scenario (entity API dead, session + budget-items live).
    await page.route("**/api/line-items**", async (route) => {
      await route.abort("failed");
    });

    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();

    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();

    // PARITY: the reference's silent empty-state renders — zeroed total,
    // 0 items, the standard empty state + Add First Item (a dead API
    // looks like an empty category on the reference; the clone renders
    // the same surfaces via the `?? []` fallback).
    await expect(dialog.getByText("Total Calculated")).toBeVisible();
    await expect(dialog.getByText("$0.00").first()).toBeVisible();
    await expect(dialog.getByText("Based on 0 items")).toBeVisible();
    await expect(
      dialog.getByText("No line items yet. Start by adding individual items that make up this category.")
    ).toBeVisible();
    await expect(dialog.getByRole("button", { name: "Add First Item" })).toBeVisible();

    // SUPERSET: the honest error toast fires (the reference stays silent —
    // its empty-state is a data-integrity illusion). exact:true per the
    // live-region lesson.
    const toast = page.getByText("Could not load the line items", { exact: true });
    await expect(toast).toBeVisible();
    await expect(
      page.getByText("Network error — check your connection and try again", {
        exact: true,
      })
    ).toBeVisible();

    // Per-open semantics (a fresh user action each time — NOT one-shot):
    // after the settle there is exactly ONE toast for this dialog open.
    await page.waitForTimeout(600);
    const toastCount = await page
      .getByText("Could not load the line items", { exact: true })
      .count();
    expect(toastCount).toBe(1);

    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();

    await page.unrouteAll({ behavior: "ignoreErrors" });
  });

  test("line-item create failure keeps the dialog open + error toast (v17 pin)", async ({ page }) => {
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();

    // Abort the line-items API before the Save (the POST dies; the
    // calculator's own load already succeeded — the row list is live).
    await page.route("**/api/line-items**", async (route) => {
      await route.abort("failed");
    });

    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await expect(lineDialog).toBeVisible();
    await lineDialog.getByLabel("Item Name *").fill("Probe Item");
    await lineDialog.getByLabel("Amount *").fill("10");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();

    // The reference's sub-dialog stays open on failure (measured) — the
    // clone matches; the honest toast is the superset.
    await expect(lineDialog).toBeVisible();
    await expect(
      page.getByText("Could not save the line item", { exact: true })
    ).toBeVisible();
    await expect(
      page.getByText("Network error — check your connection and try again", {
        exact: true,
      })
    ).toBeVisible();

    // Cancel out of the still-open sub-dialog (the nested Radix dialog
    // aria-hides the calculator behind it — the calculator assertions
    // below must wait until the sub-dialog closes).
    await lineDialog.getByRole("button", { name: "Cancel" }).click();
    await expect(lineDialog).toBeHidden();

    // No optimistic update: the calculator still reports 0 items (the
    // failed POST left the server state untouched).
    await expect(dialog.getByText("Based on 0 items")).toBeVisible();

    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();

    await page.unrouteAll({ behavior: "ignoreErrors" });
  });

  test("line-item delete failure keeps the row + error toast (v17 pin)", async ({ page }) => {
    // Seed one line item through the LIVE API first (the shared database
    // starts Rent at $1,850.00 with no line items — same as the calculator
    // happy-path specs).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await lineDialog.getByLabel("Item Name *").fill("Probe Item");
    await lineDialog.getByLabel("Amount *").fill("10");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Based on 1 item")).toBeVisible();

    // Now kill the API and attempt the delete.
    await page.route("**/api/line-items**", async (route) => {
      await route.abort("failed");
    });

    await dialog.getByRole("button", { name: "Delete Probe Item" }).click();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();

    // The reference's failed delete leaves the row silently (measured);
    // the clone keeps the row AND toasts the honest error.
    await expect(dialog.getByText("Probe Item").first()).toBeVisible();
    await expect(dialog.getByText("Based on 1 item")).toBeVisible();
    await expect(
      page.getByText("Could not remove the line item", { exact: true })
    ).toBeVisible();
    await expect(
      page.getByText("Network error — check your connection and try again", {
        exact: true,
      })
    ).toBeVisible();

    // --- fixture restore: unroute, delete for real, restore the seed's
    // Rent amount (the suite shares one database).
    await page.unrouteAll({ behavior: "ignoreErrors" });
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await dialog.getByText("Based on 0 items").waitFor();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });
});

/** Restore the seed's Rent amount through the real edit flow (the expense
 * card's hover-revealed Edit button — expense cards carry no ellipsis). */
async function restoreRent(page: import("@playwright/test").Page) {
  const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
  await rent.hover();
  await rent.getByRole("button", { name: "Edit", exact: true }).click();
  const editDialog = page.getByRole("dialog", { name: "Edit Budget Item" });
  await editDialog.getByLabel("Amount").fill("1850");
  await editDialog.getByRole("button", { name: "Save Item" }).click();
  await expect(editDialog).toBeHidden();
  await expect(page.getByText("3 items · $2235.00")).toBeVisible();
}
