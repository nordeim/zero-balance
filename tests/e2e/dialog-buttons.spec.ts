import { expect, test } from "@playwright/test";

// Dialog action buttons (session-8 audit, docs/remediation-plan-v5.md G4
// + superset pin R5). Measured live on the reference:
//
//   Cancel (every dialog): shadcn OUTLINE — white bg, 1px #e5e5e5 border,
//     #0a0a0a text, rounded-md (6px), 500, h-36.
//   Save Item (budget-item add + edit) / Save Asset / Save Liability:
//     linear-gradient(135deg, rgb(45,90,74), rgb(143,188,63)) — the
//     forest→lime gradient, white text, 6px, 500.
//   Save Item (line-item / calculator dialog):
//     linear-gradient(135deg, rgb(224,122,59), rgb(245,169,98)) — ORANGE.
//   Add First Item (calculator empty state): outline — #0a0a0a text on a
//     1px #e5e5e5 border. "• Will update category total": #ea580c.
//
// R5 superset pin: the reference's dialogs do NOT close on Escape (its
// overlay is a plain fixed div with no keyboard dismissal — only X/Cancel
// close it). The clone's Radix dialogs DO — pinned here.
// Contexts arrive AUTHENTICATED (setup-project storageState).

const FOREST_GRADIENT = "linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))";
const ORANGE_GRADIENT = "linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))";

test.describe("dialog action buttons (v5)", () => {
  test("budget dialog: outline Cancel + forest→lime gradient Save Item", async ({ page }) => {
    await page.goto("/income");
    // The prerendered page carries the empty-store state (header + empty-state
    // "Add Income" buttons both in the static HTML); wait for the seeded card
    // so the click targets exactly one button after hydration.
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.locator('[role="dialog"]');
    await expect(dialog).toBeVisible();

    const buttons = await page.evaluate(() => {
      const grab = (txt: string) => {
        const b = [...document.querySelectorAll('[role="dialog"] button')].find(
          (x) => (x.textContent || "").trim() === txt,
        );
        if (!b) return null;
        const cs = getComputedStyle(b);
        const r = b.getBoundingClientRect();
        return {
          bg: cs.backgroundColor,
          bgImage: cs.backgroundImage,
          border: `${cs.borderWidth} ${cs.borderColor}`,
          color: cs.color,
          radius: cs.borderRadius,
          h: Math.round(r.height),
          weight: cs.fontWeight,
        };
      };
      return { cancel: grab("Cancel"), save: grab("Save Item") };
    });

    // Cancel: outline chrome.
    expect(buttons.cancel).not.toBeNull();
    expect(buttons.cancel!.bg).toBe("rgb(255, 255, 255)");
    expect(buttons.cancel!.border).toBe("1px rgb(229, 229, 229)");
    expect(buttons.cancel!.color).toBe("rgb(10, 10, 10)");
    expect(buttons.cancel!.radius).toBe("6px");
    expect(buttons.cancel!.h).toBe(36);

    // Save Item: the forest→lime gradient, white text, 6px, 500.
    expect(buttons.save).not.toBeNull();
    expect(buttons.save!.bgImage).toBe(FOREST_GRADIENT);
    expect(buttons.save!.color).toBe("rgb(255, 255, 255)");
    expect(buttons.save!.radius).toBe("6px");
    expect(buttons.save!.h).toBe(36);
    expect(buttons.save!.weight).toBe("500");

    // Footer geometry (session-15 audit, plan v8 G1): the reference renders
    // the dialog footer as `flex gap-3 pt-4` with BOTH buttons at flex-1 —
    // Cancel ≈ 307px (left half of the 624px content row) + Save Item ≈ 305px
    // (right half). The clone ran content-sized right-aligned buttons
    // (81px/127px, no pt-4).
    const footer = await page.evaluate(() => {
      const dialogs = [...document.querySelectorAll('[role="dialog"]')];
      const d = dialogs[dialogs.length - 1];
      const save = [...d.querySelectorAll("button")].find(
        (x) => (x.textContent || "").trim() === "Save Item",
      );
      if (!save) return null;
      let row: HTMLElement | null = save.closest("div");
      while (row && row.getBoundingClientRect().height < 50) row = row.parentElement;
      if (!row) return null;
      const cancel = [...row.querySelectorAll("button")].find(
        (x) => (x.textContent || "").trim() === "Cancel",
      );
      const rcs = getComputedStyle(row);
      return {
        row: { display: rcs.display, gap: rcs.gap, padTop: rcs.paddingTop },
        cancelW: cancel ? Math.round(cancel.getBoundingClientRect().width) : null,
        saveW: Math.round(save.getBoundingClientRect().width),
      };
    });
    expect(footer).not.toBeNull();
    expect(footer!.row.display).toBe("flex");
    expect(footer!.row.gap).toBe("12px");
    expect(footer!.row.padTop).toBe("16px");
    // flex-1 halves: (624 − 12) / 2 = 306 each on the reference.
    expect(footer!.cancelW!).toBeGreaterThanOrEqual(300);
    expect(footer!.saveW).toBeGreaterThanOrEqual(300);
  });

  test("calculator: orange-gradient line-item Save + outline Add First Item + orange hint", async ({
    page,
  }) => {
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();
    // Open the calculator on an expense card (hover-revealed Calculate).
    const card = page.locator("main .group", { hasText: "Rent" }).first();
    await card.hover();
    await page.getByRole("button", { name: "Calculate" }).first().click();
    const calc = page.locator('[role="dialog"]');
    await expect(calc).toBeVisible();

    // Empty state button: outline chrome (#0a0a0a text, #e5e5e5 border).
    const empty = await page.evaluate(() => {
      const b = [...document.querySelectorAll('[role="dialog"] button')].find(
        (x) => (x.textContent || "").trim() === "Add First Item",
      );
      if (!b) return null;
      const cs = getComputedStyle(b);
      return { color: cs.color, border: `${cs.borderWidth} ${cs.borderColor}`, bg: cs.backgroundColor };
    });
    expect(empty).not.toBeNull();
    expect(empty!.color).toBe("rgb(10, 10, 10)");
    expect(empty!.border).toBe("1px rgb(229, 229, 229)");
    expect(empty!.bg).toBe("rgb(255, 255, 255)");

    // "• Will update category total": the reference's orange-600, plain rgb.
    const hint = await page.evaluate(() => {
      const el = [...document.querySelectorAll('[role="dialog"] span')].find((x) =>
        (x.textContent || "").includes("Will update category total"),
      );
      return el ? getComputedStyle(el).color : null;
    });
    expect(hint).toBe("rgb(234, 88, 12)");

    // Open the line-item dialog: its Save Item is the ORANGE gradient.
    await page.getByRole("button", { name: "Add First Item" }).click();
    const lineDialog = page.locator('[role="dialog"]').nth(1);
    await expect(lineDialog).toBeVisible();
    const lineSave = await page.evaluate(() => {
      const dialogs = [...document.querySelectorAll('[role="dialog"]')];
      const d = dialogs[dialogs.length - 1];
      const b = [...d.querySelectorAll("button")].find(
        (x) => (x.textContent || "").trim() === "Save Item",
      );
      if (!b) return null;
      const cs = getComputedStyle(b);
      return { bgImage: cs.backgroundImage, color: cs.color, radius: cs.borderRadius, weight: cs.fontWeight };
    });
    expect(lineSave).not.toBeNull();
    expect(lineSave!.bgImage).toBe(ORANGE_GRADIENT);
    expect(lineSave!.color).toBe("rgb(255, 255, 255)");
    expect(lineSave!.radius).toBe("6px");
    expect(lineSave!.weight).toBe("500");

    // Footer geometry (plan v8 G1): the line-item dialog's footer matches the
    // reference's flex-1 split too (Cancel ≈ 307px + Save Item ≈ 305px).
    const lineFooter = await page.evaluate(() => {
      const dialogs = [...document.querySelectorAll('[role="dialog"]')];
      const d = dialogs[dialogs.length - 1];
      const save = [...d.querySelectorAll("button")].find(
        (x) => (x.textContent || "").trim() === "Save Item",
      );
      if (!save) return null;
      let row: HTMLElement | null = save.closest("div");
      while (row && row.getBoundingClientRect().height < 50) row = row.parentElement;
      const cancel = row
        ? [...row.querySelectorAll("button")].find(
            (x) => (x.textContent || "").trim() === "Cancel",
          )
        : null;
      return {
        saveW: Math.round(save.getBoundingClientRect().width),
        cancelW: cancel ? Math.round(cancel.getBoundingClientRect().width) : null,
      };
    });
    expect(lineFooter).not.toBeNull();
    expect(lineFooter!.cancelW!).toBeGreaterThanOrEqual(300);
    expect(lineFooter!.saveW).toBeGreaterThanOrEqual(300);
  });

  test("button ambient shadows + focus-visible ring (v11 G2)", async ({ page }) => {
    // Measured live on the reference: its gradient buttons (Save Item,
    // Add Income, Add Item, the calculator's sm Add Item) carry v3's BARE
    // shadow — rgba(0,0,0,0.1) 0 1px 3px, rgba(0,0,0,0.1) 0 1px 2px -1px —
    // while its outline buttons (Cancel, Add First Item) carry v3's
    // shadow-sm (0.05, single layer). On focus-visible EVERY variant
    // renders the shadcn ring: a white zero-spread inner layer + the 1px
    // #0a0a0a ring + the variant's own ambient, plus v3's outline-none
    // (2px transparent, offset 2px). The clone's .zb-btn-add family fell
    // through to the browser-default outline and the lighter shadow.
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.locator('[role="dialog"]');
    await expect(dialog).toBeVisible();

    const V3_SM = "rgba(0, 0, 0, 0.05) 0px 1px 2px 0px";

    const budget = await page.evaluate(() => {
      const dlg = document.querySelector('[role="dialog"]');
      const grab = (txt: string) => {
        const b = [...(dlg?.querySelectorAll("button") || [])].find(
          (x) => (x.textContent || "").trim() === txt,
        );
        if (!b) return null;
        const cs = getComputedStyle(b);
        return { rest: cs.boxShadow, outlineRest: `${cs.outlineStyle}/${cs.outlineWidth}` };
      };
      return { save: grab("Save Item"), cancel: grab("Cancel") };
    });
    // Rest shadows: Save = v3 bare shadow; Cancel (Button primitive) =
    // v3 shadow-sm — both already pinned at the token level, asserted here
    // as the v11 reference composition.
    expect(budget.save!.rest).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(budget.save!.rest).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(budget.cancel!.rest).toContain(V3_SM);

    // Focus-visible: programmatic focus with focusVisible:true (the same
    // probe technique used live on the reference).
    const focused = await page.evaluate(() => {
      const dlg = document.querySelector('[role="dialog"]');
      const b = [...(dlg?.querySelectorAll("button") || [])].find(
        (x) => (x.textContent || "").trim() === "Save Item",
      );
      if (!b) return null;
      // focusVisible is a real Chromium FocusOptions member (the live
      // probes used it) — TS's DOM lib lags it, hence the cast.
      (b as HTMLElement).focus({ focusVisible: true } as unknown as FocusOptions);
      const cs = getComputedStyle(b);
      return {
        shadow: cs.boxShadow,
        outline: `${cs.outlineStyle}/${cs.outlineWidth}/${cs.outlineColor}`,
        offset: cs.outlineOffset,
      };
    });
    expect(focused!.shadow).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");
    expect(focused!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    // v3 outline-none: transparent 2px, offset 2 (NOT the browser default
    // `auto` outline the clone rendered pre-fix).
    expect(focused!.outline).toBe("solid/2px/rgba(0, 0, 0, 0)");
    expect(focused!.offset).toBe("2px");
    await page.keyboard.press("Escape");

    // The calculator's sm + outline variants carry the same slots.
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();
    const card = page.locator("main .group", { hasText: "Rent" }).first();
    await card.hover();
    await page.getByRole("button", { name: "Calculate" }).first().click();
    await expect(page.locator('[role="dialog"]')).toBeVisible();

    const calc = await page.evaluate(() => {
      const dlg = document.querySelector('[role="dialog"]');
      const grab = (txt: string) => {
        const b = [...(dlg?.querySelectorAll("button") || [])].find(
          (x) => (x.textContent || "").trim() === txt,
        );
        if (!b) return null;
        const cs = getComputedStyle(b);
        return { rest: cs.boxShadow };
      };
      return { addItem: grab("Add Item"), addFirst: grab("Add First Item") };
    });
    expect(calc.addItem!.rest).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(calc.addItem!.rest).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(calc.addFirst!.rest).toContain(V3_SM);
  });

  test("asset dialog: outline Cancel + forest→lime gradient Save Asset", async ({ page }) => {
    await page.goto("/networth");
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    await page.getByRole("button", { name: "Add Asset" }).first().click();
    await expect(page.locator('[role="dialog"]')).toBeVisible();

    const buttons = await page.evaluate(() => {
      const grab = (txt: string) => {
        const b = [...document.querySelectorAll('[role="dialog"] button')].find(
          (x) => (x.textContent || "").trim() === txt,
        );
        if (!b) return null;
        const cs = getComputedStyle(b);
        return { bg: cs.backgroundColor, bgImage: cs.backgroundImage, border: `${cs.borderWidth} ${cs.borderColor}`, color: cs.color };
      };
      return { cancel: grab("Cancel"), save: grab("Save Asset") };
    });
    expect(buttons.cancel).not.toBeNull();
    expect(buttons.cancel!.bg).toBe("rgb(255, 255, 255)");
    expect(buttons.cancel!.border).toBe("1px rgb(229, 229, 229)");
    expect(buttons.cancel!.color).toBe("rgb(10, 10, 10)");
    expect(buttons.save).not.toBeNull();
    expect(buttons.save!.bgImage).toBe(FOREST_GRADIENT);
    expect(buttons.save!.color).toBe("rgb(255, 255, 255)");

    // Footer geometry (plan v8 G1): asset dialog footer = flex-1 halves.
    const assetFooter = await page.evaluate(() => {
      const dialogs = [...document.querySelectorAll('[role="dialog"]')];
      const d = dialogs[dialogs.length - 1];
      const save = [...d.querySelectorAll("button")].find(
        (x) => (x.textContent || "").trim() === "Save Asset",
      );
      if (!save) return null;
      let row: HTMLElement | null = save.closest("div");
      while (row && row.getBoundingClientRect().height < 50) row = row.parentElement;
      const cancel = row
        ? [...row.querySelectorAll("button")].find(
            (x) => (x.textContent || "").trim() === "Cancel",
          )
        : null;
      const rcs = row ? getComputedStyle(row) : null;
      return {
        row: rcs ? { display: rcs.display, gap: rcs.gap, padTop: rcs.paddingTop } : null,
        saveW: Math.round(save.getBoundingClientRect().width),
        cancelW: cancel ? Math.round(cancel.getBoundingClientRect().width) : null,
      };
    });
    expect(assetFooter).not.toBeNull();
    expect(assetFooter!.row!.display).toBe("flex");
    expect(assetFooter!.row!.gap).toBe("12px");
    expect(assetFooter!.row!.padTop).toBe("16px");
    expect(assetFooter!.cancelW!).toBeGreaterThanOrEqual(300);
    expect(assetFooter!.saveW).toBeGreaterThanOrEqual(300);
  });

  test("dialogs close on Escape (superset over reference bug R5)", async ({ page }) => {
    // The reference's dialogs ignore Escape (no keyboard dismissal — only
    // X/Cancel close its plain fixed overlay). The clone's Radix dialogs
    // close on Escape; this pins that superset behavior.
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.locator('[role="dialog"]');
    await expect(dialog).toBeVisible();
    await page.keyboard.press("Escape");
    await expect(dialog).toHaveCount(0);
  });

  test("every Save button carries the reference's lucide Save icon (v6 G3)", async ({ page }) => {
    // Measured on the reference's Add/Edit budget-item, line-item and asset
    // dialogs: the gradient Save buttons all carry the lucide Save icon
    // (16px) before the label. The superset Loader2 spinner may replace it
    // while saving — assert the resting state.
    const saveIconCount = () =>
      page.evaluate(() => {
        const dialogs = [...document.querySelectorAll('[role="dialog"]')];
        const d = dialogs[dialogs.length - 1];
        if (!d) return -1;
        const b = [...d.querySelectorAll('button[type="submit"]')].pop();
        if (!b) return -1;
        return [...b.querySelectorAll("svg")].filter((s) => !(s.getAttribute("class") || "").includes("animate-spin")).length;
      });

    // 1. budget-item dialog (Save Item, forest gradient).
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    await expect(page.locator('[role="dialog"]')).toBeVisible();
    expect(await saveIconCount()).toBe(1);
    await page.keyboard.press("Escape");

    // 2. line-item dialog via the calculator (Save Item, orange gradient).
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();
    const rent = page.locator("main .group", { hasText: "Rent" }).first();
    await rent.hover();
    await page.getByRole("button", { name: "Calculate" }).first().click();
    await expect(page.locator('[role="dialog"]')).toBeVisible();
    await page.getByRole("button", { name: "Add First Item" }).click();
    await expect(page.locator('[role="dialog"]').nth(1)).toBeVisible();
    expect(await saveIconCount()).toBe(1);
    await page.keyboard.press("Escape");
    await page.keyboard.press("Escape");

    // 3. asset dialog (Save Asset, forest gradient).
    await page.goto("/networth");
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    await page.getByRole("button", { name: "Add Asset" }).first().click();
    await expect(page.locator('[role="dialog"]')).toBeVisible();
    expect(await saveIconCount()).toBe(1);
    await page.keyboard.press("Escape");

    // 4. liability dialog (Save Liability, orange gradient).
    await page.getByRole("tab", { name: "Liabilities" }).click();
    await expect(page.getByText("2 items · $311,250")).toBeVisible();
    await page.getByRole("button", { name: "Add Liability" }).first().click();
    await expect(page.locator('[role="dialog"]')).toBeVisible();
    expect(await saveIconCount()).toBe(1);
  });
});

// ---------------------------------------------------------------------------
// v9 — dialog chrome: X-close geometry, sticky-header height, label line box,
// classification-tile height (docs/remediation-plan-v9.md G2/G3/G4).
//
// Measured live on the reference's Add Budget Item dialog:
//   X-close: a 36×36 flex child of the STICKY header (flex justify-between
//     px-6 py-4 border-b), svg 16px, radius 6px, #0a0a0a — so the header
//     computes 69px (16 + 36 + 16 + 1).
//   Field labels: plain inline `text-sm font-medium leading-none` → glyph-box
//     rect h16 → label-bottom → input-top gap 12px (with space-y-2).
//   Classification tiles: text lh 14 → tile h 52 (p-4 + 16px content +
//     2×2px borders).
// ---------------------------------------------------------------------------

test.describe("dialog chrome (v9)", () => {
  test("X-close is a 36×36 in-header button and the header is 69px tall", async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.locator('[role="dialog"]');
    await expect(dialog).toBeVisible();

    const chrome = await page.evaluate(() => {
      const d = document.querySelector('[role="dialog"]')!;
      // The sticky header: the first child carrying border-b (the DialogHeader).
      const header = [...d.children].find(
        (c) => /border-b/.test((c as HTMLElement).className || ""),
      ) as HTMLElement | undefined;
      const x = [...d.querySelectorAll("button")].find(
        (b) => b.querySelector("svg.lucide-x, svg[class*=x]") && !b.textContent?.trim(),
      ) || header?.querySelector("button") || null;
      const svg = x?.querySelector("svg") || null;
      const headerRect = header?.getBoundingClientRect();
      const xr = x?.getBoundingClientRect();
      const xcs = x ? getComputedStyle(x) : null;
      return {
        headerH: headerRect ? Math.round(headerRect.height) : null,
        x: x && xr
          ? {
              w: Math.round(xr.width),
              h: Math.round(xr.height),
              svgW: svg ? Math.round(svg.getBoundingClientRect().width) : null,
              radius: xcs?.borderRadius,
              color: xcs?.color,
              cls: x ? (x as HTMLElement).className || "" : null,
            }
          : null,
      };
    });

    // Header: 16 + 36 + 16 + 1 = 69 (the 36px X rides in the flex row).
    expect(chrome.headerH).toBe(69);
    expect(chrome.x).not.toBeNull();
    expect(chrome.x!.w).toBe(36);
    expect(chrome.x!.h).toBe(36);
    expect(chrome.x!.svgW).toBe(16);
    expect(chrome.x!.radius).toBe("6px");
    expect(chrome.x!.color).toBe("rgb(10, 10, 10)");
    // v27 G1 — the X's keyboard-focus + hover family: the reference runs the
    // shadcn ghost-icon base (focus-visible:ring-1, hover:text-accent-foreground
    // — the SAME family as the dialog Cancel/Save buttons v26 verified
    // byte-identical). The clone had drifted to focus:outline-none
    // focus-visible:ring-2 with no hover text; the class attribute is the
    // reliable arbiter (measured live with REAL Tab walks on both sites: the
    // reference renders a 1px #0a0a0a ring, the drift rendered 2px).
    expect(chrome.x!.cls).toContain("focus-visible:outline-none");
    expect(chrome.x!.cls).toContain("focus-visible:ring-1");
    expect(chrome.x!.cls).not.toContain("focus-visible:ring-2");
    expect(chrome.x!.cls).not.toContain("focus:outline-none");
    expect(chrome.x!.cls).toContain("hover:bg-accent");
    expect(chrome.x!.cls).toContain("hover:text-accent-foreground");
  });

  test("field labels sit 12px above their inputs (inline label line box)", async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.locator('[role="dialog"]');
    await expect(dialog).toBeVisible();

    // The reference's labels are INLINE (plain shadcn-v1 form) — the glyph
    // box extends past the 14px line-height, so with the same space-y-2
    // wrapper the label-bottom → input-top gap measures 12px.
    const gap = await page.evaluate(() => {
      const d = document.querySelector('[role="dialog"]')!;
      const lbl = [...d.querySelectorAll("label")].find(
        (l) => (l.textContent || "").trim() === "Amount",
      );
      const input = lbl?.parentElement?.querySelector("input");
      if (!lbl || !input) return null;
      const lr = lbl.getBoundingClientRect();
      const ir = input.getBoundingClientRect();
      return {
        gap: Math.round(ir.y - (lr.y + lr.height)),
        labelH: Math.round(lr.height),
        display: getComputedStyle(lbl).display,
      };
    });
    expect(gap).not.toBeNull();
    expect(gap!.gap).toBe(12);
    expect(gap!.display).toBe("inline");
  });

  test("classification tiles are 52px tall (leading-none tile text)", async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.locator('[role="dialog"]');
    await expect(dialog).toBeVisible();

    // Reference tiles: p-4 + content 16 (radio 16 / text lh 14) + 2×2px
    // borders = 52. The clone's text-sm default lh 20 made them 56.
    const tiles = await page.evaluate(() => {
      const d = document.querySelector('[role="dialog"]')!;
      return [...d.querySelectorAll("[role='radio']")]
        .map((r) => r.closest("label"))
        .filter((l): l is HTMLLabelElement => !!l)
        .slice(0, 3)
        .map((l) => {
          const r = l.getBoundingClientRect();
          const txt = [...l.querySelectorAll("span")].find(
            (s) => (s.textContent || "").trim().length > 0,
          );
          return {
            h: Math.round(r.height),
            w: Math.round(r.width),
            textLh: txt ? getComputedStyle(txt).lineHeight : null,
          };
        });
    });
    expect(tiles).toHaveLength(3);
    for (const t of tiles) {
      expect(t.h).toBe(52);
      expect(t.w).toBe(197);
      expect(t.textLh).toBe("14px");
    }
  });

  test("classification tiles carry the reference's 16px lucide icons (v20 G2)", async ({ page }) => {
    // Found by the v20 populated-edit-dialog VLM sweep ("icons inside the
    // radio buttons — circle, heart, leaf") and DOM-verified on both the
    // reference's Add and Edit dialog states (docs/remediation-plan-v20.md
    // G2): each tile label carries a 16px lucide icon between the radio and
    // the text, colored by the per-classification accent — need →
    // lucide-circle-alert #e07a3b, want → lucide-heart #3b7ea1, savings →
    // lucide-piggy-bank #8fbc3f (the same family the donut legend renders).
    // The clone's tiles rendered [radio + span] with no icon; the v19
    // empty-dialog sweep missed them (full-page pairs at dialog scale).
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.locator('[role="dialog"]');
    await expect(dialog).toBeVisible();

    const tiles = await page.evaluate(() => {
      const d = document.querySelector('[role="dialog"]')!;
      return [...d.querySelectorAll("[role='radio']")]
        .map((r) => r.closest("label"))
        .filter((l): l is HTMLLabelElement => !!l)
        .slice(0, 3)
        .map((l) => {
          const value = l.querySelector("[role='radio']")?.getAttribute("value") || "";
          const icon = [...l.querySelectorAll("svg")].find(
            (s) => !s.closest("[role='radio']"),
          );
          const r = icon ? icon.getBoundingClientRect() : null;
          return {
            value,
            iconCls: icon ? icon.getAttribute("class") || "" : null,
            iconW: r ? Math.round(r.width) : 0,
            iconColor: icon ? getComputedStyle(icon).color : null,
            tileH: Math.round(l.getBoundingClientRect().height),
          };
        });
    });
    expect(tiles).toHaveLength(3);
    const byValue = Object.fromEntries(tiles.map((t) => [t.value, t]));
    expect(byValue.need).toBeDefined();
    expect(byValue.want).toBeDefined();
    expect(byValue.savings).toBeDefined();
    // 16px icons with the measured lucide names…
    expect(byValue.need.iconCls).toContain("lucide-circle-alert");
    expect(byValue.want.iconCls).toContain("lucide-heart");
    expect(byValue.savings.iconCls).toContain("lucide-piggy-bank");
    for (const t of tiles) expect(t.iconW).toBe(16);
    // …in the per-classification accent colors (the measured rgb values).
    expect(byValue.need.iconColor).toBe("rgb(224, 122, 59)");
    expect(byValue.want.iconColor).toBe("rgb(59, 126, 161)");
    expect(byValue.savings.iconColor).toBe("rgb(143, 188, 63)");
    // The tile geometry pin holds with the icon present (16px icon =
    // the radio's height — height-neutral).
    for (const t of tiles) expect(t.tileH).toBe(52);
  });

  test("calculator dialog X is 36×36 with a 16px icon", async ({ page }) => {
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();
    const rent = page.locator("main .group", { hasText: "Rent" }).first();
    await rent.hover();
    await page.getByRole("button", { name: "Calculate" }).first().click();
    const dialog = page.locator('[role="dialog"]');
    await expect(dialog).toBeVisible();

    const x = await page.evaluate(() => {
      const d = document.querySelector('[role="dialog"]')!;
      const btn = [...d.querySelectorAll('button[aria-label="Close"]')].find(
        (b) => b.closest('[role="dialog"]') === d,
      );
      if (!btn) return null;
      const r = btn.getBoundingClientRect();
      const svg = btn.querySelector("svg");
      return {
        w: Math.round(r.width),
        h: Math.round(r.height),
        svgW: svg ? Math.round(svg.getBoundingClientRect().width) : null,
      };
    });
    expect(x).not.toBeNull();
    expect(x!.w).toBe(36);
    expect(x!.h).toBe(36);
    expect(x!.svgW).toBe(16);
  });

  test("the recurring row renders the reference's switch-left tinted layout (v19)", async ({
    page,
  }) => {
    // Found by the v19 VLM visual sweep and DOM-verified on both sites
    // (docs/remediation-plan-v19.md G1): the reference renders the
    // recurring-toggle row with the SWITCH on the LEFT (the row's first
    // child, 12px gap to the text block), NO calendar icon, NO border,
    // and a green-tinted rgb(245,248,245) background — h 72, radius 8,
    // p-4. The pre-fix clone ran icon + label left, switch right
    // (justify-between), 1px border, transparent bg, h 74.
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.locator('[role="dialog"]');
    await expect(dialog).toBeVisible();

    const row = await page.evaluate(() => {
      const d = document.querySelector('[role="dialog"]')!;
      const sw = d.querySelector('[role="switch"]');
      if (!sw) return null;
      const row = sw.parentElement!;
      const rr = row.getBoundingClientRect();
      const cs = getComputedStyle(row);
      // the switch's position among the row's ELEMENT children (the
      // hidden input sits inside the Radix structure; compare against
      // element children the way the DOM probe did).
      const kids = [...row.children].filter((c) => c.tagName !== "INPUT");
      const swIdx = kids.indexOf(sw);
      const labelBlock = kids.find(
        (c) => (c.textContent || "").includes("Recurring Item"),
      );
      const sr = sw.getBoundingClientRect();
      const lr = labelBlock ? labelBlock.getBoundingClientRect() : null;
      return {
        swIdx,
        swX: Math.round(sr.x - rr.x),
        labelX: lr ? Math.round(lr.x - rr.x) : null,
        labelRightOfSwitch: lr ? lr.x > sr.x + sr.width : null,
        h: Math.round(rr.height),
        borderWidth: cs.borderWidth,
        bg: cs.backgroundColor,
        radius: cs.borderRadius,
        svgCount: row.querySelectorAll("svg").length,
        gap: cs.gap || cs.columnGap,
      };
    });
    expect(row).not.toBeNull();
    // The switch is the row's FIRST element child (index 0 among
    // non-input children), LEFT of the label block, 16px from the row's
    // edge (p-4), with the label block AFTER it (reference: sw x=16,
    // label x=64, 12px gap).
    expect(row!.swIdx).toBe(0);
    expect(row!.swX).toBe(16);
    expect(row!.labelRightOfSwitch).toBe(true);
    // Borderless, green-tinted background, 72 tall, 8px radius.
    expect(row!.borderWidth).toBe("0px");
    expect(row!.bg).toBe("rgb(245, 248, 245)");
    expect(row!.h).toBe(72);
    expect(row!.radius).toBe("8px");
    // No icons in the row (the reference carries no calendar icon).
    expect(row!.svgCount).toBe(0);
    // 12px flex gap between the switch and the text block.
    expect(row!.gap).toBe("12px");
    await page.keyboard.press("Escape");
  });

  test("the line-item sub-dialog carries the reference's third family (v22 G2)", async ({
    page,
  }) => {
    // Measured live on the reference at BOTH viewports (the populated
    // Edit state — docs/remediation-plan-v22.md G2): the line-item
    // sub-dialog is the reference's THIRD dialog family — max-w-2xl +
    // max-h-[85vh] + overflow-y-auto + form p-6 space-y-5 (the calculator
    // family is max-w-3xl/85vh/overflow-hidden; the budget-item family is
    // max-w-2xl/90vh/overflow-y-auto + space-y-6). The pre-fix clone rode
    // the generic budget-item family: desktop panel 720 vs the reference's
    // 680 (90vh vs 85vh), form row gaps 24 vs 20.
    await page.goto("/expenses");
    await expect(page.getByRole("heading", { name: "Rent" })).toBeVisible();
    const rent = page.locator("main .group", { hasText: "Rent" }).first();
    await rent.hover();
    await page.getByRole("button", { name: "Calculate" }).first().click();
    const calc = page.locator('[role="dialog"]');
    await expect(calc).toBeVisible();
    await page.getByRole("button", { name: "Add First Item" }).click();
    const sub = page.locator('[role="dialog"]').nth(1);
    await expect(sub).toBeVisible();

    const family = await page.evaluate(() => {
      const dialogs = [...document.querySelectorAll('[role="dialog"]')];
      const d = dialogs[dialogs.length - 1];
      const cs = getComputedStyle(d);
      const form = d.querySelector("form")!;
      // The form's first-level row gap: the field-grid bottom → the Notes
      // block top (space-y-5 = 20px; the budget family's space-y-6 = 24).
      const grid = form.children[0] as HTMLElement;
      const notes = form.children[1] as HTMLElement;
      const gap = Math.round(
        notes.getBoundingClientRect().top - grid.getBoundingClientRect().bottom,
      );
      return {
        maxH: cs.maxHeight,
        vhCap: Math.round((parseFloat(cs.maxHeight) / innerHeight) * 100),
        formRowGap: gap,
      };
    });
    // The 85vh panel cap — NOT the budget-item family's 90vh (the
    // reference's measured cap at both viewports).
    expect(family.vhCap).toBe(85);
    // The form's 20px row gaps — NOT space-y-6's 24px.
    expect(family.formRowGap).toBe(20);
    // The budget-item dialog (the OTHER family) keeps its 90vh cap — this
    // test pins the split, not a global restyle.
    await page.keyboard.press("Escape");
    await page.keyboard.press("Escape");
    await page.getByRole("button", { name: "Add Expense" }).click();
    const itemDialog = page.locator('[role="dialog"]');
    await expect(itemDialog).toBeVisible();
    const itemCap = await page.evaluate(() => {
      const d = document.querySelector('[role="dialog"]')!;
      return Math.round((parseFloat(getComputedStyle(d).maxHeight) / innerHeight) * 100);
    });
    expect(itemCap).toBe(90);
  });
});
