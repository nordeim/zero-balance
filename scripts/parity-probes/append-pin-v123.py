#!/usr/bin/env python3
"""Append the v123 describe block to tests/e2e/calculator.spec.ts (the
line-append form — the v112 dashboard.spec precedent + the v120/v121
items.spec + the v122 items.spec precedents: the file is ~2k lines, the
block appended at EOF)."""

BLOCK = r'''

// ---------------------------------------------------------------------------
// v123 — plan F4 (docs/remediation-plan-v123.md): the CALCULATOR
// line-item DELETE-CONFIRM BAR census at 1280 — the never-pinned FOURTH
// member of the confirm-bar family (the v121 pin holds the ITEM-CARD's
// bar; the net-worth twins are held BY CONSTRUCTION via the identical
// class strings net-worth-view.tsx:123/234; the CALCULATOR's bar — the
// mt-3 variant inside the row card, calculator-dialog.tsx:279 — held by
// NO spec: the behavioral tests assert the text + the click flow only,
// the v45/v66 row censuses read the row at REST, and the bar renders
// only while confirmingId === li.id). The CLONE-ONLY form (the v121 F3
// adapted precedent): the reference's calculator row delete destroys
// IMMEDIATELY (its R6 bug — superset fix #6's own citation), so no
// confirm bar exists on the reference and a reference-side measurement
// would require a DESTRUCTIVE click (the v46 read-only rule) — the pin
// locks the CLONE's own superset chrome. The family chrome = the v121
// pinned contract BY CONSTRUCTION (the identical class strings); the
// calculator-specific axis: mt-3 (12px — the family's other members
// carry mt-4 16px, the calculator's tighter rhythm inside the row).
// The one-shot census: confirmbar-arbit-v123.sh (the confirm ladder —
// the twin state seeded through the real UI, the at-rest 102, the bar
// census + the +60 bar-open delta, the Cancel path, the fixture
// restore + the seedcheck exact after).
// ---------------------------------------------------------------------------
test.describe("calculator line-item DELETE-CONFIRM BAR census at 1280 (v123 — plan F4)", () => {
  test("the confirm bar — the box, the label, the Cancel pill + the shadow-sm VISIBLE layer, the Delete twin, the +60 bar-open delta (the never-pinned FOURTH member of the confirm-bar family)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    // the settle pattern: the seeded count subtitle before interacting
    // (the items views' formatMoney — no grouping: "$2235.00").
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();

    // Open the Rent calculator (the hover-revealed Calculate action; the
    // native locator click IS the full pointer sequence — the v46 lesson).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();

    // The twin state: "Contents Insurance" $25 through the real Add Item
    // flow (the v66 pin's own form — the reference's OWN Rent calculator
    // carries this same single line item, the v45 measurement note).
    await dialog.getByRole("button", { name: "Add Item" }).click();
    const lineDialog = page.getByRole("dialog", { name: "Add Line Item" });
    await lineDialog.getByLabel("Item Name *").fill("Contents Insurance");
    await lineDialog.getByLabel("Amount *").fill("25");
    await lineDialog.getByRole("button", { name: "Save Item" }).click();
    await expect(lineDialog).toBeHidden();
    await expect(dialog.getByText("Contents Insurance")).toBeVisible();
    await page.waitForTimeout(300);

    // The at-rest row height FIRST (the delta's baseline — the v66
    // contract: 102 in this twin state; re-read live, never assumed).
    const rowHeight = () =>
      page.evaluate(() => {
        const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
          (d.textContent || "").includes("Rent Calculator"),
        );
        if (!panel) return null;
        const h4 = [...panel.querySelectorAll("h4")].find(
          (h) => (h.textContent || "").trim() === "Contents Insurance",
        );
        if (!h4) return null;
        let row: HTMLElement = h4;
        while (row && row !== panel) {
          const cs = getComputedStyle(row);
          if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === "rgb(255, 255, 255)") break;
          row = row.parentElement!;
        }
        return row && row !== panel ? Math.round(row.getBoundingClientRect().height) : null;
      });
    expect(await rowHeight()).toBe(102);

    // The trash click opens the confirm bar (the aria-label finder — the
    // structural form; the native click auto-hovers the row so the
    // hover-revealed action pair is engaged at click time).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await expect(dialog.getByText("Delete this line item?")).toBeVisible();

    // THE BAR CENSUS — the structural finder (the v121 form: the
    // rgb(254,242,242) bg + the exact Cancel/Delete button pair; the
    // class strings never trusted for the walk).
    const census = await page.evaluate(() => {
      const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
        (d.textContent || "").includes("Rent Calculator"),
      );
      if (!panel) return null;
      const bar = [...panel.querySelectorAll("div")].find((d) => {
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
      const lcs = label ? getComputedStyle(label) : null;
      const cancel = [...bar.querySelectorAll("button")].find(
        (b) => (b.textContent || "").trim() === "Cancel",
      )!;
      const del = [...bar.querySelectorAll("button")].find(
        (b) => (b.textContent || "").trim() === "Delete",
      )!;
      const ccs = getComputedStyle(cancel);
      const cbr = cancel.getBoundingClientRect();
      const dcs = getComputedStyle(del);
      let row: HTMLElement = bar;
      while (row && row !== panel) {
        const cs = getComputedStyle(row);
        if (parseFloat(cs.borderTopWidth) > 0 && cs.backgroundColor === "rgb(255, 255, 255)") break;
        row = row.parentElement!;
      }
      return {
        bar: {
          mt: bcs.marginTop,
          display: bcs.display,
          align: bcs.alignItems,
          justify: bcs.justifyContent,
          radius: bcs.borderRadius,
          pad: bcs.padding,
          w: Math.round(br.width),
          h: Math.round(br.height),
        },
        label: lcs
          ? { fs: lcs.fontSize, fw: lcs.fontWeight, txt: (label!.textContent || "").trim() }
          : null,
        // Colors deliberately NOT asserted (the named-palette lab()
        // discipline — text-red-700 / bg-white / bg-red-600 / text-slate-
        // 700 are named utilities whose computed forms drift between
        // engines; the v121 pin's own convention).
        cancelPill: {
          pad: ccs.padding,
          radius: ccs.borderRadius,
          fs: ccs.fontSize,
          fw: ccs.fontWeight,
          h: Math.round(cbr.height),
        },
        cancelShadow: ccs.boxShadow,
        deletePill: {
          pad: dcs.padding,
          radius: dcs.borderRadius,
          fs: dcs.fontSize,
          fw: dcs.fontWeight,
          h: Math.round(del.getBoundingClientRect().height),
        },
        rowOpenH: row && row !== panel ? Math.round(row.getBoundingClientRect().height) : null,
      };
    });
    expect(census).not.toBeNull();
    // The box — the v121 family contract + the calculator-specific mt-3
    // (12px — the family's mt-4 is 16px; THE distinguishing axis).
    expect(census!.bar).toEqual({
      mt: "12px",
      display: "flex",
      align: "center",
      justify: "space-between",
      radius: "8px",
      pad: "12px",
      w: 686,
      h: 48,
    });
    // The label — 14px/400, the exact text (the named-palette color
    // skipped by discipline).
    expect(census!.label).toEqual({ fs: "14px", fw: "400", txt: "Delete this line item?" });
    // The Cancel pill — the v121 twin chrome + the shadow-sm VISIBLE
    // layer by toContain (the accepted-leads convention: v4's
    // transparent composition leads paint nothing; a future Tailwind
    // upgrade that changes the ambient numerics must fail this pin).
    expect(census!.cancelPill).toEqual({
      pad: "4px 12px",
      radius: "6px",
      fs: "12px",
      fw: "500",
      h: 24,
    });
    expect(census!.cancelShadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");
    // The Delete pill — the twin chrome (the bg-red-600 color skipped).
    expect(census!.deletePill).toEqual({
      pad: "4px 12px",
      radius: "6px",
      fs: "12px",
      fw: "500",
      h: 24,
    });
    // THE BAR-OPEN DELTA — the row card grows +60 (the at-rest 102 →
    // 162: the bar's 48 + the mt-3's 12).
    expect(census!.rowOpenH).toBe(162);

    // The Cancel path: the bar closes, the row returns to its at-rest
    // height (the non-destructive rung of the ladder).
    await dialog.getByRole("button", { name: "Cancel" }).click();
    await expect(dialog.getByText("Delete this line item?")).toBeHidden();
    expect(await rowHeight()).toBe(102);

    // The fixture-restore: the destructive Delete through the re-opened
    // bar (the recalc to $0.00), then restoreRent — the e2e convention:
    // every calculator add/delete ends with restoreRent (a missing
    // restore poisons every later spec's dashboard arithmetic).
    await dialog.getByRole("button", { name: "Delete Contents Insurance" }).click();
    await expect(dialog.getByText("Delete this line item?")).toBeVisible();
    await dialog.getByRole("button", { name: "Delete", exact: true }).click();
    await expect(dialog.getByText("Based on 0 items")).toBeVisible();
    await dialog.getByRole("button", { name: "Close" }).click();
    await expect(dialog).toBeHidden();
    await restoreRent(page);
  });
});
'''

path = "tests/e2e/calculator.spec.ts"
text = open(path, encoding="utf-8").read()
if "v123 — plan F4" in text:
    raise SystemExit("the v123 block already present — refusing to double-append")
open(path, "w", encoding="utf-8").write(text + BLOCK)
print(f"appended the v123 describe block to {path} (+{BLOCK.count(chr(10))} lines)")
