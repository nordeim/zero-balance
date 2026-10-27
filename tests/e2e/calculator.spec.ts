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

  test("the frequency Select's listbox keyboard contract (v34 S2)", async ({ page }) => {
    // The session-69 surface #2, measured live on both sites: the
    // sub-dialog's Frequency control is the reference's Radix combobox
    // family — the same 6 options in the same order, the fresh-open
    // highlight on the SELECTED option (:focus-driven, bg #f5f5f5), arrow
    // roving CLAMPED at both ends, Home/End jumps, Escape closing the
    // POPUP only (focus back to the trigger, the sub-dialog stays), and
    // Enter selecting. Playwright's real page focus renders the :focus
    // highlight (the agent-browser L1 artifact cannot strike here).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });

    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await expect(lineDialog).toBeVisible();

    // --- (1) fresh-open: the selected value (Monthly) is focused and
    // renders the accent highlight (rgb(245,245,245) / rgb(23,23,23) —
    // the :focus-driven shadcn family, byte-measured on both sites).
    const freq = lineDialog.getByRole("combobox", { name: "Frequency" });
    await freq.click();
    const monthly = page.getByRole("option", { name: "Monthly", exact: true });
    await expect(monthly).toBeVisible();
    await expect(monthly).toBeFocused();
    await expect(monthly).toHaveCSS("background-color", "rgb(245, 245, 245)");
    await expect(monthly).toHaveCSS("color", "rgb(23, 23, 23)");

    // --- (2) ArrowDown roves (Monthly → Quarterly), the highlight
    // following the focus.
    await page.keyboard.press("ArrowDown");
    const quarterly = page.getByRole("option", { name: "Quarterly", exact: true });
    await expect(quarterly).toBeFocused();
    await expect(quarterly).toHaveCSS("background-color", "rgb(245, 245, 245)");

    // --- (3) CLAMPED at the end: walk to Annually, then two more
    // ArrowDowns leave it there (no wrap — measured on both sites).
    await page.keyboard.press("ArrowDown");
    const annually = page.getByRole("option", { name: "Annually", exact: true });
    await expect(annually).toBeFocused();
    await page.keyboard.press("ArrowDown");
    await page.keyboard.press("ArrowDown");
    await expect(annually).toBeFocused();

    // --- (4) Home jumps to the first; End back to the last.
    await page.keyboard.press("Home");
    const oneTime = page.getByRole("option", { name: "One-time", exact: true });
    await expect(oneTime).toBeFocused();
    await page.keyboard.press("End");
    await expect(annually).toBeFocused();

    // --- (5) Escape closes the POPUP ONLY — focus returns to the
    // trigger and the sub-dialog stays open (the reference's plain-div
    // dialogs ignore Escape, but its Radix popups do close; identical
    // on the clone — measured).
    await page.keyboard.press("Escape");
    await expect(page.getByRole("option", { name: "Monthly", exact: true })).toHaveCount(0);
    await expect(freq).toBeFocused();
    await expect(lineDialog).toBeVisible();

    // --- (6) Enter selects: re-open, rove, Enter — the trigger updates
    // to the highlighted option and the popup closes with focus on the
    // trigger. (Each rove gets an implicit-settle focus assertion — a
    // back-to-back press burst can outrace Radix's roving.)
    await freq.click();
    await expect(monthly).toBeFocused();
    await page.keyboard.press("ArrowDown");
    await expect(quarterly).toBeFocused();
    await page.keyboard.press("ArrowDown");
    await expect(annually).toBeFocused();
    await page.keyboard.press("Enter");
    await expect(page.getByRole("option", { name: "Quarterly", exact: true })).toHaveCount(0);
    await expect(freq).toContainText("Annually");
    await expect(freq).toBeFocused();

    // --- cleanup: cancel the sub-dialog (nothing persisted), close the
    // calculator.
    await lineDialog.getByRole("button", { name: "Cancel" }).click();
    await expect(lineDialog).toBeHidden();
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

    // v33 S1 pin (docs/remediation-plan-v33.md — the session-67 toast
    // surface): the toast ANNOUNCES. Radix's hidden portal mirrors the
    // toast text into a role=status / aria-live region for ~1s after the
    // toast mounts (measured: `Notification Line item added`,
    // aria-live=assertive — the foreground-type default). Read promptly:
    // the announcer unmounts at 1s (this read lands ~200ms after the
    // save). The visible li itself carries NO role/live (Radix's design
    // — the announcer handles the announcement), so this locator matches
    // exactly one element. Guards a future toast-system rewrite from
    // silently dropping the announcement.
    const announcer = page.locator('[role="status"][aria-live]');
    await expect(announcer).toHaveCount(1);
    await expect(announcer).toContainText("Line item added");

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

// ---------------------------------------------------------------------------
// v45 — the line-item row census + the REAL-hover shadow (plan F2,
// docs/remediation-plan-v45.md).
//
// Measured live on BOTH sites (calc-row-v45.mjs + the tag/hover driver
// steps; the reference's measurements required its RENT calculator — the
// only one of its four expense cards with line items, "Contents
// Insurance"): the dialog panel 768 wide at 1280 / 608 at 640 (w-full
// max-w-3xl inside the p-4 overlay); the row 720/560 wide, pad 16,
// radius 12, border 1px rgb(229,231,227), boxShadow none at rest, bg
// white, transition all 0.15s (v4's default 150ms = v3's — matching);
// the rest action pair opacity 0 / 32px buttons. Under a REAL pointer
// hover the row's hover:shadow-md engages on BOTH sites with the
// IDENTICAL visible layers and the action pair reveals (opacity 1).
// The hover-shadow assertions use the toContain idiom on the VISIBLE
// layers — the accepted-leads convention (v4's transparent composition
// leads paint nothing — the v10 lesson, restated at
// login-parity.spec.ts:671): a future Tailwind upgrade that changes the
// shadow-md numerics must fail these pins.
test.describe("line-item row census + REAL hover (v45 — plan F2)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
  });

  test("the row census + the hover shadow-md + the action reveal at 1280 (v45 F2a)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
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
    await page.waitForTimeout(300);

    const census = await page.evaluate(() => {
      const panel = [...document.querySelectorAll('[role="dialog"]')].pop() as HTMLElement;
      if (!panel) return null;
      const h4 = [...panel.querySelectorAll("h4")].find(
        (h) => (h.textContent || "").trim() === "Contents Insurance",
      );
      if (!h4) return null;
      let row: HTMLElement = h4 as HTMLElement;
      while (row && row !== panel) {
        const cs = getComputedStyle(row);
        if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === "rgb(255, 255, 255)" && cs.padding === "16px") break;
        row = row.parentElement!;
      }
      if (!row || row === panel) return null;
      const cs = getComputedStyle(row);
      const actions = [...row.querySelectorAll("div")].find(
        (d) =>
          getComputedStyle(d).display === "flex" &&
          getComputedStyle(d).opacity === "0" &&
          d.querySelectorAll("button").length >= 1,
      );
      return {
        panelW: Math.round(panel.getBoundingClientRect().width),
        row: {
          w: Math.round(row.getBoundingClientRect().width),
          pad: cs.padding,
          radius: cs.borderRadius,
          border: `${cs.borderTopWidth} ${cs.borderTopStyle} ${cs.borderTopColor}`,
          boxShadow: cs.boxShadow,
          bg: cs.backgroundColor,
          transition: cs.transitionProperty,
          transitionDur: cs.transitionDuration,
        },
        actions: actions
          ? {
              opacity: getComputedStyle(actions).opacity,
              btnW: Math.round(actions.querySelector("button")!.getBoundingClientRect().width),
            }
          : null,
      };
    });
    expect(census).not.toBeNull();
    expect(census!.panelW).toBe(768);
    expect(census!.row.w).toBe(720);
    expect(census!.row.pad).toBe("16px");
    expect(census!.row.radius).toBe("12px");
    expect(census!.row.border).toBe("1px solid rgb(229, 231, 227)");
    expect(census!.row.boxShadow).toBe("none");
    expect(census!.row.bg).toBe("rgb(255, 255, 255)");
    expect(census!.row.transition).toBe("all");
    expect(census!.row.transitionDur).toBe("0.15s");
    expect(census!.actions!.opacity).toBe("0");
    expect(census!.actions!.btnW).toBe(32);

    // A REAL pointer hover: shadow-md engages (the row carries NO inline
    // boxShadow — unlike the item cards, the hover is LIVE) with the
    // reference's VISIBLE layers, and the action pair reveals.
    const rowLoc = dialog
      .getByRole("heading", { name: "Contents Insurance" })
      .locator("xpath=ancestor::div[contains(@class, 'p-4')][1]");
    await rowLoc.hover();
    await page.waitForTimeout(400);
    const hovered = await page.evaluate(() => {
      const panel = [...document.querySelectorAll('[role="dialog"]')].pop() as HTMLElement;
      const h4 = [...panel.querySelectorAll("h4")].find(
        (h) => (h.textContent || "").trim() === "Contents Insurance",
      );
      let row: HTMLElement = h4 as HTMLElement;
      while (row && row !== panel) {
        const cs = getComputedStyle(row);
        if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === "rgb(255, 255, 255)" && cs.padding === "16px") break;
        row = row.parentElement!;
      }
      const actions = [...row.querySelectorAll("div")].find(
        (d) =>
          getComputedStyle(d).display === "flex" &&
          getComputedStyle(d).transitionProperty.includes("opacity") &&
          d.querySelectorAll("button").length >= 1,
      );
      return {
        boxShadow: getComputedStyle(row).boxShadow,
        actionOpacity: actions ? getComputedStyle(actions).opacity : null,
      };
    });
    expect(hovered.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 4px 6px -1px");
    expect(hovered.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 2px 4px -2px");
    expect(hovered.actionOpacity).toBe("1");

    // --- cleanup (the fixture-restore discipline).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await dialog.getByText("Based on 0 items").waitFor();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });

  test("the calculator dialog at 640 — the panel + row width (v45 F2b)", async ({ page }) => {
    await page.setViewportSize({ width: 640, height: 960 });
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
    await page.waitForTimeout(300);

    const census = await page.evaluate(() => {
      const panel = [...document.querySelectorAll('[role="dialog"]')].pop() as HTMLElement;
      if (!panel) return null;
      const h4 = [...panel.querySelectorAll("h4")].find(
        (h) => (h.textContent || "").trim() === "Contents Insurance",
      );
      if (!h4) return null;
      let row: HTMLElement = h4 as HTMLElement;
      while (row && row !== panel) {
        const cs = getComputedStyle(row);
        if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === "rgb(255, 255, 255)" && cs.padding === "16px") break;
        row = row.parentElement!;
      }
      return {
        panelW: Math.round(panel.getBoundingClientRect().width),
        rowW: Math.round(row.getBoundingClientRect().width),
        sw: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The reference's measured 640 contract (calc-row-v45 at 640):
    // panel 608 (640 − the 2×16 overlay padding), row 560, sw 640.
    expect(census!.panelW).toBe(608);
    expect(census!.rowW).toBe(560);
    expect(census!.sw).toBe(640);

    // --- cleanup.
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await dialog.getByText("Based on 0 items").waitFor();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });
});

test.describe("calculator panel chrome census at 640 (v49 — plan F3)", () => {
  test("the panel's full chrome at 640 — the read-only open state (v49 F3)", async ({ page }) => {
    await page.setViewportSize({ width: 640, height: 960 });
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(400);

    // The reference's measured 640 contract (ref-v49.sh — the read-only
    // open flow: hover → Calculate → census → X close): the panel w 608
    // (640 − the 2×16 overlay padding) at x 16, radius 16, maxW 768px
    // (max-w-3xl), maxH 816px (85vh of the 960 viewport), bg white,
    // overflow hidden, the 2xl VISIBLE shadow layer, the 36×36 close, the
    // header's border-b 1px solid rgb(229,231,227). The panel height is
    // data-dependent (the e2e seed's Rent has no line items) — the pin
    // asserts the CENTERING invariant, never the absolute height.
    const census = await page.evaluate(() => {
      const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
        (d.textContent || "").includes("Rent Calculator"),
      ) as HTMLElement | null;
      if (!panel) return null;
      const cs = getComputedStyle(panel);
      const r = panel.getBoundingClientRect();
      const closeBtn = [...panel.querySelectorAll("button")].find(
        (b) => (b.getAttribute("aria-label") || "") === "Close" || !(b.textContent || "").trim(),
      ) as HTMLElement | undefined;
      const hdr = [...panel.querySelectorAll("div")].find(
        (d) => getComputedStyle(d).borderBottomWidth !== "0px",
      ) as HTMLElement | undefined;
      return {
        panel: {
          w: Math.round(r.width),
          x: Math.round(r.x),
          y: Math.round(r.y),
          h: Math.round(r.height),
          radius: cs.borderRadius,
          maxW: cs.maxWidth,
          maxH: cs.maxHeight,
          bg: cs.backgroundColor,
          overflow: cs.overflow,
          shadow: cs.boxShadow,
        },
        closeBtn: closeBtn
          ? {
              w: Math.round(closeBtn.getBoundingClientRect().width),
              h: Math.round(closeBtn.getBoundingClientRect().height),
            }
          : null,
        hdrBorder: hdr ? getComputedStyle(hdr).borderBottom : null,
        sw: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    expect(census!.panel.w).toBe(608);
    expect(census!.panel.x).toBe(16);
    expect(census!.panel.radius).toBe("16px");
    expect(census!.panel.maxW).toBe("768px");
    expect(census!.panel.maxH).toBe("816px");
    expect(census!.panel.bg).toBe("rgb(255, 255, 255)");
    expect(census!.panel.overflow).toBe("hidden");
    // The 2xl VISIBLE layer (the reference's 2 transparent leads are the
    // accepted lead-divergence class — v10/v25/v45; the clone's
    // .zb-modal-panel emits the visible layer directly).
    expect(census!.panel.shadow).toContain("rgba(0, 0, 0, 0.25) 0px 25px 50px -12px");
    // The centering invariant (both sites center the panel in the
    // viewport — the y tracks the data-dependent height).
    expect(census!.panel.y).toBe(Math.round((960 - census!.panel.h) / 2));
    expect(census!.closeBtn).toEqual({ w: 36, h: 36 });
    expect(census!.hdrBorder).toBe("1px solid rgb(229, 231, 227)");
    expect(census!.sw).toBe(640);

    // Read-only close — no fixture restore needed (the Rent amount is
    // never recalculated; no line items touched).
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
  });
});

// ---------------------------------------------------------------------------
// v53 — plan F2 (docs/remediation-plan-v53.md): the calculator dialog's
// MOBILE census at 390 (the session-124 queue's calculator dialog 390
// reflow). The v45 F2b + v49 F3 pins walked this family at 640 only (the
// panel 608 / the row 560). The v53 pin locks the mobile chrome measured
// live on the reference at 390x844 (ref-v53.sh + clone-v53b.sh — the
// with-row state, byte-identical on every axis):
//   the panel: w 358 (390 − the 2×16 overlay pad) / radius 16 / maxW
//             768 / maxH 717.4 (the 85vh cap) / white / overflow hidden
//             / flex + the 2xl VISIBLE layer
//   the header: h 101 / pad 16px 24px / border-b — the flex row at 390
//             SQUISHES the chip to 32x40 and the close to 29x36 on BOTH
//             sites (the identical flex-shrink behavior)
//   the total card: 310 wide (358 − the 2×24 p-6) / #fff7f5 / radius 12
//             / pad 16
//   the row: 310 / pad 16 / white / border-t / radius 12
//   the Add Item button: 110x32 / 12px/500 / the orange gradient / white
//   docSW 390 (the overlay constrains the page on both sites)
// The panel h (413 with 1 row on BOTH sites) is data-dependent — never
// pinned; the CENTERING invariant (y = round((844 − h) / 2)) instead.
// ---------------------------------------------------------------------------
test.describe("calculator dialog mobile census (v53 — plan F2)", () => {
  test("the calculator's full chrome at 390 matches the reference (byte-parity)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Contents Insurance")).toBeVisible();
    await page.waitForTimeout(300);

    const census = await page.evaluate(() => {
      const panels = [...document.querySelectorAll('[role="dialog"]')];
      const panel = panels
        .filter((p) => (p.textContent || "").includes("Total Calculated"))
        .pop() as HTMLElement | undefined;
      if (!panel) return null;
      const hdr = [...panel.querySelectorAll("div")].find(
        (d) => getComputedStyle(d).borderBottomWidth !== "0px",
      );
      const h2 = panel.querySelector("h2");
      const closeBtn = [...panel.querySelectorAll("button")].filter(
        (b) => !b.textContent.trim(),
      )[0] as HTMLElement | undefined;
      const chip = panel.querySelector("div.rounded-xl, [class*=rounded-xl]") as HTMLElement | null;
      const total = [...panel.querySelectorAll("div")].find(
        (d) =>
          (d.textContent || "").includes("Total Calculated") &&
          getComputedStyle(d).backgroundColor !== "rgba(0, 0, 0, 0)" &&
          d !== panel,
      ) as HTMLElement | undefined;
      const h4 = [...panel.querySelectorAll("h4")].find(
        (h) => (h.textContent || "").trim() === "Contents Insurance",
      );
      let row: HTMLElement | null = h4 ? (h4 as HTMLElement) : null;
      while (row && row !== panel) {
        const rcs = getComputedStyle(row);
        if (
          parseFloat(rcs.borderTopWidth) > 0 &&
          rcs.backgroundColor === "rgb(255, 255, 255)" &&
          rcs.padding === "16px"
        )
          break;
        row = row.parentElement;
      }
      const addBtn = [...panel.querySelectorAll("button")].find((b) =>
        /^Add Item$/.test((b.textContent || "").trim()),
      ) as HTMLElement | undefined;
      const pr = panel.getBoundingClientRect();
      const pcs = getComputedStyle(panel);
      return {
        panel: {
          w: Math.round(pr.width),
          x: Math.round(pr.x),
          y: Math.round(pr.y),
          h: Math.round(pr.height),
          radius: pcs.borderRadius,
          maxW: pcs.maxWidth,
          maxH: pcs.maxHeight,
          bg: pcs.backgroundColor,
          overflow: pcs.overflow,
          display: pcs.display,
          shadow: pcs.boxShadow,
        },
        header: hdr
          ? {
              h: Math.round(hdr.getBoundingClientRect().height),
              pad: getComputedStyle(hdr).padding,
              borderB: getComputedStyle(hdr).borderBottom,
            }
          : null,
        h2: h2
          ? {
              fs: getComputedStyle(h2).fontSize,
              fw: getComputedStyle(h2).fontWeight,
              color: getComputedStyle(h2).color,
            }
          : null,
        chip: chip
          ? {
              w: Math.round(chip.getBoundingClientRect().width),
              h: Math.round(chip.getBoundingClientRect().height),
              radius: getComputedStyle(chip).borderRadius,
              bg: getComputedStyle(chip).backgroundImage,
            }
          : null,
        close: closeBtn
          ? {
              w: Math.round(closeBtn.getBoundingClientRect().width),
              h: Math.round(closeBtn.getBoundingClientRect().height),
            }
          : null,
        totalCard: total
          ? {
              w: Math.round(total.getBoundingClientRect().width),
              bg: getComputedStyle(total).backgroundColor,
              radius: getComputedStyle(total).borderRadius,
              pad: getComputedStyle(total).padding,
            }
          : null,
        row:
          row && row !== panel
            ? {
                w: Math.round(row.getBoundingClientRect().width),
                pad: getComputedStyle(row).padding,
                bg: getComputedStyle(row).backgroundColor,
                borderT: getComputedStyle(row).borderTop,
                radius: getComputedStyle(row).borderRadius,
              }
            : null,
        addBtn: addBtn
          ? {
              w: Math.round(addBtn.getBoundingClientRect().width),
              h: Math.round(addBtn.getBoundingClientRect().height),
              fs: getComputedStyle(addBtn).fontSize,
              fw: getComputedStyle(addBtn).fontWeight,
              bg: getComputedStyle(addBtn).backgroundImage,
              color: getComputedStyle(addBtn).color,
            }
          : null,
        sw: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The panel: the 390 − 2×16 overlay-pad arithmetic, the 85vh cap.
    expect(census!.panel!.w).toBe(358);
    expect(census!.panel!.x).toBe(16);
    expect(census!.panel!.radius).toBe("16px");
    expect(census!.panel!.maxW).toBe("768px");
    expect(census!.panel!.maxH).toBe("717.4px");
    expect(census!.panel!.bg).toBe("rgb(255, 255, 255)");
    expect(census!.panel!.overflow).toBe("hidden");
    expect(census!.panel!.display).toBe("flex");
    // The 2xl VISIBLE layer (the accepted lead-divergence class).
    expect(census!.panel!.shadow).toContain("rgba(0, 0, 0, 0.25) 0px 25px 50px -12px");
    // The CENTERING invariant (both sites center the panel; the h itself
    // is data-dependent — never pinned).
    expect(census!.panel!.y).toBe(Math.round((844 - census!.panel!.h) / 2));
    // The header: the flex row squishes the chip + the close identically
    // on both sites.
    expect(census!.header!.h).toBe(101);
    expect(census!.header!.pad).toBe("16px 24px");
    expect(census!.header!.borderB).toBe("1px solid rgb(229, 231, 227)");
    expect(census!.h2).toEqual({ fs: "18px", fw: "700", color: "rgb(26, 58, 46)" });
    expect(census!.chip).toEqual({
      w: 32,
      h: 40,
      radius: "12px",
      bg: "linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))",
    });
    expect(census!.close).toEqual({ w: 29, h: 36 });
    // The total card: the 358 − 2×24 arithmetic, the orange tint.
    expect(census!.totalCard).toEqual({
      w: 310,
      bg: "rgb(255, 247, 245)",
      radius: "12px",
      pad: "16px",
    });
    // The line-item row family.
    expect(census!.row).toEqual({
      w: 310,
      pad: "16px",
      bg: "rgb(255, 255, 255)",
      borderT: "1px solid rgb(229, 231, 227)",
      radius: "12px",
    });
    // The Add Item button.
    expect(census!.addBtn!.w).toBe(110);
    expect(census!.addBtn!.h).toBe(32);
    expect(census!.addBtn!.fs).toBe("12px");
    expect(census!.addBtn!.fw).toBe("500");
    expect(census!.addBtn!.bg).toContain("linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))");
    expect(census!.addBtn!.color).toBe("rgb(255, 255, 255)");
    // The overlay constrains the page on both sites.
    expect(census!.sw).toBe(390);

    // --- cleanup (the v45 F2b discipline): delete the row AND restore the
    // Rent amount — the line-item mutations recalculate the parent's amount
    // server-side (the calculator rule), so the add/delete cycle leaves
    // Rent recalculated; restoreRent re-edits it to $1,850 so every later
    // spec's dashboard arithmetic (+$2065.00) holds.
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(dialog.getByText("Contents Insurance")).toBeHidden();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });
});

// ---------------------------------------------------------------------------
// v59 — plan F1 (docs/remediation-plan-v59.md): the calculator panel's
// desktop census at 1280x800 (the session-139 v59 queue's first item —
// the panel + row surfaces). The v45 F2a pin walked the panelW + the ROW
// census at 1280; the v49 F3 pin walked the panel's full chrome at 640
// only; the total card is pinned at 390 only (v53 F2). The v59 pin locks
// the panel chrome + the total card at the PAIR viewport.
//
// Measured live on BOTH sites (calc-census-ref-v59.sh +
// calc-census-clone-v59.sh — the with-row state, byte-identical on every
// axis; the VLM pair vlm-shots-v59.sh + clone-vlmshots-v59.sh +
// vlm-compare-v59.mjs CLEAN per the v43 rule — both flags DOM-arbitrated:
// the "Will update category total" span is DATA-CONDITIONAL [lineTotal
// vs parentAmount at open — the pinned contract], the row action pair is
// a POINTER-POSITION artifact [both sites gate it at opacity 0 at rest]):
//   the panel: w 768 / radius 16px / maxW 768px (48rem) / maxH 680px
//             (the 85vh cap of the 800 viewport — the v49 F3's 816px was
//             the 960 viewport's) / bg white / overflow hidden / the 2xl
//             VISIBLE shadow layer (the reference's 2 transparent leads
//             are the accepted lead-divergence class — v10/v25/v45)
//   the centering invariant: y = round((800 − h) / 2) — the height is
//             data-dependent (the e2e seed's Rent has no line items),
//             never pinned
//   the close: 36×36 (the v49 F3 value)
//   the header: border-b 1px solid rgb(229,231,227) (the v49 F3 value)
//   the total card: 720 wide (768 − the 2×24 p-6) / #fff7f5 / radius 12
//             / pad 16px / border 1px solid rgb(252,221,213) — the v53
//             F2's own chrome at the 1280 viewport (the width is the
//             panel constant minus p-6, data-independent)
// The read-only open state — no line items, no recalcs, no fixture
// restore needed (the v49 F3 pattern).
// ---------------------------------------------------------------------------
test.describe("calculator panel census at 1280 (v59 — plan F1)", () => {
  test("the panel + total-card chrome at the pair viewport (read-only open state)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate(() => {
      const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
        (d.textContent || "").includes("Rent Calculator"),
      ) as HTMLElement | null;
      if (!panel) return null;
      const cs = getComputedStyle(panel);
      const r = panel.getBoundingClientRect();
      const totalCard = [...panel.querySelectorAll("div")].find(
        (d) => getComputedStyle(d).backgroundColor === "rgb(255, 247, 245)",
      );
      const tcs = totalCard ? getComputedStyle(totalCard) : null;
      const tr = totalCard ? totalCard.getBoundingClientRect() : null;
      const closeBtn = [...panel.querySelectorAll("button")].find(
        (b) => (b.getAttribute("aria-label") || "") === "Close",
      );
      const hdr = [...panel.querySelectorAll("div")].find(
        (d) => getComputedStyle(d).borderBottomWidth !== "0px",
      );
      return {
        panel: {
          w: Math.round(r.width),
          h: Math.round(r.height),
          y: Math.round(r.y),
          radius: cs.borderRadius,
          maxW: cs.maxWidth,
          maxH: cs.maxHeight,
          bg: cs.backgroundColor,
          overflow: cs.overflow,
          shadow: cs.boxShadow,
        },
        totalCard: tcs
          ? {
              w: Math.round(tr!.width),
              bg: tcs.backgroundColor,
              radius: tcs.borderRadius,
              pad: tcs.padding,
              border: tcs.border,
            }
          : null,
        closeBtn: closeBtn
          ? {
              w: Math.round(closeBtn.getBoundingClientRect().width),
              h: Math.round(closeBtn.getBoundingClientRect().height),
            }
          : null,
        hdrBorder: hdr ? getComputedStyle(hdr).borderBottom : null,
      };
    });
    expect(census).not.toBeNull();
    // The panel: the 1280 contract (the pair viewport).
    expect(census!.panel.w).toBe(768);
    expect(census!.panel.radius).toBe("16px");
    expect(census!.panel.maxW).toBe("768px");
    // The 85vh cap of the 800 viewport (680 = 0.85 × 800).
    expect(census!.panel.maxH).toBe("680px");
    expect(census!.panel.bg).toBe("rgb(255, 255, 255)");
    expect(census!.panel.overflow).toBe("hidden");
    // The 2xl VISIBLE layer (the reference's transparent leads are the
    // accepted lead-divergence class; the clone's .zb-modal-panel emits
    // the visible layer directly).
    expect(census!.panel.shadow).toContain("rgba(0, 0, 0, 0.25) 0px 25px 50px -12px");
    // The centering invariant (the height is data-dependent — the e2e
    // seed's Rent carries NO line items, so this is the EMPTY state).
    expect(census!.panel.y).toBe(Math.round((800 - census!.panel.h) / 2));
    // The close + the header (the v49 F3 values, re-measured at 1280).
    expect(census!.closeBtn).toEqual({ w: 36, h: 36 });
    expect(census!.hdrBorder).toBe("1px solid rgb(229, 231, 227)");
    // The total card: the v53 F2 chrome at the 1280 viewport.
    expect(census!.totalCard).toEqual({
      w: 720,
      bg: "rgb(255, 247, 245)",
      radius: "12px",
      pad: "16px",
      border: "1px solid rgb(252, 221, 213)",
    });

    // Read-only close — no fixture restore needed (the Rent amount is
    // never recalculated; no line items touched).
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
  });
});

// ---------------------------------------------------------------------------
// v66 — the calculator dialog's HEIGHT-family census (plan F3,
// docs/remediation-plan-v66.md).
//
// The v66 arbitration (arbit-v66.sh + arbit-v66b.sh, the fresh v59-era
// pair re-run) measured a never-pinned family: the computed HEIGHTS of
// the dialog's interior. The v45 F2a pin covers the row's width/pad/
// radius/border + the hover reveal; the v53 pin the 390 reflow; the v59
// pin the panel + the totalCard's w/bg/radius/pad/border — the HEIGHTS
// were never measured before v66. Measured BYTE-IDENTICAL on both sites
// (the reference's own Rent calculator, one "Contents Insurance" $25
// monthly-active row): the row 720×102 (the deterministic arithmetic:
// the 32px top actions row + the h4's 4px mb + the 28px amount block +
// the 32px p-4 padding + the 2px border), the name h4 block (16px/600/
// forestDark/h 24/mb 4px), the badge pill row (flex/gap 8/12px/h 20),
// the first pill (h 20/w 65/pad 2px 8px/radius 9999px/12px/400), the
// amount P (20px/700/orangeDark/h 28), and the totalCard 720×90 (the
// v59-pinned chrome's own height axis: the 32px total row + the 8px
// mb-2 + the 16px caption row + the 32px p-4 padding + the 2px border).
// The height family needs a live row — the e2e seed's Rent carries
// none — so the pin rides the v45 F2a add-then-restoreRent fixture.
test.describe("calculator dialog height-family census at 1280 (v66 — plan F3)", () => {
  test("the row + name-block + pill-row + amount + total-card HEIGHTS (the never-pinned family)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
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
    await page.waitForTimeout(300);

    const census = await page.evaluate(() => {
      // The finders modeled on the v66 arbitration's own census
      // (arbit-v66.sh / arbit-v66b.sh).
      const panel = [...document.querySelectorAll('[role="dialog"]')].find(
        (d) => (d.textContent || "").includes("Rent Calculator"),
      ) as HTMLElement | null;
      if (!panel) return null;
      const totalCard = [...panel.querySelectorAll("div")].find(
        (d) => getComputedStyle(d).backgroundColor === "rgb(255, 247, 245)",
      );
      const h4 = [...panel.querySelectorAll("h4")].find(
        (h) => (h.textContent || "").trim() === "Contents Insurance",
      );
      if (!h4 || !totalCard) return null;
      let row: HTMLElement = h4 as HTMLElement;
      while (row && row !== panel) {
        const cs = getComputedStyle(row);
        if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === "rgb(255, 255, 255)") break;
        row = row.parentElement!;
      }
      if (!row || row === panel) return null;
      const pills = [...row.querySelectorAll("span")].filter(
        (s) => parseFloat(getComputedStyle(s).borderRadius) > 100 && s.getBoundingClientRect().width > 10,
      );
      const pillRow = pills.length ? (pills[0].parentElement as HTMLElement) : null;
      const p1 = pills[0] ? getComputedStyle(pills[0]) : null;
      const p1R = pills[0] ? pills[0].getBoundingClientRect() : null;
      const amountP = [...row.querySelectorAll("p,span,div")]
        .filter((e) => e.children.length === 0 && (e.textContent || "").trim().startsWith("$"))
        .sort((a, b) => parseFloat(getComputedStyle(b).fontSize) - parseFloat(getComputedStyle(a).fontSize))[0];
      const h4cs = getComputedStyle(h4);
      const prcs = pillRow ? getComputedStyle(pillRow) : null;
      const apcs = amountP ? getComputedStyle(amountP) : null;
      return {
        row: {
          w: Math.round(row.getBoundingClientRect().width),
          h: Math.round(row.getBoundingClientRect().height),
        },
        nameH4: {
          fs: h4cs.fontSize,
          fw: h4cs.fontWeight,
          color: h4cs.color,
          h: Math.round(h4.getBoundingClientRect().height),
          mb: h4cs.marginBottom,
        },
        pillRow: prcs
          ? {
              display: prcs.display,
              gap: prcs.gap,
              fs: prcs.fontSize,
              h: Math.round(pillRow!.getBoundingClientRect().height),
            }
          : null,
        pill1: p1
          ? {
              h: Math.round(p1R!.height),
              w: Math.round(p1R!.width),
              pad: p1.padding,
              radius: p1.borderRadius,
              fs: p1.fontSize,
              fw: p1.fontWeight,
            }
          : null,
        amountP: apcs
          ? {
              fs: apcs.fontSize,
              fw: apcs.fontWeight,
              color: apcs.color,
              h: Math.round(amountP!.getBoundingClientRect().height),
            }
          : null,
        totalCard: {
          w: Math.round(totalCard.getBoundingClientRect().width),
          h: Math.round(totalCard.getBoundingClientRect().height),
        },
      };
    });
    expect(census).not.toBeNull();
    // The row: 720×102 — the deterministic arithmetic (the 32px actions
    // row + the 4px h4 mb + the 28px amount block + the 32px p-4 + the
    // 2px border), byte-identical to the reference's own row.
    expect(census!.row).toEqual({ w: 720, h: 102 });
    // The name h4 block.
    expect(census!.nameH4).toEqual({
      fs: "16px",
      fw: "600",
      color: "rgb(26, 58, 46)",
      h: 24,
      mb: "4px",
    });
    // The badge pill row + its first pill (the "monthly" default).
    expect(census!.pillRow).toEqual({ display: "flex", gap: "8px", fs: "12px", h: 20 });
    expect(census!.pill1).toEqual({
      h: 20,
      w: 65,
      pad: "2px 8px",
      radius: "9999px",
      fs: "12px",
      fw: "400",
    });
    // The amount P (the row's own text-xl orange figure).
    expect(census!.amountP).toEqual({
      fs: "20px",
      fw: "700",
      color: "rgb(224, 122, 59)",
      h: 28,
    });
    // The total card: 720×90 — the v59-pinned chrome's height axis.
    expect(census!.totalCard).toEqual({ w: 720, h: 90 });

    // --- cleanup (the fixture-restore discipline).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await dialog.getByText("Based on 0 items").waitFor();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });
});

// ---------------------------------------------------------------------------
// v73 — plan F4 (docs/remediation-plan-v73.md): the calculator's SCRIM +
// SUMMARY-TEXT chrome census at 390x844 — the never-pinned axes. The v53
// F2 pin locked the panel/header/chip/close/totalCard/row/addBtn GEOMETRY
// at 390; the v66 F3 pin locked the height-family at 1280 — the scrim and
// the text chrome were never pinned (the details-sheet overlay is pinned
// in item-details.spec.ts; the calculator's own scrim never was).
//
// Measured live on BOTH sites (arbit-v73.sh — the with-row state,
// byte-identical on every axis; the VLM pair vlm-shots-v73.sh +
// clone-vlmshots-v73.sh + vlm-compare-v73.mjs — the login mobile twin
// IDENTICAL, the calculator mobile twin CLEAN per the v43 rule — both
// flags DOM-arbitrated: the "scrim lighter" claim a PERCEPTION ARTIFACT
// [the scrim bg rgba(26,58,46,0.5) / opacity 1 / blur(8px) / 390x844
// byte-identical; the reference's wrapper-scrim carries the text, the
// clone's Radix scrim is a textless sibling — the v72 structural class],
// the "Will update category total" span the v66 DATA-CONDITIONAL class
// [the reference's Rent natively 25.00 === its line-item total 25.00 ->
// hidden; the clone's opened-at 1850 vs the recalculated 25.00 -> shown]):
//   the scrim: bg rgba(26, 58, 46, 0.5) / computed opacity 1 /
//             backdrop-filter blur(8px) / w 390 / h 844 (the full-viewport
//             fixed overlay — the clone's .zb-modal-overlay sibling)
//   the summary amount: 24px / 700 / lh 32px / rgb(224, 122, 59)
//   the "Based on 1 item" line: 12px / rgb(107, 114, 128)
//   the description: 14px / lh 20px / rgb(107, 114, 128)
//   the "• Will update category total" span (with the 1-row fixture):
//             12px / 400 / rgb(234, 88, 12)
// The fixture rides the v53 F2 discipline (hover → Calculate → Add Line
// Item → census → Delete → restoreRent).
// ---------------------------------------------------------------------------
test.describe("calculator scrim + summary-text census at 390 (v73 — plan F4)", () => {
  test("the scrim + the summary text chrome — the never-pinned axes (byte-parity)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Contents Insurance")).toBeVisible();
    await page.waitForTimeout(300);

    const census = await page.evaluate(() => {
      // The scrim: the fixed full-viewport overlay (the clone's Radix
      // sibling — textless, non-transparent bg, z>=50). Modeled on the
      // v73 arbitration's own census (arbit-v73.sh).
      const scrim = [...document.querySelectorAll("div")]
        .filter((d) => {
          const s = getComputedStyle(d);
          const r = d.getBoundingClientRect();
          return (
            s.position === "fixed" &&
            parseInt(s.zIndex || "0") >= 50 &&
            r.width >= 380 &&
            r.height >= 800 &&
            s.backgroundColor &&
            s.backgroundColor !== "rgba(0, 0, 0, 0)"
          );
        })
        .pop() as HTMLElement | undefined;
      // The panel: the calculator dialog itself.
      const panel = [...document.querySelectorAll('[role="dialog"]')]
        .filter((p) => (p.textContent || "").includes("Total Calculated"))
        .pop() as HTMLElement | undefined;
      if (!panel || !scrim) return null;
      // The total card (the #fff7f5 block) — the summary amount + the
      // based-on line live inside it.
      const totalCard = [...panel.querySelectorAll("div")].find(
        (d) => getComputedStyle(d).backgroundColor === "rgb(255, 247, 245)",
      ) as HTMLElement | undefined;
      if (!totalCard) return null;
      const leaf = (scope: HTMLElement, test: (t: string) => boolean) =>
        [...scope.querySelectorAll("*")].find(
          (e) => e.children.length === 0 && test((e.textContent || "").trim()),
        ) as HTMLElement | undefined;
      const amountEl = leaf(totalCard, (t) => /^\$25\.00$/.test(t));
      const basedOnEl = leaf(totalCard, (t) => /^Based on 1 item$/.test(t));
      const willUpdateEl = leaf(totalCard, (t) => /Will update category total/.test(t));
      const descEl = leaf(panel, (t) => /Break down your rent/i.test(t));
      const ss = getComputedStyle(scrim);
      const sr = scrim.getBoundingClientRect();
      const cs = (el?: HTMLElement) => (el ? getComputedStyle(el) : null);
      return {
        scrim: {
          bg: ss.backgroundColor,
          opacity: ss.opacity,
          blur: ss.backdropFilter,
          w: Math.round(sr.width),
          h: Math.round(sr.height),
        },
        amount: (() => {
          const c = cs(amountEl);
          return c ? { fs: c.fontSize, fw: c.fontWeight, lh: c.lineHeight, color: c.color } : null;
        })(),
        basedOn: (() => {
          const c = cs(basedOnEl);
          return c ? { fs: c.fontSize, color: c.color } : null;
        })(),
        willUpdate: (() => {
          const c = cs(willUpdateEl);
          return c ? { fs: c.fontSize, fw: c.fontWeight, color: c.color } : null;
        })(),
        desc: (() => {
          const c = cs(descEl);
          return c ? { fs: c.fontSize, lh: c.lineHeight, color: c.color } : null;
        })(),
      };
    });
    expect(census).not.toBeNull();
    // The scrim: the forest tint + the blur + the full-viewport geometry —
    // byte-identical to the reference's wrapper-scrim (the v73 arbitration).
    expect(census!.scrim).toEqual({
      bg: "rgba(26, 58, 46, 0.5)",
      opacity: "1",
      blur: "blur(8px)",
      w: 390,
      h: 844,
    });
    // The summary amount: the 24px/700 orange figure.
    expect(census!.amount).toEqual({
      fs: "24px",
      fw: "700",
      lh: "32px",
      color: "rgb(224, 122, 59)",
    });
    // The "Based on 1 item" line: the 12px gray caption.
    expect(census!.basedOn).toEqual({ fs: "12px", color: "rgb(107, 114, 128)" });
    // The conditional span: the 12px/400 orange-600 hint (present with
    // the fixture — the opened-at 1850 vs the recalculated 25.00).
    expect(census!.willUpdate).toEqual({
      fs: "12px",
      fw: "400",
      color: "rgb(234, 88, 12)",
    });
    // The description line: the 14px/20px gray subtitle.
    expect(census!.desc).toEqual({
      fs: "14px",
      lh: "20px",
      color: "rgb(107, 114, 128)",
    });

    // --- cleanup (the v53 F2b discipline): delete the row AND restore the
    // Rent amount (the line-item mutations recalculate the parent's amount
    // server-side — the calculator rule).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(dialog.getByText("Contents Insurance")).toBeHidden();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });
});

// ---------------------------------------------------------------------------
// v81 — plan F4 (docs/remediation-plan-v81.md): the calculator dialog's
// HEADER family + Add Item button + SCRIM chrome census at 1280x800 — the
// never-pinned axes. The v53 F2 pin holds the panel/header/chip/close/
// totalCard/row/addBtn GEOMETRY at 390; the v59 F1 pin the panel +
// totalCard chrome + closeBtn/hdrBorder at 1280; the v66 F3 pin the
// row-height FAMILY at 1280 (the panel body); the v73 F4 pin the scrim +
// summary-text at 390 — the title/desc TYPOGRAPHY, the addBtn CHROME, and
// the SCRIM were never pinned at the pair viewport.
//
// Measured live on BOTH sites (arbit-v81.sh — the v59-era pair's third
// re-run, byte-identical on every axis; the VLM pair vlm-shots-v81.sh +
// clone-vlmshots-v81.sh + vlm-compare-v81.mjs — the login twin IDENTICAL
// with zero style flags, the calculator twin's three flags all
// DOM-arbitrated to documented classes: the will-update span the v66
// DATA-CONDITIONAL class, the "hover buttons missing" the POINTER-POSITION
// perception class [actionsAtRest opacity 0 / btnCount 2 on BOTH sides],
// the "row height shorter" a VLM MISREAD [the row 720×102 byte-identical]):
//   the title (DialogTitle): 18px / 700 / lh 28px / rgb(26, 58, 46)
//   the desc (DialogDescription): 14px / lh 20px / rgb(107, 114, 128)
//   the Add Item button: 110×32 / radius 6px / 12px / 500 / white
//   the scrim: bg rgba(26, 58, 46, 0.5) / blur(8px) / 1280×800
// Every pinned axis is STATIC dialog chrome (none depends on the
// line-item data) — the pin rides the v59 read-only EMPTY-state
// discipline (hover → Calculate → census → Close, no fixture writes).
// ---------------------------------------------------------------------------
test.describe("calculator header + addBtn + scrim census at 1280 (v81 — plan F4)", () => {
  test("the title/desc typography + the addBtn chrome + the scrim — the never-pinned axes", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate(() => {
      // The panel: the calculator dialog itself (the v59 finder).
      const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
        (d.textContent || "").includes("Rent Calculator"),
      ) as HTMLElement | undefined;
      if (!panel) return null;
      // The scrim: the fixed full-viewport overlay (the clone's Radix
      // sibling — the v73 finder widened for the 1280 viewport).
      const scrim = [...document.querySelectorAll("div")]
        .filter((d) => {
          const s = getComputedStyle(d);
          const r = d.getBoundingClientRect();
          return (
            s.position === "fixed" &&
            parseInt(s.zIndex || "0") >= 50 &&
            r.width >= 1200 &&
            r.height >= 700 &&
            s.backgroundColor &&
            s.backgroundColor !== "rgba(0, 0, 0, 0)"
          );
        })
        .pop() as HTMLElement | undefined;
      // The title: the leaf whose text is exactly the category-adaptive
      // heading (the h2 DialogTitle).
      const title = [...panel.querySelectorAll("h2, h3, h1, div, span")].find(
        (e) => (e.textContent || "").trim() === "Rent Calculator" && e.children.length === 0,
      ) as HTMLElement | undefined;
      // The desc: the leaf matching the category-adaptive subtitle.
      const desc = [...panel.querySelectorAll("p, div, span")].find(
        (e) => /Break down your rent into individual items/i.test((e.textContent || "").trim()) && e.children.length === 0,
      ) as HTMLElement | undefined;
      // The Add Item button (the orange-gradient CTA).
      const addBtn = [...panel.querySelectorAll("button")].find((b) =>
        /^add item$/i.test((b.textContent || "").trim()),
      ) as HTMLButtonElement | undefined;
      const tcs = title ? getComputedStyle(title) : null;
      const dcs = desc ? getComputedStyle(desc) : null;
      const acs = addBtn ? getComputedStyle(addBtn) : null;
      const ar = addBtn ? addBtn.getBoundingClientRect() : null;
      const ss = scrim ? getComputedStyle(scrim) : null;
      const sr = scrim ? scrim.getBoundingClientRect() : null;
      return {
        title: tcs
          ? { fs: tcs.fontSize, fw: tcs.fontWeight, lh: tcs.lineHeight, color: tcs.color }
          : null,
        desc: dcs
          ? { fs: dcs.fontSize, lh: dcs.lineHeight, color: dcs.color }
          : null,
        addBtn: acs && ar
          ? {
              w: Math.round(ar.width),
              h: Math.round(ar.height),
              radius: acs.borderRadius,
              fs: acs.fontSize,
              fw: acs.fontWeight,
              color: acs.color,
            }
          : null,
        scrim: ss && sr
          ? {
              bg: ss.backgroundColor,
              blur: ss.backdropFilter,
              w: Math.round(sr.width),
              h: Math.round(sr.height),
            }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The title's typography family (text-lg font-bold + the inline
    // forestDark): the v53 390 pin's {fs, fw, color} twin with the
    // NEVER-pinned lh axis, at the pair viewport.
    expect(census!.title).toEqual({
      fs: "18px",
      fw: "700",
      lh: "28px",
      color: "rgb(26, 58, 46)",
    });
    // The desc's typography family (text-sm + the inline gray): the
    // v73 390 family's desktop twin.
    expect(census!.desc).toEqual({
      fs: "14px",
      lh: "20px",
      color: "rgb(107, 114, 128)",
    });
    // The Add Item button's chrome (zb-btn-add zb-btn-add-sm): the
    // v53 390 family's desktop twin — the radius never pinned before.
    expect(census!.addBtn).toEqual({
      w: 110,
      h: 32,
      radius: "6px",
      fs: "12px",
      fw: "500",
      color: "rgb(255, 255, 255)",
    });
    // The scrim (the .zb-modal-overlay forest overlay): the v73 390
    // family's desktop twin — the full-viewport fixed overlay.
    expect(census!.scrim).toEqual({
      bg: "rgba(26, 58, 46, 0.5)",
      blur: "blur(8px)",
      w: 1280,
      h: 800,
    });
    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);

    // Read-only close — no fixture restore needed (the empty state;
    // no line items touched, the Rent amount never recalculated).
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
  });
});

// ---------------------------------------------------------------------------
// v87 — plan F4 (docs/remediation-plan-v87.md): the calculator dialog's
// CLOSE-BUTTON chrome census at 1280.
//
// The v87 arbitration (arbit-v87.sh + pair-arbit-v87.sh + the
// close-arbit-v87.sh button-inventory probe, the v81-era pair's fourth
// re-run) measured a never-pinned family: the close button's chrome
// beyond the v59 {36, 36} geometry — the radius, the background, the
// border-width, the display. The v59 F1 pin holds the {w, h} at 1280
// only; the v49 F3 pin the {36, 36} at 640; the v53 F2 pin the {29, 36}
// at 390 — the radius/bg/border/display were never pinned at ANY
// viewport. Measured BYTE-IDENTICAL on both sites: 36×36 / radius 6px
// (rounded-md) / bg rgba(0,0,0,0) / borderTopWidth 0px / display flex.
//
// The cycle's own context: the REFERENCE's calculator close button lost
// its accessible name this cycle (aria-label and text both empty — the
// × now a bare SVG; the v81 census still found it by name) while its
// CHROME stayed byte-identical. The clone retains aria-label="Close"
// (the superset behavior — exercised by every dialog interaction in
// this file). The 0px-border computed-COLOR axis is EXCLUDED from the
// pin (the v66 computed-form INVISIBLE class — the width pinned, never
// the color).
//
// Every pinned axis STATIC chrome (the close button's classes are
// unconditional); the pin rides the v59/v81 read-only EMPTY-state
// discipline (hover → Calculate → census → Close — no fixture writes,
// the Rent amount never recalculated, no line items touched).
// ---------------------------------------------------------------------------
test.describe("calculator close-button chrome census at 1280 (v87 — plan F4)", () => {
  test("the close button's radius + bg + border-width + display — the never-pinned family", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate(() => {
      const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
        (d.textContent || "").includes("Rent Calculator"),
      ) as HTMLElement | undefined;
      if (!panel) return null;
      // The close button: the accessible-name finder (the clone's
      // aria-label="Close" — the name-independent fallback below finds
      // it by geometry + header position on either side's DOM).
      const btns = [...panel.querySelectorAll("button")];
      const close =
        btns.find((b) => (b.getAttribute("aria-label") || "") === "Close") ||
        btns.find((b) => {
          const r = b.getBoundingClientRect();
          return (
            Math.abs(r.width - 36) < 3 &&
            Math.abs(r.height - 36) < 3 &&
            r.top < panel.getBoundingClientRect().top + 80 &&
            !/^add item$/i.test((b.textContent || "").trim())
          );
        });
      if (!close) return { close: null };
      const cs = getComputedStyle(close);
      const r = close.getBoundingClientRect();
      return {
        close: {
          w: Math.round(r.width),
          h: Math.round(r.height),
          radius: cs.borderRadius,
          bg: cs.backgroundColor,
          borderTopWidth: cs.borderTopWidth,
          display: cs.display,
        },
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The close button's full chrome: the v59 geometry family's chrome
    // completion at the pair viewport (36×36 re-affirmed; the radius
    // 6px = rounded-md; the transparent bg; the 0px border width — the
    // computed COLOR the excluded INVISIBLE class; the flex display).
    expect(census!.close).toEqual({
      w: 36,
      h: 36,
      radius: "6px",
      bg: "rgba(0, 0, 0, 0)",
      borderTopWidth: "0px",
      display: "flex",
    });
    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);

    // Read-only close — no fixture restore needed (the empty state).
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
  });
});

// ---------------------------------------------------------------------------
// v93 — plan F4 (docs/remediation-plan-v93.md): the calculator dialog's
// TOTAL-CARD inner-text census at 1280x800 — the never-pinned axes.
//
// The v59 F1 pin holds the totalCard BOX chrome {720×90/pad/radius/
// border} at 1280; the v66 F3 pin the row/name/pill/amount height
// family at 1280; the v73 F4 pin the summary-text family
// {amount/basedOn/willUpdate} at 390 ONLY; the v81 pin the title/desc/
// addBtn/scrim at 1280; the v87 pin the close button's chrome at 1280;
// the v2-era G-test the amount's COLOR at the default viewport — the
// totalCard's inner-text family is never pinned at 1280 (the v73 390
// family's DESKTOP twin) and the "Total Calculated" LABEL leaf's
// chrome {fs/fw/lh/color} is never pinned at ANY viewport (only
// toBeVisible + locator filters elsewhere).
//
// Measured live on BOTH sites (totalcard-arbit-v93.sh +
// totalcard-clone-v93.sh — the v87-era pair's fifth re-run, the census
// JS byte-identical across the halves [md5 49aa5547]; the reference's
// NATIVE 1-row state read-only, the clone's added-then-fully-restored
// twin): the label 14px/500/lh 20px/rgb(107,114,128); the amount
// 24px/700/lh 32px/rgb(224,122,59); the basedOn 12px/lh 16px/
// rgb(107,114,128); the topRow flex/space-between/center/mb 8px; the
// bottomRow flex/space-between/12px/rgb(107,114,128); the totalCard
// 720×90/16px/12px/1px solid rgb(252,221,213); the docSW 1280. The
// will-update span the v66 DATA-CONDITIONAL class (absent on the
// reference — its Rent natively $25.00 === its line-item total;
// present in the pin's fixture state at 12px/400/rgb(234,88,12), the
// v73 390 pin's own values — the family viewport-independent).
//
// Every pinned axis is STATIC chrome (the label/amount/basedOn/rows'
// classes carry no responsive prefixes; the will-update span's
// EXISTENCE is the only data-conditional, its classes unconditional);
// the pin rides the 1-row fixture state (the v45/v66/v73 discipline —
// Add Item "Contents Insurance" $25 through the real UI) + the same
// cleanup (delete + close + restoreRent).
// ---------------------------------------------------------------------------
test.describe("calculator totalCard inner-text census at 1280 (v93 — plan F4)", () => {
  test("the label + amount + basedOn + willUpdate + rows — the never-pinned family at the pair viewport", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Contents Insurance")).toBeVisible();
    await page.waitForTimeout(300);

    const census = await page.evaluate(() => {
      // The finders modeled on the v93 arbitration's own census
      // (totalcard-arbit-v93.sh / totalcard-clone-v93.sh).
      const panel = [...document.querySelectorAll('[role="dialog"]')].find(
        (d) => (d.textContent || "").includes("Rent Calculator"),
      ) as HTMLElement | null;
      if (!panel) return null;
      const totalCard = [...panel.querySelectorAll("div")].find(
        (d) => getComputedStyle(d).backgroundColor === "rgb(255, 247, 245)",
      );
      if (!totalCard) return null;
      const leaf = (scope: HTMLElement, test: (t: string) => boolean) =>
        [...scope.querySelectorAll("*")].find(
          (e) => e.children.length === 0 && test((e.textContent || "").trim()),
        ) as HTMLElement | undefined;
      const labelEl = leaf(totalCard, (t) => t === "Total Calculated");
      const amountEl = leaf(totalCard, (t) => t === "$25.00");
      const basedOnEl = leaf(totalCard, (t) => /^Based on 1 item$/.test(t));
      const willUpdateEl = leaf(totalCard, (t) => /Will update category total/.test(t));
      if (!labelEl || !amountEl || !basedOnEl || !willUpdateEl) return null;
      const topRow = labelEl.parentElement as HTMLElement;
      const bottomRow = basedOnEl.parentElement as HTMLElement;
      const tcs = getComputedStyle(totalCard);
      const tr = totalCard.getBoundingClientRect();
      const s = (el: HTMLElement) => getComputedStyle(el);
      return {
        label: {
          fs: s(labelEl).fontSize,
          fw: s(labelEl).fontWeight,
          lh: s(labelEl).lineHeight,
          color: s(labelEl).color,
        },
        amount: {
          fs: s(amountEl).fontSize,
          fw: s(amountEl).fontWeight,
          lh: s(amountEl).lineHeight,
          color: s(amountEl).color,
        },
        basedOn: {
          fs: s(basedOnEl).fontSize,
          lh: s(basedOnEl).lineHeight,
          color: s(basedOnEl).color,
        },
        willUpdate: {
          fs: s(willUpdateEl).fontSize,
          fw: s(willUpdateEl).fontWeight,
          color: s(willUpdateEl).color,
        },
        topRow: {
          display: s(topRow).display,
          justify: s(topRow).justifyContent,
          align: s(topRow).alignItems,
          mb: s(topRow).marginBottom,
        },
        bottomRow: {
          display: s(bottomRow).display,
          justify: s(bottomRow).justifyContent,
          fs: s(bottomRow).fontSize,
          color: s(bottomRow).color,
        },
        totalCard: {
          w: Math.round(tr.width),
          h: Math.round(tr.height),
          pad: tcs.padding,
          radius: tcs.borderRadius,
          border: tcs.border,
        },
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The "Total Calculated" LABEL leaf's typography — never pinned at
    // ANY viewport before this pin (text-sm font-medium + the inline
    // gray token).
    expect(census!.label).toEqual({
      fs: "14px",
      fw: "500",
      lh: "20px",
      color: "rgb(107, 114, 128)",
    });
    // The summary amount: the v73 390 family's desktop twin (text-2xl
    // font-bold + the inline orangeDark token).
    expect(census!.amount).toEqual({
      fs: "24px",
      fw: "700",
      lh: "32px",
      color: "rgb(224, 122, 59)",
    });
    // The "Based on 1 item" line: the v73 family's desktop twin
    // (the text-xs gray caption).
    expect(census!.basedOn).toEqual({
      fs: "12px",
      lh: "16px",
      color: "rgb(107, 114, 128)",
    });
    // The conditional span: the v73 family's desktop twin (the
    // text-[#ea580c] hint — present with the fixture, the opened-at
    // 1850 vs the recalculated 25.00).
    expect(census!.willUpdate).toEqual({
      fs: "12px",
      fw: "400",
      color: "rgb(234, 88, 12)",
    });
    // The two summary rows' chrome — never pinned at any viewport.
    expect(census!.topRow).toEqual({
      display: "flex",
      justify: "space-between",
      align: "center",
      mb: "8px",
    });
    expect(census!.bottomRow).toEqual({
      display: "flex",
      justify: "space-between",
      fs: "12px",
      color: "rgb(107, 114, 128)",
    });
    // The totalCard box re-affirm (the v59 contract at the pin's own
    // viewport).
    expect(census!.totalCard).toEqual({
      w: 720,
      h: 90,
      pad: "16px",
      radius: "12px",
      border: "1px solid rgb(252, 221, 213)",
    });
    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);

    // --- cleanup (the v53 F2b discipline): delete the row AND restore
    // the Rent amount (the line-item mutations recalculate the parent's
    // amount server-side — the calculator rule).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(dialog.getByText("Contents Insurance")).toBeHidden();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });
});

test.describe("calculator Line-Items section-header row census at 1280 (v111 — plan F4)", () => {
  test("the section row + the 'Line Items' h3 — the never-pinned family at the pair viewport", async ({ page }) => {
    // The dialog's SECTION ROW between the v93-pinned totalCard and the
    // items: the row's flex chrome + the h3's computed typography — zero
    // "Line Items" assertions across all 24 specs before this pin (the
    // coverage map); the addBtn is CONTEXT ONLY (the v81 pin holds its
    // full chrome). Measured byte-identical on both sides by the v111
    // one-shot census (sectionrow-arbit-v111.sh) BEFORE the pin.
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();

    const census = await page.evaluate(() => {
      // The finders modeled on the v111 arbitration's own census
      // (sectionrow-arbit-v111.sh): the panel by the v45 chain, the h3
      // STRUCTURALLY (exact text, childless — never by tag alone), the
      // row by the walk-up to the nearest flex ancestor carrying the
      // Add Item button (the rendered chrome is the axis, never the
      // DOM shape — the v72 structural class).
      const panel = [...document.querySelectorAll('[role="dialog"]')].find(
        (d) => (d.textContent || "").includes("Rent Calculator"),
      ) as HTMLElement | null;
      if (!panel) return null;
      const h3 = [...panel.querySelectorAll("h1,h2,h3,h4,div,span,p")].find(
        (e) => (e.textContent || "").trim() === "Line Items" && e.children.length === 0,
      ) as HTMLElement | undefined;
      if (!h3) return null;
      let row: HTMLElement | null = h3.parentElement;
      for (let i = 0; i < 6 && row; i++) {
        const s = getComputedStyle(row);
        const hasAdd = [...row.querySelectorAll("button")].some((b) =>
          /Add Item/i.test(b.textContent || ""),
        );
        if (s.display === "flex" && hasAdd) break;
        row = row.parentElement;
      }
      if (!row) return null;
      const rcs = getComputedStyle(row);
      const rr = row.getBoundingClientRect();
      const hcs = getComputedStyle(h3);
      const hr = h3.getBoundingClientRect();
      const addBtn = [...row.querySelectorAll("button")].find((b) =>
        /Add Item/i.test(b.textContent || ""),
      );
      const ar = addBtn ? addBtn.getBoundingClientRect() : null;
      return {
        row: {
          display: rcs.display,
          align: rcs.alignItems,
          justify: rcs.justifyContent,
          mb: rcs.marginBottom,
          mt: rcs.marginTop,
          h: Math.round(rr.height),
          w: Math.round(rr.width),
          childCount: row.children.length,
        },
        sectionH3: {
          text: (h3.textContent || "").trim().slice(0, 16),
          tag: h3.tagName,
          fs: hcs.fontSize,
          fw: hcs.fontWeight,
          color: hcs.color,
          lh: hcs.lineHeight,
          h: Math.round(hr.height),
          margin: hcs.margin,
        },
        addBtnCtx: ar ? { w: Math.round(ar.width), h: Math.round(ar.height) } : null,
        junction: {
          h3CenterY: Math.round(hr.y + hr.height / 2),
          rowCenterY: Math.round(rr.y + rr.height / 2),
        },
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The section row's flex chrome — never pinned at ANY viewport
    // before this pin (the mb-4 flex items-center justify-between row;
    // the h 32 governed by the 32px addBtn, the w 720 by the panel's
    // content width).
    expect(census!.row).toEqual({
      display: "flex",
      align: "center",
      justify: "space-between",
      mb: "16px",
      mt: "0px",
      h: 32,
      w: 720,
      childCount: 2,
    });
    // The "Line Items" h3's computed typography — the family every
    // dialog census walked past (font-semibold + the inline forestDark
    // token; the margins Tailwind-preflight-reset to 0).
    expect(census!.sectionH3).toEqual({
      text: "Line Items",
      tag: "H3",
      fs: "16px",
      fw: "600",
      color: "rgb(26, 58, 46)",
      lh: "24px",
      h: 24,
      margin: "0px",
    });
    // The addBtn as CONTEXT ONLY (the v81 pin holds its full chrome);
    // re-walked to anchor the row's identity.
    expect(census!.addBtnCtx).toEqual({ w: 110, h: 32 });
    // The junction: the items-center alignment read live — the h3's
    // y-center coincides with the row's y-center (the absolute y is
    // the data-state axis, never pinned).
    expect(census!.junction.h3CenterY).toBe(census!.junction.rowCenterY);
    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);

    // Read-only pin — no fixtures to clean up; just close the dialog.
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
  });
});


// ---------------------------------------------------------------------------
// v123 — plan F4 (docs/remediation-plan-v123.md): the CALCULATOR
// line-item DELETE-CONFIRM BAR census at 1280 — the never-pinned FOURTH
// member of the confirm-bar family (the v121 pin holds the ITEM-CARD's
// bar; the net-worth twins are held BY CONSTRUCTION via the identical
// class strings net-worth-view.tsx:123/234; the CALCULATOR's bar — the
// mt-3 variant inside the row card, calculator-dialog.tsx:279 — held by
// NO spec: the behavioral tests assert the text + the click flow only,
// the v45/v66 row censuses read the row at REST, and the bar renders
// only while confirmingId === li.id). The CLONE-ONLY form (the v121 F3
// adapted precedent): the reference's calculator row delete destroys
// IMMEDIATELY (its R6 bug — superset fix #6's own citation), so no
// confirm bar exists on the reference and a reference-side measurement
// would require a DESTRUCTIVE click (the v46 read-only rule) — the pin
// locks the CLONE's own superset chrome. The family chrome = the v121
// pinned contract BY CONSTRUCTION (the identical class strings); the
// calculator-specific axis: mt-3 (12px — the family's other members
// carry mt-4 16px, the calculator's tighter rhythm inside the row).
// The one-shot census: confirmbar-arbit-v123.sh (the confirm ladder —
// the twin state seeded through the real UI, the at-rest 102, the bar
// census + the +60 bar-open delta, the Cancel path, the fixture
// restore + the seedcheck exact after).
// ---------------------------------------------------------------------------
test.describe("calculator line-item DELETE-CONFIRM BAR census at 1280 (v123 — plan F4)", () => {
  test("the confirm bar — the box, the label, the Cancel pill + the shadow-sm VISIBLE layer, the Delete twin, the +60 bar-open delta (the never-pinned FOURTH member of the confirm-bar family)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    // the settle pattern: the seeded count subtitle before interacting
    // (the items views' formatMoney — no grouping: "$2235.00").
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();

    // Open the Rent calculator (the hover-revealed Calculate action; the
    // native locator click IS the full pointer sequence — the v46 lesson).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();

    // The twin state: "Contents Insurance" $25 through the real Add Item
    // flow (the v66 pin's own form — the reference's OWN Rent calculator
    // carries this same single line item, the v45 measurement note).
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Contents Insurance")).toBeVisible();
    await page.waitForTimeout(300);

    // The at-rest row height FIRST (the delta's baseline — the v66
    // contract: 102 in this twin state; re-read live, never assumed).
    const rowHeight = () =>
      page.evaluate(() => {
        const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
          (d.textContent || "").includes("Rent Calculator"),
        );
        if (!panel) return null;
        const h4 = [...panel.querySelectorAll("h4")].find(
          (h) => (h.textContent || "").trim() === "Contents Insurance",
        );
        if (!h4) return null;
        let row: HTMLElement = h4;
        while (row && row !== panel) {
          const cs = getComputedStyle(row);
          if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === "rgb(255, 255, 255)") break;
          row = row.parentElement!;
        }
        return row && row !== panel ? Math.round(row.getBoundingClientRect().height) : null;
      });
    expect(await rowHeight()).toBe(102);

    // The trash click opens the confirm bar (the aria-label finder — the
    // structural form; the native click auto-hovers the row so the
    // hover-revealed action pair is engaged at click time).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await expect(dialog.getByText("Delete this line item?")).toBeVisible();

    // THE BAR CENSUS — the structural finder (the v121 form: the
    // rgb(254,242,242) bg + the exact Cancel/Delete button pair; the
    // class strings never trusted for the walk).
    const census = await page.evaluate(() => {
      const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
        (d.textContent || "").includes("Rent Calculator"),
      );
      if (!panel) return null;
      const bar = [...panel.querySelectorAll("div")].find((d) => {
        const bcs = getComputedStyle(d);
        if (bcs.backgroundColor !== "rgb(254, 242, 242)") return false;
        const btns = [...d.querySelectorAll("button")];
        return (
          btns.length === 2 &&
          (btns[0].textContent || "").trim() === "Cancel" &&
          (btns[1].textContent || "").trim() === "Delete"
        );
      });
      if (!bar) return null;
      const bcs = getComputedStyle(bar);
      const br = bar.getBoundingClientRect();
      const label = bar.querySelector("p");
      const lcs = label ? getComputedStyle(label) : null;
      const cancel = [...bar.querySelectorAll("button")].find(
        (b) => (b.textContent || "").trim() === "Cancel",
      )!;
      const del = [...bar.querySelectorAll("button")].find(
        (b) => (b.textContent || "").trim() === "Delete",
      )!;
      const ccs = getComputedStyle(cancel);
      const cbr = cancel.getBoundingClientRect();
      const dcs = getComputedStyle(del);
      let row: HTMLElement = bar;
      while (row && row !== panel) {
        const cs = getComputedStyle(row);
        if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === "rgb(255, 255, 255)") break;
        row = row.parentElement!;
      }
      return {
        bar: {
          mt: bcs.marginTop,
          display: bcs.display,
          align: bcs.alignItems,
          justify: bcs.justifyContent,
          radius: bcs.borderRadius,
          pad: bcs.padding,
          w: Math.round(br.width),
          h: Math.round(br.height),
        },
        label: lcs
          ? { fs: lcs.fontSize, fw: lcs.fontWeight, txt: (label!.textContent || "").trim() }
          : null,
        // Colors deliberately NOT asserted (the named-palette lab()
        // discipline — text-red-700 / bg-white / bg-red-600 / text-slate-
        // 700 are named utilities whose computed forms drift between
        // engines; the v121 pin's own convention).
        cancelPill: {
          pad: ccs.padding,
          radius: ccs.borderRadius,
          fs: ccs.fontSize,
          fw: ccs.fontWeight,
          h: Math.round(cbr.height),
        },
        cancelShadow: ccs.boxShadow,
        deletePill: {
          pad: dcs.padding,
          radius: dcs.borderRadius,
          fs: dcs.fontSize,
          fw: dcs.fontWeight,
          h: Math.round(del.getBoundingClientRect().height),
        },
        rowOpenH: row && row !== panel ? Math.round(row.getBoundingClientRect().height) : null,
      };
    });
    expect(census).not.toBeNull();
    // The box — the v121 family contract + the calculator-specific mt-3
    // (12px — the family's mt-4 is 16px; THE distinguishing axis).
    expect(census!.bar).toEqual({
      mt: "12px",
      display: "flex",
      align: "center",
      justify: "space-between",
      radius: "8px",
      pad: "12px",
      w: 686,
      h: 48,
    });
    // The label — 14px/400, the exact text (the named-palette color
    // skipped by discipline).
    expect(census!.label).toEqual({ fs: "14px", fw: "400", txt: "Delete this line item?" });
    // The Cancel pill — the v121 twin chrome + the shadow-sm VISIBLE
    // layer by toContain (the accepted-leads convention: v4's
    // transparent composition leads paint nothing; a future Tailwind
    // upgrade that changes the ambient numerics must fail this pin).
    expect(census!.cancelPill).toEqual({
      pad: "4px 12px",
      radius: "6px",
      fs: "12px",
      fw: "500",
      h: 24,
    });
    expect(census!.cancelShadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");
    // The Delete pill — the twin chrome (the bg-red-600 color skipped).
    expect(census!.deletePill).toEqual({
      pad: "4px 12px",
      radius: "6px",
      fs: "12px",
      fw: "500",
      h: 24,
    });
    // THE BAR-OPEN DELTA — the row card grows +60 (the at-rest 102 →
    // 162: the bar's 48 + the mt-3's 12).
    expect(census!.rowOpenH).toBe(162);

    // The Cancel path: the bar closes, the row returns to its at-rest
    // height (the non-destructive rung of the ladder).
    await dialog.getByRole("button", { name: "Cancel" }).click();
    await expect(dialog.getByText("Delete this line item?")).toBeHidden();
    expect(await rowHeight()).toBe(102);

    // The fixture-restore: the destructive Delete through the re-opened
    // bar (the recalc to $0.00), then restoreRent — the e2e convention:
    // every calculator add/delete ends with restoreRent (a missing
    // restore poisons every later spec's dashboard arithmetic).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await expect(dialog.getByText("Delete this line item?")).toBeVisible();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(dialog.getByText("Based on 0 items")).toBeVisible();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });
});


// ---------------------------------------------------------------------------
// v129 — plan F4 (docs/remediation-plan-v129.md): the CALCULATOR
// GHOST-HOVER FAMILY's OWN-HOVER END-STATE census at 1280 — the X + the
// row actions' TINT + COLOR axes. The never-measured COLOR path: the
// close family fully held at REST (the v59 F1 pin the X's {w,h} at 1280;
// the v49 F3 pin {36,36} at 640; the v53 F2 pin {29,36} at 390; the v87
// pin the at-rest chrome {radius 6px / bg transparent / border 0px /
// display flex} — every pinned axis STATIC chrome, the v87 spec's own
// comment); the v27 G1 pin holds the hover:bg-accent CLASS TOKEN on the
// ITEM-DIALOG X — a DIFFERENT element in a different file; the v45 pin
// holds the row's hover:shadow-md + the actions' REVEAL (the group-hover
// opacity path). The computed own-hover end-states — the pointer ON each
// button itself — held by NO spec at ANY viewport. Measured by the
// both-sides one-shot census xhover-arbit-v129.sh + the reference-side
// family census rowaction-hover-ref-v129.sh: the TINT axis IDENTICAL
// both sides (the hovered bg rgb(245,245,245) — the accent #f5f5f5);
// THE COLOR AXIS A CLONE GAP — the reference's ghost family carries
// hover:text-accent-foreground (the hovered color rgb(23,23,23) — the
// same shadcn ghost-icon family the v27 G1 record documents), the
// clone's three buttons (calculator-dialog.tsx:138 the X, :239 the edit,
// :247 the trash) carried hover:bg-accent alone (the hovered color
// staying rgb(10,10,10)). THE REPAIR: hover:text-accent-foreground
// added to all three — the v27 G1 precedent's own fix form. This pin
// locks the repaired contract: the ladders at-rest -> hovered ->
// restored, the row actions' revealed-at-rest colors (the trash KEEPS
// its red at rest — rgb(220,38,38) — the hover-only accent-foreground
// transition), and both hovered states' bg + color.
// ---------------------------------------------------------------------------
test.describe("calculator ghost-hover family own-hover end-state census at 1280 (v129 — plan F4)", () => {
  test("the X + the row actions' own-hover ladders — the accent tint + the repaired accent-foreground color, the at-rest red trash, the restore", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    // the settle pattern: the seeded count subtitle before interacting
    // (the items views' formatMoney — no grouping: "$2235.00").
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();

    // Open the Rent calculator (the hover-revealed Calculate action; the
    // native locator click IS the full pointer sequence — the v46 lesson).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(400);

    // The X's state read — the v87 finder family: the clone's
    // aria-label="Close" superset finder first, the geometric fallback
    // (the 36x36 button in the panel's top band) name-independent.
    const xState = () =>
      page.evaluate(() => {
        const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
          (d.textContent || "").includes("Rent Calculator"),
        ) as HTMLElement | undefined;
        if (!panel) return null;
        const btns = [...panel.querySelectorAll("button")];
        const close =
          btns.find((b) => (b.getAttribute("aria-label") || "") === "Close") ||
          btns.find((b) => {
            const r = b.getBoundingClientRect();
            return (
              Math.abs(r.width - 36) < 3 &&
              Math.abs(r.height - 36) < 3 &&
              r.top < panel.getBoundingClientRect().top + 80 &&
              !/^add item$/i.test((b.textContent || "").trim())
            );
          });
        if (!close) return null;
        const cs = getComputedStyle(close);
        const r = close.getBoundingClientRect();
        return {
          hoverMatch: close.matches(":hover"),
          bg: cs.backgroundColor,
          color: cs.color,
          radius: cs.borderRadius,
          w: Math.round(r.width),
          h: Math.round(r.height),
        };
      });

    // === THE X LADDER — the at-rest rung (the pointer parked at (5,5)) ===
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const xRest = await xState();
    expect(xRest).not.toBeNull();
    // The at-rest contract — the v87 family re-affirmed (the static
    // chrome: transparent bg, the #0a0a0a icon, 36x36, rounded-md).
    expect(xRest!).toEqual({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      radius: "6px",
      w: 36,
      h: 36,
    });

    // === THE X LADDER — the OWN-HOVERED rung (the real pointer on the X) ===
    await dialog.getByRole("button", { name: "Close" }).hover();
    await page.waitForTimeout(300);
    const xHover = await xState();
    // THE REPAIRED AXES: the accent tint + the accent-foreground color —
    // the reference's ghost family contract (rgb(23,23,23) = #171717).
    expect(xHover!).toEqual({
      hoverMatch: true,
      bg: "rgb(245, 245, 245)",
      color: "rgb(23, 23, 23)",
      radius: "6px",
      w: 36,
      h: 36,
    });

    // === THE X LADDER — the restored rung (the pointer re-parked) ===
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const xRestored = await xState();
    expect(xRestored!).toEqual({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      radius: "6px",
      w: 36,
      h: 36,
    });

    // === THE ROW-ACTION LADDERS (the fixture form — the v66/v123 twin
    // state: "Contents Insurance" $25 through the real Add Item flow). ===
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Contents Insurance")).toBeVisible();
    await page.waitForTimeout(300);

    // The row actions' state read — the row's two small buttons (<=34px
    // square, the row scoped: the X is in the header, never caught).
    const actsState = () =>
      page.evaluate(() => {
        const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
          (d.textContent || "").includes("Rent Calculator"),
        ) as HTMLElement | undefined;
        if (!panel) return null;
        const rows = [...panel.querySelectorAll("div")].filter((d) => {
          const t = d.innerText || "";
          return (
            /Contents Insurance/i.test(t) &&
            d.getBoundingClientRect().height > 80 &&
            d.getBoundingClientRect().height < 140
          );
        });
        const row = rows[0];
        if (!row) return null;
        const acts = [...row.querySelectorAll("button")].filter((b) => {
          const r = b.getBoundingClientRect();
          return Math.round(r.width) <= 34 && Math.round(r.height) <= 34;
        });
        return acts.map((b) => {
          const cs = getComputedStyle(b);
          return {
            hoverMatch: b.matches(":hover"),
            bg: cs.backgroundColor,
            color: cs.color,
          };
        });
      });

    // The row hover FIRST (the group-hover reveal — the v45 contract),
    // the pointer on the row's text: the actions revealed at their
    // at-rest colors (the trash KEEPS its red — the hover-only family).
    await dialog.getByText("Contents Insurance").hover();
    await page.waitForTimeout(300);
    const actsRest = await actsState();
    expect(actsRest).not.toBeNull();
    expect(actsRest!).toHaveLength(2);
    expect(actsRest![0]).toEqual({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
    });
    expect(actsRest![1]).toEqual({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(220, 38, 38)",
    });

    // The EDIT button's own-hovered state (the real pointer on the
    // button — the group-hover stays engaged: the pointer is inside
    // the row): the tint + THE REPAIRED color axis.
    await dialog.getByRole("button", { name: "Edit Contents Insurance" }).hover();
    await page.waitForTimeout(300);
    const editHover = await actsState();
    expect(editHover![0]).toEqual({
      hoverMatch: true,
      bg: "rgb(245, 245, 245)",
      color: "rgb(23, 23, 23)",
    });

    // The TRASH button's own-hovered state: the tint + THE REPAIRED
    // color axis (the red goes accent-foreground under hover — the
    // reference's own contract, measured live on its Rent calculator).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).hover();
    await page.waitForTimeout(300);
    const trashHover = await actsState();
    expect(trashHover![1]).toEqual({
      hoverMatch: true,
      bg: "rgb(245, 245, 245)",
      color: "rgb(23, 23, 23)",
    });

    // The fixture-restore: the destructive Delete through the confirm
    // bar, then restoreRent — the e2e convention: every calculator
    // add/delete ends with restoreRent (a missing restore poisons every
    // later spec's dashboard arithmetic).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await expect(dialog.getByText("Delete this line item?")).toBeVisible();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(dialog.getByText("Based on 0 items")).toBeVisible();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });
});
