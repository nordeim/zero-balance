#!/usr/bin/env python3
"""append-pin-v146.py — append the v146 describe block to items.spec.ts.

THE PIN: the SAVINGS VIEW PAGE-HEADER ADD SAVINGS button's FOCUS-VISIBLE
LADDER at desktop 1280x800 on /savings (the v140-era SAVINGS pair's own
surface, the pair's own viewport) — the never-pinned KEYBOARD PATH of the
pinned Add-button family (the v65 pin the AT-REST chrome on the header
row at 1280 [150×36, the blue→blueLight gradient]; the tokens v11 G4 pin
the HOVER no-fade; the v35 S2 pin the DIFFERENT-ELEMENT dashboard header
Add Item composite; the v144 pin the networth Add Asset ladder at 390;
the v145 pin the income Add Income ladder at 1280 — the fourth rung of
the Add-button focus-visible ladder family).

The measured contract (addfocus-arbit-v146.sh, BOTH sides, NO GAP):
- at-rest: outline none / 3px / 0px, opacity 1, the blue→blueLight
  gradient rgb(44,95,124)→rgb(59,126,161), the VISIBLE ambient pair (the
  v66-COLLISION-safe toContain form — the lead-layer count never pinned).
- focused (focusVisible:true): outline solid / rgba(0,0,0,0) / 2px /
  2px (the v3 outline-none form) + the FOUR-layer composite (the white
  zero-spread lead + the 1px #0a0a0a ring + the two ambient layers,
  each asserted via toContain) + opacity + gradient UNCHANGED (the
  focus != hover family).
- blurred: the at-rest contract re-established.

The V95-COLLISION-safe axis set (the at-rest outlineColor computed form
deliberately NOT asserted); the ROLE finder (the button whose accessible
name is exactly "Add Savings" — the page-header button; the empty-state
twin renders only when items.length === 0, NOT the case under the seed);
the REAL Chromium focus({focusVisible: true}) engagement (the v35 S2
idiom — the REAL FocusOptions member; the v25 plain-focus lesson does
not apply); the button NEVER clicked (it opens the Add Item dialog —
OUT OF BOUNDS under the v46 rule); the (5,5)-parked pointer first (the
v22 lesson); the blur restore; the 450ms settle (the v136 discipline).
"""
import io

SPEC = "tests/e2e/items.spec.ts"
MARKER = "// v146 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v146 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v146 — plan F4 (docs/remediation-plan-v146.md): the SAVINGS VIEW
// PAGE-HEADER ADD SAVINGS button's FOCUS-VISIBLE LADDER at desktop 1280
// (the cycle's own surface — the /savings view, the v140-era SAVINGS
// pair's FOURTEENTH re-run). The never-pinned KEYBOARD PATH of the
// pinned Add-button family (the v65 pin holds the AT-REST chrome on the
// header row at 1280 [150×36, 6px radius, 8px/16px pad, 14px-500, white,
// the blue→blueLight gradient, the zb-btn-add family, the 16×16 plus
// icon — items.spec.ts:940]; the tokens v11 G4 pin the HOVER no-fade;
// the v11 G2c composite pinned on the DIFFERENT-ELEMENT dashboard header
// Add Item button at 1280 [the v35 S2 single-rung form], the networth
// Add Asset button at 390 [the v144 ladder], and the income header Add
// Income button at 1280 [the v145 ladder] — this button's focused state
// held by NO spec at ANY viewport before this pin [the suite-wide
// survey: rg 'Add Savings' across tests/e2e/*.spec.ts — 10 matches,
// ZERO focus/ladder matches]; the button is a real BUTTON on BOTH sites
// [the v65 cycle measured the reference's own savings header Add button
// live]). The fourth rung of the Add-button focus-visible ladder family
// (the FAMILY-EXTENSION form — the v92 pattern): dashboard v35 @1280 →
// networth v144 @390 → income v145 @1280 → savings v146 @1280.
// THE CONSTRUCT: the globals.css v11 G2c COMPOSITE — the .zb-btn-add
// family (items-view.tsx:154 — the page-header button,
// className="zb-btn-add shrink-0") — outline 2px TRANSPARENT + offset 2px
// (v3's outline-none form) + the FOUR-layer box-shadow (the white
// zero-spread lead + the shadcn 1px #0a0a0a ring + the gradient family's
// two ambient layers), the gradient + opacity UNCHANGED under focus (the
// v11 G4 no-hover-fade family: focus != hover) — measured BYTE-IDENTICAL
// on BOTH sides by addfocus-arbit-v146.sh (the sole deltas: the at-rest
// outlineColor computed form — the v4 lab() twin — and the at-rest
// invisible lead-layer construct — the v66 class — both never pinned).
// ---------------------------------------------------------------------------
test.describe("savings page-header Add Savings button focus-visible ladder at 1280 (v146 — plan F4)", () => {
  test("the Add Savings button's focus-visible composite — the at-rest chrome, the focused v11 G2c four-layer composite + the UNCHANGED focus != hover family, the blur restore (the never-pinned keyboard path)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    // The settle pattern (the v65/v139 idiom: the seeded count line
    // visible before any interaction).
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();
    await page.waitForTimeout(400);

    // ROLE finder (the v145 pin's own family): the button whose accessible
    // name is exactly "Add Savings" (the page-header button — the
    // empty-state twin renders only when items.length === 0, NOT the case
    // under the seed).
    const add = page.getByRole("button", { name: /^Add Savings$/ });
    await expect(add).toBeVisible();

    const readState = () =>
      add.evaluate((el) => {
        const cs = getComputedStyle(el);
        return {
          focused: document.activeElement === el,
          fv: el.matches(":focus-visible"),
          outlineStyle: cs.outlineStyle,
          outlineColor: cs.outlineColor,
          outlineWidth: cs.outlineWidth,
          outlineOffset: cs.outlineOffset,
          boxShadow: cs.boxShadow,
          opacity: cs.opacity,
          background: cs.backgroundImage,
        };
      });

    // The at-rest rung — the REAL pointer parked at (5,5) FIRST (the v22
    // lesson): no focus, no ring (style none, the CSS-wide medium 3px,
    // offset 0px), the button's at-rest chrome — the VISIBLE ambient
    // shadow layers (the v66-COLLISION-safe toContain form: the invisible
    // lead-layer construct — the v3 four-slot form vs the v11 G2a
    // two-layer form — is the documented class, NEVER pinned) + the
    // blue→blueLight gradient + opacity 1 (the v11 G4 no-fade contract).
    // The at-rest outlineColor (the v4 lab() computed form) deliberately
    // NOT asserted (the v95 discipline).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      opacity: "1",
    });
    expect(atRest.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(atRest.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(atRest.background).toBe(
      "linear-gradient(135deg, rgb(44, 95, 124), rgb(59, 126, 161))",
    );

    // THE FOCUSED RUNG — the REAL Chromium focus({focusVisible: true})
    // (the v35 S2 idiom — the REAL FocusOptions member; a programmatic
    // PLAIN focus never engages :focus-visible, the v25 lesson — the
    // focusVisible form does). The button is NEVER clicked (it opens the
    // Add Item dialog — OUT OF BOUNDS under the v46 rule; focus()
    // dispatches no click). THE v11 G2c COMPOSITE engages (outline 2px
    // TRANSPARENT + offset 2px — v3's outline-none form — + the FOUR-layer
    // shadow: the white zero-spread lead + the 1px #0a0a0a ring + the two
    // ambient layers) while the button chrome stays UNCHANGED — focus !=
    // hover: opacity stays 1 (the v11 G4 no-fade family), the gradient
    // never moves. The 450ms settle (the v136 discipline).
    await add.evaluate((el) =>
      (el as HTMLElement).focus({ focusVisible: true } as unknown as FocusOptions),
    );
    await page.waitForTimeout(450);
    const focused = await readState();
    expect(focused).toMatchObject({
      focused: true,
      fv: true,
      outlineStyle: "solid",
      outlineColor: "rgba(0, 0, 0, 0)",
      outlineWidth: "2px",
      outlineOffset: "2px",
      opacity: "1",
    });
    expect(focused.boxShadow).toContain("rgb(255, 255, 255) 0px 0px 0px 0px");
    expect(focused.boxShadow).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");
    expect(focused.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(focused.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(focused.background).toBe(atRest.background);
    expect(focused.opacity).toBe(atRest.opacity);

    // The blurred rung — the at-rest contract re-established on every
    // axis (the composite disengages; the chrome never moved).
    await add.evaluate((el) => (el as HTMLElement).blur());
    await page.waitForTimeout(450);
    const blurred = await readState();
    expect(blurred).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      opacity: "1",
    });
    expect(blurred.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(blurred.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(blurred.background).toBe(atRest.background);
  });
});

'''

open(SPEC, "a", encoding="utf-8").write(BLOCK.lstrip("\n"))
print("appended the v146 describe block to", SPEC)
