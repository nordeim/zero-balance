#!/usr/bin/env python3
"""append-pin-v154.py — append the v154 describe block to dashboard.spec.ts.

THE PIN: the DASHBOARD DRILL-DOWN ROWS' FOCUS-VISIBLE LADDERS at desktop
1280x800 on the pair's own drill-down surface (the Net Zero Breakdown
card's EXPANDED state on / — the Total Income section open + its first
category open, the v148-era NETWORTH + drill-down pair's FIFTEENTH re-run,
the pair's own VLM state) — the never-pinned KEYBOARD PATH of the pinned
drill-down family (the sibling-completion form, the v149/v150/v151/v152/
v153 precedent: the family's HOVER paths closed by the v142 pin [the
section TINTED + the category INERT ladders]; the family's AT-REST
censuses held by the v43/v44/v50/v53/v60 pins; the v44 F1 pin the
expansion ANIMATION; the v44 F4 pin the chevron GLYPH swaps; the
accordion pin the behavior — the rows' FOCUSED chrome held by NO spec at
ANY viewport before this pin).

The measured contract (drillfocus-discovery-v154.sh, BOTH sides, NO GAP):
- at-rest: outline none / 3px / 0px on both rows; the section row
  transparent (no inline bg — the v43 F2 LIVE-hover construct) at
  254x56 (the 1280 narrow-column form — the section label's 2-line WRAP);
  the category row on its inline rgb(249,250,251) (the v29
  inline-beats-utility construct) at 214x28; boxShadow none; the
  rgb(10,10,10) text color on both. The outlineColor computed form
  deliberately NOT asserted (the v95 lab() discipline).
- focused (focusVisible:true): the UA-DEFAULT RING on each row — fv true +
  outline auto / 1px / 0px — with the row chrome UNCHANGED under focus
  (focus != hover: the section's hover tint NOT engaged [bg rgba(0,0,0,0)
  persists], the category's inline bg persisting [rgb(249,250,251)]) + the
  geometry unchanged; the SIBLING NON-INTERFERENCE cross-check at each
  focused rung (the other row stays at its at-rest contract — the v149
  form).
- blurred: the at-rest contract re-established on both rows.

The expansion path (the v142 hover pin's own form — the standing
read-only form): the one-time view-state expansion click on the Total
Income section (view-state expansion clicks allowed — the drill-down rows
mutate no data, the v46 rule; the rows NEVER clicked past this one
expansion — the accordion toggles on click, out of bounds). The
STRUCTURAL finders (the census's own form, shared by both sites — the
reference's rows carry NO aria-expanded, the v32 S1 superset): the card by
its "Net Zero Breakdown" title leaf -> its closest rounded-2xl ancestor;
the section row = the card's button whose text carries "Total Income"; the
category row = the card's first button whose trimmed text starts with
"Salary" (the first Income category on BOTH seeds — the text cross-checked
in every rung). The REAL Chromium focus({focusVisible: true}) engagement
(the v35 S2 idiom — the REAL FocusOptions member; the v25 plain-focus
lesson does not apply); the pre-rung BLUR (the expansion click leaves DOM
focus on the clicked row — blurred clean before the at-rest rung); the
(5,5)-parked pointer first (the v22 lesson); the blur restore; the 450ms
settles (the v136 discipline).
"""
import io

SPEC = "tests/e2e/dashboard.spec.ts"
MARKER = "// v154 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v154 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v154 — plan F4 (docs/remediation-plan-v154.md): the DASHBOARD DRILL-DOWN
// ROWS' FOCUS-VISIBLE LADDERS at desktop 1280x800 (the cycle's own surface
// — the Net Zero Breakdown card's EXPANDED drill-down state on /, the
// v148-era NETWORTH + drill-down pair's FIFTEENTH re-run). The
// never-pinned KEYBOARD PATH of the pinned drill-down family (the
// sibling-completion form, the v149/v150/v151/v152/v153 precedent: the
// family's HOVER paths closed by the v142 pin [the section row's TINTED
// ladder + the category row's INERT ladder]; the family's AT-REST censuses
// held by the v43/v44/v50/v53/v60 pins; the v44 F1 pin the expansion
// ANIMATION; the v44 F4 pin the chevron GLYPH swaps; the accordion pin the
// behavior — the rows' FOCUSED chrome held by NO spec at ANY viewport
// before this pin [the suite-wide survey: ZERO focus-visible/ring
// assertions on the drill-down rows across all 24 spec files; the v40
// Tab-order walk ran on the COLLAPSED dashboard — its 16 stops never
// entered the expanded drill-down; the v31 keyboard pin is the DONUT's
// sector focus, a different element]). THE CONSTRUCT: BOTH rows are real
// <button> elements with hover utilities but NO focus utilities
// (dashboard-view.tsx:306 the section row "flex w-full -mx-2
// cursor-pointer items-center justify-between rounded-lg p-2
// transition-colors hover:bg-[#f9fafb]"; :362 the category row "flex
// w-full cursor-pointer items-center justify-between rounded-lg px-3
// py-1.5 transition-colors hover:bg-gray-100" + the inline backgroundColor
// rgb(249,250,251) — the v29 inline-beats-utility class), and the global
// button rules in globals.css set only the cursor — the UA-DEFAULT RING
// contract (outline auto / 1px / 0px — the v143/v149 quick-action-card
// family form) with each row's chrome UNCHANGED under focus (focus !=
// hover) — measured BYTE-IDENTICAL on BOTH sides by
// drillfocus-discovery-v154.sh (the sole delta: the outlineColor computed
// form — REF rgba(10,10,10,0.5) vs CLONE the v4 lab() twin — the SAME
// rendered near-black-at-50% — the v95 class, deliberately NOT asserted
// here).
// ---------------------------------------------------------------------------
test.describe("dashboard drill-down rows focus-visible ladder at 1280 (v154 — plan F4)", () => {
  test("the drill-down rows' focus-visible ladders — the at-rest chrome, the section + category rows' focused UA-default rings + the UNCHANGED focus != hover family, the blur restores (the never-pinned keyboard paths)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/dashboard");
    // The settle pattern (the v42 idiom: the card title is a plain div,
    // never a role=heading) + the seeded net-balance text before any
    // interaction.
    await expect(page.getByText("Net Zero Goal")).toBeVisible();
    await expect(page.getByText("+$2065.00")).toBeVisible();
    await page.waitForTimeout(400);

    // The ONE-TIME view-state expansion click on the Total Income section
    // (the v142 pin's own form — the v46 rule: view-state expansion clicks
    // allowed, the drill-down rows mutate no data; the rows are NEVER
    // clicked past this one expansion — the accordion toggles on click,
    // out of bounds).
    const card = page.locator("div.rounded-2xl").filter({ hasText: "Net Zero Breakdown" }).first();
    await expect(card).toBeVisible();
    const secRow = card.getByRole("button", { name: /Total Income/ });
    await secRow.click();
    await expect(card.getByRole("button", { name: /^Salary/ })).toBeVisible();
    await page.waitForTimeout(600); // the Collapse band's ~200ms both-directions settle

    // STRUCTURAL finders (the census's own form, shared by both sites —
    // the reference's rows carry NO aria-expanded, the v32 S1 superset):
    // the card by its "Net Zero Breakdown" title leaf -> its closest
    // rounded-2xl ancestor; the section row = the card's button whose
    // text carries "Total Income"; the category row = the card's first
    // button whose trimmed text starts with "Salary" (the first Income
    // category on BOTH seeds — the text cross-checked in every rung).
    // The outlineColor axis deliberately NOT read into the census (the
    // v95 lab() computed-form discipline — the REF rgba(10,10,10,0.5) vs
    // the CLONE v4 lab() twin renders identically, never pinned).
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
          const r = el.getBoundingClientRect();
          return {
            txt: (el.textContent || "").trim().slice(0, 14),
            focused: document.activeElement === el,
            fv: el.matches(":focus-visible"),
            outlineStyle: cs.outlineStyle,
            outlineWidth: cs.outlineWidth,
            outlineOffset: cs.outlineOffset,
            bg: cs.backgroundColor,
            boxShadow: cs.boxShadow,
            color: cs.color,
            w: Math.round(r.width),
            h: Math.round(r.height),
          };
        };
        return { section: rd(sec), category: rd(cat) };
      });

    // The ladder's first rung — AT-REST with the click-left focus blurred
    // clean FIRST (the expansion click leaves DOM focus on the section
    // row — blurred before the at-rest read) + the REAL pointer parked at
    // (5,5) (the v22 lesson): both rows no-focus, no ring (style none,
    // the CSS-wide medium 3px, offset 0px); the section row transparent
    // (no inline bg — the v43 F2 LIVE-hover construct) at the 1280
    // narrow-column geometry 254x56 (the section label's 2-line WRAP —
    // the v44 F2b-documented class); the category row on its inline
    // rgb(249,250,251) (the v29 inert-hover construct's at-rest side) at
    // 214x28; boxShadow none on both (the drill rows carry no shadow
    // family at any state).
    await page.evaluate(() => {
      if (document.activeElement instanceof HTMLElement) document.activeElement.blur();
    });
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).not.toBeNull();
    expect(atRest!.section.txt).toContain("Total Income");
    expect(atRest!.category.txt).toContain("Salary");
    expect(atRest!.section).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      bg: "rgba(0, 0, 0, 0)",
      boxShadow: "none",
      color: "rgb(10, 10, 10)",
      w: 254,
      h: 56,
    });
    expect(atRest!.category).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      bg: "rgb(249, 250, 251)",
      boxShadow: "none",
      color: "rgb(10, 10, 10)",
      w: 214,
      h: 28,
    });

    // THE SECTION-FOCUSED RUNG — the REAL Chromium
    // focus({focusVisible: true}) (the v35 S2 idiom — the REAL
    // FocusOptions member; a programmatic PLAIN focus never engages
    // :focus-visible, the v25 lesson — the focusVisible form does). The
    // row is NEVER re-clicked (the accordion toggles on click — OUT OF
    // BOUNDS under the v46 rule; focus() dispatches no click). THE
    // UA-DEFAULT RING engages (style auto + width 1px + offset 0px)
    // while the row chrome stays UNCHANGED — focus != hover: the
    // section's hover tint NOT engaged (bg rgba(0,0,0,0) persists), no
    // shadow. The 450ms settle covers the row's transition-colors (the
    // v136 settle discipline). The SIBLING NON-INTERFERENCE cross-check
    // (the v149 form): the category row stays at its at-rest contract.
    await page.evaluate(() => {
      const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
        (e) =>
          (e.textContent || "").trim() === "Net Zero Breakdown" && e.children.length === 0,
      );
      const card = leaf ? leaf.closest('div[class*="rounded-2xl"]') : null;
      if (!card) return;
      const sec = [...card.querySelectorAll("button")].find((b) =>
        /Total Income/i.test(b.textContent || ""),
      ) as HTMLElement | null;
      if (!sec) return;
      sec.focus({ focusVisible: true } as unknown as FocusOptions);
    });
    await page.waitForTimeout(450);
    const secFocused = await readState();
    expect(secFocused!.section).toMatchObject({
      focused: true,
      fv: true,
      outlineStyle: "auto",
      outlineWidth: "1px",
      outlineOffset: "0px",
      bg: "rgba(0, 0, 0, 0)", // focus != hover — the tint NOT engaged
      boxShadow: "none",
      color: "rgb(10, 10, 10)",
      w: 254,
      h: 56,
    });
    expect(secFocused!.category).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      bg: "rgb(249, 250, 251)",
      boxShadow: "none",
      w: 214,
      h: 28,
    });

    // THE CATEGORY-FOCUSED RUNG — the section row blurred, then the REAL
    // focusVisible engagement on the category row. The UA-DEFAULT RING
    // engages on the category row while its chrome stays UNCHANGED —
    // focus != hover: the inline rgb(249,250,251) persists (the v29
    // inert-hover construct's focused side — the inline bg beats both
    // the hover utility AND any focus implication). The SECTION row's
    // restore cross-check: back to its at-rest contract the moment its
    // blur lands.
    await page.evaluate(() => {
      const leaf = [...document.querySelectorAll("h1,h2,h3,h4,p,span")].find(
        (e) =>
          (e.textContent || "").trim() === "Net Zero Breakdown" && e.children.length === 0,
      );
      const card = leaf ? leaf.closest('div[class*="rounded-2xl"]') : null;
      if (!card) return;
      const sec = [...card.querySelectorAll("button")].find((b) =>
        /Total Income/i.test(b.textContent || ""),
      ) as HTMLElement | null;
      const cat = [...card.querySelectorAll("button")].find((b) =>
        (b.textContent || "").trim().startsWith("Salary"),
      ) as HTMLElement | null;
      if (!cat) return;
      if (sec && document.activeElement === sec) sec.blur();
      cat.focus({ focusVisible: true } as unknown as FocusOptions);
    });
    await page.waitForTimeout(450);
    const catFocused = await readState();
    expect(catFocused!.category).toMatchObject({
      focused: true,
      fv: true,
      outlineStyle: "auto",
      outlineWidth: "1px",
      outlineOffset: "0px",
      bg: "rgb(249, 250, 251)", // focus != hover — the inline bg persists
      boxShadow: "none",
      color: "rgb(10, 10, 10)",
      w: 214,
      h: 28,
    });
    expect(catFocused!.section).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      bg: "rgba(0, 0, 0, 0)",
      boxShadow: "none",
      w: 254,
      h: 56,
    });

    // The blurred rung — the at-rest contract re-established on every
    // axis, BOTH rows (the rings disengage; the chrome never moved).
    await page.evaluate(() => {
      if (document.activeElement instanceof HTMLElement) document.activeElement.blur();
    });
    await page.waitForTimeout(450);
    const blurred = await readState();
    expect(blurred!.section).toMatchObject(atRest!.section);
    expect(blurred!.category).toMatchObject(atRest!.category);
  });
});
'''

io.open(SPEC, "w", encoding="utf-8").write(text + BLOCK)
print(f"appended the v154 pin block to {SPEC} (+{BLOCK.count(chr(10))} lines)")
