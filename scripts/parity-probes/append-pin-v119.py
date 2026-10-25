#!/usr/bin/env python3
"""Append the v119 describe block to tests/e2e/dashboard.spec.ts (the
line-append form — the v112 dashboard.spec precedent: the file is ~4.5k
lines, the Edit old_str is unwieldy; the block appended at EOF)."""

BLOCK = r'''

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
'''

path = "tests/e2e/dashboard.spec.ts"
text = open(path, encoding="utf-8").read()
if "v119 — plan F4" in text:
    raise SystemExit("FAIL: the v119 block already exists")
if not text.endswith("\n"):
    text += "\n"
open(path, "w", encoding="utf-8").write(text + BLOCK.lstrip("\n"))
print(f"OK: appended the v119 describe block to {path}")
