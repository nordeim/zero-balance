import { expect, test } from "@playwright/test";

// Dashboard: the NET ZERO GOAL hero (allocation %, |balance|, status-conditional
// chip/fill), the Net Zero Breakdown (3-level expandable drill-down — see
// breakdown.spec.ts), the three stat cards (text-3xl forestDark amounts), the
// Spending Breakdown donut (value-DESC sector order + iconed legend), the
// tinted Budget Guidelines cards, and the quick-action card buttons.
// Expected values are the seed's exact arithmetic:
//   income 5550 · savings 1250 · expenses 2235 → balance +2065 (Under
//   Budget), allocation 62.8%; spending over 9035 total: savings 1250
//   (13.8%), want 415 (4.6%), need 7370 (81.6%).
// Money is the reference's PLAIN format ("$5550.00", no thousands separator).
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("dashboard", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    // Wait for the store's fetch — the amounts render with the data, not
    // on the static shell.
    await expect(page.getByText("+$2065.00")).toBeVisible();
  });

  test("renders the page header with the gradient Add Item button", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
    await expect(
      page.getByText("Track your income, savings, and expenses to achieve net zero"),
    ).toBeVisible();
    const add = page.getByRole("button", { name: "Add Item" });
    await expect(add).toBeVisible();
    // The header button carries the forest→lime 135deg gradient.
    const bg = await add.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))");
  });

  test("NET ZERO GOAL hero shows allocation, |balance| and Under Budget status", async ({ page }) => {
    await expect(page.getByText("NET ZERO GOAL")).toBeVisible();
    await expect(page.getByText("Income = Savings + Expenses")).toBeVisible();
    // Allocation: (1250 + 2235) / 5550 → 62.8%
    await expect(page.getByText("Budget Allocation")).toBeVisible();
    await expect(page.getByText("62.8%")).toBeVisible();
    // Balance: 5550 - 1250 - 2235 → $2065.00 (plain format, Math.abs —
    // the sign lives in the status chip).
    await expect(page.getByText("Balance", { exact: true })).toBeVisible();
    await expect(page.getByText("$2065.00").first()).toBeVisible();
    await expect(page.getByText("Under Budget")).toBeVisible();
    // The hero's gradient: linear-gradient(135deg, forest-dark, forest-medium)
    const hero = page.locator("div.rounded-2xl").filter({ hasText: "NET ZERO GOAL" }).first();
    const bg = await hero.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(26, 58, 46)");
    // Under-budget allocation fill: orange gradient (reference bundle). The
    // computed string carries explicit 0%/100% stops.
    const fill = hero.locator("div.h-3 > div");
    const fillBg = await fill.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(fillBg).toContain("linear-gradient(90deg, rgb(224, 122, 59) 0%, rgb(245, 169, 98) 100%)");
  });

  test("stat cards show forestDark amounts, counts and navigate", async ({ page }) => {
    // Amounts: text-3xl forestDark, PLAIN format (no commas).
    await expect(page.getByText("$5550.00").first()).toBeVisible();
    await expect(page.getByText("$1250.00").first()).toBeVisible();
    await expect(page.getByText("$2235.00").first()).toBeVisible();

    // Amount color is forestDark rgb(26,58,46), NOT the type accent (the
    // breakdown row renders the same figure in lime — scope to the stat
    // card's text-3xl amount).
    const amountEl = page.locator("p.text-3xl").filter({ hasText: "$5550.00" });
    await expect(amountEl).toHaveCSS("color", "rgb(26, 58, 46)");

    // Counts (income 2, savings 2, expenses 3) with the h-px divider row.
    await expect(page.getByText("2 items", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("3 items", { exact: true }).first()).toBeVisible();

    // Stat cards are clickable and route to their view (click the card's
    // own amount — the breakdown row shows the same figure but expands
    // the drill-down instead of navigating).
    await page.locator("p.text-3xl").filter({ hasText: "$5550.00" }).click();
    await expect(page).toHaveURL(/\/income$/);
  });

  test("Spending Breakdown renders value-DESC sectors and iconed legend", async ({ page }) => {
    await expect(page.getByText("Spending Breakdown")).toBeVisible();
    await expect(page.getByText("Needs vs Wants vs Savings")).toBeVisible();

    // Sector order mirrors the reference (session-17 audit, plan v9 G1): its
    // donut data is sorted by value DESC — measured live as [Need $6025,
    // Savings $300, Want $200] with the biggest slice anchored at recharts'
    // 3-o'clock start. With the seed's data (need 7370 > savings 1250 > want
    // 415) the fills are [orange, lime, blue]. The v2-era [S, W, N] order was
    // the same convention with then-different reference data.
    const fills: string[] = await page.locator(".recharts-sector").evaluateAll((nodes) =>
      nodes.map((n) => getComputedStyle(n).fill),
    );
    expect(fills).toEqual(["rgb(224, 122, 59)", "rgb(143, 188, 63)", "rgb(59, 126, 161)"]);

    // The reference renders NO percentage-label connector lines (measured:
    // labelLineCount 0); recharts only omits them with labelLine={false}.
    const labelLines = await page.locator(".recharts-pie-label-line").count();
    expect(labelLines).toBe(0);

    // Legend rows (order Need → Savings → Want, value-desc) on the tinted bg
    // with circle-alert / piggy-bank / heart icons and plain amounts.
    const legend = page.locator("div.flex.flex-col.gap-3.mt-6");
    await expect(legend).toBeVisible();
    const rows = legend.locator("> div");
    await expect(rows).toHaveCount(3);
    await expect(rows.nth(0)).toContainText("Need");
    await expect(rows.nth(0)).toContainText("$7370.00");
    await expect(rows.nth(0)).toContainText("81.6%");
    await expect(rows.nth(0).locator("svg.lucide-circle-alert")).toBeVisible();
    await expect(rows.nth(1)).toContainText("Savings");
    await expect(rows.nth(1)).toContainText("$1250.00");
    await expect(rows.nth(1)).toContainText("13.8%");
    await expect(rows.nth(1).locator("svg.lucide-piggy-bank")).toBeVisible();
    await expect(rows.nth(2)).toContainText("Want");
    await expect(rows.nth(2)).toContainText("$415.00");
    await expect(rows.nth(2)).toContainText("4.6%");
    await expect(rows.nth(2).locator("svg.lucide-heart")).toBeVisible();
    // Tinted row background rgb(245,248,245).
    await expect(rows.nth(0)).toHaveCSS("background-color", "rgb(245, 248, 245)");
  });

  test("donut hover tooltip formats the value like the reference (v14 — plan G1)", async ({ page }) => {
    // Measured live on the reference: hovering a sector renders the recharts
    // DEFAULT tooltip with the item row "Need : $6025.00" — the value carries
    // the dollar sign and two decimals (the dashboard's plain money format).
    // The clone rendered the raw number ("7370") because <Tooltip /> had no
    // formatter. The tooltip chrome (both recharts defaults) is identical.
    // NB: the hover is dispatched synthetically (like the live probe) — a
    // Playwright .hover() loops forever because the mouse-following tooltip
    // re-triggers pointer events under the cursor.
    const hovered = await page.evaluate(() => {
      const sector = document.querySelector(".recharts-pie-sector path");
      if (!sector) return false;
      const r = sector.getBoundingClientRect();
      const cx = r.x + r.width / 2;
      const cy = r.y + r.height / 2;
      const ev = (type: string) => new MouseEvent(type, { bubbles: true, cancelable: true, clientX: cx, clientY: cy });
      sector.dispatchEvent(new PointerEvent("pointermove", { bubbles: true, cancelable: true, clientX: cx, clientY: cy }));
      sector.dispatchEvent(ev("mouseover"));
      sector.dispatchEvent(ev("mousemove"));
      return true;
    });
    expect(hovered).toBe(true);

    const value = page.locator(".recharts-tooltip-item-value");
    await expect(value).toHaveText("$7370.00"); // the seed's Need slice

    // The whole item row reads "name : value" like the reference's.
    const item = page.locator(".recharts-tooltip-item");
    await expect(item).toHaveText("Need : $7370.00");

    // The reference OVERRIDES the recharts default chrome: padding 10,
    // white bg, 1px #e5e7e3 border (its CARD token), radius 8, and the
    // soft 0 4px 12px shadow. Recharts 3's bare default (#cccccc border,
    // square corners, no shadow) drifts — pinned via contentStyle.
    const tip = page.locator(".recharts-default-tooltip");
    await expect(tip).toHaveCSS("padding", "10px");
    await expect(tip).toHaveCSS("border-radius", "8px");
    await expect(tip).toHaveCSS("border-width", "1px");
    await expect(tip).toHaveCSS("border-color", "rgb(229, 231, 227)");
    await expect(tip).toHaveCSS("box-shadow", "rgba(0, 0, 0, 0.1) 0px 4px 12px 0px");
    // recharts 2 (the reference) renders the item row in BLACK; recharts 3
    // defaults it to the sector's fill color (orange) — pinned black.
    await expect(item).toHaveCSS("color", "rgb(0, 0, 0)");
  });

  test("Budget Guidelines renders the tinted 50/30/20 cards", async ({ page }) => {
    await expect(page.getByText("Budget Guidelines")).toBeVisible();
    await expect(page.getByText("Essential expenses like rent, utilities, groceries")).toBeVisible();
    await expect(page.getByText("Discretionary spending like entertainment, dining out")).toBeVisible();
    await expect(page.getByText("Emergency fund, retirement, investments")).toBeVisible();

    // Needs card: orange tint + border (measured #fff7f5 / #fcddd5).
    const needs = page.locator("div").filter({ hasText: "Essential expenses like rent, utilities, groceries" }).last();
    await expect(needs).toHaveCSS("background-color", "rgb(255, 247, 245)");
    await expect(needs).toHaveCSS("border-color", "rgb(252, 221, 213)");
    // Savings card: green tint.
    const savings = page.locator("div").filter({ hasText: "Emergency fund, retirement, investments" }).last();
    await expect(savings).toHaveCSS("background-color", "rgb(245, 249, 240)");
    await expect(savings).toHaveCSS("border-color", "rgb(223, 236, 208)");
  });

  test("quick action card buttons open the Add Item dialog with the type preselected", async ({ page }) => {
    const income = page.getByRole("button", { name: "Add Income" });
    await expect(income).toHaveClass(/rounded-2xl/);
    await income.click();
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
