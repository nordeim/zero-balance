#!/usr/bin/env python3
"""Append the v143 describe block (the dashboard quick-action cards'
focus-visible ladder at 1280x800) to tests/e2e/dashboard.spec.ts — the
PIN-ONLY cycle's pin (the plan docs/remediation-plan-v143.md F4).

The form mirrors the v125 hover-ladder pin + the v136 focus-visible
ladder precedent adapted to the cycle's own dashboard-pair surface (the
Quick-Action row below the fold at 1280x800). THE CONSTRUCT: the
UA-DEFAULT RING contract — the cards carry NO focus classes
(dashboard-view.tsx:885 — group rounded-2xl border p-6 text-left
transition-all duration-200 hover:shadow-lg), so the focused end-state
is the engine's own ring (outlineStyle none->auto + outlineWidth
medium(3px)->1px + outlineOffset 0px) with the card chrome UNCHANGED
under focus (focus != hover: the shadow-lg is :hover-only [boxShadow
stays none]; the tile scale + the plus opacity are group-hover-only
[both stay at-rest]) — measured byte-identical on BOTH sides by
focusqa-arbit-v143.sh (the sole delta the outlineColor computed form —
rgba(10,10,10,0.5) vs the v4 lab() twin — the documented v43-F2-class
construct, NEVER pinned per the v95 discipline). The STRUCTURAL finder
(the button whose accessible name is exactly "Add Income" — the v125
pin's own getByRole family); the REAL Chromium focus({focusVisible:
true}) engagement (the v35 S2 idiom — the REAL FocusOptions member; the
v25 plain-focus lesson does not apply); the card NEVER clicked (it opens
the Add Item dialog — OUT OF BOUNDS under the v46 rule); the (5,5)-parked
pointer first (the v22 lesson); the blur restore. The V125-COLLISION-safe
family: the tile/plus axes asserted at their AT-REST values only (the
v125 pin's hover rungs untouched); the boxShadow "none" axis shared with
the v45 F3b at-rest contract (the same value, a different state)."""
import io

SPEC = "tests/e2e/dashboard.spec.ts"
MARKER = "// v143 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v143 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v143 — plan F4 (docs/remediation-plan-v143.md): the DASHBOARD QUICK-ACTION
// CARDS' FOCUS-VISIBLE LADDER at 1280 (the cycle's own surface — the
// Quick-Action row below the fold, the v137-era DASHBOARD pair's THIRTEENTH
// re-run). The never-pinned KEYBOARD PATH of the pinned quick-action family
// (the v45 F3b pin holds the card's hover:shadow-lg layers ONLY; the v61 F3
// + v107 pins the AT-REST chrome; the v95 pin the transition TIMING
// metadata; the v125 pin the HOVER end-state ladder — the focus-visible ring
// + the focused card's UNCHANGED chrome held by NO spec at ANY viewport
// before this pin [the suite-wide survey: dashboard.spec.ts's focus pins
// cover the header Add Item composite (v35 S2) + the Tab-order structural
// walk (v40 F1); the stat cards' focus path is SUPERSET-only — the
// reference's are inert divs, the v40 census]). THE CONSTRUCT: the
// UA-DEFAULT RING contract — the cards carry NO focus classes
// (dashboard-view.tsx:885), so the focused end-state is the engine's own
// ring (outlineStyle auto + outlineWidth 1px + outlineOffset 0px) with the
// card chrome UNCHANGED (focus != hover: boxShadow stays none — the
// shadow-lg is :hover-only; tileScale stays none + plusOpacity stays 0.5 —
// the group-hover reveals never engage on focus) — measured byte-identical
// on BOTH sides by focusqa-arbit-v143.sh (the sole delta the outlineColor
// computed form — the reference's rgba(10,10,10,0.5) vs the clone's v4
// lab() twin, the SAME rendered near-black-at-50% — the documented v43-F2
// construct class, never pinned per the v95 discipline).
// ---------------------------------------------------------------------------
test.describe("quick-action card focus-visible ladder at 1280 (v143 — plan F4)", () => {
  test("the Add Income card's focus-visible ring — the at-rest chrome, the focused UA-default ring + the UNCHANGED focus != hover family, the blur restore (the never-pinned keyboard path)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    // The settle pattern (the v42 idiom: the card title is a plain div,
    // never a role=heading) + the seeded net-balance text before any
    // interaction.
    await expect(page.getByText("Net Zero Goal")).toBeVisible();
    await expect(page.getByText("+$2065.00")).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the v125 pin's own family): the button whose
    // accessible name is exactly "Add Income" (the role query — the card
    // is a real <button> on BOTH sites, the v40 F1 walk's own stop).
    const qa = page.getByRole("button", { name: /^Add Income$/ });
    await expect(qa).toBeVisible();

    const readState = () =>
      qa.evaluate((el) => {
        // The tile: the v61 F3 finder (radius 12px, the 30..60 box) —
        // tag-agnostic (the v107 DIV-vs-SPAN lesson). The plus: the last
        // small svg (the v125 pin's own finder form).
        const tile = [...el.querySelectorAll("span, div")].find((s) => {
          const cs = getComputedStyle(s);
          const r = s.getBoundingClientRect();
          return cs.borderRadius === "12px" && r.width >= 30 && r.width <= 60 && r.height >= 30 && r.height <= 60;
        });
        const plus = [...el.querySelectorAll("svg")]
          .filter((sv) => {
            const r = sv.getBoundingClientRect();
            return r.width <= 20 && r.height <= 20;
          })
          .pop() as SVGElement | undefined;
        const cs = getComputedStyle(el);
        return {
          focused: document.activeElement === el,
          fv: el.matches(":focus-visible"),
          outlineStyle: cs.outlineStyle,
          outlineWidth: cs.outlineWidth,
          outlineOffset: cs.outlineOffset,
          boxShadow: cs.boxShadow,
          tileScale: tile ? getComputedStyle(tile).scale : null,
          plusOpacity: plus ? getComputedStyle(plus).opacity : null,
        };
      });

    // The at-rest rung — the REAL pointer parked at (5,5) FIRST (the v22
    // lesson): no focus, no ring (style none, the CSS-wide medium 3px,
    // offset 0px), the card's at-rest chrome (shadow none — the v45 F3b
    // at-rest contract; the tile unscaled + the plus 0.5 — the v125
    // at-rest rung's own values).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      boxShadow: "none",
      tileScale: "none",
      plusOpacity: "0.5",
    });

    // THE FOCUSED RUNG — the REAL Chromium focus({focusVisible: true})
    // (the v35 S2 idiom — the REAL FocusOptions member; a programmatic
    // PLAIN focus never engages :focus-visible, the v25 lesson — the
    // focusVisible form does). The card is NEVER clicked (it opens the
    // Add Item dialog — OUT OF BOUNDS under the v46 rule; focus()
    // dispatches no click). THE UA-DEFAULT RING engages (style auto +
    // width 1px + offset 0px) while the card chrome stays UNCHANGED —
    // focus != hover: the shadow-lg NOT engaged, the group-hover reveals
    // NOT engaged. The 450ms settle covers the card's transition-all
    // duration-200 (the v136 settle discipline).
    await qa.evaluate((el) =>
      (el as HTMLElement).focus({ focusVisible: true } as unknown as FocusOptions),
    );
    await page.waitForTimeout(450);
    const focused = await readState();
    expect(focused).toEqual({
      focused: true,
      fv: true,
      outlineStyle: "auto",
      outlineWidth: "1px",
      outlineOffset: "0px",
      boxShadow: "none",
      tileScale: "none",
      plusOpacity: "0.5",
    });

    // The blurred rung — the at-rest contract re-established on every
    // axis (the ring disengages; the chrome never moved).
    await qa.evaluate((el) => (el as HTMLElement).blur());
    await page.waitForTimeout(450);
    const blurred = await readState();
    expect(blurred).toEqual(atRest);
  });
});
'''

text += BLOCK
io.open(SPEC, "w", encoding="utf-8").write(text)
print(f"appended the v143 describe block ({len(BLOCK.splitlines())} lines) to {SPEC}")
