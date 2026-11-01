#!/usr/bin/env python3
"""Append the v142 describe block (the dashboard drill-down rows' own-hover
ladders at 1280x800) to tests/e2e/dashboard.spec.ts — the PIN-ONLY cycle's
pin (the plan docs/remediation-plan-v142.md F4).

The form mirrors the v141 submit-hover pin (login-parity.spec.ts) adapted
to the cycle's own networth+drill-down pair surface (the /dashboard view's
drill-down EXPANDED state at 1280x800) and the TWO-CONTRACT ladder (the
reference's own asymmetry): the SECTION row's TINTED contract (the v43 F2
arbitrary-hex repair — hover:bg-[#f9fafb] with NO inline bg: bg
rgba(0,0,0,0)->rgb(249,250,251) under the row's own hover) + the CATEGORY
row's INERT-HOVER contract (the v29 inline-beats-utility class — the inline
backgroundColor rgb(249,250,251) persisting UNCHANGED under the row's own
hover, the hover:bg-gray-100 utility inert). The STRUCTURAL finders (the
breakdown card by its "Net Zero Breakdown" title leaf -> its closest
rounded-2xl ancestor; the section row = the card's button whose text
carries "Total Income"; the category row = the card's first button whose
trimmed text starts with "Salary" — the clone seed's first Income
category); the ONE-TIME view-state expansion click on the section row
(the v46 incident rule: view-state expansion clicks allowed — the
drill-down rows mutate no data; the rows NEVER clicked past the one
expansion — the accordion toggles on click, out of bounds); the ladder
parks the REAL pointer at (5,5) FIRST (the v22 lesson), reads the at-rest
rung, moves the REAL pointer to each row's LIVE-READ center (two-arg
mouse move — the v123 lesson), reads the section-hovered rung, then the
category-hovered rung, parks back, reads the restored rung. The
V94-COLLISION-safe axis set: the hovered rungs' end-states alone
({hoverMatch, bg, color}); the at-rest bg axes shared with the
v43/v44/v50/v53 censuses (the at-rest state — a different state from the
hover rungs); the section-hovered bg axis shared with the v43 F2 pin
(NOTED — a section-tint removal fails both, the correct drift behavior
for the shared repair); the geometry (w/h) and the transition metadata
(the v95 documented class) deliberately NOT pinned."""
import io

SPEC = "tests/e2e/dashboard.spec.ts"
MARKER = "// v142 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v142 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v142 — plan F4 (docs/remediation-plan-v142.md): the DASHBOARD DRILL-DOWN
// ROWS' OWN-HOVER LADDERS at 1280 (the cycle's own surface — the
// drill-down EXPANDED state, the v136-era NETWORTH + drill-down pair's
// THIRTEENTH re-run). The never-pinned HOVER paths of the pinned
// drill-down family: the v43 F2 pin holds the SECTION row's hovered bg
// axis alone (bg rgb(249,250,251) + cursor pointer — the arbitrary-hex
// repair's own regression axis, never the ladder); the v43/v44/v50/v53
// censuses hold the rows' AT-REST chrome (the category row's inline bg
// pinned at four states); the v44 F1 pin the expansion animation; the
// v31 pin the drill-down keyboard path; the v60 F2 pin the sub/item
// STRUCTURE — the CATEGORY row's own-hover INERT contract held by NO
// spec at ANY viewport before this pin (breakdown.spec.ts carries zero
// hover coverage), and the ladder FORM (at-rest -> hovered -> restored,
// the hoverMatch axes) never pinned on either row. THE CONSTRUCT: the
// reference's own asymmetry — the SECTION row carries hover:bg-[#f9fafb]
// with NO inline bg (dashboard-view.tsx:309, the v43 F2 repair), so its
// own-hover end-state is the TINTED contract (bg
// rgba(0,0,0,0)->rgb(249,250,251) under the row's own hover, the
// color/geometry family unchanged); the CATEGORY row carries
// hover:bg-gray-100 BUT ALSO an inline backgroundColor rgb(249,250,251)
// (dashboard-view.tsx:365 — the inline beats the utility, the v29 class),
// so its own-hover end-state is the INERT-HOVER contract (the at-rest
// inline bg persisting unchanged under the row's own hover) — measured
// byte-identical on BOTH sides by drillhover-arbit-v142.sh (the centers
// IDENTICAL both sides: section (1088,225) + category (1116,275); the
// construct deltas — the transitionProperty metadata [the v95 family:
// the reference's v3 six-prop list vs the clone's v4 gradient-var
// compile, the transitionDuration 0.15s IDENTICAL] — the documented
// classes, never pinned).
// ---------------------------------------------------------------------------
test.describe("dashboard drill-down rows own-hover ladders at 1280 (v142 — plan F4)", () => {
  test("the drill-down rows' own-hover ladders — the at-rest chrome, the section row's hovered TINTED contract, the category row's hovered INERT contract, the restore (the never-pinned hover paths)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    const card = page.locator("div.rounded-2xl").filter({ hasText: "Net Zero Breakdown" }).first();
    await expect(card).toBeVisible();

    // The ONE-TIME view-state expansion click on the Total Income section
    // (the v46 incident rule: view-state expansion clicks allowed — the
    // drill-down rows mutate no data; the rows are NEVER clicked past
    // this one expansion — the accordion toggles on click, out of bounds).
    const secRow = card.getByRole("button", { name: /Total Income/ });
    await secRow.click();
    await expect(card.getByRole("button", { name: /^Salary/ })).toBeVisible();
    await page.waitForTimeout(600); // the Collapse band's ~200ms both-directions settle

    // STRUCTURAL finders (the census's own form, shared by both sites):
    // the card by its "Net Zero Breakdown" title leaf -> its closest
    // rounded-2xl ancestor; the section row = the card's button whose
    // text carries "Total Income"; the category row = the card's first
    // button whose trimmed text starts with "Salary" (the first Income
    // category on BOTH seeds — the text cross-checked in every rung).
    const readState = () =>
      page.evaluate(() => {
        const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) =>
            (e.textContent || "").trim() === "Net Zero Breakdown" && e.children.length === 0,
        );
        const card = leaf ? leaf.closest('div[class*="rounded-2xl"]') : null;
        if (!card) return null;
        const sec = [...card.querySelectorAll("button")].find((b) =>
          /Total Income/i.test(b.textContent || ""),
        ) as HTMLElement | null;
        const cat = [...card.querySelectorAll("button")].find((b) =>
          (b.textContent || "").trim().startsWith("Salary"),
        ) as HTMLElement | null;
        if (!sec || !cat) return null;
        const rd = (el: HTMLElement) => {
          const cs = getComputedStyle(el);
          return {
            hoverMatch: el.matches(":hover"),
            txt: (el.textContent || "").trim().slice(0, 14),
            bg: cs.backgroundColor,
            color: cs.color,
          };
        };
        return { section: rd(sec), category: rd(cat) };
      });

    // The rows' LIVE-READ centers (never guessed; the rect read AFTER the
    // scrollIntoView, inside the same evaluate — the v132 form).
    const readCenter = (which: "sec" | "cat") =>
      page.evaluate((w) => {
        const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
          (e) =>
            (e.textContent || "").trim() === "Net Zero Breakdown" && e.children.length === 0,
        );
        const card = leaf ? leaf.closest('div[class*="rounded-2xl"]') : null;
        if (!card) return null;
        const el =
          w === "cat"
            ? ([...card.querySelectorAll("button")].find((b) =>
                (b.textContent || "").trim().startsWith("Salary"),
              ) as HTMLElement | null)
            : ([...card.querySelectorAll("button")].find((b) =>
                /Total Income/i.test(b.textContent || ""),
              ) as HTMLElement | null);
        if (!el) return null;
        el.scrollIntoView({ block: "center" });
        const r = el.getBoundingClientRect();
        return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
      }, which);

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the section row transparent (no inline bg —
    // the v43 F2 LIVE-hover construct), the category row on its inline
    // rgb(249,250,251) (the v29 inert-hover construct's at-rest side).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).not.toBeNull();
    expect(atRest!.section.txt).toContain("Total Income");
    expect(atRest!.category.txt).toContain("Salary");
    expect(atRest!.section.bg).toBe("rgba(0, 0, 0, 0)");
    expect(atRest!.category.bg).toBe("rgb(249, 250, 251)");
    expect(atRest!.section.hoverMatch).toBe(false);
    expect(atRest!.category.hoverMatch).toBe(false);

    // THE SECTION-HOVERED rung — the REAL pointer at the section row's
    // own live-read center (a mouse MOVE only, never a second click): the
    // TINTED contract — the bg transitioning to rgb(249,250,251) under
    // the row's own hover (the v43 F2 arbitrary-hex repair's engaged
    // value, the reference's v3 gray-50) with the color family
    // UNCHANGED; the category row NOT hovered, its inline bg UNCHANGED.
    const secCenter = await readCenter("sec");
    expect(secCenter).not.toBeNull();
    await page.mouse.move(secCenter!.x, secCenter!.y);
    await page.waitForTimeout(400); // the transition-colors 150ms settle
    const secHovered = await readState();
    expect(secHovered!.section).toMatchObject({
      hoverMatch: true,
      bg: "rgb(249, 250, 251)", // THE TINT — the v43 F2 repair's engaged gray-50
      color: "rgb(10, 10, 10)", // UNCHANGED — the row text persists
    });
    expect(secHovered!.category).toMatchObject({
      hoverMatch: false,
      bg: "rgb(249, 250, 251)", // the category row untouched by the section's hover
    });

    // THE CATEGORY-HOVERED rung — the REAL pointer moved to the category
    // row's own live-read center: the INERT-HOVER contract — the inline
    // backgroundColor rgb(249,250,251) persisting UNCHANGED under the
    // row's own hover (the inline beats the hover:bg-gray-100 utility —
    // the v29 class, both sites); the section row restored to its
    // at-rest transparent bg.
    const catCenter = await readCenter("cat");
    expect(catCenter).not.toBeNull();
    await page.mouse.move(catCenter!.x, catCenter!.y);
    await page.waitForTimeout(400);
    const catHovered = await readState();
    expect(catHovered!.section).toMatchObject({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)", // the at-rest transparent bg re-established
    });
    expect(catHovered!.category).toMatchObject({
      hoverMatch: true,
      bg: "rgb(249, 250, 251)", // THE INERT CONTRACT — the inline bg persists under hover
      color: "rgb(10, 10, 10)", // UNCHANGED
    });

    // The restore rung — the pointer re-parked at (5,5): both rows' at-rest
    // contracts re-established, byte-identical to the first rung.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual(atRest);
  });
});
'''

io.open(SPEC, "w", encoding="utf-8").write(text + BLOCK)
print("v142 pin appended to tests/e2e/dashboard.spec.ts")
