#!/usr/bin/env python3
"""append-pin-v150.py — append the v150 e2e pin to tests/e2e/networth.spec.ts.

THE PIN (the sibling-completion form adapting the v144 pin's measurement
idiom): the NETWORTH ADD LIABILITY button's FOCUS-VISIBLE LADDER at mobile
390x844 — the never-pinned keyboard path of the Add-button family's
LIABILITY sibling (the v144 pin closed the ASSET sibling at 390; this pin
closes the LIABILITY sibling on the same view at the same viewport — the
v149 sibling-completion precedent).

THE TAB-ACTIVATION PREREQUISITE: the button renders inside the Radix
TabsContent value="liabilities" panel — NOT in the DOM while the Assets
tab is active. The pin clicks the Liabilities tab FIRST (the v6 locator
form — the Playwright full pointer sequence, the v120 pointerdown-
activation lesson carried by the real click; VIEW-STATE only).

The measurement form (the v144 pin's own idiom): the at-rest rung (the
(5,5)-parked pointer, no focus, the VISIBLE ambient layers via toContain
— the v66-COLLISION-safe form; the outlineColor axes deliberately NOT
asserted, the v95 discipline) -> the FOCUSED rung (the REAL Chromium
focus({focusVisible:true}) idiom — the v35 S2 form; the v11 G2c composite:
outline 2px TRANSPARENT + offset 2px + the FOUR-layer boxShadow; the
ORANGE gradient + opacity UNCHANGED — the focus != hover family) -> the
blurred rung (the at-rest contract re-established). The button is NEVER
clicked (it opens the Add Liability dialog — OUT OF BOUNDS under the v46
rule; focus() dispatches no click).
"""
import re
import sys

SPEC = "tests/e2e/networth.spec.ts"

PIN = '''
// ---------------------------------------------------------------------------
// v150 — plan F4 (docs/remediation-plan-v150.md): the NETWORTH ADD
// LIABILITY button's FOCUS-VISIBLE LADDER at mobile 390x844 — the
// never-pinned KEYBOARD PATH of the Add-button family's LIABILITY SIBLING
// (the sibling-completion form, the v149 precedent: the v144 pin closed
// the Add Asset button's ladder at 390 — the ASSET sibling; THIS pin
// closes the LIABILITY sibling on the same view at the same viewport.
// The held family: the at-rest ORANGE gradient [the v5-form gradient
// test above], the liability CARD census at 390 [v120 F4], the badge +
// interest lines [v29 G1], the tablist focus-visible ladder at 390 [the
// v148 pin — a different element family], the kebab ladders at 1280
// [v124/v130/v136 — different elements, different viewport], the v35 S2
// composite on the DIFFERENT-ELEMENT dashboard header Add Item button at
// 1280 — the Add Liability button's focused state held by NO spec at ANY
// viewport before this pin [the suite-wide survey: rg 'Add Liability'
// across tests/e2e/*.spec.ts — zero hover/focus/ladder matches]; the
// button is a real BUTTON on BOTH sites [the same zb-btn-add family; the
// reference's own Liabilities section-header button — measured live by
// addliabfocus-discovery-v150.sh]). THE CONSTRUCT: the globals.css v11
// G2c COMPOSITE — the .zb-btn-add family (net-worth-view.tsx:512 — the
// Liabilities section-header button, the FIRST 'Add Liability' in DOM
// order; the empty-state twin renders only when liabilities.length === 0)
// — outline 2px TRANSPARENT + offset 2px (v3's outline-none form) + the
// FOUR-layer box-shadow (the white zero-spread lead + the shadcn 1px
// #0a0a0a ring + the gradient family's two ambient layers), the ORANGE
// gradient + opacity UNCHANGED under focus (the v11 G4 no-hover-fade
// family: focus != hover) — measured BYTE-IDENTICAL on BOTH sides by
// addliabfocus-discovery-v150.sh (the sole deltas: the at-rest
// outlineColor computed form — the v4 lab() twin — and the at-rest
// invisible lead-layer construct — the v66 class — both never pinned).
// THE TAB-ACTIVATION PREREQUISITE: the button renders inside the Radix
// TabsContent value="liabilities" panel — NOT in the DOM while the Assets
// tab is active (the default). The pin clicks the Liabilities tab FIRST
// (the v6 locator form; VIEW-STATE only — the v46 rule holds).
// ---------------------------------------------------------------------------
test.describe("networth Add Liability button focus-visible ladder at 390 (v150 — plan F4)", () => {
  test("the Add Liability button's focus-visible composite — the Liabilities tab activated, the at-rest chrome, the focused v11 G2c four-layer composite + the UNCHANGED focus != hover family, the blur restore (the never-pinned keyboard path of the Add-button family's LIABILITY sibling)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    // The settle pattern (the v138 idiom) + THE TAB-ACTIVATION
    // PREREQUISITE: the Liabilities tab clicked (the v6 locator form —
    // the Playwright full pointer sequence; the Radix tabs activate on
    // pointerdown, the v120 lesson) + the seeded liability count line.
    await expect(page.getByRole("tab", { name: /Assets/i })).toBeVisible();
    await page.getByRole("tab", { name: "Liabilities" }).click();
    await expect(page.getByText("2 items · $311,250")).toBeVisible();
    await page.waitForTimeout(400);

    // ROLE finder (the v144 pin's own family): the button whose accessible
    // name is exactly "Add Liability" (the section-header button — the
    // FIRST 'Add Liability' button in DOM order; the empty-state twin
    // renders only when liabilities.length === 0, NOT the case under the
    // seed).
    const add = page.getByRole("button", { name: /^Add Liability$/ });
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
    // ORANGE gradient + opacity 1 (the v11 G4 no-fade contract).
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
      "linear-gradient(135deg, rgb(224, 122, 59), rgb(245, 169, 98))",
    );

    // THE FOCUSED RUNG — the REAL Chromium focus({focusVisible: true})
    // (the v35 S2 idiom — the REAL FocusOptions member; a programmatic
    // PLAIN focus never engages :focus-visible, the v25 lesson — the
    // focusVisible form does). The button is NEVER clicked (it opens the
    // Add Liability dialog — OUT OF BOUNDS under the v46 rule; focus()
    // dispatches no click). THE v11 G2c COMPOSITE engages (outline 2px
    // TRANSPARENT + offset 2px — v3's outline-none form — + the FOUR-layer
    // shadow: the white zero-spread lead + the 1px #0a0a0a ring + the two
    // ambient layers) while the button chrome stays UNCHANGED — focus !=
    // hover: opacity stays 1 (the v11 G4 no-fade family), the ORANGE
    // gradient never moves. The 450ms settle (the v136 discipline).
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


def main():
    text = open(SPEC, encoding="utf-8").read()

    # the append point: the file must END with the v148 pin's closing
    # bracket form (the last describe block) — the pin appends after it
    if not text.rstrip().endswith("});"):
        print("FAIL: networth.spec.ts does not end with a closing describe form")
        sys.exit(1)

    # idempotence: the pin must not already exist
    if "v150 — plan F4" in text:
        print("FAIL: the v150 pin already present in networth.spec.ts")
        sys.exit(1)

    # the verification: exactly ONE existing Add Liability focus-ladder
    # describe block should NOT exist (the never-pinned survey)
    if re.search(r"test\.describe\([^)]*Add Liability[^)]*focus-visible", text):
        print("FAIL: an Add Liability focus-visible describe already exists")
        sys.exit(1)

    open(SPEC, "a", encoding="utf-8").write("\n" + PIN.lstrip("\n"))
    print(f"appended the v150 pin (+{PIN.count(chr(10))} lines)")

    # post-append verification: the v150-SPECIFIC markers (the shared
    # measurement-idiom comments — the at-rest/focused/blurred rung notes —
    # intentionally NOT checked for uniqueness: the v144/v148 pins carry the
    # same idiom comments by construction [the adapted-form derivation])
    newtext = open(SPEC, encoding="utf-8").read()
    for marker in [
        'networth Add Liability button focus-visible ladder at 390 (v150 — plan F4)',
        'name: /^Add Liability$/',
        'the LIABILITY sibling on the same view at the same viewport',
    ]:
        if newtext.count(marker) != 1:
            print(f"FAIL: marker not exactly-once after append: {marker[:60]!r} ({newtext.count(marker)}x)")
            sys.exit(1)
    # the v150 describe's three rung markers — counted WITHIN the block
    block = newtext[newtext.index("networth Add Liability button focus-visible ladder at 390"):]
    for rung_marker in [
        "The at-rest rung — the REAL pointer parked at (5,5)",
        "focus({ focusVisible: true }",
        "The blurred rung — the at-rest contract re-established",
    ]:
        if block.count(rung_marker) != 1:
            print(f"FAIL: rung marker not exactly-once within the v150 block: {rung_marker[:50]!r}")
            sys.exit(1)
    print("post-append verification: all markers exactly-once — OK")


if __name__ == "__main__":
    main()
