#!/usr/bin/env python3
"""Append the v139 describe block (the filter-card Select triggers' own-hover
ladder at 1280x800) to tests/e2e/items.spec.ts — the PIN-ONLY cycle's pin
(the plan docs/remediation-plan-v139.md F4).

The form mirrors the v138 tablist-trigger pin (networth.spec.ts) adapted to
the cycle's own items-pair surface (the /income view at 1280x800) and the
TWO-trigger ladder: the POSITION-BASED tag-agnostic finders (button[role=
combobox] first/second — the reference's triggers carry NO aria-label, so
the position form is the ONLY form shared by both Radix sites; the v107
tag-agnostic lesson); the ladder parks the REAL pointer at (5,5) FIRST
(the v22 lesson), reads the at-rest rung (both triggers' inert at-rest
chrome), moves the REAL pointer to the CATEGORY trigger's LIVE-READ center
(two-arg mouse move — the v123 lesson), reads the category own-hovered
rung (the INERT-HOVER contract — the at-rest chrome persisting), moves to
the FREQUENCY trigger's live center, reads the frequency own-hovered rung,
parks back, reads the restored rung. The V94-COLLISION-safe axis set: the
end-states alone ({hoverMatch, bg, color, borderColor, the shadow VISIBLE
pair via toContain [immune to the lead-slot construct], iconColor} per
trigger); the transition metadata (the v95 documented class) and the w/h
geometry (held by the v64/v70 at-rest censuses) deliberately NOT pinned.
The triggers are NEVER clicked — a mouse MOVE only (the Radix Select opens
on pointerdown, the v120 lesson — a move dispatches no pointerdown, so the
ladder can never open the dropdown)."""
import io

SPEC = "tests/e2e/items.spec.ts"
MARKER = "// v139 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v139 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v139 — plan F4 (docs/remediation-plan-v139.md): the FILTER-CARD SELECT
// TRIGGERS' OWN-HOVER LADDER at 1280 (the cycle's own surface — the
// /income view, the v133-era ITEMS pair's THIRTEENTH re-run). The
// never-pinned HOVER path of the pinned filter family: the v37 S1 pin
// holds the CLOSED category trigger's focus-visible family (the 1px
// #0a0a0a ring + the ambient shadow + the untinted border + the 216x36
// geometry); the v64/v70 censuses hold BOTH triggers' at-rest geometry;
// the v50/v53 forms hold the mobile/640 chrome — every select census
// AT-REST, the trigger's own-hover END-STATE held by NO spec at ANY
// viewport before this pin. THE CONSTRUCT: the trigger carries NO hover:
// utility (select.tsx:20-27 — the focus + data-[placeholder] + disabled
// classes alone), so the own-hover end-state is the INERT-HOVER contract
// — the at-rest chrome persisting under each trigger's own hover —
// measured byte-identical on BOTH sides by selecthover-arbit-v139.sh
// (the category center REF (884,167) / CLONE (884,167), the frequency
// center REF (1115,167) / CLONE (1115,167); the construct delta — the
// shadow LEAD-LAYER count [the v37 S1's own O1 note: the reference's
// v3 three-slot construct vs the clone's Tailwind v4 five-slot, every
// lead a 0px-spread shadow invisible by construction; the VISIBLE pair
// byte-identical] — the documented class, never pinned).
// ---------------------------------------------------------------------------
test.describe("filter-card select triggers own-hover ladder at 1280 (v139 — plan F4)", () => {
  test("the category + frequency triggers' own-hover ladders — the at-rest chrome, the hovered INERT-HOVER contract (no tint on either trigger), the restore (the never-pinned hover path)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/income");
    await expect(page.getByText("2 items · $5550.00")).toBeVisible();
    await page.waitForTimeout(400);

    // POSITION-BASED finders (button[role=combobox] first/second — the
    // reference's triggers carry NO aria-label, identified by their text
    // "All Categories"/"All Frequencies"; the clone's carry the superset
    // aria-labels — the position form the ONLY form shared by both Radix
    // sites; the v107 tag-agnostic lesson). The state read: the
    // hover-ladder axis set per trigger (hoverMatch + bg + color +
    // borderColor + the shadow VISIBLE pair + the icon's currentColor).
    const readState = () =>
      page.evaluate(() => {
        const triggers = [...document.querySelectorAll("button[role=combobox]")];
        const cat = triggers[0];
        const freq = triggers[1];
        if (!cat || !freq) return null;
        const grab = (t: Element) => {
          const cs = getComputedStyle(t);
          const icon = t.querySelector("svg");
          return {
            hoverMatch: t.matches(":hover"),
            bg: cs.backgroundColor,
            color: cs.color,
            borderColor: cs.borderColor,
            shadow: cs.boxShadow,
            iconColor: icon ? getComputedStyle(icon).color : null,
          };
        };
        return { cat: grab(cat), freq: grab(freq) };
      });

    // The live-read center of a trigger (never guessed; the rect read
    // AFTER the scrollIntoView, inside the same evaluate — the v132 form).
    const readCenter = (which: "cat" | "freq") =>
      page.evaluate((w: "cat" | "freq") => {
        const triggers = [...document.querySelectorAll("button[role=combobox]")];
        const t = triggers[w === "cat" ? 0 : 1];
        if (!t) return null;
        t.scrollIntoView({ block: "center" });
        const r = t.getBoundingClientRect();
        return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
      }, which);

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the v64/v70-pinned at-rest family's chrome
    // contract, both triggers (transparent bg + the untinted #e5e5e5
    // border + the ambient shadow-sm VISIBLE pair).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).not.toBeNull();
    for (const t of [atRest!.cat, atRest!.freq]) {
      expect(t).toMatchObject({
        hoverMatch: false,
        bg: "rgba(0, 0, 0, 0)",
        color: "rgb(10, 10, 10)",
        borderColor: "rgb(229, 229, 229)",
        iconColor: "rgb(10, 10, 10)",
      });
      expect(t!.shadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");
    }

    // THE CATEGORY-HOVERED rung — the REAL pointer at the category
    // trigger's own live-read center (a mouse MOVE only, NEVER a click —
    // the Radix Select opens on pointerdown, the v120 lesson): the
    // INERT-HOVER contract — the at-rest chrome PERSISTS under the
    // trigger's own hover (no tint on either site), the frequency twin
    // untouched.
    const cc = await readCenter("cat");
    expect(cc).not.toBeNull();
    await page.mouse.move(cc!.x, cc!.y);
    await page.waitForTimeout(400);
    const catHovered = await readState();
    expect(catHovered!.cat).toMatchObject({
      hoverMatch: true,
      bg: "rgba(0, 0, 0, 0)", // UNCHANGED — the inert-hover contract
      color: "rgb(10, 10, 10)",
      borderColor: "rgb(229, 229, 229)",
      iconColor: "rgb(10, 10, 10)",
    });
    expect(catHovered!.cat!.shadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");
    expect(catHovered!.freq).toMatchObject({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      borderColor: "rgb(229, 229, 229)",
      iconColor: "rgb(10, 10, 10)",
    });
    expect(catHovered!.freq!.shadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // THE FREQUENCY-HOVERED rung — the pointer at the frequency trigger's
    // own live-read center: the second trigger's own inert-hover contract
    // (transparent bg + untinted border persisting, no tint), the
    // category twin back at rest.
    const fc = await readCenter("freq");
    expect(fc).not.toBeNull();
    await page.mouse.move(fc!.x, fc!.y);
    await page.waitForTimeout(400);
    const freqHovered = await readState();
    expect(freqHovered!.cat).toMatchObject({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      borderColor: "rgb(229, 229, 229)",
      iconColor: "rgb(10, 10, 10)",
    });
    expect(freqHovered!.cat!.shadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");
    expect(freqHovered!.freq).toMatchObject({
      hoverMatch: true,
      bg: "rgba(0, 0, 0, 0)", // UNCHANGED — the inert-hover contract
      color: "rgb(10, 10, 10)",
      borderColor: "rgb(229, 229, 229)",
      iconColor: "rgb(10, 10, 10)",
    });
    expect(freqHovered!.freq!.shadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // The restore rung — the pointer re-parked at (5,5): both triggers'
    // at-rest contracts re-established, byte-identical to the first rung.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual(atRest);
  });
});
'''

io.open(SPEC, "w", encoding="utf-8").write(text + BLOCK)
print("v139 pin appended to tests/e2e/items.spec.ts")
