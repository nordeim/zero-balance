import { expect, test } from "@playwright/test";

// Sidebar nav geometry (session-7 audit, docs/remediation-plan-v4.md G1–G3):
// the reference renders its nav links with shadcn SidebarMenuButton geometry —
// `h-8` (32px tall) — with gap-3 / px-3 / py-2.5 / rounded-lg on top, a
// `hover:bg-green-50` tint on INACTIVE links, and NO hover change on the
// ACTIVE link (its inline gradient outranks class hovers). The clone ran 40px
// links with a `hover:bg-sidebar-accent` (#f0f2ee) inactive tint and a
// `hover:opacity-90` dim on the active gradient.
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("sidebar nav geometry", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
  });

  test("nav links are 32px tall with the reference chrome (h-8)", async ({ page }) => {
    const geo = await page.evaluate(() => {
      const links = [...document.querySelectorAll("nav a")].filter((a) =>
        /^(Dashboard|Income|Expenses|Savings|Net Worth)$/.test((a.textContent || "").trim()),
      );
      if (!links.length) return null;
      const first = links[0] as HTMLAnchorElement;
      const r = first.getBoundingClientRect();
      const cs = getComputedStyle(first);
      return {
        count: links.length,
        height: r.height,
        padding: cs.padding,
        columnGap: cs.columnGap,
        fontSize: cs.fontSize,
        borderRadius: cs.borderRadius,
        cls: first.className,
      };
    });
    expect(geo).not.toBeNull();
    expect(geo!.count).toBe(5);
    // Reference: h-8 → 32px (py-2.5 padding is overridden by the fixed height).
    expect(geo!.height).toBe(32);
    expect(geo!.padding).toBe("10px 12px");
    expect(geo!.columnGap).toBe("12px");
    expect(geo!.fontSize).toBe("14px");
    expect(geo!.borderRadius).toBe("8px");
    // The class carries the reference height utility.
    expect(geo!.cls).toContain("h-8");
  });

  test("inactive nav links hover green-50, not sidebar-accent", async ({ page }) => {
    const cls = await page.evaluate(() => {
      const link = [...document.querySelectorAll("nav a")].find(
        (a) => (a.textContent || "").trim() === "Income",
      );
      return link ? link.className : null;
    });
    expect(cls).not.toBeNull();
    // Reference inactive hover: green-50 (#f0fdf4). Arbitrary-hex form —
    // v4 computes the named green-50 as oklab; the hex pins the computed
    // style to the reference's plain rgb(240, 253, 244) (plan v5 G6).
    expect(cls!).toContain("hover:bg-[#f0fdf4]");
    expect(cls!).not.toContain("hover:bg-sidebar-accent");
  });

  test("the active nav link keeps its gradient on hover (no opacity dim)", async ({ page }) => {
    const active = await page.evaluate(() => {
      const link = [...document.querySelectorAll("nav a")].find(
        (a) => (a.textContent || "").trim() === "Dashboard",
      );
      if (!link) return null;
      return {
        cls: link.className,
        backgroundImage: getComputedStyle(link).backgroundImage,
      };
    });
    expect(active).not.toBeNull();
    // Active: gradient via inline style + text-white + font-medium.
    expect(active!.backgroundImage).toContain("linear-gradient(135deg");
    expect(active!.cls).toContain("text-white");
    expect(active!.cls).toContain("font-medium");
    // Reference has NO hover dim on the active link.
    expect(active!.cls).not.toContain("hover:opacity-90");
  });

  // Session-13 audit (docs/remediation-plan-v7.md G4): the reference's rail
  // brand block renders a 40×40 forest-gradient tile with a 24px lucide-target
  // (white stroke) and the "ZeroBalance" H2 at text-lg (18px) — its nav
  // label consequently sits 4px lower than the clone's (which ran a 20px
  // hand-rolled target + text-base). Structural fidelity: the reference also
  // wraps the nav ul in a `div.w-full.text-sm`.
  test("brand block: 24px target icon, text-lg logo, ul in its text-sm wrapper (v7 G4)", async ({ page }) => {
    const brand = await page.evaluate(() => {
      const h2 = [...document.querySelectorAll("aside h2")].find(
        (h) => (h.textContent || "").trim() === "ZeroBalance",
      );
      if (!h2) return null;
      const tile = h2.parentElement?.previousElementSibling ?? null;
      const icon = tile?.querySelector("svg") ?? null;
      const ul = document.querySelector("nav ul");
      return {
        logo: { size: getComputedStyle(h2).fontSize, weight: getComputedStyle(h2).fontWeight },
        tile: tile
          ? {
              w: Math.round(tile.getBoundingClientRect().width),
              h: Math.round(tile.getBoundingClientRect().height),
              radius: getComputedStyle(tile).borderRadius,
              grad: getComputedStyle(tile).backgroundImage,
            }
          : null,
        icon: icon
          ? {
              w: getComputedStyle(icon).width,
              h: getComputedStyle(icon).height,
              stroke: getComputedStyle(icon).color,
            }
          : null,
        ulWrapperCls: ul?.parentElement?.className ?? null,
      };
    });
    expect(brand).not.toBeNull();
    // Reference: 24×24 icon (w-6 h-6), white; text-lg 18px/700 logo.
    expect(brand!.icon!.w).toBe("24px");
    expect(brand!.icon!.h).toBe("24px");
    expect(brand!.icon!.stroke).toBe("rgb(255, 255, 255)");
    expect(brand!.logo!.size).toBe("18px");
    expect(brand!.logo!.weight).toBe("700");
    // 40×40 rounded-xl (12px) forest gradient tile.
    expect(brand!.tile!.w).toBe(40);
    expect(brand!.tile!.h).toBe(40);
    expect(brand!.tile!.radius).toBe("12px");
    expect(brand!.tile!.grad).toContain("linear-gradient(135deg, rgb(26, 58, 46), rgb(45, 90, 74))");
    // The reference's ul wrapper.
    expect(brand!.ulWrapperCls).toContain("w-full");
    expect(brand!.ulWrapperCls).toContain("text-sm");
  });

  // Session-15 audit (docs/remediation-plan-v8.md G2a): the reference renders
  // INACTIVE nav links at zinc-600-family rgb(63,63,70) as plain rgb; the
  // clone's text-zinc-700 computes the same VALUE through lab() (v4 named
  // palette). Pin the computed style to plain rgb — the hex class keeps the
  // engine out of Lab space (and renders on browsers without lab() support).
  test("inactive nav link color computes as plain rgb(63,63,70), not lab (v8 G2a)", async ({
    page,
  }) => {
    const color = await page.evaluate(() => {
      const link = [...document.querySelectorAll("nav a")].find(
        (a) => (a.textContent || "").trim() === "Income",
      );
      return link ? getComputedStyle(link).color : null;
    });
    expect(color).not.toBeNull();
    expect(color).toBe("rgb(63, 63, 70)");
  });
});

// ---------------------------------------------------------------------------
// v12 — per-route document titles (docs/remediation-plan-v12.md G2).
//
// Measured live on the reference: its SPA sets the tab title client-side
// after navigation — "/income" → "Income | ZeroBudget", "/expenses" →
// "Expenses | ZeroBudget", "/savings" → "Savings | ZeroBudget",
// "/networth" → "Networth | ZeroBudget" (the reference's own ONE-WORD
// spelling), while "/", "/dashboard" and "/login" stay "ZeroBudget". The
// clone's static prerender ships "ZeroBudget" everywhere; the AppShell
// now mirrors the reference's client-side behavior with a route→title
// map. (The v7 404 pin — "Page Name | ZeroBudget" — is separate.)
// ---------------------------------------------------------------------------

test.describe("per-route document titles (v12 — plan G2)", () => {
  test("workspace routes set the reference titles; root and dashboard stay plain", async ({ page }) => {
    const cases: Array<[string, string]> = [
      ["/income", "Income | ZeroBudget"],
      ["/expenses", "Expenses | ZeroBudget"],
      ["/savings", "Savings | ZeroBudget"],
      ["/networth", "Networth | ZeroBudget"],
      ["/dashboard", "ZeroBudget"],
      ["/", "ZeroBudget"],
    ];
    for (const [route, title] of cases) {
      await page.goto(route);
      // The title lands client-side after hydration (exactly like the
      // reference's SPA) — toHaveTitle retries until the effect runs.
      await expect(page).toHaveTitle(title);
    }
  });

  test("the login route keeps the static ZeroBudget title", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    await expect(page).toHaveTitle("ZeroBudget");
  });
});

// ---------------------------------------------------------------------------
// v103 — plan F4 (docs/remediation-plan-v103.md): the rail's bottom
// USER-FOOTER tile census at 1280 — the never-census'd family. The v79 F4
// pin (items.spec) covers the AVATAR's own chrome (the round 1-2 char
// element INSIDE the tile); the mobile sheet asserts only the TEXTS'
// visibility; the tile's own box + the name/subtitle typography + the
// border-t wrapper are pinned NOWHERE else at ANY viewport. Measured
// byte-identical on BOTH sides via userfooter-arbit-v103.sh (the one-shot
// both-sides DOM census): the tile 223×60 / radius 8px / pad 12px / bg
// rgb(245,248,245) / flex center gap 12px; the wrapper border-t 1px
// rgb(229,231,227) / pad 16px / gap 8px; the name "Budget Pro" 14px/500/
// rgb(26,58,46) ellipsis; the subtitle "Track your finances" 12px/400/
// rgb(45,90,74) ellipsis. The h 60 = pad 12×2 + avatar 36. Pin-sanity:
// sidebar.tsx:116 rounded-lg → rounded-xl fails tile.radius ALONE
// (cascade-free BY CONSTRUCTION — border-radius never changes the layout
// box; the nav links' own rounded-lg at line 79 + the burger's at line 227
// untouched by the line-number scoping).
// ---------------------------------------------------------------------------

test.describe("rail user-footer tile census at 1280 (v103 — plan F4)", () => {
  test("the border-t wrapper + the tinted tile + the name/subtitle chrome (v103 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/income");
    await expect(page.getByText("2 items · $5550.00")).toBeVisible();

    const census = await page.evaluate(() => {
      const rail = document.querySelector("aside");
      if (!rail) return null;
      // the avatar — the v79 finder (the round 1-2 char element in the rail)
      const avatar = [...rail.querySelectorAll("div,span,button")].find((el) => {
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
      });
      if (!avatar) return null;
      // the TILE — the avatar's nearest ancestor with a visible bg + radius
      let tile: HTMLElement | null = avatar.parentElement;
      for (let i = 0; i < 4 && tile; i++) {
        const cs = getComputedStyle(tile);
        if (cs.backgroundColor !== "rgba(0, 0, 0, 0)" && parseFloat(cs.borderRadius) > 0) break;
        tile = tile.parentElement;
      }
      if (!tile) return null;
      const tcs = getComputedStyle(tile);
      const tr = tile.getBoundingClientRect();
      // the WRAPPER — the tile's parent (the border-t p-4 block)
      const wrap = tile.parentElement;
      if (!wrap) return null;
      const wcs = getComputedStyle(wrap);
      // the text leaves — the tile's childless text elements (>2 chars)
      const texts = [...tile.querySelectorAll("p,span,div")].filter((el) => {
        const t = (el.textContent || "").trim();
        return t.length > 2 && el.children.length === 0;
      });
      const leaf = (el: Element) => {
        const cs = getComputedStyle(el);
        return {
          text: (el.textContent || "").trim().slice(0, 24),
          fs: cs.fontSize,
          fw: cs.fontWeight,
          color: cs.color,
          truncate: cs.textOverflow,
        };
      };
      return {
        tile: {
          w: Math.round(tr.width),
          h: Math.round(tr.height),
          radius: tcs.borderRadius,
          pad: tcs.padding,
          bg: tcs.backgroundColor,
          display: tcs.display,
          align: tcs.alignItems,
          gap: tcs.gap,
        },
        wrapper: {
          borderTop: `${wcs.borderTopWidth} ${wcs.borderTopColor}`,
          pad: wcs.padding,
          gap: wcs.gap,
          display: wcs.display,
        },
        avatarW: Math.round(avatar.getBoundingClientRect().width),
        name: texts[0] ? leaf(texts[0]) : null,
        sub: texts[1] ? leaf(texts[1]) : null,
      };
    });
    expect(census).not.toBeNull();
    // The tinted tile: the reference's own 245,248,245 rounded-lg p-3 card.
    expect(census!.tile).toEqual({
      w: 223,
      h: 60,
      radius: "8px",
      pad: "12px",
      bg: "rgb(245, 248, 245)",
      display: "flex",
      align: "center",
      gap: "12px",
    });
    // The wrapper: the border-t p-4 block at the rail's bottom.
    expect(census!.wrapper).toEqual({
      borderTop: "1px rgb(229, 231, 227)",
      pad: "16px",
      gap: "8px",
      display: "flex",
    });
    // The avatar's geometry control (the v79 F4 pin's own element — re-walked).
    expect(census!.avatarW).toBe(36);
    // The name + subtitle: the static copy pair, truncate chrome live.
    expect(census!.name).toEqual({
      text: "Budget Pro",
      fs: "14px",
      fw: "500",
      color: "rgb(26, 58, 46)",
      truncate: "ellipsis",
    });
    expect(census!.sub).toEqual({
      text: "Track your finances",
      fs: "12px",
      fw: "400",
      color: "rgb(45, 90, 74)",
      truncate: "ellipsis",
    });
  });
});
