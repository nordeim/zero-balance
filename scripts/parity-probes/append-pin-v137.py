#!/usr/bin/env python3
"""Append the v137 describe block (the INTERACTIVE STAT CARD's OWN-HOVER
SHADOW LADDER at 1280x800) to tests/e2e/dashboard.spec.ts — the PIN-ONLY
cycle's pin (the plan docs/remediation-plan-v137.md F4).

The form mirrors the v131 pin's own card finder (the seeded net-balance
settle text, then the div[role=button] filtered by the Total Income text —
the clone's interactive SUPERSET card; the reference's is an inert div,
but the pin runs against the clone's own build, and the both-sides parity
was proven by the census stathovershadow-arbit-v137.sh before the pin was
written) + the v125/v131 hover-ladder idiom: the REAL pointer parked at
(5,5) FIRST (the v22 lesson), the at-rest rung read, the REAL hover at the
card's own center (the card NEVER clicked — the v46 rule: the clone's card
click navigates to the type view), the hovered rung read, the pointer
re-parked, the restored rung read.

THE CONTRACT BEING PINNED (measured byte-identical both sides): the stat
card carries BOTH the hover:shadow-lg utility AND an INLINE boxShadow
(rgba(0, 0, 0, 0.06) 0px 4px 20px) — the inline style beats the utility in
the cascade (the v43 category-row precedent), so the hovered end-state is
the INLINE PERSISTENCE: the shadow unchanged across the ladder's rungs,
the hover:shadow-lg inert — the exact opposite of the v45 F3b quick-action
twin (no inline shadow there, the utility LIVE). The V94-COLLISION-safe
axis set: the cardHover + boxShadow end-states alone; the transition
metadata (the clone's transition-all 0.2s construct vs the reference's
0s) deliberately NOT pinned — the v89 family's own form."""
import io

SPEC = "tests/e2e/dashboard.spec.ts"
MARKER = "// v137 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v137 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v137 — plan F4 (docs/remediation-plan-v137.md): the INTERACTIVE STAT
// CARD's OWN-HOVER SHADOW LADDER at 1280 (the cycle's own surface — the
// /dashboard view, the v131-era DASHBOARD pair's TWELFTH re-run). The
// never-pinned SHADOW path of the pinned hover family: the v131 pin the
// own-hover REVEAL ladder (the radial + the chevron opacity — never the
// card's own shadow); the v45 F3b pin the QUICK-ACTION TWIN's LIVE
// hover:shadow-lg layers (that card carries NO inline boxShadow, so the
// utility engages there); the v51 F2 pin the AT-REST card chrome at 390
// incl. the inline rest shadow. THE CONSTRUCT: this card carries BOTH the
// hover:shadow-lg utility AND the INLINE boxShadow (rgba(0, 0, 0, 0.06)
// 0px 4px 20px) — the inline style beats the utility in the cascade (the
// v43 category-row precedent), so the hovered end-state is the INLINE
// PERSISTENCE (the shadow unchanged across the ladder's rungs, the
// hover:shadow-lg inert) — measured byte-identical on BOTH sides by
// stathovershadow-arbit-v137.sh (both sides' card center (440,400); the
// construct deltas — the class token + the transition metadata — the
// documented classes, never pinned).
test.describe("stat-card own-hover shadow ladder at 1280 (v137 — plan F4)", () => {
  test("the Total Income card's own-hover shadow ladder — the at-rest inline shadow, the hovered INLINE PERSISTENCE (the hover:shadow-lg inert), the restore (the never-pinned shadow path)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    // The settle pattern (the v40/v51/v131 idiom: the seeded net-balance
    // text before any interaction).
    await expect(page.getByText("+$2065.00")).toBeVisible();
    await page.waitForTimeout(400);

    // The v131 finder — the clone's interactive stat card (the SUPERSET
    // div[role=button]; the reference's is an inert div).
    const card = page.locator('div[role="button"]').filter({ hasText: "Total Income" });
    await expect(card).toBeVisible();

    // The shadow axis: the FULL computed string, never truncated (the v11
    // probe-hygiene rule) — plus the card's own :hover state.
    const readState = () =>
      card.evaluate((el) => {
        const cs = getComputedStyle(el);
        return {
          cardHover: el.matches(":hover"),
          boxShadow: cs.boxShadow,
        };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the INLINE rest shadow, the contrast the
    // hover axis needs.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({
      cardHover: false,
      boxShadow: "rgba(0, 0, 0, 0.06) 0px 4px 20px 0px",
    });

    // THE HOVERED RUNG — the REAL pointer on the card (Playwright's
    // locator hover IS the real pointer move — the v43/v45/v125/v131
    // idiom): the INLINE PERSISTENCE contract — the shadow UNCHANGED
    // under hover, the hover:shadow-lg utility inert under the inline
    // style (the v43 inline-beats-utility class). The card is NEVER
    // clicked (the v46 rule — the click navigates to /income).
    await card.hover();
    await page.waitForTimeout(400); // the transition settle
    const hovered = await readState();
    expect(hovered).toEqual({
      cardHover: true,
      boxShadow: "rgba(0, 0, 0, 0.06) 0px 4px 20px 0px",
    });

    // The restore rung — the pointer re-parked at (5,5): the at-rest
    // contract re-established.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual({
      cardHover: false,
      boxShadow: "rgba(0, 0, 0, 0.06) 0px 4px 20px 0px",
    });
  });
});
'''

text += BLOCK
io.open(SPEC, "w", encoding="utf-8").write(text)
print(f"appended the v137 describe block to {SPEC} (+{BLOCK.count(chr(10))} lines)")
