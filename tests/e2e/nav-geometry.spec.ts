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

// v104 — plan F4: the rail's TOP brand-block family, never census'd as a
// whole. The v7 G4 pin holds the tile/icon/h2 size+weight ONLY; the h2's
// color + line-height, the subtitle P's computed chrome ("Budget Planner" —
// only the mobile sheet's VISIBILITY check anywhere), and the brand ROW's
// flex chrome were never pinned at ANY viewport in ANY spec. Measured
// byte-identical on BOTH sides via the one-shot census brand-arbit-v104.sh
// (the base44-fab/userfooter pattern; the reference's rail is a DIV — the
// census's fallback-chain finder, a live discovery this cycle).
test.describe("rail brand-block subtitle + row census at 1280 (v104 — plan F4)", () => {
  test("the brand row chrome + the h2 color/lh + the Budget Planner subtitle (v104 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();

    const census = await page.evaluate(() => {
      const rail = document.querySelector("aside");
      if (!rail) return null;
      const h2 = [...rail.querySelectorAll("h2")].find(
        (h) => (h.textContent || "").trim() === "ZeroBalance",
      );
      if (!h2) return null;
      // the TEXT COLUMN: the h2's parent (the tile's next sibling)
      const col = h2.parentElement;
      // the TILE: the column's previous sibling (the v7 G4 finder)
      const tile = col?.previousElementSibling ?? null;
      // the ROW: the column's parent (the flex row: tile + column)
      const row = col?.parentElement ?? null;
      // the SUBTITLE: the column's only P
      const sub = col?.querySelector("p") ?? null;
      const h2cs = getComputedStyle(h2);
      const scs = sub ? getComputedStyle(sub) : null;
      const rcs = row ? getComputedStyle(row) : null;
      const icon = tile?.querySelector("svg") ?? null;
      return {
        h2: {
          fs: h2cs.fontSize,
          fw: h2cs.fontWeight,
          lh: h2cs.lineHeight,
          color: h2cs.color,
        },
        subtitle: sub
          ? {
              text: (sub.textContent || "").trim().slice(0, 24),
              fs: scs!.fontSize,
              fw: scs!.fontWeight,
              color: scs!.color,
            }
          : null,
        row: row
          ? {
              display: rcs!.display,
              align: rcs!.alignItems,
              gap: rcs!.gap,
            }
          : null,
        col: col ? { display: getComputedStyle(col).display } : null,
        tile: tile
          ? {
              w: Math.round(tile.getBoundingClientRect().width),
              h: Math.round(tile.getBoundingClientRect().height),
              radius: getComputedStyle(tile).borderRadius,
            }
          : null,
        icon: icon
          ? {
              w: getComputedStyle(icon).width,
              h: getComputedStyle(icon).height,
            }
          : null,
      };
    });
    expect(census).not.toBeNull();
    // The brand ROW: the reference's own flex row (tile + text column).
    expect(census!.row).toEqual({
      display: "flex",
      align: "center",
      gap: "12px",
    });
    // The H2: the v7 G4 axes (fs/fw) strengthened with the never-pinned
    // color + line-height.
    expect(census!.h2).toEqual({
      fs: "18px",
      fw: "700",
      lh: "28px",
      color: "rgb(26, 58, 46)",
    });
    // The SUBTITLE: the never-pinned static copy pair.
    expect(census!.subtitle).toEqual({
      text: "Budget Planner",
      fs: "12px",
      fw: "400",
      color: "rgb(45, 90, 74)",
    });
    // The context controls: the v7 G4 geometry re-walked (the tile +
    // the icon + the column's block display).
    expect(census!.col).toEqual({ display: "block" });
    expect(census!.tile).toEqual({ w: 40, h: 40, radius: "12px" });
    expect(census!.icon).toEqual({ w: "24px", h: "24px" });
  });
});

// v110 — plan F4 (docs/remediation-plan-v110.md): the rail's NAV-BLOCK
// INTERIOR census at 1280 — the block BETWEEN the v104-pinned brand-block
// (above) and the v103-pinned user-footer (below); the family the v110
// savings-pair evidence walked past on every full-page shot. The
// session-5 pins hold the link BOX on links[0] only; the v8 G2a pin the
// inactive color; the v36 S3 bands the y positions. NEVER pinned at ANY
// viewport in ANY spec: the "Navigation" label's computed chrome, the
// UL's flex family, the LI's box, the nav ICON's computed w/h (the
// glyph-parity spec holds the icons' PATH data only), the label SPAN's
// truncate family, and the desktop ACTIVE link's computed chrome (the
// v10 pin holds the mobile SHEET variant; the v7-era desktop test is
// class-string only). Measured byte-identical on BOTH sides via
// nav-arbit-v110.sh at 1280x800 on /savings (the cycle's pair surface —
// the Savings row is the active link). The finders are STRUCTURAL: the
// reference renders NO nav landmark (its documented no-landmark bug), so
// the ul is found by its 5-anchor shape, the label by the wrapper-sibling
// walk (childless + short text; the childless-uppercase-div fallback),
// and the active link by aria-current OR the gradient background OR the
// text — never by tag alone.
test.describe("rail nav-block interior census at 1280 (v110 — plan F4)", () => {
  test("the Navigation label + the ul/li interiors + the icon + the truncate span + the active link chrome (v110 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();

    const census = await page.evaluate(() => {
      // the rail: the v103 fallback chain (the clone renders an aside;
      // the reference's rail is a DIV)
      const rail = document.querySelector("aside") || [...document.querySelectorAll("nav,aside,div")].find(d => {
        const r = d.getBoundingClientRect();
        return r.width > 180 && r.width < 320 && r.height > 700 && r.left === 0;
      });
      if (!rail) return null;
      // the ul: STRUCTURAL (the reference has no <nav> landmark)
      const ul = [...rail.querySelectorAll("ul")].find(u => {
        const r = u.getBoundingClientRect();
        return u.querySelectorAll("a").length >= 4 && r.width > 100 && r.height > 100;
      });
      if (!ul) return null;
      // the section label: the ul wrapper's previous element sibling,
      // validated childless + short text (the childless-uppercase fallback)
      const wrap = ul.parentElement;
      let label = wrap ? wrap.previousElementSibling : null;
      if (!label || label.children.length > 0 || (label.textContent || "").trim().length === 0 || (label.textContent || "").trim().length > 20) {
        label = [...rail.querySelectorAll("div")].find(d => {
          const cs2 = getComputedStyle(d);
          const r2 = d.getBoundingClientRect();
          return cs2.textTransform === "uppercase" && !d.children.length && (d.textContent || "").trim().length > 0 && (d.textContent || "").trim().length <= 20 && r2.height > 0 && r2.height <= 40;
        }) || null;
      }
      const li = ul.firstElementChild as HTMLElement | null;
      const link = li ? li.querySelector("a") : null;
      const span = link ? link.querySelector("span") : null;
      const icon = link ? link.querySelector("svg") : null;
      // the active link: aria-current OR the gradient bg OR the Savings text
      const activeLink = [...ul.querySelectorAll("a")].find(a => a.getAttribute("aria-current") === "page")
        || [...ul.querySelectorAll("a")].find(a => {
          const g = getComputedStyle(a).backgroundImage;
          return g && g !== "none" && g.includes("gradient");
        })
        || [...ul.querySelectorAll("a")].find(a => (a.textContent || "").trim() === "Savings");
      const lcs = label ? getComputedStyle(label) : null;
      const ucs = getComputedStyle(ul);
      const lic = li ? getComputedStyle(li) : null;
      const kcs = link ? getComputedStyle(link) : null;
      const scs = span ? getComputedStyle(span) : null;
      const ir = icon ? icon.getBoundingClientRect() : null;
      const acs = activeLink ? getComputedStyle(activeLink) : null;
      return {
        docSW: document.documentElement.scrollWidth,
        label: label && lcs ? {
          text: (label.textContent || "").trim().slice(0, 16),
          h: Math.round(label.getBoundingClientRect().height),
          fs: lcs.fontSize, fw: lcs.fontWeight,
          transform: lcs.textTransform, spacing: lcs.letterSpacing,
          color: lcs.color, pad: lcs.padding, radius: lcs.borderRadius,
          display: lcs.display, align: lcs.alignItems,
        } : null,
        ul: {
          display: ucs.display, dir: ucs.flexDirection, gap: ucs.rowGap,
          w: Math.round(ul.getBoundingClientRect().width), childCount: ul.children.length,
        },
        li: li && lic ? {
          position: lic.position, mb: lic.marginBottom,
          h: Math.round(li.getBoundingClientRect().height),
        } : null,
        linkBox: link && kcs ? {
          h: Math.round(link.getBoundingClientRect().height),
          pad: kcs.padding, columnGap: kcs.columnGap,
          fs: kcs.fontSize, fw: kcs.fontWeight, radius: kcs.borderRadius,
          display: kcs.display, align: kcs.alignItems,
        } : null,
        icon: ir ? { w: Math.round(ir.width), h: Math.round(ir.height) } : null,
        span: span && scs ? {
          fs: scs.fontSize, overflow: scs.overflow,
          textOverflow: scs.textOverflow, whiteSpace: scs.whiteSpace,
        } : null,
        active: activeLink && acs ? {
          text: (activeLink.textContent || "").trim().slice(0, 12),
          bg: acs.backgroundImage, color: acs.color, fw: acs.fontWeight,
          h: Math.round(activeLink.getBoundingClientRect().height),
        } : null,
        linkCount: ul.querySelectorAll("a").length,
        iconCount: ul.querySelectorAll("a svg").length,
      };
    });
    expect(census).not.toBeNull();
    expect(census!.docSW).toBe(1280);

    // The "Navigation" section label — the never-pinned chrome (the
    // shadcn group-label row: uppercase, tracking-wider, forest-medium).
    expect(census!.label).toEqual({
      text: "Navigation",
      h: 32,
      fs: "12px",
      fw: "600",
      transform: "uppercase",
      spacing: "0.6px",
      color: "rgb(45, 90, 74)",
      pad: "8px 12px",
      radius: "6px",
      display: "flex",
      align: "center",
    });

    // The UL + the LI — the stack family (flex column, the 4px row gap,
    // the 36px li box).
    expect(census!.ul).toEqual({
      display: "flex",
      dir: "column",
      gap: "4px",
      w: 215,
      childCount: 5,
    });
    expect(census!.li).toEqual({ position: "relative", mb: "0px", h: 36 });

    // The link box — the session-5 controls re-walked as context.
    expect(census!.linkBox).toEqual({
      h: 32,
      pad: "10px 12px",
      columnGap: "12px",
      fs: "14px",
      fw: "400",
      radius: "8px",
      display: "flex",
      align: "center",
    });

    // The nav ICON's computed w/h — THE never-pinned axis.
    expect(census!.icon).toEqual({ w: 16, h: 16 });

    // The label SPAN's truncate family.
    expect(census!.span).toEqual({
      fs: "14px",
      overflow: "hidden",
      textOverflow: "ellipsis",
      whiteSpace: "nowrap",
    });

    // The ACTIVE link's computed chrome (the Savings row on /savings):
    // the 135deg forest-medium→lime gradient, white text, fw 500.
    expect(census!.active).toEqual({
      text: "Savings",
      bg: "linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))",
      color: "rgb(255, 255, 255)",
      fw: "500",
      h: 32,
    });

    // The counts: five links, five icons.
    expect(census!.linkCount).toBe(5);
    expect(census!.iconCount).toBe(5);
  });
});
