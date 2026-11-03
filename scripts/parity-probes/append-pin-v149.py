#!/usr/bin/env python3
"""append-pin-v149.py — append the v149 e2e pin to tests/e2e/dashboard.spec.ts.

THE PIN (the sibling-completion form): the Add Savings + Add Expense
DASHBOARD quick-action cards' FOCUS-VISIBLE ladders at desktop 1280x800 —
the never-pinned SIBLINGS of the v143-pinned Add Income card (the v143
pin + focusqa-arbit-v143.sh measured the FIRST card only; the suite-wide
survey: ZERO focus-visible/ring assertions on these two cards across all
24 spec files). The measurement idiom adapts the v143 pin's own form
(the structural role finder, the (5,5)-parked pointer, the REAL
focusVisible idiom, the 450ms settles, the outlineColor axes deliberately
NOT asserted — the v95 computed-form discipline).

ONE test (352 -> 353): both cards' full ladders + the sibling
non-interference cross-check at each focused rung (the OTHER card stays
at its at-rest contract while one is focused).

Read-only w.r.t. the file: appends ONE describe block at EOF; every
prior line untouched (the append convention).
"""
import re

SPEC = "tests/e2e/dashboard.spec.ts"

PIN = '''
// ---------------------------------------------------------------------------
// v149 — plan F4 (docs/remediation-plan-v149.md): the DASHBOARD QUICK-ACTION
// SIBLING CARDS' FOCUS-VISIBLE LADDERS at 1280 (the cycle's own surface —
// the Quick-Action row below the fold, the v143-era DASHBOARD pair's
// FOURTEENTH re-run). The never-pinned KEYBOARD PATH of the SIBLING cards
// (the v143 pin holds the Add Income card's ladder — the FIRST card only,
// measured by focusqa-arbit-v143.sh's own structural finder; the v45 F3b
// pin the card's hover:shadow-lg layers; the v61 F3 + v107 pins the
// AT-REST chrome; the v95 pin the transition TIMING metadata; the v125 pin
// the HOVER end-state ladder — the Add Savings + Add Expense cards'
// focus-visible rings + focused-chrome contracts held by NO spec at ANY
// viewport before this pin [the suite-wide survey: ZERO focus-visible/ring
// assertions on these two cards across all 24 spec files; the items.spec
// v146 pin covers the SAVINGS page-header Add Savings BUTTON — a different
// element on a different view]). THE CONSTRUCT — the sibling-completion
// form: dashboard-view.tsx renders the three cards from the SAME component
// with the same className (the ONLY per-card deltas the tile/icon/plus
// COLOR tokens), so the sibling ladders are expected to reproduce the v143
// UA-DEFAULT RING contract exactly — measured byte-identical on BOTH sides
// by tabqa2-discovery-v149.sh (the sole delta the outlineColor computed
// form — the reference's rgba(10,10,10,0.5) vs the clone's v4 lab() twin,
// the SAME rendered near-black-at-50% — the documented v43-F2 construct
// class, deliberately NOT asserted here per the v95 discipline).
// THE LADDER per card: at-rest {outline none / 3px / 0px + the card chrome
// (shadow none, tile unscaled, plus 0.5)} -> focused (focusVisible:true)
// {outline auto / 1px / 0px + the chrome UNCHANGED — focus != hover: the
// shadow-lg is :hover-only; the group-hover reveals never engage on
// focus} -> blurred {the at-rest restored} — plus the SIBLING
// NON-INTERFERENCE cross-check at each focused rung (the other card stays
// at its at-rest contract).
// ---------------------------------------------------------------------------
test.describe("quick-action sibling cards focus-visible ladder at 1280 (v149 — plan F4)", () => {
  test("the Add Savings + Add Expense cards' focus-visible rings — the at-rest chrome, the focused UA-default rings + the UNCHANGED focus != hover family, the blur restores (the never-pinned keyboard path of the sibling cards)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    // The settle pattern (the v42 idiom: the card title is a plain div,
    // never a role=heading) + the seeded net-balance text before any
    // interaction.
    await expect(page.getByText("Net Zero Goal")).toBeVisible();
    await expect(page.getByText("+$2065.00")).toBeVisible();
    await page.waitForTimeout(400);

    // The per-card ladder runner — the v143 pin's own readState idiom,
    // parameterized over the sibling cards. The tile: the v61 F3 finder
    // (radius 12px, the 30..60 box) — tag-agnostic (the v107 DIV-vs-SPAN
    // lesson). The plus: the last small svg (the v125 pin's own finder
    // form).
    const readCard = (label: string | RegExp) =>
      page.getByRole("button", { name: label }).evaluate((el) => {
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

    // The at-rest contract object (the v143 values) — shared by both
    // sibling cards; the blurred rung must equal it exactly.
    const atRestContract = {
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      boxShadow: "none",
      tileScale: "none",
      plusOpacity: "0.5",
    };
    // The focused contract (the UA-default ring + the UNCHANGED chrome).
    const focusedContract = {
      focused: true,
      fv: true,
      outlineStyle: "auto",
      outlineWidth: "1px",
      outlineOffset: "0px",
      boxShadow: "none",
      tileScale: "none",
      plusOpacity: "0.5",
    };

    const siblings: Array<"Add Savings" | "Add Expense"> = ["Add Savings", "Add Expense"];
    for (const label of siblings) {
      const qa = page.getByRole("button", { name: new RegExp(`^${label}$`) });
      await expect(qa).toBeVisible();

      // The at-rest rung — the REAL pointer parked at (5,5) FIRST (the
      // v22 lesson): no focus, no ring (style none, the CSS-wide medium
      // 3px, offset 0px), the card's at-rest chrome (shadow none — the
      // v45 F3b at-rest contract; the tile unscaled + the plus 0.5 — the
      // v125 at-rest rung's own values).
      await page.mouse.move(5, 5);
      await page.waitForTimeout(300);
      const atRest = await readCard(new RegExp(`^${label}$`));
      expect(atRest).toEqual(atRestContract);

      // THE FOCUSED RUNG — the REAL Chromium focus({focusVisible: true})
      // (the v35 S2 idiom — the REAL FocusOptions member; a programmatic
      // PLAIN focus never engages :focus-visible, the v25 lesson — the
      // focusVisible form does). The card is NEVER clicked (it opens the
      // Add Item dialog — OUT OF BOUNDS under the v46 rule; focus()
      // dispatches no click). THE UA-DEFAULT RING engages (style auto +
      // width 1px + offset 0px) while the card chrome stays UNCHANGED —
      // focus != hover: the shadow-lg NOT engaged, the group-hover
      // reveals NOT engaged. The 450ms settle covers the card's
      // transition-all duration-200 (the v136 settle discipline).
      await qa.evaluate((el) =>
        (el as HTMLElement).focus({ focusVisible: true } as unknown as FocusOptions),
      );
      await page.waitForTimeout(450);
      const focused = await readCard(new RegExp(`^${label}$`));
      expect(focused).toEqual(focusedContract);

      // THE SIBLING NON-INTERFERENCE cross-check — the OTHER card stays
      // at its at-rest contract while this one holds the focused ring
      // (the family-completion corollary: focusing one card never moves
      // the sibling's chrome).
      const other = siblings.find((s) => s !== label)!;
      const otherAtFocus = await readCard(new RegExp(`^${other}$`));
      expect(otherAtFocus).toEqual(atRestContract);

      // The blurred rung — the at-rest contract re-established on every
      // axis (the ring disengages; the chrome never moved).
      await qa.evaluate((el) => (el as HTMLElement).blur());
      await page.waitForTimeout(450);
      const blurred = await readCard(new RegExp(`^${label}$`));
      expect(blurred).toEqual(atRestContract);
    }
  });
});
'''

text = open(SPEC, encoding="utf-8").read()

# idempotence guard: never append twice
if "quick-action sibling cards focus-visible ladder at 1280 (v149" in text:
    raise SystemExit("FAIL: the v149 pin is already present in dashboard.spec.ts")

# the append: exactly one trailing newline separation from the v143 block
if not text.endswith("\n"):
    text += "\n"
text += PIN.rstrip("\n") + "\n"

open(SPEC, "w", encoding="utf-8").write(text)

# verification: the describe + test count + the structural anchors
out = open(SPEC, encoding="utf-8").read()
checks = {
    "the v149 describe present": "quick-action sibling cards focus-visible ladder at 1280 (v149 — plan F4)" in out,
    "the v149 test present": "the Add Savings + Add Expense cards' focus-visible rings" in out,
    "the at-rest contract": 'outlineWidth: "3px"' in out,
    "the focused contract": 'outlineStyle: "auto"' in out,
    "the focusVisible idiom": "focus({ focusVisible: true } as unknown as FocusOptions)" in out,
    "the blur restore": "(el as HTMLElement).blur()" in out,
    "the role finder": 'page.getByRole("button", { name: label })' in out,
    "no outlineColor measurement in the v149 block": "outlineColor: cs.outlineColor" not in PIN,
}
bad = [k for k, v in checks.items() if not v]
if bad:
    raise SystemExit(f"FAIL: post-append verification failed: {bad}")

n_describe = len(re.findall(r"^test\.describe\(", out, re.M))
n_test = len(re.findall(r"^  test\(", out, re.M))
print(f"OK: v149 pin appended to {SPEC}")
print(f"describe blocks: {n_describe}; top-level tests: {n_test}")
