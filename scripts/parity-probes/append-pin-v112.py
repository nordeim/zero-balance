#!/usr/bin/env python3
"""Append the v112 describe block to tests/e2e/dashboard.spec.ts (the
line-append form — the v111 calculator.spec precedent: the file is 4k
lines, the Edit old_str is unwieldy; the block appended at EOF)."""

BLOCK = r'''

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
'''

path = "tests/e2e/dashboard.spec.ts"
text = open(path, encoding="utf-8").read()
assert "v112 — plan F4" not in text, "the v112 block already present"
open(path, "a", encoding="utf-8").write(BLOCK)
print("appended the v112 describe block to", path)
