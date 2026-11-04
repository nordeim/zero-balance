#!/usr/bin/env python3
"""append-pin-v153.py — append the v153 describe block to calculator.spec.ts.

THE PIN: the CALCULATOR DIALOG "Add Item" BUTTON's FOCUS-VISIBLE LADDER at
desktop 1280x800 on the pair's own calculator surface (the Rent Calculator
dialog opened on /expenses — the v147-era LOGIN + CALCULATOR pair's
FIFTEENTH re-run, the pair's own viewport) — the never-pinned KEYBOARD PATH
of the pinned Add-button family's DIALOG INSTANCE (the sibling-completion
form, the v149/v150/v151/v152 precedent: the family's focus ladders closed
on EVERY page-header sibling [dashboard v35 @1280 -> networth v144 @390 ->
income v145 @1280 -> savings v146 @1280 -> networth-liability v150 @390 ->
expenses v151 @1280]; this pin closes the family's CALCULATOR member — the
zb-btn-add-sm variant inside the Rent Calculator dialog, in the same dialog
as the v135 X-focus pin).

The measured contract (additemfocus-discovery-v153.sh, BOTH sides, NO GAP):
- at-rest: outline none / 3px / 0px, opacity 1, the VISIBLE ambient pair
  (the v11 G2a bare shadow, toContain — the invisible lead-layer construct
  never pinned), the orange calculator gradient, the 110x32 geometry, the
  12px/500 white sm-variant chrome. The at-rest outlineColor computed form
  deliberately NOT asserted (the v95 lab() discipline).
- focused (focusVisible:true): fv true + the v11 G2c FOUR-layer composite
  (the white zero-spread lead + the 1px #0a0a0a ring + the two ambient
  layers, each asserted via toContain) + the outline 2px solid TRANSPARENT
  + offset 2px (v3 outline-none form — IDENTICAL both sides, unlike the
  at-rest computed form) + the orange gradient + opacity UNCHANGED under
  focus (the v11 G4 no-hover-fade family: focus != hover) + the geometry
  unchanged.
- blurred: the at-rest contract re-established.

The dialog-open path (the v135 pin's own form — the standing read-only
form): the seeded count settle line, the Rent-card hover (the hover-revealed
Calculate action), the Calculate click, the 400ms dialog settle. The ROLE
finder: the dialog Add Item button (the clone's Radix dialog carries
role=dialog + the accessible name; the ONLY "Add Item" button in the dialog
— the empty-state twin "Add First Item" renders only when lineItems is
empty, NOT the case under the seeded fixture). The REAL Chromium
focus({focusVisible: true}) engagement (the v35 S2 idiom — the REAL
FocusOptions member; the v25 plain-focus lesson does not apply); the button
NEVER clicked (it opens the line-item modal — OUT OF BOUNDS under the v46
rule; focus() dispatches no click); the (5,5)-parked pointer first (the
v22 lesson); the blur restore; the 450ms settles (the v136 discipline).
"""
import io

SPEC = "tests/e2e/calculator.spec.ts"
MARKER = "// v153 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v153 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v153 — plan F4 (docs/remediation-plan-v153.md): the CALCULATOR DIALOG
// "Add Item" BUTTON's FOCUS-VISIBLE LADDER at desktop 1280x800 (the
// cycle's own surface — the Rent Calculator dialog opened on /expenses,
// the v147-era LOGIN + CALCULATOR pair's FIFTEENTH re-run). The
// never-pinned KEYBOARD PATH of the pinned Add-button family's DIALOG
// INSTANCE (the sibling-completion form, the v149/v150/v151/v152
// precedent: the family's focus ladders closed on EVERY page-header
// sibling [the v35 S2 dashboard header Add Item at 1280 — the
// DIFFERENT-ELEMENT quick-action card family; the v144 networth Add Asset
// at 390; the v145 income header Add Income at 1280; the v146 savings
// header Add Savings at 1280; the v150 networth Add Liability at 390; the
// v151 expenses header Add Expense at 1280]; THIS pin closes the family's
// CALCULATOR member — the zb-btn-add-sm variant inside the Rent Calculator
// dialog, in the same dialog as the v135 X-focus pin; the v81 census holds
// this button's AT-REST chrome only [110x32, 12px/500, the orange
// gradient, white]; the v129 own-hover pin's finder EXPLICITLY EXCLUDES it;
// the button's focused state held by NO spec at ANY viewport before this
// pin [the suite-wide survey: rg "Add Item" across tests/e2e/*.spec.ts —
// the focus/ladder matches are the DIFFERENT-ELEMENT dashboard quick-action
// card + the v145/v146/v151 OUT-OF-BOUNDS comments]; the button is a real
// BUTTON on BOTH sites [the v81 cycle measured the reference's own
// calculator Add Item button live at 1280]).
// THE CONSTRUCT: the globals.css v11 G2c composite — the .zb-btn-add
// family sm variant (calculator-dialog.tsx:176, className="zb-btn-add
// zb-btn-add-sm text-white" + the ADD_BUTTON_GRADIENTS.calculator orange
// gradient) — outline 2px solid TRANSPARENT + offset 2px (v3's
// outline-none form) + the FOUR-layer box-shadow (the white zero-spread
// lead + the shadcn 1px #0a0a0a ring + the gradient family's two ambient
// 0.1 layers), the gradient + opacity UNCHANGED under focus (the v11 G4
// no-hover-fade family: focus != hover) — measured BYTE-IDENTICAL on BOTH
// sides by additemfocus-discovery-v153.sh (the sole deltas: the at-rest
// outlineColor computed form — REF rgba(10,10,10,0.5) vs CLONE the v4
// lab() twin — the v95 class; the at-rest invisible lead-layer construct
// — REF's two transparent zero-spread leads vs CLONE none — the v3/v4
// construct class; both invisible by construction, NEVER pinned).
// ---------------------------------------------------------------------------
test.describe("calculator Add Item button focus-visible ladder at 1280 (v153 — plan F4)", () => {
  test("the Add Item button's focus-visible composite — the at-rest chrome, the focused v11 G2c four-layer composite + the UNCHANGED focus != hover family, the blur restore (the never-pinned keyboard path of the Add-button family's DIALOG instance)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    // The settle pattern (the v135 pin's own form): the seeded count
    // subtitle before interacting (the items views' formatMoney — no
    // grouping: "$2235.00").
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();

    // Open the Rent calculator (the v135 pin's form: the hover-revealed
    // Calculate action; the native locator click IS the full pointer
    // sequence — the v46 lesson).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(400);

    // ROLE finder: the dialog's Add Item button (the ONLY "Add Item"
    // button in the dialog — the empty-state twin "Add First Item"
    // renders only when lineItems is empty, NOT the case under the
    // seeded fixture).
    const add = dialog.getByRole("button", { name: /^Add Item$/ });
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
          color: cs.color,
          fs: cs.fontSize,
          fw: cs.fontWeight,
          w: (el as HTMLElement).offsetWidth,
          h: (el as HTMLElement).offsetHeight,
        };
      });

    // The at-rest rung — the REAL pointer parked at (5,5) FIRST (the v22
    // lesson): no focus, no ring (style none, the CSS-wide medium 3px,
    // offset 0px), the button's at-rest chrome — the VISIBLE ambient
    // layers (the v37-O1-COLLISION-safe toContain form: the invisible
    // lead-layer construct — the REF v3 four-slot form vs the CLONE
    // two-layer form — is the documented class, NEVER pinned) + the
    // orange calculator gradient + the 110x32 geometry + the sm-variant
    // 12px/500 white chrome. The at-rest outlineColor (the v4 lab()
    // computed form) deliberately NOT asserted (the v95 discipline).
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
      color: "rgb(255, 255, 255)",
      fs: "12px",
      fw: "500",
      w: 110,
      h: 32,
    });
    expect(atRest.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(atRest.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(atRest.background).toBe(
      "linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))",
    );

    // THE FOCUSED RUNG — the REAL Chromium focus({focusVisible: true})
    // (the v35 S2 idiom — the REAL FocusOptions member; a programmatic
    // PLAIN focus never engages :focus-visible, the v25 lesson — the
    // focusVisible form does). The button is NEVER clicked (it opens
    // the line-item modal — OUT OF BOUNDS under the v46 rule; focus()
    // dispatches no click). THE v11 G2c COMPOSITE engages (outline 2px
    // solid TRANSPARENT + offset 2px — v3's outline-none form, IDENTICAL
    // both sides — + the FOUR-layer shadow: the white zero-spread lead +
    // the 1px #0a0a0a ring + the two ambient layers) while the button
    // chrome stays UNCHANGED — focus != hover: opacity stays 1 (the v11
    // G4 no-fade family), the orange gradient never moves, the geometry
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
      color: "rgb(255, 255, 255)",
      fs: "12px",
      fw: "500",
      w: 110,
      h: 32,
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
      w: 110,
      h: 32,
    });
    expect(blurred.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(blurred.boxShadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(blurred.background).toBe(atRest.background);
  });
});
'''

io.open(SPEC, "w", encoding="utf-8").write(text + BLOCK)
added = BLOCK.count("\n")
print(f"appended the v153 describe block to {SPEC} (+{added} lines)")
