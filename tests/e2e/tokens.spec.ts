import { expect, test } from "@playwright/test";

// Neutral-token parity (session-8 audit, docs/remediation-plan-v5.md
// G1/G2/G5/G6/G9/G10): the reference's own :root ships shadcn's NEUTRAL
// scale — foreground 0 0% 3.9% (#0a0a0a), accent/muted 0 0% 96.1%
// (#f5f5f5), accent-foreground 0 0% 9% (#171717), input/border 0 0% 89.8%
// (#e5e5e5), sidebar-accent-foreground 240 5.9% 10% (#18181b), ring
// #0a0a0a and sidebar-ring #3b82f6 — measured live on its form controls,
// menus, nav hovers and focus rings. The clone had built these from
// zinc-ish hexes (#3f3f3f / #f0f2ee / #e5e7e3 / #1a3a2e), and three
// colored texts emitted as v4 lab()/oklab() where the reference emits
// plain rgb. These specs pin the token-level fix on real rendered surfaces.
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("neutral token parity (v5)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Income", exact: true })).toBeVisible();
  });

  test("select triggers render the reference neutral chrome (G1 + G2)", async ({ page }) => {
    const trigger = await page.evaluate(() => {
      const b = [...document.querySelectorAll("button")].find(
        (x) => (x.textContent || "").trim().startsWith("All Categories"),
      );
      if (!b) return null;
      const cs = getComputedStyle(b);
      const inner = b.querySelector("span");
      return {
        text: inner ? getComputedStyle(inner).color : cs.color,
        borderColor: cs.borderColor,
        borderWidth: cs.borderWidth,
      };
    });
    expect(trigger).not.toBeNull();
    // Reference trigger text: rgb(10, 10, 10) (their --foreground).
    expect(trigger!.text).toBe("rgb(10, 10, 10)");
    // Reference control border: rgb(229, 229, 229) (their --input token).
    expect(trigger!.borderColor).toBe("rgb(229, 229, 229)");
    expect(trigger!.borderWidth).toBe("1px");
  });

  test("dropdown menu hover + destructive item match the reference (G5 + G9)", async ({ page }) => {
    // Open the income card's ellipsis menu (hover-revealed, icon-only —
    // aria-label "Actions for {name}").
    const card = page.locator("main .group", { hasText: "Salary" }).first();
    await card.hover();
    await page.getByRole("button", { name: "Actions for Salary" }).click({ force: true });
    const menu = page.locator('[role="menu"]');
    await expect(menu).toBeVisible();

    const items = await page.evaluate(() => {
      const edit = [...document.querySelectorAll('[role="menuitem"]')].find(
        (x) => (x.textContent || "").trim() === "Edit",
      );
      const del = [...document.querySelectorAll('[role="menuitem"]')].find(
        (x) => (x.textContent || "").trim() === "Delete",
      );
      if (!edit || !del) return null;
      return {
        editRest: getComputedStyle(edit).color,
        deleteColor: getComputedStyle(del).color,
        editCls: edit.className,
        contentBorder: getComputedStyle(edit.closest('[role="menu"]')!).borderColor,
      };
    });
    expect(items).not.toBeNull();
    // Menu items rest at the near-black foreground (G1).
    expect(items!.editRest).toBe("rgb(10, 10, 10)");
    // Delete: the reference's red-600, plain rgb — not a v4 lab() emission (G9).
    expect(items!.deleteColor).toBe("rgb(220, 38, 38)");
    // Menu content border is the input neutral, not the card border (G2).
    expect(items!.contentBorder).toBe("rgb(229, 229, 229)");

    // Highlight the Edit item via the keyboard (deterministic — a mouse hover
    // can race the menu's zoom-in animation): Radix focuses the item, and the
    // item chrome (focus:bg-accent) renders the accent tint (G5).
    await page.keyboard.press("ArrowDown");
    await page.waitForTimeout(300); // transition-colors 150ms — let it settle
    const highlighted = await page.evaluate(() => {
      const edit = [...document.querySelectorAll('[role="menuitem"]')].find(
        (x) => (x.textContent || "").trim() === "Edit",
      );
      if (!edit) return null;
      return {
        bg: getComputedStyle(edit).backgroundColor,
        focused: document.activeElement === edit,
        color: getComputedStyle(edit).color,
      };
    });
    expect(highlighted).not.toBeNull();
    expect(highlighted!.focused).toBe(true);
    // Accent tint is neutral-100 with the near-black accent-foreground text.
    expect(highlighted!.bg).toBe("rgb(245, 245, 245)");
    expect(highlighted!.color).toBe("rgb(23, 23, 23)");
    await page.keyboard.press("Escape");
  });

  test("select dropdown highlighted item matches the reference (G5)", async ({ page }) => {
    await page.getByRole("combobox").first().click();
    const option = page.locator('[role="option"]').first();
    await expect(option).toBeVisible();
    const highlighted = await option.evaluate((el) => ({
      bg: getComputedStyle(el).backgroundColor,
      color: getComputedStyle(el).color,
    }));
    // Reference: neutral-100 highlight bg + neutral-900 text (their
    // accent/accent-foreground pair).
    expect(highlighted.bg).toBe("rgb(245, 245, 245)");
    expect(highlighted.color).toBe("rgb(23, 23, 23)");
    await page.keyboard.press("Escape");
  });

  test("nav hover text is zinc-900, not forest (G6)", async ({ page }) => {
    // /income: the Expenses link is inactive.
    const link = page.locator("nav a", { hasText: "Expenses" }).first();
    await link.hover();
    await page.waitForTimeout(300); // transition-all 200ms — let it settle
    const hovered = await link.evaluate((el) => ({
      bg: getComputedStyle(el).backgroundColor,
      color: getComputedStyle(el).color,
    }));
    // Reference hover: green-50 tint (v4 fix) + zinc-900 text (#18181b —
    // their sidebar-accent-foreground), NOT the clone's old forest.
    expect(hovered.bg).toBe("rgb(240, 253, 244)");
    expect(hovered.color).toBe("rgb(24, 24, 27)");
  });

  test("focus rings match the reference tokens (G10)", async ({ page }) => {
    // Search input: ring-ring (#0a0a0a on the reference).
    const search = page.getByPlaceholder("Search income items...");
    await search.click();
    const inputRing = await search.evaluate((el) => getComputedStyle(el).boxShadow);
    expect(inputRing).toContain("rgb(10, 10, 10)");

    // Nav link: ring-sidebar-ring (blue-500 #3b82f6 on the reference).
    // Walk backwards from the search input into the sidebar nav (the mobile
    // toggle is display:none at desktop, so the nav links are the previous
    // tab stops after the "Add Income" header button).
    let landed = false;
    for (let i = 0; i < 5; i++) {
      await page.keyboard.press("Shift+Tab");
      const hit = await page.evaluate(() => {
        const a = document.activeElement;
        return a && a.tagName === "A" && a.closest("nav");
      });
      if (hit) {
        landed = true;
        break;
      }
    }
    expect(landed).toBe(true);
    await page.waitForTimeout(300); // the ring animates in via transition-all
    const navRing = await page.evaluate(() => {
      const a = document.activeElement as HTMLAnchorElement;
      return { ring: getComputedStyle(a).boxShadow, text: (a.textContent || "").trim() };
    });
    expect(navRing.ring).toContain("rgb(59, 130, 246)");
  });

  test("hero white-alpha labels compute as plain rgba, not oklab (G9)", async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
    const labels = await page.evaluate(() => {
      const grab = (txt: string) => {
        const el = [...document.querySelectorAll("main span, main p")].find(
          (x) => (x.textContent || "").trim() === txt && x.querySelectorAll("*").length === 0,
        );
        return el ? getComputedStyle(el).color : null;
      };
      return { alloc: grab("Budget Allocation"), balance: grab("Balance") };
    });
    // The reference computes rgba(255, 255, 255, 0.8/0.6) — Tailwind v4's
    // text-white/NN emits oklab(0.999…). Pin the plain-rgba form.
    expect(labels.alloc).toBe("rgba(255, 255, 255, 0.8)");
    expect(labels.balance).toBe("rgba(255, 255, 255, 0.6)");
  });
});
