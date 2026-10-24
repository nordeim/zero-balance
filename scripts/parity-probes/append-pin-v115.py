#!/usr/bin/env python3
"""Append the v115 pin (the items view's md-band state census at 800x600)
to tests/e2e/items.spec.ts. Idempotent: refuses to append if the v115
describe marker is already present."""
import sys

PATH = "tests/e2e/items.spec.ts"
MARKER = 'items md-band state census at 800 (v115 — plan F4)'

text = open(PATH, encoding="utf-8").read()
if MARKER in text:
    print("FAIL: the v115 pin is already present — refusing to append a duplicate")
    sys.exit(1)

PIN = '''
// v115 — plan F4 (docs/remediation-plan-v115.md): the v109-era items pair's
// NINTH re-run (v57 → v64 → v70 → v79 → v85 → v91 → v97 → v103 → v109 →
// v115) found NO NEW GAP (the arbit-v115 two-half census reproducing the
// v109 values exactly — compare-v115-census.py: 187 axes, 163 identical +
// 24 documented-class deltas, zero new; every VLM flag DOM-arbitrated to a
// documented class: the v57 payment-chip DATA-CONDITIONAL [the reference's
// OWN income card renders the "Bank Account" chip — footer childCount 2 —
// its expense items simply ship no payment method], the v57 badge-wrap/
// classification-VALUE classes, the Base44 platform-chrome FAB re-arbitrated
// live [fabCount 0 on both sides at 1280], the user-identity avatar, the
// seed-data classes), so the iteration deepens the coverage instead: the
// ITEMS VIEW's MD-BAND STATE (768 <= w < 1024) — the viewport band NO spec
// pins on the items views. The coverage map: the items views pinned ONLY at
// 390 (the v52 mobile pin) and 1280 (the v45 grid / the v64 filter / the
// v91 interiors / the v92 savings+icon / the v109 header row); the v42
// five-route mid-viewport census sits at 640 — BELOW md, the 1-col state;
// NOTHING in the 768-1023 band on ANY items view. The family: the ITEM
// GRID's md state (the 2-col template — md:grid-cols-2, overridden at lg
// by grid-cols-3), the PAGE HEADER ROW's md state (the flex-row reflow —
// md:flex-row, overriding the 390 flex-col), the FILTER CARD's inner grid
// md state (the 4-track template — md:grid-cols-4), the CARD box at the
// 2-col width, + the docSW 800 guard. Measured BYTE-IDENTICAL on BOTH sides
// by the one-shot census mdband-arbit-v115.sh; the pin's expected values
// are that census's own measured values. The childCount (the seed count)
// and the card h (the v70b wrap consequence) stay UNPINNED — data axes
// (the v107 position-arithmetic discipline).
test.describe("items md-band state census at 800 (v115 — plan F4)", () => {
  test("the 2-col item grid + the flex-row header row + the 4-track filter grid (the never-pinned md band)", async ({
    page,
  }) => {
    await page.setViewportSize({ width: 800, height: 600 });
    await page.goto("/income");
    // the settle pattern: wait for a seeded card heading before measuring
    await expect(page.getByRole("heading", { name: "Salary" }).first()).toBeVisible();

    const census = await page.evaluate(() => {
      const main = document.querySelector("main") || document.body;
      // the ITEM GRID: the grid inside main whose children are CARD-like
      // (radius 12px + pad 20px) — robust across sites (the v115 census
      // finder; the reference's class strings are NOT trusted).
      const grids = [...main.querySelectorAll("div")].filter((d) => {
        if (getComputedStyle(d).display !== "grid") return false;
        const kids = [...d.children];
        return (
          kids.length >= 1 &&
          kids.every((k) => {
            const cs = getComputedStyle(k);
            return cs.borderRadius === "12px" && cs.padding === "20px";
          })
        );
      });
      if (!grids.length) return null;
      const grid = grids[0];
      const gcs = getComputedStyle(grid);
      const card0 = grid.children[0] as HTMLElement;
      const ccs = getComputedStyle(card0);
      // the PAGE HEADER ROW (the v109 walk): the Add button -> UP to the
      // container holding the visible h1.
      const addBtn = [...main.querySelectorAll("button")].find(
        (b) =>
          (b.textContent || "").trim().startsWith("Add") &&
          b.getBoundingClientRect().top < 200,
      );
      let row: HTMLElement | null = null;
      if (addBtn) {
        let cur: HTMLElement | null = addBtn.parentElement;
        for (let i = 0; i < 6 && cur; i++) {
          if (cur.querySelector("h1") && cur !== addBtn) {
            row = cur;
            break;
          }
          cur = cur.parentElement;
        }
      }
      const rcs = row ? getComputedStyle(row) : null;
      // the FILTER CARD's inner grid (the search input -> the
      // rounded-2xl card -> the grid child).
      const search = [...main.querySelectorAll("input")].find((i) =>
        (i.getAttribute("placeholder") || "").startsWith("Search"),
      );
      let filterInner: HTMLElement | null = null;
      let filterCard: HTMLElement | null = null;
      if (search) {
        let card: HTMLElement | null = search.parentElement;
        for (let i = 0; i < 4 && card; i++) {
          if (
            getComputedStyle(card).borderRadius === "16px" &&
            getComputedStyle(card).padding === "24px"
          )
            break;
          card = card.parentElement;
        }
        filterCard = card;
        if (card) {
          filterInner =
            ([...card.children].find(
              (c) => getComputedStyle(c).display === "grid",
            ) as HTMLElement | null) ?? null;
        }
      }
      const ics = filterInner ? getComputedStyle(filterInner) : null;
      return {
        grid: {
          display: gcs.display,
          cols: gcs.gridTemplateColumns,
          gap: gcs.gap,
        },
        card0: {
          w: Math.round(card0.getBoundingClientRect().width),
          pad: ccs.padding,
          radius: ccs.borderRadius,
          border: ccs.borderTopColor,
          bg: ccs.backgroundColor,
        },
        headerRow: row
          ? {
              display: rcs!.display,
              flexDirection: rcs!.flexDirection,
              justify: rcs!.justifyContent,
              align: rcs!.alignItems,
              gap: rcs!.columnGap,
              mb: rcs!.marginBottom,
              h: Math.round(row.getBoundingClientRect().height),
              childCount: row.children.length,
            }
          : null,
        filterInner: ics
          ? {
              cols: ics.gridTemplateColumns,
              gap: ics.gap,
              childCount: filterInner!.children.length,
            }
          : null,
        filterCard: filterCard
          ? {
              w: Math.round(filterCard.getBoundingClientRect().width),
              mb: getComputedStyle(filterCard).marginBottom,
            }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The ITEM GRID's md state — the never-pinned 2-col template: at 800
    // the tracks read 232px 232px ((800 - 256 rail - 64 p-8 - 16 gap)/2).
    // A broken md:grid-cols-2, a changed gap, or a rail/padding drift
    // flips these axes.
    expect(census!.grid).toEqual({
      display: "grid",
      cols: "232px 232px",
      gap: "16px",
    });

    // The CARD box at the 2-col width — the template's rendered
    // consequence (the card's own co-moving axis, the v45 precedent).
    expect(census!.card0).toEqual({
      w: 232,
      pad: "20px",
      radius: "12px",
      border: "rgb(229, 231, 227)",
      bg: "rgb(255, 255, 255)",
    });

    // The PAGE HEADER ROW's md state — the never-pinned flex-row reflow
    // (the v109 row family's band state: flex/row/space-between/center/
    // gap 16/mb 32/h 60 — the same chrome as 1280, held here in the band
    // between the 390 column state and the 1280 pin).
    expect(census!.headerRow).toEqual({
      display: "flex",
      flexDirection: "row",
      justify: "space-between",
      align: "center",
      gap: "16px",
      mb: "32px",
      h: 60,
      childCount: 2,
    });

    // The FILTER CARD's inner grid md state — the never-pinned 4-track
    // template at 800: 95.5px x 4 ((480 - 48 pad - 3*16 gap)/4).
    expect(census!.filterInner).toEqual({
      cols: "95.5px 95.5px 95.5px 95.5px",
      gap: "16px",
      childCount: 3,
    });

    // The filter card's own box in the band + the no-overflow guard.
    expect(census!.filterCard).toEqual({ w: 480, mb: "24px" });
    expect(census!.docSW).toBe(800);
  });
});
'''

open(PATH, "a", encoding="utf-8").write(PIN)
print("OK: the v115 pin appended to tests/e2e/items.spec.ts")
