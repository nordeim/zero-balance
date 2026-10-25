#!/usr/bin/env python3
"""Append the v118 describe block to tests/e2e/networth.spec.ts (the
line-append form — the v112 dashboard.spec precedent: the file is ~3k
lines, the Edit old_str is unwieldy; the block appended at EOF)."""

BLOCK = r'''

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
'''

path = "tests/e2e/networth.spec.ts"
text = open(path, encoding="utf-8").read()
if "v118 — plan F4" in text:
    raise SystemExit("FAIL: the v118 block already exists")
if not text.endswith("\n"):
    text += "\n"
open(path, "w", encoding="utf-8").write(text + BLOCK.lstrip("\n"))
print(f"OK: appended the v118 describe block to {path}")
