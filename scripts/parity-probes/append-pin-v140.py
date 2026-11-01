#!/usr/bin/env python3
"""Append the v140 describe block (the savings filter-card search input's
own-hover ladder at 1280x800) to tests/e2e/items.spec.ts — the PIN-ONLY
cycle's pin (the plan docs/remediation-plan-v140.md F4).

The form mirrors the v139 select-trigger pin (items.spec.ts) adapted to
the cycle's own savings-pair surface (the /savings view at 1280x800) and
the SINGLE-element ladder (the v128 kebab form): the STRUCTURAL finder
(the rounded-2xl white card containing an input -> its ONLY input —
tag-agnostic per the v107 lesson, the form shared by both sites; the
placeholder "Search savings items..." cross-checked); the ladder parks
the REAL pointer at (5,5) FIRST (the v22 lesson), reads the at-rest
rung (the input's inert at-rest chrome), moves the REAL pointer to the
input's LIVE-READ center (two-arg mouse move — the v123 lesson), reads
the own-hovered rung (the INERT-HOVER contract — the at-rest chrome
persisting), parks back, reads the restored rung. The
V94-COLLISION-safe axis set: the end-states alone ({hoverMatch, bg,
color, borderColor, caretColor, the shadow VISIBLE pair via toContain
[immune to the lead-slot construct]}); the transition metadata (the v95
documented class — the v3 6-prop list vs the v4 gradient-var compile)
and the w/h geometry (held by the v64 at-rest census on /income)
deliberately NOT pinned. The input is NEVER clicked — a mouse MOVE only
(the input opens nothing on hover; the census cannot mutate state)."""
import io

SPEC = "tests/e2e/items.spec.ts"
MARKER = "// v140 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v140 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v140 — plan F4 (docs/remediation-plan-v140.md): the SAVINGS FILTER-CARD
// SEARCH INPUT's OWN-HOVER LADDER at 1280 (the cycle's own surface — the
// /savings view, the v134-era SAVINGS pair's THIRTEENTH re-run). The
// never-pinned HOVER path of the pinned search family: the v37 S2 pin
// holds the input's focus-visible family + the REAL-key typing contract
// (on /income, the shared filter card); the v64 census holds the /income
// at-rest geometry (w 447/h 36/pad/radius/border); the v38 S2 pin holds
// the /savings instance's class-level chrome; the v134 survey measured
// the /savings at-rest + FOCUS ring — every search census AT-REST or
// FOCUS, the input's own-hover END-STATE held by NO spec at ANY viewport
// before this pin. THE CONSTRUCT: the input carries NO hover: utility
// (input.tsx:10 — the focus-visible + disabled + placeholder classes
// alone), so the own-hover end-state is the INERT-HOVER contract — the
// at-rest chrome persisting under the input's own hover — measured
// byte-identical on BOTH sides by searchhover-arbit-v140.sh (the input
// center REF (537,167) / CLONE (537,167); the construct deltas — the
// shadow LEAD-LAYER count [the v37 S1's own O1 note: the reference's v3
// three-slot construct vs the clone's Tailwind v4 five-slot, every lead
// a 0px-spread shadow invisible by construction; the VISIBLE pair
// byte-identical] + the transitionProperty metadata [the v95 family]
// — the documented classes, never pinned).
// ---------------------------------------------------------------------------
test.describe("savings filter-card search input own-hover ladder at 1280 (v140 — plan F4)", () => {
  test("the savings search input's own-hover ladder — the at-rest chrome, the hovered INERT-HOVER contract (no tint), the restore (the never-pinned hover path)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    // the settle pattern: wait for the seeded subtitle before interacting
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the v107 tag-agnostic lesson): the filter card
    // (the rounded-2xl [16px] white div containing an input) -> its ONLY
    // input — the form shared by both sites. The state read: the
    // hover-ladder axis set (hoverMatch + bg + color + borderColor +
    // caretColor + the shadow VISIBLE pair).
    const readState = () =>
      page.evaluate(() => {
        const card = [...document.querySelectorAll("div")].find((d) => {
          const cs = getComputedStyle(d);
          return cs.borderRadius === "16px" && cs.backgroundColor === "rgb(255, 255, 255)" && d.querySelector("input");
        });
        const input = card ? (card.querySelector("input") as HTMLInputElement | null) : null;
        if (!input) return null;
        const cs = getComputedStyle(input);
        return {
          hoverMatch: input.matches(":hover"),
          placeholder: (input.getAttribute("placeholder") || "").slice(0, 26),
          bg: cs.backgroundColor,
          color: cs.color,
          borderColor: cs.borderColor,
          shadow: cs.boxShadow,
          caretColor: cs.caretColor,
        };
      });

    // The live-read center of the input (never guessed; the rect read
    // AFTER the scrollIntoView, inside the same evaluate — the v132 form).
    const readCenter = () =>
      page.evaluate(() => {
        const card = [...document.querySelectorAll("div")].find((d) => {
          const cs = getComputedStyle(d);
          return cs.borderRadius === "16px" && cs.backgroundColor === "rgb(255, 255, 255)" && d.querySelector("input");
        });
        const input = card ? (card.querySelector("input") as HTMLInputElement | null) : null;
        if (!input) return null;
        input.scrollIntoView({ block: "center" });
        const r = input.getBoundingClientRect();
        return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the v64-pinned at-rest family's chrome
    // contract (transparent bg + the untinted #e5e5e5 border + the
    // ambient shadow-sm VISIBLE pair + the placeholder cross-check).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).not.toBeNull();
    expect(atRest).toMatchObject({
      hoverMatch: false,
      placeholder: "Search savings items...",
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      borderColor: "rgb(229, 229, 229)",
      caretColor: "rgb(10, 10, 10)",
    });
    expect(atRest!.shadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // THE OWN-HOVERED rung — the REAL pointer at the input's own
    // live-read center (a mouse MOVE only, NEVER a click — the input
    // opens nothing on hover): the INERT-HOVER contract — the at-rest
    // chrome PERSISTS under the input's own hover (no tint on either
    // site).
    const center = await readCenter();
    expect(center).not.toBeNull();
    await page.mouse.move(center!.x, center!.y);
    await page.waitForTimeout(400);
    const hovered = await readState();
    expect(hovered).toMatchObject({
      hoverMatch: true,
      placeholder: "Search savings items...",
      bg: "rgba(0, 0, 0, 0)", // UNCHANGED — the inert-hover contract
      color: "rgb(10, 10, 10)",
      borderColor: "rgb(229, 229, 229)", // UNCHANGED — no tint
      caretColor: "rgb(10, 10, 10)",
    });
    expect(hovered!.shadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // The restore rung — the pointer re-parked at (5,5): the at-rest
    // contract re-established, byte-identical to the first rung.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual(atRest);
  });
});
'''

io.open(SPEC, "w", encoding="utf-8").write(text + BLOCK)
print("v140 pin appended to tests/e2e/items.spec.ts")
