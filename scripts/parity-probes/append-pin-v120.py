#!/usr/bin/env python3
"""Append the v120 describe block to tests/e2e/networth.spec.ts (the
line-append form — the v112 dashboard.spec precedent: the file is ~3.1k
lines, the Edit old_str is unwieldy; the block appended at EOF)."""

BLOCK = r'''

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
        txt: "Updated Oct 25, 2026",
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
'''

path = "tests/e2e/networth.spec.ts"
text = open(path, encoding="utf-8").read()
if "liability-card census at 390 (v120" in text:
    raise SystemExit("the v120 block already present — refusing to append twice")
open(path, "a", encoding="utf-8").write(BLOCK)
print(f"appended the v120 describe block to {path}")
