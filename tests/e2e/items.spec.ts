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

  test("the header count follows the active filters (reference recomputes it)", async ({ page }) => {
    // Reference (session-7 audit, remediation-plan-v4 G6): the "N items · $X"
    // subtitle recomputes BOTH count and total from the FILTERED list.
    await expect(page.getByText("2 items · $5550.00")).toBeVisible();

    // Partial match → one item, its amount.
    await page.getByPlaceholder("Search income items...").fill("salary");
    await expect(page.getByText("1 items · $5200.00")).toBeVisible();

    // No match → zero items, zero total.
    await page.getByPlaceholder("Search income items...").fill("zzz-no-match");
    await expect(page.getByText("0 items · $0.00")).toBeVisible();

    // Clearing the search restores the full count.
    await page.getByPlaceholder("Search income items...").fill("");
    await expect(page.getByText("2 items · $5550.00")).toBeVisible();
  });

  test("filters sit inside the white rounded-2xl card with the reference search chrome", async ({
    page,
  }) => {
    // Reference (F2): search + selects live in a bg-white rounded-2xl p-6
    // bordered card; grid md:grid-cols-4 with the search spanning 2 cols
    // (income/savings), search icon w-5 h-5 + input pl-10.
    const filterCard = await page.evaluate(() => {
      const input = document.querySelector<HTMLInputElement>("input[placeholder^='Search income']");
      if (!input) return null;
      const wrapper = input.parentElement; // relative span (col-span-2)
      const grid = wrapper?.parentElement;
      const card = grid?.parentElement;
      if (!card) return null;
      const cs = getComputedStyle(card);
      const icon = wrapper?.querySelector("svg");
      return {
        cardCls: card.className,
        cardBg: cs.backgroundColor,
        cardBorder: cs.borderColor,
        cardRadius: cs.borderRadius,
        cardPadding: cs.padding,
        gridCls: grid?.className ?? null,
        wrapperCls: wrapper?.className ?? null,
        inputPlCls: input.className.match(/pl-\d+/)?.[0] ?? null,
        iconCls: icon?.getAttribute("class") ?? null,
        selectCount: grid ? grid.querySelectorAll("button[role='combobox']").length : 0,
      };
    });
    expect(filterCard).not.toBeNull();
    expect(filterCard!.cardCls).toContain("rounded-2xl");
    expect(filterCard!.cardBg).toBe("rgb(255, 255, 255)");
    expect(filterCard!.cardBorder).toBe("rgb(229, 231, 227)");
    expect(filterCard!.cardRadius).toBe("16px");
    expect(filterCard!.cardPadding).toBe("24px");
    // Income: search spans 2 of 4 md columns; 2 selects.
    expect(filterCard!.gridCls).toContain("md:grid-cols-4");
    expect(filterCard!.wrapperCls).toContain("md:col-span-2");
    expect(filterCard!.selectCount).toBe(2);
    expect(filterCard!.inputPlCls).toBe("pl-10");
    expect(filterCard!.iconCls).toContain("w-5");
  });

  test("the category filter's listbox keyboard contract (v36 S2)", async ({ page }) => {
    // Session-72 surface #2, first measured v36 on the reference's FILTER
    // instances (v34 covered the calculator sub-dialog only): fresh-open
    // via click AND Enter both land focus on the SELECTED option with the
    // accent highlight (the same :focus-driven family as the menu items);
    // the arrows rove with clamping at both ends; Home/End jump; Escape
    // closes the popup ONLY (focus → the trigger, the page unaffected);
    // Enter selects the highlighted option and updates the trigger text.
    // The clone's seed categories: All Categories / Freelance / Salary.
    const trigger = page.getByRole("combobox", { name: "Filter by category" });
    await trigger.click();
    const listbox = page.locator('[role="listbox"]');
    await expect(listbox).toBeVisible();

    // Fresh-open via CLICK: focus on the SELECTED option ("All Categories")
    // with the accent family (bg #f5f5f5 + text rgb(23,23,23)).
    const freshOpen = await page.evaluate(() => {
      const sel = [...document.querySelectorAll('[role="option"]')].find(
        (o) => o.getAttribute("aria-selected") === "true",
      );
      if (!sel) return null;
      const cs = getComputedStyle(sel);
      return {
        text: (sel.textContent || "").trim(),
        focused: document.activeElement === sel,
        bg: cs.backgroundColor,
        color: cs.color,
        optionCount: document.querySelectorAll('[role="option"]').length,
      };
    });
    expect(freshOpen).not.toBeNull();
    expect(freshOpen!.text).toBe("All Categories");
    expect(freshOpen!.focused).toBe(true);
    expect(freshOpen!.bg).toBe("rgb(245, 245, 245)");
    expect(freshOpen!.color).toBe("rgb(23, 23, 23)");
    expect(freshOpen!.optionCount).toBe(3);

    // ArrowDown roves to Freelance; ArrowDown again lands Salary (the last);
    // a third ArrowDown CLAMPS at Salary.
    await page.keyboard.press("ArrowDown");
    await expect(page.locator('[role="option"]').filter({ hasText: "Freelance" })).toBeFocused();
    await page.keyboard.press("ArrowDown");
    await expect(page.locator('[role="option"]').filter({ hasText: "Salary" })).toBeFocused();
    await page.keyboard.press("ArrowDown");
    await expect(page.locator('[role="option"]').filter({ hasText: "Salary" })).toBeFocused();
    // ArrowUp steps back; Home/End jump to the ends.
    await page.keyboard.press("ArrowUp");
    await expect(page.locator('[role="option"]').filter({ hasText: "Freelance" })).toBeFocused();
    await page.keyboard.press("Home");
    await expect(page.locator('[role="option"]').filter({ hasText: "All Categories" })).toBeFocused();
    await page.keyboard.press("End");
    await expect(page.locator('[role="option"]').filter({ hasText: "Salary" })).toBeFocused();

    // Escape closes the popup ONLY — focus returns to the trigger, the
    // page stays (no dialog in the filter instance).
    await page.keyboard.press("Escape");
    await expect(listbox).not.toBeVisible();
    await expect(trigger).toBeFocused();
    await expect(page.locator('[role="dialog"]')).toHaveCount(0);

    // Enter-open: focus lands on the SELECTED option again (the Select's
    // two open paths land identically — unlike the DropdownMenu).
    await trigger.focus();
    await page.keyboard.press("Enter");
    await expect(listbox).toBeVisible();
    await expect(
      page.locator('[role="option"]').filter({ hasText: "All Categories" }),
    ).toBeFocused();

    // Enter selects the highlighted option: popup closes, the trigger text
    // updates, focus rests on the trigger.
    await page.keyboard.press("ArrowDown");
    await expect(page.locator('[role="option"]').filter({ hasText: "Freelance" })).toBeFocused();
    await page.keyboard.press("Enter");
    await expect(listbox).not.toBeVisible();
    await expect(trigger).toBeFocused();
    await expect(trigger).toHaveText(/Freelance/);

    // Fixture restore: re-select "All Categories" (the header-count specs
    // below depend on the unfiltered view). Wait for Radix to land focus on
    // the (now) selected option BEFORE the key presses — the focus move is
    // async on mount and a racing Home hits the trigger instead (the v36
    // lesson: interleave a toBeFocused() between presses).
    await trigger.click();
    await expect(listbox).toBeVisible();
    await expect(page.locator('[role="option"]').filter({ hasText: "Freelance" })).toBeFocused();
    await page.keyboard.press("Home");
    await expect(
      page.locator('[role="option"]').filter({ hasText: "All Categories" }),
    ).toBeFocused();
    await page.keyboard.press("Enter");
    await expect(listbox).not.toBeVisible();
    await expect(trigger).toHaveText(/All Categories/);
  });

  test("the items-view Tab-order census + the trigger's focus reveal (v36 S3)", async ({ page }) => {
    // Session-72 surface #3, first measured v36 at the PAGE level (v33
    // covered the sub-dialog): the REAL-Tab walk on /income is exactly
    // the five nav links → the Add button → the search input → the
    // category combobox → the frequency combobox → the card kebab
    // triggers (one per card, DOM order) — the same sequence the
    // reference walks minus its Base44 platform badge (platform chrome,
    // not app UI). The kebab stop also pins superset #7: the clone's
    // trigger REVEALS on keyboard focus (focus-visible:opacity-100) —
    // the reference's stays invisible (opacity 0) when Tab-focused and
    // when keyboard-opened.
    const stops: Array<{ tag: string; name: string }> = [];
    const readStop = () =>
      page.evaluate(() => {
        const el = document.activeElement;
        if (!el || el === document.body) return null;
        const r = el.getBoundingClientRect();
        return {
          tag: el.tagName.toLowerCase(),
          role: el.getAttribute("role"),
          name: (
            el.getAttribute("aria-label") ||
            (el.textContent || "").trim().replace(/\s+/g, " ")
          ).slice(0, 30),
          rect: [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)],
          opacity: getComputedStyle(el).opacity,
        };
      });

    // Blur to the page start, then walk with REAL Tab presses (450ms
    // settles — the sheet-ring fade discipline).
    await page.evaluate(() => {
      const el = document.activeElement as HTMLElement | null;
      if (el && el !== document.body) el.blur();
    });
    const expected = [
      { tag: "a", name: "Dashboard" },
      { tag: "a", name: "Income" },
      { tag: "a", name: "Expenses" },
      { tag: "a", name: "Savings" },
      { tag: "a", name: "Net Worth" },
      { tag: "button", name: "Add Income" },
      { tag: "input", name: "Search income items..." },
      { tag: "button", name: "Filter by category" },
      { tag: "button", name: "Filter by frequency" },
      { tag: "button", name: "Actions for Freelance" },
      { tag: "button", name: "Actions for Salary" },
    ];
    for (const want of expected) {
      await page.keyboard.press("Tab");
      await page.waitForTimeout(450);
      const stop = await readStop();
      expect(stop).not.toBeNull();
      stops.push({ tag: stop!.tag, name: stop!.name });
      expect(stop!.tag).toBe(want.tag);
      expect(stop!.name).toBe(want.name);
    }

    // Geometry bands measured on both sites (1280×800): nav links at
    // x=20 starting y≈145 with the 40px rail pitch; the search 447×36;
    // the comboboxes 216×36; the kebabs 36×36.
    const navPitch = await page.evaluate(() => {
      const links = [...document.querySelectorAll("nav a")].slice(0, 5);
      return links.map((l) => Math.round(l.getBoundingClientRect().y));
    });
    expect(navPitch[0]).toBeGreaterThan(140);
    expect(navPitch[0]).toBeLessThan(150);
    for (let i = 1; i < navPitch.length; i++) {
      expect(navPitch[i] - navPitch[i - 1]).toBe(40);
    }

    // The kebab stop (the last walk landing): the REAL Tab engaged
    // :focus-visible, so the clone's superset reveal fires — opacity "1"
    // (the reference's stays "0" at this stop — superset #7, pinned).
    const kebab = page.getByRole("button", { name: "Actions for Salary" });
    await expect(kebab).toBeFocused();
    const reveal = await kebab.evaluate((el) => ({
      opacity: getComputedStyle(el).opacity,
      fv: el.matches(":focus-visible"),
    }));
    expect(reveal.fv).toBe(true);
    expect(reveal.opacity).toBe("1");

    // The walk wraps to the body after the last card trigger (the
    // platform-badge stop the reference carries does not exist here).
    await page.keyboard.press("Tab");
    await page.waitForTimeout(450);
    const afterWrap = await page.evaluate(
      () => document.activeElement === document.body,
    );
    expect(afterWrap).toBe(true);
  });

  test("the filter Select triggers' focus-visible family (v37 S1)", async ({ page }) => {
    // Session-76 surface #1, first measured v37 with a REAL Tab walk on
    // both sites: a REAL Tab onto the CLOSED category-filter trigger
    // engages :focus-visible and renders the 1px #0a0a0a ring layered
    // over the ambient shadow — the border stays untinted
    // rgb(229,229,229) and the geometry unchanged (216×36). O1 (the
    // v3/v4 construct note): the reference's full box-shadow string
    // carries the v3 three-slot construct (a white ring-offset lead)
    // while the clone compiles Tailwind v4's five-slot construct (four
    // transparent leads) — every lead is a 0px-spread shadow, invisible
    // by construction; the VISIBLE layers are byte-identical and are
    // what this pin asserts.
    await page.evaluate(() => {
      if (document.activeElement instanceof HTMLElement) document.activeElement.blur();
    });
    // The v36 census order: five nav links → Add Income → the search
    // input → the category combobox (the 8th Tab).
    for (let i = 0; i < 8; i++) {
      await page.keyboard.press("Tab");
      await page.waitForTimeout(120);
    }
    const trigger = page.getByRole("combobox", { name: "Filter by category" });
    await expect(trigger).toBeFocused();
    const chrome = await trigger.evaluate((el) => {
      const cs = getComputedStyle(el);
      return {
        fv: el.matches(":focus-visible"),
        boxShadow: cs.boxShadow,
        borderColor: cs.borderColor,
        borderWidth: cs.borderWidth,
        w: (el as HTMLElement).offsetWidth,
        h: (el as HTMLElement).offsetHeight,
      };
    });
    expect(chrome.fv).toBe(true);
    // The VISIBLE ring layer (byte-identical to the reference's)…
    expect(chrome.boxShadow).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");
    // …layered over the ambient shadow-sm family.
    expect(chrome.boxShadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");
    // The border stays untinted (the v33 code-input lesson).
    expect(chrome.borderColor).toBe("rgb(229, 229, 229)");
    expect(chrome.borderWidth).toBe("1px");
    expect(chrome.w).toBe(216);
    expect(chrome.h).toBe(36);
  });

  test("the search input's focus + typing contract (v37 S2)", async ({ page }) => {
    // Session-76 surface #2, first measured v37 on both sites: the search
    // input's REAL-Tab focus family (the same 1px #0a0a0a ring + ambient,
    // border untinted) and the REAL-key typing contract — an exact-name
    // match narrows the list + recomputes the header, a no-match string
    // swaps to the EMPTY state (the h3 "No income items yet"), and
    // clearing restores the full card list. The existing fill()-based
    // specs pin the filtering arithmetic; this pin adds the focus chrome
    // and the typed-char path.
    await page.evaluate(() => {
      if (document.activeElement instanceof HTMLElement) document.activeElement.blur();
    });
    // The 7th Tab lands on the search input (the v36 census order).
    for (let i = 0; i < 7; i++) {
      await page.keyboard.press("Tab");
      await page.waitForTimeout(120);
    }
    const search = page.getByPlaceholder("Search income items...");
    await expect(search).toBeFocused();
    const chrome = await search.evaluate((el) => {
      const cs = getComputedStyle(el);
      return {
        fv: el.matches(":focus-visible"),
        boxShadow: cs.boxShadow,
        borderColor: cs.borderColor,
        borderWidth: cs.borderWidth,
      };
    });
    expect(chrome.fv).toBe(true);
    expect(chrome.boxShadow).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");
    expect(chrome.boxShadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");
    expect(chrome.borderColor).toBe("rgb(229, 229, 229)");
    expect(chrome.borderWidth).toBe("1px");

    // REAL typed chars: the exact card name narrows the list.
    await search.pressSequentially("Salary");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await expect(page.getByRole("heading", { name: "Freelance" })).toHaveCount(0);
    await expect(page.getByText("1 items · $5200.00")).toBeVisible();

    // A no-match string swaps to the empty state (its title is the h3 —
    // the reference's card titles are h4, its empty-state heading h3;
    // the L1 probe lesson).
    await search.pressSequentially("zzz");
    await expect(page.getByRole("heading", { name: "No income items yet" })).toBeVisible();
    await expect(page.getByText("0 items · $0.00")).toBeVisible();

    // Clearing restores the full card list.
    await search.fill("");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await expect(page.getByRole("heading", { name: "Freelance" })).toBeVisible();
    await expect(page.getByText("2 items · $5550.00")).toBeVisible();
  });

  test("classification tiles match the reference chrome (flex gap-4, border-2, per-class colors)", async ({
    page,
  }) => {
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();

    const tiles = await dialog.evaluate(() => {
      const group = document.querySelector("[role='radiogroup']");
      if (!group) return null;
      return {
        groupCls: group.className,
        tiles: [...group.children].map((tile) => {
          const cs = getComputedStyle(tile);
          return {
            text: (tile.textContent || "").trim(),
            cls: tile.className,
            border: cs.borderColor,
            bg: cs.backgroundColor,
            borderWidth: cs.borderWidth,
            padding: cs.padding,
          };
        }),
      };
    });
    expect(tiles).not.toBeNull();
    // Reference group: flex gap-4 (tiles flex-1), NOT a 3-col grid.
    expect(tiles!.groupCls).toContain("flex");
    expect(tiles!.groupCls).toContain("gap-4");
    expect(tiles!.groupCls).not.toContain("grid-cols-3");
    expect(tiles!.tiles).toHaveLength(3);
    // Reference tiles: border-2, p-4, capitalized labels.
    for (const tile of tiles!.tiles) {
      expect(tile.borderWidth).toBe("2px");
      expect(tile.padding).toBe("16px");
      expect(tile.cls).toContain("cursor-pointer");
    }
    expect(tiles!.tiles.map((t) => t.text)).toEqual(["Need", "Want", "Savings"]);
    // Income defaults to "need" — selected tile: orange border + #fff7f5 tint
    // (per-classification colors, NOT the old uniform forestMedium).
    const need = tiles!.tiles[0];
    expect(need.border).toBe("rgb(224, 122, 59)");
    expect(need.bg).toBe("rgb(255, 247, 245)");
    // Unselected tiles: default border, white bg.
    expect(tiles!.tiles[1].border).toBe("rgb(229, 231, 227)");
    expect(tiles!.tiles[1].bg).toBe("rgb(255, 255, 255)");
    expect(tiles!.tiles[2].border).toBe("rgb(229, 231, 227)");

    await page.getByRole("button", { name: "Cancel" }).click();
    await expect(dialog).toBeHidden();
  });

  test("add → edit → delete round-trip through the dialog", async ({ page }) => {
    // --- add (wait for a seeded card first: the prerendered page carries the
    // empty-store state where BOTH the header and empty-state "Add Income"
    // buttons exist until hydration + the boot fetch land — a strict-mode race)
    await expect(page.getByRole("heading", { name: "Freelance" })).toBeVisible();
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
    // quarterly → indigo badge (reference frequency map, hex-pinned v8 G2).
    const quarterlyBadge = created.getByText("quarterly", { exact: true });
    await expect(quarterlyBadge).toBeVisible();
    await expect(quarterlyBadge).toHaveClass(/bg-\[#eef2ff\] text-\[#4338ca\]/);
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
    // Expenses filter grid (F2): md:grid-cols-2 lg:grid-cols-4 with the
    // search + 3 selects inside the rounded-2xl card.
    const gridInfo = await page.evaluate(() => {
      const input = document.querySelector<HTMLInputElement>("input[placeholder^='Search expense']");
      const grid = input?.parentElement?.parentElement ?? null;
      return grid
        ? {
            cls: grid.className,
            selectCount: grid.querySelectorAll("button[role='combobox']").length,
            cardCls: grid.parentElement?.className ?? null,
          }
        : null;
    });
    expect(gridInfo).not.toBeNull();
    expect(gridInfo!.cls).toContain("md:grid-cols-2");
    expect(gridInfo!.cls).toContain("lg:grid-cols-4");
    expect(gridInfo!.selectCount).toBe(3);
    expect(gridInfo!.cardCls).toContain("rounded-2xl");
    // Add Expense carries the orange gradient.
    const add = page.getByRole("button", { name: "Add Expense" });
    const bg = await add.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))");

    // Seeded cards with classification + frequency badges.
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await expect(rent.getByText("$1850.00")).toBeVisible();
    const needBadge = rent.getByText("need", { exact: true });
    await expect(needBadge).toBeVisible();
    // Hex-pinned badge classes (plan v8 G2 — computed values pinned in
    // tests/e2e/badge-colors.spec.ts).
    await expect(needBadge).toHaveClass(/bg-\[#fef2f2\] text-\[#b91c1c\] border-\[#fecaca\]/);
    await expect(rent.getByText("monthly", { exact: true })).toHaveClass(/bg-\[#faf5ff\]/);
    await expect(rent.getByText("active", { exact: true })).toHaveClass(/bg-\[#f8fafc\]/);
    // Recurring badge: capitalized, green, with the repeat icon (class
    // order interleaves utilities — assert each color class separately).
    const recurring = rent.getByText("Recurring", { exact: true });
    await expect(recurring).toBeVisible();
    await expect(recurring).toHaveClass(/bg-\[#f0fdf4\]/);
    await expect(recurring).toHaveClass(/text-\[#15803d\]/);
    await expect(recurring.locator("svg.lucide-repeat")).toBeVisible();
    // v28 G1: the reference's badge hover family — every card badge
    // carries transition-colors + the hover tint (a REAL CDP hover tints
    // the bg to rgba(245,245,245,0.8), secondary #f5f5f5 at 80%; measured
    // live on the reference's status/need badges this session). The tint
    // is pinned via .zb-badge-hover (globals.css) — Tailwind v4 computes
    // hover:bg-secondary/80 as oklab, the reference renders plain rgba
    // (the v7 G6 oklab-drift lesson). The reference's inert focus classes
    // (focus:ring-2 on non-focusable DIVs) render nothing on either site
    // — not pinned.
    await expect(needBadge).toHaveClass(/transition-colors/);
    await expect(needBadge).toHaveClass(/zb-badge-hover/);
    await expect(rent.getByText("monthly", { exact: true })).toHaveClass(/zb-badge-hover/);
    await expect(rent.getByText("active", { exact: true })).toHaveClass(/zb-badge-hover/);
    await expect(recurring).toHaveClass(/zb-badge-hover/);
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
    await expect(calculate).toHaveClass(/text-\[#ea580c\]/);
    // Expense cards have NO ellipsis menu (reference DOM: 0/3 cards).
    await expect(rent.getByRole("button", { name: /Actions for/ })).toHaveCount(0);
    // v28 G2: the footer buttons' keyboard family — the reference's Edit/
    // Calculate carry the shadcn focus base (focus-visible:ring-1 — a 1px
    // #0a0a0a ring on a REAL Tab walk, the same family as every reference
    // button); the clone's hand-written strings had NO focus family (the
    // UA default outline rendered instead). Edit also carries the
    // reference's hover:text-accent-foreground; Calculate keeps its
    // orange text on hover (no hover-text class on the reference either).
    await expect(edit).toHaveClass(/focus-visible:outline-none/);
    await expect(edit).toHaveClass(/focus-visible:ring-1/);
    await expect(edit).not.toHaveClass(/focus-visible:ring-2/);
    await expect(edit).toHaveClass(/hover:text-accent-foreground/);
    await expect(calculate).toHaveClass(/focus-visible:outline-none/);
    await expect(calculate).toHaveClass(/focus-visible:ring-1/);
    await expect(calculate).not.toHaveClass(/focus-visible:ring-2/);
    await expect(calculate).not.toHaveClass(/hover:text-accent-foreground/);
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

  test("the payment-method filter's full contract (v37 S3)", async ({ page }) => {
    // Session-76 surface #3, first measured v37 live on both sites: the
    // third Select's trigger ("All Payment Methods", 216×36) opens a
    // listbox whose options are DERIVED from the seed's expense payment
    // methods (the reference's own list carries only its All option —
    // its demo items hold no paymentMethod values; its edit dialog
    // carries the "payment method" field, so the model matches). The
    // clone's seed: Rent/Bank Transfer, Groceries/Credit Card,
    // Entertainment/Credit Card. Selecting "Credit Card" narrows the
    // cards to the two Credit Card expenses + recomputes the header;
    // resetting to All restores the three cards.
    const pm = page.getByRole("combobox", { name: "Filter by payment method" });
    await expect(pm).toHaveText(/All Payment Methods/);
    const trigGeom = await pm.evaluate((el) => ({
      w: (el as HTMLElement).offsetWidth,
      h: (el as HTMLElement).offsetHeight,
    }));
    expect(trigGeom.w).toBe(216);
    expect(trigGeom.h).toBe(36);

    // Open: the dynamically derived option list (the seed's two
    // payment methods + the All option).
    await pm.click();
    const listbox = page.locator('[role="listbox"]');
    await expect(listbox).toBeVisible();
    await expect(page.getByRole("option", { name: "All Payment Methods" })).toBeVisible();
    await expect(page.getByRole("option", { name: "Bank Transfer" })).toBeVisible();
    await expect(page.getByRole("option", { name: "Credit Card" })).toBeVisible();

    // Select "Credit Card" → the trigger text updates, the cards narrow
    // to the two Credit Card expenses, the header recomputes.
    await page.getByRole("option", { name: "Credit Card" }).click();
    await expect(pm).toHaveText(/Credit Card/);
    await expect(page.getByRole("heading", { name: "Entertainment" })).toBeVisible();
    await expect(page.getByRole("heading", { name: "Groceries" })).toBeVisible();
    await expect(page.getByRole("heading", { name: "Rent" })).toHaveCount(0);
    await expect(page.getByText("2 items · $385.00")).toBeVisible();

    // Reset to All (the fixture-restore discipline): the three cards
    // and the full header count come back.
    await pm.click();
    await page.getByRole("option", { name: "All Payment Methods" }).click();
    await expect(pm).toHaveText(/All Payment Methods/);
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();
    await expect(page.getByRole("heading", { name: "Groceries" })).toBeVisible();
    await expect(page.getByRole("heading", { name: "Entertainment" })).toBeVisible();
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
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
    await expect(savingsBadge).toHaveClass(/bg-\[#f0fdf4\] text-\[#15803d\] border-\[#bbf7d0\]/);
    await expect(savingsBadge.locator("svg.lucide-piggy-bank")).toBeVisible();
  });
});

test.describe("budget-item card delete failure (v18 G1)", () => {
  // The third `void` site of the v18 G1 family: the item-card inline
  // confirm bar called `void deleteItem(item.id)` — an unhandled
  // rejection with NO toast (the same accident as the net-worth
  // confirm bars, fixed the same pass; the DIALOG's delete was always
  // caught — "Could not delete the item" — but the card menu's own
  // inline confirm was not). Measured on the reference with its entity
  // API dead: the failed delete leaves the card silently (the same
  // silent no-op family as every tier). The clone keeps the surfaces
  // (card + confirm bar stay — the store filters only after the API
  // resolves) and toasts the honest error. The aborted DELETE never
  // reaches the server, so no fixture restore is needed.
  test("item-card delete failure keeps the card + confirm bar + error toast (v18 G1)", async ({ page }) => {
    await page.goto("/income");
    // The e2e seed's income census (Salary + Freelance = $5550.00).
    await expect(page.getByText("2 items · $5550.00")).toBeVisible();

    await page.route("**/api/budget-items**", async (route) => {
      await route.abort("failed");
    });

    const card = page.locator("div.rounded-xl").filter({ hasText: "Salary" }).first();
    await expect(card).toBeVisible();
    await card.hover();
    await page.getByRole("button", { name: "Actions for Salary" }).click();
    await page.getByRole("menuitem", { name: "Delete" }).click();
    await expect(page.getByText("Delete this item?")).toBeVisible();
    await page.getByRole("button", { name: "Delete", exact: true }).click();

    // PARITY: the card stays (the reference's silent no-op); the inline
    // confirm bar stays up — the user is left mid-action, not misled.
    await expect(card.getByText("Salary")).toBeVisible();
    await expect(page.getByText("Delete this item?")).toBeVisible();

    // SUPERSET: the honest error toast (the dialog-delete's established
    // text, now shared by the card path). exact:true per the live-region
    // lesson.
    await expect(
      page.getByText("Could not delete the item", { exact: true })
    ).toBeVisible();
    await expect(
      page.getByText("Network error — check your connection and try again", {
        exact: true,
      })
    ).toBeVisible();

    // Per-click semantics: exactly ONE toast for this click.
    await page.waitForTimeout(600);
    const toastCount = await page
      .getByText("Could not delete the item", { exact: true })
      .count();
    expect(toastCount).toBe(1);

    // Leave the UI clean (the API stays dead — nothing was written).
    await page.getByRole("button", { name: "Cancel", exact: true }).click();
    await expect(page.getByText("Delete this item?")).toHaveCount(0);

    await page.unrouteAll({ behavior: "ignoreErrors" });
  });
});
