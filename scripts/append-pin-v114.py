#!/usr/bin/env python3
"""Append the v114 pin (the dashboard header-ROW interior census at 390)
to tests/e2e/dashboard.spec.ts — the v113 append-pin pattern (the file is
APPENDED-ONLY; the existing content untouched)."""
PIN = '''

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
            bg: (bs.backgroundImage || "").replace(/\\s+/g, " ").slice(0, 90),
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
'''

path = "tests/e2e/dashboard.spec.ts"
text = open(path, encoding="utf-8").read()
assert "v114 — plan F4" not in text, "the v114 pin already present"
open(path, "a", encoding="utf-8").write(PIN)
print(f"appended the v114 pin to {path} ({len(PIN)} chars)")
