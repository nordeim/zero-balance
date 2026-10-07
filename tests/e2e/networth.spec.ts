import { expect, test } from "@playwright/test";

// Net Worth: the forest→lime gradient summary (Total Net Worth, Total
// Assets, Total Liabilities, Asset-to-Liability Ratio "0.21:1" — the
// reference's .toFixed(2) + ":1" with NO spaces, "∞:1" when debt-free), the
// Assets/Liabilities tabs with TYPE-GROUPED lists (capitalize h3 headers),
// dot + name + gray-type-badge cards with GROUPED comma money, stacked
// footers (institution / % interest / Updated), and the add-asset
// round-trip. Seed arithmetic: assets 65,300 − liabilities 311,250 → net
// worth −245,950; ratio 65,300 / 311,250 → 0.21.
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("net worth view", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
  });

  test("summary card shows the gradient, net figure and 2-decimal ratio", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Net Worth" })).toBeVisible();
    await expect(page.getByText("Track your assets and liabilities")).toBeVisible();

    // Networth keeps the GROUPED money format (commas).
    await expect(page.getByText("-$245,950.00")).toBeVisible();
    await expect(page.getByText("Total Assets")).toBeVisible();
    await expect(page.getByText("$65,300.00")).toBeVisible();
    await expect(page.getByText("Total Liabilities")).toBeVisible();
    await expect(page.getByText("$311,250.00")).toBeVisible();

    // Ratio: ".toFixed(2)" + ":1", no spaces (reference bundle).
    await expect(page.getByText("Asset to Liability Ratio")).toBeVisible();
    await expect(page.getByText("0.21:1")).toBeVisible();

    // The summary's forest→lime gradient (135deg).
    const hero = page.locator("div.rounded-2xl").filter({ hasText: "Total Net Worth" }).first();
    const bg = await hero.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(45, 90, 74)");
  });

  test("Assets tab groups by type with capitalize headers and badge cards", async ({ page }) => {
    await expect(page.getByRole("tab", { name: "Assets" })).toBeVisible();
    // Section header: text-2xl + always-plural count, short grouped money.
    const assetsHeader = page.getByRole("heading", { name: "Assets", level: 2 });
    await expect(assetsHeader).toBeVisible();
    await expect(page.getByText("3 items · $65,300")).toBeVisible();

    // Type-group headers (capitalize class over raw keys). The API lists
    // entities createdAt-desc (mirroring the reference's "-created_date"),
    // so first-occurrence groups run newest-type-first: investment →
    // superannuation → bank_account.
    const groups = page.locator("h3.capitalize");
    await expect(groups).toHaveCount(3);
    await expect(groups.nth(0)).toHaveText(/investment/i);
    await expect(groups.nth(1)).toHaveText(/superannuation/i);
    await expect(groups.nth(2)).toHaveText(/bank account/i);
    // Asset group headers render in forestMedium.
    await expect(groups.nth(0)).toHaveCSS("color", "rgb(45, 90, 74)");

    // Card: name + gray type badge + grouped amount + stacked footer.
    await expect(page.getByText("Everyday Account").first()).toBeVisible();
    const badge = page.getByText("Bank Account", { exact: true }).first();
    await expect(badge).toHaveClass(/bg-gray-100/);
    await expect(badge).toHaveClass(/text-gray-700/);
    await expect(page.getByText("$4,200.00").first()).toBeVisible();
    await expect(page.getByText("Commonwealth Bank").first()).toBeVisible();
    await expect(page.getByText("$48,500.00").first()).toBeVisible();
    await expect(page.getByText("$12,600.00").first()).toBeVisible();
    // "Updated" footer per card.
    await expect(page.getByText(/Updated/).first()).toBeVisible();

    // Add Asset carries the forest→lime gradient.
    const add = page.getByRole("button", { name: "Add Asset" }).first();
    const addBg = await add.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(addBg).toContain("linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))");
  });

  test("Liabilities tab lists type-grouped cards with interest lines", async ({ page }) => {
    await page.getByRole("tab", { name: "Liabilities" }).click();
    await expect(page.getByText("2 items · $311,250")).toBeVisible();
    // Liability group headers render in orange; newest first → credit card
    // precedes home loan (createdAt-desc listing).
    const groups = page.locator("h3.capitalize");
    await expect(groups).toHaveCount(2);
    await expect(groups.nth(0)).toHaveText(/credit card/i);
    await expect(groups.nth(1)).toHaveText(/home loan/i);
    await expect(groups.first()).toHaveCSS("color", "rgb(224, 122, 59)");

    await expect(page.getByText("$310,000.00").first()).toBeVisible();
    await expect(page.getByText("$1,250.00").first()).toBeVisible();
    // The liability-only "{rate}% interest" footer line.
    await expect(page.getByText("5.75% interest")).toBeVisible();
    await expect(page.getByText("19.99% interest")).toBeVisible();

    // Add Liability carries the orange gradient.
    const add = page.getByRole("button", { name: "Add Liability" }).first();
    const addBg = await add.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(addBg).toContain("linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))");
  });

  test("add → delete asset round-trip through the dialog", async ({ page }) => {
    await page.getByRole("button", { name: "Add Asset" }).first().click();
    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();

    await dialog.getByRole("combobox", { name: "Asset Type" }).click();
    await page.getByRole("option", { name: "Vehicle" }).click();
    await page.getByLabel("Current Value").fill("15000");
    await page.getByLabel("Name").fill("Test Car");
    await page.getByLabel("Institution").fill("Playwright Motors");
    await page.getByRole("button", { name: "Save Asset" }).click();
    await expect(dialog).toBeHidden();

    const created = page.locator("div.rounded-xl").filter({ hasText: "Test Car" }).first();
    await expect(created).toBeVisible();
    await expect(created.getByText("$15,000.00")).toBeVisible();

    // The tab header count updated: 4 items · $80,300 (short format).
    await expect(page.getByText("4 items · $80,300")).toBeVisible();

    // Delete (inline confirm via the ellipsis actions menu).
    await created.getByRole("button", { name: "Actions for Test Car" }).click();
    await page.getByRole("menuitem", { name: "Delete" }).click();
    await expect(page.getByText("Delete this asset?")).toBeVisible();
    await page.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(page.getByText("Test Car")).toHaveCount(0);
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
  });
});
