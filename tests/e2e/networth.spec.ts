import { expect, test } from "@playwright/test";

// Net Worth: the forest→lime gradient summary (Total Net Worth, Total
// Assets, Total Liabilities, Asset-to-Liability Ratio "0.21:1" — the
// reference's .toFixed(2) + ":1" with NO spaces, "∞:1" when debt-free), the
// Assets/Liabilities tabs with TYPE-GROUPED lists (capitalize h3 headers),
// dot + name + gray-type-badge cards with GROUPED comma money, stacked
// footers (institution / % interest / Updated), and the add-asset
// round-trip. Seed arithmetic: assets 65,300 − liabilities 311,250 → net
// worth −245,950; ratio 65,300 / 311,250 → 0.21.
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("net worth view", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
  });

  test("summary card shows the gradient, net figure and 2-decimal ratio", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Net Worth" })).toBeVisible();
    await expect(page.getByText("Track your assets and liabilities")).toBeVisible();

    // Networth keeps the GROUPED money format (commas).
    await expect(page.getByText("-$245,950.00")).toBeVisible();
    await expect(page.getByText("Total Assets")).toBeVisible();
    await expect(page.getByText("$65,300.00")).toBeVisible();
    await expect(page.getByText("Total Liabilities")).toBeVisible();
    await expect(page.getByText("$311,250.00")).toBeVisible();

    // Ratio: ".toFixed(2)" + ":1", no spaces (reference bundle).
    await expect(page.getByText("Asset to Liability Ratio")).toBeVisible();
    await expect(page.getByText("0.21:1")).toBeVisible();

    // The summary's forest→lime gradient (135deg).
    const hero = page.locator("div.rounded-2xl").filter({ hasText: "Total Net Worth" }).first();
    const bg = await hero.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(45, 90, 74)");
  });

  test("header renders the reference's gradient icon chip (v14 — plan G3)", async ({ page }) => {
    // Measured live on the reference at BOTH viewports: the /networth header
    // is a flex items-center gap-3 row — a 48×48 chip (radius 12,
    // linear-gradient(135deg, #2d5a4a, #8fbc3f)) wrapping a 24×24 white
    // lucide-trending-up, then the h1+p block. The reference renders NO chip
    // on the dashboard (pinned there — see dashboard.spec.ts); the clone's
    // net-worth header was bare.
    const h1 = page.getByRole("heading", { name: "Net Worth", level: 1 });
    await expect(h1).toBeVisible();

    // Find the 48×48 chip precisely via geometry (the h1's preceding sibling
    // in the flex row).
    const geo = await page.evaluate(() => {
      const h1El = [...document.querySelectorAll("main h1")].find((h) =>
        (h.textContent || "").trim() === "Net Worth",
      );
      if (!h1El) return null;
      const row = h1El.parentElement!.parentElement!;
      const rowCs = getComputedStyle(row);
      const chipEl = [...row.children].find((c) => c.tagName === "DIV" && c !== h1El.parentElement);
      if (!chipEl) return null;
      const cr = chipEl.getBoundingClientRect();
      const chipCs = getComputedStyle(chipEl);
      const svg = chipEl.querySelector("svg");
      const sr = svg ? svg.getBoundingClientRect() : null;
      const hr = h1El.getBoundingClientRect();
      return {
        rowClass: row.className,
        rowDisplay: rowCs.display,
        rowAlign: rowCs.alignItems,
        rowGap: rowCs.gap,
        chipW: cr.width,
        chipH: cr.height,
        chipRadius: chipCs.borderRadius,
        chipBg: chipCs.backgroundImage,
        chipFlex: chipCs.display + "/" + chipCs.alignItems + "/" + chipCs.justifyContent,
        svgClass: svg ? svg.getAttribute("class") : null,
        svgW: sr ? sr.width : null,
        svgH: sr ? sr.height : null,
        svgStroke: svg ? getComputedStyle(svg).stroke : null,
        h1X: hr.x,
        chipRight: cr.right,
        h1BelowChipTop: hr.y >= cr.top - 2,
      };
    });
    expect(geo).not.toBeNull();
    if (!geo) {
      throw new Error("networth header chip not found");
    }
    expect(geo.rowClass).toContain("flex");
    expect(geo.rowClass).toContain("items-center");
    expect(geo.rowClass).toContain("gap-3");
    expect(geo.chipW).toBe(48);
    expect(geo.chipH).toBe(48);
    expect(geo.chipRadius).toBe("12px");
    expect(geo.chipBg).toContain("linear-gradient(135deg, rgb(45, 90, 74)");
    expect(geo.chipBg).toContain("rgb(143, 188, 63)");
    expect(geo.svgClass).toContain("lucide-trending-up");
    expect(geo.svgW).toBe(24);
    expect(geo.svgH).toBe(24);
    expect(geo.svgStroke).toBe("rgb(255, 255, 255)");
    // The h1 sits 12px (gap-3) right of the chip.
    expect(geo.h1X - geo.chipRight).toBe(12);
  });

  test("tabs render the reference's 16px icons with currentColor (v14 — plan G2)", async ({ page }) => {
    // Measured live on the reference: each trigger carries a 16×16 lucide
    // icon (circle-arrow-up / circle-arrow-down) with mr-2 (8px) and
    // stroke=currentColor — the icons inherit the tab's text color: active
    // green-900, inactive rgb(115,115,115). The clone was text-only.
    const assetsTab = page.getByRole("tab", { name: "Assets" });
    const liabilitiesTab = page.getByRole("tab", { name: "Liabilities" });

    const upIcon = assetsTab.locator("svg.lucide-circle-arrow-up");
    const downIcon = liabilitiesTab.locator("svg.lucide-circle-arrow-down");
    await expect(upIcon).toBeVisible();
    await expect(downIcon).toBeVisible();

    const iconGeo = await page.evaluate(() => {
      const tabs = [...document.querySelectorAll('[role="tab"]')].filter((t) =>
        /^(Assets|Liabilities)$/.test((t.textContent || "").trim()),
      );
      return tabs.map((t) => {
        const svg = t.querySelector("svg");
        if (!svg) return { text: t.textContent?.trim(), icon: false };
        const r = svg.getBoundingClientRect();
        const cs = getComputedStyle(svg);
        return {
          text: t.textContent?.trim(),
          icon: true,
          w: r.width,
          h: r.height,
          marginRight: cs.marginRight,
          stroke: cs.stroke,
          strokeWidth: cs.strokeWidth,
          color: cs.color,
        };
      });
    });
    expect(iconGeo).toHaveLength(2);
    for (const icon of iconGeo) {
      expect(icon.icon).toBe(true);
      expect(icon.w).toBe(16);
      expect(icon.h).toBe(16);
      expect(icon.marginRight).toBe("8px");
      expect(icon.strokeWidth).toBe("2px");
    }
    // The icons inherit the tab's text color (currentColor): the ACTIVE
    // Assets tab renders green-900, the INACTIVE Liabilities gray — the
    // reference's measured pair.
    expect(iconGeo.find((i) => i.text === "Assets")!.stroke).toBe("rgb(20, 83, 45)");
    expect(iconGeo.find((i) => i.text === "Liabilities")!.stroke).toBe("rgb(115, 115, 115)");

    // After activation the icon color follows the active tab text (green-900)
    // and the deactivated one returns to gray. transition-all animates the
    // swap — settle before reading computed styles (the documented 300ms
    // transition-settle pattern).
    await liabilitiesTab.click();
    await expect(liabilitiesTab).toHaveAttribute("data-state", "active");
    await page.waitForTimeout(400);
    const activeColor = await liabilitiesTab.locator("svg").evaluate((el) => getComputedStyle(el).color);
    expect(activeColor).toBe("rgb(20, 83, 45)");
    const inactiveColor = await assetsTab.locator("svg").evaluate((el) => getComputedStyle(el).color);
    expect(inactiveColor).toBe("rgb(115, 115, 115)");
  });

  test("Assets tab groups by type with capitalize headers and badge cards", async ({ page }) => {
    await expect(page.getByRole("tab", { name: "Assets" })).toBeVisible();
    // Section header: text-2xl + always-plural count, short grouped money.
    const assetsHeader = page.getByRole("heading", { name: "Assets", level: 2 });
    await expect(assetsHeader).toBeVisible();
    await expect(page.getByText("3 items · $65,300")).toBeVisible();

    // Type-group headers (capitalize class over raw keys). The API lists
    // entities createdAt-desc (mirroring the reference's "-created_date"),
    // so first-occurrence groups run newest-type-first: investment →
    // superannuation → bank_account.
    const groups = page.locator("h3.capitalize");
    await expect(groups).toHaveCount(3);
    await expect(groups.nth(0)).toHaveText(/investment/i);
    await expect(groups.nth(1)).toHaveText(/superannuation/i);
    await expect(groups.nth(2)).toHaveText(/bank account/i);
    // Asset group headers render in forestMedium.
    await expect(groups.nth(0)).toHaveCSS("color", "rgb(45, 90, 74)");

    // Card: name + gray type badge + grouped amount + stacked footer.
    await expect(page.getByText("Everyday Account").first()).toBeVisible();
    const badge = page.getByText("Bank Account", { exact: true }).first();
    // v29 G1: the reference's card type label is a Badge-base DIV — rest
    // bg rgb(243,244,246) (gray-100 v3) / text rgb(55,65,81) (gray-700
    // v3) + the REAL-hover tint rgba(245,245,245,0.8). The TW4 palette
    // utilities computed oklab — pinned via hex + the zb-badge-hover
    // class (the v28 G1 pin) like the item-card badges before them.
    await expect(badge).toHaveClass(/bg-\[#f3f4f6\]/);
    await expect(badge).toHaveClass(/text-\[#374151\]/);
    await expect(badge).toHaveClass(/transition-colors/);
    await expect(badge).toHaveClass(/zb-badge-hover/);
    await expect(badge).toHaveCSS("background-color", "rgb(243, 244, 246)");
    await expect(badge).toHaveCSS("color", "rgb(55, 65, 81)");
    await expect(page.getByText("$4,200.00").first()).toBeVisible();
    await expect(page.getByText("Commonwealth Bank").first()).toBeVisible();
    await expect(page.getByText("$48,500.00").first()).toBeVisible();
    await expect(page.getByText("$12,600.00").first()).toBeVisible();
    // "Updated" footer per card.
    await expect(page.getByText(/Updated/).first()).toBeVisible();

    // Add Asset carries the forest→lime gradient.
    const add = page.getByRole("button", { name: "Add Asset" }).first();
    const addBg = await add.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(addBg).toContain("linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))");
  });

  test("Liabilities tab lists type-grouped cards with interest lines", async ({ page }) => {
    await page.getByRole("tab", { name: "Liabilities" }).click();
    await expect(page.getByText("2 items · $311,250")).toBeVisible();
    // Liability group headers render in orange; newest first → credit card
    // precedes home loan (createdAt-desc listing).
    const groups = page.locator("h3.capitalize");
    await expect(groups).toHaveCount(2);
    await expect(groups.nth(0)).toHaveText(/credit card/i);
    await expect(groups.nth(1)).toHaveText(/home loan/i);
    await expect(groups.first()).toHaveCSS("color", "rgb(224, 122, 59)");

    await expect(page.getByText("$310,000.00").first()).toBeVisible();
    await expect(page.getByText("$1,250.00").first()).toBeVisible();
    // v29 G1 (family consistency): the liability card's type label carries
    // the same pinned family (the reference's own liability data is empty —
    // its shared Badge component implies the identical base). Scoped to the
    // label span: the seeded home loan's NAME is also "Home Loan" (h4).
    const liabBadge = page.locator("span.zb-badge-hover").filter({ hasText: "Home Loan" }).first();
    await expect(liabBadge).toHaveClass(/bg-\[#f3f4f6\]/);
    await expect(liabBadge).toHaveClass(/text-\[#374151\]/);
    await expect(liabBadge).toHaveClass(/zb-badge-hover/);
    await expect(liabBadge).toHaveCSS("background-color", "rgb(243, 244, 246)");
    await expect(liabBadge).toHaveCSS("color", "rgb(55, 65, 81)");
    // The liability-only "{rate}% interest" footer line.
    await expect(page.getByText("5.75% interest")).toBeVisible();
    await expect(page.getByText("19.99% interest")).toBeVisible();

    // Add Liability carries the orange gradient.
    const add = page.getByRole("button", { name: "Add Liability" }).first();
    const addBg = await add.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(addBg).toContain("linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))");
  });

  test("summary card structure: 2-col grid + ratio in the border-t footer row", async ({ page }) => {
    // Reference (session-7 audit, remediation-plan-v4 G4): exactly TWO stat
    // cards (Assets, Liabilities) in a 2-col grid with text-xs/70 labels and
    // text-2xl amounts + backdrop blur; the ratio lives in a separate
    // mt-6 pt-6 border-t border-white/20 footer row with a text-sm/80 label
    // and a text-lg bold value.
    const card = await page.evaluate(() => {
      const sum = [...document.querySelectorAll("div")].find((d) =>
        (d.className || "").toString().includes("rounded-2xl") &&
        /Total Net Worth/.test(d.textContent || ""),
      );
      if (!sum) return null;
      const grid = [...sum.querySelectorAll("div")].find(
        (d) => /grid-cols-2/.test((d.className || "").toString()) && /Total Assets/.test(d.textContent || ""),
      );
      if (!grid) return { gridFound: false };
      const cards = [...grid.children].map((c) => ({
        label: (c.querySelector("p") as HTMLElement | null)?.textContent?.trim() ?? "",
        labelSize: c.querySelector("p") ? getComputedStyle(c.querySelector("p")!).fontSize : "",
        amountSize: c.lastElementChild ? getComputedStyle(c.lastElementChild).fontSize : "",
        backdropFilter: getComputedStyle(c).backdropFilter,
      }));
      // The footer row: under the grid with the ratio spans. The border is
      // an INLINE rgba style (Tailwind v4 would emit border-white/20 as
      // oklab(...) — the oklch-drift trap), so assert the computed border.
      const footer = [...sum.querySelectorAll("div")].find(
        (d) => (d.className || "").toString().includes("mt-6") && /Asset to Liability Ratio/.test(d.textContent || ""),
      );
      const ratioEl = footer?.querySelector("span:last-child");
      return {
        gridFound: true,
        gridCls: (grid.className || "").toString(),
        cards,
        footerFound: !!footer,
        footerCls: footer ? (footer.className || "").toString() : "",
        footerBorderWidth: footer ? getComputedStyle(footer).borderTopWidth : "",
        footerBorderStyle: footer ? getComputedStyle(footer).borderTopStyle : "",
        footerBorderColor: footer ? getComputedStyle(footer).borderTopColor : "",
        ratioSize: ratioEl ? getComputedStyle(ratioEl).fontSize : "",
        ratioWeight: ratioEl ? getComputedStyle(ratioEl).fontWeight : "",
      };
    });
    expect(card).not.toBeNull();
    expect(card!.gridFound).toBe(true);
    // Exactly two cards at ≥sm: Assets + Liabilities (NOT the ratio).
    const cards = card!.cards ?? [];
    expect(cards).toHaveLength(2);
    const [assetCard, liabilityCard] = cards;
    expect(assetCard?.label).toBe("Total Assets");
    expect(liabilityCard?.label).toBe("Total Liabilities");
    // Reference typography: 12px labels, 24px amounts.
    expect(assetCard?.labelSize).toBe("12px");
    expect(assetCard?.amountSize).toBe("24px");
    expect(assetCard?.backdropFilter).toContain("blur(10px)");
    // The ratio sits in the footer row (1px solid rgba white/20), 18px bold.
    expect(card!.footerFound).toBe(true);
    expect(card!.footerCls).toContain("mt-6");
    expect(card!.footerBorderWidth).toBe("1px");
    expect(card!.footerBorderStyle).toBe("solid");
    expect(card!.footerBorderColor).toBe("rgba(255, 255, 255, 0.2)");
    expect(card!.ratioSize).toBe("18px");
    expect(card!.ratioWeight).toBe("700");
    await expect(page.getByText("0.21:1")).toBeVisible();
  });

  test("mobile net-worth page has no horizontal overflow (superset fix)", async ({ page }) => {
    // The REFERENCE overflows to 464px at 390 (text-5xl H2 + fixed 2-col
    // grid); the clone must fit the viewport exactly (remediation-plan-v4
    // G5 + R4). The responsive H2 is text-3xl at mobile / text-5xl ≥sm.
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
    const dims = await page.evaluate(() => ({
      scrollWidth: document.documentElement.scrollWidth,
      clientWidth: document.documentElement.clientWidth,
      h2Size: (() => {
        const sum = [...document.querySelectorAll("div")].find((d) =>
          (d.className || "").toString().includes("rounded-2xl") && /Total Net Worth/.test(d.textContent || ""),
        );
        const h2 = sum?.querySelector("h2");
        return h2 ? getComputedStyle(h2).fontSize : "";
      })(),
      gridCls: (() => {
        const sum = [...document.querySelectorAll("div")].find((d) =>
          (d.className || "").toString().includes("rounded-2xl") && /Total Net Worth/.test(d.textContent || ""),
        );
        const grid = [...(sum?.querySelectorAll("div") ?? [])].find(
          (d) => /Total Assets/.test(d.textContent || "") && /grid-cols/.test((d.className || "").toString()),
        );
        return grid ? (grid.className || "").toString() : "";
      })(),
    }));
    expect(dims.scrollWidth).toBeLessThanOrEqual(dims.clientWidth + 1);
    // 24px H2 on phones (text-2xl — fits beside the 64px icon), 48px from
    // sm up (reference parity).
    expect(dims.h2Size).toBe("24px");
    expect(dims.gridCls).toContain("grid-cols-1");
    expect(dims.gridCls).toContain("sm:grid-cols-2");
  });

  test("add → delete asset round-trip through the dialog", async ({ page }) => {
    await page.getByRole("button", { name: "Add Asset" }).first().click();
    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();

    await dialog.getByRole("combobox", { name: "Asset Type" }).click();
    await page.getByRole("option", { name: "Vehicle" }).click();
    await page.getByLabel("Current Value").fill("15000");
    await page.getByLabel("Name").fill("Test Car");
    await page.getByLabel("Institution").fill("Playwright Motors");
    await page.getByRole("button", { name: "Save Asset" }).click();
    await expect(dialog).toBeHidden();

    const created = page.locator("div.rounded-xl").filter({ hasText: "Test Car" }).first();
    await expect(created).toBeVisible();
    await expect(created.getByText("$15,000.00")).toBeVisible();

    // The tab header count updated: 4 items · $80,300 (short format).
    await expect(page.getByText("4 items · $80,300")).toBeVisible();

    // Delete (inline confirm via the ellipsis actions menu).
    await created.getByRole("button", { name: "Actions for Test Car" }).click();
    await page.getByRole("menuitem", { name: "Delete" }).click();
    await expect(page.getByText("Delete this asset?")).toBeVisible();
    await page.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(page.getByText("Test Car")).toHaveCount(0);
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
  });
});

test.describe("net worth tabs (v5 — remediation-plan-v5.md G3)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/networth");
    await expect(page.getByRole("heading", { name: "Net Worth" })).toBeVisible();
  });

  test("tab list is the reference's 2-col grid with the green active state", async ({ page }) => {
    const tabs = await page.evaluate(() => {
      const active = [...document.querySelectorAll('button[role="tab"]')].find(
        (x) => x.getAttribute("aria-selected") === "true",
      );
      const inactive = [...document.querySelectorAll('button[role="tab"]')].find(
        (x) => x.getAttribute("aria-selected") === "false",
      );
      const list = document.querySelector('[role="tablist"]') as HTMLElement | null;
      if (!active || !inactive || !list) return null;
      const a = getComputedStyle(active);
      const i = getComputedStyle(inactive.querySelector("span") || inactive);
      const lr = list.getBoundingClientRect();
      const ar = active.getBoundingClientRect();
      return {
        listW: Math.round(lr.width),
        listBg: getComputedStyle(list).backgroundColor,
        triggerW: Math.round(ar.width),
        triggerH: Math.round(ar.height),
        activeBg: a.backgroundColor,
        activeColor: getComputedStyle(active.querySelector("span") || active).color,
        inactiveColor: i.color,
        activeCls: active.className,
      };
    });
    expect(tabs).not.toBeNull();
    // Reference list: grid w-full max-w-md grid-cols-2 → 448px wide,
    // triggers ~220px, muted bg #f5f5f5.
    expect(tabs!.listW).toBe(448);
    expect(tabs!.listBg).toBe("rgb(245, 245, 245)");
    expect(tabs!.triggerW).toBe(220);
    expect(tabs!.triggerH).toBe(28);
    // Active: green-100 bg + green-900 text (measured on the reference).
    expect(tabs!.activeBg).toBe("rgb(220, 252, 231)");
    expect(tabs!.activeColor).toBe("rgb(20, 83, 45)");
    // Inactive: muted-foreground #737373.
    expect(tabs!.inactiveColor).toBe("rgb(115, 115, 115)");
    // The trigger base carries no sheet-era extras (no gap-1.5/svg rules).
    expect(tabs!.activeCls).not.toContain("gap-1.5");
  });

  test("summary-card labels compute as plain rgba white, not oklab (G9)", async ({ page }) => {
    const labels = await page.evaluate(() => {
      const grab = (txt: string) => {
        const el = [...document.querySelectorAll("main span, main p")].find(
          (x) => (x.textContent || "").trim() === txt && x.querySelectorAll("*").length === 0,
        );
        return el ? getComputedStyle(el).color : null;
      };
      return { assets: grab("Total Assets"), ratio: grab("Asset to Liability Ratio") };
    });
    expect(labels.assets).toBe("rgba(255, 255, 255, 0.7)");
    expect(labels.ratio).toBe("rgba(255, 255, 255, 0.8)");
  });
});

test.describe("net-worth dialogs (v6 — remediation-plan-v6.md G4/G5)", () => {
  test("asset + liability dialogs: Name and Last Updated span the full 624px row", async ({ page }) => {
    // Measured on the reference's asset + Add Liability dialogs (2-col grid
    // of 304px cells + 16px gap): Name and Last Updated carry
    // md:col-span-2 → 624px wrappers; the other fields stay 304px.
    const widths = () =>
      page.evaluate(() => {
        const dlg = document.querySelector('[role="dialog"]');
        if (!dlg) return null;
        const grab = (id: string) => {
          const input = dlg.querySelector(`#${id}`);
          if (!input) return null;
          const wrap = input.closest(".space-y-2") as HTMLElement;
          return { w: Math.round(wrap.getBoundingClientRect().width), span: /col-span-2/.test(wrap.className) };
        };
        return {
          type: grab("asset-type"),
          value: grab("asset-value"),
          name: grab("asset-name"),
          account: grab("asset-account"),
          date: grab("asset-date"),
        };
      });

    await page.goto("/networth");
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    await page.getByRole("button", { name: "Add Asset" }).first().click();
    await expect(page.locator('[role="dialog"]')).toBeVisible();
    const asset = await widths();
    expect(asset).not.toBeNull();
    expect(asset!.type!.w).toBe(304);
    expect(asset!.value!.w).toBe(304);
    expect(asset!.name!.w).toBe(624);
    expect(asset!.name!.span).toBe(true);
    expect(asset!.account!.w).toBe(304);
    expect(asset!.date!.w).toBe(624);
    expect(asset!.date!.span).toBe(true);
    await page.keyboard.press("Escape");

    await page.getByRole("tab", { name: "Liabilities" }).click();
    await expect(page.getByText("2 items · $311,250")).toBeVisible();
    await page.getByRole("button", { name: "Add Liability" }).first().click();
    await expect(page.locator('[role="dialog"]')).toBeVisible();
    const liab = await page.evaluate(() => {
      const dlg = document.querySelector('[role="dialog"]');
      if (!dlg) return null;
      const grab = (id: string) => {
        const input = dlg.querySelector(`#${id}`);
        if (!input) return null;
        const wrap = input.closest(".space-y-2") as HTMLElement;
        return { w: Math.round(wrap.getBoundingClientRect().width), span: /col-span-2/.test(wrap.className) };
      };
      return { name: grab("liability-name"), institution: grab("liability-institution"), date: grab("liability-date") };
    });
    expect(liab).not.toBeNull();
    expect(liab!.name!.w).toBe(624);
    expect(liab!.name!.span).toBe(true);
    expect(liab!.institution!.w).toBe(304);
    expect(liab!.date!.w).toBe(624);
    expect(liab!.date!.span).toBe(true);
  });

  test("asset/liability Type select is disabled when editing (reference behavior)", async ({ page }) => {
    // The reference disables the Asset Type combobox in edit mode (enabled
    // on create). Same pattern for the liability dialog.
    await page.goto("/networth");
    await expect(page.getByText("3 items · $65,300")).toBeVisible();

    // Edit the first asset via its card menu.
    const card = page.locator("main .group", { hasText: "Share Portfolio" }).first();
    await card.hover();
    await card.getByRole("button", { name: "Actions for Share Portfolio" }).click();
    await page.getByRole("menuitem", { name: "Edit" }).click();
    const editDlg = page.getByRole("dialog", { name: "Edit Asset" });
    await expect(editDlg).toBeVisible();
    await expect(editDlg.locator("#asset-type")).toBeDisabled();
    // Enabled on create (checked via the Add dialog in the same run).
    await page.keyboard.press("Escape");
    await page.getByRole("button", { name: "Add Asset" }).first().click();
    const addDlg = page.getByRole("dialog", { name: "Add Asset" });
    await expect(addDlg).toBeVisible();
    await expect(addDlg.locator("#asset-type")).toBeEnabled();
  });
});

test.describe("net worth mobile header chip (v14 — plan G3)", () => {
  // The reference renders the 48×48 gradient chip at mobile too (measured
  // 390×844: chip at x=16, h1 at x=76 — the gap-3 row survives the
  // breakpoint) and its page still fits the viewport.
  test.use({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true });

  test("chip renders beside the h1 with no horizontal overflow", async ({ page }) => {
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const geo = await page.evaluate(() => {
      const h1El = [...document.querySelectorAll("main h1")].find((h) =>
        (h.textContent || "").trim() === "Net Worth",
      );
      if (!h1El) return null;
      const row = h1El.parentElement!.parentElement!;
      const chipEl = [...row.children].find((c) => c.tagName === "DIV" && c !== h1El.parentElement);
      const cr = chipEl ? chipEl.getBoundingClientRect() : null;
      const hr = h1El.getBoundingClientRect();
      return {
        chipW: cr ? cr.width : null,
        chipX: cr ? cr.x : null,
        h1X: hr.x,
        h1Y: hr.y,
        scrollWidth: document.documentElement.scrollWidth,
        clientWidth: document.documentElement.clientWidth,
      };
    });
    expect(geo).not.toBeNull();
    expect(geo!.chipW).toBe(48);
    expect(geo!.chipX).toBe(16); // p-4 content edge at 390px
    expect(geo!.h1X - (geo!.chipX! + 48)).toBe(12); // gap-3
    expect(geo!.scrollWidth).toBeLessThanOrEqual(geo!.clientWidth + 1);
  });
});
