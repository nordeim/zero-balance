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
});
