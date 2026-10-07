import { expect, test } from "@playwright/test";

// The category Calculator (the expenses view's inline "Calculate" button):
// opens on an expense item, lists its line items, adds/deletes a line item
// through the nested dialog, and every mutation recalculates and persists
// the PARENT item's amount SERVER-SIDE IMMEDIATELY — the reference's
// recalculation rule (no separate Save step; the "Total Calculated $X /
// Based on N items • Will update category total" banner just reports it).
//
// Parity detail measured on the reference: the dialog's chrome is
// CATEGORY-ADAPTIVE — the Rent card opens "Rent Calculator / Break down
// your rent into individual items". The seeded Rent item ($1,850.00)
// starts with no line items.
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("rent calculator", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2,235.00")).toBeVisible();
  });

  test("opens with the reference banner and empty line list", async ({ page }) => {
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.getByRole("button", { name: "Calculate" }).click();

    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await expect(dialog.getByText("Break down your rent into individual items")).toBeVisible();
    await expect(dialog.getByText("Total Calculated")).toBeVisible();
    await expect(dialog.getByText("Based on 0 items · Will update category total")).toBeVisible();
    await expect(dialog.getByText("No line items yet.")).toBeVisible();
    await expect(dialog.getByRole("button", { name: "Add Item" })).toBeVisible();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
  });

  test("add a line item → parent amount recalculates immediately", async ({ page }) => {
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });

    // --- open the nested line-item dialog and create one (TWO dialogs are
    // open at once — scope every lookup to its dialog by name).
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await expect(lineDialog).toBeVisible();
    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog).toBeVisible();

    // The calculator banner + row reflect the new line item…
    await expect(dialog.getByText("Contents Insurance")).toBeVisible();
    await expect(dialog.getByText("Based on 1 item · Will update category total")).toBeVisible();
    await expect(dialog.getByText("$25.00").first()).toBeVisible();

    // …and the parent already recalculated server-side. Close and verify.
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();

    // The parent card now shows $25.00 and the page total followed it:
    // 320 + 65 + 25 = 410.
    await expect(rent.getByText("$25.00")).toBeVisible();
    await expect(page.getByText("3 items · $410.00")).toBeVisible();

    // --- cleanup: restore the seed state (the suite shares one database,
    // so every test leaves its fixture as it found it). Deleting the line
    // item leaves the parent at $0.00 (the recalculated line total), so
    // the seed's $1,850.00 is restored through the real edit flow.
    await rent.getByRole("button", { name: "Calculate" }).click();
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await dialog.getByText("Based on 0 items · Will update category total").waitFor();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();

    await rent.hover();
    await page.getByRole("button", { name: "Actions for Rent" }).click();
    await page.getByRole("menuitem", { name: "Edit" }).click();
    const editDialog = page.getByRole("dialog", { name: "Edit Budget Item" });
    await editDialog.getByLabel("Amount").fill("1850");
    await editDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(editDialog).toBeHidden();
    await expect(page.getByText("3 items · $2,235.00")).toBeVisible();
  });

  test("deleting a line item recalculates the parent back", async ({ page }) => {
    // Seed state for this test: create the line item first (recalc #1).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Contents Insurance")).toBeVisible();

    // --- delete via the trash trigger + inline confirm (recalc #2)
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await expect(dialog.getByText("Delete this line item?")).toBeVisible();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(dialog.getByText("Based on 0 items · Will update category total")).toBeVisible();

    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await expect(rent.getByText("$0.00")).toBeVisible();
    // 320 + 65 + 0 = 385.
    await expect(page.getByText("3 items · $385.00")).toBeVisible();

    // --- cleanup: restore the seed's Rent amount via the edit flow.
    await rent.hover();
    await page.getByRole("button", { name: "Actions for Rent" }).click();
    await page.getByRole("menuitem", { name: "Edit" }).click();
    const editDialog = page.getByRole("dialog", { name: "Edit Budget Item" });
    await editDialog.getByLabel("Amount").fill("1850");
    await editDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(editDialog).toBeHidden();
    await expect(page.getByText("3 items · $2,235.00")).toBeVisible();
  });
});
