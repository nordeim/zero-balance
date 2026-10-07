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
