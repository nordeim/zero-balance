#!/usr/bin/env python3
"""Append the v134 describe block (the savings goal-card kebab-trigger's
focus-visible ladder at 1280x800) to tests/e2e/items.spec.ts — the
PIN-ONLY cycle's pin (the plan docs/remediation-plan-v134.md F4).

The form mirrors the v36 S3 keyboard-walk pin + the v128 savings-surface
pin: the REAL Playwright Tab walk (the keyboard form — programmatic
.focus() on a BUTTON does not engage :focus-visible, the v36 S3 lesson)
finder-bounded to the Emergency Fund card's kebab trigger (the STRUCTURAL
finder: the h4 text -> the rounded-xl card -> the ONLY small square
button — the reference's trigger is unlabelled, the aria-label the
clone's a11y superset usable as the Playwright locator per the v98
precedent); the ladder parks the REAL pointer at (5,5) FIRST (the v22
lesson), reads the at-rest rung, walks the REAL Tabs to the trigger,
reads the focused rung (the superset reveal + THE never-pinned ring
layer), blurs, reads the restored rung. The V94-COLLISION-safe axis set:
the end-states alone; the transition metadata + the lead-slot construct
(the v37 S1/v95 documented class) deliberately NOT pinned."""
import io

SPEC = "tests/e2e/items.spec.ts"
MARKER = "// v134 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v134 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v134 — plan F4 (docs/remediation-plan-v134.md): the SAVINGS GOAL-CARD
// KEBAB-TRIGGER's FOCUS-VISIBLE LADDER at 1280 (the cycle's own surface —
// the /savings view, the v128-era SAVINGS pair's TWELFTH re-run). The
// never-pinned FOCUS RING axis of the pinned reveal family: the v45 F1a
// pin holds the trigger's w/h/at-rest opacity (on /income, the shared
// component); the v116 pin the at-rest box chrome + the CARD-hover
// reveal (on /savings); the v122 pin the OPEN+parked state; the v128 pin
// the OWN-HOVER tint ladder; the v36 S3 pin the keyboard REVEAL on
// /income — {fv, opacity} alone, NEVER the ring. The ring layer (the
// 1px #0a0a0a focus family every reference button carries) held by NO
// spec at ANY viewport, and the savings surface's keyboard path entirely
// unpinned. Measured clean on BOTH sides by the one-shot census
// focusladder-arbit-v134.sh (READ-ONLY per the v46 rule — the REAL Tab
// walk reveals chrome, it clicks nothing and NEVER presses Enter; the
// menu opens on click/Enter, both out of bounds): the at-rest rung
// IDENTICAL both sides {opacity 0, boxShadow none} -> the FOCUSED rung —
// REF {fv true, opacity "0" [the v36 S3 superset class — the reference's
// trigger does NOT reveal on focus], the ring computed-present
// [rgb(255,255,255) lead + rgb(10,10,10) 0px 0px 0px 1px, visually
// masked by the opacity-0]} vs CLONE {fv true, opacity "1" [the
// keyboard-reveal superset], the SAME VISIBLE ring layer
// rgb(10,10,10) 0px 0px 0px 1px, bg transparent [focus != hover]} — the
// lead-slot count differs by construction (the reference's v3 3-slot vs
// the clone's TW v4 5-slot, the v37 S1/v95 documented class — every lead
// 0px-spread, invisible); the blurred rung restored IDENTICAL. The
// walk is FINDER-BOUNDED (Tab until the active element IS the trigger —
// never a hardcoded count; the census measured REF 10 stops / CLONE 11).
// ---------------------------------------------------------------------------
test.describe("savings goal-card kebab focus-visible ladder at 1280 (v134 — plan F4)", () => {
  test("the Emergency Fund card's kebab trigger — the at-rest state, the REAL-Tab focused reveal + the 1px ring, the restore (the never-pinned focus-ring axis on this file)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    // the settle pattern: wait for the seeded card before interacting
    await expect(page.getByText("2 items · $1250.00").first()).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the v46 F3/v128 family, tag-agnostic): the
    // Emergency Fund h4 -> the rounded-xl card -> the ONLY small square
    // button. The clone's aria-label ("Actions for Emergency Fund" — the
    // a11y superset; the reference's trigger is unlabelled, the v98
    // record) is the Playwright locator.
    const findTrigger = () =>
      page.evaluate(() => {
        const h4 = [...document.querySelectorAll("h4, h3, div")].find(
          (el) => (el.textContent || "").trim() === "Emergency Fund" && el.children.length === 0,
        );
        if (!h4) return null;
        let card: HTMLElement | null = h4 as HTMLElement;
        while (card && card !== document.body) {
          const cls = typeof card.className === "string" ? card.className : "";
          if (cls.includes("rounded-xl")) break;
          card = card.parentElement;
        }
        if (!card || card === document.body) return null;
        const btns = [...card.querySelectorAll("button")].filter((b) => {
          const r = b.getBoundingClientRect();
          return r.width >= 20 && r.width <= 50 && Math.abs(r.width - r.height) < 8;
        });
        if (btns.length !== 1) return null;
        return { tag: btns[0].tagName, label: btns[0].getAttribute("aria-label") };
      });
    const target = await findTrigger();
    expect(target).toEqual({ tag: "BUTTON", label: "Actions for Emergency Fund" });
    const trigger = page.getByRole("button", { name: "Actions for Emergency Fund" });

    const readState = () =>
      page.evaluate(() => {
        const h4 = [...document.querySelectorAll("h4, h3, div")].find(
          (el) => (el.textContent || "").trim() === "Emergency Fund" && el.children.length === 0,
        );
        if (!h4) return null;
        let card: HTMLElement | null = h4 as HTMLElement;
        while (card && card !== document.body) {
          const cls = typeof card.className === "string" ? card.className : "";
          if (cls.includes("rounded-xl")) break;
          card = card.parentElement;
        }
        if (!card || card === document.body) return null;
        const btns = [...card.querySelectorAll("button")].filter((b) => {
          const r = b.getBoundingClientRect();
          return r.width >= 20 && r.width <= 50 && Math.abs(r.width - r.height) < 8;
        });
        if (btns.length !== 1) return null;
        const t = btns[0] as HTMLElement;
        const cs = getComputedStyle(t);
        const focused = document.activeElement === t;
        return {
          focused,
          fv: focused ? t.matches(":focus-visible") : false,
          hoverMatch: t.matches(":hover"),
          opacity: cs.opacity,
          bg: cs.backgroundColor,
        };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the trigger hidden (opacity 0), no tint.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({
      focused: false,
      fv: false,
      hoverMatch: false,
      opacity: "0",
      bg: "rgba(0, 0, 0, 0)",
    });

    // THE FOCUSED RUNG — a REAL keyboard walk to the trigger (the v36 S3
    // form: programmatic .focus() on a button does not engage
    // :focus-visible; a REAL Tab does). The walk is FINDER-BOUNDED: Tab
    // until the active element IS the trigger (never a hardcoded count —
    // the census measured the clone's savings stop order at 11).
    await page.evaluate(() => {
      if (document.activeElement instanceof HTMLElement) document.activeElement.blur();
    });
    for (let i = 0; i < 30; i++) {
      await page.keyboard.press("Tab");
      await page.waitForTimeout(120);
      const landed = await trigger.evaluate((el) => document.activeElement === el);
      if (landed) break;
    }
    await expect(trigger).toBeFocused();
    await page.waitForTimeout(450); // the transition-opacity 150ms settle
    const focused = await readState();
    expect(focused).toEqual({
      focused: true,
      fv: true,
      hoverMatch: false,
      opacity: "1", // the keyboard-reveal superset (the reference's stays 0 — v36 S3)
      bg: "rgba(0, 0, 0, 0)", // focus != hover — no tint on the focus path
    });
    // THE never-pinned axis — the 1px #0a0a0a focus ring layer, the
    // shadcn focus base every reference button carries (the v28 G2
    // family), computed-present on BOTH sides per the census. The VISIBLE
    // layer asserted via toContain (the lead-slot construct differs by
    // construction — the v37 S1/v95 documented class).
    const ring = await trigger.evaluate((el) => getComputedStyle(el).boxShadow);
    expect(ring).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");

    // The restore rung — blur: the reveal disengaged, the at-rest
    // contract re-established.
    await trigger.evaluate((el) => (el as HTMLElement).blur());
    await page.waitForTimeout(450);
    const blurred = await readState();
    expect(blurred).toEqual({
      focused: false,
      fv: false,
      hoverMatch: false,
      opacity: "0",
      bg: "rgba(0, 0, 0, 0)",
    });
  });
});
'''

text += BLOCK
io.open(SPEC, "w", encoding="utf-8").write(text)
print(f"appended the v134 describe block to {SPEC} (+{BLOCK.count(chr(10))} lines)")
