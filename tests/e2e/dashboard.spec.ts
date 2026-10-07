import { expect, test } from "@playwright/test";

// Dashboard: the NET ZERO GOAL hero (allocation %, balance, goal status),
// the Net Zero Breakdown rows with their sign prefixes and navigation, the
// three stat cards, the Spending Breakdown donut (recharts sectors + legend
// rows), and the Budget Guidelines card. Expected values are the seed's
// exact arithmetic (raw-amount sums, integer-cent math):
//   income 5550 · savings 1250 · expenses 2235 → balance +2065 (Under
//   Budget), allocation 62.8%; spending: need 7370 (81.6%), want 415
//   (4.6%), savings 1250 (13.8%) over a 9035 total.
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("dashboard", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    // Wait for the store's fetch — the amounts render with the data, not
    // on the static shell.
    await expect(page.getByText("+$2,065.00")).toBeVisible();
  });

  test("renders the page header with the Add Item button", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
    await expect(
      page.getByText("Track your income, savings, and expenses to achieve net zero"),
    ).toBeVisible();
    const add = page.getByRole("button", { name: "Add Item" });
    await expect(add).toBeVisible();
  });

  test("NET ZERO GOAL hero shows allocation, balance and Under Budget status", async ({ page }) => {
    await expect(page.getByText("NET ZERO GOAL")).toBeVisible();
    await expect(page.getByText("Income = Savings + Expenses")).toBeVisible();
    // Allocation: (1250 + 2235) / 5550 → 62.8%
    await expect(page.getByText("Budget Allocation")).toBeVisible();
    await expect(page.getByText("62.8%")).toBeVisible();
    // Balance panel: 5550 - 1250 - 2235 → $2,065.00 with Under Budget
    await expect(page.getByText("Balance", { exact: true })).toBeVisible();
    await expect(page.getByText("$2,065.00").first()).toBeVisible();
    await expect(page.getByText("Under Budget")).toBeVisible();
    // The hero's gradient: linear-gradient(135deg, forest-dark, forest-medium)
    const hero = page.locator("div.rounded-2xl").filter({ hasText: "NET ZERO GOAL" }).first();
    const bg = await hero.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(26, 58, 46)");
  });

  test("Net Zero Breakdown rows carry sign prefixes and navigate", async ({ page }) => {
    const card = page.locator("div.rounded-2xl").filter({ hasText: "Net Zero Breakdown" }).first();
    await expect(card.getByText("Total Income")).toBeVisible();
    await expect(card.getByText("$5,550.00")).toBeVisible();
    await expect(card.getByText("Total Savings")).toBeVisible();
    await expect(card.getByText("- $1,250.00")).toBeVisible();
    await expect(card.getByText("Total Expenses")).toBeVisible();
    await expect(card.getByText("- $2,235.00")).toBeVisible();
    await expect(card.getByText("Net Balance")).toBeVisible();
    await expect(card.getByText("+$2,065.00")).toBeVisible();

    // Rows navigate to their view (the reference's clickable rows).
    await card.getByText("Total Income").click();
    await expect(page).toHaveURL(/\/income$/);
  });

  test("stat cards show amounts, item counts and navigate", async ({ page }) => {
    // "Total Income" also names a breakdown row — scope the stat assertions
    // to the count footers and amounts, which are unique to the cards.
    await expect(page.getByText("2 items").first()).toBeVisible();
    await expect(page.getByText("3 items").first()).toBeVisible();

    await expect(page.getByText("$5,550.00").first()).toBeVisible();
    await expect(page.getByText("$1,250.00").first()).toBeVisible();
    await expect(page.getByText("$2,235.00").first()).toBeVisible();

    // Stat cards are clickable and route to their view.
    await page.getByText("$5,550.00").first().click();
    await expect(page).toHaveURL(/\/income$/);
  });

  test("Spending Breakdown renders donut sectors and legend rows", async ({ page }) => {
    await expect(page.getByText("Spending Breakdown")).toBeVisible();
    await expect(page.getByText("Needs vs Wants vs Savings")).toBeVisible();

    // recharts sectors carry the reference palette: Need #e07a3b (orange),
    // Want #3b7ea1 (blue), Savings #8fbc3f (lime). getComputedStyle resolves
    // the hex fills to rgb() strings.
    const sector = page.locator(".recharts-sector").first();
    await expect(sector).toBeVisible();
    const fills: string[] = await page.locator(".recharts-sector").evaluateAll((nodes) =>
      Array.from(new Set(nodes.map((n) => getComputedStyle(n).fill))),
    );
    expect(fills).toEqual(
      expect.arrayContaining(["rgb(224, 122, 59)", "rgb(59, 126, 161)", "rgb(143, 188, 63)"]),
    );

    // Legend rows: tinted p-3 rows with colored amounts + one-decimal pcts.
    await expect(page.getByText("Need").first()).toBeVisible();
    await expect(page.getByText("$7,370.00").first()).toBeVisible();
    await expect(page.getByText("81.6%").first()).toBeVisible();
    await expect(page.getByText("$415.00").first()).toBeVisible();
    await expect(page.getByText("4.6%").first()).toBeVisible();
    await expect(page.getByText("$1,250.00").first()).toBeVisible();
    await expect(page.getByText("13.8%").first()).toBeVisible();
  });

  test("Budget Guidelines card lists the 50/30/20 rules", async ({ page }) => {
    await expect(page.getByText("Budget Guidelines")).toBeVisible();
    await expect(page.getByText("Essential expenses like rent, utilities, groceries")).toBeVisible();
    await expect(page.getByText("Discretionary spending like entertainment, dining out")).toBeVisible();
    await expect(page.getByText("Emergency fund, retirement, investments")).toBeVisible();
  });

  test("quick actions open the Add Item dialog with the type preselected", async ({ page }) => {
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    await expect(dialog.getByRole("heading", { name: "Add Budget Item" })).toBeVisible();
    // The type select shows the preselected type (Income for this action)
    // — assert on the trigger's own text, not a page-wide text lookup (the
    // closed dropdown's hidden "Income" option would collide).
    await expect(dialog.getByRole("combobox", { name: "Type" })).toHaveText(/Income/);
    await dialog.getByRole("button", { name: "Cancel" }).click();
    await expect(dialog).toBeHidden();

    await page.getByRole("button", { name: "Add Savings" }).click();
    await expect(page.getByRole("dialog")).toBeVisible();
    await page.getByRole("button", { name: "Cancel" }).click();

    await page.getByRole("button", { name: "Add Expense" }).click();
    await expect(page.getByRole("dialog")).toBeVisible();
  });
});
