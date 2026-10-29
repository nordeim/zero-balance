#!/usr/bin/env python3
"""Append the v133 describe block (the item-card action buttons' own-hover
ladders at 1280x800) to tests/e2e/items.spec.ts — the PIN-ONLY cycle's pin
(the plan docs/remediation-plan-v133.md F4).

The form mirrors the v127 item-card badge pin (items.spec.ts) adapted to
the cycle's own items-pair surface (the /expenses view at 1280x800) and
the TWO-button ladder: the STRUCTURAL tag-agnostic finder (the grid's
first card, its Edit + Calculate buttons by TEXT + the state-independent
chrome guards radius 6px + fs 12px — the v107 lesson); the ladder parks
the REAL pointer at (5,5) FIRST (the v22 lesson), reads the at-rest rung
(both buttons white, the action row hidden), moves the REAL pointer to
the EDIT button's LIVE-READ center (two-arg mouse move — the v123
lesson), reads the edit own-hovered rung (the row revealed by the card's
own group-hover), moves to the CALCULATE button's live center, reads the
calc own-hovered rung, parks back, reads the restored rung. The
V94-COLLISION-safe axis set: the end-states alone ({hoverMatch, bg,
color} per button + the rowOpacity}); the transition metadata (the v95
documented class) and the label-dependent w/h deliberately NOT pinned."""
import io

SPEC = "tests/e2e/items.spec.ts"
MARKER = "// v133 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v133 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v133 — plan F4 (docs/remediation-plan-v133.md): the ITEM-CARD ACTION
// BUTTONS' OWN-HOVER LADDERS at 1280 (the cycle's own surface — the
// /expenses view, the v127-era ITEMS pair's TWELFTH re-run). The
// never-pinned HOVER END-STATES of the v45-pinned at-rest family: the
// v45 F1b pin holds the action row's at-rest chrome (top/right/gap/btnH/
// padX/fs) + the buttons' at-rest shadow-md + the row's reveal (opacity
// 0 -> 1 on card hover) + the card's INERT hovered shadow; the v28 G2
// pin holds the Edit button's hover:text-accent-foreground CLASS TOKEN +
// the focus-visible families — never the computed END-STATE; the v36 S3
// pin the items-view Tab walk (the kebab's focus reveal — a different
// element, the clone's superset #7 on non-expense cards only); the v127
// pin the ITEM-CARD BADGE's hover end-state (a different element in the
// same card). The buttons' hovered computed values — Edit bg
// rgb(249,250,251) + color rgb(23,23,23), Calculate bg rgb(255,247,237)
// — held by NO spec on THIS file at ANY viewport (the only computed
// rgb(249,250,251) assertions in the suite are the dashboard's category
// rows — a different component). Measured BYTE-IDENTICAL on BOTH sides
// by the one-shot census itemhover-arbit-v133.sh (the two-button ladder
// form — READ-ONLY per the v46 rule: the hover reveals chrome, it clicks
// nothing; the buttons OPEN dialogs on click, never clicked): the
// at-rest {both white, rowOpacity 0} -> the EDIT OWN-HOVERED {bg
// rgb(249,250,251) + color rgb(23,23,23), rowOpacity 1} -> the CALC
// OWN-HOVERED {bg rgb(255,247,237), the orange color unchanged,
// rowOpacity 1} -> the restored at-rest; the transitionDuration 0.15s
// identical both sides (recorded in the census, NOT pinned — the v95
// family discipline; the label-dependent w/h likewise not pinned).
// ---------------------------------------------------------------------------
test.describe("item-card action buttons own-hover ladders at 1280 (v133 — plan F4)", () => {
  test("the first expense card's Edit + Calculate buttons — the at-rest chrome, the own-hovered tints, the restore (the never-pinned hover end-states on this file)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    // the settle pattern: wait for the seeded first card before interacting
    await expect(page.getByText("Entertainment").first()).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the v46 F3 family, tag-agnostic per the v107
    // lesson): the grid's first card, its Edit + Calculate buttons by
    // TEXT + the state-independent chrome guards (radius 6px + fs 12px).
    const readState = () =>
      page.evaluate(() => {
        const grid = [...document.querySelectorAll("div")].find(
          (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
        );
        if (!grid) return null;
        const card = grid.children[0] as HTMLElement | null;
        if (!card) return null;
        const btns = [...card.querySelectorAll("button, [role=button]")];
        const edit = btns.find((b) => (b.textContent || "").trim() === "Edit");
        const calc = btns.find((b) => (b.textContent || "").trim() === "Calculate");
        if (!edit || !calc) return null;
        const guard = (el: Element) => {
          const cs = getComputedStyle(el);
          return cs.borderRadius === "6px" && cs.fontSize === "12px";
        };
        if (!guard(edit) || !guard(calc)) return null;
        let row: HTMLElement | null = edit.parentElement;
        while (row && row !== card) {
          const cs = getComputedStyle(row);
          if (cs.position === "absolute") break;
          row = row.parentElement;
        }
        const rd = (el: Element) => {
          const cs = getComputedStyle(el);
          return {
            hoverMatch: (el as HTMLElement).matches(":hover"),
            bg: cs.backgroundColor,
            color: cs.color,
          };
        };
        return {
          edit: rd(edit),
          calc: rd(calc),
          rowOpacity: row ? getComputedStyle(row).opacity : null,
        };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): both buttons white (the Edit's zinc-900
    // text, the Calculate's orange text), the action row hidden.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({
      edit: { hoverMatch: false, bg: "rgb(255, 255, 255)", color: "rgb(10, 10, 10)" },
      calc: { hoverMatch: false, bg: "rgb(255, 255, 255)", color: "rgb(234, 88, 12)" },
      rowOpacity: "0",
    });

    // The buttons' LIVE-READ centers (never guessed; the mouse move takes
    // x y as TWO args — the v123 lesson).
    const centers = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement | null;
      if (!card) return null;
      const btns = [...card.querySelectorAll("button, [role=button]")];
      const edit = btns.find((b) => (b.textContent || "").trim() === "Edit");
      const calc = btns.find((b) => (b.textContent || "").trim() === "Calculate");
      if (!edit || !calc) return null;
      const er = edit.getBoundingClientRect();
      const cr = calc.getBoundingClientRect();
      return {
        ex: Math.round(er.x + er.width / 2),
        ey: Math.round(er.y + er.height / 2),
        cx: Math.round(cr.x + cr.width / 2),
        cy: Math.round(cr.y + cr.height / 2),
      };
    });
    expect(centers).not.toBeNull();

    // THE EDIT OWN-HOVER END-STATE — the REAL pointer at the Edit
    // button's own center: the hover:bg-[#f9fafb] tint rgb(249,250,251)
    // + the hover:text-accent-foreground color rgb(23,23,23), THE
    // never-pinned axes; the row revealed by the card's own group-hover
    // (the pointer inside the card engages both).
    await page.mouse.move(centers!.ex, centers!.ey);
    await page.waitForTimeout(400); // the transition-colors 150ms settle
    const editHovered = await readState();
    expect(editHovered).toEqual({
      edit: { hoverMatch: true, bg: "rgb(249, 250, 251)", color: "rgb(23, 23, 23)" },
      calc: { hoverMatch: false, bg: "rgb(255, 255, 255)", color: "rgb(234, 88, 12)" },
      rowOpacity: "1",
    });

    // THE CALC OWN-HOVER END-STATE — the REAL pointer at the Calculate
    // button's own center: the hover:bg-[#fff7ed] tint rgb(255,247,237),
    // the orange text unchanged (no hover-text class on either site);
    // the Edit button restored to its at-rest white.
    await page.mouse.move(centers!.cx, centers!.cy);
    await page.waitForTimeout(400);
    const calcHovered = await readState();
    expect(calcHovered).toEqual({
      edit: { hoverMatch: false, bg: "rgb(255, 255, 255)", color: "rgb(10, 10, 10)" },
      calc: { hoverMatch: true, bg: "rgb(255, 247, 237)", color: "rgb(234, 88, 12)" },
      rowOpacity: "1",
    });

    // The restore rung — the pointer re-parked at (5,5): the tints
    // disengaged, the row hidden, the at-rest contract re-established.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual({
      edit: { hoverMatch: false, bg: "rgb(255, 255, 255)", color: "rgb(10, 10, 10)" },
      calc: { hoverMatch: false, bg: "rgb(255, 255, 255)", color: "rgb(234, 88, 12)" },
      rowOpacity: "0",
    });
  });
});
'''

text += BLOCK
io.open(SPEC, "w", encoding="utf-8").write(text)
print(f"appended the v133 describe block to {SPEC} (+{BLOCK.count(chr(10))} lines)")
