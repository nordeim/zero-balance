import { expect, test } from "@playwright/test";

// Dashboard: the NET ZERO GOAL hero (allocation %, |balance|, status-conditional
// chip/fill), the Net Zero Breakdown (3-level expandable drill-down — see
// breakdown.spec.ts), the three stat cards (text-3xl forestDark amounts), the
// Spending Breakdown donut (value-DESC sector order + iconed legend), the
// tinted Budget Guidelines cards, and the quick-action card buttons.
// Expected values are the seed's exact arithmetic:
//   income 5550 · savings 1250 · expenses 2235 → balance +2065 (Under
//   Budget), allocation 62.8%; spending over 9035 total: savings 1250
//   (13.8%), want 415 (4.6%), need 7370 (81.6%).
// Money is the reference's PLAIN format ("$5550.00", no thousands separator).
// Contexts arrive AUTHENTICATED (setup-project storageState).

test.describe("dashboard", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    // Wait for the store's fetch — the amounts render with the data, not
    // on the static shell.
    await expect(page.getByText("+$2065.00")).toBeVisible();
  });

  test("renders the page header with the gradient Add Item button", async ({ page }) => {
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
    await expect(
      page.getByText("Track your income, savings, and expenses to achieve net zero"),
    ).toBeVisible();
    const add = page.getByRole("button", { name: "Add Item" });
    await expect(add).toBeVisible();
    // The header button carries the forest→lime 135deg gradient.
    const bg = await add.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))");
  });

  test("the quick-action Add Item renders the reference focus-visible composite (v35 S2)", async ({ page }) => {
    // Session-70 surface #2, first measured v35: the reference's "Add Item"
    // header button, REAL-Tab-measured, renders the FOUR-layer composite —
    // the v4 white zero-spread lead + the shadcn 1px #0a0a0a ring + the
    // gradient family's two ambient layers — with v3's outline-none
    // (transparent 2px, offset 2px). The clone's .zb-btn-add:focus-visible
    // (globals.css, v11) emits it; this pins the dashboard instance.
    const add = page.getByRole("button", { name: "Add Item" });
    await expect(add).toBeVisible();
    const focused = await add.evaluate((el) => {
      // focusVisible is a real Chromium FocusOptions member (the live
      // probes used it) — TS's DOM lib lags it, hence the cast.
      (el as HTMLElement).focus({ focusVisible: true } as unknown as FocusOptions);
      const cs = getComputedStyle(el);
      return { fv: el.matches(":focus-visible"), shadow: cs.boxShadow, outline: cs.outline };
    });
    expect(focused.fv).toBe(true);
    expect(focused.shadow).toContain("rgb(255, 255, 255) 0px 0px 0px 0px");
    expect(focused.shadow).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");
    expect(focused.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(focused.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(focused.outline).toBe("rgba(0, 0, 0, 0) solid 2px");
  });

  test("NET ZERO GOAL hero shows allocation, |balance| and Under Budget status", async ({ page }) => {
    await expect(page.getByText("NET ZERO GOAL")).toBeVisible();
    await expect(page.getByText("Income = Savings + Expenses")).toBeVisible();
    // Allocation: (1250 + 2235) / 5550 → 62.8%
    await expect(page.getByText("Budget Allocation")).toBeVisible();
    await expect(page.getByText("62.8%")).toBeVisible();
    // Balance: 5550 - 1250 - 2235 → $2065.00 (plain format, Math.abs —
    // the sign lives in the status chip).
    await expect(page.getByText("Balance", { exact: true })).toBeVisible();
    await expect(page.getByText("$2065.00").first()).toBeVisible();
    await expect(page.getByText("Under Budget")).toBeVisible();
    // The hero's gradient: linear-gradient(135deg, forest-dark, forest-medium)
    const hero = page.locator("div.rounded-2xl").filter({ hasText: "NET ZERO GOAL" }).first();
    const bg = await hero.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(bg).toContain("linear-gradient(135deg, rgb(26, 58, 46)");
    // Under-budget allocation fill: orange gradient (reference bundle). The
    // computed string carries explicit 0%/100% stops.
    const fill = hero.locator("div.h-3 > div");
    const fillBg = await fill.evaluate((el) => getComputedStyle(el).backgroundImage);
    expect(fillBg).toContain("linear-gradient(90deg, rgb(224, 122, 59) 0%, rgb(245, 169, 98) 100%)");
  });

  test("stat cards show forestDark amounts, counts and navigate", async ({ page }) => {
    // Amounts: text-3xl forestDark, PLAIN format (no commas).
    await expect(page.getByText("$5550.00").first()).toBeVisible();
    await expect(page.getByText("$1250.00").first()).toBeVisible();
    await expect(page.getByText("$2235.00").first()).toBeVisible();

    // Amount color is forestDark rgb(26,58,46), NOT the type accent (the
    // breakdown row renders the same figure in lime — scope to the stat
    // card's text-3xl amount).
    const amountEl = page.locator("p.text-3xl").filter({ hasText: "$5550.00" });
    await expect(amountEl).toHaveCSS("color", "rgb(26, 58, 46)");

    // Counts (income 2, savings 2, expenses 3) with the h-px divider row.
    await expect(page.getByText("2 items", { exact: true }).first()).toBeVisible();
    await expect(page.getByText("3 items", { exact: true }).first()).toBeVisible();

    // Stat cards are clickable and route to their view (click the card's
    // own amount — the breakdown row shows the same figure but expands
    // the drill-down instead of navigating).
    await page.locator("p.text-3xl").filter({ hasText: "$5550.00" }).click();
    await expect(page).toHaveURL(/\/income$/);
  });

  test("Spending Breakdown renders value-DESC sectors and iconed legend", async ({ page }) => {
    await expect(page.getByText("Spending Breakdown")).toBeVisible();
    await expect(page.getByText("Needs vs Wants vs Savings")).toBeVisible();

    // Sector order mirrors the reference (session-17 audit, plan v9 G1): its
    // donut data is sorted by value DESC — measured live as [Need $6025,
    // Savings $300, Want $200] with the biggest slice anchored at recharts'
    // 3-o'clock start. With the seed's data (need 7370 > savings 1250 > want
    // 415) the fills are [orange, lime, blue]. The v2-era [S, W, N] order was
    // the same convention with then-different reference data.
    const fills: string[] = await page.locator(".recharts-sector").evaluateAll((nodes) =>
      nodes.map((n) => getComputedStyle(n).fill),
    );
    expect(fills).toEqual(["rgb(224, 122, 59)", "rgb(143, 188, 63)", "rgb(59, 126, 161)"]);

    // The reference renders NO percentage-label connector lines (measured:
    // labelLineCount 0); recharts only omits them with labelLine={false}.
    const labelLines = await page.locator(".recharts-pie-label-line").count();
    expect(labelLines).toBe(0);

    // Legend rows (order Need → Savings → Want, value-desc) on the tinted bg
    // with circle-alert / piggy-bank / heart icons and plain amounts.
    const legend = page.locator("div.flex.flex-col.gap-3.mt-6");
    await expect(legend).toBeVisible();
    const rows = legend.locator("> div");
    await expect(rows).toHaveCount(3);
    await expect(rows.nth(0)).toContainText("Need");
    await expect(rows.nth(0)).toContainText("$7370.00");
    await expect(rows.nth(0)).toContainText("81.6%");
    await expect(rows.nth(0).locator("svg.lucide-circle-alert")).toBeVisible();
    await expect(rows.nth(1)).toContainText("Savings");
    await expect(rows.nth(1)).toContainText("$1250.00");
    await expect(rows.nth(1)).toContainText("13.8%");
    await expect(rows.nth(1).locator("svg.lucide-piggy-bank")).toBeVisible();
    await expect(rows.nth(2)).toContainText("Want");
    await expect(rows.nth(2)).toContainText("$415.00");
    await expect(rows.nth(2)).toContainText("4.6%");
    await expect(rows.nth(2).locator("svg.lucide-heart")).toBeVisible();
    // Tinted row background rgb(245,248,245).
    await expect(rows.nth(0)).toHaveCSS("background-color", "rgb(245, 248, 245)");
  });

  test("donut hover tooltip formats the value like the reference (v14 — plan G1)", async ({ page }) => {
    // Measured live on the reference: hovering a sector renders the recharts
    // DEFAULT tooltip with the item row "Need : $6025.00" — the value carries
    // the dollar sign and two decimals (the dashboard's plain money format).
    // The clone rendered the raw number ("7370") because <Tooltip /> had no
    // formatter. The tooltip chrome (both recharts defaults) is identical.
    // NB: the hover is dispatched synthetically (like the live probe) — a
    // Playwright .hover() loops forever because the mouse-following tooltip
    // re-triggers pointer events under the cursor.
    const hovered = await page.evaluate(() => {
      const sector = document.querySelector(".recharts-pie-sector path");
      if (!sector) return false;
      const r = sector.getBoundingClientRect();
      const cx = r.x + r.width / 2;
      const cy = r.y + r.height / 2;
      const ev = (type: string) => new MouseEvent(type, { bubbles: true, cancelable: true, clientX: cx, clientY: cy });
      sector.dispatchEvent(new PointerEvent("pointermove", { bubbles: true, cancelable: true, clientX: cx, clientY: cy }));
      sector.dispatchEvent(ev("mouseover"));
      sector.dispatchEvent(ev("mousemove"));
      return true;
    });
    expect(hovered).toBe(true);

    const value = page.locator(".recharts-tooltip-item-value");
    await expect(value).toHaveText("$7370.00"); // the seed's Need slice

    // The whole item row reads "name : value" like the reference's.
    const item = page.locator(".recharts-tooltip-item");
    await expect(item).toHaveText("Need : $7370.00");

    // The reference OVERRIDES the recharts default chrome: padding 10,
    // white bg, 1px #e5e7e3 border (its CARD token), radius 8, and the
    // soft 0 4px 12px shadow. Recharts 3's bare default (#cccccc border,
    // square corners, no shadow) drifts — pinned via contentStyle.
    const tip = page.locator(".recharts-default-tooltip");
    await expect(tip).toHaveCSS("padding", "10px");
    await expect(tip).toHaveCSS("border-radius", "8px");
    await expect(tip).toHaveCSS("border-width", "1px");
    await expect(tip).toHaveCSS("border-color", "rgb(229, 231, 227)");
    await expect(tip).toHaveCSS("box-shadow", "rgba(0, 0, 0, 0.1) 0px 4px 12px 0px");
    // recharts 2 (the reference) renders the item row in BLACK; recharts 3
    // defaults it to the sector's fill color (orange) — pinned black.
    await expect(item).toHaveCSS("color", "rgb(0, 0, 0)");
  });

  test("Budget Guidelines renders the tinted 50/30/20 cards", async ({ page }) => {
    await expect(page.getByText("Budget Guidelines")).toBeVisible();
    await expect(page.getByText("Essential expenses like rent, utilities, groceries")).toBeVisible();
    await expect(page.getByText("Discretionary spending like entertainment, dining out")).toBeVisible();
    await expect(page.getByText("Emergency fund, retirement, investments")).toBeVisible();

    // Needs card: orange tint + border (measured #fff7f5 / #fcddd5).
    const needs = page.locator("div").filter({ hasText: "Essential expenses like rent, utilities, groceries" }).last();
    await expect(needs).toHaveCSS("background-color", "rgb(255, 247, 245)");
    await expect(needs).toHaveCSS("border-color", "rgb(252, 221, 213)");
    // Savings card: green tint.
    const savings = page.locator("div").filter({ hasText: "Emergency fund, retirement, investments" }).last();
    await expect(savings).toHaveCSS("background-color", "rgb(245, 249, 240)");
    await expect(savings).toHaveCSS("border-color", "rgb(223, 236, 208)");
  });

  test("quick action card buttons open the Add Item dialog with the type preselected", async ({ page }) => {
    const income = page.getByRole("button", { name: "Add Income" });
    await expect(income).toHaveClass(/rounded-2xl/);
    await income.click();
    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    await expect(dialog.getByRole("heading", { name: "Add Budget Item" })).toBeVisible();
    // The type select shows the preselected type (Income for this action)
    // — assert on the trigger's own text, not a page-wide text lookup (the
    // closed dropdown's hidden "Income" option would collide).
    await expect(dialog.getByRole("combobox", { name: "Type" })).toHaveText(/Income/);
    await dialog.getByRole("button", { name: "Cancel" }).click();
    await expect(dialog).toBeHidden();

    await page.getByRole("button", { name: "Add Savings" }).click();
    await expect(page.getByRole("dialog")).toBeVisible();
    await page.getByRole("button", { name: "Cancel" }).click();

    await page.getByRole("button", { name: "Add Expense" }).click();
    await expect(page.getByRole("dialog")).toBeVisible();
  });
});

// ---------------------------------------------------------------------------
// Donut keyboard semantics (v31 — plan G1)
// The reference (recharts 2.15) renders an INERT chart surface (no tabindex
// attribute, no role), a tooltip with NO live-region semantics, and a pie
// layer g.recharts-pie at tabIndex=0 whose keydown handler roves sector
// focus: ArrowLeft = ++wrap (forward), ArrowRight = --wrap (BACKWARD — the
// first ArrowRight from a fresh pie focuses the LAST sector in DOM order),
// Escape blurs the tracked sector and resets the index. recharts 3 dropped
// all three: the a11y layer defaults ON (surface tabIndex=0 + role=
// application + tooltip role=status/aria-live=assertive) and the pie
// keyboard handlers were removed. Pinned here after live measurement on
// both sites (docs/remediation-plan-v31.md).
// ---------------------------------------------------------------------------

test.describe("donut keyboard semantics (v31 — plan G1)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
    await expect(page.locator(".recharts-pie")).toBeAttached();
  });

  test("the chart surface is inert and the tooltip carries no live-region role (reference = recharts 2)", async ({ page }) => {
    // The reference's svg.recharts-surface has NO tabindex attribute and NO
    // role — recharts 3's accessibilityLayer default (tabIndex="0" +
    // role="application") drifted. SVG elements without the attribute read
    // .tabIndex === -1 — assert the ATTRIBUTE is absent, not the property.
    const surface = page.locator(".recharts-surface");
    await expect(surface).toBeAttached();
    const attrs = await surface.evaluate((s) => ({
      tabindex: s.getAttribute("tabindex"),
      role: s.getAttribute("role"),
    }));
    expect(attrs.tabindex).toBeNull();
    expect(attrs.role).toBeNull();

    // The pie layer IS the reference's tab stop (recharts rootTabIndex: 0 —
    // identical in 2.15 and 3.10; the layer is where keyboard focus lands).
    const layerTb = await page.locator(".recharts-pie").evaluate((l) => l.tabIndex);
    expect(layerTb).toBe(0);

    // The tooltip's default content renders NO live-region semantics on the
    // reference — recharts 3's role="status" + aria-live="assertive" drift.
    // Hover a sector synthetically (the mouse-following tooltip loops a
    // Playwright .hover()), then census the tooltip's attribute set.
    await page.evaluate(() => {
      const sector = document.querySelector(".recharts-pie-sector path");
      if (!sector) return;
      const r = sector.getBoundingClientRect();
      const cx = r.x + r.width / 2;
      const cy = r.y + r.height / 2;
      const ev = (type: string) =>
        new MouseEvent(type, { bubbles: true, cancelable: true, clientX: cx, clientY: cy });
      sector.dispatchEvent(
        new PointerEvent("pointermove", { bubbles: true, cancelable: true, clientX: cx, clientY: cy }),
      );
      sector.dispatchEvent(ev("mouseover"));
      sector.dispatchEvent(ev("mousemove"));
    });
    const tip = page.locator(".recharts-default-tooltip");
    await expect(tip).toBeVisible();
    const tipAttrs = await tip.evaluate((t) => ({
      role: t.getAttribute("role"),
      ariaLive: t.getAttribute("aria-live"),
    }));
    expect(tipAttrs.role).toBeNull();
    expect(tipAttrs.ariaLive).toBeNull();
  });

  test("arrow keys rove sector focus and Escape resets (the recharts 2.15 pie contract)", async ({ page }) => {
    // Focus the pie layer the way a keyboard user would (it is the tab
    // stop), then drive the reference's exact roving contract.
    await page.evaluate(() => {
      const layer = document.querySelector(".recharts-pie");
      if (layer instanceof SVGGElement) layer.focus();
    });

    // ArrowRight from a fresh pie (index 0): --0 → -1 → len-1 → the LAST
    // sector in DOM order. The e2e seed's DOM order is value-DESC:
    // [Need, Savings, Want] — the first ArrowRight focuses Want.
    await page.keyboard.press("ArrowRight");
    let focused: { isSector?: boolean; index: number } = await page.evaluate(() => {
      const a = document.activeElement;
      const sectors = [...document.querySelectorAll(".recharts-pie-sector")];
      return { isSector: !!a && sectors.includes(a as Element), index: sectors.indexOf(a as Element) };
    });
    expect(focused.isSector).toBe(true);
    expect(focused.index).toBe(2); // the LAST sector (the reference's --wrap quirk)

    // A second ArrowRight moves BACKWARD to the middle sector (Savings).
    await page.keyboard.press("ArrowRight");
    focused = await page.evaluate(() => {
      const sectors = [...document.querySelectorAll(".recharts-pie-sector")];
      return { index: sectors.indexOf(document.activeElement as Element) };
    });
    expect(focused.index).toBe(1);

    // ArrowLeft roves forward (back to the last sector).
    await page.keyboard.press("ArrowLeft");
    focused = await page.evaluate(() => {
      const sectors = [...document.querySelectorAll(".recharts-pie-sector")];
      return { index: sectors.indexOf(document.activeElement as Element) };
    });
    expect(focused.index).toBe(2);

    // Escape blurs the tracked sector — focus resets to the body.
    await page.keyboard.press("Escape");
    const afterEscape = await page.evaluate(() => document.activeElement === document.body);
    expect(afterEscape).toBe(true);

    // The roving never opens the tooltip (the reference's keyboard focus is
    // visual-only — measured: tip invisible across the whole walk).
    const tipVisible = await page.evaluate(() => {
      const t = document.querySelector(".recharts-tooltip-wrapper");
      return !!t && t.textContent.trim().length > 0 && getComputedStyle(t).visibility !== "hidden";
    });
    expect(tipVisible).toBe(false);
  });

  test("the dashboard Tab-order census + the interactive stat-card superset (v40 F1)", async ({ page }) => {
    // Session-78 queue's LAST unmeasured surface, first measured v40 on
    // BOTH sites (tabwalk-v36.sh + focus-census-v40.mjs +
    // stat-card-chain-v40.mjs): the REAL-Tab walk on the dashboard is
    // the five nav links → the Add Item header button → the three
    // NetZero-breakdown stat-row buttons → the three interactive stat
    // cards → the donut's g.recharts-pie tab stop → the three
    // quick-action cards → the body wrap. The reference's cycle is the
    // same 14-app stops PLUS its Base44 "Close badge" (platform chrome,
    // correctly absent here — the v36 census treatment) MINUS the three
    // stat-card stops: its 304×210 big stat cards are INERT divs (no
    // role, no tabindex, no handler — dead UI; the clone's are
    // div[role=button] + tabIndex=0 + Enter/Space routing — the same
    // superset class as the kebab focus reveal #7).
    const readStop = () =>
      page.evaluate(() => {
        const el = document.activeElement;
        if (!el || el === document.body) return null;
        const r = el.getBoundingClientRect();
        return {
          tag: el.tagName.toLowerCase(),
          role: el.getAttribute("role"),
          name: (
            el.getAttribute("aria-label") ||
            (el.textContent || "").trim().replace(/\s+/g, " ")
          ).slice(0, 30),
          tabindex: el.getAttribute("tabindex"),
          rect: [Math.round(r.x), Math.round(r.width), Math.round(r.height)],
        };
      });

    // Blur to the page start, then walk with REAL Tab presses (450ms
    // settles — the v36 sheet-ring fade discipline; the page auto-scrolls
    // with focus, so only the scroll-independent bands (x/w/h) are
    // asserted below).
    await page.evaluate(() => {
      const el = document.activeElement as HTMLElement | null;
      if (el && el !== document.body) el.blur();
    });
    const expected: Array<{ tag: string; role: string | null; name: string; tabindex: string | null }> = [
      { tag: "a", role: null, name: "Dashboard", tabindex: null },
      { tag: "a", role: null, name: "Income", tabindex: null },
      { tag: "a", role: null, name: "Expenses", tabindex: null },
      { tag: "a", role: null, name: "Savings", tabindex: null },
      { tag: "a", role: null, name: "Net Worth", tabindex: null },
      { tag: "button", role: null, name: "Add Item", tabindex: null },
      { tag: "button", role: null, name: "Total Income$5550.00", tabindex: null },
      { tag: "button", role: null, name: "Total Savings- $1250.00", tabindex: null },
      { tag: "button", role: null, name: "Total Expenses- $2235.00", tabindex: null },
      { tag: "div", role: "button", name: "Total Income$5550.002 items", tabindex: "0" },
      { tag: "div", role: "button", name: "Total Savings$1250.002 items", tabindex: "0" },
      { tag: "div", role: "button", name: "Total Expenses$2235.003 items", tabindex: "0" },
      { tag: "g", role: null, name: "", tabindex: "0" },
      { tag: "button", role: null, name: "Add Income", tabindex: null },
      { tag: "button", role: null, name: "Add Savings", tabindex: null },
      { tag: "button", role: null, name: "Add Expense", tabindex: null },
    ];
    for (const want of expected) {
      await page.keyboard.press("Tab");
      await page.waitForTimeout(450);
      const stop = await readStop();
      expect(stop).not.toBeNull();
      expect(stop!.tag).toBe(want.tag);
      expect(stop!.role).toBe(want.role);
      expect(stop!.name).toBe(want.name);
      if (want.tabindex !== null) {
        expect(stop!.tabindex).toBe(want.tabindex);
      }
    }

    // Geometry bands measured on both sites (1280×800, doc-order census):
    // the nav links x=20 w=215 h=32 with the 40px rail pitch; Add Item
    // x≈1121 w≈127 h≈36; the stat-row buttons x=961 w=254; the stat
    // cards x=288/616/944 w=304 h=210; the quick actions w=304 h=90.
    const navPitch = await page.evaluate(() => {
      const links = [...document.querySelectorAll("nav a")].slice(0, 5);
      return links.map((l) => {
        const r = l.getBoundingClientRect();
        return [Math.round(r.x), Math.round(r.width), Math.round(r.height), Math.round(r.y)];
      });
    });
    for (const [x, w, h] of navPitch) {
      expect(x).toBe(20);
      expect(w).toBe(215);
      expect(h).toBe(32);
    }
    for (let i = 1; i < navPitch.length; i++) {
      expect(navPitch[i][3] - navPitch[i - 1][3]).toBe(40);
    }
    const bands = await page.evaluate(() => {
      const rect = (el: Element | null) => {
        if (!el) return null;
        const r = el.getBoundingClientRect();
        return [Math.round(r.x), Math.round(r.width), Math.round(r.height)];
      };
      const statRows = [...document.querySelectorAll("button")].filter((b) =>
        (b.textContent || "").includes("Total Income$5550.00"),
      );
      const addItem = [...document.querySelectorAll("button")].filter((b) =>
        (b.textContent || "").trim() === "Add Item",
      );
      const cards = [...document.querySelectorAll('div[role="button"]')].filter((d) =>
        (d.textContent || "").startsWith("Total"),
      );
      return {
        addItem: rect(addItem[0] ?? null),
        statRow: rect(statRows[0] ?? null),
        card0: rect(cards[0] ?? null),
        card1: rect(cards[1] ?? null),
        card2: rect(cards[2] ?? null),
      };
    });
    expect(bands.addItem).toEqual([1121, 127, 36]);
    expect(bands.statRow).toEqual([961, 254, 56]);
    expect(bands.card0).toEqual([288, 304, 210]);
    expect(bands.card1).toEqual([616, 304, 210]);
    expect(bands.card2).toEqual([944, 304, 210]);

    // The walk wraps to the body after the last quick action (the
    // reference's platform-badge stop does not exist here).
    await page.keyboard.press("Tab");
    await page.waitForTimeout(450);
    const afterWrap = await page.evaluate(() => document.activeElement === document.body);
    expect(afterWrap).toBe(true);

    // THE SUPERSET ACTIVATION: the reference's inert stat cards do
    // NOTHING on Enter/Space; the clone's route to the type view. Focus
    // the cards directly (the walk's stops 10-12 already proved
    // Tab-focusability).
    const incomeCard = page.locator('div[role="button"]').filter({ hasText: "Total Income" });
    await incomeCard.focus();
    await expect(incomeCard).toBeFocused();
    await page.keyboard.press("Enter");
    await expect(page).toHaveURL(/\/income$/);

    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
    const savingsCard = page.locator('div[role="button"]').filter({ hasText: "Total Savings" });
    await savingsCard.focus();
    await expect(savingsCard).toBeFocused();
    await page.keyboard.press(" ");
    await expect(page).toHaveURL(/\/savings$/);
  });
});

// ---------------------------------------------------------------------------
// Mid-viewport census (v42 — remediation-plan-v42.md F2/F3) — the
// session-90/91 queue: the MID viewport 640×960 of the five non-networth
// routes (the v41 lesson applied: an unmeasured VIEWPORT CLASS is as
// dangerous as an unmeasured surface — the rhythm bug survived 40
// iterations because 640 was never census'd; v41 measured /networth, v42
// closes the set). Measured on BOTH sites with mid-census-v42.mjs +
// hero-attrib-v42.mjs + bd-attrib-v42.mjs + tail-v42.mjs.
//
// THE V42 FINDING: the NetZeroBreakdownCard ran +13px taller than the
// reference at BOTH viewports (640: 337 vs 324; 1280: 377 vs 364) — the
// clone rendered TWO Dividers (Income|Savings AND Savings|Expenses), the
// reference ONE (Income|Savings only — the app's ONE rule grouped:
// [Income] | [Savings, Expenses] | border-t | [Net Balance]). F1 fixes
// the divider condition; these census tests pin the fix.
// ---------------------------------------------------------------------------
test.describe("mid-viewport band census (v42 — plan F2/F3)", () => {
  test("the breakdown card's band census at 1280 — the single divider, the 364px card (v42 F2)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();

    const census = await page.evaluate(() => {
      const leaf = (txt: string) =>
        [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) => (e.textContent || "").trim() === txt && e.children.length === 0,
        );
      const bdH = leaf("Net Zero Breakdown");
      if (!bdH) return null;
      const card = bdH.closest('div[class*="rounded-2xl"]');
      const stack = bdH.parentElement
        ? (bdH.parentElement.children[1] as HTMLElement | null)
        : null;
      if (!card || !stack) return null;
      const cr = card.getBoundingClientRect();
      const cs = getComputedStyle(card);
      const bands = [...stack.children].map((c) => ({
        text: (c.textContent || "").trim().slice(0, 20),
        h: Math.round(c.getBoundingClientRect().height),
      }));
      return {
        card: {
          h: Math.round(cr.height),
          pad: cs.padding,
          radius: cs.borderRadius,
          border: cs.borderTopWidth,
        },
        bands,
      };
    });
    expect(census).not.toBeNull();
    // The F1 pin: ONE divider — the reference's 5-band stack (the clone's
    // pre-fix was 6 with the second Savings|Expenses divider, +13px).
    // Row heights at 1280 wrap identically on both sites (56/64/64) with
    // their own datasets — the wrap is width-driven, not data-driven.
    expect(census!.bands).toHaveLength(5);
    expect(census!.bands.map((b) => b.h)).toEqual([56, 1, 64, 64, 45]);
    // The band texts: the divider is the empty 1px band (index 1).
    expect(census!.bands[1]!.text).toBe("");
    expect(census!.bands[0]!.text.startsWith("Total Income")).toBe(true);
    expect(census!.bands[2]!.text.startsWith("Total Savings")).toBe(true);
    expect(census!.bands[3]!.text.startsWith("Total Expenses")).toBe(true);
    expect(census!.bands[4]!.text.startsWith("Net Balance")).toBe(true);
    // The card joins the reference's measured height (364; pre-fix 377).
    expect(census!.card.h).toBe(364);
    expect(census!.card.pad).toBe("24px");
    expect(census!.card.radius).toBe("16px");
    expect(census!.card.border).toBe("1px");
  });

  test("the dashboard hero grid census at 640 — the goalCard 316, the breakdownCard 324, the scrollHeight 3029 (v42 F2)", async ({ page }) => {
    await page.setViewportSize({ width: 640, height: 960 });
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
    // Settle the allocation bar's 500ms width transition before the
    // scroll-height read.
    await page.waitForTimeout(600);

    const census = await page.evaluate(() => {
      const leaf = (txt: string) =>
        [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) => (e.textContent || "").trim() === txt && e.children.length === 0,
        );
      const h1 = [...document.querySelectorAll("h1")]
        .filter((h) => !h.closest("header"))
        .find((h) => h.getBoundingClientRect().height > 0);
      if (!h1) return null;
      const cap = h1.closest('div[class*="max-w"]');
      if (!cap) return null;
      const kids = [...cap.children];
      const hero = kids[1] as HTMLElement | undefined;
      const secondBand = kids[2] as HTMLElement | undefined;
      const thirdBand = kids[3] as HTMLElement | undefined;
      const goalH = leaf("NET ZERO GOAL");
      const goalCard = goalH ? goalH.closest('div[class*="rounded-2xl"]') : null;
      const bdH = leaf("Net Zero Breakdown");
      const bdCard = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
      if (!hero || !goalCard || !bdCard || !secondBand || !thirdBand) return null;
      const gr = goalCard.getBoundingClientRect();
      const br = bdCard.getBoundingClientRect();
      const hr = hero.getBoundingClientRect();
      const heroCs = getComputedStyle(hero);
      const rowCs = getComputedStyle(kids[0] as HTMLElement);
      const h1r = h1.getBoundingClientRect();
      return {
        hero: { h: Math.round(hr.height), display: heroCs.display, cols: heroCs.gridTemplateColumns, gap: heroCs.gap },
        goalCard: { y: Math.round(gr.y), h: Math.round(gr.height) },
        bdCard: { y: Math.round(br.y), h: Math.round(br.height) },
        gapGoalToBd: Math.round(br.y - (gr.y + gr.height)),
        secondBandY: Math.round(secondBand.getBoundingClientRect().y),
        thirdBandY: Math.round(thirdBand.getBoundingClientRect().y),
        headerRowMb: rowCs.marginBottom,
        h1Font: getComputedStyle(h1).fontSize,
        h1H: Math.round(h1r.height),
        capW: Math.round(cap.getBoundingClientRect().width),
        sw: document.documentElement.scrollWidth,
        scrollH: document.documentElement.scrollHeight,
      };
    });
    expect(census).not.toBeNull();
    // The full hero census at the MID viewport (all measured on BOTH
    // sites — mid-census-v42.mjs + hero-attrib-v42.mjs):
    expect(census!.hero.h).toBe(664); // 316 + 24 + 324 (post-fix; pre-fix 677)
    expect(census!.hero.display).toBe("grid");
    expect(census!.hero.cols).toBe("608px"); // 1 track at 640
    expect(census!.hero.gap).toBe("24px");
    expect(census!.goalCard.y).toBe(229);
    expect(census!.goalCard.h).toBe(316);
    expect(census!.bdCard.y).toBe(569);
    expect(census!.bdCard.h).toBe(324); // post-fix; pre-fix 337
    expect(census!.gapGoalToBd).toBe(24);
    // Every band below the hero shifts back 13px post-fix (925/1635;
    // pre-fix 938/1648) — the F1 fix's downstream pins.
    expect(census!.secondBandY).toBe(925);
    expect(census!.thirdBandY).toBe(1635);
    // The whole-page pin: the reference's scrollHeight is 3029 at 640
    // (the clone's pre-fix was 3042 — exactly the +13 divider band;
    // tail-v42.mjs: the last band's mb=0 on both sites, so the delta
    // is the divider alone).
    expect(census!.scrollH).toBe(3029);
    // The common mid-viewport rhythm (identical on both sites).
    expect(census!.headerRowMb).toBe("32px");
    expect(census!.h1Font).toBe("30px");
    expect(census!.h1H).toBe(36);
    expect(census!.capW).toBe(608);
    expect(census!.sw).toBe(640); // no overflow at the mid viewport
  });

  test("the MID viewport (640×960) band census of the five authed routes — the 32px rhythm, the 608 cap, no overflow (v42 F3)", async ({ page }) => {
    // The five-route loop (the a11y route-extension for-loop pattern):
    // the common census — the 32px header→first-section rhythm (the v20
    // G1 pin's class, now pinned at the mid viewport), the 608px cap
    // (640 − 2×16), no horizontal overflow, the 30px h1 — plus the
    // route-class branches: the dashboard routes' hero grid (1-col,
    // 24px gap, 664 post-fix) and the items routes' filter card (block,
    // mb-24) + item grid (1-col, 16px gap).
    const routes: Array<[string, string, "dash" | "items"]> = [
      ["/", "Budget Dashboard", "dash"],
      ["/dashboard", "Budget Dashboard", "dash"],
      ["/income", "Income", "items"],
      ["/expenses", "Expenses", "items"],
      ["/savings", "Savings", "items"],
    ];
    for (const [route, h1Text, cls] of routes) {
      await page.setViewportSize({ width: 640, height: 960 });
      await page.goto(route);
      await expect(page.getByRole("heading", { name: h1Text })).toBeVisible();
      await page.waitForTimeout(500);
      const census = await page.evaluate(() => {
        const h1 = [...document.querySelectorAll("h1")]
          .filter((h) => !h.closest("header"))
          .find((h) => h.getBoundingClientRect().height > 0);
        if (!h1) return null;
        const cap = h1.closest('div[class*="max-w"]');
        if (!cap) return null;
        const kids = [...cap.children];
        const row = kids[0] as HTMLElement | undefined;
        const first = kids[1] as HTMLElement | undefined;
        const second = kids[2] as HTMLElement | undefined;
        if (!row || !first || !second) return null;
        const rowCs = getComputedStyle(row);
        const firstCs = getComputedStyle(first);
        const secondCs = getComputedStyle(second);
        return {
          path: location.pathname,
          gapRowToFirst: Math.round(first.getBoundingClientRect().y - row.getBoundingClientRect().bottom),
          headerRowMb: rowCs.marginBottom,
          headerRowDir: rowCs.flexDirection,
          h1Font: getComputedStyle(h1).fontSize,
          capW: Math.round(cap.getBoundingClientRect().width),
          sw: document.documentElement.scrollWidth,
          first: {
            display: firstCs.display,
            mb: firstCs.marginBottom,
            cols: firstCs.display === "grid" ? firstCs.gridTemplateColumns.split(" ").length : null,
            gap: firstCs.display === "grid" ? firstCs.gap : null,
            h: Math.round(first.getBoundingClientRect().height),
          },
          second: {
            display: secondCs.display,
            cols: secondCs.display === "grid" ? secondCs.gridTemplateColumns.split(" ").length : null,
            gap: secondCs.display === "grid" ? secondCs.gap : null,
          },
        };
      });
      expect(census, `census on ${route}`).not.toBeNull();
      // The common mid-viewport census (identical on BOTH sites —
      // mid-census-v42.mjs, all five routes):
      expect(census!.gapRowToFirst, `rhythm on ${route}`).toBe(32);
      expect(census!.headerRowMb, `headerRow mb on ${route}`).toBe("32px");
      expect(census!.headerRowDir, `headerRow dir on ${route}`).toBe("column");
      expect(census!.h1Font, `h1 font on ${route}`).toBe("30px");
      expect(census!.capW, `cap width on ${route}`).toBe(608);
      expect(census!.sw, `no overflow on ${route}`).toBe(640);
      if (cls === "dash") {
        expect(census!.first.display, `hero display on ${route}`).toBe("grid");
        expect(census!.first.cols, `hero cols on ${route}`).toBe(1);
        expect(census!.first.gap, `hero gap on ${route}`).toBe("24px");
        expect(census!.first.h, `hero height on ${route}`).toBe(664); // post-fix; pre-fix 677
      } else {
        expect(census!.first.display, `filter display on ${route}`).toBe("block");
        expect(census!.first.mb, `filter mb on ${route}`).toBe("24px");
        expect(census!.second.display, `grid display on ${route}`).toBe("grid");
        expect(census!.second.cols, `grid cols on ${route}`).toBe(1);
        expect(census!.second.gap, `grid gap on ${route}`).toBe("16px");
      }
    }
  });
});

// v43 (remediation-plan-v43.md) — the drill-down EXPANDED-state census:
// the v42 session pinned the collapsed bands; the expanded
// categories/subcategories/items bands were never measured. Measured on
// BOTH sites at 640x960 (exp-census-v43.mjs + exp-detail-v43.mjs +
// exp-rotate-v43.mjs + hover-v43.mjs): the per-row chrome is
// byte-identical at every level; TWO parity gaps found — the chevrons
// ROTATE on the clone (Tailwind v4 emits the modern CSS `rotate`
// property, NOT `transform` — the transform: none reading on both sites
// was meaningless, the v4 property trap) while the reference's are
// static, and the section-row hover renders lab() (the v4 named-palette
// trap, live: the section button carries no inline bg) where the
// reference computes rgb(249, 250, 251). The category rows'
// hover:bg-gray-100 is inert on BOTH sites (the inline bg overrides —
// v29's finding, DOM-identical).
test.describe("drill-down expanded-state census (v43 — plan F3/F4)", () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 640, height: 960 });
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
  });

  test("the expanded band census at 640 — the section/category/sub/item/footer chrome + the expansion heights (v43 F3)", async ({ page }) => {
    const census = await page.evaluate(async () => {
      const leaf = (txt: string) =>
        [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) => (e.textContent || "").trim() === txt && e.children.length === 0,
        );
      const bdH = leaf("Net Zero Breakdown");
      const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
      if (!card) return null;
      const collapsedH = Math.round(card.getBoundingClientRect().height);
      // Expand the Total Income section.
      const sec = [...card.querySelectorAll("button")].find((b) =>
        /Total Income/i.test(b.textContent || ""),
      );
      if (!sec) return null;
      const sCs = getComputedStyle(sec);
      const section = {
        h: Math.round(sec.getBoundingClientRect().height),
        pad: sCs.padding,
        ml: sCs.marginLeft,
        radius: sCs.borderRadius,
        cursor: sCs.cursor,
      };
      sec.click();
      await new Promise((r) => setTimeout(r, 500));
      const secExpandedH = Math.round(card.getBoundingClientRect().height);
      // The first category row (Salary).
      const cat = [...card.querySelectorAll("button")].find(
        (b) => b.offsetParent !== null && /\$/.test(b.textContent || "") && !/Total|Net Balance/i.test(b.textContent || ""),
      );
      if (!cat) return null;
      const cCs = getComputedStyle(cat);
      const cDot = [...cat.querySelectorAll("span")].find((s) => {
        const r = s.getBoundingClientRect();
        return r.width > 0 && r.width <= 8 && getComputedStyle(s).borderRadius === "9999px";
      });
      const catLabel = [...cat.querySelectorAll("span")].find((s) => {
        const t = (s.textContent || "").trim();
        return t.length > 1 && s.children.length === 0 && !/^\$/.test(t);
      });
      const category = {
        h: Math.round(cat.getBoundingClientRect().height),
        pad: cCs.padding,
        radius: cCs.borderRadius,
        bg: cCs.backgroundColor,
        dotW: cDot ? Math.round(cDot.getBoundingClientRect().width) : null,
        labelFont: catLabel ? getComputedStyle(catLabel).fontSize : null,
        labelWeight: catLabel ? getComputedStyle(catLabel).fontWeight : null,
        labelColor: catLabel ? getComputedStyle(catLabel).color : null,
      };
      cat.click();
      await new Promise((r) => setTimeout(r, 500));
      const fullExpandedH = Math.round(card.getBoundingClientRect().height);
      // The sub + item rows under the opened category.
      const subArea = [...cat.parentElement!.children].find(
        (c) => c !== cat && c.getBoundingClientRect().height > 0,
      );
      if (!subArea) return null;
      const rows = [...subArea.querySelectorAll("div")].filter((d) => {
        const cs = getComputedStyle(d);
        return cs.display === "flex" && d.children.length >= 2 && Math.round(d.getBoundingClientRect().height) >= 16;
      });
      const subRow = rows[0] as HTMLElement | undefined;
      const itemRow = rows[rows.length - 1] as HTMLElement | undefined;
      const subLabel = subRow
        ? [...subRow.querySelectorAll("span")].find((s) => {
            const t = (s.textContent || "").trim();
            return t.length > 1 && s.children.length === 0 && !/^\$/.test(t);
          })
        : null;
      const itemLabel = itemRow
        ? [...itemRow.querySelectorAll("span")].find((s) => {
            const t = (s.textContent || "").trim();
            return t.length > 1 && s.children.length === 0 && !/^\$/.test(t);
          })
        : null;
      const sub = subRow
        ? {
            h: Math.round(subRow.getBoundingClientRect().height),
            pad: getComputedStyle(subRow).padding,
            bg: getComputedStyle(subRow).backgroundColor,
            labelFont: subLabel ? getComputedStyle(subLabel).fontSize : null,
            labelWeight: subLabel ? getComputedStyle(subLabel).fontWeight : null,
            labelColor: subLabel ? getComputedStyle(subLabel).color : null,
          }
        : null;
      const item = itemRow
        ? {
            h: Math.round(itemRow.getBoundingClientRect().height),
            pad: getComputedStyle(itemRow).padding,
            color: getComputedStyle(itemRow).color,
            font: getComputedStyle(itemRow).fontSize,
            labelMaxW: itemLabel ? getComputedStyle(itemLabel).maxWidth : null,
            labelTrunc: itemLabel ? getComputedStyle(itemLabel).textOverflow : null,
          }
        : null;
      // The footer row ("2 categories").
      const footP = [...card.querySelectorAll("span")].find(
        (e) => /categor/i.test(e.textContent || "") && e.children.length === 0,
      );
      const footRow = footP ? (footP.closest("div") as HTMLElement | null) : null;
      const footer = footRow
        ? {
            h: Math.round(footRow.getBoundingClientRect().height),
            pad: getComputedStyle(footRow).padding,
            borderTop: getComputedStyle(footRow).borderTopWidth,
            font: getComputedStyle(footP!).fontSize,
            weight: getComputedStyle(footP!).fontWeight,
          }
        : null;
      return {
        collapsedH,
        secExpandedH,
        fullExpandedH,
        section,
        category,
        sub,
        item,
        footer,
        sw: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The card's expansion arithmetic (the seed's: 2 income categories,
    // the first with 1 sub + 1 item — deterministic for db/custom.db).
    expect(census!.collapsedH).toBe(324); // the v42 single-divider card
    expect(census!.secExpandedH).toBe(441);
    expect(census!.fullExpandedH).toBe(495);
    // The per-row chrome (byte-identical on BOTH sites — exp-census-v43).
    expect(census!.section).toEqual({ h: 48, pad: "8px", ml: "-8px", radius: "8px", cursor: "pointer" });
    expect(census!.category!.h).toBe(28);
    expect(census!.category!.pad).toBe("6px 12px");
    expect(census!.category!.radius).toBe("8px");
    expect(census!.category!.bg).toBe("rgb(249, 250, 251)"); // the inline bg (inert hover — v29)
    expect(census!.category!.dotW).toBe(6);
    expect(census!.category!.labelFont).toBe("12px");
    expect(census!.category!.labelWeight).toBe("500");
    expect(census!.category!.labelColor).toBe("rgb(26, 58, 46)");
    expect(census!.sub!.h).toBe(24);
    expect(census!.sub!.pad).toBe("4px 8px");
    expect(census!.sub!.bg).toBe("rgb(250, 250, 250)");
    expect(census!.sub!.labelFont).toBe("12px");
    expect(census!.sub!.labelWeight).toBe("400");
    expect(census!.sub!.labelColor).toBe("rgb(107, 114, 128)");
    expect(census!.item!.h).toBe(24);
    expect(census!.item!.pad).toBe("4px 8px");
    expect(census!.item!.font).toBe("12px");
    expect(census!.item!.color).toBe("rgb(156, 163, 175)");
    expect(census!.item!.labelMaxW).toBe("120px");
    expect(census!.item!.labelTrunc).toBe("ellipsis");
    expect(census!.footer!.h).toBe(29);
    expect(census!.footer!.pad).toBe("6px 12px");
    expect(census!.footer!.borderTop).toBe("1px");
    expect(census!.footer!.font).toBe("12px");
    expect(census!.footer!.weight).toBe("600");
    // No overflow even fully expanded.
    expect(census!.sw).toBe(640);
  });

  test("the drill-down chevrons stay STATIC on expansion — rotate: none at both levels (v43 F1)", async ({ page }) => {
    const reading = await page.evaluate(async () => {
      const leaf = (txt: string) =>
        [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) => (e.textContent || "").trim() === txt && e.children.length === 0,
        );
      const bdH = leaf("Net Zero Breakdown");
      const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
      if (!card) return null;
      const sec = [...card.querySelectorAll("button")].find((b) =>
        /Total Income/i.test(b.textContent || ""),
      );
      if (!sec) return null;
      const readChev = (row: HTMLElement) => {
        const svgs = [...row.querySelectorAll("svg")];
        const chev = svgs[svgs.length - 1] as SVGElement | undefined;
        if (!chev) return null;
        const cs = getComputedStyle(chev);
        return {
          rotate: cs.rotate,
          transform: cs.transform,
          w: Math.round(chev.getBoundingClientRect().width),
          transitionProperty: cs.transitionProperty,
          color: cs.color,
        };
      };
      const secBefore = readChev(sec);
      sec.click();
      await new Promise((r) => setTimeout(r, 500));
      const secAfter = readChev(sec);
      const cat = [...card.querySelectorAll("button")].find(
        (b) => b.offsetParent !== null && /\$/.test(b.textContent || "") && !/Total|Net Balance/i.test(b.textContent || ""),
      );
      if (!cat) return null;
      cat.click();
      await new Promise((r) => setTimeout(r, 500));
      const catAfter = readChev(cat);
      return { secBefore, secAfter, catAfter };
    });
    expect(reading).not.toBeNull();
    // The reference's measured contract (exp-rotate-v43.mjs, fresh
    // post-expansion queries on BOTH levels): rotate: none, transform:
    // none, transition "all" 0s — the chevrons NEVER rotate. The clone's
    // pre-fix v4 `rotate-180` read "180deg" here (the `rotate` property,
    // NOT `transform` — the v4 property trap: transform reads "none"
    // even while rotating).
    expect(reading!.secBefore!.rotate).toBe("none");
    expect(reading!.secAfter!.rotate).toBe("none"); // pre-fix: "180deg"
    expect(reading!.catAfter!.rotate).toBe("none"); // pre-fix: "180deg"
    expect(reading!.secAfter!.transform).toBe("none");
    // The chevrons' sizes stay pinned (14px section, 12px category).
    expect(reading!.secAfter!.w).toBe(14);
    expect(reading!.catAfter!.w).toBe(12);
    expect(reading!.secAfter!.color).toBe("rgb(156, 163, 175)");
  });

  test("the section-row hover computes the reference's rgb(249,250,251), not lab (v43 F2)", async ({ page }) => {
    // A REAL hover (the drill-down rows carry no mouse-following tooltip —
    // the donut's synthetic-hover lesson does not apply here). The exact
    // name disambiguates from the Total Income STAT CARD (role=button,
    // name "Total Income $5550.00 2 items").
    const sec = page.getByRole("button", { name: "Total Income $5550.00", exact: true });
    await sec.hover();
    await page.waitForTimeout(300);
    const reading = await page.evaluate(() => {
      const leaf = (txt: string) =>
        [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) => (e.textContent || "").trim() === txt && e.children.length === 0,
        );
      const bdH = leaf("Net Zero Breakdown");
      const card = bdH ? bdH.closest('div[class*="rounded-2xl"]') : null;
      const secEl = card
        ? ([...card.querySelectorAll("button")].find((b) => /Total Income/i.test(b.textContent || "")) as HTMLElement | null)
        : null;
      if (!secEl) return null;
      const cs = getComputedStyle(secEl);
      return { bg: cs.backgroundColor, cursor: cs.cursor };
    });
    expect(reading).not.toBeNull();
    // The reference's engaged hover computes v3 gray-50 as plain rgb. The
    // clone's pre-fix v4 named palette computed
    // lab(98.2596 -0.247031 -0.706708) — the named-palette trap, LIVE on
    // this surface (the section button carries no inline bg).
    expect(reading!.bg).toBe("rgb(249, 250, 251)"); // pre-fix: lab(...)
    expect(reading!.cursor).toBe("pointer");
  });
});

test.describe("drill-down viewport census + expansion animation (v44 — plan F1/F2/F3)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
  });

  test("the drill-down expansion ANIMATES — height + opacity tween in both directions (v44 F1)", async ({ page }) => {
    await page.setViewportSize({ width: 640, height: 960 });
    const reading = await page.evaluate(async () => {
      const leaf = (txt: string) =>
        [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) => (e.textContent || "").trim() === txt && e.children.length === 0,
        );
      const bdH = leaf("Net Zero Breakdown");
      const card = bdH ? (bdH.closest('div[class*="rounded-2xl"]') as HTMLElement | null) : null;
      if (!card) return null;
      const sec = [...card.querySelectorAll("button")].find((b) =>
        /Total Income/i.test(b.textContent || ""),
      ) as HTMLElement | null;
      if (!sec) return null;
      const collapsedH = Math.round(card.getBoundingClientRect().height);
      // EXPAND: click + sample the card height AND the band's computed
      // opacity every ~25ms (fresh queries each iteration — a saved DOM
      // node goes stale across the re-render, the v43 lesson).
      sec.click();
      const openSamples: { h: number; op: number | null }[] = [];
      for (let i = 0; i < 12; i++) {
        const band = [...sec.parentElement!.children].find((c) => c !== sec) as HTMLElement | null;
        openSamples.push({
          h: Math.round(card.getBoundingClientRect().height),
          op: band ? Number(getComputedStyle(band).opacity) : null,
        });
        await new Promise((r) => setTimeout(r, 25));
      }
      const secExpandedH = Math.round(card.getBoundingClientRect().height);
      // COLLAPSE: click again + sample.
      sec.click();
      const closeSamples: number[] = [];
      for (let i = 0; i < 12; i++) {
        closeSamples.push(Math.round(card.getBoundingClientRect().height));
        await new Promise((r) => setTimeout(r, 25));
      }
      const collapsedAgainH = Math.round(card.getBoundingClientRect().height);
      await new Promise((r) => setTimeout(r, 400));
      // After the exit animation: the band is UNMOUNTED (the section root
      // returns to the button alone — the reference's collapsed DOM).
      const bandCountAfter = [...sec.parentElement!.children].filter((c) => c !== sec).length;
      return { collapsedH, openSamples, secExpandedH, closeSamples, collapsedAgainH, bandCountAfter };
    });
    expect(reading).not.toBeNull();
    // The reference's measured contract (exp-vp-v44.mjs + collapse-ref-v44.mjs
    // on the reference at BOTH 390 and 1280): the card's height ramps
    // smoothly over ~200ms in BOTH directions (324→346→364→387→398→405
    // across ~40ms samples on the expand; 459→429→384→359→339→324 on the
    // collapse), the band's opacity eases 0↔1, and the section band
    // unmounts after the collapse animation. The clone's pre-fix mount
    // jumped instantly (324→441 at the FIRST sample — zero in-flight
    // frames, the v44 F1 gap).
    expect(reading!.collapsedH).toBe(324);
    expect(reading!.secExpandedH).toBe(441);
    // In-flight frames exist: at least one sample strictly between the
    // endpoints on the way up AND on the way down (pre-fix: none — the
    // height jumped at the first sample).
    const openInFlight = reading!.openSamples.filter((s) => s.h > 324 && s.h < 441);
    const closeInFlight = reading!.closeSamples.filter((h) => h > 324 && h < 441);
    expect(openInFlight.length).toBeGreaterThan(0); // pre-fix: 0
    expect(closeInFlight.length).toBeGreaterThan(0); // pre-fix: 0
    // The band's opacity eases: at least one in-flight sample below 1 on
    // the entry (pre-fix: the band mounts at opacity 1 — every sample 1).
    const opInFlight = reading!.openSamples.filter((s) => s.op !== null && s.op < 1);
    expect(opInFlight.length).toBeGreaterThan(0); // pre-fix: 0
    // The end states + the unmount (the collapsed DOM returns to the
    // pre-fix node tree — the accordion count-0 pins hold).
    expect(reading!.collapsedAgainH).toBe(324);
    expect(reading!.bandCountAfter).toBe(0);
  });

  test("the drill-down census at 390 — the mobile indentation + the fully-expanded overflow guard (v44 F2a)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    const census = await page.evaluate(async () => {
      const leaf = (txt: string) =>
        [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) => (e.textContent || "").trim() === txt && e.children.length === 0,
        );
      const bdH = leaf("Net Zero Breakdown");
      const card = bdH ? (bdH.closest('div[class*="rounded-2xl"]') as HTMLElement | null) : null;
      if (!card) return null;
      const collapsedH = Math.round(card.getBoundingClientRect().height);
      const sec = [...card.querySelectorAll("button")].find((b) =>
        /Total Income/i.test(b.textContent || ""),
      ) as HTMLElement | null;
      if (!sec) return null;
      const sCs = getComputedStyle(sec);
      const section = { h: Math.round(sec.getBoundingClientRect().height), pad: sCs.padding };
      sec.click();
      await new Promise((r) => setTimeout(r, 500));
      const secExpandedH = Math.round(card.getBoundingClientRect().height);
      // The band: the non-button sibling; the inner indented content =
      // the deepest single-child chain from the band.
      const band = [...sec.parentElement!.children].find((c) => c !== sec) as HTMLElement | null;
      let inner = band;
      while (inner && inner.children.length === 1) inner = inner.children[0] as HTMLElement;
      const inCs = inner ? getComputedStyle(inner) : null;
      const indent = { ml: inCs?.marginLeft ?? null, mt: inCs?.marginTop ?? null };
      // The first category row + its expansion.
      const cat = [...card.querySelectorAll("button")].find(
        (b) => b.offsetParent !== null && /\$/.test(b.textContent || "") && !/Total|Net Balance/i.test(b.textContent || ""),
      ) as HTMLElement | null;
      if (!cat) return null;
      const catChrome = {
        h: Math.round(cat.getBoundingClientRect().height),
        pad: getComputedStyle(cat).padding,
        bg: getComputedStyle(cat).backgroundColor,
      };
      cat.click();
      await new Promise((r) => setTimeout(r, 500));
      const fullExpandedH = Math.round(card.getBoundingClientRect().height);
      // The sub + item rows under the opened category.
      const subArea = [...cat.parentElement!.children].find(
        (c) => c !== cat && c.getBoundingClientRect().height > 0,
      ) as HTMLElement | null;
      if (!subArea) return null;
      const rows = [...subArea.querySelectorAll("div")].filter((d) => {
        const cs = getComputedStyle(d);
        return cs.display === "flex" && d.children.length >= 2 && Math.round(d.getBoundingClientRect().height) >= 16;
      });
      const readRow = (row: HTMLElement) => {
        const label = [...row.querySelectorAll("span")].find((s) => {
          const t = (s.textContent || "").trim();
          return t.length > 1 && s.children.length === 0 && !/^\$/.test(t);
        });
        return {
          h: Math.round(row.getBoundingClientRect().height),
          pad: getComputedStyle(row).padding,
          bg: getComputedStyle(row).backgroundColor,
          font: getComputedStyle(row).fontSize,
          color: getComputedStyle(row).color,
          labelMaxW: label ? getComputedStyle(label).maxWidth : null,
          labelTrunc: label ? getComputedStyle(label).textOverflow : null,
        };
      };
      const subRow = rows.find((r) => getComputedStyle(r).backgroundColor !== "rgba(0, 0, 0, 0)");
      const itemRow = rows.filter((r) => getComputedStyle(r).backgroundColor === "rgba(0, 0, 0, 0)").pop();
      const footP = [...card.querySelectorAll("span")].find(
        (e) => /categor/i.test(e.textContent || "") && e.children.length === 0,
      );
      const footRow = footP ? (footP.closest("div") as HTMLElement | null) : null;
      return {
        collapsedH,
        secExpandedH,
        fullExpandedH,
        section,
        indent,
        cat: catChrome,
        sub: subRow ? readRow(subRow) : null,
        item: itemRow ? readRow(itemRow) : null,
        foot: footRow
          ? {
              h: Math.round(footRow.getBoundingClientRect().height),
              pad: getComputedStyle(footRow).padding,
              borderTop: getComputedStyle(footRow).borderTopWidth,
            }
          : null,
        sw: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The reference's measured 390 contract (exp-vp-v44.mjs, both sites):
    // the card 324→441→495 (the seed's arithmetic — the reference's own
    // 405/459 differ by DATA: its 1 category vs the seed's 2), the section
    // 48/8px, the inner indent ml 40px/mt 8px (the mobile indentation
    // arithmetic matches the 640 class — no responsive indent exists), and
    // every row's chrome byte-identical. sw stays 390 fully expanded (the
    // superset — the reference reads 395, its own horizontal-overflow bug).
    expect(census!.collapsedH).toBe(324);
    expect(census!.secExpandedH).toBe(441);
    expect(census!.fullExpandedH).toBe(495);
    expect(census!.section).toEqual({ h: 48, pad: "8px" });
    expect(census!.indent).toEqual({ ml: "40px", mt: "8px" });
    expect(census!.cat).toEqual({ h: 28, pad: "6px 12px", bg: "rgb(249, 250, 251)" });
    expect(census!.sub!.h).toBe(24);
    expect(census!.sub!.pad).toBe("4px 8px");
    expect(census!.sub!.bg).toBe("rgb(250, 250, 250)");
    expect(census!.item!.h).toBe(24);
    expect(census!.item!.pad).toBe("4px 8px");
    expect(census!.item!.font).toBe("12px");
    expect(census!.item!.color).toBe("rgb(156, 163, 175)");
    expect(census!.item!.labelMaxW).toBe("120px");
    expect(census!.item!.labelTrunc).toBe("ellipsis");
    expect(census!.foot!.h).toBe(29);
    expect(census!.foot!.pad).toBe("6px 12px");
    expect(census!.foot!.borderTop).toBe("1px");
    expect(census!.sw).toBe(390);
  });

  test("the drill-down census at 1280 — the section label's 2-line WRAP + the narrow-column chrome (v44 F2b)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    const census = await page.evaluate(async () => {
      const leaf = (txt: string) =>
        [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) => (e.textContent || "").trim() === txt && e.children.length === 0,
        );
      const bdH = leaf("Net Zero Breakdown");
      const card = bdH ? (bdH.closest('div[class*="rounded-2xl"]') as HTMLElement | null) : null;
      if (!card) return null;
      const cardW = Math.round(card.getBoundingClientRect().width);
      const collapsedH = Math.round(card.getBoundingClientRect().height);
      const sec = [...card.querySelectorAll("button")].find((b) =>
        /Total Income/i.test(b.textContent || ""),
      ) as HTMLElement | null;
      if (!sec) return null;
      const secLabel = [...sec.querySelectorAll("span")].find((s) =>
        /Total Income/i.test(s.textContent || ""),
      ) as HTMLElement | null;
      const section = {
        h: Math.round(sec.getBoundingClientRect().height),
        pad: getComputedStyle(sec).padding,
        labelH: secLabel ? Math.round(secLabel.getBoundingClientRect().height) : null,
      };
      sec.click();
      await new Promise((r) => setTimeout(r, 500));
      const secExpandedH = Math.round(card.getBoundingClientRect().height);
      const cat = [...card.querySelectorAll("button")].find(
        (b) => b.offsetParent !== null && /\$/.test(b.textContent || "") && !/Total|Net Balance/i.test(b.textContent || ""),
      ) as HTMLElement | null;
      if (!cat) return null;
      const catChrome = {
        h: Math.round(cat.getBoundingClientRect().height),
        pad: getComputedStyle(cat).padding,
        bg: getComputedStyle(cat).backgroundColor,
      };
      cat.click();
      await new Promise((r) => setTimeout(r, 500));
      const fullExpandedH = Math.round(card.getBoundingClientRect().height);
      const footP = [...card.querySelectorAll("span")].find(
        (e) => /categor/i.test(e.textContent || "") && e.children.length === 0,
      );
      const footRow = footP ? (footP.closest("div") as HTMLElement | null) : null;
      return {
        cardW,
        collapsedH,
        secExpandedH,
        fullExpandedH,
        section,
        cat: catChrome,
        foot: footRow
          ? {
              h: Math.round(footRow.getBoundingClientRect().height),
              borderTop: getComputedStyle(footRow).borderTopWidth,
            }
          : null,
        sw: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The reference's measured 1280 contract (exp-vp-v44.mjs, both sites):
    // the breakdown card sits in the NARROW 304px column, and its section
    // label "Total Income" WRAPS to two lines (labelH 40, row 56 — the
    // v42 collapsed census's 56 explained: width-driven wrap, present on
    // BOTH sites). The expansion arithmetic 364→481→535 is the seed's
    // (the reference's 364→445→499 differ by DATA).
    expect(census!.cardW).toBe(304);
    expect(census!.collapsedH).toBe(364);
    expect(census!.secExpandedH).toBe(481);
    expect(census!.fullExpandedH).toBe(535);
    expect(census!.section).toEqual({ h: 56, pad: "8px", labelH: 40 });
    expect(census!.cat).toEqual({ h: 28, pad: "6px 12px", bg: "rgb(249, 250, 251)" });
    expect(census!.foot!.h).toBe(29);
    expect(census!.foot!.borderTop).toBe("1px");
    expect(census!.sw).toBe(1280);
  });

  test("the donut legend census — the geometry chrome + the INERT hover (v44 F3)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    // The legend rows (v9 pinned the content contract: value-DESC order,
    // icons, amounts, percents, tinted bg — never the geometry). v44
    // measures the chrome: row h/pad/radius, the label/amount/pct fonts,
    // the dot, the gap, the container margin — byte-identical on both
    // sites (legend-v44.mjs at 390 AND 1280).
    const legend = page.locator("div.flex.flex-col.gap-3.mt-6");
    await expect(legend).toBeVisible();
    const rows = legend.locator("> div");
    await expect(rows).toHaveCount(3);

    // A REAL hover on the first row (the rows carry no mouse-following
    // tooltip — the donut's synthetic-hover lesson does not apply). The
    // reference's rows are inert: bg/shadow/cursor byte-identical under
    // the pointer (legend-v44.mjs: changed:false on BOTH sites).
    await rows.nth(0).hover();
    await page.waitForTimeout(300);
    const reading = await page.evaluate(() => {
      const legend = document.querySelector("div.flex.flex-col.gap-3.mt-6");
      const row = legend ? (legend.querySelector(":scope > div") as HTMLElement | null) : null;
      if (!row) return null;
      const cs = getComputedStyle(row);
      const label = [...row.querySelectorAll("span")].find((s) =>
        ["Need", "Want", "Savings"].includes((s.textContent || "").trim()),
      ) as HTMLElement | null;
      const amount = [...row.querySelectorAll("p,span")].find((s) =>
        /^\$\d/.test((s.textContent || "").trim()),
      ) as HTMLElement | null;
      const pct = [...row.querySelectorAll("p,span")].find((s) =>
        /^\d+(\.\d+)?%$/.test((s.textContent || "").trim()),
      ) as HTMLElement | null;
      const dot = [...row.querySelectorAll("div")].find((d) => {
        const w = Math.round(d.getBoundingClientRect().width);
        return !d.children.length && w > 0 && w <= 20;
      }) as HTMLElement | null;
      const icon = row.querySelector("svg");
      const secondRow = legend ? (legend.querySelectorAll(":scope > div")[1] as HTMLElement | null) : null;
      const gap = secondRow
        ? Math.round(secondRow.getBoundingClientRect().top - row.getBoundingClientRect().bottom)
        : null;
      const containerCs = legend ? getComputedStyle(legend) : null;
      return {
        row: {
          h: Math.round(row.getBoundingClientRect().height),
          pad: cs.padding,
          radius: cs.borderRadius,
          bg: cs.backgroundColor,
          cursor: cs.cursor,
          shadow: cs.boxShadow,
        },
        label: label
          ? {
              font: getComputedStyle(label).fontSize,
              weight: getComputedStyle(label).fontWeight,
              color: getComputedStyle(label).color,
            }
          : null,
        amount: amount
          ? {
              font: getComputedStyle(amount).fontSize,
              weight: getComputedStyle(amount).fontWeight,
              color: getComputedStyle(amount).color,
            }
          : null,
        pct: pct ? { font: getComputedStyle(pct).fontSize, color: getComputedStyle(pct).color } : null,
        dot: dot
          ? {
              w: Math.round(dot.getBoundingClientRect().width),
              radius: getComputedStyle(dot).borderRadius,
              bg: getComputedStyle(dot).backgroundColor,
            }
          : null,
        icon: icon
          ? {
              w: Math.round(icon.getBoundingClientRect().width),
              h: Math.round(icon.getBoundingClientRect().height),
            }
          : null,
        gap,
        containerMt: containerCs ? containerCs.marginTop : null,
        containerRowGap: containerCs ? containerCs.rowGap : null,
      };
    });
    expect(reading).not.toBeNull();
    // The reference's measured legend chrome (legend-v44.mjs at 1280 — the
    // 390 readings are identical except the row width, which is data):
    // h 64 (24px label line + 2×12px pad + 16px dot row), pad 12, radius
    // 8, the tinted rgb(245,248,245), cursor auto, NO shadow — under the
    // REAL hover too (inert divs on both sites: the queue's "legend
    // interaction" item resolved — no interaction states exist to match).
    expect(reading!.row).toEqual({
      h: 64,
      pad: "12px",
      radius: "8px",
      bg: "rgb(245, 248, 245)",
      cursor: "auto",
      shadow: "none",
    });
    expect(reading!.label).toEqual({ font: "16px", weight: "500", color: "rgb(26, 58, 46)" });
    expect(reading!.amount).toEqual({ font: "16px", weight: "700", color: "rgb(224, 122, 59)" });
    expect(reading!.pct).toEqual({ font: "12px", color: "rgb(107, 114, 128)" });
    expect(reading!.dot).toEqual({ w: 16, radius: "4px", bg: "rgb(224, 122, 59)" });
    expect(reading!.icon).toEqual({ w: 16, h: 16 });
    expect(reading!.gap).toBe(12);
    expect(reading!.containerMt).toBe("24px");
    expect(reading!.containerRowGap).toBe("12px");
  });
});

test.describe("drill-down chevron GLYPH swap (v44 — plan F4)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
  });

  test("the chevrons SWAP glyphs on expansion — chevron-down collapsed, chevron-up expanded, both levels (v44 F4)", async ({ page }) => {
    const reading = await page.evaluate(async () => {
      const leaf = (txt: string) =>
        [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) => (e.textContent || "").trim() === txt && e.children.length === 0,
        );
      const bdH = leaf("Net Zero Breakdown");
      const card = bdH ? (bdH.closest('div[class*="rounded-2xl"]') as HTMLElement | null) : null;
      if (!card) return null;
      const sec = [...card.querySelectorAll("button")].find((b) =>
        /Total Income/i.test(b.textContent || ""),
      ) as HTMLElement | null;
      if (!sec) return null;
      // The glyph reader: the chevron = the LAST svg in the row; the GLYPH
      // identity is the lucide class (the computed-style census CANNOT see
      // a glyph swap — rotate/transform read none while the icon flips:
      // the v44 lesson from the VLM-flag DOM verification).
      const readGlyph = (btn: HTMLElement) => {
        const svgs = [...btn.querySelectorAll("svg")];
        const chev = svgs[svgs.length - 1] as SVGElement | undefined;
        if (!chev) return null;
        return {
          cls: (chev.getAttribute("class") || ""),
          rotate: getComputedStyle(chev).rotate,
          h: Math.round(chev.getBoundingClientRect().height),
        };
      };
      const secCollapsed = readGlyph(sec);
      sec.click();
      await new Promise((r) => setTimeout(r, 500));
      const secExpanded = readGlyph(sec);
      const cat = [...card.querySelectorAll("button")].find(
        (b) => b.offsetParent !== null && /\$/.test(b.textContent || "") && !/Total|Net Balance/i.test(b.textContent || ""),
      ) as HTMLElement | null;
      if (!cat) return null;
      const catCollapsed = readGlyph(cat);
      cat.click();
      await new Promise((r) => setTimeout(r, 500));
      const catExpanded = readGlyph(cat);
      sec.click();
      await new Promise((r) => setTimeout(r, 500));
      const secRecollapsed = readGlyph(sec);
      return { secCollapsed, secExpanded, catCollapsed, catExpanded, secRecollapsed };
    });
    expect(reading).not.toBeNull();
    // The reference's measured contract (chev-glyph-v44.mjs, fresh queries
    // at every state on BOTH levels): the chevron is a GLYPH SWAP —
    // lucide-chevron-down when collapsed, lucide-chevron-up when expanded,
    // back to chevron-down on re-collapse — with rotate: none at EVERY
    // state (the v43 static-rotation finding was correct but incomplete:
    // the flip is the ICON, not the transform. The computed-style census
    // cannot see glyph swaps — read the svg's class).
    expect(reading!.secCollapsed!.cls).toContain("lucide-chevron-down");
    expect(reading!.secExpanded!.cls).toContain("lucide-chevron-up"); // pre-fix: chevron-down
    expect(reading!.secRecollapsed!.cls).toContain("lucide-chevron-down");
    expect(reading!.catCollapsed!.cls).toContain("lucide-chevron-down");
    expect(reading!.catExpanded!.cls).toContain("lucide-chevron-up"); // pre-fix: chevron-down
    // The sizes + the static rotation stay pinned (the v43 contract).
    expect(reading!.secExpanded!.h).toBe(14);
    expect(reading!.catExpanded!.h).toBe(12);
    expect(reading!.secExpanded!.rotate).toBe("none");
    expect(reading!.catExpanded!.rotate).toBe("none");
  });
});

// ---------------------------------------------------------------------------
// v45 — the category-level band animation + the quick-action hover shadow
// (plan F3, docs/remediation-plan-v45.md).
//
// The v44 F1 pin covers the SECTION-level Collapse; the NESTED
// (category-level) band shares the component but was unpinned. Measured
// live on the clone (the driver eval): the card ramps
// 441→453→463→479→484→491→493→495 on the category expand and
// 495→491→483→464→457→448→445→442→441 on the collapse — in-flight frames
// both directions, ~200ms (the reference's category-level contract is the
// v44 measurement: "the category level the same").
//
// Plus the quick-action card's hover:shadow-lg pin (the shadow-scale
// regression net — v4 kept v3's lg numerics; an upgrade that changes the
// scale must fail this). Measured on BOTH sites: the visible layers
// rgba(0,0,0,0.1) 0px 10px 15px -3px + rgba(0,0,0,0.1) 0px 4px 6px -4px,
// rest shadow none, the lead layers the accepted v10 class.
test.describe("category-level animation + quick-action hover shadow (v45 — plan F3)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
  });

  test("the category band ANIMATES — in-flight frames both directions at the nested level (v45 F3a)", async ({ page }) => {
    await page.setViewportSize({ width: 640, height: 960 });
    const reading = await page.evaluate(async () => {
      const leaf = (txt: string) =>
        [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) => (e.textContent || "").trim() === txt && e.children.length === 0,
        );
      const bdH = leaf("Net Zero Breakdown");
      const card = bdH ? (bdH.closest('div[class*="rounded-2xl"]') as HTMLElement | null) : null;
      if (!card) return null;
      const sec = [...card.querySelectorAll("button")].find((b) =>
        /Total Income/i.test(b.textContent || ""),
      ) as HTMLElement | null;
      if (!sec) return null;
      // Expand the section and settle (the v44 F1 arithmetic: 324 → 441).
      sec.click();
      await new Promise((r) => setTimeout(r, 600));
      const sectionExpandedH = Math.round(card.getBoundingClientRect().height);
      // The FIRST category row inside the expanded band (Salary).
      const catBtn = [...card.querySelectorAll("button")].find(
        (b) => /Salary/.test(b.textContent || "") && b !== sec,
      ) as HTMLElement | null;
      if (!catBtn) return { sectionExpandedH, catFound: false as const, catExpandedH: 0, openSamples: [] as number[], closeSamples: [] as number[], collapsedAgainH: 0 };
      // EXPAND the category: sample every ~25ms (fresh queries each
      // iteration — the v43 stale-node lesson).
      catBtn.click();
      const openSamples: number[] = [];
      for (let i = 0; i < 12; i++) {
        openSamples.push(Math.round(card.getBoundingClientRect().height));
        await new Promise((r) => setTimeout(r, 25));
      }
      const catExpandedH = Math.round(card.getBoundingClientRect().height);
      // COLLAPSE the category: sample again.
      catBtn.click();
      const closeSamples: number[] = [];
      for (let i = 0; i < 12; i++) {
        closeSamples.push(Math.round(card.getBoundingClientRect().height));
        await new Promise((r) => setTimeout(r, 25));
      }
      const collapsedAgainH = Math.round(card.getBoundingClientRect().height);
      return { sectionExpandedH, catExpandedH, openSamples, closeSamples, collapsedAgainH };
    });
    expect(reading).not.toBeNull();
    // The v44 arithmetic at 640: the section band 324→441, the category
    // band 441→495 (the seed's two subcategories under Salary).
    expect(reading!.sectionExpandedH).toBe(441);
    expect(reading!.catExpandedH).toBe(495);
    // In-flight frames at the NESTED level: at least one sample strictly
    // between the endpoints on the way up AND on the way down.
    const openInFlight = reading!.openSamples.filter((h) => h > 441 && h < 495);
    const closeInFlight = reading!.closeSamples.filter((h) => h > 441 && h < 495);
    expect(openInFlight.length).toBeGreaterThan(0);
    expect(closeInFlight.length).toBeGreaterThan(0);
    // The end states (the collapse returns to the section-expanded height).
    expect(reading!.collapsedAgainH).toBe(441);
  });

  test("the quick-action card's hover:shadow-lg — the visible layers (v45 F3b)", async ({ page }) => {
    const qa = page.getByRole("button", { name: /^Add Income$/ });
    await expect(qa).toBeVisible();
    const rest = await qa.evaluate((el) => getComputedStyle(el).boxShadow);
    expect(rest).toBe("none");
    // A REAL pointer hover (the hover-v43 idiom): shadow-lg engages — the
    // visible layers byte-identical to the reference's v3 shadow-lg (the
    // quick-action button carries no inline boxShadow, so the hover is
    // LIVE on both sites).
    await qa.hover();
    await page.waitForTimeout(400);
    const hovered = await qa.evaluate((el) => getComputedStyle(el).boxShadow);
    expect(hovered).toContain("rgba(0, 0, 0, 0.1) 0px 10px 15px -3px");
    expect(hovered).toContain("rgba(0, 0, 0, 0.1) 0px 4px 6px -4px");
  });
});

test.describe("donut legend mobile reflow census (v49 — plan F2)", () => {
  test("the legend's full chrome at 390 — the mobile reflow (v49 F2)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/");
    await expect(page.getByText("Spending Breakdown")).toBeVisible();
    // The settle pattern: the dashboard's seeded net-balance text (the
    // v42 idiom — the card title is a plain div, never a role=heading).
    await expect(page.getByText("+$2065.00")).toBeVisible();
    // The reference's measured 390 contract (ref-v49.sh leaf census —
    // the v44 F3 measured BOTH viewports but pinned only 1280; this pin
    // locks the mobile reflow). The row width 308 (NOT the reference's
    // 313): the reference's row rides its own 395 docSW overflow — the
    // documented superset-fix-#4 bug; the clone fits at 390.
    const census = await page.evaluate(() => {
      const legend = document.querySelector("div.flex.flex-col.gap-3.mt-6");
      if (!legend) return null;
      const lcs = getComputedStyle(legend);
      const row = legend.querySelector(":scope > div") as HTMLElement | null;
      if (!row) return null;
      const cs = getComputedStyle(row);
      const leaves = [...row.querySelectorAll("p, span, div")].filter(
        (el) => el.children.length === 0,
      ) as HTMLElement[];
      const dot = leaves.find((el) => {
        const w = Math.round(el.getBoundingClientRect().width);
        return w > 0 && w <= 20;
      });
      const label = row.querySelector("span");
      const amount = [...row.querySelectorAll("p")].find((s) =>
        /^\$\d/.test((s.textContent || "").trim()),
      ) as HTMLElement | null;
      const pct = [...row.querySelectorAll("p")].find((s) =>
        /^\d+(\.\d+)?%$/.test((s.textContent || "").trim()),
      ) as HTMLElement | null;
      const rightBlock = amount ? amount.parentElement : null;
      const svg = row.querySelector("svg");
      return {
        container: {
          display: lcs.display,
          dir: lcs.flexDirection,
          gap: lcs.gap,
          mt: lcs.marginTop,
          w: Math.round(legend.getBoundingClientRect().width),
        },
        row: {
          w: Math.round(row.getBoundingClientRect().width),
          h: Math.round(row.getBoundingClientRect().height),
          radius: cs.borderRadius,
          pad: cs.padding,
          bg: cs.backgroundColor,
        },
        dot: dot
          ? {
              w: Math.round(dot.getBoundingClientRect().width),
              h: Math.round(dot.getBoundingClientRect().height),
              radius: getComputedStyle(dot).borderRadius,
              bg: getComputedStyle(dot).backgroundColor,
            }
          : null,
        label: label
          ? {
              fs: getComputedStyle(label).fontSize,
              fw: getComputedStyle(label).fontWeight,
              color: getComputedStyle(label).color,
              text: label.textContent?.trim(),
            }
          : null,
        amount: amount
          ? {
              fs: getComputedStyle(amount).fontSize,
              fw: getComputedStyle(amount).fontWeight,
              color: getComputedStyle(amount).color,
            }
          : null,
        pct: pct
          ? { fs: getComputedStyle(pct).fontSize, fw: getComputedStyle(pct).fontWeight, color: getComputedStyle(pct).color }
          : null,
        rightAlign: rightBlock ? getComputedStyle(rightBlock).textAlign : null,
        svg: svg
          ? { w: Math.round(svg.getBoundingClientRect().width), color: getComputedStyle(svg).color }
          : null,
        sw: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The container: the column reflow with the 12px gap + the 24px top
    // margin (the clone's mt-6 flex flex-col gap-3 — the reference's
    // identical family).
    expect(census!.container).toEqual({
      display: "flex",
      dir: "column",
      gap: "12px",
      mt: "24px",
      w: 308,
    });
    // The row chrome: byte-identical (the h 64 = 24px label line + 2×12
    // pad + the 16px dot row).
    expect(census!.row).toEqual({
      w: 308,
      h: 64,
      radius: "8px",
      pad: "12px",
      bg: "rgb(245, 248, 245)",
    });
    // The Need row's dot: the orange 16×16 at radius 4.
    expect(census!.dot).toEqual({ w: 16, h: 16, radius: "4px", bg: "rgb(224, 122, 59)" });
    // The leaves: the label 16/500/forest; the amount 16/700/classified
    // (orange for Need); the pct 12/400/gray.
    expect(census!.label).toEqual({ fs: "16px", fw: "500", color: "rgb(26, 58, 46)", text: "Need" });
    expect(census!.amount).toEqual({ fs: "16px", fw: "700", color: "rgb(224, 122, 59)" });
    expect(census!.pct).toEqual({ fs: "12px", fw: "400", color: "rgb(107, 114, 128)" });
    expect(census!.rightAlign).toBe("right");
    expect(census!.svg).toEqual({ w: 16, color: "rgb(224, 122, 59)" });
    // The clone's superset no-overflow contract holds at 390.
    expect(census!.sw).toBe(390);
  });
});
