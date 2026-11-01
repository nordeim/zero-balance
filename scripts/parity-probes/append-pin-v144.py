#!/usr/bin/env python3
"""Append the v144 describe block (the networth Add Asset button's
focus-visible ladder at mobile 390x844) to tests/e2e/networth.spec.ts —
the PIN-ONLY cycle's pin (the plan docs/remediation-plan-v144.md F4).

The form mirrors the v143 focus-visible ladder precedent adapted to the
cycle's own mobile-twins surface (the /networth view, the v63-era twin,
at the pair's own 390 viewport). THE CONSTRUCT: the globals.css v11 G2c
COMPOSITE — the clone's Add Asset button carries the .zb-btn-add family
(net-worth-view.tsx:427 — the section-header button, the FIRST 'Add
Asset' button in DOM order; the empty-state twin renders only when
assets.length === 0, NOT the case on either site), so the focused
end-state is outline 2px TRANSPARENT + offset 2px (v3's outline-none
form) + the FOUR-layer box-shadow (the white zero-spread lead + the
shadcn 1px #0a0a0a ring + the gradient family's two ambient layers) —
measured BYTE-IDENTICAL on BOTH sides by addfocus-arbit-v144.sh (the
sole deltas: the at-rest outlineColor computed form — rgba(10,10,10,0.5)
vs the v4 lab() twin, the documented v43-F2-class construct, NEVER
pinned per the v95 discipline — and the at-rest invisible lead-layer
construct — the v3 four-slot form vs the v11 G2a two-layer form, the
v66 INVISIBLE class, the visible layers identical, never pinned per the
v66 discipline). The ROLE finder (the button whose accessible name is
exactly "Add Asset" — the v143 pin's own getByRole family); the REAL
Chromium focus({focusVisible: true}) engagement (the v35 S2 idiom — the
REAL FocusOptions member; the v25 plain-focus lesson does not apply);
the button NEVER clicked (it opens the Add Asset dialog — OUT OF BOUNDS
under the v46 rule); the (5,5)-parked pointer first (the v22 lesson);
the blur restore; the 450ms settle (the v136 discipline). The
V66-COLLISION-safe shadow form: the at-rest rung asserts the VISIBLE
ambient layers via toContain (the lead-layer count never pinned); the
focused rung asserts each of the four composite layers via toContain
(the v35 S2 form — byte-identical both sides by the census). The
V95-COLLISION-safe axis set: the at-rest outlineColor deliberately NOT
asserted (toMatchObject at the at-rest/blurred rungs); the focused
outlineColor asserted ("rgba(0, 0, 0, 0)" — the composite's own
transparent form, deterministic)."""
import io

SPEC = "tests/e2e/networth.spec.ts"
MARKER = "// v144 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v144 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v144 — plan F4 (docs/remediation-plan-v144.md): the NETWORTH ADD ASSET
// button's FOCUS-VISIBLE LADDER at mobile 390 (the cycle's own surface — the
// /networth view, the v138-era MOBILE-TWINS pair's THIRTEENTH re-run). The
// never-pinned KEYBOARD PATH of the pinned Add-Asset family (the v5 pin
// holds the GRADIENT at-rest; the v94 F4 pin the at-rest chrome on the
// section row at 1280 [36×134, the zb-btn-add family]; the v11 G2c
// composite pinned ONLY on the DIFFERENT-ELEMENT dashboard header Add Item
// button at 1280 [the v35 S2 single-rung form] — this button's focused
// state held by NO spec at ANY viewport before this pin [the suite-wide
// survey: rg 'Add Asset' across tests/e2e/*.spec.ts — zero hover/focus/
// ladder matches]; the button is a real BUTTON on BOTH sites [the v94
// cycle measured the reference's own Add Asset button live]). THE
// CONSTRUCT: the globals.css v11 G2c COMPOSITE — the .zb-btn-add family
// (net-worth-view.tsx:427 — the section-header button, the FIRST in DOM
// order; the empty-state twin renders only when assets.length === 0) —
// outline 2px TRANSPARENT + offset 2px (v3's outline-none form) + the
// FOUR-layer box-shadow (the white zero-spread lead + the shadcn 1px
// #0a0a0a ring + the gradient family's two ambient layers), the gradient
// + opacity UNCHANGED under focus (the v11 G4 no-hover-fade family:
// focus != hover) — measured BYTE-IDENTICAL on BOTH sides by
// addfocus-arbit-v144.sh (the sole deltas: the at-rest outlineColor
// computed form — the v4 lab() twin — and the at-rest invisible
// lead-layer construct — the v66 class — both never pinned).
// ---------------------------------------------------------------------------
test.describe("networth Add Asset button focus-visible ladder at 390 (v144 — plan F4)", () => {
  test("the Add Asset button's focus-visible composite — the at-rest chrome, the focused v11 G2c four-layer composite + the UNCHANGED focus != hover family, the blur restore (the never-pinned keyboard path)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    // The settle pattern (the v138 idiom: the Assets tab visible before
    // any interaction) + the seeded count line.
    await expect(page.getByRole("tab", { name: /Assets/i })).toBeVisible();
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    await page.waitForTimeout(400);

    // ROLE finder (the v143 pin's own family): the button whose accessible
    // name is exactly "Add Asset" (the section-header button — the FIRST
    // 'Add Asset' button in DOM order; the empty-state twin renders only
    // when assets.length === 0, NOT the case under the seed).
    const add = page.getByRole("button", { name: /^Add Asset$/ });
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
    // forest→lime gradient + opacity 1 (the v11 G4 no-fade contract).
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
      "linear-gradient(135deg, rgb(45, 90, 74), rgb(143, 188, 63))",
    );

    // THE FOCUSED RUNG — the REAL Chromium focus({focusVisible: true})
    // (the v35 S2 idiom — the REAL FocusOptions member; a programmatic
    // PLAIN focus never engages :focus-visible, the v25 lesson — the
    // focusVisible form does). The button is NEVER clicked (it opens the
    // Add Asset dialog — OUT OF BOUNDS under the v46 rule; focus()
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

text += BLOCK
io.open(SPEC, "w", encoding="utf-8").write(text)
print(f"appended the v144 describe block ({len(BLOCK.splitlines())} lines) to {SPEC}")
