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

  // v30 G2 (docs/remediation-plan-v30.md): the tablist's ROVING arrow-key
  // semantics — measured live on BOTH sites in v30 (the reference is Radix
  // too: the identical attribute set down to data-orientation /
  // data-radix-collection-item, only the ID namespace differs). Both
  // tablists carry the RovingFocusGroup entry-focus pattern (container
  // tabIndex=0, both triggers -1 on a fresh load), and on both a REAL
  // ArrowRight from the focused Assets trigger moves focus to Liabilities,
  // flips aria-selected, and updates the roving tabindex. The v5 test above
  // pins the static geometry; this pins the behavior.
  test("the tablist roves on arrow keys: focus moves, selection flips, panel switches (v30 G2)", async ({ page }) => {
    // Focus the active (Assets) trigger programmatically, like a real
    // Tab-into-the-group entry focus would leave it.
    await page.evaluate(() => {
      const active = [...document.querySelectorAll('button[role="tab"]')].find(
        (x) => x.getAttribute("aria-selected") === "true",
      ) as HTMLElement | undefined;
      active?.focus();
    });
    await page.waitForTimeout(200);

    await page.keyboard.press("ArrowRight");
    await page.waitForTimeout(400); // activation + panel-mount settle

    const after = await page.evaluate(() => {
      const tabs = [...document.querySelectorAll('button[role="tab"]')];
      const ae = document.activeElement;
      return {
        focusedTxt: ae && ae !== document.body ? (ae.textContent || "").trim() : "(body)",
        focusedIsTab: !!(ae && ae.closest('[role="tablist"]')),
        assets: {
          sel: tabs[0]?.getAttribute("aria-selected"),
          tabIndex: tabs[0]?.getAttribute("tabindex"),
        },
        liabilities: {
          sel: tabs[1]?.getAttribute("aria-selected"),
          tabIndex: tabs[1]?.getAttribute("tabindex"),
        },
      };
    });
    // Focus moved to the Liabilities trigger (still inside the tablist).
    expect(after.focusedTxt).toBe("Liabilities");
    expect(after.focusedIsTab).toBe(true);
    // Automatic activation: aria-selected flipped.
    expect(after.assets.sel).toBe("false");
    expect(after.liabilities.sel).toBe("true");
    // The roving tabindex updated (the entry-focus stop moved).
    expect(after.assets.tabIndex).toBe("-1");
    expect(after.liabilities.tabIndex).toBe("0");
    // The panel switched: the seeded liability cards render.
    await expect(page.locator("div.rounded-xl").filter({ hasText: "Home Loan" }).first()).toBeVisible();
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

// ---------------------------------------------------------------------------
// v41 F2/F3 (docs/remediation-plan-v41.md) — the summary card's viewport
// census, measured live on BOTH sites (nw-summary-v41.mjs +
// nw-yoffset-v41.mjs + nw-below-v41.mjs):
//
//  - At 640×960 (the unmeasured MID viewport): FULL geometry parity — the
//    608px card, the 48px figure, the 64×64 chip at x=528, the 264×2 grid,
//    the 32px page rhythm.
//  - At 390×844: the superset pair — the reference's card is 432px wide
//    (74px page overflow, sw=464, its chip 26px offscreen at x=352); the
//    clone's fits (358px card, 24px figure, 1-col grid, chip inside).
//  - THE v41 FIX: the net-worth page's section rhythm ran mb-6 (24px)
//    where the reference runs mb-8 (32px) at BOTH gaps (header row→card,
//    card→tablist) — the items-view pages carry mb-8 since v20 G1; the
//    net-worth view was the one page left at the pre-v20 rhythm.
// ---------------------------------------------------------------------------
test.describe("net worth summary card census (v41 — plan F2/F3)", () => {
  test("the MID viewport (640×960) geometry census + the 32px rhythm (v41 F2)", async ({ page }) => {
    await page.setViewportSize({ width: 640, height: 960 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const geo = await page.evaluate(() => {
      const label = [...document.querySelectorAll("p, span, h2, div")].find(
        (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0,
      );
      if (!label) return null;
      const card = label.closest("div.rounded-2xl") as HTMLElement | null;
      if (!card) return null;
      const cr = card.getBoundingClientRect();
      const cs = getComputedStyle(card);
      // The figure (the net-worth amount).
      const h2 = [...card.querySelectorAll("h1, h2, h3, p")].find(
        (e) => /-?\$[\d,]+\.\d{2}/.test((e.textContent || "").trim()) && e !== label,
      );
      const h2r = h2 ? h2.getBoundingClientRect() : null;
      const h2cs = h2 ? getComputedStyle(h2) : null;
      // The 64×64 white/20% gradient chip (the rounded-full icon circle).
      const chip = [...card.querySelectorAll("div")].find((d) => {
        const r = d.getBoundingClientRect();
        const c = getComputedStyle(d);
        return (
          r.width > 40 && r.width < 90 &&
          (c.borderRadius === "9999px" || (parseFloat(c.borderRadius) > 40 && c.borderRadius !== "0px")) &&
          d.querySelector("svg")
        );
      });
      const chr = chip ? chip.getBoundingClientRect() : null;
      const chcs = chip ? getComputedStyle(chip) : null;
      // The stats grid (the "Total Assets" cell's [class*=grid] ancestor).
      const assetsLabel = [...card.querySelectorAll("p, span")].find(
        (e) => (e.textContent || "").trim() === "Total Assets",
      );
      const grid = assetsLabel ? assetsLabel.closest('[class*="grid"]') : null;
      const gridcs = grid ? getComputedStyle(grid) : null;
      const cells = grid
        ? [...grid.children].map((c) => {
            const r = c.getBoundingClientRect();
            return { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x) };
          })
        : [];
      // The ratio value (the border-t footer's right-hand span).
      const ratioLabel = [...card.querySelectorAll("span, p, div")].find(
        (e) => /Asset to Liability Ratio/.test((e.textContent || "")) && e.children.length === 0,
      );
      const ratioVal = ratioLabel
        ? [...(ratioLabel.parentElement?.children || [])].find((e) => e !== ratioLabel)
        : null;
      // The rhythm anchors: the page header row (the h1's gap-3 flex row)
      // and the tablist.
      const h1 = [...document.querySelectorAll("main h1")].find(
        (h) => (h.textContent || "").trim() === "Net Worth",
      );
      const chipRow = h1 ? (h1.parentElement!.parentElement!) : null;
      const crr = chipRow ? chipRow.getBoundingClientRect() : null;
      const tablist = document.querySelector('[role="tablist"]');
      const tlr = tablist ? tablist.getBoundingClientRect() : null;
      // The header chip (48×48, the v14 pin re-measured in the census).
      const headerChip = h1
        ? [...(h1.parentElement?.parentElement?.children || [])].find(
            (c) => c.tagName === "DIV" && c !== h1.parentElement,
          )
        : null;
      const hcr = headerChip ? headerChip.getBoundingClientRect() : null;
      return {
        card: {
          x: Math.round(cr.x), w: Math.round(cr.width), pad: cs.padding,
          radius: cs.borderRadius, bg: (cs.backgroundImage || "").slice(0, 60),
          shadow: (cs.boxShadow || "").slice(0, 60),
        },
        figure: h2cs
          ? { font: h2cs.fontSize, weight: h2cs.fontWeight, w: Math.round(h2r!.width) }
          : null,
        chip: chcs
          ? {
              w: Math.round(chr!.width), h: Math.round(chr!.height), x: Math.round(chr!.x),
              radius: chcs.borderRadius, bg: chcs.backgroundColor,
              iconW: Math.round(chip!.querySelector("svg")!.getBoundingClientRect().width),
            }
          : null,
        grid: gridcs
          ? { cols: gridcs.gridTemplateColumns, gap: gridcs.gap, cells }
          : null,
        ratio: ratioVal
          ? { text: (ratioVal.textContent || "").trim(), font: getComputedStyle(ratioVal).fontSize }
          : null,
        headerChip: hcr ? { w: Math.round(hcr.width), x: Math.round(hcr.x) } : null,
        rhythm: {
          headerToCard: crr ? Math.round(cr.y - crr.bottom) : null,
          cardToTablist: tlr ? Math.round(tlr.y - cr.bottom) : null,
        },
        sw: document.documentElement.scrollWidth,
        vw: window.innerWidth,
      };
    });
    expect(geo).not.toBeNull();
    if (!geo) throw new Error("summary card census found no card");

    // The card box — measured 608×(auto) at 640 on BOTH sites.
    expect(geo.card.x).toBe(16); // the p-4 content edge
    expect(geo.card.w).toBe(608); // 640 − 2×16
    expect(geo.card.pad).toBe("32px"); // p-8
    expect(geo.card.radius).toBe("16px"); // rounded-2xl
    expect(geo.card.bg).toContain("linear-gradient(135deg, rgb(45, 90, 74)");
    expect(geo.card.shadow).toContain("rgba(26, 58, 46, 0.3)");

    // The figure — 48px/700 from sm up (the reference's text-5xl).
    expect(geo.figure!.font).toBe("48px");
    expect(geo.figure!.weight).toBe("700");

    // The gradient chip — 64×64 at x=528, 9999px, white/20%, the 32px icon
    // (the reference's chip at the same x — both sites' cards are 608 wide).
    expect(geo.chip!.w).toBe(64);
    expect(geo.chip!.h).toBe(64);
    expect(geo.chip!.x).toBe(528);
    expect(geo.chip!.radius).toBe("9999px");
    expect(geo.chip!.bg).toBe("rgba(255, 255, 255, 0.2)");
    expect(geo.chip!.iconW).toBe(32);

    // The stats grid — the 2-col 264×264 tracks, 16px gap, 84px cells.
    expect(geo.grid!.cols).toBe("264px 264px");
    expect(geo.grid!.gap).toBe("16px");
    expect(geo.grid!.cells).toEqual([
      { w: 264, h: 84, x: 48 },
      { w: 264, h: 84, x: 328 },
    ]);

    // The ratio footer — the seed's 0.21:1 at 18px (text-lg).
    expect(geo.ratio!.text).toBe("0.21:1");
    expect(geo.ratio!.font).toBe("18px");

    // The header chip (the v14 pin, now in-census).
    expect(geo.headerChip!.w).toBe(48);
    expect(geo.headerChip!.x).toBe(16);

    // THE v41 RHYTHM PINS — the reference's 32px section gaps (mb-8); the
    // clone's pre-v41 mb-6 rendered 24 at both gaps, both viewports.
    expect(geo.rhythm.headerToCard, "the header row→card gap must be 32 (the reference's mb-8; v41 F1)").toBe(32);
    expect(geo.rhythm.cardToTablist, "the card→tablist gap must be 32 (the reference's mb-8; v41 F1)").toBe(32);

    // No overflow at the mid viewport (both sites measured sw=vw=640).
    expect(geo.sw).toBeLessThanOrEqual(geo.vw);
  });

  test("the MOBILE viewport (390×844) superset census — the card fits, the 24px figure, the 1-col grid (v41 F3)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const geo = await page.evaluate(() => {
      const label = [...document.querySelectorAll("p, span, h2, div")].find(
        (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0,
      );
      if (!label) return null;
      const card = label.closest("div.rounded-2xl") as HTMLElement | null;
      if (!card) return null;
      const cr = card.getBoundingClientRect();
      const cs = getComputedStyle(card);
      const h2 = [...card.querySelectorAll("h1, h2, h3, p")].find(
        (e) => /-?\$[\d,]+\.\d{2}/.test((e.textContent || "").trim()) && e !== label,
      );
      const h2cs = h2 ? getComputedStyle(h2) : null;
      const chip = [...card.querySelectorAll("div")].find((d) => {
        const r = d.getBoundingClientRect();
        const c = getComputedStyle(d);
        return (
          r.width > 40 && r.width < 90 &&
          (c.borderRadius === "9999px" || (parseFloat(c.borderRadius) > 40 && c.borderRadius !== "0px")) &&
          d.querySelector("svg")
        );
      });
      const chr = chip ? chip.getBoundingClientRect() : null;
      const assetsLabel = [...card.querySelectorAll("p, span")].find(
        (e) => (e.textContent || "").trim() === "Total Assets",
      );
      const grid = assetsLabel ? assetsLabel.closest('[class*="grid"]') : null;
      const gridcs = grid ? getComputedStyle(grid) : null;
      return {
        card: { x: Math.round(cr.x), w: Math.round(cr.width), pad: cs.padding, radius: cs.borderRadius, bg: (cs.backgroundImage || "").slice(0, 60), shadow: (cs.boxShadow || "").slice(0, 60) },
        figureFont: h2cs ? h2cs.fontSize : null,
        chip: chr ? { w: Math.round(chr.width), x: Math.round(chr.x), right: Math.round(chr.right) } : null,
        gridCols: gridcs ? gridcs.gridTemplateColumns : null,
        sw: document.documentElement.scrollWidth,
        vw: window.innerWidth,
      };
    });
    expect(geo).not.toBeNull();
    if (!geo) throw new Error("summary card census found no card");

    // The superset pair: the reference's card at 390 is 432 wide (74px page
    // overflow, sw=464, its chip at x=352 — 26px past the viewport); the
    // clone's FITS: 358 = 390 − 2×16 (p-4), sw=390.
    expect(geo.card.x).toBe(16);
    expect(geo.card.w).toBe(358);
    expect(geo.sw).toBeLessThanOrEqual(geo.vw + 1);

    // The card CHROME matches the reference's byte-for-byte (the gradient,
    // the radius, the 32px pad, the shadow) — the superset class, not a
    // visual divergence.
    expect(geo.card.pad).toBe("32px");
    expect(geo.card.radius).toBe("16px");
    expect(geo.card.bg).toContain("linear-gradient(135deg, rgb(45, 90, 74)");
    expect(geo.card.shadow).toContain("rgba(26, 58, 46, 0.3)");

    // The figure at 24px (text-2xl — superset fix #6: the reference's fixed
    // 48px text-5xl overflows its own 390 viewport by 74px).
    expect(geo.figureFont).toBe("24px");

    // The 1-col grid (the reference's fixed 2-col overflows at 390).
    expect(geo.gridCols).toBe("294px");

    // The chip fully visible (the reference's hangs 26px offscreen).
    expect(geo.chip!.w).toBe(64);
    expect(geo.chip!.x).toBeGreaterThanOrEqual(16);
    expect(geo.chip!.right).toBeLessThanOrEqual(geo.vw - 16 + 1);
  });

  // v63 F3 (docs/remediation-plan-v63.md) — the stat-tile family census at
  // 390, measured live on BOTH sites (arbit-v63.sh, the /networth 390
  // full-page pair's three-flag arbitration): the v41 F3 pin above covers
  // the card w/pad/radius/bg/shadow, the 24px figure, the gridCols and the
  // chip bounds — but NOT the tile geometry, the tile chrome, the grid
  // gap, the card HEIGHT arithmetic, or the medallion's inner icon.
  //
  //   - The stat grid: cols "294px" (1-col), gap "16px", w 294, 2 children.
  //   - The tiles: 294×84 each — the h 84 = p-4 16 + label 16 + mb-1 4 +
  //     text-2xl amount 32 + p-4 16 (deterministic under the fixed seed);
  //     chrome: bg rgba(255,255,255,0.1), backdrop blur(10px), radius 12,
  //     pad 16px — byte-identical to the reference's own tiles.
  //   - The card HEIGHT: 421 — the 1-col stacking arithmetic (the
  //     reference's own card renders h 333 with its fixed 2-col grid
  //     inside its 432-wide overflow; the clone's 421 = 333 + the second
  //     84px tile row + the 16px gap — the v63 pair's flag-1/flag-2
  //     contract, the v41 mobile-superset class).
  //   - The medallion's inner icon: 32×32 (h-8 w-8) inside the 64×64
  //     circle — byte-identical on both sides (the reference's CLIPS the
  //     390 viewport at right 416, the v54 class; the VLM's "larger in the
  //     clone" flag was the perception artifact of that clipping).
  test("the stat-tile family census at 390 — the tiles, the grid gap, the card height arithmetic, the medallion icon (v63 F3)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const census = await page.evaluate(() => {
      const label = [...document.querySelectorAll("p, span, h2, div")].find(
        (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0,
      );
      if (!label) return null;
      const card = label.closest("div.rounded-2xl") as HTMLElement | null;
      if (!card) return null;
      const cr = card.getBoundingClientRect();
      // The stat grid: the "Total Assets" leaf label's grid parent — NOT
      // the card grid (the v46 F2 lesson: the summary card's inner
      // sm:grid-cols-2 stat grid, never an outer grid).
      const assetsLabel = [...card.querySelectorAll("p, span")].find(
        (e) => (e.textContent || "").trim() === "Total Assets",
      );
      const grid = assetsLabel ? (assetsLabel.closest('[class*="grid"]') as HTMLElement | null) : null;
      if (!grid) return null;
      const gcs = getComputedStyle(grid);
      const gr = grid.getBoundingClientRect();
      const tiles = [...grid.children].map((c) => {
        const el = c as HTMLElement;
        const r = el.getBoundingClientRect();
        const s = getComputedStyle(el);
        return {
          w: Math.round(r.width), h: Math.round(r.height),
          bg: s.backgroundColor, blur: s.backdropFilter,
          radius: s.borderRadius, pad: s.padding,
        };
      });
      // The medallion (the v41 chip finder) + its inner svg.
      const chip = [...card.querySelectorAll("div")].find((d) => {
        const r = d.getBoundingClientRect();
        const c = getComputedStyle(d);
        return (
          r.width > 40 && r.width < 90 &&
          (c.borderRadius === "9999px" || (parseFloat(c.borderRadius) > 40 && c.borderRadius !== "0px")) &&
          d.querySelector("svg")
        );
      });
      const svg = chip ? chip.querySelector("svg") : null;
      const sr = svg ? svg.getBoundingClientRect() : null;
      return {
        cardH: Math.round(cr.height),
        grid: { cols: gcs.gridTemplateColumns, gap: gcs.gap, w: Math.round(gr.width), children: grid.children.length },
        tiles,
        medallionSvg: sr ? { w: Math.round(sr.width), h: Math.round(sr.height) } : null,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("stat-tile census found no grid");

    // The stat grid: 1-col at 390, the 16px gap, the 294px track.
    expect(census.grid.cols).toBe("294px");
    expect(census.grid.gap).toBe("16px");
    expect(census.grid.w).toBe(294);
    expect(census.grid.children).toBe(2);

    // The tiles: 294×84 each, the translucent-blur chrome byte-identical
    // to the reference's own tiles (176×84 in its overflowing 2-col).
    expect(census.tiles).toHaveLength(2);
    for (const t of census.tiles) {
      expect(t.w).toBe(294);
      expect(t.h).toBe(84);
      expect(t.bg).toBe("rgba(255, 255, 255, 0.1)");
      expect(t.blur).toBe("blur(10px)");
      expect(t.radius).toBe("12px");
      expect(t.pad).toBe("16px");
    }

    // The card height: the 1-col stacking arithmetic (the reference's own
    // 333 + 84 + 16 — the superset class, not a divergence).
    expect(census.cardH).toBe(421);

    // The medallion's inner icon: 32×32, byte-identical both sides.
    expect(census.medallionSvg).not.toBeNull();
    expect(census.medallionSvg!.w).toBe(32);
    expect(census.medallionSvg!.h).toBe(32);
  });
});

test.describe("net-worth asset card census (v46 — remediation-plan-v46.md F2/F3)", () => {
  test("the ASSET CARD census at 1280 + the REAL-hover inert + the kebab reveal (v46 F2)", async ({ page }) => {
    // The session-101 queue's first candidate, measured live on BOTH sites
    // (nw-card-v46.mjs + the REAL-hover driver steps): the grid, the card
    // chrome, the hover state — everything byte-identical EXCEPT the
    // value→facts spacing (the reference's mb-4 wrap = 16px vs the clone's
    // pre-v46 bare mb-2 P = 8px — the F1 fix; the card h 186→194).
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
    // The settle pattern: wait for the first seeded card before probing.
    const card0 = page.locator("div.rounded-xl").filter({ hasText: "Everyday Account" }).first();
    await expect(card0).toBeVisible();

    const census = await page.evaluate(() => {
      // The asset-card grid: md:grid-cols-2 lg:grid-cols-3 at 1280
      // (net-worth-view.tsx:459; the reference's own grid the identical
      // family). NOT the summary card's inner sm:grid-cols-2 stat grid.
      const grid = [...document.querySelectorAll("div")].find((d) => {
        if (typeof d.className !== "string") return false;
        return d.className.includes("lg:grid-cols-3") && d.children.length >= 1;
      });
      if (!grid) return null;
      const gcs = getComputedStyle(grid);
      const gr = grid.getBoundingClientRect();
      const card = grid.children[0] as HTMLElement;
      const cs = getComputedStyle(card);
      const cr = card.getBoundingClientRect();
      const titleEl = card.querySelector("h4");
      const dot = [...card.querySelectorAll("div")].find((d) => {
        const dcs = getComputedStyle(d);
        const dcr = d.getBoundingClientRect();
        return !d.children.length && dcr.width > 0 && dcr.width <= 12 && dcs.backgroundColor !== "rgba(0, 0, 0, 0)";
      });
      const value = [...card.querySelectorAll("p")].find((p) => {
        const pcs = getComputedStyle(p);
        return pcs.fontSize === "24px" && pcs.fontWeight === "700";
      });
      const facts = [...card.querySelectorAll("div")].find((d) =>
        typeof d.className === "string" && d.className.includes("space-y-2"),
      );
      const kebab = [...card.querySelectorAll("button")].find(
        (b) => !(b.textContent || "").trim() && b.querySelectorAll("svg").length === 1,
      );
      // Tag for the REAL hover step.
      card.setAttribute("data-v46-card", "first");
      if (kebab) kebab.setAttribute("data-v46-kebab", "first");
      return {
        grid: {
          w: Math.round(gr.width),
          cols: gcs.gridTemplateColumns,
          gap: gcs.gap,
        },
        card: {
          w: Math.round(cr.width),
          h: Math.round(cr.height),
          pad: cs.padding,
          radius: cs.borderRadius,
          border: `${cs.borderTopWidth} ${cs.borderTopStyle} ${cs.borderTopColor}`,
          boxShadow: cs.boxShadow,
          bg: cs.backgroundColor,
          transition: cs.transitionProperty,
          transitionDur: cs.transitionDuration,
        },
        titleRow: titleEl
          ? {
              gap: getComputedStyle(titleEl.parentElement!).gap,
              dotW: dot ? Math.round(dot.getBoundingClientRect().width) : null,
              dotBg: dot ? getComputedStyle(dot).backgroundColor : null,
              titleFont: getComputedStyle(titleEl).fontSize,
              titleWeight: getComputedStyle(titleEl).fontWeight,
            }
          : null,
        value: value
          ? {
              font: getComputedStyle(value).fontSize,
              weight: getComputedStyle(value).fontWeight,
              mb: getComputedStyle(value).marginBottom,
            }
          : null,
        facts: facts ? { font: getComputedStyle(facts).fontSize, color: getComputedStyle(facts).color } : null,
        kebab: kebab
          ? {
              w: Math.round(kebab.getBoundingClientRect().width),
              h: Math.round(kebab.getBoundingClientRect().height),
              opacity: getComputedStyle(kebab).opacity,
            }
          : null,
        sw: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("card census found no grid");

    // The grid: 960 = the rail 256 + the content column 1024 − the p-8 64;
    // 3 columns × 309.328, gap 16 — byte-identical to the reference's.
    expect(census.grid.w).toBe(960);
    expect(census.grid.cols).toBe("309.328px 309.328px 309.328px");
    expect(census.grid.gap).toBe("16px");

    // The card chrome (the v45 items-card family): pad 20, radius 12, the
    // border + the INLINE rest shadow (Chrome normalizes the 3-value inline
    // to the reference's 4-value computed — byte-identical strings).
    expect(census.card.w).toBe(309);
    expect(census.card.pad).toBe("20px");
    expect(census.card.radius).toBe("12px");
    expect(census.card.border).toBe("1px solid rgb(229, 231, 227)");
    expect(census.card.boxShadow).toContain("rgba(0, 0, 0, 0.04) 0px 2px 8px 0px");
    expect(census.card.bg).toBe("rgb(255, 255, 255)");
    expect(census.card.transition).toContain("all");
    expect(census.card.transitionDur).toBe("0.2s");

    // THE F1 FIX (the v46 gap): the value→facts spacing — the reference
    // wraps its value in mb-4 (16px); the clone's pre-fix bare mb-2 P
    // rendered 8px (the card h 186 vs the reference's 194).
    expect(census.value!.mb).toBe("16px");
    expect(census.card.h).toBe(194);

    // The title row + the value + the facts (byte-identical chrome).
    expect(census.titleRow!.gap).toBe("8px");
    expect(census.titleRow!.dotW).toBe(8);
    expect(census.titleRow!.dotBg).toBe("rgb(143, 188, 63)");
    expect(census.titleRow!.titleFont).toBe("16px");
    expect(census.titleRow!.titleWeight).toBe("600");
    expect(census.value!.font).toBe("24px");
    expect(census.value!.weight).toBe("700");
    expect(census.facts!.font).toBe("12px");
    expect(census.facts!.color).toBe("rgb(107, 114, 128)");

    // The kebab: 36×36, opacity 0 at rest (the group-hover reveal).
    expect(census.kebab!.w).toBe(36);
    expect(census.kebab!.h).toBe(36);
    expect(census.kebab!.opacity).toBe("0");

    // The REAL hover (locator.hover — the ONLY way to engage CSS :hover,
    // the v45 lesson): the card's shadow stays INERT (the inline beats the
    // hover:shadow-lg utility — the v29 family, both sites) while the
    // kebab REVEALS (opacity 0→1) and the card never translates.
    const restShadow = census.card.boxShadow;
    await page.locator('[data-v46-card="first"]').hover();
    await page.waitForTimeout(300);
    const hoverState = await page.evaluate(() => {
      const c = document.querySelector('[data-v46-card="first"]')!;
      const kb = document.querySelector('[data-v46-kebab="first"]');
      return {
        boxShadow: getComputedStyle(c).boxShadow,
        kebabOpacity: kb ? getComputedStyle(kb).opacity : null,
        translateY: getComputedStyle(c).translate,
      };
    });
    expect(hoverState.boxShadow).toBe(restShadow); // INERT — byte-identical
    expect(hoverState.kebabOpacity).toBe("1");
    expect(hoverState.translateY).toBe("none");
  });

  test("the confirm-bar white-pill census + the shadow-sm regression pin (v46 F3)", async ({ page }) => {
    // The five-site confirm-bar Cancel-pill family's shadow-sm (the
    // session-101 queue's third candidate): the --shadow-sm theme pin's
    // regression net — the reference has NO confirm bars (its deletes are
    // direct, the v18 superset-fix-#6 family re-confirmed live this
    // session), so this pins the CLONE's own superset chrome.
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
    const card = page.locator("div.rounded-xl").filter({ hasText: "Everyday Account" }).first();
    await expect(card).toBeVisible();

    // The native click opens the Radix menu (the v46 lesson: synthetic
    // el.click() does NOT open it — Radix ignores non-pointer events).
    await card.getByRole("button", { name: "Actions for Everyday Account" }).click();
    await page.getByRole("menuitem", { name: "Delete" }).click();
    await expect(card.getByText("Delete this asset?")).toBeVisible();

    const census = await page.evaluate(() => {
      const bar = [...document.querySelectorAll("div")].find((d) => {
        const bcs = getComputedStyle(d);
        if (bcs.backgroundColor !== "rgb(254, 242, 242)") return false;
        const btns = [...d.querySelectorAll("button")];
        return btns.length === 2 && btns[0].textContent.trim() === "Cancel" && btns[1].textContent.trim() === "Delete";
      });
      if (!bar) return null;
      const barCs = getComputedStyle(bar);
      const barR = bar.getBoundingClientRect();
      const label = bar.querySelector("p");
      const cancel = [...bar.querySelectorAll("button")].find((b) => b.textContent.trim() === "Cancel")!;
      const ccs = getComputedStyle(cancel);
      const del = [...bar.querySelectorAll("button")].find((b) => b.textContent.trim() === "Delete")!;
      const dcs = getComputedStyle(del);
      return {
        bar: {
          mt: barCs.marginTop,
          radius: barCs.borderRadius,
          pad: barCs.padding,
          bg: barCs.backgroundColor,
          justify: barCs.justifyContent,
          h: Math.round(barR.height),
        },
        label: label ? { font: getComputedStyle(label).fontSize, weight: getComputedStyle(label).fontWeight } : null,
        cancelPill: {
          bg: ccs.backgroundColor,
          pad: ccs.padding,
          radius: ccs.borderRadius,
          font: ccs.fontSize,
          weight: ccs.fontWeight,
          boxShadow: ccs.boxShadow,
          h: Math.round(cancel.getBoundingClientRect().height),
        },
        deleteBtn: {
          color: dcs.color,
          pad: dcs.padding,
          radius: dcs.borderRadius,
          font: dcs.fontSize,
          weight: dcs.fontWeight,
        },
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("confirm-bar census found no bar");

    // The bar chrome (the v18 superset's family): the red-tinted row.
    expect(census.bar.mt).toBe("16px");
    expect(census.bar.radius).toBe("8px");
    expect(census.bar.pad).toBe("12px");
    expect(census.bar.bg).toBe("rgb(254, 242, 242)");
    expect(census.bar.justify).toBe("space-between");
    expect(census.label!.font).toBe("14px");

    // The Cancel pill: the white bg + the 4/12 pad + the 6px radius + the
    // 12px-500 — and THE PIN: the shadow-sm VISIBLE layer `rgba(0, 0, 0,
    // 0.05) 0px 1px 2px 0px` (the --shadow-sm theme pin's restored v3
    // value — the shadow-scale regression net's fifth site, the v45 family;
    // toContain = the accepted-leads convention, the v10 lesson).
    expect(census.cancelPill.bg).toBe("rgb(255, 255, 255)");
    expect(census.cancelPill.pad).toBe("4px 12px");
    expect(census.cancelPill.radius).toBe("6px");
    expect(census.cancelPill.font).toBe("12px");
    expect(census.cancelPill.weight).toBe("500");
    expect(census.cancelPill.boxShadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // The Delete twin: the same pad/radius/font family, white text.
    expect(census.deleteBtn.color).toBe("rgb(255, 255, 255)");
    expect(census.deleteBtn.pad).toBe("4px 12px");
    expect(census.deleteBtn.radius).toBe("6px");
    expect(census.deleteBtn.font).toBe("12px");
    expect(census.deleteBtn.weight).toBe("500");

    // The fixture-restore discipline: Cancel dismisses the bar (the delete
    // NEVER fires — the census ran while the bar was up).
    await card.getByRole("button", { name: "Cancel" }).click();
    await expect(card.getByText("Delete this asset?")).not.toBeVisible();
    await expect(card.getByRole("heading", { name: "Everyday Account" })).toBeVisible();
  });
});

test.describe("net-worth card mobile census (v47 — plan F2)", () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
  });

  test("the asset card's mobile rhythm matches the reference's 194px census", async ({ page }) => {
    // v47 — the v46 fix's mobile follow-up, measured live on BOTH sites
    // at 390: the reference's asset card (inside its 432-wide
    // OVERFLOWING grid — its documented superset-fix-#4 bug) renders h
    // 194 / pad 20 / radius 12 / border 1px rgb(229,231,227) / rest
    // shadow rgba(0,0,0,0.04) 0px 2px 8px 0px / transition 0.2s; the
    // value→facts gap 16 (its div.mb-4 wrap); the facts 12px
    // rgb(107,114,128). The clone's card: the identical chrome +
    // rhythm (the v46 fix holds at 390 — the clone carries the margin
    // ON the P, the computed geometry is the contract) — and the page
    // FITS (docSW 390 vs the reference's 464, the superset fix).
    const census = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) =>
          d.className.toString().includes("grid-cols-1") &&
          d.className.toString().includes("md:grid-cols-2") &&
          d.className.toString().includes("lg:grid-cols-3") &&
          d.querySelector("button"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement;
      const cs = getComputedStyle(card);
      const r = card.getBoundingClientRect();
      const vp = card.querySelector("p.text-2xl");
      const facts = vp ? (vp.nextElementSibling as HTMLElement | null) : null;
      return {
        gridW: Math.round(grid.getBoundingClientRect().width),
        gridGap: getComputedStyle(grid).gap,
        gridCols: getComputedStyle(grid).gridTemplateColumns.split(" ").length,
        card: {
          w: Math.round(r.width),
          h: Math.round(r.height),
          pad: cs.padding,
          radius: cs.borderRadius,
          border: cs.border,
          shadow: cs.boxShadow,
          transition: cs.transition,
        },
        value: vp
          ? {
              mb: getComputedStyle(vp).marginBottom,
              fs: getComputedStyle(vp).fontSize,
              lh: getComputedStyle(vp).lineHeight,
              color: getComputedStyle(vp).color,
            }
          : null,
        facts: facts
          ? {
              fs: getComputedStyle(facts).fontSize,
              color: getComputedStyle(facts).color,
              gap: Math.round(facts.getBoundingClientRect().y - (vp as HTMLElement).getBoundingClientRect().bottom),
            }
          : null,
        docSW: document.documentElement.scrollWidth,
        mainSW: document.querySelector("main")?.scrollWidth ?? null,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("mobile census found no card grid");

    // The grid: single column at 390, the 16px gap — the page fits.
    expect(census.gridW).toBe(358);
    expect(census.gridGap).toBe("16px");
    expect(census.gridCols).toBe(1);
    expect(census.docSW).toBe(390);
    expect(census.mainSW).toBe(390);

    // The card chrome — byte-identical to the reference's measured
    // mobile census (the 432-wide card's INTERNAL metrics, the same).
    expect(census.card.w).toBe(358);
    expect(census.card.h).toBe(194);
    expect(census.card.pad).toBe("20px");
    expect(census.card.radius).toBe("12px");
    expect(census.card.border).toBe("1px solid rgb(229, 231, 227)");
    expect(census.card.shadow).toContain("rgba(0, 0, 0, 0.04) 0px 2px 8px 0px");
    expect(census.card.transition).toContain("0.2s cubic-bezier(0.4, 0, 0.2, 1)");

    // The value→facts rhythm: the v46 fix holds at 390 — mb 16 / fs 24
    // / lh 32 / the lime value color / the measured gap 16.
    expect(census.value!.mb).toBe("16px");
    expect(census.value!.fs).toBe("24px");
    expect(census.value!.lh).toBe("32px");
    expect(census.value!.color).toBe("rgb(143, 188, 63)");
    expect(census.facts!.fs).toBe("12px");
    expect(census.facts!.color).toBe("rgb(107, 114, 128)");
    expect(census.facts!.gap).toBe(16);
  });
});

// ---------------------------------------------------------------------------
// v50 — plan F2 (docs/remediation-plan-v50.md): the tablist's CHROME census
// at the 640 mid viewport. The v14 G2 pinned the tab icons' 16px
// currentColor family and the EXISTING 1280 test pins the 448 grid + the
// green active pair; the v41 F2/F3 pinned the summary card at 640. The
// v50 pin locks the mid-viewport tablist chrome measured live on the
// reference at 640x960 (ref-v50.sh — byte-identical on every axis):
//   the list: w 448 / h 36 / grid "220px 220px" / bg #f5f5f5 / radius 8
//             / pad 4 / x 16
//   the active trigger: 220x28 / radius 6 / 14px/500 / #14532d on
//             #dcfce7 / a 2-slot all-transparent shadow / the 16x16
//             icon at currentColor #14532d
//   the inactive trigger: 220x28 / radius 6 / 14px/500 / #737373 /
//             transparent / no shadow / the 16x16 icon at #737373
// ---------------------------------------------------------------------------
test.describe("net worth tablist chrome census (v50 — plan F2)", () => {
  test("the tablist's full chrome at 640 matches the reference (byte-parity)", async ({ page }) => {
    await page.setViewportSize({ width: 640, height: 960 });
    await page.goto("/networth");
    await expect(page.getByRole("tab", { name: /Assets/i })).toBeVisible();

    const census = await page.evaluate(() => {
      const triggers = [...document.querySelectorAll('button[role="tab"]')];
      const active = triggers.find((t) => t.getAttribute("aria-selected") === "true");
      const inactive = triggers.find((t) => t.getAttribute("aria-selected") === "false");
      const list = document.querySelector('[role="tablist"]') as HTMLElement | null;
      if (!active || !inactive || !list) return null;
      const grab = (t: HTMLElement) => {
        const cs = getComputedStyle(t);
        const r = t.getBoundingClientRect();
        const icon = t.querySelector("svg");
        return {
          w: Math.round(r.width),
          h: Math.round(r.height),
          radius: cs.borderRadius,
          fs: cs.fontSize,
          fw: cs.fontWeight,
          color: cs.color,
          bg: cs.backgroundColor,
          shadow: cs.boxShadow,
          icon: icon
            ? {
                w: Math.round(icon.getBoundingClientRect().width),
                h: Math.round(icon.getBoundingClientRect().height),
                color: getComputedStyle(icon).color,
              }
            : null,
        };
      };
      const lcs = getComputedStyle(list);
      const lr = list.getBoundingClientRect();
      return {
        list: {
          w: Math.round(lr.width),
          h: Math.round(lr.height),
          display: lcs.display,
          gridCols: lcs.gridTemplateColumns,
          bg: lcs.backgroundColor,
          radius: lcs.borderRadius,
          pad: lcs.padding,
          x: Math.round(lr.x),
        },
        active: grab(active as HTMLElement),
        inactive: grab(inactive as HTMLElement),
      };
    });
    expect(census).not.toBeNull();
    // The list: the reference's grid w-full max-w-md grid-cols-2 at the
    // 640 mid viewport (the 608 content minus... the max-w-md cap 448).
    expect(census!.list).toEqual({
      w: 448,
      h: 36,
      display: "grid",
      gridCols: "220px 220px",
      bg: "rgb(245, 245, 245)",
      radius: "8px",
      pad: "4px",
      x: 16,
    });
    // The ACTIVE trigger (Assets): the green pair + the
    // data-[state=active]:shadow emission.
    expect(census!.active).toMatchObject({
      w: 220,
      h: 28,
      radius: "6px",
      fs: "14px",
      fw: "500",
      color: "rgb(20, 83, 45)",
      bg: "rgb(220, 252, 231)",
    });
    // The shadow: the shadow-sm VISIBLE pair byte-identical on both
    // sites (the full reference string: 2 transparent leads + the two
    // visible layers; the clone emits 4 transparent leads — the
    // documented accepted lead-divergence class, v10/v25/v45/v49:
    // transparent layers never render). Pin the visible layers.
    expect(census!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(census!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(census!.active!.icon).toEqual({ w: 16, h: 16, color: "rgb(20, 83, 45)" });
    // The INACTIVE trigger (Liabilities): the muted pair, transparent,
    // shadow none.
    expect(census!.inactive).toMatchObject({
      w: 220,
      h: 28,
      radius: "6px",
      fs: "14px",
      fw: "500",
      color: "rgb(115, 115, 115)",
      bg: "rgba(0, 0, 0, 0)",
      shadow: "none",
    });
    expect(census!.inactive!.icon).toEqual({ w: 16, h: 16, color: "rgb(115, 115, 115)" });
  });
});

// ---------------------------------------------------------------------------
// v53 — plan F1 (docs/remediation-plan-v53.md): the tablist's MOBILE census
// at 390. The v50 F2 pinned this family at the 640 mid viewport only (the
// list 448 / the triggers 220); the v41 F2/F3 + the v47 net-worth card
// censuses walked the page's other mobile surfaces. The v53 pin locks the
// mobile tablist chrome measured live on the reference at 390x844
// (ref-v53.sh — byte-identical on every axis except the width family):
//   the list: w 358 (the in-bounds content column) / h 36 / grid
//             "175px 175px" / bg #f5f5f5 / radius 8 / pad 4 / x 16
//   the active trigger: 175x28 / radius 6 / 14px/500 / #14532d on
//             #dcfce7 / the shadow-sm VISIBLE pair / the 16x16 icon at
//             #14532d
//   the inactive trigger: 175x28 / radius 6 / 14px/500 / #737373 /
//             transparent / no shadow / the 16x16 icon at #737373
//   docSW 390 (the superset invariant — the reference reads 464, its own
//   documented overflow bug: its list renders 432 wide inside the
//   464-overflow page, overhanging the 390 viewport; the same documented
//   divergence class as the v47 net-worth card mobile census).
// ---------------------------------------------------------------------------
test.describe("net worth tablist mobile census (v53 — plan F1)", () => {
  test("the tablist's full chrome at 390 matches the reference (byte-parity)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByRole("tab", { name: /Assets/i })).toBeVisible();

    const census = await page.evaluate(() => {
      const triggers = [...document.querySelectorAll('button[role="tab"]')];
      const active = triggers.find((t) => t.getAttribute("aria-selected") === "true");
      const inactive = triggers.find((t) => t.getAttribute("aria-selected") === "false");
      const list = document.querySelector('[role="tablist"]') as HTMLElement | null;
      if (!active || !inactive || !list) return null;
      const grab = (t: HTMLElement) => {
        const cs = getComputedStyle(t);
        const r = t.getBoundingClientRect();
        const icon = t.querySelector("svg");
        return {
          w: Math.round(r.width),
          h: Math.round(r.height),
          radius: cs.borderRadius,
          fs: cs.fontSize,
          fw: cs.fontWeight,
          color: cs.color,
          bg: cs.backgroundColor,
          shadow: cs.boxShadow,
          pad: cs.padding,
          icon: icon
            ? {
                w: Math.round(icon.getBoundingClientRect().width),
                h: Math.round(icon.getBoundingClientRect().height),
                color: getComputedStyle(icon).color,
              }
            : null,
        };
      };
      const lcs = getComputedStyle(list);
      const lr = list.getBoundingClientRect();
      return {
        list: {
          w: Math.round(lr.width),
          h: Math.round(lr.height),
          x: Math.round(lr.x),
          display: lcs.display,
          gridCols: lcs.gridTemplateColumns,
          bg: lcs.backgroundColor,
          radius: lcs.borderRadius,
          pad: lcs.padding,
          maxW: lcs.maxWidth,
        },
        active: grab(active as HTMLElement),
        inactive: grab(inactive as HTMLElement),
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The list: the in-bounds mobile column (the reference's own list is
    // 432 wide inside its 464-overflow page — its documented bug; every
    // non-width axis byte-identical).
    expect(census!.list).toEqual({
      w: 358,
      h: 36,
      x: 16,
      display: "grid",
      gridCols: "175px 175px",
      bg: "rgb(245, 245, 245)",
      radius: "8px",
      pad: "4px",
      maxW: "448px",
    });
    // The ACTIVE trigger (Assets): the green pair + the shadow emission.
    expect(census!.active).toMatchObject({
      w: 175,
      h: 28,
      radius: "6px",
      fs: "14px",
      fw: "500",
      color: "rgb(20, 83, 45)",
      bg: "rgb(220, 252, 231)",
      pad: "4px 12px",
    });
    // The shadow: the shadow-sm VISIBLE pair (the accepted
    // lead-divergence class — transparent layers never render).
    expect(census!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(census!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(census!.active!.icon).toEqual({ w: 16, h: 16, color: "rgb(20, 83, 45)" });
    // The INACTIVE trigger (Liabilities): the muted pair.
    expect(census!.inactive).toMatchObject({
      w: 175,
      h: 28,
      radius: "6px",
      fs: "14px",
      fw: "500",
      color: "rgb(115, 115, 115)",
      bg: "rgba(0, 0, 0, 0)",
      shadow: "none",
      pad: "4px 12px",
    });
    expect(census!.inactive!.icon).toEqual({ w: 16, h: 16, color: "rgb(115, 115, 115)" });
    // The superset invariant: the clone's /networth page stays in-bounds
    // at 390 (the reference overflows to 464 — its documented bug).
    expect(census!.docSW).toBe(390);
  });
});

test.describe("net worth view census at 1280 (v60 — plan F1)", () => {
  // The v60 standing pair's pin: the summary card + the tablist at the
  // 1280x800 pair viewport (the v41 F2/F3 pins walk them at 640/390; the
  // v50 F2 tablist at 640, the v53 F1 at 390 — the 1280 axes unpinned
  // until v60). Measured live on BOTH sites (nw-census-ref-v60.sh +
  // nw-census-clone-v60.sh): byte-identical on every axis — the summary
  // card 960/32px/16px/the 135deg forest→lime gradient/the 26-58-46
  // shadow; the figure 48px/700; the medallion 64×64; the stat grid
  // 440×2 gap 16; the stat tile 16px/12px/white-10%/blur(10px); the
  // ratio value 18px/700 (the seed's 0.21:1 vs the reference's own ∞:1
  // — the formatRatio data class); the tablist 448/36/220px 220px (the
  // v50 F2's own values, max-w-md capped at every viewport ≥ 448); the
  // group header 18px/600/forest-medium; + the v46 F2 grid/card controls
  // re-asserted (960 / 3×309.328 / gap 16 / the card 309/20px/12px).
  test("the summary card + tablist + group/grid controls at the pair viewport (v60 F1)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const census = await page.evaluate(() => {
      const label = [...document.querySelectorAll("p, span, h2, div")].find(
        (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0,
      );
      if (!label) return null;
      const card = label.closest("div.rounded-2xl") as HTMLElement | null;
      if (!card) return null;
      const cr = card.getBoundingClientRect();
      const cs = getComputedStyle(card);
      // The figure (the net-worth amount).
      const h2 = [...card.querySelectorAll("h1, h2, h3, p")].find(
        (e) => /-?\$[\d,]+\.\d{2}/.test((e.textContent || "").trim()) && e !== label,
      );
      const h2cs = h2 ? getComputedStyle(h2) : null;
      // The medallion (the round icon chip in the card head).
      const chip = [...card.querySelectorAll("div")].find((d) => {
        const r = d.getBoundingClientRect();
        const c = getComputedStyle(d);
        return r.width > 40 && r.width < 90 && c.borderRadius === "9999px" && d.querySelector("svg");
      });
      // The stats grid + the first tile.
      const assetsLabel = [...card.querySelectorAll("p, span")].find(
        (e) => (e.textContent || "").trim() === "Total Assets",
      );
      const grid = assetsLabel ? assetsLabel.closest('[class*="grid"]') : null;
      const gcs = grid ? getComputedStyle(grid) : null;
      const tile = assetsLabel ? assetsLabel.closest('[class*="rounded"]') : null;
      const tcs = tile ? getComputedStyle(tile) : null;
      const amt = tile
        ? [...tile.querySelectorAll("p, span")].find((e) => e !== assetsLabel && /\$/.test(e.textContent || ""))
        : null;
      // The ratio value (the border-t footer's right-hand span).
      const ratioLabel = [...card.querySelectorAll("span, p, div")].find(
        (e) => /Asset to Liability Ratio/.test(e.textContent || "") && e.children.length === 0,
      );
      const ratioVal = ratioLabel
        ? [...(ratioLabel.parentElement?.children || [])].find((e) => e !== ratioLabel)
        : null;
      // The tablist.
      const list = document.querySelector('[role="tablist"]') as HTMLElement | null;
      const lcs = list ? getComputedStyle(list) : null;
      const lr = list ? list.getBoundingClientRect() : null;
      const active = list
        ? ([...list.querySelectorAll('button[role="tab"]')].find(
            (t) => t.getAttribute("aria-selected") === "true",
          ) as HTMLElement | null)
        : null;
      const acs = active ? getComputedStyle(active) : null;
      // The type-group header + the card grid (the v46 F2 controls).
      const groupH = [...document.querySelectorAll("h3")].find(
        (e) => e.getBoundingClientRect().height > 0,
      );
      const ghs = groupH ? getComputedStyle(groupH) : null;
      const cardGrid = groupH ? groupH.nextElementSibling : null;
      const cgcs = cardGrid ? getComputedStyle(cardGrid) : null;
      const c0 = cardGrid ? (cardGrid.children[0] as HTMLElement) : null;
      const c0cs = c0 ? getComputedStyle(c0) : null;
      return {
        card: {
          x: Math.round(cr.x), w: Math.round(cr.width), pad: cs.padding,
          radius: cs.borderRadius, bg: (cs.backgroundImage || "").replace(/\s+/g, " ").slice(0, 110),
          shadow: (cs.boxShadow || "").replace(/\s+/g, " ").slice(0, 80),
        },
        figure: h2cs ? { fs: h2cs.fontSize, fw: h2cs.fontWeight, color: h2cs.color } : null,
        label: { fs: getComputedStyle(label).fontSize, color: getComputedStyle(label).color },
        medallion: chip
          ? {
              w: Math.round(chip.getBoundingClientRect().width),
              h: Math.round(chip.getBoundingClientRect().height),
              bg: getComputedStyle(chip).backgroundColor,
              iconW: Math.round(chip.querySelector("svg")!.getBoundingClientRect().width),
            }
          : null,
        statGrid: gcs ? { template: gcs.gridTemplateColumns, gap: gcs.gap } : null,
        statTile: tcs
          ? {
              w: Math.round(tile!.getBoundingClientRect().width), pad: tcs.padding,
              radius: tcs.borderRadius, bg: tcs.backgroundColor, blur: tcs.backdropFilter,
              amtFs: amt ? getComputedStyle(amt).fontSize : null,
              amtFw: amt ? getComputedStyle(amt).fontWeight : null,
            }
          : null,
        ratio: ratioVal
          ? { text: (ratioVal.textContent || "").trim(), fs: getComputedStyle(ratioVal).fontSize, fw: getComputedStyle(ratioVal).fontWeight }
          : null,
        tablist: lcs && lr
          ? {
              w: Math.round(lr.width), h: Math.round(lr.height),
              template: lcs.gridTemplateColumns, maxW: lcs.maxWidth, pad: lcs.padding,
              trigH: active ? Math.round(active.getBoundingClientRect().height) : null,
              trigPad: acs ? acs.padding : null, trigFs: acs ? acs.fontSize : null,
              trigFw: acs ? acs.fontWeight : null, trigColor: acs ? acs.color : null,
            }
          : null,
        groupHeader: ghs
          ? {
              fs: ghs.fontSize, fw: ghs.fontWeight, color: ghs.color,
              mb: ghs.marginBottom, tt: ghs.textTransform,
            }
          : null,
        grid: cgcs && cardGrid
          ? {
              w: Math.round(cardGrid.getBoundingClientRect().width),
              cols: cgcs.gridTemplateColumns, gap: cgcs.gap,
            }
          : null,
        card0: c0cs && c0
          ? { w: Math.round(c0.getBoundingClientRect().width), pad: c0cs.padding, radius: c0cs.borderRadius }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("networth 1280 census found no card");

    // The summary card — the 960 column (1280 − the 256 rail − the 64 p-8),
    // 32px pad, 16px radius, the 135deg forest→lime gradient, the 26-58-46
    // shadow (byte-identical to the reference's live census).
    expect(census.card.x).toBe(288);
    expect(census.card.w).toBe(960);
    expect(census.card.pad).toBe("32px");
    expect(census.card.radius).toBe("16px");
    expect(census.card.bg).toBe("linear-gradient(135deg, rgb(45, 90, 74) 0%, rgb(143, 188, 63) 100%)");
    expect(census.card.shadow).toContain("rgba(26, 58, 46, 0.3) 0px 20px 60px");

    // The figure + the label (the sm:text-5xl tier: 48px from 640 up).
    expect(census.figure).toEqual({ fs: "48px", fw: "700", color: "rgb(255, 255, 255)" });
    expect(census.label).toEqual({ fs: "14px", color: "rgba(255, 255, 255, 0.8)" });

    // The medallion — 64×64, white/20%, the 32px icon.
    expect(census.medallion).toEqual({ w: 64, h: 64, bg: "rgba(255, 255, 255, 0.2)", iconW: 32 });

    // The stat grid + the tile — the 440×440 tracks inside the 896 content
    // box, 16px gap; the tile 16px pad / 12px radius / white-10% / blur.
    expect(census.statGrid).toEqual({ template: "440px 440px", gap: "16px" });
    expect(census.statTile).toEqual({
      w: 440, pad: "16px", radius: "12px",
      bg: "rgba(255, 255, 255, 0.1)", blur: "blur(10px)",
      amtFs: "24px", amtFw: "700",
    });

    // The ratio footer's value — the seed's 0.21:1 at 18px/700 (the
    // reference's own ∞:1 is the formatRatio data class, not chrome).
    expect(census.ratio).toEqual({ text: "0.21:1", fs: "18px", fw: "700" });

    // The tablist — max-w-md capped at 448 (the v50 F2 values at the pair
    // viewport; the reference's own list byte-identical).
    expect(census.tablist).toEqual({
      w: 448, h: 36, template: "220px 220px", maxW: "448px", pad: "4px",
      trigH: 28, trigPad: "4px 12px", trigFs: "14px", trigFw: "500",
      trigColor: "rgb(20, 83, 45)",
    });

    // The type-group header — 18px/600/forest-medium/capitalize/mb 12.
    expect(census.groupHeader).toEqual({
      fs: "18px", fw: "600", color: "rgb(45, 90, 74)", mb: "12px", tt: "capitalize",
    });

    // The controls — the v46 F2 grid/card values re-asserted at 1280.
    expect(census.grid).toEqual({ w: 960, cols: "309.328px 309.328px 309.328px", gap: "16px" });
    expect(census.card0).toEqual({ w: 309, pad: "20px", radius: "12px" });

    // No overflow at the pair viewport.
    expect(census.docSW).toBe(1280);
  });
});

test.describe("net worth summary card HEIGHT census at 1280 (v67 — plan F3)", () => {
  // The v67 re-run pair's pin: the summary card's computed HEIGHT family at
  // the 1280x800 pair viewport — the arbitration census (arbit-v67.sh +
  // arbit-v67b.sh) measured the family byte-identical on BOTH sites, a
  // family never pinned before v67: the v60 F1 pin covers the card's
  // width/pad/radius/gradient/shadow + the figure/label/medallion/tile
  // FONTS + the grid template/gap + the ratio value's text axes; the v63
  // F3 pin the stat-tile heights at 390 — NEVER the 1280 heights. The
  // arithmetic is deterministic: the card h 333 = 32 (pad-top) + 76 (the
  // head row: the label h 20 + mb 8 + the figure h 48) + 32 (the head
  // row's mb-8) + 84 (the one-row stat grid: the tile h 84 = pad 16 +
  // the label h 16 + mb 4 + the amount h 32 + pad 16) + 24 (the footer's
  // mt-6) + 24 (the footer's pt-6) + 1 (the border-top) + 28 (the ratio
  // row — text-lg's 28px line-height) + 32 (pad-bottom).
  test("the summary card's height family — the card h 333, the head row 76, the figure h 48, the grid rows 84, the tile h 84, the footer h 53 (v67 F3)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const census = await page.evaluate(() => {
      const label = [...document.querySelectorAll("p, span, h2, div")].find(
        (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0,
      );
      if (!label) return null;
      const card = label.closest("div.rounded-2xl") as HTMLElement | null;
      if (!card) return null;
      const cr = card.getBoundingClientRect();
      const cs = getComputedStyle(card);
      // The head row: the label block's parent — the flex justify-between
      // holding the label+figure block beside the medallion.
      const headRow = (label.closest("div") as HTMLElement | null)?.parentElement ?? null;
      const hrs = headRow ? getComputedStyle(headRow) : null;
      const hrr = headRow ? headRow.getBoundingClientRect() : null;
      // The label + the figure.
      const lcs = getComputedStyle(label);
      const lr = label.getBoundingClientRect();
      const h2 = [...card.querySelectorAll("h1, h2, h3, p")].find(
        (e) => /-?\$[\d,]+\.\d{2}/.test((e.textContent || "").trim()) && e !== label,
      );
      const h2cs = h2 ? getComputedStyle(h2) : null;
      const h2r = h2 ? h2.getBoundingClientRect() : null;
      // The medallion (the round icon chip).
      const chip = [...card.querySelectorAll("div")].find((d) => {
        const r = d.getBoundingClientRect();
        const c = getComputedStyle(d);
        return r.width > 40 && r.width < 90 && c.borderRadius === "9999px" && d.querySelector("svg");
      });
      const svg = chip ? chip.querySelector("svg") : null;
      // The stat grid + the first tile (Total Assets).
      const assetsLabel = [...card.querySelectorAll("p, span")].find(
        (e) => (e.textContent || "").trim() === "Total Assets",
      );
      const grid = assetsLabel ? assetsLabel.closest("[class*=grid]") : null;
      const gcs = grid ? getComputedStyle(grid) : null;
      const gr = grid ? grid.getBoundingClientRect() : null;
      const tile = assetsLabel ? assetsLabel.closest("[class*=rounded]") : null;
      const tr = tile ? tile.getBoundingClientRect() : null;
      const alr = assetsLabel ? assetsLabel.getBoundingClientRect() : null;
      const alcs = assetsLabel ? getComputedStyle(assetsLabel) : null;
      const amt = tile
        ? [...tile.querySelectorAll("p, span")].find((e) => e !== assetsLabel && /\$/.test(e.textContent || ""))
        : null;
      const ar = amt ? amt.getBoundingClientRect() : null;
      // The ratio footer: walk UP from the ratio leaf to the border-t block.
      const ratioLabel = [...card.querySelectorAll("span, p, div")].find(
        (e) => /Asset to Liability Ratio/.test(e.textContent || "") && e.children.length === 0,
      );
      let footer: HTMLElement | null = null;
      if (ratioLabel) {
        let node: HTMLElement | null = ratioLabel as HTMLElement;
        while (node && node !== card) {
          const s = getComputedStyle(node);
          if (parseInt(s.borderTopWidth || "0") > 0) { footer = node; break; }
          node = node.parentElement;
        }
      }
      const fcs = footer ? getComputedStyle(footer) : null;
      const fr = footer ? footer.getBoundingClientRect() : null;
      return {
        card: { w: Math.round(cr.width), h: Math.round(cr.height), pad: cs.padding, radius: cs.borderRadius },
        headRow: hrs && hrr ? { h: Math.round(hrr.height), mb: hrs.marginBottom, display: hrs.display } : null,
        label: { mb: lcs.marginBottom, h: Math.round(lr.height) },
        figure: h2cs && h2r ? { lh: h2cs.lineHeight, h: Math.round(h2r.height) } : null,
        medallion: chip
          ? {
              h: Math.round(chip.getBoundingClientRect().height),
              iconH: svg ? Math.round(svg.getBoundingClientRect().height) : null,
            }
          : null,
        statGrid: gcs && gr ? { rows: gcs.gridTemplateRows, h: Math.round(gr.height) } : null,
        statTile: tr && alr && alcs && ar
          ? {
              h: Math.round(tr.height),
              labelH: Math.round(alr.height), labelMb: alcs.marginBottom,
              amtH: Math.round(ar.height),
            }
          : null,
        ratioFooter: fcs && fr
          ? {
              mt: fcs.marginTop, pt: fcs.paddingTop, borderTopW: fcs.borderTopWidth,
              h: Math.round(fr.height),
            }
          : null,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("networth height census found no card");

    // The card — the w/pad/radius controls (the v60 F1 axes) + the height
    // axis: the deterministic 333 (32 + 76 + 32 + 84 + 24 + 24 + 1 + 28 + 32).
    expect(census.card).toEqual({ w: 960, h: 333, pad: "32px", radius: "16px" });

    // The head row — h 76 (the label 20 + mb 8 + the figure 48 govern; the
    // 64px medallion rides), the 32px mb-8 rhythm below it.
    expect(census.headRow).toEqual({ h: 76, mb: "32px", display: "flex" });

    // The label — mb 8px (mb-2), h 20 (text-sm's 20px line box).
    expect(census.label).toEqual({ mb: "8px", h: 20 });

    // The figure — lineHeight 48px, one line, h 48 (sm:text-5xl's lh-1).
    expect(census.figure).toEqual({ lh: "48px", h: 48 });

    // The medallion — 64 tall, the 32px icon (the v63 F3 axes at 1280).
    expect(census.medallion).toEqual({ h: 64, iconH: 32 });

    // The stat grid — ONE 84px row at 1280 (the 390 twin's two-row 184 is
    // the v63 F3 class), the grid h 84.
    expect(census.statGrid).toEqual({ rows: "84px", h: 84 });

    // The stat tile — h 84 (pad 16 + the label 16 + mb 4 + the amount 32 +
    // pad 16); the label mb 4px (mb-1), the amount h 32 (text-2xl's 32px
    // line box).
    expect(census.statTile).toEqual({ h: 84, labelH: 16, labelMb: "4px", amtH: 32 });

    // The ratio footer — mt-6/pt-6 (24/24), the 1px border-top, h 53
    // (the pt 24 + the border 1 + the ratio row 28 — text-lg's 28px lh).
    expect(census.ratioFooter).toEqual({ mt: "24px", pt: "24px", borderTopW: "1px", h: 53 });
  });
});

test.describe("net worth page-header row census at 390 (v69 — plan F3)", () => {
  // The v69 re-run pair's pin: the /networth view's PAGE-HEADER ROW computed
  // census at 390x844 — the never-census'd family (the v14 G3 chip test
  // pins the chip/h1 x-positions only; the v65 F3 savings page-header-row
  // pin's sibling for the networth surface, at the v69 re-run pair's
  // viewport). Measured live on the clone (nw-header-v69.sh): the row
  // flex/center/gap-3 (12px) with the mb-8 (32px) section rhythm (the v41
  // F1 rhythm, re-measured); the chip 48x48 rounded-xl (12px) with the
  // forest-medium→lime 135deg gradient wrapping the 24x24 white
  // TrendingUp; the h1 30px/700/lh 36px/forestDark; the subtitle 16px/400/
  // gray-500 lh 24px — ONE line at the 250px block (the subtitle's
  // max-content governs the block width); the block h 60 = the h1 36 + the
  // subtitle 24 — the TEXT BLOCK governs the row height, not the 48px chip
  // (the v65 lesson); the row→card gap 32; the page FITS 390 (the superset
  // — the reference's own page overflows to 464, its R-bug-4).
  test("the header row — the row flex/gap-3/mb-8, the chip 48x48 gradient, the h1 30px/700, the subtitle 16px one-line, the block-governed h 60, the row→card gap 32 (v69 F3)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const census = await page.evaluate(() => {
      const h1 = [...document.querySelectorAll("main h1")].find(
        (h) => (h.textContent || "").trim() === "Net Worth",
      );
      if (!h1) return null;
      const block = h1.parentElement as HTMLElement | null;
      const row = block?.parentElement as HTMLElement | null;
      if (!block || !row) return null;
      const rcs = getComputedStyle(row);
      const chip = [...row.children].find((c) => c !== block) as HTMLElement | null;
      const chipCs = chip ? getComputedStyle(chip) : null;
      const chipIcon = chip?.querySelector("svg") ?? null;
      const h1cs = getComputedStyle(h1);
      const sub = [...block.children].find((c) => c.tagName === "P") as HTMLElement | null;
      const subCs = sub ? getComputedStyle(sub) : null;
      const next = row.nextElementSibling;
      return {
        docSW: document.documentElement.scrollWidth,
        row: {
          display: rcs.display,
          align: rcs.alignItems,
          gap: rcs.gap,
          mb: rcs.marginBottom,
          w: Math.round(row.getBoundingClientRect().width),
          h: Math.round(row.getBoundingClientRect().height),
        },
        chip: chip
          ? {
              w: Math.round(chip.getBoundingClientRect().width),
              h: Math.round(chip.getBoundingClientRect().height),
              radius: chipCs!.borderRadius,
              bg: chipCs!.backgroundImage,
            }
          : null,
        chipIcon: chipIcon
          ? {
              w: Math.round(chipIcon.getBoundingClientRect().width),
              h: Math.round(chipIcon.getBoundingClientRect().height),
              color: getComputedStyle(chipIcon).color,
            }
          : null,
        h1: {
          fs: h1cs.fontSize,
          fw: h1cs.fontWeight,
          lh: h1cs.lineHeight,
          color: h1cs.color,
          h: Math.round(h1.getBoundingClientRect().height),
          x: Math.round(h1.getBoundingClientRect().x),
        },
        block: {
          w: Math.round(block.getBoundingClientRect().width),
          h: Math.round(block.getBoundingClientRect().height),
        },
        subtitle: sub
          ? {
              fs: subCs!.fontSize,
              fw: subCs!.fontWeight,
              color: subCs!.color,
              lh: subCs!.lineHeight,
              h: Math.round(sub.getBoundingClientRect().height),
            }
          : null,
        rowToCardGap: next
          ? Math.round(next.getBoundingClientRect().top - row.getBoundingClientRect().bottom)
          : null,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("networth header census found no row");

    // The row — flex/center/gap-3 (12px), the mb-8 (32px) section rhythm,
    // w 358 (the 390 column − 2×16 p-4), h 60 — the TEXT BLOCK governs
    // (the v65 lesson), not the 48px chip.
    expect(census.row).toEqual({
      display: "flex", align: "center", gap: "12px",
      mb: "32px", w: 358, h: 60,
    });

    // The chip — 48×48, rounded-xl (12px), the forest-medium→lime 135deg
    // gradient (the networth HEADER_CHIP_GRADIENTS entry).
    expect(census.chip).toEqual({
      w: 48, h: 48, radius: "12px",
      bg: "linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))",
    });

    // The chip icon — the 24×24 white TrendingUp (h-6 w-6).
    expect(census.chipIcon).toEqual({ w: 24, h: 24, color: "rgb(255, 255, 255)" });

    // The h1 — 30px/700, lh 36px, forestDark rgb(26, 58, 46), h 36, x 76
    // (the chip 48 at x 16 + the gap 12 — the v14 axes re-asserted).
    expect(census.h1).toEqual({
      fs: "30px", fw: "700", lh: "36px",
      color: "rgb(26, 58, 46)", h: 36, x: 76,
    });

    // The block — w 250 (the subtitle's max-content governs; the h1 fills
    // it block-level), h 60 (the h1 36 + the subtitle 24, no gap utility).
    expect(census.block).toEqual({ w: 250, h: 60 });

    // The subtitle — 16px/400, gray-500 rgb(107, 114, 128), lh 24px,
    // ONE line at the 250px block (h 24).
    expect(census.subtitle).toEqual({
      fs: "16px", fw: "400", color: "rgb(107, 114, 128)",
      lh: "24px", h: 24,
    });

    // The row→card gap — 32 (the v41 F1 rhythm re-measured live).
    expect(census.rowToCardGap).toBe(32);

    // No overflow (the superset — the reference's own page overflows to
    // 464 at 390, its R-bug-4; the clone's page fits).
    expect(census.docSW).toBe(390);
  });
});

test.describe("net worth summary card completion census at 1280 (v82 — plan F4)", () => {
  // The v82 re-run pair's pin: the summary card's never-pinned COMPLETION
  // family at the 1280x800 pair viewport — the arbitration census
  // (arbit-v82.sh PART B) measured the axes byte-identical on BOTH sites:
  // the head row's ALIGNMENT (items center — the v80 titleRow.alignItems
  // pattern's networth twin; the v67 F3 pin holds the row's h 76/mb 32px/
  // display flex but never its items axis), the label block's HEIGHT (76 —
  // the min-w-0 wrapper's own height, the label 20 + mb 8 + the figure 48
  // stack; the v67 pin holds the PARENT row's 76, never the block's own),
  // the stat grid's content-box WIDTH (896 — the 960 card − the 2×32 pad
  // arithmetic twin; the v60 F1 pin holds the template/gap, the v67 pin
  // the rows/h), and the ratio label's TYPOGRAPHY (fs 14px — text-sm; the
  // G9 test holds the label's COLOR, the v4-era structure test the VALUE's
  // 18px/700 + the tile label's 12px + the footer border's rgba — never
  // the ratio label's own font-size). Every pinned axis STATIC chrome —
  // none depends on the figures (the labelBlock's WIDTH is the
  // data-conditional axis — the 48px figure's text length — and is
  // EXCLUDED); the pin rides the plain authenticated view.
  test("the summary card's head-row alignment + label-block height + stat-grid width + ratio-label typography (v82 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const census = await page.evaluate(() => {
      const label = [...document.querySelectorAll("p, span, h2, div")].find(
        (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0,
      );
      if (!label) return null;
      const card = label.closest("div.rounded-2xl") as HTMLElement | null;
      if (!card) return null;
      // The head row: the label block's parent — the flex justify-between.
      const headRow = (label.closest("div") as HTMLElement | null)?.parentElement ?? null;
      const hrs = headRow ? getComputedStyle(headRow) : null;
      // The label block (the min-w-0 wrapper around the label + figure).
      const labelBlock = label.parentElement;
      const lbr = labelBlock ? labelBlock.getBoundingClientRect() : null;
      // The stat grid (the 2-col tile grid) + its bounding width.
      const assetsLabel = [...card.querySelectorAll("p, span")].find(
        (e) => (e.textContent || "").trim() === "Total Assets",
      );
      const grid = assetsLabel ? assetsLabel.closest("[class*=grid]") : null;
      const gr = grid ? grid.getBoundingClientRect() : null;
      // The ratio label (the text-sm leaf in the border-t footer row).
      const ratioLabel = [...card.querySelectorAll("span, p, div")].find(
        (e) => /Asset to Liability Ratio/.test(e.textContent || "") && e.children.length === 0,
      );
      return {
        headRow: hrs ? { items: hrs.alignItems } : null,
        labelBlock: lbr ? { h: Math.round(lbr.height) } : null,
        statGrid: gr ? { w: Math.round(gr.width) } : null,
        ratioLabel: ratioLabel ? { fs: getComputedStyle(ratioLabel).fontSize } : null,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("networth completion census found no card");

    // The head row's ALIGNMENT — items center (the medallion rides the
    // row's 76px height, vertically centered against the label block).
    expect(census.headRow).toEqual({ items: "center" });

    // The label block — h 76 (the label 20 + mb 8 + the figure 48 stack;
    // the v67 pin holds the parent row's h — this is the block's own).
    expect(census.labelBlock).toEqual({ h: 76 });

    // The stat grid — the 896 content-box width (the 960 card − the 2×32
    // pad; the 440px 440px tracks + the 16px gap live inside it).
    expect(census.statGrid).toEqual({ w: 896 });

    // The ratio label — text-sm's 14px (the label's own font-size; the
    // value beside it is the v60-pinned 18px/700).
    expect(census.ratioLabel).toEqual({ fs: "14px" });
  });
});

test.describe("net worth ratio-footer census at 390 (v84 — plan F4)", () => {
  // The v84 re-run pair's pin: the summary card's RATIO-FOOTER family at
  // the 390x844 mobile viewport — the divider-arbitration census
  // (ratio-divider-arbit-v84.sh) measured the axes byte-identical on BOTH
  // sites after the VLM's "divider missing in the clone" flag (a misread):
  // the footer row's border-t family (1px solid rgba(255,255,255,0.2) —
  // the INLINE style, unconditional across viewports), the mt-6/pt-6
  // rhythm (24/24), the footer h 53 (the pt 24 + the border 1 + the
  // value-governed 28px ratio row — text-lg's line box governs over any
  // label line box), and the ratio LABEL's typography + box (text-sm's
  // 14px/400 + the 156x20 line box of the static label text).
  //
  // The coverage map (why every axis is never-pinned at 390): the v67 F3
  // pin holds the footer's {mt, pt, borderTopW, h} at 1280 ONLY; the
  // v4-era structure test the border style/color + the VALUE's 18px/700
  // at 1280; the v82 pin the label's fs at 1280; the v41 F3 + v63 F3
  // pins stop at the card box/figure/gridCols/tiles/medallion/card h.
  // Every pinned axis STATIC chrome — the label text is static, the
  // value a single-line 28px line box regardless of the ratio string
  // ("0.21:1" and "∞:1" alike); the pin rides the plain authenticated
  // view at 390x844.
  test("the summary card's ratio-footer divider + label census at 390 (v84 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const census = await page.evaluate(() => {
      const label = [...document.querySelectorAll("p, span, h2, div")].find(
        (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0,
      );
      if (!label) return null;
      const card = label.closest("div.rounded-2xl") as HTMLElement | null;
      if (!card) return null;
      // The ratio label (the text-sm leaf in the border-t footer row).
      const ratioLabel = [...card.querySelectorAll("span, p, div")].find(
        (e) => /Asset to Liability Ratio/.test(e.textContent || "") && e.children.length === 0,
      );
      if (!ratioLabel) return null;
      // The footer: walk UP from the label leaf to the border-t block.
      let footer: HTMLElement | null = ratioLabel as HTMLElement;
      while (footer && footer !== card) {
        const s = getComputedStyle(footer);
        if (parseInt(s.borderTopWidth || "0") > 0) break;
        footer = footer.parentElement;
      }
      if (!footer || footer === card) return null;
      const fcs = getComputedStyle(footer);
      const fr = footer.getBoundingClientRect();
      const lr = ratioLabel.getBoundingClientRect();
      const lcs = getComputedStyle(ratioLabel);
      return {
        ratioFooter: {
          mt: fcs.marginTop,
          pt: fcs.paddingTop,
          borderTopW: fcs.borderTopWidth,
          borderTopS: fcs.borderTopStyle,
          borderTopC: fcs.borderTopColor,
          h: Math.round(fr.height),
        },
        ratioLabel: {
          fs: lcs.fontSize,
          fw: lcs.fontWeight,
          w: Math.round(lr.width),
          h: Math.round(lr.height),
        },
        sw: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("networth ratio-footer census found no footer");

    // The footer's border-t family — the divider the v84 VLM flag claimed
    // missing: 1px solid rgba(255,255,255,0.2), byte-identical on both
    // sites (the inline style, never a Tailwind v4 oklab computed form).
    expect(census.ratioFooter).toEqual({
      mt: "24px",
      pt: "24px",
      borderTopW: "1px",
      borderTopS: "solid",
      borderTopC: "rgba(255, 255, 255, 0.2)",
      h: 53,
    });

    // The ratio label — text-sm's 14px/400 + the 156x20 line box (the
    // static label text; the value beside it is the 1280-pinned 18px/700).
    expect(census.ratioLabel).toEqual({ fs: "14px", fw: "400", w: 156, h: 20 });

    // The page fits the mobile viewport (the v41 superset contract).
    expect(census.sw).toBeLessThanOrEqual(391);
  });
});

// ---------------------------------------------------------------------------
// v90 — plan F4: the stat-tile INTERIOR census at 390 (the mobile-twins
// re-run pair's pin — the pair's FOURTH re-run [v62/v63 → v69 → v78 →
// v84 → v90]). The v41 F3 pin holds the card box/figure/chip/gridCols;
// the v63 F3 pin the stat-tile BOX family {w/h/bg/blur/radius/pad} + the
// grid + the card h 421 + the medallion svg; the v84 F4 pin the
// ratio-footer family. The NEVER-pinned axes here (the
// tile-interior-arbit-v90.sh census's own measurements, byte-identical on
// BOTH sides at 390x844): the two tiles' LABEL family (the mb-1 text-xs P
// with the inline color — fs 12px / rgba(255,255,255,0.7) / mb 4px / the
// 16px glyph box) + the two tiles' VALUE family (the text-2xl font-bold
// text-white P — fs 24px / fw 700 / white). The tile WIDTH is the v41
// mobile-superset class (the reference's overflowing 2-col 176s vs the
// clone's fitting 1-col 294s) — the INTERIOR typography is the contract.
// The finder is the v63 F3 finder verbatim.
// ---------------------------------------------------------------------------
test.describe("stat-tile interior census at 390 (v90 — plan F4)", () => {
  test("the summary card's stat-tile interiors — both tiles' label + value families", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const census = await page.evaluate(() => {
      const label = [...document.querySelectorAll("p, span, h2, div")].find(
        (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0,
      );
      if (!label) return null;
      const card = label.closest("div.rounded-2xl") as HTMLElement | null;
      if (!card) return null;
      const assetsLabel = [...card.querySelectorAll("p, span")].find(
        (e) => (e.textContent || "").trim() === "Total Assets",
      );
      const grid = assetsLabel ? (assetsLabel.closest('[class*="grid"]') as HTMLElement | null) : null;
      if (!grid) return null;
      const gcs = getComputedStyle(grid);
      const tiles = [...grid.children].map((c): {
        box: { w: number; h: number };
        label: { tag: string; fs: string; color: string; mb: string; h: number };
        value: { tag: string; fs: string; fw: string; color: string };
      } | null => {
        const tile = c as HTMLElement;
        const tr = tile.getBoundingClientRect();
        const ps = [...tile.querySelectorAll("p")] as HTMLElement[];
        const [l, v] = ps;
        if (!l || !v) return null;
        const lcs = getComputedStyle(l);
        const vcs = getComputedStyle(v);
        const lr = l.getBoundingClientRect();
        return {
          box: { w: Math.round(tr.width), h: Math.round(tr.height) },
          label: { tag: l.tagName, fs: lcs.fontSize, color: lcs.color, mb: lcs.marginBottom, h: Math.round(lr.height) },
          value: { tag: v.tagName, fs: vcs.fontSize, fw: vcs.fontWeight, color: vcs.color },
        };
      });
      if (tiles.some((t) => t === null)) return null;
      return {
        gridCols: gcs.gridTemplateColumns,
        tiles: tiles as NonNullable<(typeof tiles)[number]>[],
        sw: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("stat-tile interior census found no tiles");

    // The grid + the tile boxes — the v63 F3 contract re-affirmed (the
    // 1-col 294px track, the 84px tile height arithmetic).
    expect(census.gridCols).toBe("294px");
    expect(census.tiles).toHaveLength(2);
    for (const t of census.tiles) {
      expect(t.box).toEqual({ w: 294, h: 84 });
    }

    // The LABEL family — the mb-1 text-xs P with the inline 0.7 white:
    // 12px / rgba(255,255,255,0.7) / mb 4px / the 16px glyph box, on BOTH
    // tiles, byte-identical to the reference's own tile labels.
    for (const t of census.tiles) {
      expect(t.label).toEqual({
        tag: "P", fs: "12px", color: "rgba(255, 255, 255, 0.7)", mb: "4px", h: 16,
      });
    }

    // The VALUE family — the text-2xl font-bold text-white P: 24px / 700 /
    // white, on BOTH tiles, byte-identical to the reference's own.
    for (const t of census.tiles) {
      expect(t.value).toEqual({ tag: "P", fs: "24px", fw: "700", color: "rgb(255, 255, 255)" });
    }

    // The page fits the mobile viewport (the v41 superset contract).
    expect(census.sw).toBeLessThanOrEqual(391);
  });
});

// ---------------------------------------------------------------------------
// v94 — plan F4 (docs/remediation-plan-v94.md): the networth view's
// SECTION-HEADER row census at 1280.
//
// The v94 arbitration (nwsection-arbit-v94.sh + nwsection-clone-v94.sh, the
// v88-era pair's fifth re-run) measured a never-pinned family: the tab
// panel's "Assets" header row — the row's flex chrome, the h2's typography,
// the count subtitle P, the Add Asset button's chrome on this row, and the
// row→group rhythm. The v60 F1 pin holds the summary card + the tablist +
// the type-group header + the card grid at 1280 (never the section row);
// the v69 F3 pin the PAGE-header row at 390 (a different row); the v46 F2
// pin the asset CARD family at 1280; the tokens.spec G2/G3 pins the Add
// buttons' 16px Plus + the bare-shadow ambient at the DEFAULT viewport;
// grep-verified: NO spec asserts the "Assets" section h2's computed styles
// at ANY viewport. The block's WIDTH and the countText are EXCLUDED (the
// countText length's data-coupled width class — the v82 labelBlock
// convention); the group wrapper's margin-TOP form is EXCLUDED (the v3/v4
// space-y margin-attribution computed class — the rendered gap delta 24 is
// the parity contract, byte-identical on both sides).
//
// Every pinned axis STATIC chrome (the row's flex classes, the h2's
// text-2xl font-bold + inline forestDark, the countP's bare P + inline
// gray, the button's zb-btn-add family, the space-y-6 rhythm — all
// unconditional); the pin rides the plain authenticated /networth view on
// the e2e seed (the Assets tab is the DEFAULT panel) — read-only, no
// fixture writes, no tab interactions.
// ---------------------------------------------------------------------------
interface NwSectionCensus {
  row: { display: string; align: string; justify: string; h: number; w: number };
  h2: { fs: string; fw: string; lh: string; color: string; mb: string; h: number };
  countP: { fs: string; fw: string; lh: string; color: string } | null;
  block: { h: number };
  addBtn: {
    h: number; w: number; pad: string; radius: string; fs: string; fw: string; color: string;
    bg: string; icon: { w: number; h: number } | null;
  } | null;
  groupGap: { delta: number } | null;
  groupH3: { fs: string; fw: string; lh: string; mb: string } | null;
  docSW: number;
}
test.describe("networth section-header row census at 1280 (v94 — plan F4)", () => {
  test("the section row's flex chrome + the h2 typography + the count P + the Add Asset chrome + the row-to-group rhythm (v94 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
    // The settle pattern: the count subtitle renders with the panel.
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate((): NwSectionCensus | null => {
      const h2 = [...document.querySelectorAll("main h2")].find(
        (h) => (h.textContent || "").trim() === "Assets",
      );
      if (!h2) return null;
      const block = h2.parentElement as HTMLElement | null;
      const row = block ? (block.parentElement as HTMLElement | null) : null;
      if (!block || !row) return null;
      const rcs = getComputedStyle(row);
      const rr = row.getBoundingClientRect();
      const h2cs = getComputedStyle(h2);
      const h2r = h2.getBoundingClientRect();
      const countP = [...block.children].find(
        (c) => c.tagName === "P",
      ) as HTMLElement | undefined;
      const pcs = countP ? getComputedStyle(countP) : null;
      const br = block.getBoundingClientRect();
      const addBtn = [...row.querySelectorAll("button")].find((b) =>
        /Add Asset/i.test(b.textContent || ""),
      ) as HTMLElement | undefined;
      const btn = addBtn
        ? (() => {
            const s = getComputedStyle(addBtn!);
            const r = addBtn!.getBoundingClientRect();
            const icon = addBtn!.querySelector("svg");
            return {
              h: Math.round(r.height),
              w: Math.round(r.width),
              pad: s.padding,
              radius: s.borderRadius,
              fs: s.fontSize,
              fw: s.fontWeight,
              color: s.color,
              bg: (s.backgroundImage || "").replace(/\s+/g, " ").slice(0, 90),
              icon: icon
                ? {
                    w: Math.round(icon.getBoundingClientRect().width),
                    h: Math.round(icon.getBoundingClientRect().height),
                  }
                : null,
            };
          })()
        : null;
      const group = row.nextElementSibling as HTMLElement | null;
      const g3 = group ? (group.querySelector("h3") as HTMLElement | null) : null;
      const g3cs = g3 ? getComputedStyle(g3) : null;
      return {
        docSW: document.documentElement.scrollWidth,
        row: {
          display: rcs.display,
          align: rcs.alignItems,
          justify: rcs.justifyContent,
          h: Math.round(rr.height),
          w: Math.round(rr.width),
        },
        h2: {
          fs: h2cs.fontSize,
          fw: h2cs.fontWeight,
          lh: h2cs.lineHeight,
          color: h2cs.color,
          mb: h2cs.marginBottom,
          h: Math.round(h2r.height),
        },
        countP: pcs
          ? { fs: pcs.fontSize, fw: pcs.fontWeight, lh: pcs.lineHeight, color: pcs.color }
          : null,
        block: { h: Math.round(br.height) },
        addBtn: btn,
        groupGap: group
          ? { delta: Math.round(group.getBoundingClientRect().top - rr.bottom) }
          : null,
        groupH3: g3cs
          ? { fs: g3cs.fontSize, fw: g3cs.fontWeight, lh: g3cs.lineHeight, mb: g3cs.marginBottom }
          : null,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("section-header census found no row");

    // The section header row — flex/center/space-between, h 56, the full
    // 960 content column (byte-identical to the reference's own row).
    expect(census.row).toEqual({
      display: "flex",
      align: "center",
      justify: "space-between",
      h: 56,
      w: 960,
    });

    // The h2 "Assets" — text-2xl font-bold + the inline forestDark:
    // 24px/700/lh 32px, the preflight mb 0, h 32.
    expect(census.h2).toEqual({
      fs: "24px",
      fw: "700",
      lh: "32px",
      color: "rgb(26, 58, 46)",
      mb: "0px",
      h: 32,
    });

    // The count subtitle P — the bare P + the inline gray: 16px/400/lh 24px.
    expect(census.countP).toEqual({
      fs: "16px",
      fw: "400",
      lh: "24px",
      color: "rgb(107, 114, 128)",
    });

    // The left block's height — the h2 lh 32 + the countP lh 24 arithmetic
    // (the block's WIDTH excluded: the countText length's data-coupled
    // class, the v82 labelBlock convention).
    expect(census.block).toEqual({ h: 56 });

    // The Add Asset button — the zb-btn-add family on this row: 36×134,
    // 8px 16px pad, 6px radius, 14px/500 white, the forest→lime gradient,
    // the 16px Plus icon.
    expect(census.addBtn).toEqual({
      h: 36,
      w: 134,
      pad: "8px 16px",
      radius: "6px",
      fs: "14px",
      fw: "500",
      color: "rgb(255, 255, 255)",
      bg: "linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))",
      icon: { w: 16, h: 16 },
    });

    // The row → first-group rhythm — the space-y-6 rendered gap (the
    // margin-TOP form excluded: the v3/v4 margin-attribution computed
    // class; the rendered delta byte-identical on both sides).
    expect(census.groupGap).toEqual({ delta: 24 });

    // The first type-group header re-affirmed in the row's rhythm context —
    // 18px/600/lh 28px/mb 12 (the v60 F1 family, the position-adjacent
    // member).
    expect(census.groupH3).toEqual({ fs: "18px", fw: "600", lh: "28px", mb: "12px" });

    // The page fits the pair viewport.
    expect(census.docSW).toBe(1280);
  });
});

// ---------------------------------------------------------------------------
// v96 (docs/remediation-plan-v96.md) — the MOBILE 390 twins' fifth re-run
// pair (the /networth + the dashboard FULL-PAGE at 390x844, last re-shot
// v90). The FAMILY-EXTENSION pin (the v93 label-first lesson): the
// summary card's HEAD-ROW text chrome at 390 — the figure's fw + color
// are pinned at 640 (v41 F2: 48px/700) and 1280 (v60 F1: the full
// family) but NEVER at 390 (the v41 F3 pin holds figureFont fs only);
// the label's family is pinned at 1280 only; the figure's FIT contract
// (the v96 figclip arbitration's own axes — the NEW clipped-figure VLM
// flag disproven by the Range-walk textRect vs the padding-aware
// content box) is never pinned at ANY viewport. The pin's own axes
// first measured byte-identical on BOTH sides by the supplemental
// two-half census (headrow-arbit-v96.sh + headrow-clone-v96.sh, the
// census JS md5 519ef222): the label {14px/400/rgba(255,255,255,0.8)/
// mb 8/h 20} + the figure fw 700/white + the flush-left start
// (textLeftOverhang 0) + figureScrolls false — all byte-identical
// across sides; the card w + the figure fs + the text metrics are the
// documented v41/seed-data classes (the pin asserts the clone's own
// deterministic values).
// ---------------------------------------------------------------------------
test.describe("summary card head-row typography + figure-fit census at 390 (v96 — plan F4)", () => {
  test("the figure's fw/color family at 390 + the label family + the in-bounds fit contract (the v96 figclip arbitration)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
    await expect(page.getByText("-$245,950.00")).toBeVisible();

    const census = await page.evaluate(() => {
      // The supplemental census's own finder (the NW_CENSUS gradient-card
      // finder + the label leaf + the largest-$-font figure walk).
      const cards = [...document.querySelectorAll("main div, div")].filter((d) => {
        const s = getComputedStyle(d);
        return d.getBoundingClientRect().height > 100 && d.getBoundingClientRect().width > 200
          && s.backgroundImage && s.backgroundImage.includes("linear-gradient");
      });
      const card = cards.find((c) => c.getBoundingClientRect().width < 500) || cards[0];
      if (!card) return null;
      const cr = card.getBoundingClientRect();
      const cs = getComputedStyle(card);
      const label = [...card.querySelectorAll("p, span")].find(
        (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0,
      );
      let fig: HTMLElement | null = null;
      let figFs = 0;
      for (const el of card.querySelectorAll("h1,h2,h3,p,span,div")) {
        const s = getComputedStyle(el);
        const fs = parseFloat(s.fontSize);
        const t = (el.textContent || "").trim();
        if (!t || t.length > 40) continue;
        if (/^[-]?\s*[$]/.test(t) && fs > figFs) { fig = el as HTMLElement; figFs = fs; }
      }
      if (!fig || !label) return null;
      const fr = fig.getBoundingClientRect();
      const fcs = getComputedStyle(fig);
      const lcs = getComputedStyle(label);
      const range = document.createRange();
      range.selectNodeContents(fig);
      const tr = range.getBoundingClientRect();
      const padL = parseFloat(cs.paddingLeft);
      const padR = parseFloat(cs.paddingRight);
      const contentL = cr.left + padL;
      const contentR = cr.right - padR;
      return {
        card: { w: Math.round(cr.width), padL, padR },
        label: { fs: lcs.fontSize, fw: lcs.fontWeight, color: lcs.color, mb: lcs.marginBottom, h: Math.round(label.getBoundingClientRect().height) },
        figure: {
          text: (fig.textContent || "").trim(),
          fs: fcs.fontSize, fw: fcs.fontWeight, color: fcs.color, lh: fcs.lineHeight,
          el: { x: Math.round(fr.x), h: Math.round(fr.height) },
          textRect: { x: Math.round(tr.x), w: Math.round(tr.width) },
        },
        fit: {
          textLeftOverhang: Math.round(contentL - tr.x),
          textRightMargin: Math.round(contentR - tr.right),
          figureScrolls: fig.scrollWidth > fig.clientWidth,
          docSW: document.documentElement.scrollWidth,
        },
      };
    });
    expect(census, "the head-row census finder (the gradient card + the label leaf + the figure walk)").not.toBeNull();
    if (!census) throw new Error("head-row census found no card");

    // The figure's typography family at 390 — the fw/color NEVER pinned at
    // this tier before (the 640/1280 tiers hold them; the v41 F3 pin holds
    // the fs only). 24px/700/white at lh 32 (the text-2xl responsive tier —
    // the superset fix #6 family).
    expect(census.figure.text).toBe("-$245,950.00");
    expect(census.figure.fs).toBe("24px");
    expect(census.figure.fw).toBe("700");
    expect(census.figure.color).toBe("rgb(255, 255, 255)");
    expect(census.figure.lh).toBe("32px");
    expect(census.figure.el.x).toBe(48);
    expect(census.figure.el.h).toBe(32);
    expect(census.figure.textRect.x).toBe(48);

    // The label's family at 390 — pinned at 1280 only before (the v60-era
    // tier); the text-sm family is viewport-independent.
    expect(census.label).toEqual({
      fs: "14px", fw: "400", color: "rgba(255, 255, 255, 0.8)", mb: "8px", h: 20,
    });

    // The FIT contract — the v96 figclip arbitration's own axes (the NEW
    // clipped-figure VLM flag disproven): the text starts flush at the
    // content-left (zero overhang) and ends INSIDE the content-right; the
    // figure never scrolls; the page never overflows.
    expect(census.fit.textLeftOverhang).toBe(0);
    expect(census.fit.textRightMargin).toBeGreaterThanOrEqual(0);
    expect(census.fit.figureScrolls).toBe(false);
    expect(census.fit.docSW).toBe(390);

    // The card box re-affirm (the v41 arithmetic: 358 = 390 − 2×16, the
    // 32px pad) — the content-box anchors the fit contract.
    expect(census.card.w).toBe(358);
    expect(census.card.padL).toBe(32);
    expect(census.card.padR).toBe(32);
  });
});

// ---------------------------------------------------------------------------
// v100 (docs/remediation-plan-v100.md) — the re-run pair's SIXTH cycle (the
// v94-era NETWORTH + DRILL-DOWN pair). The FAMILY-EXTENSION pin (the v94
// missing-middle lesson applied to the INTER-BLOCK RHYTHM): the TABLIST→
// SECTION-ROW junction — the TabsContent's mt-6 gap. The v41 F2 pin (640)
// walks the UPPER rhythm only (headerToCard 32 + cardToTablist 32 — the two
// mb-8 gaps above the tablist); the v60 F1 pin (1280) walks the summary
// card + tablist interiors (no rhythm axes); the v94 F4 pin walks the
// section row's own chrome + the row-to-group rhythm (the space-y-6 INSIDE
// the TabsContent) — the JUNCTION between them was NEVER pinned at ANY
// viewport in ANY spec (zero specs assert any TabsContent margin; the only
// mt-6 assertions in the suite are the summary card's ratio footer — a
// different element). The pin's own axes first measured byte-identical on
// BOTH sides by the supplemental two-half census (nwjunction-arbit-v100.sh +
// nwjunction-clone-v100.sh via build-nwjunction-v100.py, the census JS md5
// 5f124436): tablist {448/36/bottom 525/220px 220px/448px/4px} + sectionRow
// {top 549/56/960/flex/space-between} + junction {gap 24} + the continuation
// families — every axis DATA-INDEPENDENT (the structural chrome; the v98
// data-independent-panel strength class: the cross-side-verified values
// assert directly).
// ---------------------------------------------------------------------------
test.describe("networth tablist→section-row junction census at 1280 (v100 — plan F4)", () => {
  test("the junction's gap + the anchor geometry — the TabsContent's mt-6 family, never pinned before (v100 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
    // The settle pattern: the section row renders with the panel.
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate(() => {
      // THE TABLIST (the Assets/Liabilities trigger row — the v60 finder).
      const tablist = document.querySelector('[role="tablist"]');
      if (!tablist) return null;
      const tl = tablist.getBoundingClientRect();
      const tcs = getComputedStyle(tablist);
      // THE SECTION ROW (the v94 finder: the Assets h2 → block → row).
      const h2 = [...document.querySelectorAll("main h2")].find(
        (h) => (h.textContent || "").trim() === "Assets",
      );
      if (!h2) return null;
      const block = h2.parentElement as HTMLElement | null;
      const row = block ? (block.parentElement as HTMLElement | null) : null;
      if (!block || !row) return null;
      const rr = row.getBoundingClientRect();
      const rcs = getComputedStyle(row);
      // The first type-group continuation (the v94 families re-measured).
      const group = row.nextElementSibling as HTMLElement | null;
      const g3 = group ? (group.querySelector("h3") as HTMLElement | null) : null;
      const g3cs = g3 ? getComputedStyle(g3) : null;
      return {
        tablist: {
          w: Math.round(tl.width),
          h: Math.round(tl.height),
          bottom: Math.round(tl.bottom),
          template: tcs.gridTemplateColumns,
          maxW: tcs.maxWidth,
          pad: tcs.padding,
        },
        sectionRow: {
          top: Math.round(rr.top),
          h: Math.round(rr.height),
          w: Math.round(rr.width),
          display: rcs.display,
          justify: rcs.justifyContent,
        },
        // THE JUNCTION: the tablist's bottom → the section row's top (the
        // TabsContent's mt-6 — the never-pinned axis).
        junction: { gap: Math.round(rr.top - tl.bottom) },
        groupH3: g3cs
          ? { fs: g3cs.fontSize, fw: g3cs.fontWeight, mb: g3cs.marginBottom }
          : null,
        rowToGroup: group
          ? { gap: Math.round(group.getBoundingClientRect().top - rr.bottom) }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("junction census found no tablist/row");

    // The tablist anchor — the v60 F1 family re-anchored in the junction
    // context (byte-identical on both sites, the nwjunction census).
    expect(census.tablist).toEqual({
      w: 448,
      h: 36,
      bottom: 525,
      template: "220px 220px",
      maxW: "448px",
      pad: "4px",
    });

    // The section-row anchor — the v94 F4 family re-anchored.
    expect(census.sectionRow).toEqual({
      top: 549,
      h: 56,
      w: 960,
      display: "flex",
      justify: "space-between",
    });

    // THE JUNCTION — the never-pinned axis: the TabsContent's mt-6 gap
    // (the tablist bottom 525 → the section row top 549).
    expect(census.junction).toEqual({ gap: 24 });

    // The continuation families re-measured in the junction context (the
    // v94 F4 values — the rhythm map now junction-complete).
    expect(census.groupH3).toEqual({ fs: "18px", fw: "600", mb: "12px" });
    expect(census.rowToGroup).toEqual({ gap: 24 });

    // The page fits the pair viewport.
    expect(census.docSW).toBe(1280);
  });
});

// ---------------------------------------------------------------------------
// v102 (docs/remediation-plan-v102.md) — the re-run pair's SIXTH cycle (the
// v96-era MOBILE 390 twins pair). The FAMILY-EXTENSION pin (the v100
// junction-walk lesson applied to the MOBILE viewport + the SECOND panel's
// own junction): the MOBILE junctions at 390 — the card→tablist gap (the
// summary card's mb-8) + the tablist→section gap (the ASSETS TabsContent's
// mt-6) + the LIABILITIES panel's OWN junction (its own mt-6 — never pinned
// at ANY viewport in ANY spec). The v69 F3 pin (390) walks the header
// row→card gap only; the v41 F2 pin (640) the UPPER rhythm at 640; the v53
// F1 pin (390) the tablist's own chrome; the v94 F4 pin (1280) the section
// row + the row-to-group rhythm; the v100 F4 pin (1280) the ASSETS junction
// — the MOBILE junctions and the SECOND panel's junction were NEVER pinned
// (the coverage-map grep: zero junction assertions at 390; zero
// liabilities-panel junction assertions at any viewport). The pin's own
// axes first measured byte-identical on BOTH sides by the supplemental
// two-half census (mobjunction-arbit-v102.sh + mobjunction-clone-v102.sh
// via build-mobjunction-v102.py, the census JS md5 83a04c0e): the gaps
// {32, 24, 24} + the tablist {h 36, pad 4px} + the rows {h 56, flex,
// space-between} — every axis DATA-INDEPENDENT (the structural margins and
// chrome; the v98 data-independent-panel strength class). The reference-side
// pointerdown lesson: the reference's Radix-style trigger ignores a bare
// DOM click — the Playwright locator click (the full pointer family
// natively) is the load-bearing form.
// ---------------------------------------------------------------------------
test.describe("networth mobile junctions census at 390 (v102 — plan F4)", () => {
  test("the card→tablist gap + the assets tablist→section gap + the LIABILITIES panel's own junction — never pinned before (v102 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
    // The settle pattern: the tablist + the Assets section render with the panel.
    await expect(page.getByRole("tab", { name: /Assets/i })).toBeVisible();
    await page.waitForTimeout(400);

    // ---- The ASSETS-side junction walk (the gradient card → tablist →
    // the Assets h2 → block → row — the NW_CENSUS/v94/v100 finders). ----
    const census = await page.evaluate(() => {
      const cards = [...document.querySelectorAll("main div, div")].filter(
        (d) => {
          const s = getComputedStyle(d);
          return (
            d.getBoundingClientRect().height > 100 &&
            d.getBoundingClientRect().width > 200 &&
            s.backgroundImage &&
            s.backgroundImage.includes("linear-gradient")
          );
        },
      );
      const card = cards.find(
        (c) => c.getBoundingClientRect().width < 500,
      ) as HTMLElement | undefined;
      const tablist = document.querySelector('[role="tablist"]');
      const h2 = [...document.querySelectorAll("main h2")].find(
        (h) => (h.textContent || "").trim() === "Assets",
      );
      if (!card || !tablist || !h2) return null;
      const block = h2.parentElement as HTMLElement | null;
      const row = block ? (block.parentElement as HTMLElement | null) : null;
      if (!block || !row) return null;
      const cr = card.getBoundingClientRect();
      const tl = tablist.getBoundingClientRect();
      const tcs = getComputedStyle(tablist);
      const rr = row.getBoundingClientRect();
      return {
        card: { w: Math.round(cr.width), bottom: Math.round(cr.bottom) },
        tablist: {
          w: Math.round(tl.width),
          h: Math.round(tl.height),
          bottom: Math.round(tl.bottom),
          template: tcs.gridTemplateColumns,
          pad: tcs.padding,
        },
        // THE JUNCTION 1: the summary card bottom → tablist top (the
        // card's mb-8 — never pinned at 390 before this pin).
        cardToTablist: { gap: Math.round(tl.top - cr.bottom) },
        sectionRow: {
          top: Math.round(rr.top),
          h: Math.round(rr.height),
          display: getComputedStyle(row).display,
          justify: getComputedStyle(row).justifyContent,
        },
        // THE JUNCTION 2: the tablist bottom → the ASSETS section row top
        // (the assets TabsContent's mt-6 — pinned at 1280 only before).
        tablistToSection: { gap: Math.round(rr.top - tl.bottom) },
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("mobile junction census found no card/tablist/row");

    // The card + tablist anchors — the in-bounds mobile column (the
    // reference's own card/tablist are 432 wide inside its 464-overflow
    // page, its documented bug; every non-width axis byte-identical).
    expect(census.card.w).toBe(358);
    expect(census.tablist).toEqual({
      w: 358,
      h: 36,
      bottom: 658,
      template: "175px 175px",
      pad: "4px",
    });

    // THE JUNCTION 1 — the never-pinned axis at this viewport: the
    // summary card's mb-8 (32px) between the card's bottom and the
    // tablist's top.
    expect(census.cardToTablist).toEqual({ gap: 32 });

    // THE JUNCTION 2 — the assets TabsContent's mt-6 (24px), re-anchored
    // at the mobile viewport (the v100 pin holds it at 1280).
    expect(census.tablistToSection).toEqual({ gap: 24 });
    expect(census.sectionRow.h).toBe(56);
    expect(census.sectionRow.display).toBe("flex");
    expect(census.sectionRow.justify).toBe("space-between");

    // ---- THE LIABILITIES PASS: switch to the SECOND panel (the Playwright
    // locator click — the full pointer-event family natively; the
    // reference-side pointerdown lesson) and measure ITS OWN junction. ----
    await page.getByRole("tab", { name: /Liabilities/i }).click();
    await expect(
      page.getByRole("heading", { name: "Liabilities", exact: true }),
    ).toBeVisible();
    await page.waitForTimeout(400);

    const liab = await page.evaluate(() => {
      const tablist = document.querySelector('[role="tablist"]');
      const h2b = [...document.querySelectorAll("main h2")].find(
        (h) => (h.textContent || "").trim() === "Liabilities",
      );
      if (!tablist || !h2b) return null;
      const blockB = h2b.parentElement as HTMLElement | null;
      const rowB = blockB
        ? (blockB.parentElement as HTMLElement | null)
        : null;
      if (!blockB || !rowB) return null;
      const tl = tablist.getBoundingClientRect();
      const rrb = rowB.getBoundingClientRect();
      const rcsb = getComputedStyle(rowB);
      return {
        tablistBottom: Math.round(tl.bottom),
        row: {
          top: Math.round(rrb.top),
          h: Math.round(rrb.height),
          w: Math.round(rrb.width),
          display: rcsb.display,
          justify: rcsb.justifyContent,
        },
        // THE JUNCTION 3: the tablist bottom → the LIABILITIES section row
        // top (the LIABILITIES TabsContent's OWN mt-6 — the never-pinned
        // axis at ANY viewport before this pin).
        liabJunction: { gap: Math.round(rrb.top - tl.bottom) },
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(liab).not.toBeNull();
    if (!liab) throw new Error("liabilities junction census found no tablist/row");

    // THE JUNCTION 3 — the never-pinned axis: the LIABILITIES
    // TabsContent's own mt-6 (24px — byte-identical to the reference's
    // measured 24 per the mobjunction two-half census).
    expect(liab.liabJunction).toEqual({ gap: 24 });

    // The liabilities section row — the v94 family at the mobile viewport
    // (the in-bounds column: the reference's own row is 432 wide inside
    // its 464-overflow page — its documented bug).
    expect(liab.row).toEqual({
      top: 682,
      h: 56,
      w: 358,
      display: "flex",
      justify: "space-between",
    });

    // The tablist anchor unchanged by the panel swap.
    expect(liab.tablistBottom).toBe(658);

    // The page fits the mobile viewport (the superset invariant — the
    // reference reads 464, its own documented overflow bug).
    expect(liab.docSW).toBe(390);
  });
});

test.describe("networth asset-card facts-row interior census at 1280 (v106 — plan F4)", () => {
  test("the facts wrapper + both rows' flex chrome + the 12×12 icon family + the space-y-2 rhythm (the never-pinned family)", async ({ page }) => {
    // The v106 F4 pin (remediation-plan-v106.md): the v46 F2 pin holds the
    // facts WRAPPER's {font, color} + the value→facts mb-4 gap; the rows'
    // OWN interiors — the per-row flex chrome, the 12×12 icon family, the
    // row heights, and the space-y-2 vertical rhythm — were never pinned
    // at ANY viewport in ANY spec. Measured byte-identical on BOTH sides
    // by the one-shot census (nw-facts-arbit-v106.sh: the reference's own
    // "Savings Account" card vs the clone's "Share Portfolio" — every
    // axis data-independent; the texts each site's own seed).
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();
    // The settle pattern: wait for the first seeded card before probing.
    const firstCard = page.locator("div.rounded-xl").filter({ hasText: "Share Portfolio" }).first();
    await expect(firstCard).toBeVisible();

    const census = await page.evaluate(() => {
      // The first asset card: rounded-xl + an h4 + a 24px/700 value (the
      // v46 census's own finder family — NOT the summary card).
      const cards = [...document.querySelectorAll("div")].filter((d) => {
        if (typeof d.className !== "string") return false;
        if (!d.className.includes("rounded-xl")) return false;
        const h4 = d.querySelector("h4");
        const val = [...d.querySelectorAll("p")].find((p) => {
          const pcs = getComputedStyle(p);
          return pcs.fontSize === "24px" && pcs.fontWeight === "700";
        });
        return !!h4 && !!val;
      });
      if (!cards.length) return null;
      const card = cards[0] as HTMLElement;
      // The Updated ROW: text starts with "Updated" + a 12px svg sibling.
      const updated = [...card.querySelectorAll("div")].find((e) => {
        const t = (e.textContent || "").trim();
        return t.startsWith("Updated") && e.querySelector("svg") && getComputedStyle(e).fontSize === "12px";
      });
      if (!updated) return null;
      const wrapper = updated.parentElement;
      if (!wrapper) return null;
      const wcs = getComputedStyle(wrapper);
      const rows = [...wrapper.children].filter((c) => c.tagName === "DIV") as HTMLElement[];
      const rowCensus = rows.map((row) => {
        const rcs = getComputedStyle(row);
        const svg = row.querySelector("svg");
        const sr = svg ? svg.getBoundingClientRect() : null;
        const scs = svg ? getComputedStyle(svg) : null;
        return {
          display: rcs.display,
          align: rcs.alignItems,
          gap: rcs.gap,
          h: Math.round(row.getBoundingClientRect().height),
          mt: rcs.marginBlockStart,
          iconW: sr ? Math.round(sr.width) : null,
          iconH: sr ? Math.round(sr.height) : null,
          iconColor: scs ? scs.color : null,
          iconViewBox: svg ? svg.getAttribute("viewBox") : null,
        };
      });
      return {
        wrapper: {
          display: wcs.display,
          fs: wcs.fontSize,
          color: wcs.color,
          h: Math.round(wrapper.getBoundingClientRect().height),
          rowCount: rows.length,
        },
        rows: rowCensus,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("facts census found no card");

    // The wrapper — the v46 pin's own family extended to the geometry
    // (block layout, the 40 = 16 + 8 + 16 arithmetic of two rows + the
    // 8px rhythm).
    expect(census.wrapper).toEqual({
      display: "block",
      fs: "12px",
      color: "rgb(107, 114, 128)",
      h: 40,
      rowCount: 2,
    });

    // The institution row — flex/center/8px, h 16, mt 0, the 12×12
    // Building2 icon inheriting the wrapper's gray via currentColor.
    expect(census.rows[0]).toEqual({
      display: "flex",
      align: "center",
      gap: "8px",
      h: 16,
      mt: "0px",
      iconW: 12,
      iconH: 12,
      iconColor: "rgb(107, 114, 128)",
      iconViewBox: "0 0 24 24",
    });

    // The Updated row — the same chrome PLUS the 8px rhythm (the v3
    // space-y-2 margin-top semantics restored by globals.css — the
    // trap-log family holding on a networth surface).
    expect(census.rows[1]).toEqual({
      display: "flex",
      align: "center",
      gap: "8px",
      h: 16,
      mt: "8px",
      iconW: 12,
      iconH: 12,
      iconColor: "rgb(107, 114, 128)",
      iconViewBox: "0 0 24 24",
    });
  });
});
// ---------------------------------------------------------------------------
// v118 — plan F4 (docs/remediation-plan-v118.md): the /networth PAGE-HEADER
// ROW census at 1280 (the pair viewport). The never-pinned family (the
// coverage map: the v60 view census jumps straight to the summary card's
// label; the v67/v82 pins the card interior; the v94 the GROUP headers;
// the v100 the tablist junction; the v106 the asset cards — the PAGE
// header row pinned ONLY at 390 before this [the v69 F3 pin, measured on
// the CLONE alone]; the v14 G3 test holds the chip's existence + gradient
// colors + geometry + the h1 x-positions). Measured byte-identical on BOTH
// sides by the v118 one-shot census (nwheader-arbit-v118.sh) — with ONE
// mechanism axis diverging: the row's margin-bottom (the reference 0px —
// it wraps the row in a single-child responsive wrapper [flex flex-col
// md:flex-row justify-between items-start md:items-center gap-4 mb-8]
// that carries the mb-8; the clone puts the mb-8 directly on the row —
// the CONSTRUCT class per the v7 accepted-construct convention: the
// wrapper paints nothing, organizes only [childCount 1 — nothing on the
// right], the pixel arithmetic identical [row 32→92, card 124, gap 32]).
// The pin holds the clone's own rhythm (mb 32px) — the visual contract,
// not the wrapper mechanism.
// ---------------------------------------------------------------------------
test.describe("networth page-header row census at 1280 (v118 — plan F4)", () => {
  test("the row flex/gap-3 + the chip 48x48 gradient + the h1 30px/700 + the subtitle 16px + the block-governed h 60 + the row→card gap 32 (the never-pinned 1280 family)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const census = await page.evaluate(() => {
      // The h1 by its text; the block + row via the parent chain; the chip
      // as the row's svg-carrying child — STRUCTURAL finders (the v72
      // class: the class strings never trusted).
      const h1 = [...document.querySelectorAll("main h1")].find(
        (h) => (h.textContent || "").trim() === "Net Worth",
      );
      if (!h1) return null;
      const block = h1.parentElement as HTMLElement | null;
      const row = block?.parentElement as HTMLElement | null;
      if (!block || !row) return null;
      const rcs = getComputedStyle(row);
      const chip = [...row.children].find(
        (c) => c !== block && (c as HTMLElement).querySelector("svg"),
      ) as HTMLElement | null;
      const chipCs = chip ? getComputedStyle(chip) : null;
      const chipR = chip ? chip.getBoundingClientRect() : null;
      const svg = chip?.querySelector("svg") || null;
      const svgR = svg ? svg.getBoundingClientRect() : null;
      const hcs = getComputedStyle(h1);
      const sub = [...block.children].find((c) => c !== h1) as HTMLElement | null;
      const scs = sub ? getComputedStyle(sub) : null;
      const subR = sub ? sub.getBoundingClientRect() : null;
      // The summary card via its label (the v60 finder) for the gap + the
      // width context.
      const label = [...document.querySelectorAll("p, span, h2, div")].find(
        (e) => (e.textContent || "").trim() === "Total Net Worth" && e.children.length === 0,
      );
      let cardGap: number | string = "card not found";
      let cardW: number | string = "card not found";
      if (label) {
        let card = label as HTMLElement | null;
        while (card && card !== document.body) {
          const c = getComputedStyle(card);
          if (parseFloat(c.borderRadius) > 12 && card.getBoundingClientRect().width > 500) break;
          card = card.parentElement;
        }
        if (card && card !== document.body) {
          const cr = card.getBoundingClientRect();
          cardGap = Math.round(cr.top - row.getBoundingClientRect().bottom);
          cardW = Math.round(cr.width);
        }
      }
      return {
        row: {
          display: rcs.display,
          alignItems: rcs.alignItems,
          gap: rcs.gap,
          mb: rcs.marginBottom,
          h: Math.round(row.getBoundingClientRect().height),
        },
        chip: chipCs
          ? {
              w: Math.round(chipR!.width),
              h: Math.round(chipR!.height),
              radius: chipCs.borderRadius,
              bgImage: chipCs.backgroundImage,
              svgW: svgR ? Math.round(svgR.width) : null,
              svgH: svgR ? Math.round(svgR.height) : null,
            }
          : null,
        h1: {
          fs: hcs.fontSize,
          fw: hcs.fontWeight,
          lh: hcs.lineHeight,
          color: hcs.color,
          h: Math.round(h1.getBoundingClientRect().height),
        },
        subtitle: scs
          ? {
              fs: scs.fontSize,
              fw: scs.fontWeight,
              lh: scs.lineHeight,
              color: scs.color,
              h: Math.round(subR!.height),
            }
          : null,
        block: {
          h: Math.round(block.getBoundingClientRect().height),
          w: Math.round(block.getBoundingClientRect().width),
        },
        cardGap,
        cardW,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("page-header census found no header row");

    // The row — the clone's own rhythm (the reference's mb-8 lives on its
    // single-child wrapper: the v118 construct class).
    expect(census.row).toEqual({
      display: "flex",
      alignItems: "center",
      gap: "12px",
      mb: "32px",
      h: 60,
    });
    // The chip — the v14 G3 gradient re-held with the geometry.
    expect(census.chip).toEqual({
      w: 48,
      h: 48,
      radius: "12px",
      bgImage: "linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))",
      svgW: 24,
      svgH: 24,
    });
    // The h1 + subtitle typography.
    expect(census.h1).toEqual({
      fs: "30px",
      fw: "700",
      lh: "36px",
      color: "rgb(26, 58, 46)",
      h: 36,
    });
    expect(census.subtitle).toEqual({
      fs: "16px",
      fw: "400",
      lh: "24px",
      color: "rgb(107, 114, 128)",
      h: 24,
    });
    // The TEXT BLOCK governs the row height, not the 48px chip (the
    // v65/v69 lesson).
    expect(census.block).toEqual({ h: 60, w: 250 });
    // The row→card gap + the card width context (the v60 family).
    expect(census.cardGap).toBe(32);
    expect(census.cardW).toBe(960);
    expect(census.docSW).toBe(1280);
  });
});


// ---------------------------------------------------------------------------
// v120 — plan F4 (docs/remediation-plan-v120.md): the /networth LIABILITY
// CARD census at 390 (the mobile twin #1's own surface). The never-pinned
// family (the coverage map: the liability card's box + interior NEVER
// pinned in ANY spec at ANY viewport — only the badge's family-consistency
// pin [v29 G1] + the interest-line TEXT existence + the group headers +
// the Add Liability gradient; the ASSET twin fully pinned [v46 at 1280 +
// v47 at 390 + v106 facts-row at 1280]). The FAMILY-CONSISTENCY form (the
// v29 G1 precedent): the reference's own liability data is EMPTY (0
// liabilities — no cards to measure; the v46 READ-ONLY rule forbids
// writing reference data), and the liability card's chrome family is the
// AssetCard's pinned contract BY CONSTRUCTION (net-worth-view.tsx:169 the
// identical class strings to :65 the asset twin; the v46 F1 liability-twin
// fix's own comment documents the shared mb-4 P + space-y-2 facts stack).
// Measured live by liabcard-arbit-v120.sh on the clone at 390 (the
// LIABILITIES tab, the seeded Home Loan card): the card h 218 = the
// asset's pinned 194 + the third facts row's 16 + the space-y-2's 8 — the
// arithmetic exact. The liability-ONLY axes: the 3-row facts stack
// (institution + interest + updated vs the asset's 2 rows) with the
// interest row, the orange dot/value (the LIABILITY_COLOR family).
// ---------------------------------------------------------------------------
test.describe("networth liability-card census at 390 (v120 — plan F4)", () => {
  test("the liability card's full family — the card box, the head row, the dot, the h4, the badge, the orange value P, the 3-row facts stack with the interest row (the never-pinned family — the asset card's v47 contract + the liability-only interior)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    // The LIABILITIES tab — Playwright's locator click dispatches the full
    // pointer sequence (the Radix tabs activate on pointerdown; the bare
    // el.click() leaves the tab inactive — the liabcard-arbit-v120.sh
    // lesson, baked into the census script's own tab switch).
    const liabilitiesTab = page.getByRole("tab", { name: "Liabilities" });
    await liabilitiesTab.click();
    await expect(liabilitiesTab).toHaveAttribute("data-state", "active");

    // The settle: the first seeded liability card renders before probing.
    const card0 = page.locator("div.rounded-xl").filter({ hasText: "Home Loan" }).first();
    await expect(card0).toBeVisible();

    const census = await page.evaluate(() => {
      // The liability card — STRUCTURAL finders (the v72 class: the class
      // strings never trusted for the WALK, only for the card's own
      // identity — the same finder family as the v29-era visibility
      // assertion and the v46/v47 asset censuses).
      const card = [...document.querySelectorAll("main div")].find((d) => {
        if (typeof d.className !== "string") return false;
        return (
          d.className.includes("group rounded-xl border bg-white p-5") &&
          /Home Loan/.test(d.textContent || "")
        );
      }) as HTMLElement | null;
      if (!card) return null;
      const cr = card.getBoundingClientRect();
      const cs = getComputedStyle(card);
      // The head row: the card's first child div (mb-3 flex items-start
      // justify-between — the shared asset-twin structure).
      const head = card.querySelector("div") as HTMLElement | null;
      const hs = head ? getComputedStyle(head) : null;
      const hr = head ? head.getBoundingClientRect() : null;
      // The dot: the h-2 w-2 rounded-[9999px] type dot (the orange).
      const dot = [...card.querySelectorAll("div")].find((d) =>
        (d.className || "").toString().includes("h-2 w-2"),
      ) as HTMLElement | null;
      const dotS = dot ? getComputedStyle(dot) : null;
      const dotR = dot ? dot.getBoundingClientRect() : null;
      // The h4 name; the badge by its zb-badge-hover class + the type text.
      const h4 = card.querySelector("h4");
      const h4S = h4 ? getComputedStyle(h4) : null;
      const badge = [...card.querySelectorAll("span")].find(
        (s) =>
          /home loan/i.test((s.textContent || "").trim()) &&
          (s.className || "").toString().includes("zb-badge-hover"),
      );
      const bS = badge ? getComputedStyle(badge) : null;
      const bR = badge ? badge.getBoundingClientRect() : null;
      // The value P: the money-figure paragraph (the orange).
      const valP = [...card.querySelectorAll("p")].find((p) =>
        /^[-]?[\$]?[0-9]/.test((p.textContent || "").trim()),
      );
      const vS = valP ? getComputedStyle(valP) : null;
      const vR = valP ? valP.getBoundingClientRect() : null;
      // The facts stack: the space-y-2 text-xs child (the shared twin).
      const facts = [...card.children].find((c) =>
        (c.className || "").toString().includes("space-y-2"),
      ) as HTMLElement | null;
      const fS = facts ? getComputedStyle(facts) : null;
      const rowRects = facts ? [...facts.children].map((r) => r.getBoundingClientRect()) : [];
      const rowGap =
        rowRects.length >= 2 ? Math.round(rowRects[1].top - rowRects[0].bottom) : null;
      const rows = facts
        ? [...facts.children].map((r) => {
            const s = getComputedStyle(r);
            const rr = r.getBoundingClientRect();
            const icon = r.querySelector("svg");
            const ir = icon ? icon.getBoundingClientRect() : null;
            return {
              txt: (r.textContent || "").trim().slice(0, 22),
              display: s.display,
              align: s.alignItems,
              gap: s.gap,
              h: Math.round(rr.height),
              icon: ir ? { w: Math.round(ir.width), h: Math.round(ir.height) } : null,
            };
          })
        : [];
      return {
        docSW: document.documentElement.scrollWidth,
        card: {
          w: Math.round(cr.width),
          h: Math.round(cr.height),
          radius: cs.borderRadius,
          pad: cs.padding,
          border: cs.border,
          shadow: cs.boxShadow,
          bg: cs.backgroundColor,
          transition: cs.transitionProperty + " " + cs.transitionDuration,
        },
        headRow: hr
          ? {
              mb: hs ? hs.marginBottom : null,
              display: hs ? hs.display : null,
              align: hs ? hs.alignItems : null,
              justify: hs ? hs.justifyContent : null,
              h: Math.round(hr.height),
            }
          : null,
        dot: dotS && dotR
          ? {
              w: Math.round(dotR.width),
              h: Math.round(dotR.height),
              radius: dotS.borderRadius,
              bg: dotS.backgroundColor,
            }
          : null,
        h4: h4S ? { fs: h4S.fontSize, fw: h4S.fontWeight, color: h4S.color } : null,
        badge: bS && bR
          ? {
              h: Math.round(bR.height),
              fs: bS.fontSize,
              fw: bS.fontWeight,
              bg: bS.backgroundColor,
              color: bS.color,
              pad: bS.padding,
              radius: bS.borderRadius,
            }
          : null,
        valueP: vS && vR
          ? {
              fs: vS.fontSize,
              fw: vS.fontWeight,
              color: vS.color,
              mb: vS.marginBottom,
              h: Math.round(vR.height),
            }
          : null,
        facts: fS
          ? { fs: fS.fontSize, color: fS.color, rowGap: rowGap, rowCount: rows.length }
          : null,
        rows: rows,
        valueToFactsGap:
          valP && facts
            ? Math.round(facts.getBoundingClientRect().top - valP.getBoundingClientRect().bottom)
            : null,
      };
    });

    expect(census).not.toBeNull();
    // The superset invariant holds on the liabilities panel too.
    expect(census!.docSW).toBe(390);
    // The card box — every axis the v47 asset-card contract (the h 218 =
    // the asset's 194 + the third row's 16 + the space-y-2's 8).
    expect(census!.card).toEqual({
      w: 358,
      h: 218,
      radius: "12px",
      pad: "20px",
      border: "1px solid rgb(229, 231, 227)",
      shadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px 0px",
      bg: "rgb(255, 255, 255)",
      transition: "all 0.2s",
    });
    // The head row (the shared asset-twin structure).
    expect(census!.headRow).toEqual({
      mb: "12px",
      display: "flex",
      align: "flex-start",
      justify: "space-between",
      h: 52,
    });
    // The dot — the LIABILITY_COLOR orange, the 8x8 round type dot.
    expect(census!.dot).toEqual({
      w: 8,
      h: 8,
      radius: "9999px",
      bg: "rgb(224, 122, 59)",
    });
    // The h4 name.
    expect(census!.h4).toEqual({ fs: "16px", fw: "600", color: "rgb(26, 58, 46)" });
    // The badge — the v29 G1 family-consistency contract, in the census form.
    expect(census!.badge).toEqual({
      h: 22,
      fs: "12px",
      fw: "600",
      bg: "rgb(243, 244, 246)",
      color: "rgb(55, 65, 81)",
      pad: "2px 10px",
      radius: "6px",
    });
    // The value P — the orange figure, the v46 F1 liability-twin mb-4.
    expect(census!.valueP).toEqual({
      fs: "24px",
      fw: "700",
      color: "rgb(224, 122, 59)",
      mb: "16px",
      h: 32,
    });
    // The facts stack — 12px gray, the space-y-2 8px rhythm, THREE rows
    // (the liability-only axis: institution + interest + updated).
    expect(census!.facts).toEqual({
      fs: "12px",
      color: "rgb(107, 114, 128)",
      rowGap: 8,
      rowCount: 3,
    });
    // The Updated row's date text — the SEED-DAY axis, COMPUTED (the v122
    // repair of the v120 pin's time-bomb: the original literal "Oct 25,
    // 2026" was green only on its own seed day and reds every day after —
    // prisma/seed.ts stamps lastUpdated: isoDate(0) [TODAY] and the card
    // renders it via formatDate's toLocaleDateString; this spec runs in the
    // same process/TZ class as the seed, so the same rule reproduces the
    // rendered string. The midnight-crossing window [seed 23:59, assert
    // 00:01] is accepted per the same-day-seed law.)
    const seedDay = new Date().toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric",
    });
    // The three rows — the shared row chrome family.
    expect(census!.rows).toEqual([
      {
        txt: "NAB",
        display: "flex",
        align: "center",
        gap: "8px",
        h: 16,
        icon: { w: 12, h: 12 },
      },
      {
        txt: "5.75% interest",
        display: "flex",
        align: "center",
        gap: "8px",
        h: 16,
        icon: { w: 12, h: 12 },
      },
      {
        txt: `Updated ${seedDay}`,
        display: "flex",
        align: "center",
        gap: "8px",
        h: 16,
        icon: { w: 12, h: 12 },
      },
    ]);
    // The value→facts gap — the v46 F1 liability-twin's mb-4 rendered.
    expect(census!.valueToFactsGap).toBe(16);
  });
});
test.describe("networth kebab-trigger OPEN-MENU reveal census at 1280 (v124 — plan F4)", () => {
  test("the trigger's open+parked reveal — the data-[state=open] path holds opacity 1 with the pointer off the card (the reveal family's open path on the never-pinned networth file)", async ({ page }) => {
    // The v124 F4 pin: the kebab reveal family's OPEN path on the NETWORTH
    // twins (net-worth-view.tsx:82 asset + :192 liability) — held by NO
    // spec before this pin. The coverage map (read per the SPEC-ALIAS
    // lesson against the specs' own assertions): the v46 F2 census holds
    // the networth kebab's AT-REST opacity-0 + the REAL-HOVER group-hover
    // reveal; the v36 S3 census the KEYBOARD focus-visible reveal; the
    // v122 pin the OPEN path on the SAVINGS item-card (item-card.tsx:139
    // — a DIFFERENT FILE whose pin-sanity mutation left these networth
    // twins green, the different-file immunity proven live in the v122
    // cycle). The CLONE-ONLY form (the v46 F3 adapted precedent + the
    // v122 twin): the reference's trigger stays INVISIBLE when its menu
    // is opened (its own superset-#7 bug), and a reference-side
    // measurement would require a CLICK on the reference's net-worth
    // kebab (the v46 read-only rule — and the net-worth kebab flow is
    // NEVER safe to probe past the menu open: the menu's Delete click IS
    // the delete). The family chrome = the v122 pinned contract BY
    // CONSTRUCTION (the identical class string, net-worth-view.tsx:82/192
    // <-> item-card.tsx:139).
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    // The settle pattern: the seeded Share Portfolio asset card (the v106
    // pin's own card — the first networth asset).
    const card = page.locator("div.rounded-xl").filter({ hasText: "Share Portfolio" }).first();
    await expect(card).toBeVisible();
    // STRUCTURAL finder (the v72 discipline + the v122 pin's own live-red
    // discovery): the aria-label CSS form, NOT getByRole — while the menu
    // is OPEN Radix marks the app aria-hidden (the modal layer), which
    // EXCLUDES the trigger from the accessibility tree and makes the
    // role-name locator unresolvable mid-open.
    const trigger = card.locator('button[aria-label="Actions for Share Portfolio"]');

    // Park the REAL pointer off-card, then read the at-rest baseline (the
    // v45/v46 contract: opacity 0, data-state closed — the ladder's
    // first rung, establishing the contrast the axis needs).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await trigger.evaluate((el) => ({
      opacity: getComputedStyle(el).opacity,
      state: el.getAttribute("data-state"),
    }));
    expect(atRest).toEqual({ opacity: "0", state: "closed" });

    // The native click opens the Radix menu (Playwright's locator click
    // IS the full pointer sequence — the v46 lesson), then the REAL
    // pointer parks at (5,5): the group-hover path disengages and the
    // focus path is unengaged (Radix holds focus in the menu content) —
    // the open-state token must ALONE hold the reveal (THE AXIS).
    await card.hover();
    await trigger.click();
    const menu = page.getByRole("menu");
    await expect(menu).toBeVisible();
    await expect(menu.getByRole("menuitem")).toHaveCount(2);
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400); // the transition-opacity settle
    const census = await trigger.evaluate((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      const host = el.closest("div.rounded-xl") as HTMLElement | null;
      const cr = host ? host.getBoundingClientRect() : null;
      return {
        opacity: cs.opacity,
        state: el.getAttribute("data-state"),
        w: Math.round(r.width),
        h: Math.round(r.height),
        radius: cs.borderRadius,
        bg: cs.backgroundColor,
        color: cs.color,
        cardTop: cr ? Math.round(r.top - cr.top) : null,
        cardRight: cr ? Math.round(cr.right - r.right) : null,
      };
    });
    // THE AXIS + the unchanged box chrome (the v46/v116/v122 pinned
    // family contract — the reveal costs no geometry; the insets 21/21 =
    // the p-5 20px + the 1px border).
    expect(census).toEqual({
      opacity: "1",
      state: "open",
      w: 36,
      h: 36,
      radius: "6px",
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      cardTop: 21,
      cardRight: 21,
    });

    // The fixture-restore: the REAL Escape press dismisses the menu (the
    // v98 form; no menuitem ever clicked — the data never touched).
    await page.keyboard.press("Escape");
    await expect(menu).not.toBeVisible();
    const closed = await trigger.evaluate((el) => el.getAttribute("data-state"));
    expect(closed).toBe("closed");
  });
});
