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

    // Session-13 audit (plan v7 G5): the reference's toggle renders a 16px
    // panel-left icon in near-black rgb(10,10,10) — pinned with
    // [&_svg]:size-4 [&_svg]:shrink-0 so the padded 28px box cannot flex-
    // squeeze it (the clone's icon measured 12px, forestDark).
    const toggle = await page.evaluate(() => {
      const btn = [...document.querySelectorAll("button")].find((b) =>
        (b.querySelector("svg")?.getAttribute("class") || "").includes("panel-left"),
      );
      if (!btn) return null;
      const icon = btn.querySelector("svg");
      const cs = icon ? getComputedStyle(icon) : null;
      return {
        btnW: Math.round(btn.getBoundingClientRect().width),
        btnH: Math.round(btn.getBoundingClientRect().height),
        iconW: cs ? cs.width : null,
        iconColor: cs ? cs.color : null,
      };
    });
    expect(toggle).not.toBeNull();
    expect(toggle!.btnW).toBe(28);
    expect(toggle!.btnH).toBe(28);
    expect(toggle!.iconW).toBe("16px");
    expect(toggle!.iconColor).toBe("rgb(10, 10, 10)");
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

    // Session-13 audit (plan v7 G6): the reference's sheet borders with the
    // shadcn neutral #e5e5e5 (NOT the warm card border #e5e7e3) and its
    // overlay computes plain rgba(0,0,0,0.8) — v4's bg-black/80 drifts to
    // oklab, so the clone pins the color inline.
    const sheetChrome = await page.evaluate(() => {
      const sheet = document.querySelector<HTMLElement>("[data-state='open'].fixed.inset-y-0");
      const ov = document.querySelector<HTMLElement>("[data-state='open'].fixed.inset-0:not(.inset-y-0)");
      if (!sheet || !ov) return null;
      const scs = getComputedStyle(sheet);
      const ocs = getComputedStyle(ov);
      return {
        borderRight: `${scs.borderRightWidth} ${scs.borderRightColor}`,
        overlayBg: ocs.backgroundColor,
      };
    });
    expect(sheetChrome).not.toBeNull();
    expect(sheetChrome!.borderRight).toBe("1px rgb(229, 229, 229)");
    expect(sheetChrome!.overlayBg).toBe("rgba(0, 0, 0, 0.8)");

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

  test("the sheet highlights the CURRENT route like the reference (v10 — plan G1)", async ({
    page,
  }) => {
    // Session-19 audit (plan v10 G1): measured live on the reference's sheet
    // at /income — the Income link carries the FULL active style (the same
    // 135deg forest-medium→lime gradient as the desktop rail, white text,
    // fw 500) while the other four links stay inactive #3f3f46/400. The
    // clone's sheet suppressed highlighting since session 1
    // (highlightActive={false}); the fix lets the sheet share the rail's
    // active logic.
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Income", exact: true })).toBeVisible();
    await page.getByRole("button", { name: "Toggle Sidebar" }).click();
    const sheet = page.locator("[data-state='open'].fixed.inset-y-0");
    await expect(sheet).toBeVisible();

    const links = await sheet.evaluate(() => {
      const sheetEl = document.querySelector("[data-state='open'].fixed.inset-y-0");
      if (!sheetEl) return null;
      return ["Dashboard", "Income", "Expenses", "Savings", "Net Worth"].map((label) => {
        const a = [...sheetEl.querySelectorAll("a")].find(
          (el) => (el.textContent || "").trim() === label,
        );
        if (!a) return { label, missing: true };
        const cs = getComputedStyle(a);
        return {
          label,
          color: cs.color,
          fontWeight: cs.fontWeight,
          bgImage: cs.backgroundImage,
        };
      });
    });
    expect(links).not.toBeNull();
    const byLabel = Object.fromEntries((links!).map((l: any) => [l.label, l]));
    // The current route's link is ACTIVE: white + the reference's exact
    // gradient + medium weight.
    expect(byLabel["Income"].color).toBe("rgb(255, 255, 255)");
    expect(byLabel["Income"].fontWeight).toBe("500");
    expect(byLabel["Income"].bgImage).toBe(
      "linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))",
    );
    // The other four stay inactive: zinc-700 at regular weight, no gradient.
    for (const label of ["Dashboard", "Expenses", "Savings", "Net Worth"]) {
      expect(byLabel[label].color).toBe("rgb(63, 63, 70)");
      expect(byLabel[label].fontWeight).toBe("400");
      expect(byLabel[label].bgImage).toBe("none");
    }
  });

  test("the sheet highlights Dashboard on the root route (superset #3, v10)", async ({ page }) => {
    // The reference's own sheet marks nothing active on `/` (its active
    // check compares the pathname to `/dashboard` — the documented
    // root-route gap). The clone highlights Dashboard everywhere the
    // dashboard is on screen — rail AND sheet.
    await page.goto("/");
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
    await page.getByRole("button", { name: "Toggle Sidebar" }).click();
    const sheet = page.locator("[data-state='open'].fixed.inset-y-0");
    await expect(sheet).toBeVisible();

    const dash = await sheet.evaluate(() => {
      const sheetEl = document.querySelector("[data-state='open'].fixed.inset-y-0");
      const a = sheetEl
        ? [...sheetEl.querySelectorAll("a")].find(
            (el) => (el.textContent || "").trim() === "Dashboard",
          )
        : null;
      if (!a) return null;
      const cs = getComputedStyle(a);
      return { color: cs.color, fontWeight: cs.fontWeight, bgImage: cs.backgroundImage };
    });
    expect(dash).not.toBeNull();
    expect(dash!.color).toBe("rgb(255, 255, 255)");
    expect(dash!.fontWeight).toBe("500");
    expect(dash!.bgImage).toBe(
      "linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))",
    );
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

test.describe("hover semantics on touch-capable contexts (v5 — plan G7)", () => {
  // Tailwind v4 media-gates `hover:` utilities behind @media (hover: hover);
  // the reference's v3-era engine applies :hover on EVERY device. The pin
  // `@variant hover (&:hover)` in globals.css restores v3 semantics. This
  // spec runs in the mobile context (isMobile + hasTouch → hover: none)
  // and asserts the nav tint STILL applies — as it does on the reference.
  test("nav hover tint applies under hover:none emulation (v3 semantics)", async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();

    // Sanity: this context must really report hover: none.
    const hoverNone = await page.evaluate(() => matchMedia("(hover: none)").matches);
    expect(hoverNone).toBe(true);

    // Open the sheet and hover the Income link.
    await page.getByRole("button", { name: "Toggle Sidebar" }).click();
    const sheetLink = page.locator("a", { hasText: "Income" }).last();
    await expect(sheetLink).toBeVisible();
    await sheetLink.hover();
    await page.waitForTimeout(300); // transition-all 200ms — let it settle
    const hovered = await sheetLink.evaluate((el) => ({
      bg: getComputedStyle(el).backgroundColor,
      color: getComputedStyle(el).color,
    }));
    // Reference behavior: the green-50 tint + zinc-900 text render even
    // when the device reports no hover capability.
    expect(hovered.bg).toBe("rgb(240, 253, 244)");
    expect(hovered.color).toBe("rgb(24, 24, 27)");
  });
});
