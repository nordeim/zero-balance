import { expect, test } from "@playwright/test";

// The category Calculator (the expenses view's hover-revealed "Calculate"
// button): opens on an expense item, lists its line items, adds/deletes a
// line item through the nested dialog, and every mutation recalculates and
// persists the PARENT item's amount SERVER-SIDE IMMEDIATELY — the
// reference's recalculation rule (no separate Save step; the orange total
// card's "Based on N item(s)" + conditional "• Will update category total"
// just reports it).
//
// Parity details measured on the reference: the dialog's chrome is
// CATEGORY-ADAPTIVE ("Rent Calculator / Break down your rent into individual
// items"); the header carries an orange-gradient calculator chip + Close X;
// the total card is the bordered orange tint (#fff7f5 / #fcddd5) with the
// amount right in #e07a3b. The seeded Rent item ($1,850.00) starts with no
// line items.
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("rent calculator", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
  });

  test("opens with the orange total card and empty line list", async ({ page }) => {
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();

    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await expect(dialog.getByText("Break down your rent into individual items")).toBeVisible();

    // Header: the orange-gradient calculator chip + white icon.
    const chip = dialog.locator("div.rounded-xl").first();
    const chipBg = await chip.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(chipBg).toContain("linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))");

    // Total card: bordered orange tint, "Total Calculated" left, $0.00
    // right in #e07a3b, "Based on 0 items" + the conditional orange span
    // (0 !== 1850 → shown). Scope by the card's own rounded-xl class (the
    // chip shares rounded-xl but not the "Total Calculated" text).
    const totalCard = dialog.locator("div.rounded-xl").filter({ hasText: "Total Calculated" });
    await expect(totalCard).toHaveCSS("background-color", "rgb(255, 247, 245)");
    await expect(totalCard).toHaveCSS("border-color", "rgb(252, 221, 213)");
    await expect(dialog.getByText("Total Calculated")).toBeVisible();
    const amount = dialog.getByText("$0.00").first();
    await expect(amount).toBeVisible();
    await expect(amount).toHaveCSS("color", "rgb(224, 122, 59)");
    await expect(dialog.getByText("Based on 0 items")).toBeVisible();
    const willUpdate = dialog.getByText("• Will update category total");
    await expect(willUpdate).toBeVisible();
    // v5 (plan G9): the hint pins the reference's orange-600 as an arbitrary
    // hex class — v4 computes the named orange as lab(); assert the computed
    // color instead of the class name.
    await expect(willUpdate).toHaveCSS("color", "rgb(234, 88, 12)");

    await expect(dialog.getByText("No line items yet. Start by adding individual items that make up this category.")).toBeVisible();
    await expect(dialog.getByRole("button", { name: "Add Item" })).toBeVisible();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
  });

  test("the nested line-item dialog matches the reference fields and status enum", async ({ page }) => {
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });

    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await expect(lineDialog).toBeVisible();

    // Reference field order (F4): Item Name, Amount, Frequency, Provider /
    // Company, Policy / Account Number, Start / Renewal Date, End / Expiry
    // Date, Payment Method, Status, Notes.
    const labels = await lineDialog.evaluate((root) =>
      [...root.querySelectorAll("label")].map((l) => l.textContent?.trim() ?? ""),
    );
    expect(labels).toEqual([
      "Item Name *",
      "Amount *",
      "Frequency",
      "Provider / Company",
      "Policy / Account Number",
      "Start / Renewal Date",
      "End / Expiry Date",
      "Payment Method",
      "Status",
      "Notes",
    ]);

    // Line items carry their OWN status enum — Active/Pending/Cancelled —
    // NOT the budget-item planned/completed trio.
    await lineDialog.getByRole("combobox", { name: "Status" }).click();
    for (const option of ["Active", "Pending", "Cancelled"]) {
      await expect(page.getByRole("option", { name: option, exact: true })).toBeVisible();
    }
    await expect(page.getByRole("option", { name: "Planned" })).toHaveCount(0);
    await expect(page.getByRole("option", { name: "Completed" })).toHaveCount(0);
    await page.getByRole("option", { name: "Pending", exact: true }).click();
    await expect(lineDialog.getByRole("combobox", { name: "Status" })).toContainText("Pending");

    // Cancel — nothing is persisted.
    await lineDialog.getByRole("button", { name: "Cancel" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Based on 0 items")).toBeVisible();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
  });

  test("add a line item → parent amount recalculates immediately", async ({ page }) => {
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
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
    await expect(dialog.getByText("Based on 1 item")).toBeVisible();
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
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await dialog.getByText("Based on 0 items").waitFor();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();

    await restoreRent(page);
  });

  test("deleting a line item recalculates the parent back", async ({ page }) => {
    // Seed state for this test: create the line item first (recalc #1).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
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
    await expect(dialog.getByText("Based on 0 items")).toBeVisible();

    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await expect(rent.getByText("$0.00")).toBeVisible();
    // 320 + 65 + 0 = 385.
    await expect(page.getByText("3 items · $385.00")).toBeVisible();

    // --- cleanup: restore the seed's Rent amount via the edit flow.
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
