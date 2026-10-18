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

  test("the filter-card computed census at 1280 (v64 — plan F3)", async ({ page }) => {
    // The v64 fresh sweep of the OLDEST desktop pair (the v57-era items
    // pair re-run) measured a never-census'd family: the INCOME view's
    // filter card at desktop 1280 — the never-census'd sibling of the
    // v38 S2 savings pin (v37/v38 measured the /expenses triggers + the
    // /savings instance; the v52 F2 pin covered this card's MOBILE 390
    // state; the test above pins the CLASS STRINGS only). Measured
    // BYTE-IDENTICAL on BOTH sites via arbit-v64.sh: the card 960×86,
    // the search 447×36 with the asymmetric 40px left pad, the 4-track
    // 215.5px grid with the search spanning 2, the two 216×36
    // comboboxes at 14px. This pin locks the computed geometry.
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/income");
    await expect(page.getByText("2 items · $5550.00")).toBeVisible();

    const census = await page.evaluate(() => {
      const search = document.querySelector<HTMLInputElement>(
        "input[placeholder^='Search income']",
      );
      if (!search) return null;
      const card = search.closest("div.rounded-2xl") as HTMLElement | null;
      if (!card) return null;
      const ccs = getComputedStyle(card);
      const scs = getComputedStyle(search);
      // the inner grid: the card's direct grid child
      const inner = [...card.children].find(
        (c) => getComputedStyle(c).display === "grid",
      );
      const ics = inner ? getComputedStyle(inner) : null;
      return {
        card: {
          w: Math.round(card.getBoundingClientRect().width),
          h: Math.round(card.getBoundingClientRect().height),
          pad: ccs.padding,
          radius: ccs.borderRadius,
          bg: ccs.backgroundColor,
          border: ccs.borderTopColor,
          mb: ccs.marginBottom,
        },
        search: {
          w: Math.round(search.getBoundingClientRect().width),
          h: Math.round(search.getBoundingClientRect().height),
          pad: scs.padding,
          radius: scs.borderRadius,
          border: scs.borderTopColor,
        },
        innerGrid: ics
          ? {
              cols: ics.gridTemplateColumns,
              gap: ics.gap,
              childCount: inner!.children.length,
            }
          : null,
        comboboxes: inner
          ? [...inner.querySelectorAll<HTMLElement>('[role="combobox"]')].map(
              (c) => ({
                w: Math.round(c.getBoundingClientRect().width),
                h: Math.round(c.getBoundingClientRect().height),
                fs: getComputedStyle(c).fontSize,
                text: (c.textContent || "").trim().slice(0, 22),
              }),
            )
          : null,
      };
    });
    expect(census).not.toBeNull();

    // The card chrome — measured byte-identical on BOTH sites: the
    // 960-wide (the rail 256 + the content column 1024 − the p-8 64)
    // 86-tall (24 pad + 36 control + 24 pad + the 2px borders) card.
    expect(census!.card).toEqual({
      w: 960,
      h: 86,
      pad: "24px",
      radius: "16px",
      bg: "rgb(255, 255, 255)",
      border: "rgb(229, 231, 227)",
      mb: "24px",
    });

    // The search input: 447×36 (the 2-col span: 215.5 + 16 + 215.5)
    // with the asymmetric 40px left pad (the search icon's room).
    expect(census!.search).toEqual({
      w: 447,
      h: 36,
      pad: "4px 12px 4px 40px",
      radius: "6px",
      border: "rgb(229, 229, 229)",
    });

    // The inner grid: 4 tracks × 215.5px, 16px gap, 3 children (the
    // search wrapper spanning 2 + the two comboboxes).
    expect(census!.innerGrid).toEqual({
      cols: "215.5px 215.5px 215.5px 215.5px",
      gap: "16px",
      childCount: 3,
    });

    // The comboboxes: 216×36 each at 14px with the All-rest texts.
    expect(census!.comboboxes).toHaveLength(2);
    for (const combo of census!.comboboxes!) {
      expect(combo).toMatchObject({ w: 216, h: 36, fs: "14px" });
    }
    expect(census!.comboboxes![0].text).toBe("All Categories");
    expect(census!.comboboxes![1].text).toBe("All Frequencies");
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

  test("the frequency filter's option census + round-trip (v38 S1)", async ({ page }) => {
    // Session-78 queue surface #1, first measured v38 live on BOTH sites:
    // the second Select's option list is the STATIC 7-option list —
    // byte-identical to the reference's (All Frequencies + One-time +
    // Weekly + Bi-weekly + Monthly + Quarterly + Annually; the same
    // static list the v34 pin covered in the sub-dialog instance — here
    // measured live at the /expenses filter instance for the first time).
    // The round-trip on the reference: "One-time" → 0 cards + "0 items ·
    // $0.00" (its demo expenses are all recurring — data-level); on the
    // clone: "Weekly" → the Groceries card + "1 items · $320.00". The
    // contract shape is identical; the seed's frequencies differ.
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();

    const freq = page.getByRole("combobox", { name: "Filter by frequency" });
    await expect(freq).toHaveText(/All Frequencies/);
    const geom = await freq.evaluate((el) => ({
      w: (el as HTMLElement).offsetWidth,
      h: (el as HTMLElement).offsetHeight,
    }));
    expect(geom.w).toBe(216);
    expect(geom.h).toBe(36);

    // Open: the static option census — the reference's byte-identical list.
    await freq.click();
    const listbox = page.locator('[role="listbox"]');
    await expect(listbox).toBeVisible();
    await expect(page.locator('[role="option"]')).toHaveCount(7);
    // exact:true — "Weekly" is a substring of "Bi-weekly" (a strict-mode
    // collision the census loop must avoid).
    for (const name of [
      "All Frequencies",
      "One-time",
      "Weekly",
      "Bi-weekly",
      "Monthly",
      "Quarterly",
      "Annually",
    ]) {
      await expect(page.getByRole("option", { name, exact: true })).toBeVisible();
    }

    // Select Weekly → the cards narrow to the seed's one weekly expense.
    await page.getByRole("option", { name: "Weekly", exact: true }).click();
    await expect(freq).toHaveText(/Weekly/);
    await expect(page.getByRole("heading", { name: "Groceries" })).toBeVisible();
    await expect(page.getByRole("heading", { name: "Rent" })).toHaveCount(0);
    await expect(page.getByRole("heading", { name: "Entertainment" })).toHaveCount(0);
    await expect(page.getByText("1 items · $320.00")).toBeVisible();

    // Reset to All (the fixture-restore discipline): the three cards and
    // the full header count come back.
    await freq.click();
    await page.getByRole("option", { name: "All Frequencies" }).click();
    await expect(freq).toHaveText(/All Frequencies/);
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

  test("the filter-card instance + the category round-trip (v38 S2)", async ({ page }) => {
    // Session-78 queue surface #2, first measured v38 live on BOTH sites:
    // the /savings filter card is byte-identical to the reference's —
    // the white rounded-2xl card (bg rgb(255,255,255), radius 16px,
    // border rgb(229,231,227), padding 24px), the 447×36 search input,
    // the two 216×36 comboboxes ("All Categories" / "All Frequencies"),
    // the 4-column grid (md:grid-cols-4 with the search spanning 2). The
    // reference's own category list carries only its All + "Emergency
    // Fund" (its demo savings has ONE item — data-level); the clone's
    // adds "Investments" (its richer seed). The reference's search input
    // carries NO aria-label; the clone's does (the superset).
    await page.goto("/savings");
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();

    // The filter card's chrome (measured on both sites).
    const card = page.locator("main .rounded-2xl").first();
    const chrome = await card.evaluate((el) => {
      const cs = getComputedStyle(el);
      return {
        bg: cs.backgroundColor,
        radius: cs.borderRadius,
        borderColor: cs.borderColor,
        padding: cs.padding,
      };
    });
    expect(chrome.bg).toBe("rgb(255, 255, 255)");
    expect(chrome.radius).toBe("16px");
    expect(chrome.borderColor).toBe("rgb(229, 231, 227)");
    expect(chrome.padding).toBe("24px");

    // The search input: 447×36 with the savings placeholder + the
    // aria-label superset (the reference's input carries no label).
    const search = page.getByPlaceholder("Search savings items...");
    await expect(search).toHaveAttribute("aria-label", "Search savings items...");
    const searchGeom = await search.evaluate((el) => ({
      w: (el as HTMLElement).offsetWidth,
      h: (el as HTMLElement).offsetHeight,
    }));
    expect(searchGeom.w).toBe(447);
    expect(searchGeom.h).toBe(36);

    // The two comboboxes at the reference's 216×36.
    const cat = page.getByRole("combobox", { name: "Filter by category" });
    const freqC = page.getByRole("combobox", { name: "Filter by frequency" });
    for (const combo of [cat, freqC]) {
      const g = await combo.evaluate((el) => ({
        w: (el as HTMLElement).offsetWidth,
        h: (el as HTMLElement).offsetHeight,
      }));
      expect(g.w).toBe(216);
      expect(g.h).toBe(36);
    }

    // The category round-trip: the options = All + the seed's two
    // categories (the reference's list adds only its own one).
    await cat.click();
    const listbox = page.locator('[role="listbox"]');
    await expect(listbox).toBeVisible();
    await expect(page.getByRole("option", { name: "All Categories" })).toBeVisible();
    await expect(page.getByRole("option", { name: "Emergency Fund" })).toBeVisible();
    await expect(page.getByRole("option", { name: "Investments" })).toBeVisible();
    await page.getByRole("option", { name: "Emergency Fund" }).click();
    await expect(cat).toHaveText(/Emergency Fund/);
    await expect(page.getByRole("heading", { name: "Emergency Fund" })).toBeVisible();
    await expect(page.getByRole("heading", { name: "Investments" })).toHaveCount(0);
    await expect(page.getByText("1 items · $800.00")).toBeVisible();

    // Reset to All (the fixture-restore discipline): both cards and the
    // full header count come back.
    await cat.click();
    await page.getByRole("option", { name: "All Categories" }).click();
    await expect(cat).toHaveText(/All Categories/);
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();
  });

  test("the page-header row computed census at 1280 (v65 — plan F3)", async ({ page }) => {
    // The v65 fresh sweep of the OLDEST remaining desktop pair (the
    // v58-era savings pair re-run) measured a never-census'd family: the
    // DESKTOP 1280 page-header row of the items views — the v42 census
    // pinned the MID-640 STACKED state only (dir column); the v63 pin
    // the mobile 390 networth header block; the early-era tests pin
    // CLASS STRINGS (the chip h-12, the Add-button gradient) but never
    // the computed geometry of the 1280 row. Measured BYTE-IDENTICAL on
    // BOTH sites via arbit-v65.sh + arbit-v65b.sh: the row flex
    // space-between/center/gap 16/mb 32/h 60, the chip 48×48 rounded-xl
    // with the savings blue gradient, the white 24×24 chip icon, the h1
    // 30px/700/lh 36/forestDark, the subtitle 16px/400/gray-500, the
    // Add button 150×36/6px radius/8px 16px pad/14px-500/white with the
    // .zb-btn-add visible shadow layers, the 16×16 plus icon. (The
    // reference carries a HIDDEN zero-size h1 "ZeroBalance" first in
    // its DOM — its own SEO pattern; the VISIBLE h1 is the contract.)
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();

    const census = await page.evaluate(() => {
      const addBtn = [...document.querySelectorAll("button")].find(
        (b) => (b.textContent || "").includes("Add") && b.getBoundingClientRect().width > 0,
      );
      if (!addBtn) return null;
      // the header row: walk UP from the Add button to the container
      // that also holds the visible h1 (the v65 arbitration's finder)
      let row: HTMLElement | null = null;
      let cur: HTMLElement | null = addBtn.parentElement;
      for (let i = 0; i < 6 && cur; i++) {
        if (cur.querySelector("h1") && cur !== addBtn) {
          row = cur;
          break;
        }
        cur = cur.parentElement;
      }
      if (!row) return null;
      const rcs = getComputedStyle(row);
      const h1 = row.querySelector("h1") as HTMLElement | null;
      if (!h1) return null;
      const h1cs = getComputedStyle(h1);
      const chip = row.querySelector<HTMLElement>("div.h-12");
      const chipCs = chip ? getComputedStyle(chip) : null;
      const chipIcon = chip?.querySelector("svg") ?? null;
      const sub = h1.parentElement?.querySelector("p") ?? null;
      const subCs = sub ? getComputedStyle(sub) : null;
      const btcs = getComputedStyle(addBtn);
      const btnIcon = addBtn.querySelector("svg");
      return {
        row: {
          display: rcs.display,
          justify: rcs.justifyContent,
          align: rcs.alignItems,
          gap: rcs.gap,
          mb: rcs.marginBottom,
          h: Math.round(row.getBoundingClientRect().height),
        },
        chip: chip
          ? {
              w: Math.round(chip.getBoundingClientRect().width),
              h: Math.round(chip.getBoundingClientRect().height),
              radius: chipCs!.borderRadius,
              bg: chipCs!.backgroundImage,
            }
          : null,
        chipIcon: chipIcon
          ? {
              w: Math.round(chipIcon.getBoundingClientRect().width),
              h: Math.round(chipIcon.getBoundingClientRect().height),
              color: getComputedStyle(chipIcon).color,
            }
          : null,
        h1: {
          fs: h1cs.fontSize,
          fw: h1cs.fontWeight,
          lh: h1cs.lineHeight,
          color: h1cs.color,
        },
        subtitle: sub
          ? {
              fs: subCs!.fontSize,
              fw: subCs!.fontWeight,
              color: subCs!.color,
            }
          : null,
        addButton: {
          text: (addBtn.textContent || "").trim().slice(0, 20),
          w: Math.round(addBtn.getBoundingClientRect().width),
          h: Math.round(addBtn.getBoundingClientRect().height),
          radius: btcs.borderRadius,
          pad: btcs.padding,
          fs: btcs.fontSize,
          fw: btcs.fontWeight,
          color: btcs.color,
          bg: btcs.backgroundImage,
          shadow: btcs.boxShadow,
        },
        addButtonIcon: btnIcon
          ? {
              w: Math.round(btnIcon.getBoundingClientRect().width),
              h: Math.round(btnIcon.getBoundingClientRect().height),
            }
          : null,
      };
    });
    expect(census).not.toBeNull();

    // The header row — measured byte-identical on BOTH sites: the
    // space-between row (the chip block left, the Add button right),
    // gap 16px, mb 32px, h 60 (the chip 48 + the 12px centering).
    expect(census!.row).toEqual({
      display: "flex",
      justify: "space-between",
      align: "center",
      gap: "16px",
      mb: "32px",
      h: 60,
    });

    // The gradient chip + its white icon (h-12 w-12 rounded-xl).
    expect(census!.chip).toEqual({
      w: 48,
      h: 48,
      radius: "12px",
      bg: "linear-gradient(135deg, rgb(44, 95, 124), rgb(59, 126, 161))",
    });
    expect(census!.chipIcon).toEqual({
      w: 24,
      h: 24,
      color: "rgb(255, 255, 255)",
    });

    // The h1 + the count subtitle (the subtitle TEXT is the data class;
    // the chrome — 16px/400/gray-500 — is the pin).
    expect(census!.h1).toEqual({
      fs: "30px",
      fw: "700",
      lh: "36px",
      color: "rgb(26, 58, 46)",
    });
    expect(census!.subtitle).toEqual({
      fs: "16px",
      fw: "400",
      color: "rgb(107, 114, 128)",
    });

    // The Add button + its icon — the .zb-btn-add chrome (v11) with the
    // savings blue gradient; the visible shadow layers byte-identical
    // to the reference's (the v4 lead-layer form documented in AGENTS).
    expect(census!.addButton).toEqual({
      text: "Add Savings",
      w: 150,
      h: 36,
      radius: "6px",
      pad: "8px 16px",
      fs: "14px",
      fw: "500",
      color: "rgb(255, 255, 255)",
      bg: "linear-gradient(135deg, rgb(44, 95, 124), rgb(59, 126, 161))",
      shadow: "rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px",
    });
    expect(census!.addButtonIcon).toEqual({ w: 16, h: 16 });
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

// ---------------------------------------------------------------------------
// v45 — the item-card grid census at 1280 (plan F1,
// docs/remediation-plan-v45.md).
//
// Measured live on BOTH sites (items-card-v45.mjs, drivers ref-v45.sh +
// clone-v45.sh): the grid 960 wide (the rail 256 + the content column
// 1024 − the p-8 64 — the SAME arithmetic on both sites), 3 columns ×
// 309.328px, gap 16; the card 309 wide / pad 20 / radius 12 / border 1px
// rgb(229,231,227) / the rest shadow rgba(0,0,0,0.04) 0px 2px 8px 0px
// (computed 4-value — Chrome normalizes the 3-value inline to the SAME
// string the reference computes) / transition all 0.2s; the title row
// gap 8 / dot 8×8 / title 16px-600; the income kebab 36×36 opacity 0;
// the expense action row top 12 / right 12 / gap 8 / btn h 32 / padX 12
// / fontSize 12. THE CARD'S REAL HOVER IS INERT ON BOTH SITES (the
// inline boxShadow beats the hover:shadow-lg utility — the v29
// inline-beats-class family) while the expense action row REVEALS
// (opacity 0→1) and its buttons carry shadow-md's VISIBLE layers at
// rest (the shadow-scale regression pin — v4 kept v3's numerics for md;
// a Tailwind upgrade that changes the scale must fail this test).
test.describe("item-card grid census at 1280 (v45 — plan F1)", () => {
  test("the income card grid + chrome + the INERT hover (v45 F1a)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/income");
    await expect(page.getByText("Salary").first()).toBeVisible();

    const census = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement;
      const readCard = (c: HTMLElement) => {
        const cs = getComputedStyle(c);
        return {
          w: Math.round(c.getBoundingClientRect().width),
          pad: cs.padding,
          radius: cs.borderRadius,
          border: `${cs.borderTopWidth} ${cs.borderTopStyle} ${cs.borderTopColor}`,
          boxShadow: cs.boxShadow,
          bg: cs.backgroundColor,
          cursor: cs.cursor,
          transition: cs.transitionProperty,
          transitionDur: cs.transitionDuration,
        };
      };
      const gcs = getComputedStyle(grid);
      const dot = [...card.querySelectorAll("div,span")].find((d) => {
        const cs = getComputedStyle(d);
        const r = d.getBoundingClientRect();
        return !d.children.length && r.width > 0 && r.width <= 12 && cs.backgroundColor !== "rgba(0, 0, 0, 0)";
      });
      const title = [...card.querySelectorAll("h1,h2,h3,h4")][0] as HTMLElement | undefined;
      const kebab = [...card.querySelectorAll("button")].find(
        (b) => !(b.textContent || "").trim() && b.querySelectorAll("svg").length === 1,
      );
      return {
        grid: {
          w: Math.round(grid.getBoundingClientRect().width),
          gap: gcs.gap,
          childCount: grid.children.length,
        },
        card: readCard(card),
        titleRow: title
          ? {
              gap: getComputedStyle(title.parentElement!).gap,
              dotW: dot ? Math.round(dot.getBoundingClientRect().width) : null,
              dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
              font: getComputedStyle(title).fontSize,
              weight: getComputedStyle(title).fontWeight,
            }
          : null,
        kebab: kebab
          ? {
              w: Math.round(kebab.getBoundingClientRect().width),
              h: Math.round(kebab.getBoundingClientRect().height),
              opacity: getComputedStyle(kebab).opacity,
            }
          : null,
      };
    });
    expect(census).not.toBeNull();
    expect(census!.grid.w).toBe(960);
    expect(census!.grid.gap).toBe("16px");
    expect(census!.grid.childCount).toBe(2); // Salary + Freelance
    expect(census!.card.w).toBe(309);
    expect(census!.card.pad).toBe("20px");
    expect(census!.card.radius).toBe("12px");
    expect(census!.card.border).toBe("1px solid rgb(229, 231, 227)");
    expect(census!.card.boxShadow).toBe("rgba(0, 0, 0, 0.04) 0px 2px 8px 0px");
    expect(census!.card.bg).toBe("rgb(255, 255, 255)");
    expect(census!.card.cursor).toBe("pointer");
    expect(census!.card.transition).toBe("all");
    expect(census!.card.transitionDur).toBe("0.2s");
    expect(census!.titleRow!.gap).toBe("8px");
    expect(census!.titleRow!.dotW).toBe(8);
    expect(census!.titleRow!.dotBg).toBe("rgb(143, 188, 63)");
    expect(census!.titleRow!.font).toBe("16px");
    expect(census!.titleRow!.weight).toBe("600");
    expect(census!.kebab!.w).toBe(36);
    expect(census!.kebab!.h).toBe(36);
    expect(census!.kebab!.opacity).toBe("0");

    // A REAL pointer hover leaves the card's shadow INERT (the inline
    // boxShadow beats hover:shadow-lg on BOTH sites — the v29 family).
    const cardLoc = page.locator('div[class*="grid-cols-3"] > div').first();
    await cardLoc.hover();
    await page.waitForTimeout(400);
    const hovered = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      const card = grid!.children[0] as HTMLElement;
      return { boxShadow: getComputedStyle(card).boxShadow, translate: getComputedStyle(card).translate };
    });
    expect(hovered.boxShadow).toBe("rgba(0, 0, 0, 0.04) 0px 2px 8px 0px");
    expect(hovered.translate).toBe("none");
  });

  test("the expense card action row + the hover reveal + the shadow-md regression pin (v45 F1b)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    await expect(page.getByText("Rent").first()).toBeVisible();

    const census = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement;
      const actionRow = [...card.querySelectorAll("div")].find((d) => {
        const cs = getComputedStyle(d);
        return cs.position === "absolute" && cs.opacity === "0" && d.children.length > 0;
      });
      const actionBtn = actionRow ? (actionRow.querySelector("button") as HTMLElement) : null;
      return {
        grid: {
          w: Math.round(grid.getBoundingClientRect().width),
          gap: getComputedStyle(grid).gap,
          childCount: grid.children.length,
        },
        cardW: Math.round(card.getBoundingClientRect().width),
        cardShadow: getComputedStyle(card).boxShadow,
        actionRow: actionRow
          ? {
              top: getComputedStyle(actionRow).top,
              right: getComputedStyle(actionRow).right,
              gap: getComputedStyle(actionRow).gap,
              btnH: Math.round(actionRow.querySelector("button")!.getBoundingClientRect().height),
              btnPadX: getComputedStyle(actionRow.querySelector("button")!).paddingLeft,
              fontSize: getComputedStyle(actionRow.querySelector("button")!).fontSize,
            }
          : null,
        // The action buttons' REST shadow-md (v45 F4-family): the
        // VISIBLE layers — the accepted-leads convention (v10 lesson).
        actionBtnShadow: actionBtn ? getComputedStyle(actionBtn).boxShadow : null,
      };
    });
    expect(census).not.toBeNull();
    expect(census!.grid.w).toBe(960);
    expect(census!.grid.gap).toBe("16px");
    expect(census!.grid.childCount).toBe(3); // Rent + Groceries + Entertainment
    expect(census!.cardW).toBe(309);
    expect(census!.cardShadow).toBe("rgba(0, 0, 0, 0.04) 0px 2px 8px 0px");
    expect(census!.actionRow!.top).toBe("12px");
    expect(census!.actionRow!.right).toBe("12px");
    expect(census!.actionRow!.gap).toBe("8px");
    expect(census!.actionRow!.btnH).toBe(32);
    expect(census!.actionRow!.btnPadX).toBe("12px");
    expect(census!.actionRow!.fontSize).toBe("12px");
    // shadow-md's visible layers at rest (identical on both sites; the
    // lead-layer count diverges by construction — the accepted class).
    expect(census!.actionBtnShadow).toContain("rgba(0, 0, 0, 0.1) 0px 4px 6px -1px");
    expect(census!.actionBtnShadow).toContain("rgba(0, 0, 0, 0.1) 0px 2px 4px -2px");

    // A REAL hover: the card's shadow stays INERT (the inline beats the
    // utility — both sites) while the action row REVEALS (opacity 1).
    const cardLoc = page.locator('div[class*="grid-cols-3"] > div').first();
    await cardLoc.hover();
    await page.waitForTimeout(400);
    const hovered = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      const card = grid!.children[0] as HTMLElement;
      const actionRow = [...card.querySelectorAll("div")].find((d) => {
        const cs = getComputedStyle(d);
        return cs.position === "absolute" && d.children.length > 0 && d.querySelectorAll("button").length >= 1;
      });
      return {
        boxShadow: getComputedStyle(card).boxShadow,
        actionOpacity: actionRow ? getComputedStyle(actionRow).opacity : null,
      };
    });
    expect(hovered.boxShadow).toBe("rgba(0, 0, 0, 0.04) 0px 2px 8px 0px");
    expect(hovered.actionOpacity).toBe("1");
  });
});

// v51 F3 (docs/remediation-plan-v51.md): the savings view's MOBILE
// census at 390 — the goal card's chrome + the view chrome, measured
// live on BOTH sites at byte-parity (READ-ONLY on the reference). The
// card HEIGHT is a data class (the richer seed's 4-chip badge row wraps
// to 52px where the reference's 3 chips fit one 22px row) — never
// pinned; the chrome axes are byte-identical.
test.describe("savings view mobile census at 390 (v51 — plan F3)", () => {
  test("the goal card's chrome + the view chrome (v51 F3)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/savings");
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();

    const census = await page.evaluate(() => {
      // The goal card: the first rounded-xl card below the filter card.
      const cards = [...document.querySelectorAll("div.rounded-xl")].filter(
        (d) => {
          const cs = getComputedStyle(d);
          const r = d.getBoundingClientRect();
          return (
            r.width > 300 &&
            r.width < 380 &&
            r.height > 100 &&
            r.height < 400 &&
            cs.backgroundColor === "rgb(255, 255, 255)" &&
            d.querySelector("p, span")
          );
        },
      ) as HTMLElement[];
      const goal = cards.find((c) => c.querySelector("h4")) ?? null;
      if (!goal) return null;
      const csC = getComputedStyle(goal);
      const rC = goal.getBoundingClientRect();
      const h4 = goal.querySelector("h4") as HTMLElement;
      const sub = [...goal.querySelectorAll("p")].find((p) =>
        /^[A-Za-z]/.test((p.textContent || "").trim()),
      ) as HTMLElement | undefined;
      const amount = [...goal.querySelectorAll("p")].find((p) =>
        /^[\$]?[0-9]/.test((p.textContent || "").trim()),
      ) as HTMLElement | undefined;
      const dot = [...goal.querySelectorAll("div")].find((d) => {
        const r = d.getBoundingClientRect();
        return Math.abs(r.width - 8) < 1 && Math.abs(r.height - 8) < 1;
      }) as HTMLElement | undefined;
      const grid = goal.parentElement as HTMLElement;
      const csG = getComputedStyle(grid);
      // The view chrome: the H1 page title, the count sub, the filter
      // card, the search input.
      const h1 = [...document.querySelectorAll("h1")].find(
        (h) => (h.textContent || "").trim() === "Savings",
      ) as HTMLElement | undefined;
      const subP = [...document.querySelectorAll("p")].find((p) =>
        (p.textContent || "").includes("items ·"),
      ) as HTMLElement | undefined;
      const search = document.querySelector(
        'input[placeholder*="Search" i]',
      ) as HTMLInputElement | null;
      let filterCard = search as HTMLElement | null;
      while (
        filterCard &&
        filterCard.parentElement &&
        !getComputedStyle(filterCard).borderRadius.includes("16")
      )
        filterCard = filterCard.parentElement as HTMLElement | null;
      return {
        card: {
          w: Math.round(rC.width),
          radius: csC.borderRadius,
          pad: csC.padding,
          border: csC.borderTopColor,
          bg: csC.backgroundColor,
          shadow: csC.boxShadow,
        },
        title: {
          fs: getComputedStyle(h4).fontSize,
          fw: getComputedStyle(h4).fontWeight,
          color: getComputedStyle(h4).color,
        },
        sub: sub
          ? {
              fs: getComputedStyle(sub).fontSize,
              color: getComputedStyle(sub).color,
            }
          : null,
        amount: amount
          ? {
              fs: getComputedStyle(amount).fontSize,
              fw: getComputedStyle(amount).fontWeight,
              color: getComputedStyle(amount).color,
            }
          : null,
        dot: dot
          ? {
              bg: getComputedStyle(dot).backgroundColor,
              radius: getComputedStyle(dot).borderRadius,
            }
          : null,
        grid: {
          display: csG.display,
          cols: csG.gridTemplateColumns,
          gap: csG.gap,
        },
        h1: h1
          ? {
              fs: getComputedStyle(h1).fontSize,
              fw: getComputedStyle(h1).fontWeight,
              color: getComputedStyle(h1).color,
            }
          : null,
        viewSub: subP
          ? {
              fs: getComputedStyle(subP).fontSize,
              color: getComputedStyle(subP).color,
            }
          : null,
        filterCard: filterCard
          ? {
              w: Math.round(filterCard.getBoundingClientRect().width),
              radius: getComputedStyle(filterCard).borderRadius,
              pad: getComputedStyle(filterCard).padding,
              bg: getComputedStyle(filterCard).backgroundColor,
            }
          : null,
        search: search
          ? {
              w: Math.round(search.getBoundingClientRect().width),
              h: Math.round(search.getBoundingClientRect().height),
            }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The goal card: radius 12 / pad 20 / the border / white / the
    // reference's own inline shadow family (v28 G3's hover pin shares
    // the string).
    expect(census!.card).toEqual({
      w: 358,
      radius: "12px",
      pad: "20px",
      border: "rgb(229, 231, 227)",
      bg: "rgb(255, 255, 255)",
      shadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px 0px",
    });
    // The H4 16/600 forestDark; the subtitle 14/400 gray; the amount
    // 24/700 in the savings blue rgb(59,126,161).
    expect(census!.title).toEqual({ fs: "16px", fw: "600", color: "rgb(26, 58, 46)" });
    expect(census!.sub).toEqual({ fs: "14px", color: "rgb(107, 114, 128)" });
    expect(census!.amount).toEqual({ fs: "24px", fw: "700", color: "rgb(59, 126, 161)" });
    // The 8×8 accent dot in the savings blue, fully rounded.
    expect(census!.dot).toEqual({ bg: "rgb(59, 126, 161)", radius: "9999px" });
    // The card grid: 1 column, 16px gap (the seed's 2 cards stack).
    expect(census!.grid).toEqual({ display: "grid", cols: "358px", gap: "16px" });
    // The view chrome: the H1 30/700 forestDark; the sub 16 gray; the
    // filter card 358 / radius 16 / pad 24 / white; the search 308×36.
    expect(census!.h1).toEqual({ fs: "30px", fw: "700", color: "rgb(26, 58, 46)" });
    expect(census!.viewSub).toEqual({ fs: "16px", color: "rgb(107, 114, 128)" });
    expect(census!.filterCard).toEqual({
      w: 358,
      radius: "16px",
      pad: "24px",
      bg: "rgb(255, 255, 255)",
    });
    expect(census!.search).toEqual({ w: 308, h: 36 });
    // The clone's superset no-overflow contract at 390.
    expect(census!.docSW).toBe(390);
  });
});

// v52 F2/F3 (docs/remediation-plan-v52.md): the /income and /expenses
// views' MOBILE census at 390 — the header row's reflow (the chip + the
// H1 + the sub + the Add button stacking under the v20 G1 row), the
// filter card's 1-column grid (the search + the select triggers at the
// 52px rhythm), the item grid, and the first card's chrome. Every value
// below was measured live on BOTH sites this session (byte-identical
// unless noted — the card HEIGHT and the count/amount texts are the
// richer seed's documented data class, never pinned).

test.describe("income view mobile census at 390 (v52 — plan F2)", () => {
  test("the header row + filter card + item grid chrome (v52 F2)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();

    const census = await page.evaluate(() => {
      const h1 = [...document.querySelectorAll("h1")].find(
        (x) => (x.textContent || "").trim() === "Income",
      );
      if (!h1) return null;
      // the header row: walk up to the flex row carrying the Add button
      let headRow: HTMLElement | null = h1.closest("div.flex") || h1.parentElement;
      if (!headRow) return null;
      for (let i = 0; i < 4 && headRow.parentElement; i++) {
        if (headRow.querySelector("button")) break;
        headRow = headRow.parentElement as HTMLElement;
      }
      const hrs = headRow!.getBoundingClientRect();
      const csR = getComputedStyle(headRow!);
      const chip = headRow!.querySelector("div.rounded-xl") as HTMLElement | null;
      const addBtn = [...headRow!.querySelectorAll("button")].pop() as HTMLElement | null;
      const sub = [...headRow!.querySelectorAll("p")].find((p) =>
        /items/.test(p.textContent || ""),
      );
      // the filter card: the next rounded sibling with an input
      let filter: HTMLElement | null = null;
      let el: HTMLElement | null = headRow!.nextElementSibling as HTMLElement | null;
      while (el && !filter) {
        if (/rounded/.test(el.className || "") && el.querySelector("input")) filter = el;
        el = el.nextElementSibling as HTMLElement | null;
      }
      const fcs = filter ? getComputedStyle(filter) : null;
      const inner = filter ? (filter.querySelector("div.grid") as HTMLElement | null) : null;
      const ics = inner ? getComputedStyle(inner) : null;
      const search = filter ? (filter.querySelector("input") as HTMLInputElement | null) : null;
      // the first item card: the Salary H4's rounded-xl ancestor in a grid
      const h4 = [...document.querySelectorAll("h4")].find((x) =>
        /Salary/i.test((x.textContent || "").trim()),
      );
      let card: HTMLElement | null = h4
        ? ((h4.closest("div.rounded-xl") as HTMLElement | null) ?? h4.parentElement)
        : null;
      for (let i = 0; card && i < 5; i++) {
        const cs = getComputedStyle(card!.parentElement!);
        if (cs.display === "grid") break;
        card = card!.parentElement as HTMLElement;
      }
      const grid = card ? (card.parentElement as HTMLElement | null) : null;
      const gcs = grid ? getComputedStyle(grid!) : null;
      const ccs = card ? getComputedStyle(card) : null;
      const amount = card
        ? [...card.querySelectorAll("p, span, div")].find(
            (p) =>
              /^[-+]?\$?[\d,]+/.test((p.textContent || "").trim()) &&
              p.children.length <= 1,
          )
        : null;
      return {
        headRow: {
          w: Math.round(hrs.width),
          h: Math.round(hrs.height),
          display: csR.display,
          direction: csR.flexDirection,
          gap: csR.gap,
          mb: csR.marginBottom,
          alignItems: csR.alignItems,
        },
        chip: chip
          ? {
              w: Math.round(chip.getBoundingClientRect().width),
              h: Math.round(chip.getBoundingClientRect().height),
              radius: getComputedStyle(chip).borderRadius,
              bg: (getComputedStyle(chip).backgroundImage ||
                getComputedStyle(chip).backgroundColor),
            }
          : null,
        h1: {
          fs: getComputedStyle(h1).fontSize,
          fw: getComputedStyle(h1).fontWeight,
          color: getComputedStyle(h1).color,
        },
        sub: sub
          ? {
              fs: getComputedStyle(sub).fontSize,
              fw: getComputedStyle(sub).fontWeight,
              color: getComputedStyle(sub).color,
            }
          : null,
        addBtn: addBtn
          ? {
              w: Math.round(addBtn.getBoundingClientRect().width),
              h: Math.round(addBtn.getBoundingClientRect().height),
              radius: getComputedStyle(addBtn).borderRadius,
              bg: (getComputedStyle(addBtn).backgroundImage ||
                getComputedStyle(addBtn).backgroundColor),
              color: getComputedStyle(addBtn).color,
              fs: getComputedStyle(addBtn).fontSize,
              fw: getComputedStyle(addBtn).fontWeight,
              pad: getComputedStyle(addBtn).padding,
            }
          : null,
        filterCard: filter
          ? {
              w: Math.round(filter.getBoundingClientRect().width),
              radius: fcs!.borderRadius,
              pad: fcs!.padding,
              bg: fcs!.backgroundColor,
              border: fcs!.border,
              mb: fcs!.marginBottom,
            }
          : null,
        filterInner: inner
          ? {
              cols: ics!.gridTemplateColumns,
              gap: ics!.gap,
              children: inner.children.length,
              kidYs: [...inner.children].map(
                (c) => Math.round(c.getBoundingClientRect().y),
              ),
            }
          : null,
        search: search
          ? {
              w: Math.round(search.getBoundingClientRect().width),
              h: Math.round(search.getBoundingClientRect().height),
              pad: getComputedStyle(search).padding,
            }
          : null,
        itemGrid: gcs
          ? { display: gcs.display, cols: gcs.gridTemplateColumns, gap: gcs.gap }
          : null,
        firstCard: card
          ? {
              w: Math.round(card.getBoundingClientRect().width),
              radius: ccs!.borderRadius,
              pad: ccs!.padding,
              border: ccs!.border,
              bg: ccs!.backgroundColor,
              shadow: ccs!.boxShadow,
            }
          : null,
        h4: h4
          ? {
              fs: getComputedStyle(h4).fontSize,
              fw: getComputedStyle(h4).fontWeight,
              color: getComputedStyle(h4).color,
            }
          : null,
        amount: amount
          ? {
              fs: getComputedStyle(amount).fontSize,
              fw: getComputedStyle(amount).fontWeight,
              color: getComputedStyle(amount).color,
            }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The header row: the mobile reflow (flex-col, gap 16, mb 32).
    expect(census!.headRow).toEqual({
      w: 358,
      h: 112,
      display: "flex",
      direction: "column",
      gap: "16px",
      mb: "32px",
      alignItems: "flex-start",
    });
    // The gradient chip: 48x48, radius 12, the lime gradient.
    expect(census!.chip!.w).toBe(48);
    expect(census!.chip!.h).toBe(48);
    expect(census!.chip!.radius).toBe("12px");
    expect(census!.chip!.bg).toBe(
      "linear-gradient(135deg, rgb(143, 188, 63), rgb(184, 216, 126))",
    );
    // The H1 + the count sub.
    expect(census!.h1).toEqual({ fs: "30px", fw: "700", color: "rgb(26, 58, 46)" });
    expect(census!.sub).toEqual({ fs: "16px", fw: "400", color: "rgb(107, 114, 128)" });
    // The Add button: 147x36, radius 6, the lime gradient, 14/500.
    expect(census!.addBtn!.w).toBe(147);
    expect(census!.addBtn!.h).toBe(36);
    expect(census!.addBtn!.radius).toBe("6px");
    expect(census!.addBtn!.bg).toBe(
      "linear-gradient(135deg, rgb(143, 188, 63), rgb(184, 216, 126))",
    );
    expect(census!.addBtn!.color).toBe("rgb(255, 255, 255)");
    expect(census!.addBtn!.fs).toBe("14px");
    expect(census!.addBtn!.fw).toBe("500");
    expect(census!.addBtn!.pad).toBe("8px 16px");
    // The filter card + its 1-column grid (3 children at the 52px rhythm).
    expect(census!.filterCard!.w).toBe(358);
    expect(census!.filterCard!.radius).toBe("16px");
    expect(census!.filterCard!.pad).toBe("24px");
    expect(census!.filterCard!.bg).toBe("rgb(255, 255, 255)");
    expect(census!.filterCard!.mb).toBe("24px");
    expect(census!.filterInner!.cols).toBe("308px");
    expect(census!.filterInner!.gap).toBe("16px");
    expect(census!.filterInner!.children).toBe(3);
    expect(census!.filterInner!.kidYs).toEqual([246, 298, 350]);
    // The search: 308x36, the pl-10 pad.
    expect(census!.search!.w).toBe(308);
    expect(census!.search!.h).toBe(36);
    expect(census!.search!.pad).toBe("4px 12px 4px 40px");
    // The item grid: 1 column, gap 16.
    expect(census!.itemGrid!.display).toBe("grid");
    expect(census!.itemGrid!.cols).toBe("358px");
    expect(census!.itemGrid!.gap).toBe("16px");
    // The first card's chrome (the height is data — never pinned).
    expect(census!.firstCard!.w).toBe(358);
    expect(census!.firstCard!.radius).toBe("12px");
    expect(census!.firstCard!.pad).toBe("20px");
    expect(census!.firstCard!.bg).toBe("rgb(255, 255, 255)");
    expect(census!.firstCard!.shadow).toBe("rgba(0, 0, 0, 0.04) 0px 2px 8px 0px");
    // The card's leaves.
    expect(census!.h4).toEqual({ fs: "16px", fw: "600", color: "rgb(26, 58, 46)" });
    expect(census!.amount).toEqual({ fs: "16px", fw: "400", color: "rgb(10, 10, 10)" });
    // The clone's superset no-overflow contract at 390.
    expect(census!.docSW).toBe(390);
  });
});

test.describe("expenses view mobile census at 390 (v52 — plan F3)", () => {
  test("the header row + the 4-child filter grid + the first card (v52 F3)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();

    const census = await page.evaluate(() => {
      const h1 = [...document.querySelectorAll("h1")].find(
        (x) => (x.textContent || "").trim() === "Expenses",
      );
      if (!h1) return null;
      let headRow: HTMLElement | null = h1.closest("div.flex") || h1.parentElement;
      if (!headRow) return null;
      for (let i = 0; i < 4 && headRow.parentElement; i++) {
        if (headRow.querySelector("button")) break;
        headRow = headRow.parentElement as HTMLElement;
      }
      const addBtn = [...headRow!.querySelectorAll("button")].pop() as HTMLElement | null;
      const sub = [...headRow!.querySelectorAll("p")].find((p) =>
        /items/.test(p.textContent || ""),
      );
      let filter: HTMLElement | null = null;
      let el: HTMLElement | null = headRow!.nextElementSibling as HTMLElement | null;
      while (el && !filter) {
        if (/rounded/.test(el.className || "") && el.querySelector("input")) filter = el;
        el = el.nextElementSibling as HTMLElement | null;
      }
      const inner = filter ? (filter.querySelector("div.grid") as HTMLElement | null) : null;
      const ics = inner ? getComputedStyle(inner) : null;
      const triggers = filter
        ? filter.querySelectorAll("button[role=combobox], select").length
        : 0;
      const h4 = [...document.querySelectorAll("h4")].find((x) =>
        /Rent/i.test((x.textContent || "").trim()),
      );
      let card: HTMLElement | null = h4
        ? ((h4.closest("div.rounded-xl") as HTMLElement | null) ?? h4.parentElement)
        : null;
      for (let i = 0; card && i < 5; i++) {
        const cs = getComputedStyle(card!.parentElement!);
        if (cs.display === "grid") break;
        card = card!.parentElement as HTMLElement;
      }
      const ccs = card ? getComputedStyle(card) : null;
      return {
        h1: {
          fs: getComputedStyle(h1).fontSize,
          fw: getComputedStyle(h1).fontWeight,
          color: getComputedStyle(h1).color,
        },
        sub: sub
          ? {
              fs: getComputedStyle(sub).fontSize,
              fw: getComputedStyle(sub).fontWeight,
              color: getComputedStyle(sub).color,
            }
          : null,
        addBtn: addBtn
          ? {
              w: Math.round(addBtn.getBoundingClientRect().width),
              h: Math.round(addBtn.getBoundingClientRect().height),
              bg: (getComputedStyle(addBtn).backgroundImage ||
                getComputedStyle(addBtn).backgroundColor),
            }
          : null,
        filterCard: filter
          ? {
              w: Math.round(filter.getBoundingClientRect().width),
              radius: getComputedStyle(filter).borderRadius,
              pad: getComputedStyle(filter).padding,
            }
          : null,
        filterInner: ics
          ? {
              cols: ics.gridTemplateColumns,
              gap: ics.gap,
              children: inner!.children.length,
              triggers,
            }
          : null,
        firstCard: card
          ? {
              w: Math.round(card.getBoundingClientRect().width),
              radius: ccs!.borderRadius,
              pad: ccs!.padding,
              bg: ccs!.backgroundColor,
              shadow: ccs!.boxShadow,
            }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The H1 + the count sub.
    expect(census!.h1).toEqual({ fs: "30px", fw: "700", color: "rgb(26, 58, 46)" });
    expect(census!.sub).toEqual({ fs: "16px", fw: "400", color: "rgb(107, 114, 128)" });
    // The Add button: 155x36, the orange gradient.
    expect(census!.addBtn!.w).toBe(155);
    expect(census!.addBtn!.h).toBe(36);
    expect(census!.addBtn!.bg).toBe(
      "linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))",
    );
    // The filter card + the 4-child grid (the payment-method family).
    expect(census!.filterCard!.w).toBe(358);
    expect(census!.filterCard!.radius).toBe("16px");
    expect(census!.filterCard!.pad).toBe("24px");
    expect(census!.filterInner!.cols).toBe("308px");
    expect(census!.filterInner!.gap).toBe("16px");
    expect(census!.filterInner!.children).toBe(4);
    expect(census!.filterInner!.triggers).toBe(3);
    // The first card's chrome.
    expect(census!.firstCard!.w).toBe(358);
    expect(census!.firstCard!.radius).toBe("12px");
    expect(census!.firstCard!.pad).toBe("20px");
    expect(census!.firstCard!.shadow).toBe("rgba(0, 0, 0, 0.04) 0px 2px 8px 0px");
    // The clone's superset no-overflow contract at 390.
    expect(census!.docSW).toBe(390);
  });
});

// v54 F1 (docs/remediation-plan-v54.md): the savings goal-card's
// INTERNALS at 390 — the badge chip row + the date/payment footer —
// the internals BEYOND the v51 F3 chrome pin, measured live on BOTH
// sites at byte-parity (READ-ONLY on the reference). The chip COUNT
// (the reference's 3 vs the seed's 4 — the Recurring chip) and the
// row HEIGHT (22 vs 52, the wrap) are DATA classes — never pinned;
// the chip + footer CHROME axes are byte-identical (the "monthly"
// chip's w 78 on BOTH sites is the strongest width-parity signal).
test.describe("savings goal-card internals census at 390 (v54 — plan F1)", () => {
  test("the badge row + the chips + the footer (v54 F1)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/savings");
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();

    const census = await page.evaluate(() => {
      // The goal card: the Emergency Fund h4's rounded-xl ancestor in
      // the grid (the v51 F3 walk).
      const h4 = [...document.querySelectorAll("h4")].find((x) =>
        /Emergency Fund/i.test((x.textContent || "").trim()),
      );
      if (!h4) return null;
      let card: HTMLElement | null =
        (h4.closest("div.rounded-xl") as HTMLElement | null) ?? h4.parentElement;
      for (let i = 0; card && i < 5; i++) {
        const cs = getComputedStyle(card!.parentElement!);
        if (cs.display === "grid") break;
        card = card!.parentElement as HTMLElement;
      }
      if (!card) return null;
      // The header row (the dot + h4 line): the h4's direct parent.
      const hdrRow = h4.parentElement as HTMLElement;
      const hcs = getComputedStyle(hdrRow);
      const dot = [...hdrRow.querySelectorAll("div")].find(
        (d) => d.getBoundingClientRect().width < 12,
      ) as HTMLElement | null;
      // The badge row: the flex-wrap chip row (the chips are inline-flex
      // SOURCE classes but compute to "flex" — flex items are blockified
      // per the CSS spec; the probe's OR-clause lesson).
      const badgeRow = [...card.querySelectorAll("div")].find((d) => {
        const cs = getComputedStyle(d);
        return (
          cs.display === "flex" &&
          cs.flexWrap === "wrap" &&
          d.children.length >= 2 &&
          [...d.children].every(
            (c) => getComputedStyle(c as HTMLElement).display === "flex",
          )
        );
      }) as HTMLElement | null;
      if (!badgeRow) return null;
      const brcs = getComputedStyle(badgeRow);
      const chipGrab = (el: Element) => {
        const cs = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        const icon = el.querySelector("svg");
        return {
          text: (el.textContent || "").trim(),
          w: Math.round(r.width),
          h: Math.round(r.height),
          radius: cs.borderRadius,
          pad: cs.padding,
          fs: cs.fontSize,
          fw: cs.fontWeight,
          icon: icon
            ? {
                w: Math.round(icon.getBoundingClientRect().width),
                h: Math.round(icon.getBoundingClientRect().height),
                mr: getComputedStyle(icon).marginRight,
              }
            : null,
        };
      };
      const chips = [...badgeRow.children].map(chipGrab);
      // The footer: the LAST justify-between direct child WITHOUT an
      // h4 (the header row also carries justify-between — the v54
      // probe-debug lesson).
      const footer = [...card.children]
        .filter((d) => {
          const cs = getComputedStyle(d as HTMLElement);
          return (
            cs.display === "flex" &&
            cs.justifyContent === "space-between" &&
            !d.querySelector("h4")
          );
        })
        .pop() as HTMLElement | undefined;
      if (!footer) return null;
      const fcs = getComputedStyle(footer);
      const dateSpan = footer.children[0] as HTMLElement;
      const dscs = getComputedStyle(dateSpan);
      const dateIcon = dateSpan.querySelector("svg");
      return {
        hdrRow: {
          display: hcs.display,
          gap: hcs.gap,
          mb: hcs.marginBottom,
          alignItems: hcs.alignItems,
        },
        dot: dot
          ? {
              w: Math.round(dot.getBoundingClientRect().width),
              h: Math.round(dot.getBoundingClientRect().height),
              radius: getComputedStyle(dot).borderRadius,
              bg: getComputedStyle(dot).backgroundColor,
            }
          : null,
        badgeRow: {
          display: brcs.display,
          gap: brcs.gap,
          wrap: brcs.flexWrap,
          mb: brcs.marginBottom,
          n: badgeRow.children.length,
        },
        firstChip: chips[0] ?? null,
        monthlyChip: chips.find((c) => c.text === "monthly") ?? null,
        activeChip: chips.find((c) => c.text === "active") ?? null,
        footer: {
          display: fcs.display,
          justify: fcs.justifyContent,
          fs: fcs.fontSize,
          color: fcs.color,
          h: Math.round(footer.getBoundingClientRect().height),
        },
        dateSpan: {
          display: dscs.display,
          gap: dscs.gap,
          fs: dscs.fontSize,
          color: dscs.color,
          icon: dateIcon
            ? {
                w: Math.round(dateIcon.getBoundingClientRect().width),
                h: Math.round(dateIcon.getBoundingClientRect().height),
                color: getComputedStyle(dateIcon).color,
              }
            : null,
        },
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The header row (the dot + h4 line).
    expect(census!.hdrRow).toEqual({
      display: "flex",
      gap: "8px",
      mb: "4px",
      alignItems: "center",
    });
    // The dot: 8x8, the savings teal accent.
    expect(census!.dot).toEqual({
      w: 8,
      h: 8,
      radius: "9999px",
      bg: "rgb(59, 126, 161)",
    });
    // The badge row: flex / wrap / gap 8 / mb 12 (the chip COUNT is a
    // data class — the reference's 3 vs the seed's 4).
    expect(census!.badgeRow).toEqual({
      display: "flex",
      gap: "8px",
      wrap: "wrap",
      mb: "12px",
      n: 4,
    });
    // The FIRST chip (the classification chip, icon-bearing):
    // h 22 / radius 6 / pad 2px 10px / 12/600 / the 12x12 icon mr 4.
    expect(census!.firstChip!.h).toBe(22);
    expect(census!.firstChip!.radius).toBe("6px");
    expect(census!.firstChip!.pad).toBe("2px 10px");
    expect(census!.firstChip!.fs).toBe("12px");
    expect(census!.firstChip!.fw).toBe("600");
    expect(census!.firstChip!.icon).toEqual({ w: 12, h: 12, mr: "4px" });
    // The MONTHLY chip: w 78 on BOTH sites (the byte-parity width
    // proof — the same text at the same chrome) / NO icon.
    expect(census!.monthlyChip).toMatchObject({
      w: 78,
      h: 22,
      radius: "6px",
      pad: "2px 10px",
      fs: "12px",
      fw: "600",
      icon: null,
    });
    // The ACTIVE chip: w 63 on BOTH sites / NO icon.
    expect(census!.activeChip).toMatchObject({
      w: 63,
      h: 22,
      radius: "6px",
      pad: "2px 10px",
      fs: "12px",
      fw: "600",
      icon: null,
    });
    // The footer row: 12/rgb(107,114,128)/h 16.
    expect(census!.footer).toEqual({
      display: "flex",
      justify: "space-between",
      fs: "12px",
      color: "rgb(107, 114, 128)",
      h: 16,
    });
    // The date span: flex gap 4 + the 12x12 calendar icon at gray.
    expect(census!.dateSpan).toEqual({
      display: "flex",
      gap: "4px",
      fs: "12px",
      color: "rgb(107, 114, 128)",
      icon: { w: 12, h: 12, color: "rgb(107, 114, 128)" },
    });
    // The clone's superset no-overflow contract at 390.
    expect(census!.docSW).toBe(390);
  });
});

// ---------------------------------------------------------------------------
// v57 — plan F1: the items-card FOOTER + BADGE-ROW census at desktop 1280.
// The session-134 v57 queue's own standing-check suggestion (the items
// view's 1280 state — the v56 pair covered the dashboard + networth). The
// v57 VLM pair (income + expenses) came back CLEAN after DOM arbitration:
// the footer chrome and the badge-row chrome are byte-identical on both
// sites — only the DATA differs (the payment-method chips are conditional
// renders; the clone's Recurring superset badge wraps the row). This pin
// locks the measured chrome.
// ---------------------------------------------------------------------------

test.describe("items card footer + badge census at 1280 (v57 — plan F1)", () => {
  test("the income card's footer row + badge chrome (v57 F1a)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/income");
    await expect(page.getByText("Freelance").first()).toBeVisible();

    const census = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement;
      const cardCs = getComputedStyle(card);
      // The badge row: the DIRECT child with the flex-wrap class.
      const badgeRow = [...card.children].find(
        (c) => typeof c.className === "string" && /flex-wrap/.test(c.className),
      ) as HTMLElement | undefined;
      // The footer row: the LAST direct child (the date + payment row).
      const footer = card.children[card.children.length - 1] as HTMLElement;
      const fcs = getComputedStyle(footer);
      const spanGrab = (el: Element) => {
        const cs = getComputedStyle(el);
        const icon = el.querySelector("svg");
        return {
          display: cs.display,
          gap: cs.gap,
          fs: cs.fontSize,
          color: cs.color,
          text: (el.textContent || "").trim().slice(0, 24),
          icon: icon
            ? {
                w: Math.round(icon.getBoundingClientRect().width),
                h: Math.round(icon.getBoundingClientRect().height),
                color: getComputedStyle(icon).color,
              }
            : null,
        };
      };
      const badgeGrab = (el: Element) => {
        const cs = getComputedStyle(el);
        const icon = el.querySelector("svg");
        return {
          text: (el.textContent || "").trim().slice(0, 16),
          display: cs.display,
          alignItems: cs.alignItems,
          radius: cs.borderRadius,
          pad: cs.padding,
          fs: cs.fontSize,
          fw: cs.fontWeight,
          h: Math.round(el.getBoundingClientRect().height),
          iconW: icon ? Math.round(icon.getBoundingClientRect().width) : null,
        };
      };
      const bcs = badgeRow ? getComputedStyle(badgeRow) : null;
      return {
        card: {
          w: Math.round(card.getBoundingClientRect().width),
          pad: cardCs.padding,
          radius: cardCs.borderRadius,
        },
        footer: {
          display: fcs.display,
          alignItems: fcs.alignItems,
          justify: fcs.justifyContent,
          fs: fcs.fontSize,
          color: fcs.color,
          h: Math.round(footer.getBoundingClientRect().height),
          childCount: footer.children.length,
          children: [...footer.children].map(spanGrab),
        },
        badgeRow: bcs
          ? {
              display: bcs.display,
              wrap: bcs.flexWrap,
              gap: bcs.gap,
              mb: bcs.marginBottom,
              h: Math.round(badgeRow!.getBoundingClientRect().height),
              badgeCount: badgeRow!.children.length,
              texts: [...badgeRow!.children].map((b) => (b.textContent || "").trim()),
            }
          : null,
        badges: badgeRow ? [...badgeRow.children].map(badgeGrab) : null,
      };
    });
    expect(census).not.toBeNull();

    // The footer row's chrome — measured byte-identical on BOTH sites
    // (the reference: flex justify-between 12px rgb(107,114,128) h 16).
    expect(census!.footer).toMatchObject({
      display: "flex",
      alignItems: "center",
      justify: "space-between",
      fs: "12px",
      color: "rgb(107, 114, 128)",
      h: 16,
    });
    // The two-children conditional render: the date span + the
    // payment-method span (the Freelance card carries PayPal — the
    // reference's own income card renders the same two-child structure
    // with its "Bank Account" chip).
    expect(census!.footer.childCount).toBe(2);
    expect(census!.footer.children[0]).toMatchObject({
      display: "flex",
      gap: "4px",
      fs: "12px",
      color: "rgb(107, 114, 128)",
      icon: { w: 12, h: 12, color: "rgb(107, 114, 128)" },
    });
    expect(census!.footer.children[1]).toMatchObject({
      display: "flex",
      gap: "4px",
      fs: "12px",
      text: "PayPal",
      icon: { w: 12, h: 12 },
    });

    // The badge row's chrome — measured byte-identical on BOTH sites
    // (flex wrap, 8px gap, 12px bottom margin).
    expect(census!.badgeRow).toEqual({
      display: "flex",
      wrap: "wrap",
      gap: "8px",
      mb: "12px",
      h: 22,
      badgeCount: 3,
      texts: ["want", "monthly", "active"],
    });
    // Every badge's own chrome (the reference's: flex center, 6px radius,
    // 2px 10px pad, 12px/600, h 22 — the classification COLORS are locked
    // by badge-colors.spec.ts; this pin locks the GEOMETRY).
    for (const b of census!.badges!) {
      expect(b).toMatchObject({
        display: "flex",
        alignItems: "center",
        radius: "6px",
        pad: "2px 10px",
        fs: "12px",
        fw: "600",
        h: 22,
      });
    }
    expect(census!.badges![0].iconW).toBe(12);

    // The card chrome control (the v45 F1a pin's own values — unchanged).
    expect(census!.card).toEqual({ w: 309, pad: "20px", radius: "12px" });
  });

  test("the expenses grid + the first card's footer + the wrapped badge row (v57 F1b)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    await expect(page.getByText("Entertainment").first()).toBeVisible();

    const census = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const gcs = getComputedStyle(grid);
      const card = grid.children[0] as HTMLElement;
      const cardCs = getComputedStyle(card);
      const badgeRow = [...card.children].find(
        (c) => typeof c.className === "string" && /flex-wrap/.test(c.className),
      ) as HTMLElement | undefined;
      const footer = card.children[card.children.length - 1] as HTMLElement;
      const fcs = getComputedStyle(footer);
      const bcs = badgeRow ? getComputedStyle(badgeRow) : null;
      return {
        grid: {
          w: Math.round(grid.getBoundingClientRect().width),
          gap: gcs.gap,
          childCount: grid.children.length,
          template: gcs.gridTemplateColumns,
        },
        card: {
          w: Math.round(card.getBoundingClientRect().width),
          pad: cardCs.padding,
          radius: cardCs.borderRadius,
        },
        footer: {
          display: fcs.display,
          justify: fcs.justifyContent,
          fs: fcs.fontSize,
          color: fcs.color,
          h: Math.round(footer.getBoundingClientRect().height),
          childCount: footer.children.length,
          paymentText: footer.children[1]
            ? (footer.children[1].textContent || "").trim().slice(0, 24)
            : null,
        },
        badgeRow: bcs
          ? {
              display: bcs.display,
              wrap: bcs.flexWrap,
              gap: bcs.gap,
              h: Math.round(badgeRow!.getBoundingClientRect().height),
              badgeCount: badgeRow!.children.length,
              texts: [...badgeRow!.children].map((b) => (b.textContent || "").trim()),
            }
          : null,
      };
    });
    expect(census).not.toBeNull();

    // The grid: the reference's own 3-col template (960 wide, 16px gap —
    // each column ~=309.33px) with the e2e seed's 3 expense cards.
    expect(census!.grid.w).toBe(960);
    expect(census!.grid.gap).toBe("16px");
    expect(census!.grid.childCount).toBe(3);
    expect(census!.grid.template).toMatch(/^309\.\d+px 309\.\d+px 309\.\d+px$/);

    // The first card (Entertainment — the date-DESC order): the same
    // chrome as the income card (the v45 control).
    expect(census!.card).toEqual({ w: 309, pad: "20px", radius: "12px" });

    // The footer: the same chrome + the payment chip (every e2e expense
    // carries a payment method — the reference's own items do not, the
    // documented data class; the conditional render is the point).
    expect(census!.footer).toMatchObject({
      display: "flex",
      justify: "space-between",
      fs: "12px",
      color: "rgb(107, 114, 128)",
      h: 16,
      childCount: 2,
    });
    expect(census!.footer.paymentText).toMatch(/^(Bank Transfer|Credit Card)$/);

    // The wrapped badge row: the clone's Recurring superset badge makes
    // 4 badges — the row WRAPS to h 52 (the measured two-line layout:
    // 22 + 8 gap + 22; the reference's 3-badge rows stay h 22 — the
    // wrap is the data class, the row chrome is identical).
    expect(census!.badgeRow).toEqual({
      display: "flex",
      wrap: "wrap",
      gap: "8px",
      h: 52,
      badgeCount: 4,
      texts: ["want", "monthly", "Recurring", "active"],
    });
  });
});

// ---------------------------------------------------------------------------
// v58 — plan F1: the savings goal-card census at desktop 1280. The
// session-137 v58 queue's own first suggestion (the items family's
// remaining view — the v57 pair covered income + expenses). The v58 VLM
// pair (/savings) came back CLEAN after DOM arbitration: the footer chrome
// and the badge-row chrome are byte-identical on both sites — only the
// DATA differs (the reference's savings item carries no paymentMethod so
// its footer renders one child; its item is classified "need" [red] while
// the clone's are "savings" [green] — the classification VALUE is the
// data class, the color maps stay locked by badge-colors.spec.ts; the
// clone's Recurring superset badge wraps the row). This pin locks the
// measured chrome on the third view.
// ---------------------------------------------------------------------------

test.describe("the savings goal-card census at 1280 (v58 — plan F1)", () => {
  test("the savings grid + the goal card's footer + the wrapped badge row (v58 F1)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    await expect(page.getByText("Investments").first()).toBeVisible();

    const census = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const gcs = getComputedStyle(grid);
      const card = grid.children[0] as HTMLElement;
      const cardCs = getComputedStyle(card);
      // The badge row: the DIRECT child with the flex-wrap class (the v57
      // P1.1 lesson — a nested querySelectorAll filter misses it).
      const badgeRow = [...card.children].find(
        (c) => typeof c.className === "string" && /flex-wrap/.test(c.className),
      ) as HTMLElement | undefined;
      // The footer row: the LAST direct child (the date + payment row).
      const footer = card.children[card.children.length - 1] as HTMLElement;
      const fcs = getComputedStyle(footer);
      const spanGrab = (el: Element) => {
        const cs = getComputedStyle(el);
        const icon = el.querySelector("svg");
        return {
          display: cs.display,
          gap: cs.gap,
          fs: cs.fontSize,
          color: cs.color,
          text: (el.textContent || "").trim().slice(0, 24),
          icon: icon
            ? {
                w: Math.round(icon.getBoundingClientRect().width),
                h: Math.round(icon.getBoundingClientRect().height),
                color: getComputedStyle(icon).color,
              }
            : null,
        };
      };
      const badgeGrab = (el: Element) => {
        const cs = getComputedStyle(el);
        const icon = el.querySelector("svg");
        return {
          text: (el.textContent || "").trim().slice(0, 16),
          display: cs.display,
          alignItems: cs.alignItems,
          radius: cs.borderRadius,
          pad: cs.padding,
          fs: cs.fontSize,
          fw: cs.fontWeight,
          h: Math.round(el.getBoundingClientRect().height),
          iconW: icon ? Math.round(icon.getBoundingClientRect().width) : null,
        };
      };
      const bcs = badgeRow ? getComputedStyle(badgeRow) : null;
      return {
        grid: {
          w: Math.round(grid.getBoundingClientRect().width),
          gap: gcs.gap,
          childCount: grid.children.length,
          template: gcs.gridTemplateColumns,
        },
        card: {
          w: Math.round(card.getBoundingClientRect().width),
          pad: cardCs.padding,
          radius: cardCs.borderRadius,
        },
        footer: {
          display: fcs.display,
          alignItems: fcs.alignItems,
          justify: fcs.justifyContent,
          fs: fcs.fontSize,
          color: fcs.color,
          h: Math.round(footer.getBoundingClientRect().height),
          childCount: footer.children.length,
          children: [...footer.children].map(spanGrab),
        },
        badgeRow: bcs
          ? {
              display: bcs.display,
              wrap: bcs.flexWrap,
              gap: bcs.gap,
              mb: bcs.marginBottom,
              h: Math.round(badgeRow!.getBoundingClientRect().height),
              badgeCount: badgeRow!.children.length,
              texts: [...badgeRow!.children].map((b) => (b.textContent || "").trim()),
            }
          : null,
        badges: badgeRow ? [...badgeRow.children].map(badgeGrab) : null,
      };
    });
    expect(census).not.toBeNull();

    // The grid: the reference's own 3-col template (960 wide, 16px gap —
    // each column ~=309.33px) with the e2e seed's 2 savings goal cards
    // (the reference's own savings view carries 1 — the seed class).
    expect(census!.grid.w).toBe(960);
    expect(census!.grid.gap).toBe("16px");
    expect(census!.grid.childCount).toBe(2);
    expect(census!.grid.template).toMatch(/^309\.\d+px 309\.\d+px 309\.\d+px$/);

    // The first goal card (Investments — the date-DESC order): the same
    // chrome as the income/expense cards (the v45 control).
    expect(census!.card).toEqual({ w: 309, pad: "20px", radius: "12px" });

    // The footer row's chrome — measured byte-identical on BOTH sites
    // (the reference: flex justify-between 12px rgb(107,114,128) h 16 —
    // its own savings footer renders the one-child date-only form; the
    // two-children conditional render is the v57 contract measured on
    // the third view: the Investments card carries the "Brokerage"
    // paymentMethod, the same structure the reference's own income card
    // renders with its "Bank Account" chip).
    expect(census!.footer).toMatchObject({
      display: "flex",
      alignItems: "center",
      justify: "space-between",
      fs: "12px",
      color: "rgb(107, 114, 128)",
      h: 16,
      childCount: 2,
    });
    expect(census!.footer.children[0]).toMatchObject({
      display: "flex",
      gap: "4px",
      fs: "12px",
      color: "rgb(107, 114, 128)",
      icon: { w: 12, h: 12, color: "rgb(107, 114, 128)" },
    });
    expect(census!.footer.children[0].text).toMatch(/^Oct \d+, 2026$/);
    expect(census!.footer.children[1]).toMatchObject({
      display: "flex",
      gap: "4px",
      fs: "12px",
      text: "Brokerage",
      icon: { w: 12, h: 12 },
    });

    // The wrapped badge row: the clone's Recurring superset badge makes
    // 4 badges — the row WRAPS to h 52 (the measured two-line layout:
    // 22 + 8 gap + 22; the reference's 3-badge row [need, monthly,
    // active] stays h 22 — the classification VALUE and the badge COUNT
    // are the data classes, the row chrome is identical).
    expect(census!.badgeRow).toEqual({
      display: "flex",
      wrap: "wrap",
      gap: "8px",
      mb: "12px",
      h: 52,
      badgeCount: 4,
      texts: ["savings", "monthly", "Recurring", "active"],
    });
    // Every badge's own chrome (flex center, 6px radius, 2px 10px pad,
    // 12px/600, h 22 — the classification COLORS are locked by
    // badge-colors.spec.ts; this pin locks the GEOMETRY).
    for (const b of census!.badges!) {
      expect(b).toMatchObject({
        display: "flex",
        alignItems: "center",
        radius: "6px",
        pad: "2px 10px",
        fs: "12px",
        fw: "600",
        h: 22,
      });
    }
    expect(census!.badges![0].iconW).toBe(12);
  });
});

// v74 F4 (docs/remediation-plan-v74.md): the savings goal-card's
// INTERIOR-TEXT chrome at 1280 + the hidden app-shell h1 — the re-run
// cycle's OLDEST candidate (the v58-era savings pair's second re-run,
// after v65) surfaced the never-pinned axes: the h4 title + the amount
// are pinned at 390 ONLY (the v51 F3 pin covers fs/fw/color; the lh and
// the 1280 state never), and the HIDDEN first-in-DOM h1 "ZeroBalance"
// (the app-shell mobile header's h1, sidebar.tsx:234, text-xl font-bold,
// display:none at 1280) is documented in the v65 notes but pinned
// nowhere. Measured BYTE-IDENTICAL on BOTH sites via arbit-v74.sh (the
// both-sides /savings census at 1280). Read-only (the logged-in
// storageState, the seeded Investments card — the v58 pin's own style).
test.describe("savings goal-card interior-text + hidden app-shell h1 census at 1280 (v74 — plan F4)", () => {
  test("the h4 title + amount chrome (the lh family) + the hidden ZeroBalance h1 (v74 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    await expect(page.getByText("Investments").first()).toBeVisible();

    const census = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement;
      // The h4 title (the card's colored-dot row heading) + the amount
      // (the text-2xl p — formatMoney's dollar-prefixed string, matched
      // by CLASS never text: the v64 dollar rule's census corollary).
      const h4 = card.querySelector("h4");
      const amtP = [...card.querySelectorAll("p")].find(
        (p) => typeof p.className === "string" && /text-2xl/.test(p.className),
      );
      // The hidden first-in-DOM h1 "ZeroBalance" — the app-shell mobile
      // topbar's h1 (the header carries md:hidden; at 1280 the subtree is
      // out of layout — the h1 keeps its OWN display (block) but renders
      // ZERO-SIZE (w 0 / h 0 — the v65 note's "hidden zero-size"), while
      // getComputedStyle still reports its computed family).
      const hiddenH1 = document.querySelector("h1");
      const grab = (el: Element | null | undefined, extra: string[] = []) => {
        if (!el) return null;
        const cs = getComputedStyle(el);
        const out: Record<string, unknown> = {
          fs: cs.fontSize,
          fw: cs.fontWeight,
          color: cs.color,
        };
        if (extra.includes("lh")) out.lh = cs.lineHeight;
        if (extra.includes("text")) out.text = (el.textContent || "").trim().slice(0, 20);
        return out;
      };
      return {
        cardTitle: grab(h4, ["lh"]),
        cardAmount: grab(amtP, ["lh"]),
        hiddenH1: grab(hiddenH1, ["text"]),
        hiddenH1Box: hiddenH1
          ? {
              w: Math.round(hiddenH1.getBoundingClientRect().width),
              h: Math.round(hiddenH1.getBoundingClientRect().height),
              display: getComputedStyle(hiddenH1).display,
            }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The h4 title's full chrome at 1280 — the v51 pin's 390 family
    // (fs/fw/color) plus the never-pinned lh, byte-identical on both
    // sides' savings goal cards.
    expect(census!.cardTitle).toEqual({
      fs: "16px",
      fw: "600",
      lh: "24px",
      color: "rgb(26, 58, 46)",
    });
    // The amount's full chrome at 1280 — the savings blue accent
    // (rgb(59,126,161)), the 24/700/32 family.
    expect(census!.cardAmount).toEqual({
      fs: "24px",
      fw: "700",
      lh: "32px",
      color: "rgb(59, 126, 161)",
    });
    // The hidden first-in-DOM h1 "ZeroBalance" — the app-shell mobile
    // topbar's h1: at 1280 the md:hidden header puts the subtree out of
    // layout, so the h1 renders ZERO-SIZE (w 0 / h 0 — the v65 note's
    // "hidden zero-size" mechanism; its own display stays "block" — the
    // VISIBLE h1 is the v65-pinned contract), its computed chrome
    // 20px/700/forestDark, byte-identical on both sides (the
    // v65-documented surface, pinned for the first time).
    expect(census!.hiddenH1).toEqual({
      text: "ZeroBalance",
      fs: "20px",
      fw: "700",
      color: "rgb(26, 58, 46)",
    });
    expect(census!.hiddenH1Box).toEqual({ w: 0, h: 0, display: "block" });
    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);
  });
});

// v70 F4 (docs/remediation-plan-v70.md): the EXPENSES view's filter card
// at desktop 1280 — the last never-census'd filter-card variant (the v38
// S2 pin covered the /savings instance, the v64 pin the /income variant,
// the v52 F3 pin the expenses card's MOBILE 390 state only; the v37 S3
// payment-trigger pin asserts the trigger's 216×36 geometry alone). The
// expenses DESKTOP variant differs structurally from both siblings: the
// `lg:grid-cols-4` grid with the search NOT spanning (1 col, 216 wide —
// vs the income/savings 447 two-col span) and the 4th child — the third
// payment-method combobox. Measured BYTE-IDENTICAL on BOTH sites via
// arbit-v70.sh (the v70 items-pair re-run): the card 960×86, the search
// 216×36 with the asymmetric 40px left pad, the 4-track 215.5px grid,
// the three 216×36 comboboxes at 14px. This pin locks the computed
// geometry. Read-only (the logged-in storageState, no fixture flow).
test.describe("expenses view filter-card census at 1280 (v70 — plan F4)", () => {
  test("the filter-card computed census at 1280 — the search NOT spanning, the 4-child grid, the 3 comboboxes (v70 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();

    const census = await page.evaluate(() => {
      const search = document.querySelector<HTMLInputElement>(
        "input[placeholder^='Search expense']",
      );
      if (!search) return null;
      const card = search.closest("div.rounded-2xl") as HTMLElement | null;
      if (!card) return null;
      const ccs = getComputedStyle(card);
      const scs = getComputedStyle(search);
      // the inner grid: the card's direct grid child
      const inner = [...card.children].find(
        (c) => getComputedStyle(c).display === "grid",
      );
      const ics = inner ? getComputedStyle(inner) : null;
      return {
        card: {
          w: Math.round(card.getBoundingClientRect().width),
          h: Math.round(card.getBoundingClientRect().height),
          pad: ccs.padding,
          radius: ccs.borderRadius,
          bg: ccs.backgroundColor,
          border: ccs.borderTopColor,
          mb: ccs.marginBottom,
        },
        search: {
          w: Math.round(search.getBoundingClientRect().width),
          h: Math.round(search.getBoundingClientRect().height),
          pad: scs.padding,
          radius: scs.borderRadius,
          border: scs.borderTopColor,
        },
        innerGrid: ics
          ? {
              cols: ics.gridTemplateColumns,
              gap: ics.gap,
              childCount: inner!.children.length,
            }
          : null,
        comboboxes: inner
          ? [...inner.querySelectorAll<HTMLElement>('[role="combobox"]')].map(
              (c) => ({
                w: Math.round(c.getBoundingClientRect().width),
                h: Math.round(c.getBoundingClientRect().height),
                fs: getComputedStyle(c).fontSize,
                text: (c.textContent || "").trim().slice(0, 22),
              }),
            )
          : null,
      };
    });
    expect(census).not.toBeNull();

    // The card chrome — measured byte-identical on BOTH sites (the same
    // 960-wide [the rail 256 + the content column 1024 − the p-8 64]
    // 86-tall [24 pad + 36 control + 24 pad + the 2px borders] card as
    // the income/savings variants — the shared component).
    expect(census!.card).toEqual({
      w: 960,
      h: 86,
      pad: "24px",
      radius: "16px",
      bg: "rgb(255, 255, 255)",
      border: "rgb(229, 231, 227)",
      mb: "24px",
    });

    // The search input: 216×36 — the 1-COL span (the expenses variant's
    // defining difference: the search does NOT span 2 columns here, so
    // 215.5px rounds to 216 via offsetWidth) with the same asymmetric
    // 40px left pad (the search icon's room).
    expect(census!.search).toEqual({
      w: 216,
      h: 36,
      pad: "4px 12px 4px 40px",
      radius: "6px",
      border: "rgb(229, 229, 229)",
    });

    // The inner grid: 4 tracks × 215.5px, 16px gap, 4 children (the
    // search wrapper [1 col] + the three comboboxes).
    expect(census!.innerGrid).toEqual({
      cols: "215.5px 215.5px 215.5px 215.5px",
      gap: "16px",
      childCount: 4,
    });

    // The comboboxes: 216×36 each at 14px — the THIRD one is the
    // payment-method filter (the expenses variant's extra child).
    expect(census!.comboboxes).toHaveLength(3);
    for (const combo of census!.comboboxes!) {
      expect(combo).toMatchObject({ w: 216, h: 36, fs: "14px" });
    }
    expect(census!.comboboxes![0].text).toBe("All Categories");
    expect(census!.comboboxes![1].text).toBe("All Frequencies");
    expect(census!.comboboxes![2].text).toBe("All Payment Methods");
  });
});

// v71 F4+F5 (docs/remediation-plan-v71.md): the item-card SUBTITLE-P
// conditional render — the v71 NEW-pair program's arbitration discovery.
// The reference's Miscellaneous/Investments expense cards (EMPTY
// subcategory) render NO subtitle P at all (titleRow h 28, card h 180 —
// the arithmetic: 20 pad + 28 titleRow + 12 mb + 32 amount + 16 mb + 22
// badge + 12 mb + 16 footer + 20 pad + 2 border), while its Netflix/Rent
// cards (WITH subcategory) render the P (h 20, fs 14px, lh 20px, gray)
// with titleRow h 48 — the reference CONDITIONALLY RENDERS the subtitle P
// on the non-empty value. The clone's item-card rendered it
// unconditionally (`{item.subcategory ?? ""}`) — a user-created
// empty-subcategory item carried a 20px EMPTY BLOCK. The v52
// details-sheet idiom applied to the card. The dev seed carries no
// empty-subcategory items, so the F4 fixture creates one through the Add
// Expense flow (defaults: need + monthly + active = 3 badges, recurring
// OFF — the same badge family as the reference's Miscellaneous card);
// the cleanup rides the expense card's Edit dialog → Delete → the inline
// confirm (the superset delete path — expense cards carry no kebab).
test.describe("item-card subtitle-P conditional render at 390 (v71 — plan F4)", () => {
  test("an empty-subcategory expense card renders NO subtitle P (titleRow 28, card h 180)", async ({ page }) => {
    // 390 viewport FIRST: the 1-col grid gives every card its own row →
    // the probe card's height is its NATURAL height (the grid STRETCH
    // governs only same-row siblings — the v67/v70 lesson).
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();

    // --- create the probe: an expense with NO subcategory (the field
    // stays empty — the Add dialog's default form state).
    await page.getByRole("button", { name: "Add Expense" }).click();
    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    await page.getByLabel("Amount").fill("10.00");
    await page.getByLabel("Category", { exact: true }).fill("Probe NoSub");
    // Subcategory intentionally left EMPTY. The classification/frequency/
    // status defaults (need / monthly / active) match the reference's own
    // Miscellaneous card's badge family; recurring stays OFF.
    await page.getByRole("button", { name: "Save Item" }).click();
    await expect(dialog).toBeHidden();

    const probe = page.locator("div.rounded-xl").filter({ hasText: "Probe NoSub" }).first();
    await expect(probe).toBeVisible();

    const census = await probe.evaluate((card) => {
      // the title row: the card's flex child carrying the h4
      const titleRow = [...card.children].find(
        (ch) =>
          getComputedStyle(ch).display.includes("flex") &&
          ch.querySelector("h4") &&
          (ch.textContent || "").trim().length > 0,
      ) as HTMLElement | undefined;
      if (!titleRow) return null;
      const h4 = titleRow.querySelector("h4")!;
      // the subtitle P: the P child of the h4's grandparent flex-1 block
      const flex1 = h4.parentElement!.parentElement!;
      const subP = [...flex1.children].filter(
        (ch) => ch.tagName === "P",
      ) as HTMLElement[];
      return {
        titleRowH: Math.round(titleRow.getBoundingClientRect().height),
        titleRowMb: getComputedStyle(titleRow).marginBottom,
        subtitleCount: subP.length,
        cardH: Math.round(card.getBoundingClientRect().height),
        cardW: Math.round(card.getBoundingClientRect().width),
        badgeRowH: Math.round(
          ([...card.children].find((ch) =>
            typeof ch.className === "string" && /flex-wrap/.test(ch.className),
          ) as HTMLElement)!.getBoundingClientRect().height,
        ),
      };
    });
    expect(census).not.toBeNull();
    // THE CONDITIONAL: NO subtitle P renders for the empty subcategory.
    expect(census!.subtitleCount).toBe(0);
    // The title row collapses to the reference's own no-subtitle geometry
    // (the dot+h4 row 24 + the mb-1 4 = 28) …
    expect(census!.titleRowH).toBe(28);
    expect(census!.titleRowMb).toBe("12px");
    // … and the card carries the reference's no-subtitle height: 180 (the
    // 3-badge row stays single-line h 22 — the wrap class needs the 4th
    // Recurring badge the probe does not carry).
    expect(census!.badgeRowH).toBe(22);
    expect(census!.cardW).toBe(358);
    expect(census!.cardH).toBe(180);

    // --- cleanup: the expense card's Edit dialog → Delete → the inline
    // confirm (the superset delete path; expense cards carry no kebab).
    await probe.hover();
    await probe.getByRole("button", { name: "Edit", exact: true }).click();
    const editDialog = page.getByRole("dialog");
    await expect(editDialog).toBeVisible();
    await editDialog.getByRole("button", { name: "Delete" }).click();
    await expect(editDialog.getByText("Delete this item?")).toBeVisible();
    await editDialog.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(page.getByText("Probe NoSub")).toHaveCount(0);
    // The header count + total restored (the fixture discipline).
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();
  });
});

// v71 F5: the WITH-subtitle side of the conditional — the seeded Rent
// card's subtitle-P chrome + the title-row geometry pinned at 390 so the
// F4 fix cannot regress the populated state (GREEN before AND after the
// fix — the pin's expected values are the arbit-v71.sh census's own
// measured values, byte-identical on both sides' seeded cards).
test.describe("item-card subtitle-P chrome pin at 390 (v71 — plan F5)", () => {
  test("the seeded Rent card's subtitle P renders the measured chrome (titleRow 48, P h 20)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();

    const card = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    const census = await card.evaluate((el) => {
      const titleRow = [...el.children].find(
        (ch) =>
          getComputedStyle(ch).display.includes("flex") &&
          ch.querySelector("h4") &&
          (ch.textContent || "").trim().length > 0,
      ) as HTMLElement | undefined;
      if (!titleRow) return null;
      const h4 = titleRow.querySelector("h4")!;
      const flex1 = h4.parentElement!.parentElement!;
      const subP = [...flex1.children].find(
        (ch) => ch.tagName === "P",
      ) as HTMLElement | undefined;
      if (!subP) return null;
      const cs = getComputedStyle(subP);
      return {
        titleRowH: Math.round(titleRow.getBoundingClientRect().height),
        titleRowMb: getComputedStyle(titleRow).marginBottom,
        p: {
          h: Math.round(subP.getBoundingClientRect().height),
          fs: cs.fontSize,
          lh: cs.lineHeight,
          color: cs.color,
          text: (subP.textContent || "").trim(),
        },
      };
    });
    expect(census).not.toBeNull();
    // The title row WITH the subtitle: 24 (dot+h4) + 4 (mb-1) + 20 (P) = 48.
    expect(census!.titleRowH).toBe(48);
    expect(census!.titleRowMb).toBe("12px");
    // The subtitle P's chrome — the reference's own measured values.
    expect(census!.p).toEqual({
      h: 20,
      fs: "14px",
      lh: "20px",
      color: "rgb(107, 114, 128)",
      text: "Apartment",
    });
  });
});

// v79 F4 (docs/remediation-plan-v79.md): the items pair's third re-run
// found NO NEW GAP (every census delta a documented class — the identity
// avatar, the seed counts, the v57 DATA-CONDITIONAL chips, the Recurring
// wrap) and this pin locks the re-run's never-pinned chrome axes at 1280:
// the rail AVATAR's full chrome (the tokens.spec pin holds its radius
// only — w/h/fs/fw/color/bg never pinned), the item-card AMOUNT leaf's
// per-type accent family (the v74 pin holds the savings variant; the
// income lime + expenses orange twins never pinned — plus the leaf's box
// h), and the income view's first-card HEIGHT — the v70b lesson's
// wrap/stretch arithmetic regression guard (the Salary card's
// Recurring-wrap natural 230 + the 1-row grid stretching the Freelance
// sibling to match; if the stretch or the wrap ever breaks, this fails).
// The pin's expected values are the arbit-v79.sh census's own measured
// values, byte-identical on both sides' items views at 1280x800.
test.describe("rail avatar + item-card amount-accent + card-height census at 1280 (v79 — plan F4)", () => {
  test("the avatar chrome + the amount's per-type accents + the wrap/stretch card height (v79 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/income");
    await expect(page.getByText("Freelance").first()).toBeVisible();

    const income = await page.evaluate(() => {
      const out: Record<string, unknown> = {};
      // The rail avatar — the arbitration's own finder (the v70b pattern:
      // the round 1-2 char element in the fixed aside).
      const rail = document.querySelector("aside");
      const avatar = rail
        ? [...rail.querySelectorAll("div,span,button")].find((el) => {
            const r = el.getBoundingClientRect();
            const cs = getComputedStyle(el);
            const t = (el.textContent || "").trim();
            return (
              r.width >= 30 &&
              r.width <= 45 &&
              Math.abs(r.width - r.height) < 3 &&
              parseFloat(cs.borderRadius) > 100 &&
              t.length >= 1 &&
              t.length <= 2
            );
          })
        : null;
      if (avatar) {
        const cs = getComputedStyle(avatar);
        out.avatar = {
          w: Math.round(avatar.getBoundingClientRect().width),
          h: Math.round(avatar.getBoundingClientRect().height),
          radius: cs.borderRadius,
          fs: cs.fontSize,
          fw: cs.fontWeight,
          color: cs.color,
          bg: cs.backgroundColor,
        };
      }
      // The first income card's height + its amount leaf.
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (grid) {
        const card = grid.children[0] as HTMLElement;
        out.cardH = Math.round(card.getBoundingClientRect().height);
        const amount = [...card.querySelectorAll("p")].find(
          (p) => parseFloat(getComputedStyle(p).fontSize) >= 20,
        );
        if (amount) {
          const cs = getComputedStyle(amount);
          out.incomeAmount = {
            fs: cs.fontSize,
            fw: cs.fontWeight,
            color: cs.color,
            lh: cs.lineHeight,
            h: Math.round(amount.getBoundingClientRect().height),
          };
        }
      }
      out.docSW = document.documentElement.scrollWidth;
      return out;
    });
    expect(income.avatar).toEqual({
      w: 36,
      h: 36,
      radius: "9999px",
      fs: "14px",
      fw: "600",
      color: "rgb(255, 255, 255)",
      bg: "rgb(143, 188, 63)",
    });
    // The card height — the v70b wrap/stretch arithmetic: the Salary
    // sibling's Recurring badge wraps its row to 52px (natural 230) and
    // the 1-row grid stretches the Freelance card (natural 200) to match.
    expect(income.cardH).toBe(230);
    expect(income.incomeAmount).toEqual({
      fs: "24px",
      fw: "700",
      color: "rgb(143, 188, 63)",
      lh: "32px",
      h: 32,
    });
    expect(income.docSW).toBe(1280);

    // The expenses twin — the orange accent on the same leaf family.
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Entertainment" })).toBeVisible();
    const expenses = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement;
      const amount = [...card.querySelectorAll("p")].find(
        (p) => parseFloat(getComputedStyle(p).fontSize) >= 20,
      );
      if (!amount) return null;
      const cs = getComputedStyle(amount);
      return {
        expenseAmount: {
          fs: cs.fontSize,
          fw: cs.fontWeight,
          color: cs.color,
          lh: cs.lineHeight,
          h: Math.round(amount.getBoundingClientRect().height),
        },
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(expenses).not.toBeNull();
    expect(expenses!.expenseAmount).toEqual({
      fs: "24px",
      fw: "700",
      color: "rgb(224, 122, 59)",
      lh: "32px",
      h: 32,
    });
    expect(expenses!.docSW).toBe(1280);
  });
});

// v80 F4 (docs/remediation-plan-v80.md): the savings pair's third re-run
// found NO NEW GAP (every census delta a documented class — the seed
// counts, the v58 DATA-CONDITIONAL chips, the classification-VALUE
// badges, the user identity) and this pin locks the re-run's
// never-pinned axes at 1280: the savings goal-card's CARD-HEIGHT TWINS
// (the v58 pin asserts the first card's w/pad/radius but never its
// height; the v79 pin holds the income view's WRAP twin — this adds the
// savings view's own wrap twin [the Investments card's Recurring-badge
// wrap → natural 230] AND the STRETCH twin [the Emergency Fund
// sibling's natural 200 stretched by the 1-row grid to the taller
// card's height — pinned nowhere; a broken wrap OR a broken stretch
// both flip this pin]), the TITLE ROW's geometry (the 1280 state of the
// v51/v54 390-only family, measured byte-identical on both sides by
// arbit-v80.sh: flex/8px/center/h 24/the 8x8 dot at 9999px in the
// savings blue — the v45 F1a pin's income lime-dot twin completed to
// the savings type), and the card's BORDER + BG (the v45 F1a pin's
// income-card family's savings twin). The pin's expected values are the
// arbit-v80.sh census's own measured values, byte-identical on both
// sides' savings views at 1280x800.
test.describe("savings goal-card height-twins + title-row geometry + card chrome census at 1280 (v80 — plan F4)", () => {
  test("the wrap + stretch card heights + the titleRow + the border/bg (v80 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();

    const census = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      // The CARD-HEIGHT TWINS: the first card's WRAP-governed natural
      // height + the second card's STRETCH-governed height (the live
      // grid probe measured [230, 230] with alignItems "normal" — the
      // grid default = stretch, byte-identical CSS with the reference).
      const heights = [...grid.children].map((c) =>
        Math.round(c.getBoundingClientRect().height),
      );
      const card = grid.children[0] as HTMLElement;
      const ccs = getComputedStyle(card);
      const cardChrome = {
        border: `${ccs.borderTopWidth} ${ccs.borderTopStyle} ${ccs.borderTopColor}`,
        bg: ccs.backgroundColor,
      };
      // The TITLE ROW — the h4's direct parent (the dot + title line —
      // the arbitration's own walk): the row's flex geometry + the
      // category dot's full chrome.
      const h4 = card.querySelector("h4");
      let titleRow: Record<string, unknown> | null = null;
      if (h4 && h4.parentElement && h4.parentElement !== card) {
        const row = h4.parentElement;
        const rs = getComputedStyle(row);
        const dot = [...row.querySelectorAll("div,span")].find((d) => {
          const b = d.getBoundingClientRect();
          return b.width > 0 && b.width <= 12 && b.height > 0 && b.height <= 12;
        });
        titleRow = {
          display: rs.display,
          gap: rs.gap,
          alignItems: rs.alignItems,
          h: Math.round(row.getBoundingClientRect().height),
          dotW: dot ? Math.round(dot.getBoundingClientRect().width) : null,
          dotH: dot ? Math.round(dot.getBoundingClientRect().height) : null,
          dotRadius: dot ? getComputedStyle(dot).borderRadius : null,
          dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
        };
      }
      return {
        childCount: grid.children.length,
        heights,
        cardChrome,
        titleRow,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The CARD-HEIGHT TWINS — the v70b lesson's full arithmetic on the
    // savings view's own two-card row: the Investments card's
    // Recurring-badge wrap (the badge row's 52px two-line height) gives
    // its natural 230 (the WRAP twin), and the 1-row grid STRETCHES the
    // Emergency Fund sibling (natural 200) to match (the STRETCH twin).
    // A broken badge wrap, a broken grid stretch, or a changed card
    // interior each flip these values.
    expect(census!.childCount).toBe(2);
    expect(census!.heights).toEqual([230, 230]);

    // The TITLE ROW's geometry at 1280 — the 1280 state of the v51/v54
    // 390-only family, byte-identical on both sides' savings goal cards:
    // the dot + h4 line at flex/8px/center/h 24 with the 8x8 fully-round
    // dot in the savings blue.
    expect(census!.titleRow).toEqual({
      display: "flex",
      gap: "8px",
      alignItems: "center",
      h: 24,
      dotW: 8,
      dotH: 8,
      dotRadius: "9999px",
      dotBg: "rgb(59, 126, 161)",
    });

    // The card's border + bg at 1280 — the v45 F1a pin's income-card
    // family's savings twin.
    expect(census!.cardChrome).toEqual({
      border: "1px solid rgb(229, 231, 227)",
      bg: "rgb(255, 255, 255)",
    });

    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);
  });
});

// v85 F4 (docs/remediation-plan-v85.md): the v79-era items pair's FOURTH
// re-run (v57 → v64 → v70 → v79 → v85) found NO NEW GAP (every census
// delta a documented class — the seed counts/data, the v57
// DATA-CONDITIONAL chips + Recurring wrap, the user identity; the one NEW
// VLM flag — the "Edit with Base44" FAB claimed present in the CLONE —
// disproven as an IMAGE-ATTRIBUTION SWAP by the two-step arbitration: the
// DOM census finds no Base44 element on either side, the pixel census
// locates the dark FAB pixels in the REFERENCE shot's corner only, and
// the single-image VLM reads confirm it — the platform-chrome class on
// the reference) and this pin locks the re-run's never-pinned axes at
// 1280: the EXPENSE-ONLY content wrapper (the pr-24 family — the room
// reserved for the hover action row, never censused before
// wrapper-arbit-v85.sh measured it byte-identical on both sides), the
// expenses TITLE ROW's full geometry (the orange dot's FIRST pin anywhere
// — TYPE_COLORS.expense on the dot, completing the v80 savings blue
// twin's per-type trilogy; the h4's forestDark color, never pinned on
// any item-card title), and the income twin's paddingRight-0 control
// (the conditional's other leg — the pr scoped to expenses only, on both
// sides). The pin's expected values are the wrapper-arbit-v85.sh
// census's own measured values, byte-identical on both sides' items
// views at 1280x800.
test.describe("expense-card content-wrapper + orange-dot titleRow census at 1280 (v85 — plan F4)", () => {
  test("the wrapper's pr family + the titleRow's full geometry + the income pr-0 control (v85 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Entertainment" })).toBeVisible();

    const census = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement;
      const h4 = card.querySelector("h4");
      if (!h4 || !h4.parentElement || !h4.parentElement.parentElement) return null;
      // titleRow = the h4's parent (the dot + title line); the WRAPPER =
      // the titleRow's parent (the flex-1 pr-24 column on expenses — the
      // wrapper-arbit-v85.sh walk).
      const row = h4.parentElement as HTMLElement;
      const wrapper = row.parentElement as HTMLElement;
      const rcs = getComputedStyle(row);
      const wcs = getComputedStyle(wrapper);
      const dot = [...row.querySelectorAll("div,span")].find((d) => {
        const b = d.getBoundingClientRect();
        return b.width > 0 && b.width <= 12 && b.height > 0 && b.height <= 12;
      });
      return {
        wrapper: {
          display: wcs.display,
          flexGrow: wcs.flexGrow,
          paddingRight: wcs.paddingRight,
        },
        titleRow: {
          display: rcs.display,
          alignItems: rcs.alignItems,
          gap: rcs.gap,
          h: Math.round(row.getBoundingClientRect().height),
          dotW: dot ? Math.round(dot.getBoundingClientRect().width) : null,
          dotH: dot ? Math.round(dot.getBoundingClientRect().height) : null,
          dotRadius: dot ? getComputedStyle(dot).borderRadius : null,
          dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
          h4Fs: getComputedStyle(h4).fontSize,
          h4Fw: getComputedStyle(h4).fontWeight,
          h4Color: getComputedStyle(h4).color,
        },
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The WRAPPER's pr family — the expenses-conditional pr-24 (the
    // hover action row's reserved room): display block, flex-1, 96px
    // right padding. A broken conditional — the pr leaking to
    // income/savings or dropping from expenses — flips these axes.
    expect(census!.wrapper).toEqual({
      display: "block",
      flexGrow: "1",
      paddingRight: "96px",
    });

    // The TITLE ROW's full geometry at 1280 — the orange twin's first
    // pin: flex/center/8px/h 24 with the 8×8 fully-round dot in the
    // expenses orange (TYPE_COLORS.expense on the DOT — the v79 pin
    // holds the same color on the amount leaf) and the h4 at 16px/600
    // in rgb.forestDark.
    expect(census!.titleRow).toEqual({
      display: "flex",
      alignItems: "center",
      gap: "8px",
      h: 24,
      dotW: 8,
      dotH: 8,
      dotRadius: "9999px",
      dotBg: "rgb(224, 122, 59)",
      h4Fs: "16px",
      h4Fw: "600",
      h4Color: "rgb(26, 58, 46)",
    });

    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);

    // The income twin's paddingRight control — the conditional's other
    // leg: the pr is scoped to expenses ONLY (both sides measured 0 on
    // the income wrapper — the plain flex-1 column).
    await page.goto("/income");
    await expect(page.getByText("Freelance").first()).toBeVisible();
    const income = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement;
      const h4 = card.querySelector("h4");
      if (!h4 || !h4.parentElement || !h4.parentElement.parentElement) return null;
      const wrapper = h4.parentElement.parentElement as HTMLElement;
      return {
        paddingRight: getComputedStyle(wrapper).paddingRight,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(income).not.toBeNull();
    expect(income!.paddingRight).toBe("0px");
    expect(income!.docSW).toBe(1280);
  });
});

// v86 F4 (docs/remediation-plan-v86.md): the v80-era savings pair's FOURTH
// re-run (v58 → v65 → v74 → v80 → v86) found NO NEW GAP — the VLM verdict
// IDENTICAL for the first time in the pair's five-shot history (every
// called-out delta the expected data/identity classes, zero layout/style
// flags), and the both-sides census reproducing the v80 values exactly
// (zero drift). This pin locks the re-run's never-pinned axes at 1280:
// the savings goal-card's SUBTITLE P full chrome (the 1280 state of the
// v51 F3 390-only family — the fs/color held at 390, the lh + the box +
// the mt NEVER, and no 1280 subtitle pin anywhere on any view), the
// with-subtitle ARITHMETIC (the titleRow's mb-1 4px + the header row's own
// geometry — the 48 = 24 + 4 + 20 twin of the 390 Rent-card family, never
// pinned at 1280), and the WRAPPER's savings paddingRight-0 THIRD LEG
// (completing the v85 conditional trilogy: expenses pr-24 / income 0 /
// savings 0 — the pr scoped to expenses only, now verified on all three
// types). The pin's expected values are the wrapper-arbit-v86.sh census's
// own measured values, byte-identical on both sides' savings views at
// 1280x800 (the reference's Emergency Fund "Home Savings" vs the clone's
// Investments "Index Funds" — the TEXT the data class, the CHROME the
// pin).
test.describe("savings goal-card subtitle + header-row + wrapper third-leg census at 1280 (v86 — plan F4)", () => {
  test("the subtitle P's full chrome + the with-subtitle arithmetic + the savings pr-0 control (v86 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    await expect(page.getByText("Investments").first()).toBeVisible();

    const census = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement;
      const h4 = card.querySelector("h4");
      if (!h4 || !h4.parentElement || !h4.parentElement.parentElement) return null;
      // titleRow = the h4's parent (the dot + title line); the WRAPPER =
      // the titleRow's parent (the flex-1 column — NO pr on savings, the
      // conditional's third leg — the wrapper-arbit-v86.sh walk).
      const row = h4.parentElement as HTMLElement;
      const wrapper = row.parentElement as HTMLElement;
      // The SUBTITLE P: the wrapper's P child (the v71 F4 conditional —
      // rendered only for a non-empty subcategory; the seeded
      // Investments card carries "Index Funds").
      const subP = [...wrapper.children].find((ch) => ch.tagName === "P") as
        | HTMLElement
        | undefined;
      const headerRow = wrapper.parentElement as HTMLElement;
      const rcs = getComputedStyle(row);
      const wcs = getComputedStyle(wrapper);
      const hrs = getComputedStyle(headerRow);
      const pcs = subP ? getComputedStyle(subP) : null;
      return {
        wrapper: {
          display: wcs.display,
          flexGrow: wcs.flexGrow,
          paddingRight: wcs.paddingRight,
        },
        subtitle: subP
          ? {
              h: Math.round(subP.getBoundingClientRect().height),
              fs: pcs!.fontSize,
              lh: pcs!.lineHeight,
              color: pcs!.color,
              mt: pcs!.marginTop,
            }
          : null,
        titleRowMb: rcs.marginBottom,
        headerRow: {
          display: hrs.display,
          justify: hrs.justifyContent,
          alignItems: hrs.alignItems,
          h: Math.round(headerRow.getBoundingClientRect().height),
          mb: hrs.marginBottom,
        },
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The WRAPPER's savings third leg — the pr conditional's last
    // uncovered type: the plain flex-1 block column, paddingRight 0
    // (with the v85 pin's expenses 96px + income 0px legs, the
    // conditional is now pinned on ALL THREE types; a pr leaking to
    // savings flips this axis).
    expect(census!.wrapper).toEqual({
      display: "block",
      flexGrow: "1",
      paddingRight: "0px",
    });

    // The SUBTITLE P's full chrome at 1280 — the 1280 state of the v51
    // F3 390-only family: text-sm's 14px/20px pair, the gray
    // rgb(107,114,128), the lh-governed 20px box, no top margin (the
    // spacing comes from the titleRow's mb-1). A broken text-sm, a
    // changed gray, or a stray margin flips these axes.
    expect(census!.subtitle).toEqual({
      h: 20,
      fs: "14px",
      lh: "20px",
      color: "rgb(107, 114, 128)",
      mt: "0px",
    });

    // The with-subtitle ARITHMETIC at 1280 — the header row's own
    // geometry, never pinned at any viewport: flex/space-between/
    // items-start with h 48 (24 titleRow + 4 mb-1 + 20 P) and the
    // mb-3 12px rhythm below. The titleRow's own mb is the 4px
    // (mb-1) — the dot+title row to subtitle spacing.
    expect(census!.titleRowMb).toBe("4px");
    expect(census!.headerRow).toEqual({
      display: "flex",
      justify: "space-between",
      alignItems: "flex-start",
      h: 48,
      mb: "12px",
    });

    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);
  });
});
