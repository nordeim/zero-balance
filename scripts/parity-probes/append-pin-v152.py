#!/usr/bin/env python3
"""append-pin-v152.py — append the v152 describe block to items.spec.ts.

THE PIN: the SAVINGS FILTER-CARD FREQUENCY SELECT TRIGGER's FOCUS-VISIBLE
LADDER at desktop 1280x800 on /savings (the v146-era SAVINGS pair's own
surface, the pair's own viewport) — the never-pinned KEYBOARD PATH of the
pinned filter-card Select family's FREQUENCY SIBLING (the sibling-completion
form, the v149/v150/v151 precedent: the v37 S1 pin closed the CATEGORY
trigger's focus-visible family at 1280 on /income — the CATEGORY sibling;
this pin closes the FREQUENCY sibling on the savings pair's own /savings
surface at the same viewport; the v139 pin holds BOTH triggers' OWN-HOVER
ladders — the INERT-HOVER contract, hover only, NOT focus).

The measured contract (freqfocus-discovery-v152.sh, BOTH sides, NO GAP):
- at-rest: outline none / 3px / 0px, the border untinted rgb(229,229,229),
  the 216x36 geometry, the VISIBLE ambient layer (the v37-O1-COLLISION-safe
  toContain form — the lead-layer count construct never pinned).
- focused (focusVisible:true): fv true + the 1px #0a0a0a ring layered over
  the ambient (each asserted via toContain) + the border untinted + the
  geometry unchanged. The outline-family axes deliberately NOT asserted
  (the v148 tablist-trigger invisible-construct discipline: the reference's
  v3 ENGAGED-but-TRANSPARENT outline [solid 2px rgba(0,0,0,0) + offset 2px]
  vs the clone's v4 none — both forms invisible by construction).
- blurred: the at-rest contract re-established.

The V95-COLLISION-safe axis set (the at-rest outlineColor computed form
deliberately NOT asserted); the ROLE finder (the combobox whose accessible
name is "Filter by frequency" — the clone's trigger carries the aria-label,
the a11y superset over the reference's unlabeled trigger; the only
frequency combobox on the page); the REAL Chromium focus({focusVisible:
true}) engagement (the v35 S2 idiom — the REAL FocusOptions member; the
v25 plain-focus lesson does not apply); the trigger NEVER clicked (it opens
the Select dropdown — OUT OF BOUNDS under the v46 rule); the (5,5)-parked
pointer first (the v22 lesson); the blur restore; the 450ms settle (the
v136 discipline).
"""
import io

SPEC = "tests/e2e/items.spec.ts"
MARKER = "// v152 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v152 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v152 — plan F4 (docs/remediation-plan-v152.md): the SAVINGS FILTER-CARD
// FREQUENCY SELECT TRIGGER's FOCUS-VISIBLE LADDER at desktop 1280x800
// (the cycle's own surface — the /savings view, the v146-era SAVINGS
// pair's FIFTEENTH re-run). The never-pinned KEYBOARD PATH of the pinned
// filter-card Select family's FREQUENCY SIBLING (the sibling-completion
// form, the v149/v150/v151 precedent: the v37 S1 pin closed the CATEGORY
// trigger's focus-visible family at 1280 on /income [the REAL-Tab walk,
// the 8th Tab — the 1px #0a0a0a ring + the ambient shadow + the untinted
// border + the 216x36 geometry]; THIS pin closes the FREQUENCY sibling on
// the savings pair's own /savings surface at the same viewport; the v139
// pin holds BOTH triggers' OWN-HOVER ladders [the INERT-HOVER contract —
// hover only, NOT focus]; the v64/v70 censuses hold both triggers'
// AT-REST geometry; the frequency trigger's focused state held by NO spec
// at ANY viewport before this pin [the suite-wide survey: rg 'frequency'
// across tests/e2e/*.spec.ts — 19 matches, ZERO focus/ladder matches —
// one badge-color comment + the v139 hover pin; the v37 S1 pin is the
// CATEGORY sibling only]; the trigger is a real combobox BUTTON on BOTH
// sites [the same filter-card family the v37 cycle measured live at 1280
// on /income — the reference's own /savings filter card carries the twin
// triggers, located by their text "All Categories"/"All Frequencies";
// the reference's triggers carry NO aria-labels, the clone's carry them —
// the a11y superset]).
// THE CONSTRUCT: the shadcn select.tsx ring — focus:outline-none
// focus:ring-1 focus:ring-ring (src/components/ui/select.tsx) — the 1px
// #0a0a0a ring layered over the ambient shadow-sm family, the border
// untinted rgb(229,229,229), the geometry unchanged (216x36) — measured
// BYTE-IDENTICAL on BOTH sides by freqfocus-discovery-v152.sh (the sole
// deltas: the focused outline construct — REF the v3 ENGAGED-but-
// TRANSPARENT form [solid 2px rgba(0,0,0,0) + offset 2px] vs CLONE the
// v4 none form — the v148 tablist-trigger invisible-construct class; the
// boxShadow lead-layer construct — REF the white zero-spread lead vs
// CLONE the four transparent leads — the v37 O1/v148 class; the at-rest
// outlineColor computed form — the v4 lab() twin — the v95 class; all
// invisible by construction, NEVER pinned).
// ---------------------------------------------------------------------------
test.describe("savings filter-card frequency Select trigger focus-visible ladder at 1280 (v152 — plan F4)", () => {
  test("the frequency trigger's focus-visible ring — the at-rest chrome, the focused 1px #0a0a0a ring + ambient + untinted border + geometry, the blur restore (the never-pinned keyboard path)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    // The settle pattern (the v65/v139/v146 idiom: the seeded count line
    // visible before any interaction).
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();
    await page.waitForTimeout(400);

    // ROLE finder (the v37 S1 pin's own family): the combobox whose
    // accessible name is "Filter by frequency" (the clone's trigger
    // carries the aria-label — the a11y superset over the reference's
    // unlabeled trigger; the only frequency combobox on the page).
    const trigger = page.getByRole("combobox", { name: "Filter by frequency" });
    await expect(trigger).toBeVisible();

    const readState = () =>
      trigger.evaluate((el) => {
        const cs = getComputedStyle(el);
        return {
          focused: document.activeElement === el,
          fv: el.matches(":focus-visible"),
          outlineStyle: cs.outlineStyle,
          outlineColor: cs.outlineColor,
          outlineWidth: cs.outlineWidth,
          outlineOffset: cs.outlineOffset,
          boxShadow: cs.boxShadow,
          borderColor: cs.borderColor,
          borderWidth: cs.borderWidth,
          w: (el as HTMLElement).offsetWidth,
          h: (el as HTMLElement).offsetHeight,
        };
      });

    // The at-rest rung — the REAL pointer parked at (5,5) FIRST (the v22
    // lesson): no focus, no ring (style none, the CSS-wide medium 3px,
    // offset 0px), the trigger's at-rest chrome — the VISIBLE ambient
    // layer + the untinted border + the 216x36 geometry (the
    // v37-O1-COLLISION-safe toContain form: the invisible lead-layer
    // construct — the v3 three-slot form vs the v4 five-slot form — is
    // the documented class, NEVER pinned). The at-rest outlineColor (the
    // v4 lab() computed form) deliberately NOT asserted (the v95
    // discipline).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      borderColor: "rgb(229, 229, 229)",
      borderWidth: "1px",
      w: 216,
      h: 36,
    });
    expect(atRest.boxShadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // THE FOCUSED RUNG — the REAL Chromium focus({focusVisible: true})
    // (the v35 S2 idiom — the REAL FocusOptions member; a programmatic
    // PLAIN focus never engages :focus-visible, the v25 lesson — the
    // focusVisible form does). The trigger is NEVER clicked (it opens
    // the Select dropdown — OUT OF BOUNDS under the v46 rule; focus()
    // dispatches no click). The 1px #0a0a0a ring ENGAGES, layered over
    // the ambient, the border untinted, the geometry unchanged. The
    // outline-family axes (the v3-transparent vs v4-none construct) and
    // the lead-layer constructs deliberately NOT asserted (the v148
    // discipline — both forms invisible by construction). The 450ms
    // settle (the v136 discipline).
    await trigger.evaluate((el) =>
      (el as HTMLElement).focus({ focusVisible: true } as unknown as FocusOptions),
    );
    await page.waitForTimeout(450);
    const focused = await readState();
    expect(focused).toMatchObject({
      focused: true,
      fv: true,
      borderColor: "rgb(229, 229, 229)",
      borderWidth: "1px",
      w: 216,
      h: 36,
    });
    expect(focused.boxShadow).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");
    expect(focused.boxShadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // The blurred rung — the at-rest contract re-established on every
    // axis (the ring disengages; the chrome never moved).
    await trigger.evaluate((el) => (el as HTMLElement).blur());
    await page.waitForTimeout(450);
    const blurred = await readState();
    expect(blurred).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      borderColor: "rgb(229, 229, 229)",
      borderWidth: "1px",
      w: 216,
      h: 36,
    });
    expect(blurred.boxShadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");
  });
});
'''

io.open(SPEC, "w", encoding="utf-8").write(text + BLOCK)
added = len((text + BLOCK).splitlines()) - len(text.splitlines())
print(f"appended the v152 describe block to {SPEC} (+{added} lines)")
