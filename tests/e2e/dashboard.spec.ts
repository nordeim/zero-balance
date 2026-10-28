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

// ---------------------------------------------------------------------------
// v50 — plan F3 (docs/remediation-plan-v50.md): the dashboard HERO's mobile
// reflow at 390. The v42 F2 pinned the hero grid at 640 (goalCard 316,
// breakdownCard 324@y=569, hero 664); the v50 pin locks the 390 reflow —
// measured live on the reference (ref-v50.sh — byte-identical on every
// visible axis):
//   the hero grid: 1 column / gap 24 / 2 children
//   the goal card: 358×316@y 253 / radius 16 / pad 32 / the 135deg forest
//     gradient / the shadow rgba(26,58,46,0.3) 0px 20px 60px
//   the breakdown card: 358×324 @ y 593 (the 24px rhythm: 253+316+24)
//   the internals: the icon circle 48×48 rgba(143,188,63,0.2) + the 24px
//     target icon at rgb(143,188,63); the H3 18/700/white/lh 28; the
//     sublabel 14/rgba(255,255,255,0.6); the allocation row (the label
//     14/rgba(255,255,255,0.8) + the pct 18/600/white); the track
//     12px/rgba(255,255,255,0.1)/9999px; the fill's 90deg orange status
//     gradient at 9999px; the balance box radius 12/pad 24/
//     rgba(255,255,255,0.05)/blur(10px); the label 14/0.6; the figure
//     30/700/white; the chip row: the flex gap-8 center + the span
//     16/600 rgb(245,169,98) + the svg color rgb(245,169,98) — both
//     sites' 20px svg squishes identically under the row's flex-shrink
//     (a shared data-pressure artifact, byte-identical).
// The reference's own card w 363 rides its 395 docSW overflow (the
// documented superset-fix-#4 family — the clone's 358 fits, docSW 390).
// ---------------------------------------------------------------------------
test.describe("dashboard hero mobile reflow census (v50 — plan F3)", () => {
  test("the hero's 390 reflow — the grid, the cards, the goal card's full internals", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/");
    await expect(page.getByRole("heading", { name: "NET ZERO GOAL" })).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate(() => {
      const h3 = [...document.querySelectorAll("h3")].find(
        (h) => (h.textContent || "").trim() === "NET ZERO GOAL",
      );
      if (!h3) return null;
      // walk up to the card: the radius-16 shadowed forest panel
      let card = h3.parentElement as HTMLElement | null;
      for (let i = 0; i < 12 && card; i++) {
        const cs = getComputedStyle(card);
        const r = card.getBoundingClientRect();
        if (r.width > 300 && r.width < 400 && r.height > 250 && cs.borderRadius !== "0px" && cs.boxShadow !== "none") break;
        card = card.parentElement as HTMLElement | null;
      }
      if (!card) return null;
      const csCard = getComputedStyle(card);
      const rCard = card.getBoundingClientRect();
      const grid = (card.parentElement as HTMLElement).parentElement!;
      const csG = getComputedStyle(grid);
      const cards = [...grid.children].map((c) => {
        const r = c.getBoundingClientRect();
        return { w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y) };
      });
      // internals
      const ic = [...card.querySelectorAll("div")].find((d) => {
        const cs = getComputedStyle(d);
        const r = d.getBoundingClientRect();
        return cs.borderRadius === "9999px" && r.width > 40 && r.width < 60;
      });
      const icSvg = ic ? ic.querySelector("svg") : null;
      const sub = [...card.querySelectorAll("p")].find((p) => /Income\s*=\s*Savings/i.test(p.textContent || ""));
      const alloc = [...card.querySelectorAll("span, p")].find(
        (s) => /allocation/i.test((s.textContent || "").trim()) && s.getBoundingClientRect().width < 160,
      );
      const pct = [...card.querySelectorAll("span, p")].find((s) =>
        /^[0-9.]+%$/.test((s.textContent || "").trim()),
      );
      const track = [...card.querySelectorAll("div")].find((d) => {
        const r = d.getBoundingClientRect();
        const cs = getComputedStyle(d);
        return r.height >= 10 && r.height <= 16 && cs.borderRadius === "9999px" && r.width > 200;
      });
      const fillEl = track && track.firstElementChild ? (track.firstElementChild as HTMLElement) : null;
      const balBox = [...card.querySelectorAll("div")].find((d) => {
        const cs = getComputedStyle(d);
        const r = d.getBoundingClientRect();
        return cs.borderRadius === "12px" && r.width > 200;
      });
      const balLabel = balBox
        ? [...balBox.querySelectorAll("p")].find((p) => /balance/i.test(p.textContent || ""))
        : null;
      const fig = balBox
        ? [...balBox.querySelectorAll("p, div, span")]
            .filter((x) => /^[-+]?\$[0-9]/.test((x.textContent || "").trim()))
            .pop()
        : null;
      // the chip: the flex row with the trending icon + the status span
      const chipBox = balBox
        ? [...balBox.children].find((c) => /Under Budget|Over Budget|Net Zero/i.test(c.textContent || ""))
        : null;
      const chipSvg = chipBox ? chipBox.querySelector("svg") : null;
      const chipSpan = chipBox
        ? [...(chipBox as HTMLElement).children].find((c) => c.tagName === "SPAN")
        : null;
      return {
        grid: {
          display: csG.display,
          cols: csG.gridTemplateColumns,
          gap: csG.gap,
          w: Math.round(grid.getBoundingClientRect().width),
          children: grid.children.length,
        },
        goalCard: {
          w: Math.round(rCard.width),
          h: Math.round(rCard.height),
          y: Math.round(rCard.y),
          radius: csCard.borderRadius,
          pad: csCard.padding,
          bg: csCard.backgroundImage,
          shadow: csCard.boxShadow,
        },
        cards,
        iconCircle: ic
          ? {
              w: Math.round(ic.getBoundingClientRect().width),
              h: Math.round(ic.getBoundingClientRect().height),
              bg: getComputedStyle(ic).backgroundColor,
              svg: icSvg
                ? {
                    w: Math.round(icSvg.getBoundingClientRect().width),
                    color: getComputedStyle(icSvg).color,
                  }
                : null,
            }
          : null,
        h3: {
          fs: getComputedStyle(h3).fontSize,
          fw: getComputedStyle(h3).fontWeight,
          color: getComputedStyle(h3).color,
          lh: getComputedStyle(h3).lineHeight,
        },
        sublabel: sub
          ? { fs: getComputedStyle(sub).fontSize, color: getComputedStyle(sub).color }
          : null,
        allocLabel: alloc
          ? { fs: getComputedStyle(alloc).fontSize, color: getComputedStyle(alloc).color }
          : null,
        pct: pct
          ? {
              fs: getComputedStyle(pct).fontSize,
              fw: getComputedStyle(pct).fontWeight,
              color: getComputedStyle(pct).color,
            }
          : null,
        track: track
          ? {
              w: Math.round(track.getBoundingClientRect().width),
              h: Math.round(track.getBoundingClientRect().height),
              bg: getComputedStyle(track).backgroundColor,
              radius: getComputedStyle(track).borderRadius,
            }
          : null,
        fill: fillEl
          ? {
              bg: getComputedStyle(fillEl).backgroundImage,
              radius: getComputedStyle(fillEl).borderRadius,
            }
          : null,
        balBox: balBox
          ? {
              w: Math.round(balBox.getBoundingClientRect().width),
              h: Math.round(balBox.getBoundingClientRect().height),
              radius: getComputedStyle(balBox).borderRadius,
              pad: getComputedStyle(balBox).padding,
              bg: getComputedStyle(balBox).backgroundColor,
              blur: getComputedStyle(balBox).backdropFilter,
            }
          : null,
        balLabel: balLabel
          ? { fs: getComputedStyle(balLabel).fontSize, color: getComputedStyle(balLabel).color }
          : null,
        figure: fig
          ? {
              fs: getComputedStyle(fig).fontSize,
              fw: getComputedStyle(fig).fontWeight,
              color: getComputedStyle(fig).color,
            }
          : null,
        chip: chipBox
          ? {
              display: getComputedStyle(chipBox).display,
              gap: getComputedStyle(chipBox).gap,
              svgColor: chipSvg ? getComputedStyle(chipSvg).color : null,
              span: chipSpan
                ? {
                    text: (chipSpan.textContent || "").trim(),
                    fs: getComputedStyle(chipSpan).fontSize,
                    fw: getComputedStyle(chipSpan).fontWeight,
                    color: getComputedStyle(chipSpan).color,
                  }
                : null,
            }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The hero grid: 1 column, the 24px gap, 2 children.
    expect(census!.grid.display).toBe("grid");
    expect(census!.grid.cols).toBe("358px");
    expect(census!.grid.gap).toBe("24px");
    expect(census!.grid.children).toBe(2);
    // The goal card: the reference's 316-tall forest panel (the
    // reference's 363 rides its own 395 overflow — the clone's 358 fits).
    expect(census!.goalCard.w).toBe(358);
    expect(census!.goalCard.h).toBe(316);
    expect(census!.goalCard.y).toBe(253);
    expect(census!.goalCard.radius).toBe("16px");
    expect(census!.goalCard.pad).toBe("32px");
    expect(census!.goalCard.bg).toContain("linear-gradient(135deg, rgb(26, 58, 46)");
    expect(census!.goalCard.shadow).toBe("rgba(26, 58, 46, 0.3) 0px 20px 60px 0px");
    // The 24px rhythm: the breakdown card at y 593 (253 + 316 + 24).
    expect(census!.cards).toEqual([
      { w: 358, h: 316, y: 253 },
      { w: 358, h: 324, y: 593 },
    ]);
    // The internals.
    expect(census!.iconCircle!.w).toBe(48);
    expect(census!.iconCircle!.h).toBe(48);
    expect(census!.iconCircle!.bg).toBe("rgba(143, 188, 63, 0.2)");
    expect(census!.iconCircle!.svg).toEqual({ w: 24, color: "rgb(143, 188, 63)" });
    expect(census!.h3).toEqual({ fs: "18px", fw: "700", color: "rgb(255, 255, 255)", lh: "28px" });
    expect(census!.sublabel).toEqual({ fs: "14px", color: "rgba(255, 255, 255, 0.6)" });
    expect(census!.allocLabel).toEqual({ fs: "14px", color: "rgba(255, 255, 255, 0.8)" });
    expect(census!.pct).toEqual({ fs: "18px", fw: "600", color: "rgb(255, 255, 255)" });
    expect(census!.track!.h).toBe(12);
    expect(census!.track!.bg).toBe("rgba(255, 255, 255, 0.1)");
    expect(census!.track!.radius).toBe("9999px");
    // The fill: the under-budget orange 90deg status gradient (the seed's
    // state — data-dependent, the gradient family is not).
    expect(census!.fill!.bg).toContain("linear-gradient(90deg, rgb(224, 122, 59)");
    expect(census!.fill!.radius).toBe("9999px");
    expect(census!.balBox!.radius).toBe("12px");
    expect(census!.balBox!.pad).toBe("24px");
    expect(census!.balBox!.bg).toBe("rgba(255, 255, 255, 0.05)");
    expect(census!.balBox!.blur).toBe("blur(10px)");
    expect(census!.balLabel).toEqual({ fs: "14px", color: "rgba(255, 255, 255, 0.6)" });
    expect(census!.figure).toEqual({ fs: "30px", fw: "700", color: "rgb(255, 255, 255)" });
    // The chip: the flex gap-8 row with the orange pair (the reference's
    // svg squishes identically — flex-shrink under the row's width
    // pressure, a byte-shared artifact).
    expect(census!.chip!.display).toBe("flex");
    expect(census!.chip!.gap).toBe("8px");
    expect(census!.chip!.svgColor).toBe("rgb(245, 169, 98)");
    expect(census!.chip!.span).toEqual({
      text: "Under Budget",
      fs: "16px",
      fw: "600",
      color: "rgb(245, 169, 98)",
    });
    // The clone's superset no-overflow contract at 390.
    expect(census!.docSW).toBe(390);
  });
});

// v51 (docs/remediation-plan-v51.md): the dashboard's remaining MOBILE
// surfaces at 390 — the stats row (F2), the Budget Guidelines card
// (F4), and the quick-actions row (F5), all measured live on BOTH
// sites at byte-parity (READ-ONLY on the reference). The widths ride
// the documented overflow family (the reference's 363 cards on its own
// 395 docSW; the clone's 358 fitting docSW 390); the heights and the
// vertical rhythm are byte-identical.
test.describe("mobile surface census at 390 (v51 — plan F2/F4/F5)", () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
  });

  test("the stats row — the three cards' grid, rhythm and full chrome (v51 F2)", async ({ page }) => {
    const census = await page.evaluate(() => {
      const h3 = [...document.querySelectorAll("h3")].find(
        (x) => (x.textContent || "").trim() === "Total Income",
      );
      if (!h3) return null;
      let card = h3 as HTMLElement;
      while (card && card.parentElement) {
        const p = card.parentElement;
        const statCards = [...p.children].filter((c) =>
          [...c.querySelectorAll("h3")].some((h) =>
            /^(Total Income|Total Savings|Total Expenses)$/.test(
              (h.textContent || "").trim(),
            ),
          ),
        );
        if (statCards.length >= 2) break;
        card = p as HTMLElement;
      }
      const grid = card.parentElement as HTMLElement;
      const csG = getComputedStyle(grid);
      const first = ([...grid.children].find((c) =>
        [...c.querySelectorAll("h3")].some(
          (h) => (h.textContent || "").trim() === "Total Income",
        ),
      ) as HTMLElement)!;
      const csC = getComputedStyle(first);
      const rC = first.getBoundingClientRect();
      const circle = [...first.querySelectorAll("div")].find((d) => {
        const r = d.getBoundingClientRect();
        return Math.abs(r.width - 48) < 1 && Math.abs(r.height - 48) < 1;
      }) as HTMLElement | undefined;
      const icon = first.querySelector("svg") as SVGSVGElement | null;
      const amount = [...first.querySelectorAll("p")].find((p) =>
        /^[-+]?[\$]?[0-9]/.test((p.textContent || "").trim()),
      ) as HTMLElement | undefined;
      const countRow = [...first.querySelectorAll("div")].find(
        (d) =>
          (d.textContent || "").includes("item") &&
          d.children.length > 0 &&
          getComputedStyle(d).display === "flex",
      ) as HTMLElement | undefined;
      const trend = [...first.querySelectorAll("svg")].pop() as
        | SVGSVGElement
        | undefined;
      return {
        grid: {
          display: csG.display,
          cols: csG.gridTemplateColumns,
          gap: csG.gap,
          children: grid.children.length,
        },
        cards: [...grid.children].map((c) => {
          const r = c.getBoundingClientRect();
          return { w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y) };
        }),
        card: {
          w: Math.round(rC.width),
          h: Math.round(rC.height),
          radius: csC.borderRadius,
          pad: csC.padding,
          border: csC.borderTopColor,
          bg: csC.backgroundColor,
          shadow: csC.boxShadow,
        },
        circle: circle
          ? {
              w: Math.round(circle.getBoundingClientRect().width),
              radius: getComputedStyle(circle).borderRadius,
              bg: getComputedStyle(circle).backgroundColor,
            }
          : null,
        icon: icon
          ? {
              w: Math.round(icon.getBoundingClientRect().width),
              color: getComputedStyle(icon).color,
            }
          : null,
        title: {
          fs: getComputedStyle(h3).fontSize,
          fw: getComputedStyle(h3).fontWeight,
          color: getComputedStyle(h3).color,
          mb: getComputedStyle(h3).marginBottom,
        },
        amount: amount
          ? {
              fs: getComputedStyle(amount).fontSize,
              fw: getComputedStyle(amount).fontWeight,
              color: getComputedStyle(amount).color,
              mb: getComputedStyle(amount).marginBottom,
            }
          : null,
        countRow: countRow
          ? {
              fs: getComputedStyle(countRow).fontSize,
              gap: getComputedStyle(countRow).gap,
              color: getComputedStyle(countRow).color,
            }
          : null,
        trend: trend
          ? { w: Math.round(trend.getBoundingClientRect().width) }
          : null,
      };
    });
    expect(census).not.toBeNull();
    // The grid: 1 column, 24px gap, three cards.
    expect(census!.grid).toEqual({
      display: "grid",
      cols: "358px",
      gap: "24px",
      children: 3,
    });
    // The 24px rhythm: 949 + 210 + 24 = 1183 + 210 + 24 = 1417 — the
    // y positions byte-identical on both sites (the reference's cards
    // at 949/1183/1417 with its own 363-wide cards on the 395 docSW).
    expect(census!.cards).toEqual([
      { w: 358, h: 210, y: 949 },
      { w: 358, h: 210, y: 1183 },
      { w: 358, h: 210, y: 1417 },
    ]);
    // The card chrome: radius 16 / pad 24 / the border / white / the
    // reference's own inline shadow family.
    expect(census!.card).toEqual({
      w: 358,
      h: 210,
      radius: "16px",
      pad: "24px",
      border: "rgb(229, 231, 227)",
      bg: "rgb(255, 255, 255)",
      shadow: "rgba(0, 0, 0, 0.06) 0px 4px 20px 0px",
    });
    // The 48px icon circle (radius 12, the income lime tint).
    expect(census!.circle).toEqual({
      w: 48,
      radius: "12px",
      bg: "rgba(143, 188, 63, 0.125)",
    });
    expect(census!.icon).toEqual({ w: 24, color: "rgb(143, 188, 63)" });
    // The title 14/500 gray mb-4; the amount 30/700 forestDark mb-4;
    // the count row 14px / gap 8px (the count TEXT is seed data).
    expect(census!.title).toEqual({
      fs: "14px",
      fw: "500",
      color: "rgb(107, 114, 128)",
      mb: "4px",
    });
    expect(census!.amount).toEqual({
      fs: "30px",
      fw: "700",
      color: "rgb(26, 58, 46)",
      mb: "16px",
    });
    expect(census!.countRow).toEqual({
      fs: "14px",
      gap: "8px",
      color: "rgb(10, 10, 10)",
    });
    expect(census!.trend).toEqual({ w: 16 });
  });

  test("the Budget Guidelines card — the card, the block tiles stack, the three tinted tiles (v51 F4)", async ({ page }) => {
    const census = await page.evaluate(() => {
      const heading = [...document.querySelectorAll("h1, h2, h3, div")].find(
        (x) => (x.textContent || "").trim() === "Budget Guidelines",
      ) as HTMLElement | undefined;
      if (!heading) return null;
      let card = heading as HTMLElement;
      while (
        card &&
        card.parentElement &&
        !(
          getComputedStyle(card).boxShadow !== "none" &&
          getComputedStyle(card).borderRadius &&
          card.querySelector("span, p")
        )
      )
        card = card.parentElement as HTMLElement;
      const csC = getComputedStyle(card);
      const rC = card.getBoundingClientRect();
      const tiles = [...card.querySelectorAll("div")].filter((d) => {
        const cs = getComputedStyle(d);
        const r = d.getBoundingClientRect();
        return (
          cs.borderRadius === "8px" &&
          r.height > 60 &&
          r.height < 200 &&
          d.querySelector("span, p") &&
          cs.backgroundColor !== "rgba(0, 0, 0, 0)"
        );
      }) as HTMLElement[];
      const grid = tiles.length
        ? (tiles[0]!.parentElement as HTMLElement)
        : null;
      return {
        card: {
          w: Math.round(rC.width),
          h: Math.round(rC.height),
          radius: csC.borderRadius,
          border: csC.borderTopColor,
          bg: csC.backgroundColor,
          shadow: csC.boxShadow,
        },
        grid: grid
          ? {
              display: getComputedStyle(grid).display,
              children: grid.children.length,
            }
          : null,
        tiles: tiles.slice(0, 3).map((t) => {
          const cs = getComputedStyle(t);
          const r = t.getBoundingClientRect();
          const label = t.querySelector("span") as HTMLElement;
          const pct = [...t.querySelectorAll("span")].pop() as HTMLElement;
          const desc = t.querySelector("p") as HTMLElement;
          return {
            w: Math.round(r.width),
            h: Math.round(r.height),
            radius: cs.borderRadius,
            pad: cs.padding,
            bg: cs.backgroundColor,
            border: cs.borderTopColor,
            label: {
              text: label.textContent!.trim().slice(0, 12),
              fs: getComputedStyle(label).fontSize,
              fw: getComputedStyle(label).fontWeight,
              color: getComputedStyle(label).color,
            },
            pct: {
              text: pct.textContent!.trim().slice(0, 8),
              fs: getComputedStyle(pct).fontSize,
              color: getComputedStyle(pct).color,
            },
            desc: {
              fs: getComputedStyle(desc).fontSize,
              color: getComputedStyle(desc).color,
            },
          };
        }),
      };
    });
    expect(census).not.toBeNull();
    // The card: 358×380, radius 12, the shadow's VISIBLE pair byte-
    // identical (the clone's 4 transparent leads vs the reference's 2 —
    // the accepted lead-divergence class, v10/v25/v45/v49/v50).
    expect(census!.card).toEqual({
      w: 358,
      h: 380,
      radius: "12px",
      border: "rgb(229, 231, 227)",
      bg: "rgb(255, 255, 255)",
      shadow:
        "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px",
    });
    // The tiles stack: display BLOCK (the space-y-3 stack, not a grid).
    expect(census!.grid).toEqual({ display: "block", children: 3 });
    // The three tiles: radius 8 / pad 16 / h 94, 94, 78 — the two-line
    // descs on Needs/Wants, the one-line on Savings.
    const [needs, wants, savings] = census!.tiles;
    expect(needs).toEqual({
      w: 308,
      h: 94,
      radius: "8px",
      pad: "16px",
      bg: "rgb(255, 247, 245)",
      border: "rgb(252, 221, 213)",
      label: { text: "Needs", fs: "16px", fw: "500", color: "rgb(224, 122, 59)" },
      pct: { text: "~50%", fs: "14px", color: "rgb(224, 122, 59)" },
      desc: { fs: "12px", color: "rgb(107, 114, 128)" },
    });
    expect(wants).toEqual({
      w: 308,
      h: 94,
      radius: "8px",
      pad: "16px",
      bg: "rgb(240, 247, 251)",
      border: "rgb(212, 233, 245)",
      label: { text: "Wants", fs: "16px", fw: "500", color: "rgb(59, 126, 161)" },
      pct: { text: "~30%", fs: "14px", color: "rgb(59, 126, 161)" },
      desc: { fs: "12px", color: "rgb(107, 114, 128)" },
    });
    expect(savings).toEqual({
      w: 308,
      h: 78,
      radius: "8px",
      pad: "16px",
      bg: "rgb(245, 249, 240)",
      border: "rgb(223, 236, 208)",
      label: { text: "Savings", fs: "16px", fw: "500", color: "rgb(143, 188, 63)" },
      pct: { text: "~20%", fs: "14px", color: "rgb(143, 188, 63)" },
      desc: { fs: "12px", color: "rgb(107, 114, 128)" },
    });
  });

  test("the quick-actions row — the three cards' grid, rhythm and full chrome (v51 F5)", async ({ page }) => {
    const census = await page.evaluate(() => {
      const btn = [...document.querySelectorAll("button")].find((b) =>
        (b.textContent || "").trim().startsWith("Add Income"),
      ) as HTMLElement | undefined;
      if (!btn) return null;
      const grid = btn.parentElement as HTMLElement;
      const csG = getComputedStyle(grid);
      const csC = getComputedStyle(btn);
      const rC = btn.getBoundingClientRect();
      // The circle is a SPAN in the clone (a DIV on the reference —
      // tag-agnostic, identical computed chrome).
      const circle = [...btn.querySelectorAll("span, div")].find((d) => {
        const r = d.getBoundingClientRect();
        return Math.abs(r.width - 40) < 1 && Math.abs(r.height - 40) < 1;
      }) as HTMLElement | undefined;
      const icon = btn.querySelector("svg") as SVGSVGElement | null;
      const label = [...btn.querySelectorAll("span, div")].find(
        (k) =>
          k.children.length === 0 && (k.textContent || "").trim() === "Add Income",
      ) as HTMLElement | undefined;
      const plus = [...btn.querySelectorAll("svg")].pop() as
        | SVGSVGElement
        | undefined;
      return {
        grid: {
          display: csG.display,
          cols: csG.gridTemplateColumns,
          gap: csG.gap,
          children: grid.children.length,
          mt: csG.marginTop,
        },
        cards: [...grid.children].map((c) => {
          const r = c.getBoundingClientRect();
          return { w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y) };
        }),
        card: {
          w: Math.round(rC.width),
          h: Math.round(rC.height),
          radius: csC.borderRadius,
          pad: csC.padding,
          border: csC.borderTopColor,
          bg: csC.backgroundColor,
          shadow: csC.boxShadow,
        },
        circle: circle
          ? {
              w: Math.round(circle.getBoundingClientRect().width),
              radius: getComputedStyle(circle).borderRadius,
              bg: getComputedStyle(circle).backgroundColor,
            }
          : null,
        icon: icon
          ? {
              w: Math.round(icon.getBoundingClientRect().width),
              color: getComputedStyle(icon).color,
            }
          : null,
        label: label
          ? {
              fs: getComputedStyle(label).fontSize,
              fw: getComputedStyle(label).fontWeight,
              color: getComputedStyle(label).color,
            }
          : null,
        plus: plus
          ? {
              w: Math.round(plus.getBoundingClientRect().width),
              opacity: getComputedStyle(plus).opacity,
              color: getComputedStyle(plus).color,
            }
          : null,
      };
    });
    expect(census).not.toBeNull();
    // The grid: 1 column, 24px gap, three cards, the mt-8 section gap.
    expect(census!.grid).toEqual({
      display: "grid",
      cols: "358px",
      gap: "24px",
      children: 3,
      mt: "32px",
    });
    // The 114px rhythm: 2751 + 90 + 24 = 2865 + 90 + 24 = 2979 — the
    // full-page vertical rhythm byte-identical through the whole
    // dashboard on both sites.
    expect(census!.cards).toEqual([
      { w: 358, h: 90, y: 2751 },
      { w: 358, h: 90, y: 2865 },
      { w: 358, h: 90, y: 2979 },
    ]);
    // The card chrome: radius 16 / pad 24 / the border / white / NO
    // shadow at rest (the hover adds shadow-lg — the transition family).
    expect(census!.card).toEqual({
      w: 358,
      h: 90,
      radius: "16px",
      pad: "24px",
      border: "rgb(229, 231, 227)",
      bg: "rgb(255, 255, 255)",
      shadow: "none",
    });
    // The 40px icon circle (radius 12, the income lime tint).
    expect(census!.circle).toEqual({
      w: 40,
      radius: "12px",
      bg: "rgba(143, 188, 63, 0.125)",
    });
    expect(census!.icon).toEqual({ w: 20, color: "rgb(143, 188, 63)" });
    // The label 16/500 forestDark; the trailing plus 16×16 at 50%
    // opacity in the accent color (the reference's own ml-auto
    // opacity-50 group-hover:opacity-100 idiom).
    expect(census!.label).toEqual({ fs: "16px", fw: "500", color: "rgb(26, 58, 46)" });
    expect(census!.plus).toEqual({ w: 16, opacity: "0.5", color: "rgb(143, 188, 63)" });
  });
});

test.describe("hero desktop 1280 census (v56 — plan F1)", () => {
  // The v56 pin (PIN-ONLY — no production change): the NET ZERO GOAL
  // card's DESKTOP 1280x800 state, measured byte-identical on BOTH sites
  // (scripts/parity-probes/hero-desk-v56.sh, the session-131 v56 queue's
  // desktop standing pair surface). The v50 F3 census pins the hero at
  // mobile 390; the v55 glyph census pins the stat-row/tile SHAPE data;
  // THIS pin locks the hero's desktop chrome geometry — the grid's
  // 304px triple-column template, the 632x316 goal panel with its 32px
  // pad and forest gradient + shadow, the 568x12 progress track, the
  // fill's 90deg status-gradient family + its pct-proportional width
  // (the reference's own fill: 173px = 30.5% x 568 — the arithmetic is
  // data-INDEPENDENT, the geometry is data-locked), and the 48px stat
  // tiles' 24x24 svgs.
  test("the goal card's desktop geometry + track + fill family + stat tiles (v56 F1)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();

    const census = await page.evaluate(() => {
      const h3 = [...document.querySelectorAll("h3")].find(
        (e) => (e.textContent || "").trim() === "NET ZERO GOAL",
      );
      if (!h3) return null;
      let card = h3.parentElement as HTMLElement | null;
      for (let i = 0; i < 12 && card; i++) {
        const cs = getComputedStyle(card);
        const r = card.getBoundingClientRect();
        if (r.width > 500 && r.height > 250 && cs.borderRadius !== "0px" && cs.boxShadow !== "none") break;
        card = card.parentElement as HTMLElement | null;
      }
      if (!card) return null;
      const csC = getComputedStyle(card);
      const rC = card.getBoundingClientRect();
      // The hero grid: the lg:grid-cols-3 wrapper (goal panel spans 2).
      const grid = (card.parentElement as HTMLElement).parentElement!;
      const csG = getComputedStyle(grid);
      const children = [...grid.children].map((c) => {
        const r = c.getBoundingClientRect();
        return { w: Math.round(r.width), h: Math.round(r.height), y: Math.round(r.y) };
      });
      // The progress track: the 12px rounded bar inside the card.
      const track = [...card.querySelectorAll("div")].find((d) => {
        const r = d.getBoundingClientRect();
        const cs = getComputedStyle(d);
        return r.height >= 10 && r.height <= 16 && cs.borderRadius === "9999px" && r.width > 200;
      });
      const fillEl = track && track.firstElementChild ? (track.firstElementChild as HTMLElement) : null;
      // The rendered pct figure (the allocation label's sibling).
      const pct = [...card.querySelectorAll("span, p")].find((s) =>
        /^[0-9.]+%$/.test((s.textContent || "").trim()),
      );
      // The stat-row icon tiles: the 48px squares carrying the 24x24
      // legacy glyphs (the v55 swap chrome).
      const main = card.closest("main");
      const tiles = main
        ? [...main.querySelectorAll("div")]
            .filter((d) => {
              const r = d.getBoundingClientRect();
              return Math.abs(r.width - 48) < 2 && Math.abs(r.height - 48) < 2;
            })
            .slice(0, 3)
            .map((d) => {
              const svg = d.querySelector("svg");
              return {
                w: Math.round(d.getBoundingClientRect().width),
                svg: svg ? Math.round(svg.getBoundingClientRect().width) : null,
              };
            })
        : [];
      return {
        grid: { cols: csG.gridTemplateColumns, gap: csG.gap, children },
        card: {
          w: Math.round(rC.width),
          h: Math.round(rC.height),
          radius: csC.borderRadius,
          pad: csC.padding,
          bg: csC.backgroundImage,
          shadow: csC.boxShadow,
        },
        track: track
          ? {
              w: Math.round(track.getBoundingClientRect().width),
              h: Math.round(track.getBoundingClientRect().height),
              bg: getComputedStyle(track).backgroundColor,
              radius: getComputedStyle(track).borderRadius,
            }
          : null,
        fill: fillEl
          ? {
              w: Math.round(fillEl.getBoundingClientRect().width),
              bg: getComputedStyle(fillEl).backgroundImage,
              radius: getComputedStyle(fillEl).borderRadius,
            }
          : null,
        pct: pct ? (pct.textContent || "").trim() : null,
        tiles,
      };
    });
    expect(census).not.toBeNull();
    // The hero grid: the 304px triple-column template, the 24px gap, and
    // the two children — the 632-wide goal panel (col-span-2) + the
    // 304-wide breakdown card, both 364 tall at y 136 (byte-identical on
    // both sites — hero-desk-v56.sh).
    expect(census!.grid.cols).toBe("304px 304px 304px");
    expect(census!.grid.gap).toBe("24px");
    expect(census!.grid.children).toEqual([
      { w: 632, h: 364, y: 136 },
      { w: 304, h: 364, y: 136 },
    ]);
    // The goal card: 632x316, radius 16, pad 32, the 135deg forest
    // gradient + the 26-58-46/0.3 shadow (byte-identical on both sites).
    expect(census!.card.w).toBe(632);
    expect(census!.card.h).toBe(316);
    expect(census!.card.radius).toBe("16px");
    expect(census!.card.pad).toBe("32px");
    expect(census!.card.bg).toContain("linear-gradient(135deg, rgb(26, 58, 46)");
    expect(census!.card.shadow).toBe("rgba(26, 58, 46, 0.3) 0px 20px 60px 0px");
    // The track: 568x12 at the white/10 tint, pill radius (the v56
    // arbitration's byte-identical finding — the VLM's "longer bar" flag
    // was the FILL's data-driven width, never the track).
    expect(census!.track!.w).toBe(568);
    expect(census!.track!.h).toBe(12);
    expect(census!.track!.bg).toBe("rgba(255, 255, 255, 0.1)");
    expect(census!.track!.radius).toBe("9999px");
    // The fill: the 90deg orange status-gradient family + the pill
    // radius (data-independent), and the DATA-INTEGRITY arithmetic —
    // the fill's width is pct/100 of the 568 track within ±2px (the
    // reference's own 173 = 30.5% x 568).
    expect(census!.fill!.bg).toContain("linear-gradient(90deg, rgb(224, 122, 59)");
    expect(census!.fill!.radius).toBe("9999px");
    expect(census!.pct).toMatch(/^[0-9.]+%$/);
    const pctNum = parseFloat((census!.pct || "0").replace("%", ""));
    const expectedFill = Math.round((pctNum / 100) * 568);
    expect(Math.abs(census!.fill!.w - expectedFill)).toBeLessThanOrEqual(2);
    // The stat tiles: three 48px squares each carrying a 24x24 svg (the
    // v55 legacy-glyph swap's chrome — the shapes pinned by the v55
    // glyph-parity spec, the tile geometry pinned here).
    expect(census!.tiles).toEqual([
      { w: 48, svg: 24 },
      { w: 48, svg: 24 },
      { w: 48, svg: 24 },
    ]);
  });
});

test.describe("drill-down sub/item-row census at 1280 (v60 — plan F2)", () => {
  // The v60 standing pair's pin: the drill-down's SUB + ITEM rows at the
  // 1280x800 pair viewport (the v43 F3 pin walks them at 640; the v44 F2b
  // 1280 pin walked the section/category/footer heights — the sub/item
  // chrome at 1280 unpinned until v60). Measured live on BOTH sites
  // (drill-census-ref-v60.sh + drill-census-clone-v60.sh + the
  // drill-itemdump-ref-v60.sh finder arbitration): byte-identical — the
  // sub row 24 / "4px 8px" / rgb(250,250,250) / the label 12px/400/
  // rgb(107,114,128); the item row 24 / "4px 8px" / 12px /
  // rgb(156,163,175) / the label maxW 120px + ellipsis. The reference's
  // own expansion heights 364→445→499 differ from the seed's
  // 364→481→535 by DATA (its one Salary category vs the seed's two).
  test("the sub + item rows' chrome at the pair viewport + the expansion controls (v60 F2)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();

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
      const subArea = [...cat.parentElement!.children].find(
        (c) => c !== cat && c.getBoundingClientRect().height > 0,
      ) as HTMLElement | null;
      if (!subArea) return null;
      // The v60 itemdump lesson: pin the REAL rows (justify-between +
      // py-1 px-2 — pad "4px 8px"), never the inner label-group divs
      // (gap-2/gap-1.5 wrappers, pad 0 — the reference-side census's
      // rows[last] false-negative class).
      const realRows = [...subArea.querySelectorAll("div")].filter((d) => {
        const cs = getComputedStyle(d);
        return (
          cs.display === "flex" &&
          cs.justifyContent === "space-between" &&
          cs.padding === "4px 8px" &&
          d.children.length >= 2
        );
      });
      const subRow = realRows.find((d) => getComputedStyle(d).backgroundColor === "rgb(250, 250, 250)") as HTMLElement | undefined;
      const itemRow = realRows.find((d) => getComputedStyle(d).backgroundColor === "rgba(0, 0, 0, 0)") as HTMLElement | undefined;
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
        sub: subRow
          ? {
              h: Math.round(subRow.getBoundingClientRect().height),
              pad: getComputedStyle(subRow).padding,
              bg: getComputedStyle(subRow).backgroundColor,
              labelFont: subLabel ? getComputedStyle(subLabel).fontSize : null,
              labelWeight: subLabel ? getComputedStyle(subLabel).fontWeight : null,
              labelColor: subLabel ? getComputedStyle(subLabel).color : null,
            }
          : null,
        item: itemRow
          ? {
              h: Math.round(itemRow.getBoundingClientRect().height),
              pad: getComputedStyle(itemRow).padding,
              color: getComputedStyle(itemRow).color,
              font: getComputedStyle(itemRow).fontSize,
              labelMaxW: itemLabel ? getComputedStyle(itemLabel).maxWidth : null,
              labelTrunc: itemLabel ? getComputedStyle(itemLabel).textOverflow : null,
            }
          : null,
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
    // The v44 F2b expansion controls re-asserted (the seed's deterministic
    // arithmetic; the reference's own 364→445→499 is the data class).
    expect(census!.cardW).toBe(304);
    expect(census!.collapsedH).toBe(364);
    expect(census!.secExpandedH).toBe(481);
    expect(census!.fullExpandedH).toBe(535);
    expect(census!.section).toEqual({ h: 56, pad: "8px", labelH: 40 });
    expect(census!.cat).toEqual({ h: 28, pad: "6px 12px", bg: "rgb(249, 250, 251)" });
    // THE v60 PIN — the sub row (the reference's own live values:
    // 24 / "4px 8px" / rgb(250,250,250) / 12px/400/rgb(107,114,128)).
    expect(census!.sub).toEqual({
      h: 24, pad: "4px 8px", bg: "rgb(250, 250, 250)",
      labelFont: "12px", labelWeight: "400", labelColor: "rgb(107, 114, 128)",
    });
    // THE v60 PIN — the item row (the reference's own live values:
    // 24 / "4px 8px" / 12px / rgb(156,163,175) / maxW 120px + ellipsis).
    expect(census!.item).toEqual({
      h: 24, pad: "4px 8px", color: "rgb(156, 163, 175)", font: "12px",
      labelMaxW: "120px", labelTrunc: "ellipsis",
    });
    expect(census!.foot).toEqual({ h: 29, borderTop: "1px" });
    expect(census!.sw).toBe(1280);
  });
});

// ---------------------------------------------------------------------------
// v61 — plan F2: the Budget Guidelines card census at 1280 (the pair
// viewport). The card chrome is byte-identical both sides (the v61
// census); the STRETCH contract is the F1 fix's pin: the reference's
// card sits at NATURAL height inside a stretched space-y-4 wrapper —
// the card never stretches to the row height (the clone's pre-v61 bug:
// the card itself stretched to 656 with ~308px of empty white body
// below the Savings tile).
// ---------------------------------------------------------------------------
test.describe("the Budget Guidelines card census at 1280 (v61 — plan F2)", () => {
  test("the card chrome + the NO-STRETCH contract + the tiles", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByText("Budget Guidelines")).toBeVisible();
    const census = await page.evaluate(() => {
      const heading = [...document.querySelectorAll("h1, h2, h3, div, span")].find(
        (x) => (x.textContent || "").trim() === "Budget Guidelines" && x.children.length === 0,
      );
      if (!heading) return null;
      // Walk up to the bordered card (shadow + radius + a <p> descendant).
      let card = heading as HTMLElement;
      while (card.parentElement) {
        const cs = getComputedStyle(card);
        if (cs.boxShadow !== "none" && cs.borderRadius !== "0px" && card.querySelector("p")) break;
        card = card.parentElement as HTMLElement;
      }
      // The row: the ancestor 2-col grid (the lg:grid-cols-2 row holding
      // the breakdown card + the guidelines column).
      let row = card.parentElement as HTMLElement;
      while (row) {
        const cls = (row.className || "").toString();
        if (/grid-cols-2/.test(cls) && row.children.length === 2) break;
        row = row.parentElement as HTMLElement;
      }
      const csC = getComputedStyle(card);
      const rC = card.getBoundingClientRect();
      const header = heading.parentElement as HTMLElement;
      const body = [...card.children].find((c) => c !== header) as HTMLElement | undefined;
      const tiles = [...card.querySelectorAll("div")].filter((d) => {
        const cs = getComputedStyle(d);
        const r = d.getBoundingClientRect();
        return (
          cs.borderRadius === "8px" && r.height > 40 && r.height < 200 &&
          d.querySelector("span, p") && cs.backgroundColor !== "rgba(0, 0, 0, 0)" && d !== card
        );
      }) as HTMLElement[];
      const lastTile = tiles[tiles.length - 1];
      return {
        card: {
          w: Math.round(rC.width), h: Math.round(rC.height),
          radius: csC.borderRadius, border: csC.borderTopColor,
          bg: csC.backgroundColor, shadow: csC.boxShadow,
        },
        header: {
          pad: getComputedStyle(header).padding,
          fs: getComputedStyle(heading).fontSize,
          fw: getComputedStyle(heading).fontWeight,
          color: getComputedStyle(heading).color,
        },
        body: body ? { pad: getComputedStyle(body).padding } : null,
        tileCount: tiles.length,
        firstTile: tiles[0]
          ? {
              w: Math.round(tiles[0].getBoundingClientRect().width),
              h: Math.round(tiles[0].getBoundingClientRect().height),
              radius: getComputedStyle(tiles[0]).borderRadius,
              pad: getComputedStyle(tiles[0]).padding,
              bg: getComputedStyle(tiles[0]).backgroundColor,
              border: getComputedStyle(tiles[0]).borderTopColor,
            }
          : null,
        // THE STRETCH CONTRACT — the F1 fix's pin.
        cardH: Math.round(rC.height),
        cardBottom: Math.round(rC.bottom),
        lastTileBottom: lastTile ? Math.round(lastTile.getBoundingClientRect().bottom) : null,
        rowH: row ? Math.round(row.getBoundingClientRect().height) : null,
      };
    });
    expect(census).not.toBeNull();
    expect(census!.tileCount).toBe(3);
    // The card chrome (the v61 census — byte-identical both sides).
    expect(census!.card.w).toBe(468);
    expect(census!.card.radius).toBe("12px");
    expect(census!.card.border).toBe("rgb(229, 231, 227)");
    expect(census!.card.bg).toBe("rgb(255, 255, 255)");
    expect(census!.card.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(census!.card.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(census!.header.pad).toBe("24px");
    expect(census!.header.fs).toBe("16px");
    expect(census!.header.fw).toBe("600");
    expect(census!.header.color).toBe("rgb(26, 58, 46)");
    expect(census!.body!.pad).toBe("0px 24px 24px");
    expect(census!.firstTile).toEqual({
      w: 418, h: 78, radius: "8px", pad: "16px",
      bg: "rgb(255, 247, 245)", border: "rgb(252, 221, 213)",
    });
    // THE STRETCH CONTRACT: the card at NATURAL height (the reference's
    // own 348 — the header 64 + the body 282 arithmetic; the GUIDELINE_ROWS
    // constant makes it deterministic)…
    expect(census!.cardH).toBe(348);
    // …the card's bottom sits exactly one body-pad (24px) below the last
    // tile — NO empty card body below the tiles (the ±1 is the subpixel
    // rounding of the two rects — the pre-fix value was 308+ — v61)…
    expect(census!.cardBottom - census!.lastTileBottom!).toBeGreaterThanOrEqual(24);
    expect(census!.cardBottom - census!.lastTileBottom!).toBeLessThanOrEqual(25);
    // …and the ROW (the 2-col grid) is taller than the card — the stretch
    // lives on the space-y-4 WRAPPER (the grid child), never the card.
    expect(census!.rowH!).toBe(656);
    expect(census!.rowH! - census!.cardH).toBe(308);
  });
});

// ---------------------------------------------------------------------------
// v61 — plan F3: the quick-action card row census at 1280 (the pair
// viewport). The v61 census measured the row byte-identical on both
// sites (grid 960 / 3×304 / gap 24; the cards 304×90 / radius 16 /
// pad 24; the tile 40×40 / radius 12 / the type tints; the icon 20;
// the label 16px/500/forestDark; the plus 16 / opacity 0.5). The label
// finder pins the LEAF span (exact text + zero element children) — a
// bare textContent match catches the row WRAPPER span (the v61 label
// lesson: the clone's wrapper read fw 400 / rgb(10,10,10) before the
// finder fix). The hover:shadow-lg layers are the v45 F3b pin.
// ---------------------------------------------------------------------------
test.describe("the quick-action card row census at 1280 (v61 — plan F3)", () => {
  test("the row grid + the three cards' chrome + the tile/icon/label/plus", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByRole("button", { name: "Add Income" })).toBeVisible();
    const census = await page.evaluate(() => {
      const qas = [...document.querySelectorAll("button")].filter(
        (b) => /^Add (Income|Savings|Expense)$/.test((b.textContent || "").trim()),
      ) as HTMLElement[];
      if (qas.length !== 3) return null;
      const grid = qas[0]!.parentElement as HTMLElement;
      const csG = getComputedStyle(grid);
      const cards = qas.map((b) => {
        const cs = getComputedStyle(b);
        const r = b.getBoundingClientRect();
        const tile = [...b.querySelectorAll("span, div")].find((s) => {
          const st = getComputedStyle(s);
          const sr = s.getBoundingClientRect();
          return (
            st.borderRadius === "12px" &&
            sr.width >= 30 && sr.width <= 60 && sr.height >= 30 && sr.height <= 60
          );
        }) as HTMLElement | undefined;
        // THE LEAF-SPAN FINDER (the v61 label lesson): the exact text +
        // zero element children — never the row wrapper.
        const label = [...b.querySelectorAll("span")].find(
          (s) =>
            /^Add (Income|Savings|Expense)$/.test((s.textContent || "").trim()) &&
            s.children.length === 0,
        ) as HTMLElement | undefined;
        const svgs = [...b.querySelectorAll("svg")];
        const icon = svgs[0] as SVGElement | undefined;
        const plus = svgs[svgs.length - 1] as SVGElement | undefined;
        return {
          text: (b.textContent || "").trim(),
          w: Math.round(r.width), h: Math.round(r.height),
          radius: cs.borderRadius, pad: cs.padding,
          bg: cs.backgroundColor, border: cs.borderTopColor,
          shadow: cs.boxShadow, textAlign: cs.textAlign,
          tile: tile
            ? {
                w: Math.round(tile.getBoundingClientRect().width),
                h: Math.round(tile.getBoundingClientRect().height),
                radius: getComputedStyle(tile).borderRadius,
                bg: getComputedStyle(tile).backgroundColor,
              }
            : null,
          icon: icon
            ? {
                w: Math.round(icon.getBoundingClientRect().width),
                h: Math.round(icon.getBoundingClientRect().height),
                color: getComputedStyle(icon).color,
              }
            : null,
          label: label
            ? {
                fs: getComputedStyle(label).fontSize,
                fw: getComputedStyle(label).fontWeight,
                color: getComputedStyle(label).color,
              }
            : null,
          plus: plus && svgs.length > 1
            ? {
                w: Math.round(plus.getBoundingClientRect().width),
                h: Math.round(plus.getBoundingClientRect().height),
                opacity: getComputedStyle(plus).opacity,
                color: getComputedStyle(plus).color,
              }
            : null,
        };
      });
      return {
        grid: {
          display: csG.display, template: csG.gridTemplateColumns,
          gap: csG.columnGap, w: Math.round(grid.getBoundingClientRect().width),
        },
        cards,
      };
    });
    expect(census).not.toBeNull();
    // The row grid (the v61 census — byte-identical both sides).
    expect(census!.grid).toEqual({
      display: "grid", template: "304px 304px 304px", gap: "24px", w: 960,
    });
    // The three cards (identical chrome; the accent trio per type).
    const expected = [
      { text: "Add Income", tint: "rgba(143, 188, 63, 0.125)", accent: "rgb(143, 188, 63)" },
      { text: "Add Savings", tint: "rgba(59, 126, 161, 0.125)", accent: "rgb(59, 126, 161)" },
      { text: "Add Expense", tint: "rgba(224, 122, 59, 0.125)", accent: "rgb(224, 122, 59)" },
    ];
    census!.cards.forEach((c, i) => {
      const e = expected[i]!;
      expect(c.text).toBe(e.text);
      expect(c.w).toBe(304);
      expect(c.h).toBe(90);
      expect(c.radius).toBe("16px");
      expect(c.pad).toBe("24px");
      expect(c.bg).toBe("rgb(255, 255, 255)");
      expect(c.border).toBe("rgb(229, 231, 227)");
      expect(c.shadow).toBe("none");
      expect(c.textAlign).toBe("left");
      expect(c.tile).toEqual({ w: 40, h: 40, radius: "12px", bg: e.tint });
      expect(c.icon).toEqual({ w: 20, h: 20, color: e.accent });
      expect(c.label).toEqual({ fs: "16px", fw: "500", color: "rgb(26, 58, 46)" });
      expect(c.plus).toEqual({ w: 16, h: 16, opacity: "0.5", color: e.accent });
    });
  });
});

// v62 — plan F2: the mobile header-subtitle block census at 390. The M2
// arbitration of the v62 VLM pair (the mobile dashboard full-page pair's
// one non-chrome flag — the VLM claimed the clone's subtitle wraps to a
// THIRD line) measured this surface live on BOTH sites: the wrap is
// IDENTICAL (2 lines, h 48, block h 92, top 121) — the VLM's claim was a
// perception artifact (the DOM census is the authority, the v61
// meta-lesson's inverse). The surface was never pinned: the desktop
// header test (above) asserts the subtitle's VISIBILITY only. This pin
// locks the mobile wrap outcome: the subtitle P (16px/400/gray-500,
// lh 24px, 2 lines, h 48) inside the header block DIV (h 92 = h1 36 +
// mb-2 8 + p 48) — the geometry both sites share. The WIDTH axis is
// deliberately NOT pinned: the reference renders its content column 5px
// wider (its own 395px docSW overflow, the R-bug-4 family) — the WRAP
// OUTCOME is the contract, not the absolute width.
test.describe("the mobile header-subtitle block census at 390 (v62 — plan F2)", () => {
  test.beforeEach(async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/dashboard");
    await expect(page.getByText("+$2065.00")).toBeVisible();
  });

  test("the subtitle P wraps to two 24px lines inside the 92px header block", async ({ page }) => {
    const census = await page.evaluate(() => {
      const h1 = [...document.querySelectorAll("h1")].find(
        (x) => (x.textContent || "").trim() === "Budget Dashboard",
      );
      if (!h1) return null;
      // v61 lesson: parentElement, never closest() — the h1's own block
      // is the immediate parent DIV (dashboard-view.tsx:927-934).
      const block = h1.parentElement as HTMLElement | null;
      if (!block) return null;
      const p = block.querySelector("p") as HTMLElement | null;
      if (!p) return null;
      const range = document.createRange();
      range.selectNodeContents(p);
      // The line rects are GLYPH boxes (~19px for a 16px font — the
      // font-metric content height), NOT the 24px line boxes: the wrap
      // rhythm lives in the DELTA between consecutive line tops (= the
      // line-height) and the P's total height (2 × lh).
      const lineRects = [...range.getClientRects()].filter(
        (r) => r.width > 1 && r.height > 1,
      );
      const lineTops = lineRects.map((r) => r.top);
      const csP = getComputedStyle(p);
      const rp = p.getBoundingClientRect();
      const rb = block.getBoundingClientRect();
      const csH1 = getComputedStyle(h1);
      const rh1 = h1.getBoundingClientRect();
      return {
        text: (p.textContent || "").trim(),
        p: {
          h: Math.round(rp.height),
          top: Math.round(rp.top),
          fs: csP.fontSize,
          fw: csP.fontWeight,
          color: csP.color,
          lh: csP.lineHeight,
          lines: lineRects.length,
          lineRhythm:
            lineTops.length === 2
              ? Math.round((lineTops[1] - lineTops[0]) * 10) / 10
              : null,
        },
        block: {
          h: Math.round(rb.height),
          top: Math.round(rb.top),
          display: getComputedStyle(block).display,
        },
        h1: {
          h: Math.round(rh1.height),
          fs: csH1.fontSize,
          fw: csH1.fontWeight,
          mb: csH1.marginBottom,
        },
      };
    });
    expect(census, "the header block finder (h1 → parentElement → p)").toBeTruthy();
    expect(census!.text).toBe("Track your income, savings, and expenses to achieve net zero");
    // The subtitle P: the reference's measured chrome, byte-identical.
    // lineRhythm = the delta between the two line tops — exactly the
    // 24px line-height (the glyph boxes themselves are ~19px font
    // metrics, an implementation detail deliberately not pinned).
    expect(census!.p).toEqual({
      h: 48,
      top: 121,
      fs: "16px",
      fw: "400",
      color: "rgb(107, 114, 128)",
      lh: "24px",
      lines: 2,
      lineRhythm: 24,
    });
    // The header block: h1 (36) + mb-2 (8) + p (48) = 92 — the exact
    // arithmetic both sites render at 390 (block top 77 + 36 + 8 = the
    // P's top 121).
    expect(census!.block).toEqual({ h: 92, top: 77, display: "block" });
    expect(census!.h1).toEqual({ h: 36, fs: "30px", fw: "700", mb: "8px" });
  });
});

test.describe("breakdown section-icon glyph + donut label chrome census at 1280 (v76 — plan F4)", () => {
  // The v76 re-run pair's pin: the never-pinned axes the arbitration
  // census (arbit-v76.sh PART A) measured byte-identical on BOTH sites at
  // 1280x800 — the Net Zero Breakdown card's INCOME-SECTION ICON CHIP (the
  // h-4 w-4 legacy TrendingUpIcon inside the section button's h-8 w-8
  // rounded-lg chip, limeGreen on the tinted 12.5% bg) and the DONUT
  // LABEL chrome. The existing pins cover around them: the v43 F2/v44
  // F1-F4 censuses pin the section rows' geometry/chevron glyph swap, the
  // v60 F2 pin the expanded sub/item rows, the v55 glyph census the
  // stat-tile SHAPE row, the v9 G1b contract the labelLineCount 0 + the
  // early test the sector fill order — NEVER the section icon's own
  // glyph signature, color, or viewBox, and never the donut label
  // elements' own count/fs/fill. The trend icon: the legacy
  // TrendingUpIcon's twin-polyline path in the 0 0 24 24 viewBox; the
  // donut labels: the percent formatter's text nodes inherit the
  // document defaults (16px/black), recharts rendering one label element
  // per sector + one grouping element — count 4 with the 3-sector seed.
  test("the breakdown card's income-section icon chip + the donut's label chrome (v76 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByText("Spending Breakdown")).toBeVisible();

    const census = await page.evaluate(() => {
      const out: Record<string, unknown> = {};
      // The breakdown card's income SECTION: the aria-expanded section
      // button (the same surface the arbitration census measured — its
      // statCards[0] finder resolved to this row on BOTH sites).
      const section = [...document.querySelectorAll("button[aria-expanded]")].find(
        (b) => /Total Income/.test(b.textContent || ""),
      );
      if (section) {
        const icons = [...section.querySelectorAll("svg")].filter((s) => {
          const r = s.getBoundingClientRect();
          return Math.round(r.width) === 16 && Math.round(r.height) === 16;
        });
        out.sectionIcons = icons.map((s) => {
          const r = s.getBoundingClientRect();
          const cs = getComputedStyle(s);
          return {
            w: Math.round(r.width),
            h: Math.round(r.height),
            color: cs.color,
            glyphSig: (s.innerHTML || "").replace(/\s+/g, " ").slice(0, 110),
            viewBox: s.getAttribute("viewBox"),
          };
        });
        // The chip that carries the icon (the h-8 w-8 rounded-lg tile).
        const chip = icons[0]?.parentElement ?? null;
        if (chip) {
          const chr = chip.getBoundingClientRect();
          const chcs = getComputedStyle(chip);
          out.iconChip = {
            w: Math.round(chr.width),
            h: Math.round(chr.height),
            radius: chcs.borderRadius,
            bg: chcs.backgroundColor,
          };
        }
      }
      // The donut labels: the recharts pie label text nodes (the sector
      // labels, the connector lines filtered out — the v9 G1b finder).
      const pieSvgs = [...document.querySelectorAll("svg")].filter((s) =>
        s.querySelector("[class*=recharts-pie-sector], [class*=recharts-pie-label]"),
      );
      if (pieSvgs.length) {
        const svg = pieSvgs[0];
        const labels = [...svg.querySelectorAll("[class*=recharts-pie-label]")].filter(
          (e) => !/line/i.test(e.getAttribute("class") || ""),
        );
        const labelLines = [...svg.querySelectorAll("[class*=recharts-pie-label-line]")];
        out.donutLabels = {
          count: labels.length,
          labelLineCount: labelLines.length,
          labelFs: labels.length ? getComputedStyle(labels[0]).fontSize : null,
          labelFill: labels.length ? getComputedStyle(labels[0]).fill : null,
          sectors: [...svg.querySelectorAll("[class*=recharts-pie-sector]")].length,
        };
      }
      return out;
    });

    // The income-section icon chip — the arbitration's own measured
    // values (the 16x16 twin-polyline trending-up, limeGreen, in the
    // 32x32 rounded-lg tinted chip).
    expect(census!.sectionIcons).toEqual([
      {
        w: 16,
        h: 16,
        color: "rgb(143, 188, 63)",
        glyphSig:
          '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"></polyline><polyline points="16 7 22 7 22 13"></polyline>',
        viewBox: "0 0 24 24",
      },
    ]);
    expect(census!.iconChip).toEqual({
      w: 32,
      h: 32,
      radius: "8px",
      bg: "rgba(143, 188, 63, 0.125)",
    });
    // The donut label chrome — the v9 G1b contract's axes extended.
    expect(census!.donutLabels).toEqual({
      count: 4,
      labelLineCount: 0,
      labelFs: "16px",
      labelFill: "rgb(0, 0, 0)",
      sectors: 3,
    });
  });
});

// ---------------------------------------------------------------------------
// v77 — plan F4: the Budget Guidelines card's interior-TEXT family + the
// quick-action icons' viewBox census at 1280 (the pair viewport). The v61
// F2 pin covers the card's box chrome + the FIRST tile + the STRETCH
// contract; the v51 F4 pin covers the tiles' text family at 390 ONLY.
// The never-pinned axes here: the header's lh + tracking, the tiles 2/3
// (Wants/Savings) chrome, ALL three tiles' label/pct/desc TEXT chrome at
// 1280 (the one-line-desc h-78 arithmetic — the v51 mobile twin's
// 94/94/78 contrast), and the quick-action icons' viewBox (the v76
// glyph-pin family's quick-action extension). The values are the
// arbit-v77.sh census's own measurements, byte-identical on both sides.
// The label leaf is the tile's FIRST span, the pct the LAST (no wrapper
// ambiguity in the guidelines tiles — the v61 label lesson's
// quick-action-only trap, re-confirmed by the v77 census delta).
// ---------------------------------------------------------------------------
test.describe("Budget Guidelines interior-text + quick-action icon viewBox census at 1280 (v77 — plan F4)", () => {
  test("the header typography + the three tiles' full chrome + the icons' viewBox", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByText("Budget Guidelines")).toBeVisible();
    const census = await page.evaluate(() => {
      const heading = [...document.querySelectorAll("h1, h2, h3, div, span")].find(
        (x) => (x.textContent || "").trim() === "Budget Guidelines" && x.children.length === 0,
      ) as HTMLElement | undefined;
      if (!heading) return null;
      let card = heading as HTMLElement;
      while (card.parentElement) {
        const cs = getComputedStyle(card);
        if (cs.boxShadow !== "none" && cs.borderRadius !== "0px" && card.querySelector("p")) break;
        card = card.parentElement as HTMLElement;
      }
      const header = heading.parentElement as HTMLElement;
      const tiles = [...card.querySelectorAll("div")].filter((d) => {
        const cs = getComputedStyle(d);
        const r = d.getBoundingClientRect();
        return (
          cs.borderRadius === "8px" && r.height > 40 && r.height < 200 &&
          d.querySelector("span, p") && cs.backgroundColor !== "rgba(0, 0, 0, 0)" && d !== card
        );
      }) as HTMLElement[];
      const qas = [...document.querySelectorAll("button")].filter(
        (b) => /^Add (Income|Savings|Expense)$/.test((b.textContent || "").trim()),
      ) as HTMLElement[];
      return {
        header: {
          pad: getComputedStyle(header).padding,
          fs: getComputedStyle(heading).fontSize,
          fw: getComputedStyle(heading).fontWeight,
          color: getComputedStyle(heading).color,
          lh: getComputedStyle(heading).lineHeight,
          tracking: getComputedStyle(heading).letterSpacing,
        },
        tileCount: tiles.length,
        tiles: tiles.map((t) => {
          const cs = getComputedStyle(t);
          const r = t.getBoundingClientRect();
          const label = t.querySelector("span") as HTMLElement | null;
          const pct = [...t.querySelectorAll("span")].pop() as HTMLElement | undefined;
          const desc = t.querySelector("p") as HTMLElement | null;
          return {
            w: Math.round(r.width),
            h: Math.round(r.height),
            radius: cs.borderRadius,
            pad: cs.padding,
            bg: cs.backgroundColor,
            border: cs.borderTopColor,
            label: label
              ? {
                  text: (label.textContent || "").trim().slice(0, 10),
                  fs: getComputedStyle(label).fontSize,
                  fw: getComputedStyle(label).fontWeight,
                  color: getComputedStyle(label).color,
                }
              : null,
            pct: pct
              ? {
                  text: (pct.textContent || "").trim().slice(0, 8),
                  fs: getComputedStyle(pct).fontSize,
                  fw: getComputedStyle(pct).fontWeight,
                  color: getComputedStyle(pct).color,
                }
              : null,
            desc: desc
              ? {
                  fs: getComputedStyle(desc).fontSize,
                  color: getComputedStyle(desc).color,
                  lh: getComputedStyle(desc).lineHeight,
                }
              : null,
          };
        }),
        qaIcons: qas.map((b) => {
          const svg = b.querySelector("svg") as SVGElement | null;
          return svg ? svg.getAttribute("viewBox") || "" : null;
        }),
      };
    });
    expect(census).not.toBeNull();
    // The header's full typography — the lh (leading-none) + tracking
    // (tracking-tight) never pinned before v77.
    expect(census!.header).toEqual({
      pad: "24px",
      fs: "16px",
      fw: "600",
      color: "rgb(26, 58, 46)",
      lh: "16px",
      tracking: "-0.4px",
    });
    // The three tiles' full census at 1280 (the v51 F4 family's desktop
    // twin — the one-line descs at the 418px width, h 78 each; the mobile
    // twin's 94/94/78 two-line arithmetic is the v51 pin's own).
    expect(census!.tileCount).toBe(3);
    const expectedTiles = [
      {
        w: 418, h: 78, radius: "8px", pad: "16px",
        bg: "rgb(255, 247, 245)", border: "rgb(252, 221, 213)",
        label: { text: "Needs", fs: "16px", fw: "500", color: "rgb(224, 122, 59)" },
        pct: { text: "~50%", fs: "14px", fw: "400", color: "rgb(224, 122, 59)" },
        desc: { fs: "12px", color: "rgb(107, 114, 128)", lh: "16px" },
      },
      {
        w: 418, h: 78, radius: "8px", pad: "16px",
        bg: "rgb(240, 247, 251)", border: "rgb(212, 233, 245)",
        label: { text: "Wants", fs: "16px", fw: "500", color: "rgb(59, 126, 161)" },
        pct: { text: "~30%", fs: "14px", fw: "400", color: "rgb(59, 126, 161)" },
        desc: { fs: "12px", color: "rgb(107, 114, 128)", lh: "16px" },
      },
      {
        w: 418, h: 78, radius: "8px", pad: "16px",
        bg: "rgb(245, 249, 240)", border: "rgb(223, 236, 208)",
        label: { text: "Savings", fs: "16px", fw: "500", color: "rgb(143, 188, 63)" },
        pct: { text: "~20%", fs: "14px", fw: "400", color: "rgb(143, 188, 63)" },
        desc: { fs: "12px", color: "rgb(107, 114, 128)", lh: "16px" },
      },
    ];
    census!.tiles.forEach((t, i) => {
      expect(t).toEqual(expectedTiles[i]);
    });
    // The quick-action icons' viewBox — the v76 glyph-pin family's
    // quick-action extension (the w/h/color are the v61 F3 pin's own).
    expect(census!.qaIcons).toEqual(["0 0 24 24", "0 0 24 24", "0 0 24 24"]);
  });
});

// ---------------------------------------------------------------------------
// v78 — plan F4: the Net Zero Breakdown card's mobile SVG family +
// chart-absence + width census at 390 (the mobile-twins re-run pair's
// pin). The v44 F2a pin covers the card's HEIGHTS at 390 (324 collapsed /
// 441 / 495 expanded + the section/indent/cat geometry); the v76 pin the
// section icon chip at 1280; the v62 pin the subtitle block; the v49/v50/
// v51 families the donut legend / hero / stats / guidelines / quick
// actions. The NEVER-pinned axes here (the arbit-v78.sh census's own
// measurements, byte-identical on BOTH sides at 390x844): the card's
// WIDTH 358 (the 390 − 2×16 page-padding arithmetic), the SVG FAMILY —
// svgCount 7 with the full size census [16,14,16,14,16,14,16] (the three
// section icons h-4 w-4 + the three collapsed chevrons h-3.5 w-3.5 + the
// net-balance icon h-4 w-4) — the CHART-ABSENCE contract
// (rechartsWrappers 0 + pieSectors 0: no donut exists in the breakdown
// card on EITHER side — the v69 donut-invention lesson's regression
// guard; the VLM claimed a "faint circle behind the text" that the DOM
// disproved), and the children's width family (the H3 308×20 + the
// content DIV 308×238 — the 358 − 2×1 border − 2×24 p-6 arithmetic).
// The card finder is the arbitration's own: the 'Net Zero Breakdown'
// leaf heading → the 6-parent radius/white walk.
// ---------------------------------------------------------------------------
test.describe("breakdown card mobile svg + chart-absence + width census at 390 (v78 — plan F4)", () => {
  test("the card's mobile box + the svg size family + the no-donut contract + the children widths", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/dashboard");
    await expect(page.getByText("Net Zero Breakdown")).toBeVisible();
    // Let the collapsed drill-down settle (the expansion state is the
    // default collapsed surface the arbitration measured).
    await expect(page.getByText("+$2065.00")).toBeVisible();

    const census = await page.evaluate(() => {
      // The arbitration's own card finder: the heading leaf, then the
      // 6-parent radius/white walk (arbit-v78.sh's DASH_CENSUS).
      const bd = [...document.querySelectorAll("h1, h2, h3, h4")].find(
        (e) => (e.textContent || "").trim() === "Net Zero Breakdown",
      );
      if (!bd) return null;
      let card: HTMLElement | null = bd as HTMLElement;
      for (let i = 0; i < 6; i++) {
        card = card!.parentElement as HTMLElement | null;
        if (!card) break;
        const s = getComputedStyle(card);
        if ((s.borderRadius && s.borderRadius !== "0px") || s.backgroundColor === "rgb(255, 255, 255)") break;
      }
      if (!card) return null;
      const cr = card.getBoundingClientRect();
      const svgs = [...card.querySelectorAll("svg")].map((s) => {
        const r = s.getBoundingClientRect();
        return { w: Math.round(r.width), h: Math.round(r.height) };
      });
      return {
        docSW: document.documentElement.scrollWidth,
        card: { w: Math.round(cr.width), h: Math.round(cr.height) },
        svgCount: svgs.length,
        svgs: svgs.map((s) => [s.w, s.h] as [number, number]),
        rechartsWrappers: card.querySelectorAll(".recharts-wrapper").length,
        pieSectors: card.querySelectorAll(".recharts-pie-sector").length,
        children: [...card.children].map((c) => {
          const r = c.getBoundingClientRect();
          return { tag: c.tagName, w: Math.round(r.width), h: Math.round(r.height) };
        }),
      };
    });
    expect(census, "the breakdown card finder (the heading leaf → the radius/white walk)").not.toBeNull();
    if (!census) throw new Error("breakdown census found no card");

    // The card's mobile box — the arbitration's own measured values
    // (the w never pinned at 390; the h re-asserts the v44 contract).
    expect(census.docSW).toBe(390);
    expect(census.card).toEqual({ w: 358, h: 324 });

    // The SVG FAMILY — svgCount 7 with the full size census: the three
    // section icons (16×16) + the three collapsed chevrons (14×14) + the
    // net-balance icon (16×16), in DOM order.
    expect(census.svgCount).toBe(7);
    expect(census.svgs).toEqual([
      [16, 16], [14, 14], [16, 16], [14, 14], [16, 16], [14, 14], [16, 16],
    ]);

    // The CHART-ABSENCE contract — no recharts wrapper, no pie sector
    // inside the breakdown card on EITHER side (the v69 lesson's guard:
    // a chart-presence claim needs this census, never a screenshot read).
    expect(census.rechartsWrappers).toBe(0);
    expect(census.pieSectors).toBe(0);

    // The children's width family — the H3 (308×20) + the content DIV
    // (308×238): the 358 − 2×1 border − 2×24 p-6 arithmetic.
    expect(census.children).toEqual([
      { tag: "H3", w: 308, h: 20 },
      { tag: "DIV", w: 308, h: 238 },
    ]);
  });
});

// ---------------------------------------------------------------------------
// v83 — plan F4: the dashboard's CROSS-ROW vertical-rhythm census at 1280
// (the pair viewport). The v83 re-run pair's pin: the never-pinned PART X
// family — the vertical rhythm ACROSS the two below-the-fold rows (the
// guidelines card → the quick-action grid). The v61 F2 pin holds the
// guidelines card's box chrome + the STRETCH contract (cardH 348,
// cardBottom−lastTileBottom 24–25, rowH 656); the v61 F3 pin holds the
// quick-action grid's {display/template/gap/w} + the cards' chrome; the
// v77 pin holds the interior-text family; the v51 F5 pin holds the grid's
// mt "32px" at 390 ONLY. The never-pinned axes here: the guidelines
// card's BOTTOM (1122 — the cumulative upstream rhythm), the grid's TOP
// (1462), the RENDERED cross-row GAP (340 — the byte-identical both-sides
// parity axis: the reference achieves the same 340 through its own wrapper
// structure; the clone through the wrapper stretch 308 + the grid's mt-8
// 32px), and the grid's OWN mt at 1280 (the v51 F5 390 axis's desktop
// twin). The values are the arbit-v83.sh PART X census's own measurements,
// byte-identical on both sides.
// ---------------------------------------------------------------------------
test.describe("the dashboard cross-row vertical-rhythm census at 1280 (v83 — plan F4)", () => {
  test("the guidelines card's bottom + the quick-action grid's top + the rendered gap + the grid's mt", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByText("Budget Guidelines")).toBeVisible();

    const census = await page.evaluate(() => {
      const heading = [...document.querySelectorAll("h1, h2, h3, div, span")].find(
        (x) => (x.textContent || "").trim() === "Budget Guidelines" && x.children.length === 0,
      );
      if (!heading) return null;
      // The guidelines card (the v61 F2 walk: shadow + radius + a <p>).
      let card = heading as HTMLElement;
      while (card.parentElement) {
        const cs = getComputedStyle(card);
        if (cs.boxShadow !== "none" && cs.borderRadius !== "0px" && card.querySelector("p")) break;
        card = card.parentElement as HTMLElement;
      }
      // The quick-action grid: the parent of the Add Income button.
      const btn = [...document.querySelectorAll("button")].find((b) =>
        (b.textContent || "").trim() === "Add Income",
      );
      if (!btn) return null;
      const grid = btn.parentElement as HTMLElement;
      const rG = grid.getBoundingClientRect();
      const rC = card.getBoundingClientRect();
      return {
        cardBottom: Math.round(rC.bottom),
        gridTop: Math.round(rG.top),
        gap: Math.round(rG.top - rC.bottom),
        gridMt: getComputedStyle(grid).marginTop,
      };
    });
    expect(census, "the cross-row census finder (the guidelines heading + the Add Income button)").not.toBeNull();
    if (!census) throw new Error("cross-row census found no card or grid");

    // The guidelines card's BOTTOM — the cumulative upstream rhythm
    // (the hero + breakdown + stat rows + the guidelines row's own
    // 656 stretch, all upstream-pinned — this is their sum).
    expect(census.cardBottom).toBe(1122);

    // The quick-action grid's TOP — cardBottom 1122 + the wrapper
    // stretch 308 + the grid's mt-8 32px.
    expect(census.gridTop).toBe(1462);

    // The RENDERED cross-row gap — the byte-identical both-sides parity
    // axis (the reference's own wrapper mechanism produces the same 340).
    expect(census.gap).toBe(340);

    // The grid's OWN mt at 1280 — the v51 F5 390 axis's desktop twin
    // (the clone's mechanism axis).
    expect(census.gridMt).toBe("32px");
  });
});

// ---------------------------------------------------------------------------
// v88 — plan F4 (docs/remediation-plan-v88.md): the stat cards' COUNT-ROW
// + DIVIDER census at 1280.
//
// The v88 arbitration (arbit-v88.sh + stat-divider-arbit-v88.sh, the
// v82-era pair's fourth re-run) measured a never-pinned family: the stat
// card count row's full chrome + the h-px flex-1 DIVIDER between the
// "N items" text and the trend icon + the trend icon's per-type color.
// The v51 F2 pin holds the stats row at 390 only (the countRow fs/gap/
// color — never the divider, never the row's display/alignItems/height,
// never the trend icon's color); the v40 F1 pin holds the 1280 geometry
// bands + the role/tabindex census — never the count-row chrome;
// grep-verified: NO spec asserts the stat-card divider's height/bg/
// flexGrow at ANY viewport. The v88 cycle's own context: the VLM flagged
// the divider as "missing in the reference" — the stat-divider-arbit-v88.sh
// both-sides census disproved the claim (the divider renders
// BYTE-IDENTICALLY on both sides: {DIV, h 1px, bg rgb(229,231,227),
// flexGrow 1} on every card — a VLM MISREAD of the faint 1px line's
// visibility). The divider's WIDTH is EXCLUDED (the flex-1
// data-conditional remainder — the v82 labelBlock-width convention).
//
// Every pinned axis STATIC chrome (the row's classes and the divider's
// height/flex/background unconditional; the trend colors per-card
// constants); the pin rides the plain authenticated dashboard view on
// the e2e seed — read-only, no fixture writes.
// ---------------------------------------------------------------------------
interface StatRowCensus {
  title?: string;
  itemsText?: string;
  err?: string;
  row?: { h: number; display: string; gap: string; alignItems: string; fs: string; color: string };
  divider?: { tag: string; h: string; bg: string; flexGrow: string } | null;
  trend?: { w: number; h: number; color: string } | null;
}
interface StatCardsCensus {
  cards: number;
  rows: StatRowCensus[];
  docSW: number;
}
test.describe("stat-card count-row + divider census at 1280 (v88 — plan F4)", () => {
  test("the count row's chrome + the h-px divider + the trend icon's per-type colors — the never-pinned family", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/");
    await expect(page.getByText("Net Zero Breakdown")).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate((): StatCardsCensus => {
      // The three stat cards: rounded-2xl cards with a "Total X" h3 +
      // svgs (the geometry + text-content finder — the v87
      // name-independent-finder lesson; never class or name selectors).
      const cards = [...document.querySelectorAll("div")].filter((d) => {
        if (!d.className || typeof d.className !== "string") return false;
        if (!d.className.includes("rounded-2xl")) return false;
        const h3s = [...d.querySelectorAll("h3")];
        const hasTitle = h3s.some((h) =>
          /^(Total Income|Total Savings|Total Expenses)/i.test((h.textContent || "").trim()),
        );
        const r = d.getBoundingClientRect();
        return hasTitle && r.width > 200 && r.width < 500 && r.height > 150 && d.querySelectorAll("svg").length > 0;
      });
      if (cards.length < 3)
        return { cards: cards.length, rows: [], docSW: document.documentElement.scrollWidth };
      return {
        cards: cards.length,
        rows: cards.slice(0, 3).map((card) => {
          const title = ([...card.querySelectorAll("h3")].find((h) => /^Total /i.test((h.textContent || "").trim())) || {}).textContent;
          // The count row: the flex row containing the "N items" text leaf.
          const itemsText = [...card.querySelectorAll("span, p")].find(
            (e) => /^\d+ items?$/.test((e.textContent || "").trim()) && e.children.length === 0,
          );
          if (!itemsText) return { title, err: "no items text" };
          const row = (itemsText.closest("div.flex") || itemsText.parentElement) as HTMLElement;
          const rr = row.getBoundingClientRect();
          const rcs = getComputedStyle(row);
          // The divider: the structural middle child — not the items-text
          // span, not the trend svg (the finder never filters on the
          // height axis it is about to assert — the v87 lesson).
          const kids = [...row.children] as HTMLElement[];
          const divider = kids.find((k) => k !== itemsText && k.tagName !== "svg") || null;
          const trendSvg = row.querySelector("svg");
          const dcs = divider ? getComputedStyle(divider) : null;
          return {
            title,
            itemsText: (itemsText.textContent || "").trim(),
            row: {
              h: Math.round(rr.height),
              display: rcs.display,
              gap: rcs.gap,
              alignItems: rcs.alignItems,
              fs: rcs.fontSize,
              color: rcs.color,
            },
            divider: divider
              ? {
                  tag: divider.tagName,
                  h: dcs!.height,
                  bg: dcs!.backgroundColor,
                  flexGrow: dcs!.flexGrow,
                }
              : null,
            trend: trendSvg
              ? {
                  w: Math.round(trendSvg.getBoundingClientRect().width),
                  h: Math.round(trendSvg.getBoundingClientRect().height),
                  color: getComputedStyle(trendSvg).color,
                }
              : null,
          };
        }),
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    expect(census.cards).toBe(3);

    // The three count rows' chrome — byte-identical on both sides (the
    // stat-divider-arbit-v88.sh census): the 20px text line box, the
    // flex/8px/center rhythm, text-sm 14px, the inherited #0a0a0a.
    for (const row of census.rows) {
      expect(row.err).toBeUndefined();
      expect(row.row).toEqual({
        h: 20,
        display: "flex",
        gap: "8px",
        alignItems: "center",
        fs: "14px",
        color: "rgb(10, 10, 10)",
      });
      // The divider — the never-pinned family: the 1px flex-1 line in
      // the border token color (the WIDTH excluded — the flex-1
      // data-conditional remainder, the v82 convention).
      expect(row.divider).toEqual({
        tag: "DIV",
        h: "1px",
        bg: "rgb(229, 231, 227)",
        flexGrow: "1",
      });
    }

    // The trend icons: 16×16 with the per-type color trilogy (the
    // income lime / savings blue / expenses orange — the v80/v85
    // per-type-dot trilogy's stat-card twin, never pinned before).
    expect(census.rows[0]!.trend).toEqual({ w: 16, h: 16, color: "rgb(143, 188, 63)" });
    expect(census.rows[1]!.trend).toEqual({ w: 16, h: 16, color: "rgb(59, 126, 161)" });
    expect(census.rows[2]!.trend).toEqual({ w: 16, h: 16, color: "rgb(224, 122, 59)" });

    // The no-overflow guard on the same surface.
    expect(census.docSW).toBe(1280);
  });
});

// ---------------------------------------------------------------------------
// v89 — plan F4 (docs/remediation-plan-v89.md): the quick-action cards'
// TRANSITION + PLUS-viewBox + the guidelines body's DISPLAY census at 1280.
//
// The v89 arbitration (qa-transition-arbit-v89.sh, the v83-era pair's
// fourth re-run — the VLM verdict IDENTICAL, the both-sides census
// reproducing the v83 values exactly) measured a never-pinned family: the
// quick-action cards' transition chrome + the plus icons' viewBox + the
// guidelines body's display. The v61 F3 pin holds the cards' full chrome
// {text/w/h/radius/pad/bg/border/shadow/textAlign/tile/icon/label/plus} —
// never the TRANSITION family; the v77 pin holds the ICONS' viewBox (the
// first svg) — never the PLUS icons' own; the v61 F2 pin holds the
// guidelines body's PAD — never the DISPLAY; grep-verified: NO
// dashboard.spec.ts spec asserts the quick-action card's
// transitionDuration/transitionProperty at ANY viewport (the items.spec.ts
// transitionDur pins are the ITEM card's own family — a different
// component), no spec asserts the plus svg's viewBox, and no spec asserts
// the guidelines body's display.
//
// Every pinned axis STATIC chrome (the transition classes, the viewBox
// constant, and the body's display unconditional — no data, no viewport
// conditionals); the pin rides the plain authenticated dashboard view on
// the e2e seed — read-only, no fixture writes, no hover state.
// ---------------------------------------------------------------------------
interface QaTransitionCensus {
  cards: {
    text: string;
    transitionDuration: string;
    transitionProperty: string;
    plusViewBox: string | null;
    plusW: number | null;
  }[];
  guidelinesBody: { display: string; pad: string } | null;
  docSW: number;
  err?: string;
}
test.describe("quick-action transition + plus-viewBox + guidelines-body-display census at 1280 (v89 — plan F4)", () => {
  test("the three cards' transition chrome + the plus viewBoxes + the guidelines body display — the never-pinned family", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByRole("button", { name: "Add Income" })).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate((): QaTransitionCensus => {
      // The three quick-action cards (the v61 F3 finder: the exact-text
      // regex on the button trio).
      const qas = [...document.querySelectorAll("button")].filter(
        (b) => /^Add (Income|Savings|Expense)$/.test((b.textContent || "").trim()),
      );
      if (qas.length !== 3)
        return {
          cards: [],
          guidelinesBody: null,
          docSW: document.documentElement.scrollWidth,
          err: `qa count ${qas.length}`,
        };
      const cards = qas.map((b) => {
        const cs = getComputedStyle(b);
        const svgs = [...b.querySelectorAll("svg")];
        const plusSvg = svgs[svgs.length - 1];
        return {
          text: (b.textContent || "").trim(),
          transitionDuration: cs.transitionDuration,
          transitionProperty: cs.transitionProperty,
          plusViewBox: plusSvg ? plusSvg.getAttribute("viewBox") || "" : null,
          plusW: plusSvg ? Math.round(plusSvg.getBoundingClientRect().width) : null,
        };
      });
      // The guidelines card (the v61 F2 walk: shadow + radius + a <p>
      // descendant) → the body = the non-header child.
      const heading = [...document.querySelectorAll("h1, h2, h3, div, span")].find(
        (x) => (x.textContent || "").trim() === "Budget Guidelines" && x.children.length === 0,
      );
      let body: HTMLElement | null = null;
      if (heading) {
        let card = heading as HTMLElement;
        while (card.parentElement) {
          const cs = getComputedStyle(card);
          if (cs.boxShadow !== "none" && cs.borderRadius !== "0px" && card.querySelector("p")) break;
          card = card.parentElement as HTMLElement;
        }
        const header = heading.parentElement as HTMLElement;
        body = ([...card.children].find((c) => c !== header) as HTMLElement) || null;
      }
      return {
        cards,
        guidelinesBody: body
          ? { display: getComputedStyle(body).display, pad: getComputedStyle(body).padding }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census.err).toBeUndefined();
    expect(census.cards.length).toBe(3);

    // The three cards' transition chrome — byte-identical on both sides
    // (the qa-transition-arbit-v89.sh census): transition-all duration-200
    // (the reference's own resting 0.2s family on every card).
    const expectedTexts = ["Add Income", "Add Savings", "Add Expense"];
    census.cards.forEach((c, i) => {
      expect(c.text).toBe(expectedTexts[i]);
      expect(c.transitionDuration).toBe("0.2s");
      expect(c.transitionProperty).toBe("all");
      // The plus icons' viewBox — the v77 icon-viewBox family's plus twin
      // (the LAST svg in the card, never pinned before v89).
      expect(c.plusViewBox).toBe("0 0 24 24");
      expect(c.plusW).toBe(16);
    });

    // The guidelines body's display — the v61 F2 pad family's companion
    // axis (the pad "0px 24px 24px" re-affirming the v61 F2 pin).
    expect(census.guidelinesBody).toEqual({ display: "block", pad: "0px 24px 24px" });

    // The no-overflow guard on the same surface.
    expect(census.docSW).toBe(1280);
  });
});

// ---------------------------------------------------------------------------
// v95 — plan F4 (docs/remediation-plan-v95.md): the quick-action row's
// TRANSITION-TIMING family census at 1280.
//
// The v89-era dashboard pair's FIFTH re-run's pin: the never-pinned
// transition-TIMING chrome — the three cards' transitionTimingFunction +
// transitionDelay (the v89 pin holds the duration/property only), the
// three tinted tiles' transition-transform family (the v61 F3 pin holds
// the tile's geometry; the timing/duration never pinned at ANY viewport),
// and the three plus icons' transition-opacity family (never pinned — the
// v61 F3 pin holds the plus's resting opacity/color only).
//
// The axes first measured byte-identical on BOTH sides by the qa-timing
// two-half census (qa-timing-arbit-v95.sh + qa-timing-clone-v95.sh, the
// census JS md5-identical across the halves): cardTiming
// cubic-bezier(0.4, 0, 0.2, 1) + cardDelay 0s; tile {dur 0.2s, timing
// cubic-bezier(0.4, 0, 0.2, 1)}; plus {prop opacity, dur 0.15s, timing
// cubic-bezier(0.4, 0, 0.2, 1), delay 0s}; docSW 1280.
//
// THE v4 TRANSITION-PROPERTY COMPUTED-FORM CLASS (the v95 lesson): the
// reference (Tailwind v3) computes the tile's transitionProperty as
// "transform" while the clone (v4) computes "transform, translate, scale,
// rotate" — the v4 utility's expanded property list, the rendered behavior
// identical (the tile's only animated property `scale` covered by BOTH
// lists). The property axis is asserted in the CONTAINS form, never exact
// (the v66 shadow lead-layer / v82 labelBlock width / v94 margin-form
// family's newest member).
// ---------------------------------------------------------------------------
interface QaTimingCensus {
  cards: {
    text: string;
    cardTiming: string;
    cardDelay: string;
    tileTransition: { prop: string; dur: string; timing: string } | null;
    plusTransition: { prop: string; dur: string; timing: string; delay: string } | null;
  }[];
  docSW: number;
  err?: string;
}
test.describe("quick-action transition-timing family census at 1280 (v95 — plan F4)", () => {
  test("the three cards' timing function + delay + the tiles' and pluses' transition families — the never-pinned family", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByRole("button", { name: "Add Income" })).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate((): QaTimingCensus => {
      // The three quick-action cards (the v61 F3 finder: the exact-text
      // regex on the button trio).
      const qas = [...document.querySelectorAll("button")].filter(
        (b) => /^Add (Income|Savings|Expense)$/.test((b.textContent || "").trim()),
      );
      if (qas.length !== 3)
        return {
          cards: [],
          docSW: document.documentElement.scrollWidth,
          err: `qa count ${qas.length}`,
        };
      const cards = qas.map((b) => {
        const cs = getComputedStyle(b);
        const svgs = [...b.querySelectorAll("svg")];
        const plus = svgs[svgs.length - 1] as SVGElement | undefined;
        // The tile: the v61 F3 finder (radius 12px, the 30..60 box).
        const tile = [...b.querySelectorAll("span, div")].find((s) => {
          const st = getComputedStyle(s);
          const sr = s.getBoundingClientRect();
          return st.borderRadius === "12px" && sr.width >= 30 && sr.width <= 60 && sr.height >= 30 && sr.height <= 60;
        }) as HTMLElement | undefined;
        const pcs = plus ? getComputedStyle(plus) : null;
        const tcs = tile ? getComputedStyle(tile) : null;
        return {
          text: (b.textContent || "").trim(),
          cardTiming: cs.transitionTimingFunction,
          cardDelay: cs.transitionDelay,
          tileTransition: tcs
            ? { prop: tcs.transitionProperty, dur: tcs.transitionDuration, timing: tcs.transitionTimingFunction }
            : null,
          plusTransition: pcs
            ? { prop: pcs.transitionProperty, dur: pcs.transitionDuration, timing: pcs.transitionTimingFunction, delay: pcs.transitionDelay }
            : null,
        };
      });
      return { cards, docSW: document.documentElement.scrollWidth };
    });
    expect(census.err).toBeUndefined();
    expect(census.cards.length).toBe(3);

    // The three cards' timing function + delay — byte-identical on both
    // sides (the qa-timing two-half census): Tailwind's default timing
    // (the duration-200 family's own curve) + no delay.
    const expectedTexts = ["Add Income", "Add Savings", "Add Expense"];
    census.cards.forEach((c, i) => {
      expect(c.text).toBe(expectedTexts[i]);
      expect(c.cardTiming).toBe("cubic-bezier(0.4, 0, 0.2, 1)");
      expect(c.cardDelay).toBe("0s");
      // The tiles' transition-transform family — the duration + timing
      // byte-identical; the PROPERTY in the CONTAINS form (the v95 v4
      // computed-form class: the clone's "transform, translate, scale,
      // rotate" superset vs the reference's "transform" — the rendered
      // behavior identical).
      expect(c.tileTransition).not.toBeNull();
      expect(c.tileTransition!.prop).toContain("transform");
      expect(c.tileTransition!.dur).toBe("0.2s");
      expect(c.tileTransition!.timing).toBe("cubic-bezier(0.4, 0, 0.2, 1)");
      // The pluses' transition-opacity family — all four axes
      // byte-identical (the Tailwind default 150ms — no duration class
      // on the plus).
      expect(c.plusTransition).toEqual({
        prop: "opacity",
        dur: "0.15s",
        timing: "cubic-bezier(0.4, 0, 0.2, 1)",
        delay: "0s",
      });
    });

    // The no-overflow guard on the same surface.
    expect(census.docSW).toBe(1280);
  });
});

// ---------------------------------------------------------------------------
// v101 — plan F4 (docs/remediation-plan-v101.md): the spending+guidelines
// 2-COL ROW's grid + the Spending Breakdown card's own box/header census
// at 1280 (the pair viewport). The never-pinned family (the coverage-map
// grep across all 24 specs: zero "468px 468px" template matches, zero
// spending-card radius/border/shadow assertions, the subtitle only
// visibility-asserted at line ~106, the only columnGap census the v61 F3
// quick-action grid's own): the v61 F2 pin walks the row ONLY for rowH 656
// (the stretch contract) + the guidelines card's own box; the v77 pin the
// guidelines card's interior text; the v83 F4 pin the card-level cross-row
// gap — but the ROW'S OWN GRID CHROME (the lg:grid-cols-2 template, the
// 24px column gap, the 960 width, the two children's 468 widths) and the
// SPENDING CARD'S OWN BOX + HEADER (the card radius/border/bg/shadow, the
// title's typography, the subtitle's chrome, the title→subtitle rhythm,
// the body's pt-0 contract) were NEVER pinned at ANY viewport in ANY
// spec. The values are the supplemental two-half census's own measurements
// (spending-arbit-v101.sh + spending-clone-v101.sh via
// build-spending-v101.py, the census JS byte-identical by the md5
// line-block contract [7e6a13c3]) — byte-identical on BOTH sides; every
// axis DATA-INDEPENDENT (the structural chrome + the fixed header texts;
// the data-locked heights stay with the v61 F2 pin's own rowH contract —
// the v98 data-independent-panel strength class).
// ---------------------------------------------------------------------------
test.describe("the spending+guidelines 2-col row grid + the spending card's box/header census at 1280 (v101 — plan F4)", () => {
  test("the row's grid chrome + the two children + the card's box + the header block + the body-pad contract", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByText("Spending Breakdown")).toBeVisible();

    const census = await page.evaluate(() => {
      // THE SPENDING CARD: the leaf title → the bordered card walk (the
      // v61 F2 pattern: shadow + radius + a <p> descendant).
      const title = [...document.querySelectorAll("h1, h2, h3, h4, div, span, p")].find(
        (e) => (e.textContent || "").trim() === "Spending Breakdown" && e.children.length === 0,
      ) as HTMLElement | undefined;
      if (!title) return null;
      let card = title as HTMLElement;
      while (card.parentElement) {
        const cs = getComputedStyle(card);
        if (cs.boxShadow !== "none" && cs.borderRadius !== "0px" && card.querySelector("p")) break;
        card = card.parentElement as HTMLElement;
      }
      const csC = getComputedStyle(card);
      const rC = card.getBoundingClientRect();
      // THE HEADER BLOCK (the title's parent) + the subtitle <p>.
      const header = title.parentElement as HTMLElement;
      const subtitle = header.querySelector("p") as HTMLElement | null;
      const rT = title.getBoundingClientRect();
      // THE BODY (the card's non-header child — the p-6 pt-0 contract).
      const body = [...card.children].find((c) => c !== header) as HTMLElement | undefined;
      // THE ROW: the ancestor 2-col grid (the v61 F2 walk).
      let row = card.parentElement as HTMLElement | null;
      while (row) {
        const cls = (row.className || "").toString();
        if (/grid-cols-2/.test(cls) && row.children.length === 2) break;
        row = row.parentElement as HTMLElement | null;
      }
      if (!row) return null;
      const csR = getComputedStyle(row);
      const rR = row.getBoundingClientRect();
      return {
        docSW: document.documentElement.scrollWidth,
        card: {
          w: Math.round(rC.width),
          radius: csC.borderRadius,
          border: csC.borderTopColor,
          bg: csC.backgroundColor,
          shadow: csC.boxShadow,
        },
        header: { pad: getComputedStyle(header).padding },
        title: {
          fs: getComputedStyle(title).fontSize,
          fw: getComputedStyle(title).fontWeight,
          color: getComputedStyle(title).color,
          lh: getComputedStyle(title).lineHeight,
          tracking: getComputedStyle(title).letterSpacing,
        },
        subtitle: subtitle
          ? {
              text: (subtitle.textContent || "").trim(),
              fs: getComputedStyle(subtitle).fontSize,
              fw: getComputedStyle(subtitle).fontWeight,
              color: getComputedStyle(subtitle).color,
              lh: getComputedStyle(subtitle).lineHeight,
              // THE TITLE→SUBTITLE RHYTHM (the space-y-1.5) — the
              // subtitle's top minus the title's bottom.
              top: Math.round(subtitle.getBoundingClientRect().top - rT.bottom),
            }
          : null,
        body: body ? { pad: getComputedStyle(body).padding } : null,
        row: {
          display: csR.display,
          template: csR.gridTemplateColumns,
          colGap: csR.columnGap,
          w: Math.round(rR.width),
        },
        children: [...row.children].map((k) => {
          const kr = k.getBoundingClientRect();
          return { w: Math.round(kr.width), display: getComputedStyle(k).display };
        }),
      };
    });
    expect(census, "the spending-row census finder (the leaf title + the 2-col row walk)").not.toBeNull();
    if (!census) throw new Error("spending-row census found no card or row");

    // THE ROW'S OWN GRID CHROME — never pinned before v101 (the
    // lg:grid-cols-2 2-equal-track template + the gap-6 column gap +
    // the 960 cap arithmetic).
    expect(census.row).toEqual({
      display: "grid",
      template: "468px 468px",
      colGap: "24px",
      w: 960,
    });
    // The two children: the spending card + the stretched guidelines
    // wrapper — both 468 (the (960−24)/2 arithmetic).
    expect(census.children).toEqual([
      { w: 468, display: "block" },
      { w: 468, display: "block" },
    ]);
    // The SPENDING CARD's own box — the v61 F2 guidelines-box twin (the
    // left column's card): radius/border/bg byte-identical both sides;
    // the shadow's VISIBLE pair (the clone's transparent lead layers —
    // the v66 computed-form INVISIBLE class).
    expect(census.card.w).toBe(468);
    expect(census.card.radius).toBe("12px");
    expect(census.card.border).toBe("rgb(229, 231, 227)");
    expect(census.card.bg).toBe("rgb(255, 255, 255)");
    expect(census.card.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(census.card.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    // The header block: the pad + the title's full typography (the v77
    // guidelines-header twin — the lh + tracking included).
    expect(census.header.pad).toBe("24px");
    expect(census.title).toEqual({
      fs: "16px",
      fw: "600",
      color: "rgb(26, 58, 46)",
      lh: "16px",
      tracking: "-0.4px",
    });
    // The subtitle: the fixed text + the chrome + the title→subtitle
    // rhythm (the space-y-1.5 = 6px).
    expect(census.subtitle).toEqual({
      text: "Needs vs Wants vs Savings",
      fs: "14px",
      fw: "400",
      color: "rgb(107, 114, 128)",
      lh: "20px",
      top: 6,
    });
    // The BODY PAD contract: the pt-0 (the header's own p-6 bottom
    // provides the header→body separation).
    expect(census.body!.pad).toBe("0px 24px 24px");
    // The no-overflow guard on the same surface.
    expect(census.docSW).toBe(1280);
  });
});

// ---------------------------------------------------------------------------
// v107 — plan F4: the quick-action card's INTERIOR flex-row census at 1280
// (the pair viewport). The qarow one-shot census (qarow-arbit-v107.sh)
// measured the family byte-identical on both sites: the row {flex/center/
// gap 12px/h 40/childCount 3}, the tile {flex/center/center/40×40/radius
// 12px}, the icon {20×20, offsets 10/10 — the (40−20)/2 centering
// arithmetic}, the label leaf {16px/500/forestDark}, the plus {16/16/0.5}.
// THE STRUCTURAL-FINDER LESSON (the v107 DIV-vs-SPAN finding): the
// reference's row/tile are DIVs while the clone's are SPANs — identical
// computed chrome, different tags — so the finders walk POSITIONALLY
// (firstElementChild children order), never by tag; the label leaf finder
// is the v61 leaf lesson generalized TAG-AGNOSTIC (exact text + zero
// element children, any tag). The v61 F3 pin holds the card/tile/icon/
// label/plus BOX chrome; THIS pin adds the interior row's own flex/gap
// centering + the tile's flex centering + the icon's centering offsets —
// never pinned at ANY viewport before. The label's xInRow (52) and the
// plus's xInRow (238) stay census-documented but UNPINNED (position
// arithmetic a future layout change could co-move with unrelated axes —
// the pin holds the structural chrome, the single-axis discipline
// protected by construction).
// ---------------------------------------------------------------------------
test.describe("the quick-action card interior flex-row census at 1280 (v107 — plan F4)", () => {
  test("the row's flex/gap centering + the tile's flex centering + the icon's centering offsets (the never-pinned family)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByRole("button", { name: "Add Income" })).toBeVisible();
    const census = await page.evaluate(() => {
      const qas = [...document.querySelectorAll("button")].filter(
        (b) => /^Add (Income|Savings|Expense)$/.test((b.textContent || "").trim()),
      ) as HTMLElement[];
      if (qas.length !== 3) return null;
      const cards = qas.map((b) => {
        // STRUCTURAL walk (the v107 DIV-vs-SPAN lesson): positional
        // children — never a tag match.
        const row = b.firstElementChild as HTMLElement | null;
        const rcs = row ? getComputedStyle(row) : null;
        const rr = row ? row.getBoundingClientRect() : null;
        const tile = row ? (row.firstElementChild as HTMLElement | null) : null;
        const tcs = tile ? getComputedStyle(tile) : null;
        const tr = tile ? tile.getBoundingClientRect() : null;
        const svgs = row ? ([...row.querySelectorAll("svg")] as SVGElement[]) : [];
        const icon = svgs[0];
        const ir = icon ? icon.getBoundingClientRect() : null;
        const plus = svgs[svgs.length - 1];
        const pr = plus ? plus.getBoundingClientRect() : null;
        // THE TAG-AGNOSTIC LEAF LABEL (the v61 lesson generalized): the
        // exact text + zero element children — any tag.
        const label = row
          ? [...row.querySelectorAll("*")].find(
              (e) =>
                /^Add (Income|Savings|Expense)$/.test((e.textContent || "").trim()) &&
                e.children.length === 0,
            )
          : undefined;
        const lcs = label ? getComputedStyle(label) : null;
        return {
          text: (b.textContent || "").trim(),
          row:
            rcs && rr
              ? {
                  display: rcs.display,
                  align: rcs.alignItems,
                  gap: rcs.gap,
                  h: Math.round(rr.height),
                  childCount: row!.children.length,
                }
              : null,
          tile:
            tcs && tr
              ? {
                  display: tcs.display,
                  align: tcs.alignItems,
                  justify: tcs.justifyContent,
                  w: Math.round(tr.width),
                  h: Math.round(tr.height),
                  radius: tcs.borderRadius,
                }
              : null,
          icon:
            icon && ir && tr
              ? {
                  w: Math.round(ir.width),
                  h: Math.round(ir.height),
                  offX: Math.round(ir.x - tr.x),
                  offY: Math.round(ir.y - tr.y),
                  color: getComputedStyle(icon).color,
                }
              : null,
          label: lcs ? { fs: lcs.fontSize, fw: lcs.fontWeight, color: lcs.color } : null,
          plus:
            plus && pr
              ? {
                  w: Math.round(pr.width),
                  h: Math.round(pr.height),
                  opacity: getComputedStyle(plus).opacity,
                }
              : null,
        };
      });
      return { cards, docSW: document.documentElement.scrollWidth };
    });
    expect(census).not.toBeNull();
    // The three cards (identical interior chrome; the icon accent trio).
    const expected = [
      { text: "Add Income", accent: "rgb(143, 188, 63)" },
      { text: "Add Savings", accent: "rgb(59, 126, 161)" },
      { text: "Add Expense", accent: "rgb(224, 122, 59)" },
    ];
    census!.cards.forEach((c, i) => {
      const e = expected[i]!;
      expect(c.text).toBe(e.text);
      // The row: the flex/gap-12 centering (the never-pinned interior).
      expect(c.row).toEqual({
        display: "flex",
        align: "center",
        gap: "12px",
        h: 40,
        childCount: 3,
      });
      // The tile: the flex centering (display/align/justify + the box).
      expect(c.tile).toEqual({
        display: "flex",
        align: "center",
        justify: "center",
        w: 40,
        h: 40,
        radius: "12px",
      });
      // The icon: the (40−20)/2 centering offsets — never pinned before.
      expect(c.icon).toEqual({
        w: 20,
        h: 20,
        offX: 10,
        offY: 10,
        color: e.accent,
      });
      // The label leaf chrome (the tag-agnostic leaf — the v61 lesson).
      expect(c.label).toEqual({ fs: "16px", fw: "500", color: "rgb(26, 58, 46)" });
      // The plus box + opacity (the xInRow anchor stays census-only).
      expect(c.plus).toEqual({ w: 16, h: 16, opacity: "0.5" });
    });
    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);
  });
});


// ---------------------------------------------------------------------------
// v112 — plan F4 (docs/remediation-plan-v112.md): the Net Zero Breakdown
// card's NET-BALANCE FOOTER ROW interior census at 1280 (the pair
// viewport). The never-pinned family (the coverage map: the v5-era
// "Net Balance renders positive" test pins the AMOUNT color + the icon's
// existence only; the v42 F1 band census the divider's EXISTENCE + the
// band texts; the v43/v44/v60/v76/v82 censuses the section/category/
// sub/item rows, the income-section chip and the networth ratio — NEVER
// the net-balance row's own interior). Measured byte-identical on BOTH
// sides by the v112 one-shot census (netrow-arbit-v112.sh) BEFORE the
// pin: the wrapper {mt-3 border-t pt-3} + the row {flex center
// justify-between, h 32} + the left block {flex, gap-2} + the h-8 w-8
// rounded-lg chip on the 12.5% orangeLight tint + the h-4 w-4 trending-up
// glyph + the text-sm font-semibold gray label + the text-lg font-bold
// value — both sides' POSITIVE balances putting the sign-conditional
// family orangeLight on BOTH sides (the value TEXT the data class, never
// asserted).
test.describe("drill-down net-balance footer-row census at 1280 (v112 — plan F4)", () => {
  test("the wrapper + the row + the chip + the label + the value — the never-pinned family", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    // The settle: the seeded net balance (5550 − 1250 − 2235 = +$2065.00)
    // — the same deterministic anchor the v60 F2 pin uses.
    await expect(page.getByText("+$2065.00")).toBeVisible();

    const census = await page.evaluate(() => {
      // The finders modeled on the v112 arbitration's own census
      // (netrow-arbit-v112.sh) — all STRUCTURAL (the v72 class): the
      // card by the "Net Zero Breakdown" leaf walk-up; the label by
      // exact text (childless); the value as the LAST childless signed
      // money leaf in the card (the section/category totals live inside
      // BUTTON text, never as bare leaves; the net row sits last in DOM
      // order); the row as the flex ancestor of the label that ALSO
      // contains the value (never by class alone — a naive closest
      // walk can land on the left block when it is itself a flex div);
      // the chip by the left block's rounded-lg child; the wrapper as
      // the row's parent.
      const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
        (e) => (e.textContent || "").trim() === "Net Zero Breakdown" && e.children.length === 0,
      );
      if (!leaf) return null;
      const card = leaf.closest('div[class*="rounded-2xl"]') as HTMLElement | null;
      if (!card) return null;
      const label = [...card.querySelectorAll("span")].find(
        (s) => (s.textContent || "").trim() === "Net Balance" && s.children.length === 0,
      ) as HTMLElement | undefined;
      if (!label) return null;
      const moneyRe = /^[-+]\$[\d,]+(\.\d+)?$/;
      const moneyLeaves = [...card.querySelectorAll("span,p,div")].filter(
        (s) => s.children.length === 0 && moneyRe.test((s.textContent || "").trim()),
      );
      const value = moneyLeaves.length
        ? (moneyLeaves[moneyLeaves.length - 1] as HTMLElement)
        : null;
      if (!value) return null;
      let row: HTMLElement | null = label.parentElement;
      while (row && row !== card) {
        if (row.contains(value) && getComputedStyle(row).display === "flex") break;
        row = row.parentElement;
      }
      if (!row || row === card) return null;
      const leftBlock = label.parentElement as HTMLElement;
      const chip = leftBlock.querySelector("span.rounded-lg, div.rounded-lg") as HTMLElement | null;
      const icon = chip ? (chip.querySelector("svg") as SVGElement | null) : null;
      const wrapper = row.parentElement;
      if (!chip || !icon || !wrapper) return null;
      const wcs = getComputedStyle(wrapper);
      const rcs = getComputedStyle(row);
      const rr = row.getBoundingClientRect();
      const lcs = getComputedStyle(leftBlock);
      const ccs = getComputedStyle(chip);
      const cr = chip.getBoundingClientRect();
      const ics = getComputedStyle(icon);
      const ir = icon.getBoundingClientRect();
      const lbcs = getComputedStyle(label);
      const lr = label.getBoundingClientRect();
      const vr = value.getBoundingClientRect();
      const vcs = getComputedStyle(value);
      return {
        wrapper: {
          mt: wcs.marginTop,
          pt: wcs.paddingTop,
          borderTopW: wcs.borderTopWidth,
          borderTopC: wcs.borderTopColor,
        },
        row: {
          display: rcs.display,
          align: rcs.alignItems,
          justify: rcs.justifyContent,
          h: Math.round(rr.height),
        },
        leftBlock: {
          display: lcs.display,
          align: lcs.alignItems,
          gap: lcs.gap,
          h: Math.round(leftBlock.getBoundingClientRect().height),
        },
        chip: {
          w: Math.round(cr.width),
          h: Math.round(cr.height),
          radius: ccs.borderRadius,
          bg: ccs.backgroundColor,
        },
        chipIcon: {
          w: Math.round(ir.width),
          h: Math.round(ir.height),
          color: ics.color,
          glyphSig: (icon.innerHTML || "").replace(/\s+/g, " ").slice(0, 110),
          viewBox: icon.getAttribute("viewBox"),
        },
        label: {
          text: (label.textContent || "").trim(),
          fs: lbcs.fontSize,
          fw: lbcs.fontWeight,
          color: lbcs.color,
          h: Math.round(lr.height),
        },
        value: {
          fs: vcs.fontSize,
          fw: vcs.fontWeight,
          color: vcs.color,
          h: Math.round(vr.height),
        },
        junction: {
          chipCy: Math.round(cr.y + cr.height / 2),
          rowCy: Math.round(rr.y + rr.height / 2),
          labelCy: Math.round(lr.y + lr.height / 2),
        },
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The border-t wrapper — the v42 F1 divider's computed chrome (the
    // band census held its EXISTENCE + position; never its mt/pt/color).
    expect(census!.wrapper).toEqual({
      mt: "12px",
      pt: "12px",
      borderTopW: "1px",
      borderTopC: "rgb(229, 231, 227)",
    });
    // The row's flex chrome — never pinned at ANY viewport before this
    // pin (the h 32 governed by the 32px chip; the justify-between puts
    // the value at the card's right edge).
    expect(census!.row).toEqual({
      display: "flex",
      align: "center",
      justify: "space-between",
      h: 32,
    });
    // The left block — the chip + label cluster (gap-2 = 8px).
    expect(census!.leftBlock).toEqual({
      display: "flex",
      align: "center",
      gap: "8px",
      h: 32,
    });
    // The icon chip — the h-8 w-8 rounded-lg tile on the 12.5%
    // orangeLight tint (the POSITIVE case; the sign-conditional family
    // resolved by the seed's +$2065.00).
    expect(census!.chip).toEqual({
      w: 32,
      h: 32,
      radius: "8px",
      bg: "rgba(245, 169, 98, 0.125)",
    });
    // The chip icon — the legacy TrendingUpIcon twin-polyline path in
    // the 0 0 24 24 viewBox (the same glyph family the v76 pin holds on
    // the income-section chip — here on the net row's own chip).
    expect(census!.chipIcon).toEqual({
      w: 16,
      h: 16,
      color: "rgb(245, 169, 98)",
      glyphSig:
        '<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"></polyline><polyline points="16 7 22 7 22 13"></polyline>',
      viewBox: "0 0 24 24",
    });
    // The label — the text-sm font-semibold gray leaf (the mutation
    // target line: dashboard-view.tsx:532).
    expect(census!.label).toEqual({
      text: "Net Balance",
      fs: "14px",
      fw: "600",
      color: "rgb(107, 114, 128)",
      h: 20,
    });
    // The value's typography — text-lg font-bold on the positive-case
    // orangeLight (the text itself the data class, never asserted).
    expect(census!.value).toEqual({
      fs: "18px",
      fw: "700",
      color: "rgb(245, 169, 98)",
      h: 28,
    });
    // The junction — the items-center alignment read live: all three
    // centers coincide (the absolute y the data-state axis, never
    // pinned; the EQUALITY is the contract).
    expect(census!.junction.chipCy).toBe(census!.junction.rowCy);
    expect(census!.junction.labelCy).toBe(census!.junction.rowCy);
    // The viewport guard.
    expect(census!.docSW).toBe(1280);
  });
});

// ---------------------------------------------------------------------------
// v113 — plan F4: the Budget Guidelines card's TILE LABEL-ROW family + the
// tile stack rhythm census at 1280 (the re-run pair's pin). The v61 F2 pin
// holds the card box + the first tile box + the STRETCH contract; the v77
// F4 pin the header typography + all three tiles' label/pct/desc TEXT
// chrome; the v83 F4 pin the card bottom / grid top / rendered gap / grid
// mt; the v89 F4 pin the qa transition + the plus viewBoxes + the body
// display/pad. NEVER pinned at ANY viewport before this pin: the tile
// label-row's own flex chrome {display/align/justify/mb/h/childCount} and
// the tile-to-tile stack rhythm (the space-y-3 12px gaps). The label/pct
// x-position axes (xInRow 0 / rightGap 0 / the justify-between edge
// anchors) stay CENSUS-documented but UNPINNED — the v107 xInRow
// discipline (position arithmetic that a future layout change could
// co-move with unrelated axes). The values are the glrow-arbit-v113.sh
// census's own measurements, byte-identical on both sides (the mutation
// target line: dashboard-view.tsx:847).
// ---------------------------------------------------------------------------
interface GlLabelRowCensus {
  row: {
    display: string;
    align: string;
    justify: string;
    mb: string;
    h: number;
    w: number;
    childCount: number;
  } | null;
  tileRhythm: { gap1: number; gap2: number } | null;
  docSW: number;
  err?: string;
}
test.describe("guidelines tile label-row + stack-rhythm census at 1280 (v113 — plan F4)", () => {
  test("the label row's flex chrome + the 12px tile rhythm — the never-pinned family", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByText("Budget Guidelines")).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate((): GlLabelRowCensus => {
      // The heading leaf (childless exact text — the v77 finder).
      const heading = [...document.querySelectorAll("h1, h2, h3, div, span")].find(
        (x) => (x.textContent || "").trim() === "Budget Guidelines" && x.children.length === 0,
      ) as HTMLElement | undefined;
      if (!heading)
        return { row: null, tileRhythm: null, docSW: document.documentElement.scrollWidth, err: "no heading" };
      // The card walk-up (shadow + radius + a <p> descendant — the v61 F2 walk).
      let card = heading as HTMLElement;
      while (card.parentElement) {
        const cs = getComputedStyle(card);
        if (cs.boxShadow !== "none" && cs.borderRadius !== "0px" && card.querySelector("p")) break;
        card = card.parentElement as HTMLElement;
      }
      // The three tiles (the v77 finder: radius 8px, the height band, the
      // non-transparent bg, not the card).
      const tiles = [...card.querySelectorAll("div")].filter((d) => {
        const cs = getComputedStyle(d);
        const r = d.getBoundingClientRect();
        return (
          cs.borderRadius === "8px" &&
          r.height > 40 &&
          r.height < 200 &&
          d.querySelector("span, p") &&
          cs.backgroundColor !== "rgba(0, 0, 0, 0)" &&
          d !== card
        );
      }) as HTMLElement[];
      if (tiles.length !== 3)
        return { row: null, tileRhythm: null, docSW: document.documentElement.scrollWidth, err: `tile count ${tiles.length}` };
      // The label row of tile 0: label = the FIRST childless span, pct =
      // the LAST; the row = the nearest flex ancestor of the label that
      // ALSO contains the pct (the structural walk — the v72 class).
      const t0 = tiles[0];
      const spans = [...t0.querySelectorAll("span")].filter((s) => s.children.length === 0) as HTMLElement[];
      const label = spans[0];
      const pct = spans[spans.length - 1];
      if (!label || !pct || label === pct)
        return { row: null, tileRhythm: null, docSW: document.documentElement.scrollWidth, err: "no label/pct pair" };
      let row = label.parentElement as HTMLElement | null;
      while (row && row !== t0) {
        if (row.contains(pct) && getComputedStyle(row).display === "flex") break;
        row = row.parentElement as HTMLElement | null;
      }
      if (!row || row === t0)
        return { row: null, tileRhythm: null, docSW: document.documentElement.scrollWidth, err: "no label row" };
      const rcs = getComputedStyle(row);
      const rr = row.getBoundingClientRect();
      const trs = tiles.map((t) => t.getBoundingClientRect());
      return {
        row: {
          display: rcs.display,
          align: rcs.alignItems,
          justify: rcs.justifyContent,
          mb: rcs.marginBottom,
          h: Math.round(rr.height),
          w: Math.round(rr.width),
          childCount: row.children.length,
        },
        tileRhythm: {
          gap1: Math.round(trs[1].top - trs[0].bottom),
          gap2: Math.round(trs[2].top - trs[1].bottom),
        },
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    expect(census!.err).toBeUndefined();
    // The label row's flex chrome — the mb-1 flex items-center
    // justify-between row (the 384 = the 418 tile − 2×16 pad − 2×1 border;
    // the h 24 = the 16px label's 1.5 line box; the children [label, pct]).
    expect(census!.row).toEqual({
      display: "flex",
      align: "center",
      justify: "space-between",
      mb: "4px",
      h: 24,
      w: 384,
      childCount: 2,
    });
    // The tile stack rhythm — the space-y-3 12px gaps between the three
    // tiles (never pinned at ANY viewport before this pin).
    expect(census!.tileRhythm).toEqual({ gap1: 12, gap2: 12 });
    // The viewport guard.
    expect(census!.docSW).toBe(1280);
  });
});


// ---------------------------------------------------------------------------
// The v114 re-run pair's pin (the MOBILE TWINS — BOTH 390x844 full-page
// twins, the v108-era pair's EIGHTH re-run): the DASHBOARD mobile twin's
// HEADER-ROW interior census at 390. The never-pinned family (the
// coverage-map grep across all 24 specs): the v62 F2 pin walks the h1's
// PARENT BLOCK's interior (the subtitle P's chrome + the block {h 92,
// top 77} + the h1's {h 36, fs 30px, fw 700, mb 8px}) — NEVER the ROW that
// carries the block + the Add Item button; the session-5 pin the button's
// background GRADIENT only; the v35 S2 pin the focus-visible shadow; the
// G3 pin the Plus icon at the default viewport; the v52 F3/v65/v109 F4
// pins the ITEMS-VIEW header rows (different elements); the hero
// 390-reflow pin the goal card below the row. NEVER pinned at ANY
// viewport before this pin: the row's own flex chrome
// {display/flexDirection/align/justify/gap/mb}, the junction (the h1
// block's bottom -> the Add Item button's top: the row's gap-4), and the
// Add Item button's BOX chrome {h/w/pad/radius/fs/fw/color/icon}. The
// block's/button's x positions and absolute y values stay
// CENSUS-documented but UNPINNED (the v107 position-arithmetic
// discipline). The values are the drow-arbit-v114.sh census's own
// measurements, byte-identical on both sides (the mutation target line:
// dashboard-view.tsx:927).
// ---------------------------------------------------------------------------
interface DashHeaderRowCensus {
  row: {
    display: string;
    flexDirection: string;
    align: string;
    justify: string;
    gap: string;
    mb: string;
    h: number;
  } | null;
  block: { h: number; bottom: number } | null;
  addBtn: {
    top: number;
    h: number;
    w: number;
    pad: string;
    radius: string;
    fs: string;
    fw: string;
    color: string;
    bg: string;
    icon: { w: number; h: number } | null;
  } | null;
  junction: { gap: number } | null;
  docSW: number;
  err?: string;
}
test.describe("dashboard header-row interior census at 390 (v114 — plan F4)", () => {
  test("the row's flex chrome + the block→button junction + the Add Item button's box chrome — the never-pinned family", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/");
    await expect(page.getByRole("heading", { name: "NET ZERO GOAL" })).toBeVisible();
    await page.waitForTimeout(400);

    const census = await page.evaluate((): DashHeaderRowCensus | null => {
      try {
        // THE FINDER CHAIN (the v62 lesson: parentElement, never closest()).
        // The h1 by childless exact text -> the block = h1.parentElement ->
        // the row = block.parentElement -> the button by the row's
        // button-with-Add-Item-text walk.
        const h1 = [...document.querySelectorAll("h1")].find(
          (x) => (x.textContent || "").trim() === "Budget Dashboard",
        );
        if (!h1) return { row: null, block: null, addBtn: null, junction: null, docSW: 0, err: "no h1" };
        const block = h1.parentElement as HTMLElement | null;
        const row = block ? (block.parentElement as HTMLElement | null) : null;
        if (!block || !row) return { row: null, block: null, addBtn: null, junction: null, docSW: 0, err: "no block/row" };
        const rcs = getComputedStyle(row);
        const rr = row.getBoundingClientRect();
        const br = block.getBoundingClientRect();
        const btn = [...row.querySelectorAll("button")].find((b) =>
          /Add Item/i.test(b.textContent || ""),
        ) as HTMLElement | undefined;
        if (!btn) return { row: null, block: null, addBtn: null, junction: null, docSW: 0, err: "no Add Item button" };
        const bs = getComputedStyle(btn);
        const brr = btn.getBoundingClientRect();
        const icon = btn.querySelector("svg");
        const iconR = icon ? icon.getBoundingClientRect() : null;
        return {
          row: {
            display: rcs.display,
            flexDirection: rcs.flexDirection,
            align: rcs.alignItems,
            justify: rcs.justifyContent,
            gap: rcs.rowGap,
            mb: rcs.marginBottom,
            h: Math.round(rr.height),
          },
          block: { h: Math.round(br.height), bottom: Math.round(br.bottom) },
          addBtn: {
            top: Math.round(brr.top),
            h: Math.round(brr.height),
            w: Math.round(brr.width),
            pad: bs.padding,
            radius: bs.borderRadius,
            fs: bs.fontSize,
            fw: bs.fontWeight,
            color: bs.color,
            bg: (bs.backgroundImage || "").replace(/\s+/g, " ").slice(0, 90),
            icon: iconR ? { w: Math.round(iconR.width), h: Math.round(iconR.height) } : null,
          },
          // THE JUNCTION: the block's bottom -> the button's top (the row's
          // gap-4 at 390 — the never-pinned axis).
          junction: { gap: Math.round(brr.top) - Math.round(br.bottom) },
          docSW: document.documentElement.scrollWidth,
        };
      } catch (e) {
        return { row: null, block: null, addBtn: null, junction: null, docSW: 0, err: String(e) };
      }
    });
    expect(census).not.toBeNull();
    expect(census!.err).toBeUndefined();

    // The header ROW's own flex chrome — flex-col at 390 with the
    // items-start cross-axis alignment and the space-between main-axis
    // distribution over the 16px gap (the h 144 = the block 92 + the gap 16
    // + the button 36; the mb 32 the row→hero junction's own arithmetic).
    expect(census!.row).toEqual({
      display: "flex",
      flexDirection: "column",
      align: "flex-start",
      justify: "space-between",
      gap: "16px",
      mb: "32px",
      h: 144,
    });

    // The block — the junction's anchor (the v62 pin holds the block's
    // full interior at 390; re-anchored here for the junction arithmetic).
    expect(census!.block).toEqual({ h: 92, bottom: 169 });

    // The Add Item button's BOX chrome — never pinned at ANY viewport
    // before this pin (the session-5 pin holds the gradient; the v35 S2 the
    // focus shadow; the G3 the icon at the default viewport). The w 127 =
    // the auto-width of the fixed "Add Item" text + the 16px icon + pad.
    expect(census!.addBtn).toEqual({
      top: 185,
      h: 36,
      w: 127,
      pad: "8px 16px",
      radius: "6px",
      fs: "14px",
      fw: "500",
      color: "rgb(255, 255, 255)",
      bg: "linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))",
      icon: { w: 16, h: 16 },
    });

    // THE JUNCTION — the row's gap-4: the button's top 185 − the block's
    // bottom 169 = 16px (never pinned at any viewport before).
    expect(census!.junction).toEqual({ gap: 16 });

    // The superset invariant: the clone's dashboard stays in-bounds at 390
    // (the reference overflows to 395 — its own documented bug).
    expect(census!.docSW).toBe(390);
  });
});
// ---------------------------------------------------------------------------
// v119 — plan F4 (docs/remediation-plan-v119.md): the /dashboard PAGE-HEADER
// ROW census at 1280 (the pair viewport). The never-pinned family (the
// coverage map: the pair's own below-the-fold surfaces fully pinned by
// v61/v77/v83/v89/v95/v101/v107/v113 — the PAGE header row pinned ONLY at
// 390 before this [the v114 F4 pin: the row's flex chrome + the
// block→button junction + the Add Item button's box chrome; the v62 F2 pin
// the subtitle block's interior — both 390-only]; at 1280 the family only
// POSITION-pinned [the v40 F1 Tab-order census: the Add Item button's band
// x 1121 / w 127 / h 36; the session-5 gradient; the v35 S2 focus shadow;
// the G3 Plus-icon geometry]). Measured BYTE-IDENTICAL on BOTH sides by
// the v119 one-shot census (drow-arbit-v119.sh) — not even a mechanism
// axis diverged (unlike the v118 networth find): the row
// mb-8 flex flex-col justify-between items-start gap-4 md:flex-row
// md:items-center [dashboard-view.tsx:927] renders the same computed
// chrome on both sites at md+. The h1's md:text-4xl tier (36px) is the
// 1280 twin of the 390 pin's text-3xl 30px — the breakpoint pair both
// now pinned. The Add Item band cross-validates the v40 F1 pin exactly
// [1121, 127, 36].
// ---------------------------------------------------------------------------
test.describe("dashboard page-header row census at 1280 (v119 — plan F4)", () => {
  test("the row flex-row/center/gap-4/mb-8 + the h1 36px/700 + the subtitle 16px + the block 498x72 + the Add Item box chrome + the row→grid rhythm 32 (the never-pinned 1280 family — the v114 390 pin's desktop twin)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByRole("heading", { level: 1, name: "Budget Dashboard" })).toBeVisible();

    const census = await page.evaluate(() => {
      // The h1 by its childless text; the block + row via the parent chain;
      // the button by its text within the row — STRUCTURAL finders (the
      // v72 class: the class strings never trusted).
      const h1 = [...document.querySelectorAll("h1")].find(
        (h) => (h.textContent || "").trim() === "Budget Dashboard",
      );
      if (!h1) return null;
      const block = h1.parentElement as HTMLElement | null;
      const row = block?.parentElement as HTMLElement | null;
      if (!block || !row) return null;
      const rcs = getComputedStyle(row);
      const rr = row.getBoundingClientRect();
      const hcs = getComputedStyle(h1);
      const sub = [...block.children].find((c) => c !== h1) as HTMLElement | null;
      const scs = sub ? getComputedStyle(sub) : null;
      const subR = sub ? sub.getBoundingClientRect() : null;
      const btn = [...row.querySelectorAll("button")].find((b) =>
        /Add Item/i.test(b.textContent || ""),
      ) as HTMLElement | undefined;
      const next = row.nextElementSibling;
      const nr = next ? next.getBoundingClientRect() : null;
      const btnOut = btn
        ? (() => {
            const s = getComputedStyle(btn);
            const r = btn.getBoundingClientRect();
            const icon = btn.querySelector("svg");
            const ir = icon ? icon.getBoundingClientRect() : null;
            return {
              left: Math.round(r.left),
              h: Math.round(r.height),
              w: Math.round(r.width),
              pad: s.padding,
              radius: s.borderRadius,
              fs: s.fontSize,
              fw: s.fontWeight,
              color: s.color,
              bg: (s.backgroundImage || "").replace(/\s+/g, " "),
              icon: ir ? { w: Math.round(ir.width), h: Math.round(ir.height) } : null,
            };
          })()
        : null;
      return {
        row: {
          display: rcs.display,
          flexDirection: rcs.flexDirection,
          align: rcs.alignItems,
          justify: rcs.justifyContent,
          gap: rcs.columnGap,
          mb: rcs.marginBottom,
          h: Math.round(rr.height),
          w: Math.round(rr.width),
        },
        h1: {
          fs: hcs.fontSize,
          fw: hcs.fontWeight,
          lh: hcs.lineHeight,
          color: hcs.color,
          h: Math.round(h1.getBoundingClientRect().height),
          mb: hcs.marginBottom,
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
          right: Math.round(block.getBoundingClientRect().right),
        },
        addBtn: btnOut,
        junction: btnOut
          ? { hGap: btnOut.left - Math.round(block.getBoundingClientRect().right) }
          : null,
        nextGap: nr
          ? { gap: Math.round(nr.top - rr.bottom), nextTag: next!.tagName.toLowerCase() }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    if (!census) throw new Error("page-header census found no header row");

    // The row — the md:flex-row tier (the 390 twin's flex-col the other
    // breakpoint; the clone's row carries the mb-8 itself — byte-identical
    // both sides, no construct question this cycle).
    expect(census.row).toEqual({
      display: "flex",
      flexDirection: "row",
      align: "center",
      justify: "space-between",
      gap: "16px",
      mb: "32px",
      h: 72,
      w: 960,
    });
    // The h1 — the md:text-4xl tier (36px; the 390 pin's text-3xl 30px).
    expect(census.h1).toEqual({
      fs: "36px",
      fw: "700",
      lh: "40px",
      color: "rgb(26, 58, 46)",
      h: 40,
      mb: "8px",
    });
    expect(census.subtitle).toEqual({
      fs: "16px",
      fw: "400",
      lh: "24px",
      color: "rgb(107, 114, 128)",
      h: 24,
    });
    // The TEXT BLOCK governs the row height (h1 40 + mb 8 + subtitle 24 =
    // 72; the v65/v69/v118 lesson) and its width is data-stable (the
    // fixed subtitle string).
    expect(census.block).toEqual({ h: 72, w: 498, right: 786 });
    // The Add Item button's BOX chrome — the v114 390 pin's desktop twin;
    // the band [left 1121, w 127, h 36] cross-validates the v40 F1 pin.
    expect(census.addBtn).toEqual({
      left: 1121,
      h: 36,
      w: 127,
      pad: "8px 16px",
      radius: "6px",
      fs: "14px",
      fw: "500",
      color: "rgb(255, 255, 255)",
      bg: "linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))",
      icon: { w: 16, h: 16 },
    });
    // The horizontal junction — the justify-between spread (the block's
    // right → the button's left), data-stable via the fixed strings.
    expect(census.junction).toEqual({ hGap: 335 });
    // The row→stat-grid rhythm — the mb-8 rendered (32px), the next
    // sibling the lg:grid-cols-3 stat grid.
    expect(census.nextGap).toEqual({ gap: 32, nextTag: "div" });
    // The viewport guard.
    expect(census.docSW).toBe(1280);
  });
});
test.describe("quick-action hover end-state census at 1280 (v125 — plan F4)", () => {
  test("the hovered card's tile scale reveal + the plus opacity reveal — the never-pinned hover end-states", async ({ page }) => {
    // The v125 F4 pin: the quick-action family's HOVER END-STATES — the
    // tile's group-hover:scale-110 (dashboard-view.tsx:890) + the plus's
    // group-hover:opacity-100 (:899) — held by NO spec before this pin
    // (the coverage map, read per the SPEC-ALIAS lesson: the v45 F3b pin
    // holds the CARD's hover:shadow-lg layers ONLY — the sole .hover()
    // on the QA surface in the entire suite; the v61 F3 + v107 pins the
    // AT-REST chrome; the v95 pin the transition TIMING metadata, never
    // the end-states). The both-sides census (qahover-arbit-v125.sh):
    // the rendered parity contract IDENTICAL on both sites — the tile
    // 40->44x44 + the plus 0.5->1 — the computed form the documented
    // class (the reference's Tailwind v3 transform matrix(1.1,...) vs
    // the clone's v4 `scale` property — the v95 transition-property
    // class's hover-state twin).
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByRole("button", { name: "Add Income" })).toBeVisible();
    await page.waitForTimeout(400);

    const qa = page.getByRole("button", { name: /^Add Income$/ });
    const readState = () =>
      qa.evaluate((el) => {
        // The tile: the v61 F3 finder (radius 12px, the 30..60 box) —
        // tag-agnostic (the v107 DIV-vs-SPAN lesson: the reference
        // builds the tile as a DIV, the clone as a span).
        const tile = [...el.querySelectorAll("span, div")].find((s) => {
          const cs = getComputedStyle(s);
          const r = s.getBoundingClientRect();
          return cs.borderRadius === "12px" && r.width >= 30 && r.width <= 60 && r.height >= 30 && r.height <= 60;
        });
        const svgs = [...el.querySelectorAll("svg")];
        const plus = svgs[svgs.length - 1];
        if (!tile || !plus) return null;
        const cs = getComputedStyle(tile);
        const r = tile.getBoundingClientRect();
        return {
          cardHover: el.matches(":hover"),
          tile: { transform: cs.transform, scale: cs.scale, w: Math.round(r.width), h: Math.round(r.height) },
          plus: { opacity: getComputedStyle(plus).opacity, w: Math.round(plus.getBoundingClientRect().width) },
        };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5): the v61 F3 contract (the tile 40x40 unscaled, the plus
    // 0.5), establishing the contrast the hover axes need.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({
      cardHover: false,
      tile: { transform: "none", scale: "none", w: 40, h: 40 },
      plus: { opacity: "0.5", w: 16 },
    });

    // THE HOVER END-STATES — the REAL pointer on the card (Playwright's
    // locator hover IS the real pointer move — the v43/v45 idiom): the
    // tile's scale-110 reveal (the rendered 44x44 the parity contract;
    // the clone's v4 `scale` computed form asserted as the clone's own
    // chrome) + the plus's opacity-100 reveal + the card's own :hover
    // state.
    await qa.hover();
    await page.waitForTimeout(400); // the duration-200 transition settle
    const hovered = await readState();
    expect(hovered).toEqual({
      cardHover: true,
      tile: { transform: "none", scale: "1.1", w: 44, h: 44 },
      plus: { opacity: "1", w: 16 },
    });

    // The restore rung — the pointer re-parked at (5,5): both reveals
    // disengaged, the at-rest contract re-established (the v95 timing
    // pin holds the transition metadata; THIS rung holds the restore
    // end-state).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual({
      cardHover: false,
      tile: { transform: "none", scale: "none", w: 40, h: 40 },
      plus: { opacity: "0.5", w: 16 },
    });
  });
});
test.describe("Spending Breakdown donut geometry census at 390 (v126 — plan F4)", () => {
  test("the donut's rendered geometry — the card/wrap/svg boxes + the pie circle's bbox/center/radius (the never-pinned family at any viewport)", async ({ page }) => {
    // The v126 F4 pin: the mobile twin #2's own surface — the Spending
    // Breakdown DONUT'S RENDERED GEOMETRY, held by NO spec at ANY
    // viewport before this pin (the coverage map, read per the
    // SPEC-ALIAS lesson: the v9/v14 pins hold the donut's DATA order +
    // the hover tooltip's sector FILL; the v31 pin the keyboard
    // semantics; the v44 F3 + v49 pins the LEGEND at 1280/390; the v76
    // pin the LABEL CHROME at 1280 [count/fs/lineCount — never the
    // geometry]; the v101 pin the CARD BOX + header at 1280 — the 390
    // header twin rejected as the collision). The both-sides census
    // (donut-arbit-v126.sh): the pie circle 200x200 / r 100
    // byte-identical both sides; the card/wrap/svg heights identical;
    // the width family the documented width-guard class alone (the
    // reference's own 395px overflow vs the clone's fitting 390).
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/dashboard");
    // The settle pattern (the v42 idiom: the card title is a plain div,
    // never a role=heading) + the seeded net-balance text.
    await expect(page.getByText("Spending Breakdown")).toBeVisible();
    await expect(page.getByText("+$2065.00")).toBeVisible();
    await page.waitForTimeout(600);

    const census = await page.evaluate(() => {
      // The card finder — the v78 radius/white walk from the text leaf,
      // TAG-AGNOSTIC (the title is a plain div on both sites).
      const title = [...document.querySelectorAll("div, h1, h2, h3, h4, span, p")].find(
        (e) => (e.textContent || "").trim() === "Spending Breakdown" && e.children.length === 0,
      );
      if (!title) return null;
      let card: HTMLElement | null = title as HTMLElement;
      for (let i = 0; i < 8; i++) {
        card = card!.parentElement as HTMLElement | null;
        if (!card) break;
        const cs = getComputedStyle(card);
        if ((cs.borderRadius && cs.borderRadius !== "0px") || cs.backgroundColor === "rgb(255, 255, 255)") break;
      }
      if (!card) return null;
      const cr = card.getBoundingClientRect();
      const svg = card.querySelector("svg.recharts-surface, svg") as SVGSVGElement | null;
      if (!svg) return null;
      const wrap = svg.parentElement as HTMLElement;
      const wr = wrap.getBoundingClientRect();
      const wcs = getComputedStyle(wrap);
      const sr = svg.getBoundingClientRect();
      const sectors = [...card.querySelectorAll(".recharts-pie-sector path, path.recharts-pie-sector")];
      if (!sectors.length) return null;
      // The pie circle — the UNION BBOX of the sector paths (the
      // rendered diameter/center, never the svg's outer box); the
      // center recomputed RELATIVE TO THE SVG (the v107 local-geometry
      // discipline — never the absolute page position).
      let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
      for (const p of sectors) {
        const r = p.getBoundingClientRect();
        x0 = Math.min(x0, r.x); y0 = Math.min(y0, r.y);
        x1 = Math.max(x1, r.x + r.width); y1 = Math.max(y1, r.y + r.height);
      }
      const bbW = Math.round(x1 - x0);
      const bbH = Math.round(y1 - y0);
      return {
        docSW: document.documentElement.scrollWidth,
        card: { w: Math.round(cr.width), h: Math.round(cr.height) },
        wrap: { w: Math.round(wr.width), h: Math.round(wr.height), pos: wcs.position },
        svg: { w: Math.round(sr.width), h: Math.round(sr.height) },
        pieCircle: {
          w: bbW,
          h: bbH,
          r: Math.round(bbW / 2),
          cxInSvg: Math.round(x0 + bbW / 2 - sr.x),
          cyInSvg: Math.round(y0 + bbH / 2 - sr.y),
        },
        sectorCount: sectors.length,
      };
    });
    expect(census, "the donut census finder (the text leaf -> the radius/white walk)").not.toBeNull();
    if (!census) throw new Error("donut census found no card/svg/sectors");

    // The docSW guard — the clone FITS at 390 (the reference's own 395px
    // overflow the documented width-guard class, the superset invariant).
    expect(census.docSW).toBe(390);

    // The CARD BOX — the 390 width axis (358 = 390 - 2*16 wrapper pad)
    // + the full height (the header + the fixed 300 donut + the legend
    // stack + the p-6 paddings, the seeded 3-slice state).
    expect(census.card).toEqual({ w: 358, h: 656 });

    // The DONUT WRAPPER — the fixed-height ResponsiveContainer box (the
    // width:100% style riding the card's content width; the height the
    // literal 300; the relative position the keyboard-parity anchor).
    expect(census.wrap).toEqual({ w: 308, h: 300, pos: "relative" });

    // The SVG — the recharts surface filling the wrapper exactly (the
    // ResponsiveContainer's fill contract at 390: 308x300).
    expect(census.svg).toEqual({ w: 308, h: 300 });

    // THE PIE CIRCLE — the rendered diameter (200 = outerRadius 100 x 2,
    // the reference's recharts 2.15 and the clone's 3.10 agreeing
    // byte-for-byte) + the CENTERED contract (cxInSvg = svg.w/2 = 154,
    // cyInSvg = svg.h/2 = 150 — the local-geometry discipline).
    expect(census.pieCircle).toEqual({ w: 200, h: 200, r: 100, cxInSvg: 154, cyInSvg: 150 });

    // The settle guard — the seeded 3-slice state (Need/Savings/Want all
    // non-zero). The labelCount/labelLineCount axes are NOT pinned here
    // (the v76 1280 collision discipline — the viewport-invariant count
    // tokens held by the v76 label-chrome pin).
    expect(census.sectorCount).toBe(3);
  });
});
// ---------------------------------------------------------------------------
// v131 — plan F4 (docs/remediation-plan-v131.md): the INTERACTIVE STAT
// CARD's OWN-HOVER REVEAL census at 1280 (the pair's OWN surface — the
// /dashboard view's stat grid). The never-pinned HOVER END-STATES of the
// most-pinned family on the dashboard: the v40 pin holds the TAB stops +
// the geometry bands + the Enter/Space SUPERSET activation (the
// reference's big stat cards are INERT divs — dead UI; the clone's
// route to the type view); the v42 pin the hero grid census; the v51 F2
// pin the AT-REST grid/card/circle/icon chrome; the v88 pin the
// count-row + the h-px divider + the trend colors; the v125 pin the
// QUICK-ACTION cards' hover end-states (dashboard-view.tsx:885-899 — a
// DIFFERENT component family); every chevron pin the DRILL-DOWN family
// [v43/v44]. The stat card's hover end-states — the RADIAL-GRADIENT
// CIRCLE's group-hover:opacity-10 (dashboard-view.tsx:587) + the
// ChevronRight's group-hover:opacity-100 (:602) — held by NO spec at ANY
// viewport before this pin. Measured BYTE-IDENTICAL on BOTH sides by the
// one-shot census stathover-arbit-v131.sh (the hover-ladder form —
// READ-ONLY per the v46 rule: login + passive navigation + a REAL
// pointer hover only; the hover reveals chrome, it clicks nothing — the
// CLONE's card CLICK NAVIGATES to /income, so the card is NEVER
// clicked): the reference's own INERT card carries the SAME reveal
// family (pure-CSS group-hover chrome — absolute top-0 right-0 w-32
// h-32 rounded-full opacity-0 group-hover:opacity-10 + the
// lucide-chevron-right w-5 h-5 opacity-0 group-hover:opacity-100), so
// the reveals are the reference's own idiom — a BOTH-SIDES parity axis,
// NOT a superset axis (only the INTERACTIVITY is superset): the at-rest
// {radial opacity 0, chevron opacity 0} -> the OWN-HOVERED {radial
// opacity 0.1, chevron opacity 1, cardHover true} -> the restored
// at-rest, the transitions opacity 0.3s/0.2s identical (the metadata
// axes recorded in the census, NOT pinned — the v95 family discipline,
// and the v125 pin's own axis-set precedent on the quick-action twin:
// the V94-COLLISION criterion keeps this spec the SOLE failure surface
// for the reveal-family mutation).
// ---------------------------------------------------------------------------
test.describe("stat-card own-hover reveal census at 1280 (v131 — plan F4)", () => {
  test("the Total Income card's own-hover ladder — the at-rest state, the hovered radial-circle + chevron reveals, the restore (the never-pinned hover end-states)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    // the settle pattern (the v40/v51 idiom: the seeded net-balance text
    // before any interaction).
    await expect(page.getByText("+$2065.00")).toBeVisible();
    await page.waitForTimeout(400);

    // The v40 finder — the clone's interactive stat card (the
    // SUPERSET div[role=button]; the reference's is an inert div).
    const card = page.locator('div[role="button"]').filter({ hasText: "Total Income" });
    await expect(card).toBeVisible();

    // STRUCTURAL finders (tag/class-agnostic by computed shape, per the
    // v107 lesson): the RADIAL = the absolute 9999px-radius decorative
    // div; the CHEVRON = the 19..21 width band (state-INDEPENDENT across
    // the ladder's rungs — the type icon is w-6 = 24px, the trend icon
    // w-4 = 16px; the at-rest opacity-0 form would FAIL on the hovered
    // rung, the opacity being the animated axis this pin measures).
    const readState = () =>
      card.evaluate((el) => {
        const radial = [...el.querySelectorAll("div")].find((d) => {
          const cs = getComputedStyle(d);
          return cs.position === "absolute" && cs.borderRadius === "9999px";
        });
        const chevron = [...el.querySelectorAll("svg")].find((s) => {
          const r = s.getBoundingClientRect();
          return r.width >= 19 && r.width <= 21;
        });
        if (!radial || !chevron) return null;
        return {
          cardHover: el.matches(":hover"),
          radial: { opacity: getComputedStyle(radial).opacity },
          chevron: { opacity: getComputedStyle(chevron).opacity },
        };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): both reveals retired (opacity 0), the
    // contrast the hover axes need.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({
      cardHover: false,
      radial: { opacity: "0" },
      chevron: { opacity: "0" },
    });

    // THE HOVER END-STATES — the REAL pointer on the card (Playwright's
    // locator hover IS the real pointer move — the v43/v45/v125 idiom):
    // the radial's group-hover:opacity-10 reveal + the chevron's
    // group-hover:opacity-100 reveal + the card's own :hover state. The
    // card is NEVER clicked (the v46 rule — the click navigates).
    await card.hover();
    await page.waitForTimeout(400); // the 0.3s transition settle
    const hovered = await readState();
    expect(hovered).toEqual({
      cardHover: true,
      radial: { opacity: "0.1" },
      chevron: { opacity: "1" },
    });

    // The restore rung — the pointer re-parked at (5,5): both reveals
    // disengaged, the at-rest contract re-established.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual({
      cardHover: false,
      radial: { opacity: "0" },
      chevron: { opacity: "0" },
    });
  });
});
