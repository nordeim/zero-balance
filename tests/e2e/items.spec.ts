import { expect, test } from "@playwright/test";

// Item views (Income / Expenses / Savings): headers with the gradient icon
// chip and the always-plural "N items · $X" subtitle (plain money format),
// search + category/frequency(/payment-method) filters, seeded item cards
// with the reference's badge maps (per-classification icon/border,
// per-frequency colors, capitalized green Recurring, always-slate status),
// and the add → edit → delete round-trip. Expense cards carry the
// hover-revealed Edit/Calculate buttons (the calculator itself is covered by
// calculator.spec.ts).
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("income view", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByText("$5550.00").first()).toBeVisible();
  });

  test("renders the header, gradient chip, count subtitle and seeded cards", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Income" })).toBeVisible();
    // The subtitle is ALWAYS plural ("2 items") with plain money.
    await expect(page.getByText("2 items · $5550.00")).toBeVisible();
    const add = page.getByRole("button", { name: "Add Income" });
    await expect(add).toBeVisible();
    // Add Income carries the lime→limeLight gradient.
    const bg = await add.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(143, 188, 63), rgb(184, 216, 126))");

    // Header chip: lime gradient with a WHITE wallet icon (reference DOM).
    // Scope to the h-12 chip (the sidebar's Income link also carries a
    // wallet icon inside an <a>).
    const chip = page.locator("div.h-12").filter({ has: page.locator("svg.lucide-wallet") });
    const chipBg = await chip.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(chipBg).toContain("linear-gradient(135deg, rgb(143, 188, 63), rgb(184, 216, 126))");
    await expect(chip.locator("svg.lucide-wallet")).toHaveClass(/text-white/);

    await expect(page.getByText("Salary").first()).toBeVisible();
    await expect(page.getByText("Freelance").first()).toBeVisible();
    // Amounts colored per type: income lime, plain format.
    const card = page.locator("div.rounded-xl").filter({ hasText: "Salary" }).first();
    await expect(card.getByText("$5200.00")).toBeVisible();
  });

  test("search filters the card list", async ({ page }) => {
    await page.getByPlaceholder("Search income items...").fill("salary");
    await expect(page.getByText("Freelance")).toHaveCount(0);
    await expect(page.getByText("Salary").first()).toBeVisible();

    await page.getByPlaceholder("Search income items...").fill("zzz-no-match");
    await expect(page.getByText("Salary")).toHaveCount(0);
  });

  test("add → edit → delete round-trip through the dialog", async ({ page }) => {
    // --- add
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    await page.getByLabel("Amount").fill("77.50");
    // exact: the "Filter by category" combobox and the Subcategory input
    // also substring-match "Category".
    await page.getByLabel("Category", { exact: true }).fill("Dividends");
    await page.getByLabel("Subcategory").fill("Shares");
    dialog.getByRole("radio", { name: /Want/i }).check();
    // Settle beat: the radio click re-renders the form (adjust-state pattern
    // + controlled Select); clicking the trigger mid-re-render can dispatch
    // onto a stale node and the dropdown never opens.
    await page.waitForTimeout(400);
    await dialog.getByRole("combobox", { name: "Frequency" }).click();
    await page.getByRole("option", { name: "Quarterly" }).click();
    await page.getByRole("button", { name: "Save Item" }).click();
    await expect(dialog).toBeHidden();

    const created = page.locator("div.rounded-xl").filter({ hasText: "Dividends" }).first();
    await expect(created).toBeVisible();
    await expect(created.getByText("$77.50")).toBeVisible();
    // quarterly → indigo badge (reference frequency map).
    const quarterlyBadge = created.getByText("quarterly", { exact: true });
    await expect(quarterlyBadge).toBeVisible();
    await expect(quarterlyBadge).toHaveClass(/bg-indigo-50/);
    // The header count + subtitle updated (plain money).
    await expect(page.getByText("3 items · $5627.50")).toBeVisible();

    // --- edit via the ellipsis actions menu (income cards have no inline
    // Edit button — that's the expenses-only affordance)
    const card = page.locator("div.rounded-xl").filter({ hasText: "Dividends" }).first();
    await card.hover();
    await page.getByRole("button", { name: "Actions for Dividends" }).click();
    await page.getByRole("menuitem", { name: "Edit" }).click();
    await expect(page.getByRole("dialog")).toBeVisible();
    await page.getByLabel("Amount").fill("99.99");
    await page.getByRole("button", { name: "Save Item" }).click();
    await expect(page.getByRole("dialog")).toBeHidden();
    await expect(page.locator("div.rounded-xl").filter({ hasText: "Dividends" }).first().getByText("$99.99")).toBeVisible();

    // --- delete (inline confirm, never a modal)
    await card.hover();
    await page.getByRole("button", { name: "Actions for Dividends" }).click();
    await page.getByRole("menuitem", { name: "Delete" }).click();
    await expect(page.getByText("Delete this item?")).toBeVisible();
    await page.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(page.getByText("Dividends")).toHaveCount(0);
    await expect(page.getByText("2 items · $5550.00")).toBeVisible();
  });
});

test.describe("expenses view", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
  });

  test("renders seeded cards with badges and the extra payment-method filter", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Expenses" })).toBeVisible();
    await expect(page.getByPlaceholder("Search expense items...")).toBeVisible();

    // The expenses-only "All Payment Methods" filter (superset parity).
    await expect(page.getByText("All Payment Methods")).toBeVisible();
    // Add Expense carries the orange gradient.
    const add = page.getByRole("button", { name: "Add Expense" });
    const bg = await add.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))");

    // Seeded cards with classification + frequency badges.
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await expect(rent.getByText("$1850.00")).toBeVisible();
    const needBadge = rent.getByText("need", { exact: true });
    await expect(needBadge).toBeVisible();
    await expect(needBadge).toHaveClass(/bg-red-50 text-red-700 border-red-200/);
    await expect(rent.getByText("monthly", { exact: true })).toHaveClass(/bg-purple-50/);
    await expect(rent.getByText("active", { exact: true })).toHaveClass(/bg-slate-50/);
    // Recurring badge: capitalized, green, with the repeat icon (class
    // order interleaves utilities — assert each color class separately).
    const recurring = rent.getByText("Recurring", { exact: true });
    await expect(recurring).toBeVisible();
    await expect(recurring).toHaveClass(/bg-green-50/);
    await expect(recurring).toHaveClass(/text-green-700/);
    await expect(recurring.locator("svg.lucide-repeat")).toBeVisible();
  });

  test("expense cards carry the hover-revealed Edit and Calculate buttons", async ({ page }) => {
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    const edit = rent.getByRole("button", { name: "Edit", exact: true });
    const calculate = rent.getByRole("button", { name: "Calculate" });
    // Hover-revealed (opacity-0 → group-hover) white buttons.
    await rent.hover();
    await expect(edit).toBeVisible();
    await expect(edit).toHaveAttribute("title", "Edit Category");
    await expect(calculate).toBeVisible();
    await expect(calculate).toHaveAttribute("title", "Open Calculator");
    await expect(calculate).toHaveClass(/text-orange-600/);
    // Expense cards have NO ellipsis menu (reference DOM: 0/3 cards).
    await expect(rent.getByRole("button", { name: /Actions for/ })).toHaveCount(0);
  });

  test("the edit dialog offers the superset delete path", async ({ page }) => {
    // The reference has no delete affordance on expense cards; the clone's
    // edit dialog carries a red Delete button (edit mode only).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Edit", exact: true }).click();
    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    const del = dialog.getByRole("button", { name: "Delete" });
    await expect(del).toBeVisible();
    await del.click();
    await expect(dialog.getByText("Delete this item?")).toBeVisible();
    await dialog.getByRole("button", { name: "Cancel", exact: true }).last().click();
  });

  test("category filter narrows the list", async ({ page }) => {
    await page.getByText("All Categories").click();
    await page.getByRole("option", { name: "Groceries" }).click();
    await expect(page.getByText("Rent")).toHaveCount(0);
    await expect(page.getByText("Groceries").first()).toBeVisible();
  });
});

test.describe("savings view", () => {
  test("renders the seeded savings items with the blue accent", async ({ page }) => {
    await page.goto("/savings");
    // Wait for the store's fetch — the empty state renders transiently
    // before the items arrive (the h1 + transient h3 would collide in a
    // non-exact heading lookup).
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();
    await expect(page.getByRole("heading", { name: "Savings", exact: true })).toBeVisible();
    await expect(page.getByText("Emergency Fund").first()).toBeVisible();
    await expect(page.getByText("Investments").first()).toBeVisible();
    // Add Savings carries the blue gradient.
    const add = page.getByRole("button", { name: "Add Savings" });
    const bg = await add.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(44, 95, 124), rgb(59, 126, 161))");
    // The savings classification badge is green with a piggy-bank icon.
    const fund = page.locator("div.rounded-xl").filter({ hasText: "Emergency Fund" }).first();
    const savingsBadge = fund.getByText("savings", { exact: true });
    await expect(savingsBadge).toHaveClass(/bg-green-50 text-green-700 border-green-200/);
    await expect(savingsBadge.locator("svg.lucide-piggy-bank")).toBeVisible();
  });
});
