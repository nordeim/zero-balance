import { expect, test } from "@playwright/test";

// Mobile navigation (390×844 — the reference's mobile chrome). This is the
// highest-regression-risk surface AND the home of the two reference bugs
// the clone fixes (the superset mandate):
//
//   1. TOASTER CLICK-BLOCK: on the reference, an empty toast viewport
//      (fixed, full-width, top 32px, z-100, pointer-events: auto) sits on
//      top of the hamburger's top half — the first tap of the hamburger at
//      (24,16) misses. The clone's viewport is pointer-events: none (the
//      sonner pattern), so a REAL Playwright click on the hamburger works.
//      A real .click() is the assertion: it hit-tests at the element's
//      center, which the reference's overlay would swallow.
//   2. SHEET STAYS OPEN AFTER NAV: on the reference, tapping a nav link in
//      the sheet changes the route but leaves the sheet + overlay up,
//      trapping the user. The clone closes the sheet on every navigation.
//
// Tailwind v4 note: the sheet's width uses the v4-native arbitrary-value
// with CSS var — w-(--sheet-width) — pinned to 18rem (288px), matching the
// reference's --sidebar-width in its sheet context.
// Contexts arrive AUTHENTICATED (setup-project storageState).

// A touch-enabled 390×844 chromium context.
test.use({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true });

test.describe("mobile navigation", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
  });

  test("mobile header shows the hamburger + brand title, no desktop rail", async ({ page }) => {
    await expect(page.getByRole("button", { name: "Toggle Sidebar" })).toBeVisible();
    await expect(page.getByRole("heading", { name: "ZeroBalance" })).toBeVisible();
    // The desktop rail is hidden below md (768px).
    await expect(page.locator("aside")).toBeHidden();
  });

  test("the empty toast viewport never blocks the hamburger (superset fix #1)", async ({
    page,
  }) => {
    // Computed-style proof: the toast viewport is pointer-events: none.
    const viewportStyle = await page.evaluate(() => {
      const el = document.querySelector<HTMLElement>(".zb-toast-viewport");
      if (!el) return null;
      const cs = getComputedStyle(el);
      return { pointerEvents: cs.pointerEvents, zIndex: cs.zIndex };
    });
    // If a viewport rendered, it must not intercept taps.
    if (viewportStyle) {
      expect(viewportStyle.pointerEvents).toBe("none");
    }

    // Behavioral proof: a REAL click on the hamburger opens the sheet —
    // Playwright clicks hit-test the point, so an overlay at the button's
    // center would time out with "element intercepts pointer events".
    await page.getByRole("button", { name: "Toggle Sidebar" }).click();
    const sheet = page.locator("[data-state='open'].fixed.inset-y-0");
    await expect(sheet).toBeVisible();
  });

  test("the sheet opens at the reference geometry (288px, left-anchored)", async ({ page }) => {
    await page.getByRole("button", { name: "Toggle Sidebar" }).click();
    const sheet = page.locator("[data-state='open'].fixed.inset-y-0");
    await expect(sheet).toBeVisible();
    // Let the 500ms slide-in-from-left entrance animation settle —
    // measuring mid-flight reports the translated (-78px…) position.
    await page.waitForTimeout(700);

    // 18rem = 288px — the reference's --sidebar-width for the sheet.
    // (isMobile viewports report subpixel widths — 287.999… — so round.)
    const box = await sheet.boundingBox();
    expect(Math.round(box?.width ?? 0)).toBe(288);
    expect(Math.round(box?.x ?? 0)).toBe(0);
    expect(Math.round(box?.y ?? 0)).toBe(0);
    expect(Math.round(box?.height ?? 0)).toBe(844);

    // The overlay dims the page behind the sheet.
    const overlay = page.locator("[data-state='open'].fixed.inset-0:not(.inset-y-0)").first();
    await expect(overlay).toBeVisible();

    // Sheet content: brand, all five nav items, the user footer.
    await expect(sheet.getByText("ZeroBalance").first()).toBeVisible();
    await expect(sheet.getByText("Budget Planner").first()).toBeVisible();
    for (const label of ["Dashboard", "Income", "Expenses", "Savings", "Net Worth"]) {
      await expect(sheet.getByRole("link", { name: label, exact: true })).toBeVisible();
    }
    await expect(sheet.getByText("Budget Pro")).toBeVisible();
    await expect(sheet.getByText("Track your finances")).toBeVisible();
  });

  test("tapping a nav link navigates AND closes the sheet (superset fix #2)", async ({ page }) => {
    await page.getByRole("button", { name: "Toggle Sidebar" }).click();
    const sheet = page.locator("[data-state='open'].fixed.inset-y-0");
    await expect(sheet).toBeVisible();

    // Tap the Income link inside the sheet.
    await sheet.getByRole("link", { name: "Income", exact: true }).tap();

    // Route changed…
    await expect(page).toHaveURL(/\/income$/);
    await expect(page.getByRole("heading", { name: "Income" })).toBeVisible();
    // …and the sheet + overlay are GONE (the reference leaves them up).
    await expect(sheet).toBeHidden();
    await expect(page.locator("[data-state='open'].fixed.inset-0")).toHaveCount(0);
  });

  test("Escape and overlay taps also close the sheet", async ({ page }) => {
    await page.getByRole("button", { name: "Toggle Sidebar" }).click();
    const sheet = page.locator("[data-state='open'].fixed.inset-y-0");
    await expect(sheet).toBeVisible();

    await page.keyboard.press("Escape");
    await expect(sheet).toBeHidden();

    // Overlay tap path.
    await page.getByRole("button", { name: "Toggle Sidebar" }).click();
    await expect(sheet).toBeVisible();
    await page.mouse.click(370, 500); // right of the 288px sheet
    await expect(sheet).toBeHidden();
  });

  test("every nav link is reachable through the sheet without a stuck overlay", async ({
    page,
  }) => {
    for (const [label, url, heading] of [
      ["Income", "/income", "Income"],
      ["Expenses", "/expenses", "Expenses"],
      ["Savings", "/savings", "Savings"],
      ["Net Worth", "/networth", "Net Worth"],
      ["Dashboard", "/dashboard", "Budget Dashboard"],
    ] as const) {
      await page.getByRole("button", { name: "Toggle Sidebar" }).click();
      const sheet = page.locator("[data-state='open'].fixed.inset-y-0");
      await expect(sheet).toBeVisible();
      await sheet.getByRole("link", { name: label, exact: true }).tap();
      await expect(page).toHaveURL(new RegExp(`${url}$`));
      await expect(page.getByRole("heading", { name: heading })).toBeVisible();
      await expect(sheet).toBeHidden();
    }
  });
});

test.describe("desktop navigation (≥768px)", () => {
  // This file's test.use pins a mobile viewport; re-pin per describe.
  test.use({ viewport: { width: 1280, height: 800 } });

  test("the fixed 256px rail replaces the mobile chrome", async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();

    const rail = page.locator("aside");
    await expect(rail).toBeVisible();
    const box = await rail.boundingBox();
    expect(box?.width).toBe(256); // 16rem
    expect(box?.x).toBe(0);

    // No hamburger, no mobile header.
    await expect(page.getByRole("button", { name: "Toggle Sidebar" })).toBeHidden();

    // The active item carries the forest→lime gradient + white text.
    const active = rail.locator("a[aria-current='page']");
    await expect(active).toHaveAttribute("href", "/dashboard");
    const bg = await active.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(45, 90, 74)");
  });
});
