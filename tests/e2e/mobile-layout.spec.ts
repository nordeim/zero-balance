import { expect, test } from "@playwright/test";

// Mobile layout geometry (390×844) — pins the session-5 fix for the mobile
// top bar. Before the fix the <header> (md:hidden) rendered as a ROW-FLEX
// SIBLING of <main> inside div.flex.min-h-svh: at mobile widths it became a
// 222px full-height column, squeezing main to 214px and pushing
// document.scrollWidth to 480. The reference nests the header INSIDE main
// (stacked above the content), 61px tall, full width (see
// docs/remediation-plan-v3.md F1).
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.use({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true });

test.describe("mobile layout geometry", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
  });

  test("the document does not overflow horizontally", async ({ page }) => {
    const dims = await page.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
    }));
    expect(dims.scrollWidth).toBeLessThanOrEqual(dims.clientWidth + 1);
  });

  test("main takes the full viewport width with the top bar stacked above the content", async ({
    page,
  }) => {
    const geo = await page.evaluate(() => {
      const main = document.querySelector("main");
      const header = document.querySelector("header");
      const h1 = [...document.querySelectorAll("h1")].find((h) =>
        (h.textContent || "").trim().startsWith("Budget Dashboard"),
      );
      if (!main || !header || !h1) return null;
      const mr = main.getBoundingClientRect();
      const hr = header.getBoundingClientRect();
      const hr1 = h1.getBoundingClientRect();
      return {
        main: { x: mr.x, width: mr.width },
        header: { x: hr.x, y: hr.y, width: hr.width, height: hr.height },
        // The header must be INSIDE main (reference structure) and above the
        // page heading.
        headingBelowHeader: hr1.y >= hr.bottom - 1,
        headingWidth: hr1.width,
        headerInMain: main.contains(header),
      };
    });
    expect(geo).not.toBeNull();
    expect(geo!.main.x).toBe(0);
    expect(geo!.main.width).toBeGreaterThanOrEqual(389);
    expect(geo!.headerInMain).toBe(true);
    expect(geo!.header.x).toBe(0);
    expect(geo!.header.width).toBeGreaterThanOrEqual(389);
    // Reference height: py-4 (32) + 28px button + 1px border = 61px.
    expect(geo!.header.height).toBeLessThanOrEqual(65);
    expect(geo!.headingBelowHeader).toBe(true);
    // The dashboard content is NOT squeezed into a side column.
    expect(geo!.headingWidth).toBeGreaterThanOrEqual(300);
  });

  test("the hamburger matches the reference chrome (28px panel-left button, sr-only name, text-xl brand)", async ({
    page,
  }) => {
    const chrome = await page.evaluate(() => {
      const btn = [...document.querySelectorAll("button")].find((b) =>
        (b.getAttribute("aria-label") ?? "").includes("Toggle Sidebar") ||
        (b.textContent || "").includes("Toggle Sidebar"),
      );
      const brand = document.querySelector("header h1");
      if (!btn || !brand) return null;
      const br = btn.getBoundingClientRect();
      const cs = getComputedStyle(btn);
      const icon = btn.querySelector("svg");
      const iconCls = icon ? icon.getAttribute("class") || "" : "";
      const brandCls = brand.className || "";
      return {
        w: br.width,
        h: br.height,
        borderRadius: cs.borderRadius,
        icon: iconCls,
        brandText: brand.textContent?.trim(),
        brandCls,
      };
    });
    expect(chrome).not.toBeNull();
    // Reference button: h-7 w-7 p-2 rounded-lg (28×28, 8px radius).
    expect(chrome!.w).toBeLessThanOrEqual(30);
    expect(chrome!.h).toBeLessThanOrEqual(30);
    expect(chrome!.borderRadius).toBe("8px");
    // Reference icon: lucide-panel-left at 16px ([&_svg]:size-4).
    expect(chrome!.icon).toContain("lucide-panel-left");
    // Reference brand: text-xl font-bold.
    expect(chrome!.brandCls).toContain("text-xl");
    expect(chrome!.brandText).toBe("ZeroBalance");
  });

  test("the items-view Add button is auto-width and the header gap is 32px (v20 G1)", async ({
    page,
  }) => {
    // Found by the v20 mobile VLM sweep and DOM-verified on both sites
    // (docs/remediation-plan-v20.md G1): the reference's items-view header
    // row runs `flex flex-col md:flex-row justify-between items-start
    // md:items-center gap-4 mb-8` — base items-start blocks the flex-col
    // cross-axis stretch (the Add button stays auto-width: 147/155/150px
    // on income/expenses/savings), and mb-8 sets the header→filter-card
    // gap at 32px. The clone's row had drifted to a bare flex-col (the
    // button stretched to 358px full-width) + mb-6 (a 24px gap, both
    // viewports). The clone's DASHBOARD header row already carries the
    // reference pattern; this pins it for the items views.
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Income" })).toBeVisible();

    const mobile = await page.evaluate(() => {
      const btn = [...document.querySelectorAll("main button")].find((b) =>
        /^add income/i.test((b.textContent || "").trim()),
      );
      if (!btn) return null;
      const row = btn.parentElement as HTMLElement;
      const next = row.nextElementSibling;
      const br = btn.getBoundingClientRect();
      const cs = getComputedStyle(row);
      return {
        btnW: Math.round(br.width),
        btnH: Math.round(br.height),
        rowMarginBottom: cs.marginBottom,
        rowAlignItems: cs.alignItems,
        gap: next
          ? Math.round(next.getBoundingClientRect().top - row.getBoundingClientRect().bottom)
          : null,
      };
    });
    expect(mobile).not.toBeNull();
    // Auto-width (the reference's measured 147): NOT stretched to the
    // 358px full-width column.
    expect(mobile!.btnW).toBeLessThan(200);
    expect(mobile!.btnH).toBe(36);
    // mb-8: 32px below the header row at BOTH viewports.
    expect(mobile!.rowMarginBottom).toBe("32px");
    expect(mobile!.gap).toBe(32);
    // Base items-start (the reference's class; md:items-center overrides
    // at ≥768 — the cross-axis stretch is what made the button full-width).
    expect(mobile!.rowAlignItems).toBe("flex-start");

    // Desktop companion: the same 32px gap at 1280×800 (the v20 audit
    // measured the ref's filter card at nextTop 124 vs the clone's 116).
    await page.setViewportSize({ width: 1280, height: 800 });
    const desktop = await page.evaluate(() => {
      const btn = [...document.querySelectorAll("main button")].find((b) =>
        /^add income/i.test((b.textContent || "").trim()),
      );
      if (!btn) return null;
      const row = btn.parentElement as HTMLElement;
      const next = row.nextElementSibling;
      const br = btn.getBoundingClientRect();
      return {
        btnW: Math.round(br.width),
        gap: next
          ? Math.round(next.getBoundingClientRect().top - row.getBoundingClientRect().bottom)
          : null,
      };
    });
    expect(desktop).not.toBeNull();
    expect(desktop!.btnW).toBe(147);
    expect(desktop!.gap).toBe(32);
  });
});

// v108 — the MOBILE TOPBAR's interior junction census at 390 (plan F4):
// the never-pinned family. The v7 G5 pin (mobile-navigation.spec.ts) holds
// the burger's box + icon color; the session-5 pins above hold the topbar's
// box GEOMETRY (h <= 65, x 0, full width, inside main) + the hamburger
// radius/icon CLASS + the brand CLASS — but the header's own chrome (pad
// 24/16, border-b 1px rgb(229,231,227), bg white, h 61), the interior
// row's flex chrome (flex/center/gap 16px), the burger's POSITION (the
// px-6/py-4 rhythm), and the brand h1's COMPUTED chrome (fs 20px/fw 700/
// lh 28px/forestDark) were never asserted at ANY viewport in ANY spec.
// Measured byte-identical on BOTH sides via the one-shot
// topbar-arbit-v108.sh census (the reference's own values: the panel-left
// glyph form documented since remediation-plan-v3/v7).
test.describe("mobile topbar interior census at 390 (v108 — plan F4)", () => {
  test("the header chrome + the row flex + the burger position + the brand computed chrome (the never-pinned family)", async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
    const census = await page.evaluate(() => {
      const btn = [...document.querySelectorAll("button")].find((b) =>
        (b.querySelector("svg")?.getAttribute("class") || "").includes("panel-left"),
      );
      if (!btn) return null;
      const header = btn.closest("header");
      if (!header) return null;
      const row = header.firstElementChild as HTMLElement;
      const brand = row.lastElementChild as HTMLElement;
      const icon = btn.querySelector("svg");
      const hcs = getComputedStyle(header);
      const rcs = getComputedStyle(row);
      const bcs = getComputedStyle(btn);
      const ics = icon ? getComputedStyle(icon) : null;
      const br = btn.getBoundingClientRect();
      const bc = getComputedStyle(brand);
      return {
        docSW: document.documentElement.scrollWidth,
        header: {
          h: Math.round(header.getBoundingClientRect().height),
          padX: hcs.paddingLeft,
          padY: hcs.paddingTop,
          borderBW: hcs.borderBottomWidth,
          borderBColor: hcs.borderBottomColor,
          bg: hcs.backgroundColor,
        },
        row: {
          display: rcs.display,
          align: rcs.alignItems,
          gap: rcs.columnGap,
          h: Math.round(row.getBoundingClientRect().height),
          childCount: row.children.length,
        },
        burger: {
          x: Math.round(br.x),
          y: Math.round(br.y),
          w: Math.round(br.width),
          h: Math.round(br.height),
          radius: bcs.borderRadius,
        },
        icon: ics ? { w: ics.width, h: ics.height, color: ics.color } : null,
        brand: {
          text: (brand.textContent || "").trim(),
          fs: bc.fontSize,
          fw: bc.fontWeight,
          lh: bc.lineHeight,
          color: bc.color,
        },
      };
    });
    expect(census).not.toBeNull();
    // The header's own chrome — the py-4/px-6/border-b arithmetic
    // (h 61 = 16 + 28 + 16 + 1 border). The header's w stays unpinned
    // (the reference reads 395 — its own documented dashboard overflow;
    // the clone pins the docSW guard below instead).
    expect(census!.header.h).toBe(61);
    expect(census!.header.padX).toBe("24px");
    expect(census!.header.padY).toBe("16px");
    expect(census!.header.borderBW).toBe("1px");
    expect(census!.header.borderBColor).toBe("rgb(229, 231, 227)");
    expect(census!.header.bg).toBe("rgb(255, 255, 255)");
    // The interior row's flex chrome — the never-pinned gap-4 rhythm.
    expect(census!.row.display).toBe("flex");
    expect(census!.row.align).toBe("center");
    expect(census!.row.gap).toBe("16px");
    expect(census!.row.h).toBe(28);
    expect(census!.row.childCount).toBe(2);
    // The burger's position — the px-6/py-4 junction arithmetic (the
    // first child's x/y; the brand's x-position stays UNPINNED per the
    // v107 xInRow lesson — position arithmetic co-moves with row
    // mutations, so pinning it would break the single-axis discipline).
    expect(census!.burger.x).toBe(24);
    expect(census!.burger.y).toBe(16);
    expect(census!.burger.w).toBe(28);
    expect(census!.burger.h).toBe(28);
    expect(census!.burger.radius).toBe("8px");
    // The icon glyph — the computed 16×16 box + the near-black stroke
    // (the v7 G5 pin holds w/color; this adds the h + the family context).
    expect(census!.icon!.w).toBe("16px");
    expect(census!.icon!.h).toBe("16px");
    expect(census!.icon!.color).toBe("rgb(10, 10, 10)");
    // The brand's COMPUTED chrome — the session-5 pin's class-only
    // text-xl/font-bold assertions never pinned the computed values.
    expect(census!.brand.text).toBe("ZeroBalance");
    expect(census!.brand.fs).toBe("20px");
    expect(census!.brand.fw).toBe("700");
    expect(census!.brand.lh).toBe("28px");
    expect(census!.brand.color).toBe("rgb(26, 58, 46)");
    // The superset invariant: the clone fits at 390 (the reference reads
    // 395 — its own documented dashboard overflow, the R-bug family).
    expect(census!.docSW).toBe(390);
  });
});
