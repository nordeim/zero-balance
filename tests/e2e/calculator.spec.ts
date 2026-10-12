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
