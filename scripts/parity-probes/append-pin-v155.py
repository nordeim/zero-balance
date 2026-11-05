#!/usr/bin/env python3
"""append-pin-v155.py — append the v155 describe block to dashboard.spec.ts.

THE PIN: the DASHBOARD QUICK-ACTION SIBLING CARDS' HOVER END-STATE LADDERS
at desktop 1280x800 (the Add Savings + Add Expense cards — the pair's own
below-the-fold quick-action row surface, the v149-era DASHBOARD pair's
FIFTEENTH re-run) — the never-pinned HOVER PATH of the SIBLING cards (the
hover family's sibling-completion form, the v125/v149 precedent chain: the
v125 pin holds the FIRST card's hover end-states — the tile's scale-110
reveal + the plus's opacity-100 reveal, the sole .hover() on the QA
surface in the entire suite; the v149 pin the SIBLING cards' focus-visible
ladders — the keyboard paths; the v45 F3b pin the card's hover:shadow-lg
layers; the v61 F3 + v107 pins the AT-REST chrome; the v95 pin the
transition TIMING metadata — the siblings' HOVER end-states held by NO
spec at ANY viewport before this pin).

The measured contract (qasibhover-discovery-v155.sh, BOTH sides, NO GAP):
- at-rest: the tile 40x40 unscaled at its own tint (savings
  rgba(59,126,161,0.125) / expense rgba(224,122,59,0.125) — identical both
  sides) + the plus 0.5 + the card shadow none;
- hovered (the REAL pointer on the card): the tile's group-hover:scale-110
  reveal — the rendered 44x44 the parity contract (the clone's v4 `scale`
  computed form asserted as the clone's own chrome per the v125 form; the
  reference's Tailwind v3 transform-matrix form the documented computed-form
  class, the same rendered rect) + the plus's group-hover:opacity-100
  reveal 0.5 -> 1 + the cardHover state true; the card's hovered shadow
  transparent lead layers (the v66 class) held by the v45 F3b pin,
  deliberately NOT asserted here;
- the SIBLING NON-INTERFERENCE cross-check at the hovered rung (the other
  card stays at its own at-rest contract — the v149 form);
- restored (the pointer re-parked at 5,5): the at-rest contract
  re-established on every axis.
"""
import io

SPEC = "tests/e2e/dashboard.spec.ts"

BLOCK = '''
// ---------------------------------------------------------------------------
// v155 — plan F4 (docs/remediation-plan-v155.md): the DASHBOARD QUICK-ACTION
// SIBLING CARDS' HOVER END-STATE LADDERS at 1280 (the cycle's own surface —
// the Quick-Action row below the fold, the v149-era DASHBOARD pair's
// FIFTEENTH re-run). The never-pinned HOVER PATH of the SIBLING cards (the
// hover family's sibling-completion form: the v125 pin holds the Add
// Income FIRST card's hover end-states — the tile's scale-110 reveal + the
// plus's opacity-100 reveal, the sole .hover() on the QA surface in the
// entire suite; the v149 pin the SIBLING cards' focus-visible ladders —
// the keyboard paths; the v45 F3b pin the card's hover:shadow-lg layers;
// the v61 F3 + v107 pins the AT-REST chrome; the v95 pin the transition
// TIMING metadata — the Add Savings + Add Expense cards' HOVER end-states
// held by NO spec at ANY viewport before this pin [the suite-wide survey:
// ZERO hover/scale/opacity assertions on these two cards across all 24
// spec files; the items.spec v146/v151 pins cover the SAVINGS/EXPENSES
// page-header BUTTONS — different elements on different views]).
// THE CONSTRUCT — the same-component reasoning (dashboard-view.tsx renders
// the three cards from the SAME QuickActionCard component, the ONLY
// per-card deltas the label/icon/COLOR tokens) — measured byte-identical
// on BOTH sides by qasibhover-discovery-v155.sh (the sole deltas the
// documented classes: the tile's computed form — the reference's Tailwind
// v3 transform matrix vs the clone's v4 `scale` property, the v125
// computed-form class, the clone's own chrome asserted here per that form;
// the card's hovered-shadow transparent lead layers — the v66 class, held
// by the v45 F3b pin, deliberately NOT asserted here).
// THE LADDER per card: at-rest {the tile 40x40 unscaled at its own tint +
// the plus 0.5} -> hovered (the REAL pointer on the card) {the tile's
// scale-110 reveal 44x44 + the plus's opacity-100 reveal 1 + the cardHover
// state} -> restored (the pointer re-parked at 5,5) {the at-rest contract}
// — plus the SIBLING NON-INTERFERENCE cross-check at the hovered rung
// (the other card stays at its at-rest contract — the v149 form).
// ---------------------------------------------------------------------------
test.describe("quick-action sibling cards hover end-state ladder at 1280 (v155 — plan F4)", () => {
  test("the Add Savings + Add Expense cards' hover reveals — the tile's scale-110 44x44 + the plus's opacity-100, the per-card tints, the sibling non-interference, the restores (the never-pinned hover path of the sibling cards)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    await expect(page.getByRole("button", { name: "Add Income" })).toBeVisible();
    await page.waitForTimeout(400);

    const CARDS = [
      { name: "Add Savings", tint: "rgba(59, 126, 161, 0.125)" },
      { name: "Add Expense", tint: "rgba(224, 122, 59, 0.125)" },
    ] as const;

    for (const card of CARDS) {
      const other = CARDS.find((c) => c.name !== card.name)!;
      const qa = page.getByRole("button", { name: new RegExp(`^${card.name}$`) });
      const qaOther = page.getByRole("button", { name: new RegExp(`^${other.name}$`) });
      const readState = (loc: typeof qa) =>
        loc.evaluate((el) => {
          // The tile: the v61 F3 finder (radius 12px, the 30..60 box) —
          // tag-agnostic (the v107 DIV-vs-SPAN lesson: the reference
          // builds the tile as a DIV, the clone as a span) — with the
          // state-read band 25..65 covering BOTH rungs (the at-rest 40
          // and the hovered 44).
          const tile = [...el.querySelectorAll("span, div")].find((s) => {
            const cs = getComputedStyle(s);
            const r = s.getBoundingClientRect();
            return cs.borderRadius === "12px" && r.width >= 25 && r.width <= 65 && r.height >= 25 && r.height <= 65;
          });
          const svgs = [...el.querySelectorAll("svg")];
          const plus = svgs[svgs.length - 1];
          if (!tile || !plus) return null;
          const cs = getComputedStyle(tile);
          const r = tile.getBoundingClientRect();
          return {
            cardHover: el.matches(":hover"),
            tile: { transform: cs.transform, scale: cs.scale, w: Math.round(r.width), h: Math.round(r.height), bg: cs.backgroundColor },
            plus: { opacity: getComputedStyle(plus).opacity, w: Math.round(plus.getBoundingClientRect().width) },
          };
        });

      // The ladder's first rung — AT-REST with the REAL pointer parked at
      // (5,5): the v61 F3/v107 contract (the tile 40x40 unscaled at its own
      // tint — the per-card color token, byte-identical both sides per the
      // discovery — the plus 0.5), establishing the contrast the hover
      // axes need.
      await page.mouse.move(5, 5);
      await page.waitForTimeout(300);
      const atRest = await readState(qa);
      expect(atRest).toEqual({
        cardHover: false,
        tile: { transform: "none", scale: "none", w: 40, h: 40, bg: card.tint },
        plus: { opacity: "0.5", w: 16 },
      });

      // THE HOVER END-STATES — the REAL pointer on the card (Playwright's
      // locator hover IS the real pointer move — the v43/v45/v125 idiom):
      // the tile's scale-110 reveal (the rendered 44x44 the parity
      // contract; the clone's v4 `scale` computed form asserted as the
      // clone's own chrome — the v125 form) + the plus's opacity-100
      // reveal + the card's own :hover state.
      await qa.hover();
      await page.waitForTimeout(400); // the duration-200 transition settle
      const hovered = await readState(qa);
      expect(hovered).toEqual({
        cardHover: true,
        tile: { transform: "none", scale: "1.1", w: 44, h: 44, bg: card.tint },
        plus: { opacity: "1", w: 16 },
      });

      // The SIBLING NON-INTERFERENCE cross-check (the v149 form): the
      // other card stays at its own at-rest contract while this one
      // hovers — its tile unscaled at its OWN tint, its plus at 0.5.
      const sibling = await readState(qaOther);
      expect(sibling).toEqual({
        cardHover: false,
        tile: { transform: "none", scale: "none", w: 40, h: 40, bg: other.tint },
        plus: { opacity: "0.5", w: 16 },
      });

      // The restore rung — the pointer re-parked at (5,5): both reveals
      // disengaged, the at-rest contract re-established (the v95 timing
      // pin holds the transition metadata; THIS rung holds the restore
      // end-state).
      await page.mouse.move(5, 5);
      await page.waitForTimeout(400);
      const restored = await readState(qa);
      expect(restored).toEqual({
        cardHover: false,
        tile: { transform: "none", scale: "none", w: 40, h: 40, bg: card.tint },
        plus: { opacity: "0.5", w: 16 },
      });
    }
  });
});
'''

text = io.open(SPEC, encoding="utf-8").read()
if "v155 — plan F4" in text:
    raise SystemExit("the v155 pin block is already present — refusing to double-append")

io.open(SPEC, "w", encoding="utf-8").write(text + BLOCK)
print(f"appended the v155 pin block to {SPEC} (+{BLOCK.count(chr(10))} lines)")
