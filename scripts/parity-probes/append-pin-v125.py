#!/usr/bin/env python3
"""append-pin-v125.py — append the v125 pin (the quick-action card's HOVER
END-STATE census at 1280) to tests/e2e/dashboard.spec.ts as the v125
describe block, following the v124 pin's own append form. The axes are the
one-shot census's measured values (qahover-arbit-v125.sh, measured cleanly
on both sides — the re-run post-cycle reproducing the values exactly): the
hover-ladder at-rest {cardHover false / tile {transform "none", scale
"none", 40x40} / plus {opacity "0.5", w 16}} -> the REAL-hover end-states
{cardHover true / tile {transform "none", scale "1.1", 44x44} / plus
{opacity "1", w 16}} -> the restore rung back to at-rest."""
import sys

PIN = '''
test.describe("quick-action hover end-state census at 1280 (v125 — plan F4)", () => {
  test("the hovered card's tile scale reveal + the plus opacity reveal — the never-pinned hover end-states", async ({ page }) => {
    // The v125 F4 pin: the quick-action family's HOVER END-STATES — the
    // tile's group-hover:scale-110 (dashboard-view.tsx:890) + the plus's
    // group-hover:opacity-100 (:899) — held by NO spec before this pin
    // (the coverage map, read per the SPEC-ALIAS lesson: the v45 F3b pin
    // holds the CARD's hover:shadow-lg layers ONLY — the sole .hover()
    // on the QA surface in the entire suite; the v61 F3 + v107 pins the
    // AT-REST chrome; the v95 pin the transition TIMING metadata, never
    // the end-states). The both-sides census (qahover-arbit-v125.sh):
    // the rendered parity contract IDENTICAL on both sites — the tile
    // 40->44x44 + the plus 0.5->1 — the computed form the documented
    // class (the reference's Tailwind v3 transform matrix(1.1,...) vs
    // the clone's v4 `scale` property — the v95 transition-property
    // class's hover-state twin).
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByRole("button", { name: "Add Income" })).toBeVisible();
    await page.waitForTimeout(400);

    const qa = page.getByRole("button", { name: /^Add Income$/ });
    const readState = () =>
      qa.evaluate((el) => {
        // The tile: the v61 F3 finder (radius 12px, the 30..60 box) —
        // tag-agnostic (the v107 DIV-vs-SPAN lesson: the reference
        // builds the tile as a DIV, the clone as a span).
        const tile = [...el.querySelectorAll("span, div")].find((s) => {
          const cs = getComputedStyle(s);
          const r = s.getBoundingClientRect();
          return cs.borderRadius === "12px" && r.width >= 30 && r.width <= 60 && r.height >= 30 && r.height <= 60;
        });
        const svgs = [...el.querySelectorAll("svg")];
        const plus = svgs[svgs.length - 1];
        if (!tile || !plus) return null;
        const cs = getComputedStyle(tile);
        const r = tile.getBoundingClientRect();
        return {
          cardHover: el.matches(":hover"),
          tile: { transform: cs.transform, scale: cs.scale, w: Math.round(r.width), h: Math.round(r.height) },
          plus: { opacity: getComputedStyle(plus).opacity, w: Math.round(plus.getBoundingClientRect().width) },
        };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5): the v61 F3 contract (the tile 40x40 unscaled, the plus
    // 0.5), establishing the contrast the hover axes need.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({
      cardHover: false,
      tile: { transform: "none", scale: "none", w: 40, h: 40 },
      plus: { opacity: "0.5", w: 16 },
    });

    // THE HOVER END-STATES — the REAL pointer on the card (Playwright's
    // locator hover IS the real pointer move — the v43/v45 idiom): the
    // tile's scale-110 reveal (the rendered 44x44 the parity contract;
    // the clone's v4 `scale` computed form asserted as the clone's own
    // chrome) + the plus's opacity-100 reveal + the card's own :hover
    // state.
    await qa.hover();
    await page.waitForTimeout(400); // the duration-200 transition settle
    const hovered = await readState();
    expect(hovered).toEqual({
      cardHover: true,
      tile: { transform: "none", scale: "1.1", w: 44, h: 44 },
      plus: { opacity: "1", w: 16 },
    });

    // The restore rung — the pointer re-parked at (5,5): both reveals
    // disengaged, the at-rest contract re-established (the v95 timing
    // pin holds the transition metadata; THIS rung holds the restore
    // end-state).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual({
      cardHover: false,
      tile: { transform: "none", scale: "none", w: 40, h: 40 },
      plus: { opacity: "0.5", w: 16 },
    });
  });
});
'''

path = "tests/e2e/dashboard.spec.ts"
text = open(path, encoding="utf-8").read()
if "v125 — plan F4" in text:
    print("FAIL: the v125 pin already present")
    sys.exit(1)
if not text.endswith("\n"):
    text += "\n"
open(path, "w", encoding="utf-8").write(text + PIN.lstrip("\n"))
print(f"OK: appended the v125 pin ({len(PIN.lstrip(chr(10)).splitlines())} lines) to {path}")
