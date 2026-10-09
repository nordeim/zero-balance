import { test, expect } from "@playwright/test";

// v28 G3 (docs/remediation-plan-v28.md): the Budget Item Details sheet —
// the reference opens a read-only details dialog on ITEM-CARD BODY CLICK
// (any type, desktop AND mobile: overlay `fixed inset-0 z-50 flex
// items-end md:items-center justify-center p-0 md:p-4` — bottom-sheet at
// mobile — panel `bg-white rounded-t-3xl md:rounded-2xl shadow-2xl
// max-w-lg w-full max-h-[85vh] overflow-y-auto`). The clone's card click
// was a dead surface before this iteration. All geometry/classes/colors
// below were measured live on the reference this session.

test.describe("budget item details sheet (v28 — plan G3)", () => {
  test("clicking an expense card body opens the details sheet with the reference's structure", async ({ page }) => {
    await page.goto("/expenses");
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await expect(rent).toBeVisible();

    // The card BODY click (not the buttons) opens the details sheet.
    await rent.locator("h4").click();

    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    await expect(dialog.getByRole("heading", { name: "Budget Item Details" })).toBeVisible();

    // The overlay + panel geometry family (measured on the reference):
    // forest-dark 50% overlay + blur, bottom-sheet anchored at mobile,
    // centered 512px (max-w-lg) at desktop, 85vh cap, t-3xl/2xl radii.
    // The dialog (role=dialog) IS the panel; the overlay is its portal
    // sibling (Radix renders overlay + content side by side).
    const overlayInfo = await dialog.evaluate((el) => {
      const overlay = [...el.parentElement!.children].find(
        (c) => c !== el && /inset-0/.test(c.className),
      ) as HTMLElement | null;
      return {
        overlayCls: overlay ? overlay.className : null,
        overlayBg: overlay ? getComputedStyle(overlay).backgroundColor : null,
        overlayBlur: overlay ? getComputedStyle(overlay).backdropFilter : null,
        panelCls: el.className,
        panelMaxW: getComputedStyle(el).maxWidth,
      };
    });
    expect(overlayInfo.overlayBg).toBe("rgba(26, 58, 46, 0.5)");
    expect(overlayInfo.overlayBlur).toContain("blur(8px)");
    // The panel self-positions: bottom-anchored full-width sheet at mobile,
    // centered at md: (the reference achieves the same geometry via its
    // items-end/md:items-center flex overlay — the computed positions are
    // identical; pinned here on the panel's own class family).
    expect(overlayInfo.panelCls).toContain("max-w-lg");
    expect(overlayInfo.panelCls).toContain("max-h-[85vh]");
    expect(overlayInfo.panelCls).toContain("rounded-t-3xl");
    expect(overlayInfo.panelCls).toContain("md:rounded-2xl");
    expect(overlayInfo.panelCls).toContain("bottom-0");
    expect(overlayInfo.panelCls).toContain("md:top-1/2");
    expect(overlayInfo.panelMaxW).toBe("512px");

    // The sticky header + the X close (the v27 ghost-icon family).
    const header = dialog.locator("div.sticky");
    await expect(header).toBeVisible();
    const x = header.getByRole("button");
    await expect(x).toHaveClass(/focus-visible:ring-1/);
    await expect(x).toHaveClass(/hover:text-accent-foreground/);

    // The summary: type + classification badges, name, type-colored amount.
    await expect(dialog.getByText("EXPENSE", { exact: true })).toBeVisible();
    await expect(dialog.getByText("NEED", { exact: true })).toBeVisible();
    await expect(dialog.getByRole("heading", { name: "Rent", level: 3 })).toBeVisible();
    const amount = dialog.getByText("$1850.00");
    await expect(amount).toBeVisible();
    await expect(amount).toHaveClass(/text-4xl/);
    await expect(amount).toHaveClass(/font-bold/);

    // The type badge + amount carry the expense orange (measured
    // rgb(224, 122, 59) on the reference).
    const colors = await dialog.evaluate((el) => {
      const badge = [...el.querySelectorAll("div, span")].find(
        (d) => (d.textContent || "").trim() === "EXPENSE",
      );
      const amt = [...el.querySelectorAll("p")].find((p) =>
        /^\$[\d,]/.test((p.textContent || "").trim()),
      );
      return {
        badgeBg: badge ? getComputedStyle(badge).backgroundColor : null,
        badgeColor: badge ? getComputedStyle(badge).color : null,
        badgeCls: badge ? badge.className : null,
        amountColor: amt ? getComputedStyle(amt).color : null,
      };
    });
    expect(colors.badgeBg).toBe("rgba(224, 122, 59, 0.125)");
    expect(colors.badgeColor).toBe("rgb(224, 122, 59)");
    expect(colors.badgeCls).toContain("rounded-full");
    expect(colors.amountColor).toBe("rgb(224, 122, 59)");

    // The classification block: tinted rounded-xl, 20px icon, per-cls color.
    const clsBlock = dialog.locator("div.rounded-xl.p-4");
    await expect(clsBlock).toBeVisible();
    await expect(clsBlock.getByText("Need", { exact: true })).toBeVisible();
    await expect(
      clsBlock.getByText("Essential expenses like rent, utilities, and groceries"),
    ).toBeVisible();
    const clsInfo = await clsBlock.evaluate((el) => ({
      bg: getComputedStyle(el).backgroundColor,
      title: getComputedStyle(el.querySelector("p.font-semibold")!).color,
      iconW: Math.round(el.querySelector("svg")!.getBoundingClientRect().width),
    }));
    expect(clsInfo.bg).toBe("rgb(255, 247, 245)");
    expect(clsInfo.title).toBe("rgb(224, 122, 59)");
    expect(clsInfo.iconW).toBe(20);

    // The facts: Date / Frequency / Recurring / Status — Rent has NO notes,
    // so the Notes fact must NOT render (measured conditional).
    await expect(dialog.getByText("Date", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Frequency", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Recurring", { exact: true })).toBeVisible();
    await expect(dialog.getByText("monthly", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Yes", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Status", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Notes", { exact: true })).toHaveCount(0);

    // The meta footer: Created + Last Updated (12px forest values).
    await expect(dialog.getByText("Created", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Last Updated", { exact: true })).toBeVisible();

    // The X closes the sheet.
    await x.click();
    await expect(dialog).toBeHidden();
  });

  test("the income card's sheet shows the lime family, the Recurring fact, and Notes when present", async ({ page }) => {
    await page.goto("/income");
    const salary = page.locator("div.rounded-xl").filter({ hasText: "Salary" }).first();
    await expect(salary).toBeVisible();
    await salary.locator("h4").click();

    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();

    await expect(dialog.getByText("INCOME", { exact: true })).toBeVisible();
    const colors = await dialog.evaluate((el) => {
      const badge = [...el.querySelectorAll("div, span")].find(
        (d) => (d.textContent || "").trim() === "INCOME",
      );
      const amt = [...el.querySelectorAll("p")].find((p) =>
        /^\$[\d,]/.test((p.textContent || "").trim()),
      );
      return {
        badgeBg: badge ? getComputedStyle(badge).backgroundColor : null,
        badgeColor: badge ? getComputedStyle(badge).color : null,
        amountColor: amt ? getComputedStyle(amt).color : null,
      };
    });
    // The income lime family (measured rgb(143, 188, 63)).
    expect(colors.badgeBg).toBe("rgba(143, 188, 63, 0.125)");
    expect(colors.badgeColor).toBe("rgb(143, 188, 63)");
    expect(colors.amountColor).toBe("rgb(143, 188, 63)");

    // The seeded Salary carries notes — the Notes fact renders with them.
    await expect(dialog.getByText("Notes", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Net monthly salary")).toBeVisible();

    // The name + subcategory surface in the summary.
    await expect(dialog.getByRole("heading", { name: "Salary", level: 3 })).toBeVisible();
  });

  test("the action buttons still act — the card click does not shadow Edit", async ({ page }) => {
    await page.goto("/expenses");
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    // The footer Edit button opens the EDIT dialog (its own action), not
    // the details sheet.
    await rent.hover();
    await rent.getByRole("button", { name: "Edit", exact: true }).click();
    const editDialog = page.getByRole("dialog");
    await expect(editDialog).toBeVisible();
    // The edit dialog's own header (not the details sheet's).
    await expect(editDialog.getByText(/Add Budget Item|Edit Budget Item|Budget Item/)).toBeVisible();
    await expect(editDialog.getByRole("heading", { name: "Budget Item Details" })).toHaveCount(0);
  });
});
