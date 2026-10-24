#!/usr/bin/env python3
"""Append the v113 pin to tests/e2e/dashboard.spec.ts (the v112 python-append
precedent for large files — the file is 4284 lines; the append is
structurally identical to the v107/v112 describe blocks)."""

PIN = '''
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
'''

path = "tests/e2e/dashboard.spec.ts"
text = open(path, encoding="utf-8").read()
if "v113 — plan F4" in text:
    print("SKIP: the v113 pin already present")
else:
    if not text.endswith("\n"):
        text += "\n"
    text += PIN
    open(path, "w", encoding="utf-8").write(text)
    print("appended: the v113 pin (guidelines label-row + rhythm census)")
