import { expect, test } from "@playwright/test";

// Net Zero Breakdown — the 3-level expandable drill-down pinned against the
// live reference (clicking a section expands categories IN PLACE; clicking a
// category reveals subcategory + item rows; no navigation happens).
//
// Seed arithmetic (plain "$" + toFixed(2) money, no separators):
//   Income: Salary 5200 (Main Job) + Freelance 350 (Side Projects) → 5550
//   Savings: Emergency Fund 800 (Safety Net) + Investments 450 (Index Funds) → 1250
//   Expenses: Rent 1850 (Apartment) + Groceries 320 (Weekly Shop) +
//             Entertainment 65 (Streaming) → 2235 (3 categories)
//   Net Balance: +2065 → orangeLight (positive), trending-up icon.
// Item labels: notes truncated to 30 chars, else the literal "Item".

test.describe("net zero breakdown drill-down", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
  });

  test("section rows list totals with sign prefixes and chevrons", async ({ page }) => {
    const card = page.locator("div.rounded-2xl").filter({ hasText: "Net Zero Breakdown" }).first();
    const incomeRow = card.getByRole("button", { name: /Total Income/ });
    await expect(incomeRow).toBeVisible();
    await expect(incomeRow).toContainText("$5550.00");
    await expect(card.getByRole("button", { name: /Total Savings/ })).toContainText("- $1250.00");
    await expect(card.getByRole("button", { name: /Total Expenses/ })).toContainText("- $2235.00");
    // Every section button carries a chevron (the drill-down affordance).
    for (const label of ["Total Income", "Total Savings", "Total Expenses"]) {
      const row = card.getByRole("button", { name: new RegExp(label) });
      await expect(row.locator("svg.lucide-chevron-down")).toBeVisible();
    }
  });

  test("clicking a section expands categories in place (no navigation)", async ({ page }) => {
    const card = page.locator("div.rounded-2xl").filter({ hasText: "Net Zero Breakdown" }).first();
    const expenseRow = card.getByRole("button", { name: /Total Expenses/ });

    // v32 S1 (the superset pin): the section rows carry aria-expanded with
    // ACCURATE state — the reference's rows have no attribute (its screen
    // readers can't tell the row expands). A deliberate, kept a11y superset
    // in the same family as the row-action aria-labels; pinned here so a
    // future parity sweep doesn't "fix" it away as drift.
    await expect(expenseRow).toHaveAttribute("aria-expanded", "false");
    await expenseRow.click();
    await expect(expenseRow).toHaveAttribute("aria-expanded", "true");

    // Categories appear sorted by amount desc, each with its total.
    const catSalary = card.getByRole("button", { name: /^Rent/ });
    await expect(catSalary).toBeVisible();
    await expect(catSalary).toContainText("$1850.00");
    await expect(card.getByRole("button", { name: /^Groceries/ })).toContainText("$320.00");
    await expect(card.getByRole("button", { name: /^Entertainment/ })).toContainText("$65.00");

    // The category drill-down rows carry the same accurate state.
    await expect(catSalary).toHaveAttribute("aria-expanded", "false");
    await catSalary.click();
    await expect(catSalary).toHaveAttribute("aria-expanded", "true");

    // The section footer: "3 categories" + the section total in orange.
    await expect(card.getByText("3 categories")).toBeVisible();

    // No navigation happened — we are still on the dashboard.
    await expect(page).toHaveURL(/\/dashboard$/);
  });

  test("clicking a category reveals subcategory and item rows", async ({ page }) => {
    const card = page.locator("div.rounded-2xl").filter({ hasText: "Net Zero Breakdown" }).first();
    await card.getByRole("button", { name: /Total Income/ }).click();
    await card.getByRole("button", { name: /^Salary/ }).click();

    // Subcategory row (gray) and its total both render ($5200.00 appears
    // at every drill level — the first is the category row).
    await expect(card.getByText("Main Job")).toBeVisible();
    await expect(card.getByText("$5200.00").first()).toBeVisible();

    // Item row: the seed's notes ("Net monthly salary") + amount.
    await expect(card.getByText("Net monthly salary")).toBeVisible();

    // Freelance has no notes → the literal "Item" label.
    await card.getByRole("button", { name: /^Freelance/ }).click();
    await expect(card.getByText("Item", { exact: true })).toBeVisible();
    await expect(card.getByText("$350.00").first()).toBeVisible();
  });

  test("the drill-down is an accordion — one section open at a time", async ({ page }) => {
    // Verified live on the reference: expanding a second section collapses
    // the first (bundle: i(r===E?null:E) + openCategories reset).
    const card = page.locator("div.rounded-2xl").filter({ hasText: "Net Zero Breakdown" }).first();
    await card.getByRole("button", { name: /Total Income/ }).click();
    await expect(card.getByRole("button", { name: /^Salary/ })).toBeVisible();

    await card.getByRole("button", { name: /Total Savings/ }).click();
    // Income's categories are gone; Savings' are in.
    await expect(card.getByRole("button", { name: /^Salary/ })).toHaveCount(0);
    await expect(card.getByRole("button", { name: /^Emergency Fund/ })).toBeVisible();
    await expect(card.getByText("2 categories").first()).toBeVisible();

    // Clicking the open section again collapses it.
    await card.getByRole("button", { name: /Total Savings/ }).click();
    await expect(card.getByRole("button", { name: /^Emergency Fund/ })).toHaveCount(0);
  });

  test("Net Balance renders positive in orangeLight with trending-up", async ({ page }) => {
    const card = page.locator("div.rounded-2xl").filter({ hasText: "Net Zero Breakdown" }).first();
    const net = card.getByText("Net Balance");
    await expect(net).toBeVisible();
    const amount = card.getByText("+$2065.00");
    // Positive balance → #f5a962 orangeLight (the reference's conditional).
    await expect(amount).toHaveCSS("color", "rgb(245, 169, 98)");
    await expect(net.locator("..").locator("svg.lucide-trending-up")).toBeVisible();
  });
});
