import { test, expect } from "@playwright/test";

// v28 G3 (docs/remediation-plan-v28.md): the Budget Item Details sheet —
// the reference opens a read-only details dialog on ITEM-CARD BODY CLICK
// (any type, desktop AND mobile: overlay `fixed inset-0 z-50 flex
// items-end md:items-center justify-center p-0 md:p-4` — bottom-sheet at
// mobile — panel `bg-white rounded-t-3xl md:rounded-2xl shadow-2xl
// max-w-lg w-full max-h-[85vh] overflow-y-auto`). The clone's card click
// was a dead surface before this iteration. All geometry/classes/colors
// below were measured live on the reference this session.

test.describe("budget item details sheet (v28 — plan G3)", () => {
  test("clicking an expense card body opens the details sheet with the reference's structure", async ({ page }) => {
    await page.goto("/expenses");
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await expect(rent).toBeVisible();

    // The card BODY click (not the buttons) opens the details sheet.
    await rent.locator("h4").click();

    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    await expect(dialog.getByRole("heading", { name: "Budget Item Details" })).toBeVisible();

    // The overlay + panel geometry family (measured on the reference):
    // forest-dark 50% overlay + blur, bottom-sheet anchored at mobile,
    // centered 512px (max-w-lg) at desktop, 85vh cap, t-3xl/2xl radii.
    // The dialog (role=dialog) IS the panel; the overlay is its portal
    // sibling (Radix renders overlay + content side by side).
    const overlayInfo = await dialog.evaluate((el) => {
      const overlay = [...el.parentElement!.children].find(
        (c) => c !== el && /inset-0/.test(c.className),
      ) as HTMLElement | null;
      return {
        overlayCls: overlay ? overlay.className : null,
        overlayBg: overlay ? getComputedStyle(overlay).backgroundColor : null,
        overlayBlur: overlay ? getComputedStyle(overlay).backdropFilter : null,
        panelCls: el.className,
        panelMaxW: getComputedStyle(el).maxWidth,
      };
    });
    expect(overlayInfo.overlayBg).toBe("rgba(26, 58, 46, 0.5)");
    expect(overlayInfo.overlayBlur).toContain("blur(8px)");
    // The panel self-positions: bottom-anchored full-width sheet at mobile,
    // centered at md: (the reference achieves the same geometry via its
    // items-end/md:items-center flex overlay — the computed positions are
    // identical; pinned here on the panel's own class family).
    expect(overlayInfo.panelCls).toContain("max-w-lg");
    expect(overlayInfo.panelCls).toContain("max-h-[85vh]");
    expect(overlayInfo.panelCls).toContain("rounded-t-3xl");
    expect(overlayInfo.panelCls).toContain("md:rounded-2xl");
    expect(overlayInfo.panelCls).toContain("bottom-0");
    expect(overlayInfo.panelCls).toContain("md:top-1/2");
    expect(overlayInfo.panelMaxW).toBe("512px");

    // The sticky header + the X close (the v27 ghost-icon family).
    const header = dialog.locator("div.sticky");
    await expect(header).toBeVisible();
    const x = header.getByRole("button");
    await expect(x).toHaveClass(/focus-visible:ring-1/);
    await expect(x).toHaveClass(/hover:text-accent-foreground/);

    // The summary: type + classification badges, name, type-colored amount.
    await expect(dialog.getByText("EXPENSE", { exact: true })).toBeVisible();
    await expect(dialog.getByText("NEED", { exact: true })).toBeVisible();
    await expect(dialog.getByRole("heading", { name: "Rent", level: 3 })).toBeVisible();
    const amount = dialog.getByText("$1850.00");
    await expect(amount).toBeVisible();
    await expect(amount).toHaveClass(/text-4xl/);
    await expect(amount).toHaveClass(/font-bold/);

    // The type badge + amount carry the expense orange (measured
    // rgb(224, 122, 59) on the reference).
    const colors = await dialog.evaluate((el) => {
      const badge = [...el.querySelectorAll("div, span")].find(
        (d) => (d.textContent || "").trim() === "EXPENSE",
      );
      const amt = [...el.querySelectorAll("p")].find((p) =>
        /^\$[\d,]/.test((p.textContent || "").trim()),
      );
      return {
        badgeBg: badge ? getComputedStyle(badge).backgroundColor : null,
        badgeColor: badge ? getComputedStyle(badge).color : null,
        badgeCls: badge ? badge.className : null,
        amountColor: amt ? getComputedStyle(amt).color : null,
      };
    });
    expect(colors.badgeBg).toBe("rgba(224, 122, 59, 0.125)");
    expect(colors.badgeColor).toBe("rgb(224, 122, 59)");
    expect(colors.badgeCls).toContain("rounded-full");
    expect(colors.amountColor).toBe("rgb(224, 122, 59)");

    // The classification block: tinted rounded-xl, 20px icon, per-cls color.
    const clsBlock = dialog.locator("div.rounded-xl.p-4");
    await expect(clsBlock).toBeVisible();
    await expect(clsBlock.getByText("Need", { exact: true })).toBeVisible();
    await expect(
      clsBlock.getByText("Essential expenses like rent, utilities, and groceries"),
    ).toBeVisible();
    const clsInfo = await clsBlock.evaluate((el) => ({
      bg: getComputedStyle(el).backgroundColor,
      title: getComputedStyle(el.querySelector("p.font-semibold")!).color,
      iconW: Math.round(el.querySelector("svg")!.getBoundingClientRect().width),
    }));
    expect(clsInfo.bg).toBe("rgb(255, 247, 245)");
    expect(clsInfo.title).toBe("rgb(224, 122, 59)");
    expect(clsInfo.iconW).toBe(20);

    // The facts: Date / Frequency / Recurring / Status — Rent has NO notes,
    // so the Notes fact must NOT render (measured conditional).
    await expect(dialog.getByText("Date", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Frequency", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Recurring", { exact: true })).toBeVisible();
    await expect(dialog.getByText("monthly", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Yes", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Status", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Notes", { exact: true })).toHaveCount(0);

    // The meta footer: Created + Last Updated (12px forest values).
    await expect(dialog.getByText("Created", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Last Updated", { exact: true })).toBeVisible();

    // The X closes the sheet.
    await x.click();
    await expect(dialog).toBeHidden();
  });

  test("the income card's sheet shows the lime family, the Recurring fact, and Notes when present", async ({ page }) => {
    await page.goto("/income");
    const salary = page.locator("div.rounded-xl").filter({ hasText: "Salary" }).first();
    await expect(salary).toBeVisible();
    await salary.locator("h4").click();

    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();

    await expect(dialog.getByText("INCOME", { exact: true })).toBeVisible();
    const colors = await dialog.evaluate((el) => {
      const badge = [...el.querySelectorAll("div, span")].find(
        (d) => (d.textContent || "").trim() === "INCOME",
      );
      const amt = [...el.querySelectorAll("p")].find((p) =>
        /^\$[\d,]/.test((p.textContent || "").trim()),
      );
      return {
        badgeBg: badge ? getComputedStyle(badge).backgroundColor : null,
        badgeColor: badge ? getComputedStyle(badge).color : null,
        amountColor: amt ? getComputedStyle(amt).color : null,
      };
    });
    // The income lime family (measured rgb(143, 188, 63)).
    expect(colors.badgeBg).toBe("rgba(143, 188, 63, 0.125)");
    expect(colors.badgeColor).toBe("rgb(143, 188, 63)");
    expect(colors.amountColor).toBe("rgb(143, 188, 63)");

    // The seeded Salary carries notes — the Notes fact renders with them.
    await expect(dialog.getByText("Notes", { exact: true })).toBeVisible();
    await expect(dialog.getByText("Net monthly salary")).toBeVisible();

    // The name + subcategory surface in the summary.
    await expect(dialog.getByRole("heading", { name: "Salary", level: 3 })).toBeVisible();
  });

  test("the action buttons still act — the card click does not shadow Edit", async ({ page }) => {
    await page.goto("/expenses");
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    // The footer Edit button opens the EDIT dialog (its own action), not
    // the details sheet.
    await rent.hover();
    await rent.getByRole("button", { name: "Edit", exact: true }).click();
    const editDialog = page.getByRole("dialog");
    await expect(editDialog).toBeVisible();
    // The edit dialog's own header (not the details sheet's).
    await expect(editDialog.getByText(/Add Budget Item|Edit Budget Item|Budget Item/)).toBeVisible();
    await expect(editDialog.getByRole("heading", { name: "Budget Item Details" })).toHaveCount(0);
  });

  // v30 G1 (docs/remediation-plan-v30.md): the sheet's KEYBOARD semantics —
  // measured live on both sites in v29 (desktop) and v30 (mobile). The
  // reference opens with NO initial focus (activeElement stays BODY), no
  // role/aria-modal, and a real Tab walk tours the ENTIRE underlying page
  // (stops 1–14: the sidebar links, Add Expense, the filter triggers, the
  // cards' Edit/Calculate buttons) — its sheet never traps and its single
  // focusable (the X) is reachable only after every page element. The
  // clone (Radix) is the documented accessible superset: initial focus ON
  // the X, full Tab containment, Escape close. Nothing pinned these before.
  test("the sheet's keyboard semantics: initial focus on X, Tab traps, Escape closes", async ({ page }) => {
    await page.goto("/expenses");
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await expect(rent).toBeVisible();
    await rent.locator("h4").click();

    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    await expect(dialog.getByRole("heading", { name: "Budget Item Details" })).toBeVisible();
    // Radix's open animation settle before reading programmatic focus.
    await page.waitForTimeout(300);

    // Initial focus lands on the X (the sr-only "Close" text — the v29
    // probe lesson: the clone's X has no aria-label).
    const initialFocus = await page.evaluate(() => {
      const el = document.activeElement;
      if (!el || el === document.body) return null;
      return {
        tag: el.tagName,
        txt: (el.textContent || "").trim(),
        inDialog: !!el.closest('[role="dialog"]'),
      };
    });
    expect(initialFocus).not.toBeNull();
    expect(initialFocus!.txt).toBe("Close");
    expect(initialFocus!.inDialog).toBe(true);

    // The trap: every Tab stop stays inside the dialog (the reference's
    // stops 1–14 tour the underlying page — activeInSheet: false).
    const stops: Array<{ txt: string; inDialog: boolean }> = [];
    for (let i = 0; i < 3; i++) {
      await page.keyboard.press("Tab");
      await page.waitForTimeout(60);
      stops.push(
        await page.evaluate(() => {
          const el = document.activeElement;
          return {
            txt: el && el !== document.body ? (el.textContent || "").trim().slice(0, 24) : "(body)",
            inDialog: !!(el && el.closest('[role="dialog"]')),
          };
        }),
      );
    }
    for (const stop of stops) {
      expect(stop.inDialog).toBe(true);
    }

    // Escape closes (the reference's sheet ignores it).
    await page.keyboard.press("Escape");
    await expect(dialog).toBeHidden();
  });

  // v30 G1 (mobile variant): the same keyboard contract at the bottom-sheet
  // breakpoint, plus the computed mobile geometry measured on BOTH sites in
  // v30 (the reference's inner panel and the clone's self-positioned panel
  // compute the identical rectangle: x=0, y=127, w=390, h=717 with max-h
  // 85vh = 717.4px).
  test("the keyboard trap + bottom-sheet geometry hold at MOBILE (390x844)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/expenses");
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await expect(rent).toBeVisible();
    await rent.locator("h4").click();

    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(300);

    // The bottom-sheet geometry (measured on both sites, byte-identical).
    const geom = await dialog.evaluate((el) => {
      const r = el.getBoundingClientRect();
      const cs = getComputedStyle(el);
      return {
        x: Math.round(r.x),
        y: Math.round(r.y),
        w: Math.round(r.width),
        maxH: cs.maxHeight,
        overflowY: cs.overflowY,
      };
    });
    expect(geom.x).toBe(0);
    expect(geom.w).toBe(390);
    expect(geom.maxH).toBe("717.4px"); // 85% of 844
    expect(geom.overflowY).toBe("auto");

    // The trap holds at mobile: initial focus on the X, Tab stays inside.
    const initialFocus = await page.evaluate(() => {
      const el = document.activeElement;
      return el && el !== document.body ? (el.textContent || "").trim() : null;
    });
    expect(initialFocus).toBe("Close");
    await page.keyboard.press("Tab");
    await page.waitForTimeout(60);
    const inDialog = await page.evaluate(() => {
      const el = document.activeElement;
      return !!(el && el.closest('[role="dialog"]'));
    });
    expect(inDialog).toBe(true);

    await page.keyboard.press("Escape");
    await expect(dialog).toBeHidden();
  });
});

test.describe("item-details shadow-2xl census (v48 — plan F1)", () => {
  test("the details panel carries the reference's v3 shadow-2xl visible layer (the net's seventh site)", async ({ page }) => {
    // Session-108 queue #1, measured live on BOTH sites (v48): the
    // reference's details panel composes 2 transparent leads + the v3
    // shadow-2xl layer `rgba(0,0,0,0.25) 0px 25px 50px -12px`; the
    // clone's shadow-2xl composes 4 transparent leads + the SAME
    // visible layer (v4's 5-slot construction — the accepted
    // v10/v25/v45 lead-divergence class, this time at the 2xl end on
    // the details surface). The panel: w 512 (max-w-lg) / h 680 (the
    // 85vh cap at an 800 viewport) / radius 16 (md:rounded-2xl) / bg
    // white. The overlay: the v7 G6 forest scrim rgba(26,58,46,0.5) +
    // z 50 + blur(8px) — re-verified live in the same sweep. The close
    // button: the v9 36x36 in-header X family, re-verified.
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/income");
    await expect(page.getByRole("heading", { name: "Salary" })).toBeVisible();
    const card = page.locator("div.rounded-xl").filter({ hasText: "Salary" }).first();
    await card.locator("h4").click();
    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();

    const census = await dialog.evaluate((el) => {
      const panel = el as HTMLElement;
      const ps = getComputedStyle(panel);
      const layerCount = (ps.boxShadow.match(/px, /g) || []).length + 1;
      const overlay = [...panel.parentElement!.children].find(
        (c) => c !== panel && /inset-0/.test(c.className),
      ) as HTMLElement | null;
      const os = overlay ? getComputedStyle(overlay) : null;
      // The in-header X (the v9 family): its accessible name is "Close"
      // via the sr-only span (the v28 keyboard test's initial-focus idiom).
      const closeBtn = [...panel.querySelectorAll("button")].find(
        (b) => (b.textContent || "").trim() === "Close",
      );
      const cb = closeBtn ? getComputedStyle(closeBtn) : null;
      const r = panel.getBoundingClientRect();
      return {
        w: Math.round(r.width),
        h: Math.round(r.height),
        radius: ps.borderRadius,
        maxW: ps.maxWidth,
        bg: ps.backgroundColor,
        shadow: ps.boxShadow,
        layerCount,
        overlay: os
          ? { bg: os.backgroundColor, z: os.zIndex, blur: os.backdropFilter }
          : null,
        closeBtn: cb
          ? {
              w: Math.round(closeBtn!.getBoundingClientRect().width),
              h: Math.round(closeBtn!.getBoundingClientRect().height),
              radius: cb.borderRadius,
              bg: cb.backgroundColor,
              borderW: cb.borderWidth,
            }
          : null,
      };
    });

    // The panel geometry (measured identical on both sites at 1280x800).
    expect(census.w).toBe(512);
    expect(census.h).toBe(680); // the 85vh cap
    expect(census.radius).toBe("16px");
    expect(census.maxW).toBe("512px");
    expect(census.bg).toBe("rgb(255, 255, 255)");
    // THE SHADOW: the v3 2xl VISIBLE layer + the v4 5-slot count.
    expect(census.shadow).toContain("rgba(0, 0, 0, 0.25) 0px 25px 50px -12px");
    expect(census.layerCount).toBe(5);
    // The overlay: the forest scrim, z 50, blur(8px).
    expect(census.overlay!.bg).toBe("rgba(26, 58, 46, 0.5)");
    expect(census.overlay!.z).toBe("50");
    expect(census.overlay!.blur).toContain("blur(8px)");
    // The close button: the 36x36 transparent X.
    expect(census.closeBtn!.w).toBe(36);
    expect(census.closeBtn!.h).toBe(36);
    expect(census.closeBtn!.radius).toBe("6px");
    expect(census.closeBtn!.bg).toBe("rgba(0, 0, 0, 0)");

    await page.keyboard.press("Escape");
    await expect(dialog).toBeHidden();
  });
});

// v52 F1 (docs/remediation-plan-v52.md): the summary's FIFTH element —
// the subcategory P. Measured live on the reference this session (the
// Rent sheet on /expenses + the Salary sheet on /income, both via the
// card-body click at 390): the summary renders chip row → H3 (name,
// text-2xl font-bold mb-2, 24/700/forest) → the SUBCATEGORY P
// (`text-lg`, 18/400/rgb(107,114,128) — Rent → "Apartment", Salary →
// "Main Job") → the amount P (text-4xl font-bold mt-4). The clone
// rendered the H3 → the amount directly (the field was never wired
// into the details view — the card and the edit dialog both render
// it). The one-insert fix lands between the H3 and the amount.

test.describe("details summary subcategory census (v52 — plan F1)", () => {
  test("the summary renders the subcategory P between the H3 and the amount", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/income");
    const salary = page.locator("div.rounded-xl").filter({ hasText: "Salary" }).first();
    await expect(salary).toBeVisible();
    await salary.locator("h4").click();

    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(300);

    // The subcategory P: visible, the seeded "Main Job", the
    // reference's chrome (text-lg, 18/400/rgb(107,114,128)).
    const sub = dialog.locator("p.text-lg");
    await expect(sub).toBeVisible();
    await expect(sub).toHaveText("Main Job");
    const subInfo = await sub.evaluate((el) => {
      const cs = getComputedStyle(el);
      return { fs: cs.fontSize, fw: cs.fontWeight, color: cs.color };
    });
    expect(subInfo.fs).toBe("18px");
    expect(subInfo.fw).toBe("400");
    expect(subInfo.color).toBe("rgb(107, 114, 128)");

    // The DOM sequence: the H3 name → the subcategory P → the amount.
    const seq = await dialog.evaluate((el) => {
      const h3 = el.querySelector("h3");
      const subP = [...el.querySelectorAll("p")].find(
        (p) => (p.textContent || "").trim() === "Main Job",
      );
      const amount = [...el.querySelectorAll("p")].find((p) =>
        /^\$[\d,]/.test((p.textContent || "").trim()),
      );
      if (!h3 || !subP || !amount) return { h3: !!h3, subP: !!subP, amount: !!amount };
      const all = [...el.querySelectorAll("h3, p")];
      return {
        h3Idx: all.indexOf(h3),
        subIdx: all.indexOf(subP),
        amountIdx: all.indexOf(amount),
      };
    });
    expect(seq.h3Idx).toBeDefined();
    expect(seq.subIdx).toBeGreaterThan(seq.h3Idx!);
    expect(seq.amountIdx).toBeGreaterThan(seq.subIdx!);

    await page.keyboard.press("Escape");
    await expect(dialog).toBeHidden();
  });
});

// v52 F4 (docs/remediation-plan-v52.md): the details sheet's INTERNALS
// at 390 — the census beyond the v28/v48 panel pins (those walked the
// panel chrome + the bottom-sheet geometry; the internals were never
// pinned). Every value below was measured live on BOTH sites this
// session (byte-identical unless noted).

test.describe("details sheet internals census (v52 — plan F4)", () => {
  test("the panel internals carry the reference's chrome at 390", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/expenses");
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await expect(rent).toBeVisible();
    await rent.locator("h4").click();

    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(400);

    const census = await dialog.evaluate((el) => {
      const ps = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      // the sticky header (the first child) + the body (the p-6 stack)
      const header = [...el.children].find(
        (c) => /sticky/.test((c.className || "").toString()),
      ) as HTMLElement | null;
      const hcs = header ? getComputedStyle(header) : null;
      const body = [...el.children].find((c) =>
        /space-y-6/.test((c.className || "").toString()),
      ) as HTMLElement | null;
      const bcs = body ? getComputedStyle(body) : null;
      // the title + the close button live in the header
      const title = header?.querySelector("h2, h3");
      const closeBtn = header ? [...header.querySelectorAll("button")].pop() : null;
      // the summary block (the body's first child)
      const summary = body?.firstElementChild as HTMLElement | null;
      const chipRow = summary?.firstElementChild as HTMLElement | null;
      const chip = chipRow?.querySelector("span, div");
      // the classification block (the rounded-xl p-4 tinted tile)
      const clsBlock = [...(body?.querySelectorAll("div") || [])].find(
        (d) => /rounded-xl/.test((d.className || "").toString()) && /p-4/.test((d.className || "").toString()),
      ) as HTMLElement | null;
      // the facts container (space-y-4) + its first row
      const facts = [...(body?.children || [])].find(
        (c) => /space-y-4/.test((c.className || "").toString()),
      ) as HTMLElement | null;
      const factRow = facts?.querySelector("div.flex");
      // the meta footer (border-t)
      const footer = [...(body?.children || [])].find(
        (c) => /border-t/.test((c.className || "").toString()),
      ) as HTMLElement | null;
      const fLabel = footer?.querySelector("p");
      return {
        panel: {
          x: Math.round(r.x),
          w: Math.round(r.width),
          radius: ps.borderRadius,
          maxH: ps.maxHeight,
          bg: ps.backgroundColor,
          overflowY: ps.overflowY,
          shadow: ps.boxShadow,
        },
        header: hcs
          ? {
              h: Math.round(header!.getBoundingClientRect().height),
              pad: hcs.padding,
              pos: hcs.position,
              top: hcs.top,
              borderB: hcs.borderBottom,
              bg: hcs.backgroundColor,
            }
          : null,
        title: title
          ? {
              fs: getComputedStyle(title).fontSize,
              fw: getComputedStyle(title).fontWeight,
              color: getComputedStyle(title).color,
            }
          : null,
        closeBtn: closeBtn
          ? {
              w: Math.round(closeBtn.getBoundingClientRect().width),
              h: Math.round(closeBtn.getBoundingClientRect().height),
            }
          : null,
        body: bcs ? { cls: (body!.className || "").toString(), pad: bcs.padding } : null,
        chipRow: chipRow
          ? {
              gap: getComputedStyle(chipRow).gap,
              mb: getComputedStyle(chipRow).marginBottom,
              justify: getComputedStyle(chipRow).justifyContent,
            }
          : null,
        chip: chip
          ? {
              fs: getComputedStyle(chip).fontSize,
              fw: getComputedStyle(chip).fontWeight,
              color: getComputedStyle(chip).color,
              cls: (chip.className || "").toString(),
              pad: getComputedStyle(chip).padding,
            }
          : null,
        clsBlock: clsBlock
          ? {
              radius: getComputedStyle(clsBlock).borderRadius,
              pad: getComputedStyle(clsBlock).padding,
            }
          : null,
        factRow: factRow
          ? {
              cls: (factRow.className || "").toString().slice(0, 40),
              gap: getComputedStyle(factRow).gap,
              pad: getComputedStyle(factRow).padding,
            }
          : null,
        footer: footer
          ? {
              cls: (footer.className || "").toString().slice(0, 30),
              pt: getComputedStyle(footer).paddingTop,
              borderT: getComputedStyle(footer).borderTopWidth,
              labelFs: fLabel ? getComputedStyle(fLabel).fontSize : null,
              labelColor: fLabel ? getComputedStyle(fLabel).color : null,
            }
          : null,
      };
    });

    // The panel: the 390 bottom-sheet chrome (v48's mobile re-measure).
    expect(census.panel!.x).toBe(0);
    expect(census.panel!.w).toBe(390);
    expect(census.panel!.radius).toBe("24px 24px 0px 0px");
    expect(census.panel!.maxH).toBe("717.4px");
    expect(census.panel!.bg).toBe("rgb(255, 255, 255)");
    expect(census.panel!.overflowY).toBe("auto");
    expect(census.panel!.shadow).toContain("rgba(0, 0, 0, 0.25) 0px 25px 50px -12px");

    // The sticky header: h 69 (py-4 16 + the 18px title line + border).
    expect(census.header!.h).toBe(69);
    expect(census.header!.pad).toBe("16px 24px");
    expect(census.header!.pos).toBe("sticky");
    expect(census.header!.top).toBe("0px");
    expect(census.header!.borderB).toBe("1px solid rgb(229, 231, 227)");
    expect(census.header!.bg).toBe("rgb(255, 255, 255)");

    // The title + the close (the v9 36x36 X family).
    expect(census.title!.fs).toBe("18px");
    expect(census.title!.fw).toBe("700");
    expect(census.title!.color).toBe("rgb(26, 58, 46)");
    expect(census.closeBtn!.w).toBe(36);
    expect(census.closeBtn!.h).toBe(36);

    // The body: space-y-6 p-6.
    expect(census.body!.cls).toContain("space-y-6");
    expect(census.body!.pad).toBe("24px");

    // The summary's chip row: centered, gap 8 (gap-2), mb 12 (mb-3).
    expect(census.chipRow!.gap).toBe("8px");
    expect(census.chipRow!.mb).toBe("12px");
    expect(census.chipRow!.justify).toBe("center");
    // The chips: 12/500 in the expense orange, rounded-full, px-3 py-1.
    expect(census.chip!.fs).toBe("12px");
    expect(census.chip!.fw).toBe("500");
    expect(census.chip!.color).toBe("rgb(224, 122, 59)");
    // rounded-full: the v3 reference computes 9999px, the v4 clone
    // 3.35544e+07px — both fully-round pills (the class is the contract).
    expect(census.chip!.cls).toContain("rounded-full");
    expect(census.chip!.pad).toBe("4px 12px");

    // The classification block: rounded-xl p-4 (the tinted tile).
    expect(census.clsBlock!.radius).toBe("12px");
    expect(census.clsBlock!.pad).toBe("16px");

    // The fact rows: flex gap-3 (12px) py-2 (8px 0px).
    expect(census.factRow!.gap).toBe("12px");
    expect(census.factRow!.pad).toBe("8px 0px");

    // The meta footer: border-t, pt 16, the labels 12/gray.
    expect(census.footer!.pt).toBe("16px");
    expect(census.footer!.borderT).toBe("1px");
    expect(census.footer!.labelFs).toBe("12px");
    expect(census.footer!.labelColor).toBe("rgb(107, 114, 128)");

    await page.keyboard.press("Escape");
    await expect(dialog).toBeHidden();
  });
});
