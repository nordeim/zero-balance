#!/usr/bin/env python3
"""Append the v121 describe block to tests/e2e/items.spec.ts (the
line-append form — the v112 dashboard.spec precedent + the v120 networth
precedent: the file is ~4.6k lines, the Edit old_str is unwieldy; the
block appended at EOF)."""

BLOCK = r'''

// ---------------------------------------------------------------------------
// v121 — plan F4 (docs/remediation-plan-v121.md): the ITEM-CARD's inline
// CONFIRM-BAR census at 1280 (the pair's OWN first surface — the /income
// view). The never-pinned twin of the pinned confirm-bar family (the v120
// LIABILITY-TWIN precedent form): the v46 F3 pin holds the /networth
// instances ("Delete this asset?" — the bar box + the label + the
// cancelPill + the deleteBtn + the shadow-sm regression net); the
// ITEM-CARD instance — the income/savings cards' "Delete this item?" bar
// — held by NO spec (every existing confirm-bar assertion in the items
// specs is BEHAVIORAL only: the text visibility, the click paths, the
// failed-delete toast). The reference has NO confirm bars at all (its
// card-menu Delete destroys immediately — its R6 bug), so no both-sides
// census is possible: the pin locks the CLONE's own superset chrome
// (the v46 F3 adapted form). The family chrome = the v46 F3 contract BY
// CONSTRUCTION (the identical class strings: item-card.tsx:210 vs
// net-worth-view.tsx:124/235); the item-card-only axes: the label text
// "Delete this item?", the bar's width 267 (the pinned card 309 - the 40
// p-5 - the 2px border), and the BAR-OPEN DELTA (the cardAtRest 230 ->
// the cardWithBar 310 = +80 = the mt 16 + the bar 64 — the arithmetic
// exact, the data-independent chrome delta).
// The colors (the label red-700 / the delete bg red-600) read lab() in
// Tailwind v4 (the named-palette drift class) — deliberately NOT
// asserted, the v46 F3 family form (the engine-independence discipline).
// The FIRST candidate (the expenses filter md-band state at 800 —
// measured byte-identical both sides) was REJECTED by the live
// sole-failure test: the v1-era items.spec.ts:622 asserts the RAW
// md:grid-cols-2 CLASS TOKEN, so the line-175 mutation reds both (the
// SPEC-ALIAS COVERAGE lesson re-hit, the v116 first-attempt precedent).
// ---------------------------------------------------------------------------
test.describe("item-card inline confirm-bar census at 1280 (v121 — plan F4)", () => {
  test("the income card's Delete-this-item bar — the box, the label, the Cancel pill + the shadow-sm, the Delete twin, the +80 bar-open delta (the never-pinned family twin)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/income");
    // the settle pattern: wait for the seeded card before interacting
    const card = page.locator("div.rounded-xl").filter({ hasText: "Salary" }).first();
    await expect(card).toBeVisible();

    // The at-rest height FIRST (the bar-open delta's baseline — the
    // seeded Salary card's 230, the v79 pin's own value).
    const atRest = await card.evaluate((el) => Math.round(el.getBoundingClientRect().height));
    expect(atRest).toBe(230);

    // The native click opens the Radix menu (the v46 lesson: synthetic
    // el.click() does NOT open it — Radix ignores non-pointer events;
    // Playwright's locator click IS the full pointer sequence).
    await card.hover();
    await card.getByRole("button", { name: "Actions for Salary" }).click();
    await page.getByRole("menuitem", { name: "Delete" }).click();
    await expect(card.getByText("Delete this item?")).toBeVisible();

    const census = await page.evaluate(() => {
      // The confirm bar — STRUCTURAL finders (the v46 F3 finder family:
      // the bg + the Cancel/Delete button pair; the class strings not
      // trusted for the walk).
      const bar = [...document.querySelectorAll("div")].find((d) => {
        const bcs = getComputedStyle(d);
        if (bcs.backgroundColor !== "rgb(254, 242, 242)") return false;
        const btns = [...d.querySelectorAll("button")];
        return (
          btns.length === 2 &&
          (btns[0].textContent || "").trim() === "Cancel" &&
          (btns[1].textContent || "").trim() === "Delete"
        );
      });
      if (!bar) return null;
      const bcs = getComputedStyle(bar);
      const br = bar.getBoundingClientRect();
      const label = bar.querySelector("p");
      const cancel = [...bar.querySelectorAll("button")].find(
        (b) => (b.textContent || "").trim() === "Cancel",
      )!;
      const del = [...bar.querySelectorAll("button")].find(
        (b) => (b.textContent || "").trim() === "Delete",
      )!;
      const ccs = getComputedStyle(cancel);
      const dcs = getComputedStyle(del);
      return {
        bar: {
          mt: bcs.marginTop,
          display: bcs.display,
          align: bcs.alignItems,
          justify: bcs.justifyContent,
          radius: bcs.borderRadius,
          pad: bcs.padding,
          bg: bcs.backgroundColor,
          w: Math.round(br.width),
        },
        label: label
          ? {
              fs: getComputedStyle(label).fontSize,
              fw: getComputedStyle(label).fontWeight,
              text: (label.textContent || "").trim(),
            }
          : null,
        cancelPill: {
          bg: ccs.backgroundColor,
          pad: ccs.padding,
          radius: ccs.borderRadius,
          fs: ccs.fontSize,
          fw: ccs.fontWeight,
          h: Math.round(cancel.getBoundingClientRect().height),
          boxShadow: ccs.boxShadow,
        },
        deleteBtn: {
          color: dcs.color,
          pad: dcs.padding,
          radius: dcs.borderRadius,
          fs: dcs.fontSize,
          fw: dcs.fontWeight,
          h: Math.round(del.getBoundingClientRect().height),
        },
      };
    });
    expect(census).not.toBeNull();

    // The bar chrome — the v46 F3 family contract (the identical class
    // strings to the networth twins): the red-tinted row + the item-card
    // width consequence (267 = the pinned 309 - the 40 p-5 - the 2px
    // border).
    expect(census!.bar).toEqual({
      mt: "16px",
      display: "flex",
      align: "center",
      justify: "space-between",
      radius: "8px",
      pad: "12px",
      bg: "rgb(254, 242, 242)",
      w: 267,
    });

    // The label — the item-card-only text (the asset twin reads "Delete
    // this asset?"); the color deliberately NOT asserted (the lab()
    // named-palette drift — the v46 F3 family form).
    expect(census!.label).toEqual({ fs: "14px", fw: "400", text: "Delete this item?" });

    // The Cancel pill: the white bg + the 4/12 pad + the 6px radius + the
    // 12px-500 + h 24 — and THE PIN: the shadow-sm VISIBLE layer
    // `rgba(0, 0, 0, 0.05) 0px 1px 2px 0px` (the --shadow-sm theme pin's
    // restored v3 value — the regression net's sixth site, the v45/v46
    // family; toContain = the accepted-leads convention, the v10 lesson).
    expect(census!.cancelPill).toMatchObject({
      bg: "rgb(255, 255, 255)",
      pad: "4px 12px",
      radius: "6px",
      fs: "12px",
      fw: "500",
      h: 24,
    });
    expect(census!.cancelPill.boxShadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // The Delete twin: the same pad/radius/font family, white text, h 24
    // (the bg deliberately NOT asserted — the red-600 lab() drift).
    expect(census!.deleteBtn).toMatchObject({
      color: "rgb(255, 255, 255)",
      pad: "4px 12px",
      radius: "6px",
      fs: "12px",
      fw: "500",
      h: 24,
    });

    // The BAR-OPEN DELTA — the data-independent chrome arithmetic: the
    // card grows by exactly the mt 16 + the bar 64 = +80 (the at-rest
    // 230 -> the bar-open 310; the label's 2-line wrap at the 267 content
    // width is data-stable for the fixed strings — the seeded Salary
    // card's own census).
    const withBar = await card.evaluate((el) => Math.round(el.getBoundingClientRect().height));
    expect(withBar - atRest).toBe(80);

    // The fixture-restore discipline: Cancel dismisses the bar (the
    // delete NEVER fires — the census ran while the bar was up) and the
    // card returns to its at-rest height.
    await card.getByRole("button", { name: "Cancel", exact: true }).click();
    await expect(card.getByText("Delete this item?")).not.toBeVisible();
    await expect(card.getByText("$5200.00")).toBeVisible();
  });
});
'''

path = "tests/e2e/items.spec.ts"
text = open(path, encoding="utf-8").read()
if "item-card inline confirm-bar census at 1280 (v121" in text:
    raise SystemExit("the v121 block already present — refusing to append twice")
open(path, "a", encoding="utf-8").write(BLOCK)
print(f"appended the v121 describe block to {path}")
