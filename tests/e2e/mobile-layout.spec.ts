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
});
