#!/usr/bin/env python3
"""Append the v116 pin to tests/e2e/items.spec.ts (the savings goal-card
kebab-trigger census at 1280 — docs/remediation-plan-v116.md F4).
The append is idempotent: a second run inserts nothing (the v113
idempotent-run duplication trap — the anchor text SURVIVES an insertion,
so the guard checks the marker before appending)."""
import sys

SPEC = "tests/e2e/items.spec.ts"
MARKER = 'test.describe("savings goal-card kebab-trigger census at 1280 (v116 — plan F4)"'

text = open(SPEC, encoding="utf-8").read()
if MARKER in text:
    print("ALREADY PRESENT — nothing appended (idempotent guard)")
    sys.exit(0)

PIN = '''

// ---------------------------------------------------------------------------
// v116 — plan F4 (docs/remediation-plan-v116.md): the v110-era savings pair's
// NINTH re-run (v58 → v65 → v74 → v80 → v86 → v92 → v98 → v104 → v110 → v116)
// found NO NEW GAP (the arbit-v116 two-half census reproducing the v104/v110
// values exactly — compare-v116-census.py: 120 axes, 80 identical + 40
// documented-class deltas, zero new; every VLM flag DOM-arbitrated to a
// documented class: the v57 payment-chip DATA-CONDITIONAL [the reference's
// savings item ships no paymentMethod — its footer renders the date-only
// DIV; the clone's items carry paymentMethods and render the SPAN pair the
// reference's own income card renders], the seed-count/seed-data classes
// [the reference's 1-item seed vs the clone's 2-item dev seed; the
// classification-VALUE badge colors], the user-identity avatar, NO FAB flag
// — the disproof not required, the v103 standing class), so the iteration
// deepens the coverage instead: the SAVINGS GOAL-CARD's KEBAB TRIGGER at
// 1280 — the hover-revealed action element on the pair's OWN target
// surface, never pinned at ANY viewport in ANY spec. The coverage map: the
// tab-walk pin holds ONLY the focus-visible reveal (the opacity "1" + the
// :focus-visible match at the Tab stop — the FOCUS path); the v98 pin holds
// the menu PANEL + the first menuitem's resting interior (the trigger's
// DOWNSTREAM, measured after a force-click — no trigger axis held); the
// v54/v51 pins hold the 390 mobile census (no trigger axis); NO spec pins
// the trigger's box chrome (h/w/radius/display/bg/color), its at-rest
// opacity "0", its HOVER-path reveal (the group-hover form — the
// focus-path pin's sibling), or its in-card geometry. Measured
// BYTE-IDENTICAL on BOTH sides by the one-shot census hover-arbit-v116.sh
// (the at-rest read with the pointer parked at (5,5), the hover read at
// the card's OWN center — the static-hover-coordinate trap documented);
// the pin's expected values are that census's own measured values.
test.describe("savings goal-card kebab-trigger census at 1280 (v116 — plan F4)", () => {
  test("the at-rest box chrome + the hover-path group-hover reveal", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();

    // The at-rest census (Playwright moves no pointer before the hover —
    // the trigger reads opacity "0"). STRUCTURAL finders: the goal card
    // via the Emergency Fund h4's rounded-xl ancestor (the v54 walk); the
    // trigger via the at-rest opacity-"0" small square button inside it.
    const census = await page.evaluate(() => {
      const h4 = [...document.querySelectorAll("h4")].find((x) =>
        /Emergency Fund/i.test((x.textContent || "").trim()),
      );
      if (!h4) return null;
      let card: HTMLElement | null =
        (h4.closest("div.rounded-xl") as HTMLElement | null) ?? h4.parentElement;
      if (!card) return null;
      const buttons = [...card.querySelectorAll("button")];
      const trigger = buttons.find(
        (b) =>
          getComputedStyle(b).opacity === "0" &&
          Math.round(b.getBoundingClientRect().width) < 60,
      );
      if (!trigger) return null;
      const cs = getComputedStyle(trigger);
      const r = trigger.getBoundingClientRect();
      const cr = card.getBoundingClientRect();
      return {
        tag: trigger.tagName,
        opacity: cs.opacity,
        display: cs.display,
        h: Math.round(r.height),
        w: Math.round(r.width),
        radius: cs.borderRadius,
        bg: cs.backgroundColor,
        color: cs.color,
        cardTop: Math.round(r.top - cr.top),
        cardRight: Math.round(cr.right - r.right),
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The at-rest box chrome + the in-card geometry — byte-identical to
    // the reference's measured census (the h4 items-start header-row
    // placement: cardTop 21 / cardRight 21).
    expect(census).toEqual({
      tag: "BUTTON",
      opacity: "0",
      display: "flex",
      h: 36,
      w: 36,
      radius: "6px",
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      cardTop: 21,
      cardRight: 21,
      docSW: 1280,
    });

    // The HOVER-path reveal — a REAL pointer hover on the card (the
    // group-hover form; the v45 F2a real-pointer precedent). The trigger
    // must read opacity "1" with its box chrome unchanged.
    const card = page.locator("main .group", { hasText: "Emergency Fund" }).first();
    await card.hover();
    const reveal = await page.evaluate(() => {
      const h4 = [...document.querySelectorAll("h4")].find((x) =>
        /Emergency Fund/i.test((x.textContent || "").trim()),
      );
      if (!h4) return null;
      let card: HTMLElement | null =
        (h4.closest("div.rounded-xl") as HTMLElement | null) ?? h4.parentElement;
      if (!card) return null;
      const buttons = [...card.querySelectorAll("button")];
      const small = buttons.filter((b) => {
        const r = b.getBoundingClientRect();
        return r.width < 60 && r.height < 60 && r.width === r.height;
      });
      if (small.length !== 1) return null;
      const t = small[0];
      const cs = getComputedStyle(t);
      const r = t.getBoundingClientRect();
      return {
        opacity: cs.opacity,
        h: Math.round(r.height),
        w: Math.round(r.width),
        radius: cs.borderRadius,
      };
    });
    expect(reveal).not.toBeNull();

    // The reveal — the group-hover opacity "1" with the box chrome held.
    expect(reveal).toEqual({ opacity: "1", h: 36, w: 36, radius: "6px" });
  });
});
'''

with open(SPEC, "a", encoding="utf-8") as f:
    f.write(PIN)
print("v116 pin appended to tests/e2e/items.spec.ts")
