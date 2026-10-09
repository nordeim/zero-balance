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

  test("card action menus render PLAIN-TEXT items — no icons (v6 G1/G2/G14)", async ({ page }) => {
    // The reference's card menus (income items AND net-worth asset/liability
    // cards) render Edit/Delete as plain text — zero SVGs, label starting at
    // the item's left padding. The clone rendered pencil/trash icons.
    const menuShape = () =>
      page.evaluate(() => {
        const menu = document.querySelector('[role="menu"]');
        if (!menu) return null;
        const grab = (txt: string) => {
          const el = [...menu.querySelectorAll('[role="menuitem"]')].find(
            (x) => (x.textContent || "").trim() === txt,
          );
          if (!el) return null;
          const r = el.getBoundingClientRect();
          const label = el.firstChild?.textContent ?? "";
          return {
            svg: el.querySelectorAll("svg").length,
            color: getComputedStyle(el).color,
            labelStartsText: /^\s*(Edit|Delete)\s*$/.test((el.textContent || "")),
            itemX: Math.round(r.x),
          };
        };
        return { edit: grab("Edit"), del: grab("Delete") };
      });

    // 1. Income card menu (item-card).
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    const card = page.locator("main .group", { hasText: "Salary" }).first();
    await card.hover();
    await page.getByRole("button", { name: "Actions for Salary" }).click({ force: true });
    await expect(page.locator('[role="menu"]')).toBeVisible();
    let shape = await menuShape();
    expect(shape!.edit!.svg).toBe(0);
    expect(shape!.del!.svg).toBe(0);
    expect(shape!.edit!.color).toBe("rgb(10, 10, 10)");
    expect(shape!.del!.color).toBe("rgb(220, 38, 38)");
    // The trigger carries the reference's hover:text-accent-foreground (G14).
    const trigCls = await page.evaluate(() => {
      const b = [...document.querySelectorAll('button[aria-label="Actions for Salary"]')][0];
      return b ? b.className : null;
    });
    expect(trigCls).toContain("hover:text-accent-foreground");
    await page.keyboard.press("Escape");

    // 2. Net-worth asset menu — same plain-text shape, and its Delete must
    // compute plain rgb (the old named text-red-600 emitted lab()).
    await page.goto("/networth");
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    const aCard = page.locator("main .group", { hasText: "Share Portfolio" }).first();
    await aCard.hover();
    await aCard.getByRole("button", { name: "Actions for Share Portfolio" }).click({ force: true });
    await expect(page.locator('[role="menu"]')).toBeVisible();
    shape = await menuShape();
    expect(shape!.edit!.svg).toBe(0);
    expect(shape!.del!.svg).toBe(0);
    expect(shape!.del!.color).toBe("rgb(220, 38, 38)");
    await page.keyboard.press("Escape");
  });
});

// ---------------------------------------------------------------------------
// v9 — primitive chrome: the radio/switch #171717 family + the 9999px radius
// convention (docs/remediation-plan-v9.md G5/G6).
//
// Measured live on the reference's Add Budget Item dialog:
//   Radio circle: 16px, border rgb(23,23,23) (its --primary is shadcn's
//     #171717, NOT brand forest), radius 9999px, focus-visible ring-1.
//   Switch (its own Recurring switch, flipped + measured + restored):
//     track 36×20, checked bg rgb(23,23,23), unchecked bg #e5e5e5 (input),
//     thumb 16px #ffffff with ring-0, translate-x-4.
//   rounded-full: the reference's build emits 9999px — v4's emits
//     calc(infinity * 1px) → 33554432px. Same surfaces, same classes; pin
//     the computed value (the v8 lab() doctrine applied to radii).
// ---------------------------------------------------------------------------

test.describe("primitive chrome (v9)", () => {
  test("radio circles render the #171717 primary, not brand forest", async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    await expect(page.locator('[role="dialog"]')).toBeVisible();

    const radio = await page.evaluate(() => {
      const r = document.querySelector('[role="dialog"] [role="radio"]');
      if (!r) return null;
      const cs = getComputedStyle(r);
      return { border: cs.borderColor, w: cs.width, radius: cs.borderRadius };
    });
    expect(radio).not.toBeNull();
    // Reference: border-primary computes rgb(23,23,23) — the clone's brand
    // --primary (#1a3a2e forest) must not leak into the primitive.
    expect(radio!.border).toBe("rgb(23, 23, 23)");
    expect(radio!.w).toBe("16px");
    expect(radio!.radius).toBe("9999px");
  });

  test("the recurring switch renders the #171717 checked track + white thumb", async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    await page.getByRole("button", { name: "Add Income" }).click();
    const dialog = page.locator('[role="dialog"]');
    await expect(dialog).toBeVisible();

    const sw = dialog.locator('[role="switch"]');
    await expect(sw).toBeVisible();
    // Flip ON, then POLL the computed bg — the switch carries
    // `transition-colors` (150ms), so an immediate read races the animation
    // and returns the pre-flip value.
    await sw.click();
    await expect(sw).toHaveAttribute("aria-checked", "true");
    const readSwitch = () =>
      page.evaluate(() => {
        const s = document.querySelector('[role="dialog"] [role="switch"]')!;
        const thumb = s.querySelector("span")!;
        return { bg: getComputedStyle(s).backgroundColor, thumbBg: getComputedStyle(thumb).backgroundColor };
      });
    await expect.poll(async () => (await readSwitch()).bg).toBe("rgb(23, 23, 23)");
    const checked = await readSwitch();
    expect(checked.thumbBg).toBe("rgb(255, 255, 255)");
    await sw.click();
    await expect(sw).toHaveAttribute("aria-checked", "false");
    await expect.poll(async () => (await readSwitch()).bg).toBe("rgb(229, 229, 229)");
    const unchecked = await page.evaluate(() => {
      const s = document.querySelector('[role="dialog"] [role="switch"]')!;
      return { bg: getComputedStyle(s).backgroundColor, radius: getComputedStyle(s).borderRadius };
    });
    // Unchecked track: the input token #e5e5e5; track radius 9999px (the
    // reference's rounded-full, not v4's calc(infinity)).
    expect(unchecked.bg).toBe("rgb(229, 229, 229)");
    expect(unchecked.radius).toBe("9999px");
    await page.keyboard.press("Escape");
  });

  test("fully-rounded chrome computes 9999px, not v4 infinity (hero bar, avatar)", async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
    const radii = await page.evaluate(() => {
      // Hero allocation bar: the 12px-tall h-3 rounded track/fill (class now
      // pinned to rounded-[9999px] — the reference's computed value).
      const bar = [...document.querySelectorAll("main div")].find(
        (d) => {
          const r = d.getBoundingClientRect();
          return Math.round(r.height) === 12 && /rounded-\[9999px\]/.test((d as HTMLElement).className || "");
        },
      );
      // Rail avatar: the 36×36 rounded circle in the fixed aside.
      const avatar = [...document.querySelectorAll("aside div")].find(
        (d) => {
          const r = d.getBoundingClientRect();
          return Math.round(r.width) === 36 && /rounded-\[9999px\]/.test((d as HTMLElement).className || "");
        },
      );
      return {
        bar: bar ? getComputedStyle(bar).borderRadius : null,
        avatar: avatar ? getComputedStyle(avatar).borderRadius : null,
      };
    });
    // The reference's Tailwind emits 9999px; v4's rounded-full computes
    // calc(infinity * 1px) → 33554432px. Visually identical, computed-
    // style parity says pin the reference value.
    expect(radii.bar).toBe("9999px");
    expect(radii.avatar).toBe("9999px");
  });
});

test.describe("gradient Add-button chrome (v11)", () => {
  // The .zb-btn-add family (page-level / empty-state / net-worth /
  // dashboard Add buttons): measured live on the reference, every Plus
  // icon renders 16px (buttons 147/134/127 wide), the rest ambient is
  // v3's BARE shadow (two 0.1 layers), and hover changes NOTHING
  // (opacity stays 1 — the clone's 0.9 fade was a session-1 assumption).

  test("page Add buttons: 16px Plus icon, v3 bare-shadow ambient, no hover fade (G2/G3/G4)", async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();

    const topbar = await page.evaluate(() => {
      const b = [...document.querySelectorAll("main button")].find(
        (x) => (x.textContent || "").trim() === "Add Income" && x.getBoundingClientRect().top < 120,
      );
      if (!b) return null;
      const svg = b.querySelector("svg");
      return {
        svgW: svg ? Math.round(svg.getBoundingClientRect().width) : null,
        shadow: getComputedStyle(b).boxShadow,
      };
    });
    expect(topbar!.svgW).toBe(16);
    expect(topbar!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(topbar!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");

    // Real hover: opacity must stay 1 (reference has no hover change).
    await page.locator("main button", { hasText: "Add Income" }).first().hover();
    const hovered = await page.evaluate(() => {
      const b = [...document.querySelectorAll("main button")].find(
        (x) => (x.textContent || "").trim() === "Add Income" && x.getBoundingClientRect().top < 120,
      );
      return b ? { opacity: getComputedStyle(b).opacity, hover: b.matches(":hover") } : null;
    });
    expect(hovered!.hover).toBe(true);
    expect(hovered!.opacity).toBe("1");

    // The empty-state Add button carries the same 16px Plus (filter to zero).
    await page.getByPlaceholder("Search income items...").fill("zzz-no-match");
    await expect(page.getByText("No income items yet")).toBeVisible();
    const emptyAdd = await page.evaluate(() => {
      const b = [...document.querySelectorAll("main button")].filter(
        (x) => (x.textContent || "").trim() === "Add Income" && x.getBoundingClientRect().top > 200,
      )[0];
      if (!b) return null;
      const svg = b.querySelector("svg");
      return svg ? Math.round(svg.getBoundingClientRect().width) : null;
    });
    expect(emptyAdd).toBe(16);
    await page.getByPlaceholder("Search income items...").fill("");
  });

  test("net-worth Add Asset + dashboard Add Item: 16px Plus icons (G3)", async ({ page }) => {
    await page.goto("/networth");
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    const asset = await page.evaluate(() => {
      const b = [...document.querySelectorAll("main button")].find(
        (x) => (x.textContent || "").trim() === "Add Asset",
      );
      const svg = b?.querySelector("svg");
      return svg ? Math.round(svg.getBoundingClientRect().width) : null;
    });
    expect(asset).toBe(16);

    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
    const dash = await page.evaluate(() => {
      const b = [...document.querySelectorAll("main button")].find(
        (x) => (x.textContent || "").trim() === "Add Item",
      );
      const svg = b?.querySelector("svg");
      return svg ? Math.round(svg.getBoundingClientRect().width) : null;
    });
    expect(dash).toBe(16);
  });
});

// ---------------------------------------------------------------------------
// v25 — the app shell's warm paper + the body's white canvas
// (docs/remediation-plan-v25.md G3).
//
// Measured live up the DOM chain on both sites: the reference styles NO
// body background (browser-white canvas) and paints its warm #fafaf8
// paper on the app-shell wrapper (`min-h-screen flex w-full` →
// rgb(250,250,248)); its 404 page paints its own #f8fafc root (v21 pin).
// The clone had the paper on the BODY (the v7-era manifest read — the PWA
// splash color, not a rendered surface) — visually invisible (every page
// covers the body), but a real computed-style + layer-structure drift
// (the login body pinned in login-parity). This pin holds the corrected
// layering on an authenticated app page.
test.describe("app-shell warm paper + white body (v25 — plan G3)", () => {
  test("the shell wrapper paints #fafaf8 over a white body canvas", async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Income", exact: true })).toBeVisible();
    const layers = await page.evaluate(() => {
      const shell = [...document.querySelectorAll("body div")].find((d) =>
        /min-h-svh/.test((d as HTMLElement).className || "") && /flex/.test((d as HTMLElement).className || ""),
      );
      return {
        body: getComputedStyle(document.body).backgroundColor,
        shell: shell ? getComputedStyle(shell).backgroundColor : null,
      };
    });
    // The reference's layering: white body canvas + the warm paper on the
    // shell wrapper (rgb(250,250,248) — the same rendered color the app
    // pages always showed, now painted at the reference's layer).
    expect(layers.body).toBe("rgb(255, 255, 255)");
    expect(layers.shell).toBe("rgb(250, 250, 248)");
  });
});
