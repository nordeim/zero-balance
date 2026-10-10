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

  test("line-item row chrome + dialog placeholders match the reference (v6 G7-G11)", async ({ page }) => {
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });

    // G7: the empty-state calculator icon inherits the near-black foreground
    // (the clone pinned forestDark — the ref is rgb(10,10,10)), 48px, 0.2.
    const emptyIcon = await page.evaluate(() => {
      const dlg = document.querySelector('[role="dialog"]');
      const svg = dlg?.querySelector("svg.opacity-20") ?? null;
      if (!svg) return null;
      const cs = getComputedStyle(svg);
      const r = svg.getBoundingClientRect();
      return { color: cs.color, opacity: cs.opacity, w: Math.round(r.width) };
    });
    expect(emptyIcon).not.toBeNull();
    expect(emptyIcon!.color).toBe("rgb(10, 10, 10)");
    expect(emptyIcon!.opacity).toBe("0.2");
    expect(emptyIcon!.w).toBe(48);

    // G8: the reference's placeholders for Payment Method + Notes.
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await expect(lineDialog).toBeVisible();
    await expect(lineDialog.getByLabel("Payment Method")).toHaveAttribute(
      "placeholder",
      "e.g., Direct Debit, Credit Card",
    );
    await expect(lineDialog.getByLabel("Notes")).toHaveAttribute(
      "placeholder",
      "Additional details about this item...",
    );

    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Based on 1 item")).toBeVisible();

    // G9/G10 (v21 re-measure): the reference's row actions are now
    // HOVER-REVEALED — the action container renders `opacity-0
    // group-hover:opacity-100` (measured at rest with the pointer parked
    // far from the row; the v6-era always-visible measurement predates the
    // reference's chrome change). The buttons keep the geometry: 32px
    // buttons, 16px icons, edit near-black, delete red. A real .hover() on
    // the row flips the container to opacity 1.
    await page.mouse.move(8, 400); // park the pointer far from the row
    await page.waitForTimeout(300); // let any transition settle
    const rowChrome = await page.evaluate(() => {
      const dlg = document.querySelector('[role="dialog"]');
      const editBtn = dlg?.querySelector<HTMLButtonElement>('button[aria-label="Edit Contents Insurance"]');
      const delBtn = dlg?.querySelector<HTMLButtonElement>('button[aria-label="Delete Contents Insurance"]');
      if (!editBtn || !delBtn) return null;
      const shape = (b: HTMLButtonElement) => {
        const cs = getComputedStyle(b);
        const svg = b.querySelector("svg");
        const r = svg ? svg.getBoundingClientRect() : null;
        return {
          opacity: cs.opacity,
          containerOpacity: getComputedStyle(b.parentElement!).opacity,
          w: Math.round(b.getBoundingClientRect().width),
          iconW: r ? Math.round(r.width) : null,
          color: cs.color,
        };
      };
      // the "active" status pill
      const pill = [...(dlg?.querySelectorAll("span") || [])].find(
        (s) => (s.textContent || "").trim() === "active",
      );
      const pcs = pill ? getComputedStyle(pill) : null;
      return {
        edit: shape(editBtn),
        del: shape(delBtn),
        pill: pill ? { bg: pcs!.backgroundColor, color: pcs!.color } : null,
      };
    });
    expect(rowChrome).not.toBeNull();
    // At rest the actions are hidden (the reference's hover-gate).
    expect(rowChrome!.edit.containerOpacity).toBe("0");
    expect(rowChrome!.del.containerOpacity).toBe("0");
    expect(rowChrome!.edit.w).toBe(32);
    expect(rowChrome!.del.w).toBe(32);
    expect(rowChrome!.edit.iconW).toBe(16);
    expect(rowChrome!.del.iconW).toBe(16);
    expect(rowChrome!.edit.color).toBe("rgb(10, 10, 10)");
    expect(rowChrome!.del.color).toBe("rgb(220, 38, 38)");
    // Under a real row hover the actions reveal (opacity 1) — the
    // group-hover chain works (and the v4 media-gate pin in globals.css
    // keeps it working on hover:none devices too).
    await page.hover("text=Contents Insurance");
    await page.waitForTimeout(350); // transition-opacity settle
    const revealed = await page.evaluate(() => {
      const dlg = document.querySelector('[role="dialog"]');
      const editBtn = dlg?.querySelector<HTMLButtonElement>('button[aria-label="Edit Contents Insurance"]');
      return editBtn ? getComputedStyle(editBtn.parentElement!).opacity : null;
    });
    expect(revealed).toBe("1");
    // G11: the active status pill = green-50/green-700 in plain rgb.
    expect(rowChrome!.pill!.bg).toBe("rgb(240, 253, 244)");
    expect(rowChrome!.pill!.color).toBe("rgb(21, 128, 61)");

    // --- cleanup: remove the row, restore the seed's Rent amount.
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await dialog.getByText("Based on 0 items").waitFor();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });

  test("row actions render the reference's focus-visible ring family (v32 G1)", async ({ page }) => {
    // The reference's 32px row-action buttons carry the shadcn focus
    // family (measured live via a REAL Tab walk: the focused Edit renders
    // outline solid 2px TRANSPARENT + the 1px #0a0a0a ring shadow with
    // the white 0-width lead layer — the class string includes
    // focus-visible:outline-none focus-visible:ring-1
    // focus-visible:ring-ring). The clone's raw buttons rendered the
    // browser-default `outline: auto` instead — this test pins the fix.
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });

    // Create the fixture row (the row-chrome test's pattern).
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Based on 1 item")).toBeVisible();

    // Park the pointer far from the row (the hover-gate stays closed —
    // the reveal is hover-only, the ring is what a keyboard user gets).
    await page.mouse.move(8, 400);
    await page.waitForTimeout(300);

    // focusVisible:true is the same probe technique the dialog-buttons
    // spec uses (a real Chromium FocusOptions member; TS's DOM lib lags).
    // SETTLE before reading: the buttons carry transition-colors, whose v4
    // property list includes outline-color — an immediate read catches the
    // transparent settle MID-FLIGHT (oklab-interpolated, the v23 G1 lesson).
    const focused = await page.evaluate(async () => {
      const dlg = document.querySelector('[role="dialog"]');
      const read = async (b: HTMLButtonElement | null) => {
        if (!b) return null;
        (b as HTMLElement).focus({ focusVisible: true } as unknown as FocusOptions);
        await new Promise((r) => setTimeout(r, 350));
        const cs = getComputedStyle(b);
        return {
          shadow: cs.boxShadow,
          outline: `${cs.outlineStyle}/${cs.outlineWidth}/${cs.outlineColor}`,
          offset: cs.outlineOffset,
        };
      };
      return {
        edit: await read(dlg?.querySelector<HTMLButtonElement>('button[aria-label="Edit Contents Insurance"]') ?? null),
        del: await read(dlg?.querySelector<HTMLButtonElement>('button[aria-label="Delete Contents Insurance"]') ?? null),
      };
    });
    expect(focused.edit).not.toBeNull();
    expect(focused.del).not.toBeNull();
    // The 1px #0a0a0a ring (ring-1 ring-ring — --color-ring: #0a0a0a).
    expect(focused.edit!.shadow).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");
    expect(focused.del!.shadow).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");
    // The v3 outline-none form: transparent 2px + offset 2 — NOT the
    // browser-default `auto` outline the drifted build rendered.
    expect(focused.edit!.outline).toBe("solid/2px/rgba(0, 0, 0, 0)");
    expect(focused.edit!.offset).toBe("2px");

    // --- cleanup: remove the row, restore the seed's Rent amount.
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
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
