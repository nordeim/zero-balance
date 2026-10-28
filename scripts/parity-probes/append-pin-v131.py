#!/usr/bin/env python3
"""Append the v131 describe block to tests/e2e/dashboard.spec.ts (the
line-append form — the v112 dashboard.spec + v120/v124 networth + v128
items + v130 networth precedents: the file is ~4.9k lines, the Edit
old_str is unwieldy; the block appended at EOF)."""

BLOCK = r'''

// ---------------------------------------------------------------------------
// v131 — plan F4 (docs/remediation-plan-v131.md): the INTERACTIVE STAT
// CARD's OWN-HOVER REVEAL census at 1280 (the pair's OWN surface — the
// /dashboard view's stat grid). The never-pinned HOVER END-STATES of the
// most-pinned family on the dashboard: the v40 pin holds the TAB stops +
// the geometry bands + the Enter/Space SUPERSET activation (the
// reference's big stat cards are INERT divs — dead UI; the clone's
// route to the type view); the v42 pin the hero grid census; the v51 F2
// pin the AT-REST grid/card/circle/icon chrome; the v88 pin the
// count-row + the h-px divider + the trend colors; the v125 pin the
// QUICK-ACTION cards' hover end-states (dashboard-view.tsx:885-899 — a
// DIFFERENT component family); every chevron pin the DRILL-DOWN family
// [v43/v44]. The stat card's hover end-states — the RADIAL-GRADIENT
// CIRCLE's group-hover:opacity-10 (dashboard-view.tsx:587) + the
// ChevronRight's group-hover:opacity-100 (:602) — held by NO spec at ANY
// viewport before this pin. Measured BYTE-IDENTICAL on BOTH sides by the
// one-shot census stathover-arbit-v131.sh (the hover-ladder form —
// READ-ONLY per the v46 rule: login + passive navigation + a REAL
// pointer hover only; the hover reveals chrome, it clicks nothing — the
// CLONE's card CLICK NAVIGATES to /income, so the card is NEVER
// clicked): the reference's own INERT card carries the SAME reveal
// family (pure-CSS group-hover chrome — absolute top-0 right-0 w-32
// h-32 rounded-full opacity-0 group-hover:opacity-10 + the
// lucide-chevron-right w-5 h-5 opacity-0 group-hover:opacity-100), so
// the reveals are the reference's own idiom — a BOTH-SIDES parity axis,
// NOT a superset axis (only the INTERACTIVITY is superset): the at-rest
// {radial opacity 0, chevron opacity 0} -> the OWN-HOVERED {radial
// opacity 0.1, chevron opacity 1, cardHover true} -> the restored
// at-rest, the transitions opacity 0.3s/0.2s identical (the metadata
// axes recorded in the census, NOT pinned — the v95 family discipline,
// and the v125 pin's own axis-set precedent on the quick-action twin:
// the V94-COLLISION criterion keeps this spec the SOLE failure surface
// for the reveal-family mutation).
// ---------------------------------------------------------------------------
test.describe("stat-card own-hover reveal census at 1280 (v131 — plan F4)", () => {
  test("the Total Income card's own-hover ladder — the at-rest state, the hovered radial-circle + chevron reveals, the restore (the never-pinned hover end-states)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    // the settle pattern (the v40/v51 idiom: the seeded net-balance text
    // before any interaction).
    await expect(page.getByText("+$2065.00")).toBeVisible();
    await page.waitForTimeout(400);

    // The v40 finder — the clone's interactive stat card (the
    // SUPERSET div[role=button]; the reference's is an inert div).
    const card = page.locator('div[role="button"]').filter({ hasText: "Total Income" });
    await expect(card).toBeVisible();

    // STRUCTURAL finders (tag/class-agnostic by computed shape, per the
    // v107 lesson): the RADIAL = the absolute 9999px-radius decorative
    // div; the CHEVRON = the 19..21 width band (state-INDEPENDENT across
    // the ladder's rungs — the type icon is w-6 = 24px, the trend icon
    // w-4 = 16px; the at-rest opacity-0 form would FAIL on the hovered
    // rung, the opacity being the animated axis this pin measures).
    const readState = () =>
      card.evaluate((el) => {
        const radial = [...el.querySelectorAll("div")].find((d) => {
          const cs = getComputedStyle(d);
          return cs.position === "absolute" && cs.borderRadius === "9999px";
        });
        const chevron = [...el.querySelectorAll("svg")].find((s) => {
          const r = s.getBoundingClientRect();
          return r.width >= 19 && r.width <= 21;
        });
        if (!radial || !chevron) return null;
        return {
          cardHover: el.matches(":hover"),
          radial: { opacity: getComputedStyle(radial).opacity },
          chevron: { opacity: getComputedStyle(chevron).opacity },
        };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): both reveals retired (opacity 0), the
    // contrast the hover axes need.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({
      cardHover: false,
      radial: { opacity: "0" },
      chevron: { opacity: "0" },
    });

    // THE HOVER END-STATES — the REAL pointer on the card (Playwright's
    // locator hover IS the real pointer move — the v43/v45/v125 idiom):
    // the radial's group-hover:opacity-10 reveal + the chevron's
    // group-hover:opacity-100 reveal + the card's own :hover state. The
    // card is NEVER clicked (the v46 rule — the click navigates).
    await card.hover();
    await page.waitForTimeout(400); // the 0.3s transition settle
    const hovered = await readState();
    expect(hovered).toEqual({
      cardHover: true,
      radial: { opacity: "0.1" },
      chevron: { opacity: "1" },
    });

    // The restore rung — the pointer re-parked at (5,5): both reveals
    // disengaged, the at-rest contract re-established.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual({
      cardHover: false,
      radial: { opacity: "0" },
      chevron: { opacity: "0" },
    });
  });
});
'''

PATH = "tests/e2e/dashboard.spec.ts"
with open(PATH, "r", encoding="utf-8") as f:
    text = f.read()

# guard: never append twice
if "v131 — plan F4" in text:
    raise SystemExit("the v131 block already present — refusing to append twice")

if not text.endswith("\n"):
    text += "\n"
text += BLOCK.lstrip("\n")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(text)

lines = text.count("\n") + 1
print(f"appended the v131 describe block -> {PATH} ({lines} lines)")
