import { expect, test } from "@playwright/test";

// Loading-state parity (v15 G1 — measured live on the reference): a FULL
// page load shows a DOM-replacing full-screen spinner while the data
// fetches. The reference's #root contains ONLY the overlay + its toast
// viewport (no rail, no header, no main), the body behind is white, and
// the spinner is the slate ring:
//
//   <div class="fixed inset-0 flex items-center justify-center">
//     <div class="w-8 h-8 border-4 border-slate-200 border-t-slate-800
//                 rounded-full animate-spin"></div>
//   </div>
//
// computed: 32×32 border-box, 4px borders (slate-200 rgb(226,232,240) on
// three sides, slate-800 rgb(30,41,59) on TOP), radius 9999px, spin 1s
// linear infinite, centered at the viewport midpoint. The spinner covers
// the DATA fetch — it stays up until the figures render, not just until
// the session probe resolves.
//
// Trigger: full-page loads ONLY. Client-side navigations show no spinner
// on either site (the store persists; booted stays true) — pinned by the
// last spec. /login never shows one (it doesn't mount the AppShell).
//
// Route delays reproduce the reference's network window: the specs
// intercept the API endpoints and hold them briefly. No fixture impact —
// the handlers only delay, never write.

/** Delay every matching API request by `ms` (read-only — always continues). */
async function delayRoutes(page: import("@playwright/test").Page, ms: number) {
  await page.route("**/api/auth/me", async (route) => {
    await page.waitForTimeout(ms);
    await route.continue();
  });
  for (const path of ["budget-items", "assets", "liabilities"]) {
    await page.route(`**/api/${path}`, async (route) => {
      await page.waitForTimeout(ms);
      await route.continue();
    });
  }
}

test.describe("loading state (v15)", () => {
  test("full-page loading state renders the reference's spinner overlay (v15 G1)", async ({ page }) => {
    await delayRoutes(page, 1200);
    await page.goto("/");

    // The overlay exists with the reference's chrome: fixed, full-viewport,
    // flex-centered, WHITE behind (the reference's pre-app body — its warm
    // background only mounts with the shell).
    const overlay = page.locator("div.fixed.inset-0");
    await expect(overlay).toBeVisible();
    const overlayState = await page.evaluate(() => {
      const ov = document.querySelector("div.fixed.inset-0");
      if (!ov) return null;
      const cs = getComputedStyle(ov);
      const r = ov.getBoundingClientRect();
      return {
        position: cs.position,
        display: cs.display,
        justifyContent: cs.justifyContent,
        alignItems: cs.alignItems,
        background: cs.backgroundColor,
        w: Math.round(r.width),
        h: Math.round(r.height),
        cx: Math.round(r.x + r.width / 2),
        cy: Math.round(r.y + r.height / 2),
        spinner: (() => {
          const sp = ov.querySelector("div[role='status']") || ov.querySelector("div");
          if (!sp) return null;
          const scs = getComputedStyle(sp);
          const sr = sp.getBoundingClientRect();
          return {
            offsetW: (sp as HTMLElement).offsetWidth,
            offsetH: (sp as HTMLElement).offsetHeight,
            borderTop: scs.borderTopWidth + " " + scs.borderTopColor,
            borderRight: scs.borderRightColor,
            borderBottom: scs.borderBottomColor,
            borderLeft: scs.borderLeftColor,
            borderW: [scs.borderTopWidth, scs.borderRightWidth, scs.borderBottomWidth, scs.borderLeftWidth],
            radius: scs.borderRadius,
            anim: `${scs.animationName} ${scs.animationDuration} ${scs.animationTimingFunction} ${scs.animationIterationCount}`,
            cx: Math.round(sr.x + sr.width / 2),
            cy: Math.round(sr.y + sr.height / 2),
            role: sp.getAttribute("role"),
            ariaLabel: sp.getAttribute("aria-label"),
          };
        })(),
        shell: {
          aside: !!document.querySelector("aside"),
          header: !!document.querySelector("header"),
          main: !!document.querySelector("main"),
        },
      };
    });
    expect(overlayState).toBeTruthy();
    expect(overlayState!.position).toBe("fixed");
    expect(overlayState!.display).toBe("flex");
    expect(overlayState!.justifyContent).toBe("center");
    expect(overlayState!.alignItems).toBe("center");
    // The reference's observable loading background is white.
    expect(overlayState!.background).toBe("rgb(255, 255, 255)");
    // Full-viewport overlay, spinner centered at the viewport midpoint
    // (Playwright's Desktop Chrome context is 1280×720 — read it live).
    const vp = await page.evaluate(() => ({ w: window.innerWidth, h: window.innerHeight }));
    expect(overlayState!.w).toBeGreaterThanOrEqual(vp.w);
    expect(overlayState!.h).toBeGreaterThanOrEqual(vp.h);
    const spinner = overlayState!.spinner!;
    expect(spinner.offsetW).toBe(32);
    expect(spinner.offsetH).toBe(32);
    // 4px borders; the TOP side carries the dark "spoke" (slate-800),
    // the other three the light track (slate-200).
    expect(spinner.borderW).toEqual(["4px", "4px", "4px", "4px"]);
    expect(spinner.borderTop).toBe("4px rgb(30, 41, 59)");
    expect(spinner.borderRight).toBe("rgb(226, 232, 240)");
    expect(spinner.borderBottom).toBe("rgb(226, 232, 240)");
    expect(spinner.borderLeft).toBe("rgb(226, 232, 240)");
    expect(spinner.radius).toBe("9999px");
    expect(spinner.anim).toBe("spin 1s linear infinite");
    // Centered at the live viewport midpoint.
    expect(spinner.cx).toBe(vp.w / 2);
    expect(spinner.cy).toBe(vp.h / 2);
    // The a11y superset (documented class — the reference has no aria).
    expect(spinner.role).toBe("status");
    expect(spinner.ariaLabel).toBe("Loading");
    // DOM replacement: no shell is mounted while loading (the reference's
    // #root holds ONLY the overlay + toast viewport).
    expect(overlayState!.shell.aside).toBe(false);
    expect(overlayState!.shell.header).toBe(false);
    expect(overlayState!.shell.main).toBe(false);
    // The delayed routes may still be mid-flight — unhook them.
    await page.unrouteAll({ behavior: "ignoreErrors" });
  });

  test("the spinner persists while the data is in flight — not just the session probe (v15 G1)", async ({ page }) => {
    // The session probe resolves instantly; the data routes are held 1200ms.
    // The OLD behavior flipped booted after /api/auth/me — the spinner
    // vanished and the views rendered empty before the data popped in.
    await page.route("**/api/auth/me", async (route) => {
      await route.continue();
    });
    for (const path of ["budget-items", "assets", "liabilities"]) {
      await page.route(`**/api/${path}`, async (route) => {
        await page.waitForTimeout(1200);
        await route.continue();
      });
    }
    await page.goto("/");

    // t+400ms: the session probe has long resolved, the data is still in
    // flight — the overlay must STILL be up and no money painted.
    await page.waitForTimeout(400);
    expect(await page.locator("div.fixed.inset-0").count()).toBe(1);
    expect(await page.locator("main").count()).toBe(0);
    expect(await page.getByText(/\$[\d,]+\.\d{2}/).count()).toBe(0);

    // After the delay: the overlay unmounts and the seeded dashboard's
    // hero figure renders (the seed's exact arithmetic).
    await expect(page.locator("div.fixed.inset-0")).toHaveCount(0, { timeout: 15_000 });
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
    await expect(page.getByText("+$2065.00")).toBeVisible();
    await page.unrouteAll({ behavior: "ignoreErrors" });
  });

  test("client-side navigation shows NO spinner (v15 G1)", async ({ page }) => {
    // First load: hold the data briefly so the overlay is observable, then
    // let it resolve; then click a rail link — the store persists and
    // booted stays true, so the overlay must NOT reappear.
    await delayRoutes(page, 400);
    await page.goto("/");
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
    await page.getByRole("link", { name: "Income" }).click();
    await expect(page.getByRole("heading", { name: "Income", level: 1 })).toBeVisible();
    // No overlay, no spinner: the data was already in the store.
    await expect(page.locator("div.fixed.inset-0")).toHaveCount(0);
    expect(await page.locator("div[role='status']").count()).toBe(0);
    // The income view renders its seeded card (not an empty state).
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    // The client-side re-boot fetch (AppShell re-mounts per route; the
    // store persists) may still be mid-flight through the delayed routes —
    // unhook them so the route callbacks don't outlive the test.
    await page.unrouteAll({ behavior: "ignoreErrors" });
  });
});

// A touch-enabled 390×844 context — the reference's mobile loading overlay
// measures 390×844 with the same spinner chrome.
test.describe("loading state mobile (v15)", () => {
  test.use({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true });

  test("mobile loading overlay covers the viewport (v15 G1)", async ({ page }) => {
    await delayRoutes(page, 1200);
    await page.goto("/");
    const overlay = page.locator("div.fixed.inset-0");
    await expect(overlay).toBeVisible();
    const state = await page.evaluate(() => {
      const ov = document.querySelector("div.fixed.inset-0");
      if (!ov) return null;
      const cs = getComputedStyle(ov);
      const r = ov.getBoundingClientRect();
      const sp = ov.querySelector("div[role='status']") || ov.querySelector("div");
      const scs = sp ? getComputedStyle(sp) : null;
      return {
        w: Math.round(r.width),
        h: Math.round(r.height),
        innerH: window.innerHeight,
        background: cs.backgroundColor,
        spinnerOffsetW: sp ? (sp as HTMLElement).offsetWidth : 0,
        spinnerBorderTop: scs ? scs.borderTopWidth + " " + scs.borderTopColor : "",
        spinnerRadius: scs ? scs.borderRadius : "",
        shell: {
          aside: !!document.querySelector("aside"),
          header: !!document.querySelector("header"),
          main: !!document.querySelector("main"),
        },
      };
    });
    expect(state).toBeTruthy();
    expect(state!.w).toBe(390);
    expect(state!.h).toBeGreaterThanOrEqual(state!.innerH);
    expect(state!.background).toBe("rgb(255, 255, 255)");
    expect(state!.spinnerOffsetW).toBe(32);
    expect(state!.spinnerBorderTop).toBe("4px rgb(30, 41, 59)");
    expect(state!.spinnerRadius).toBe("9999px");
    expect(state!.shell.aside).toBe(false);
    expect(state!.shell.header).toBe(false);
    expect(state!.shell.main).toBe(false);
    await page.unrouteAll({ behavior: "ignoreErrors" });
  });
});
