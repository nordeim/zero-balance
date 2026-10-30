#!/usr/bin/env python3
"""Append the v135 describe block (the calculator X's focus-visible ladder
at 1280x800) to tests/e2e/calculator.spec.ts — the REPAIR + PIN cycle's pin
(the plan docs/remediation-plan-v135.md F4).

The form mirrors the v129 pin's own dialog-open + X-finder families + the
v134 pin's REAL keyboard walk: the native locator click on the
hover-revealed Calculate action (the full pointer sequence — the v46
lesson); the v87 X finder family (the clone's aria-label="Close" superset
finder first, the geometric 36x36-in-the-panel-top fallback); the ladder
parks the REAL pointer at (5,5) FIRST (the v22 lesson), reads the at-rest
rung, walks the REAL Tabs to the X, reads the focused rung (THE repaired
ring + the outline form), blurs, reads the restored rung. The walk is
FINDER-BOUNDED and REQUIRES :focus-visible to match — the clone's Radix
auto-focus on dialog open is PROGRAMMATIC (fv false) and must not satisfy
the landing check; the walk presses on until the X receives focus VIA THE
KEYBOARD (the census measured the clone's walk at 4 stops). The
V94-COLLISION-safe axis set: the end-states alone; the transition
metadata + the lead-slot construct deliberately NOT pinned."""
import io

SPEC = "tests/e2e/calculator.spec.ts"
MARKER = "// v135 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v135 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v135 — plan F4 (docs/remediation-plan-v135.md): the CALCULATOR X's
// FOCUS-VISIBLE LADDER at 1280 (the cycle's own surface — the /expenses
// view, the v129-era LOGIN + CALCULATOR pair's TWELFTH re-run). The
// never-pinned KEYBOARD path of the pinned close family: the v59 F1 pin
// the X's {w, h} at 1280; the v49 F3 pin {36, 36} at 640; the v53 F2 pin
// {29, 36} at 390; the v87 pin the at-rest chrome; the v129 pin the
// OWN-HOVER tint ladder; the v32 pin the ROW ACTIONS' focus family (the
// globals.css zb-row-action class) — the X itself carried NO focus class
// at ANY viewport. Measured by the both-sides one-shot census
// focusx-arbit-v135.sh (READ-ONLY per the v46 rule — the REAL Tab walk
// reveals chrome, it clicks nothing and NEVER presses Enter — the dialog
// opens on click/Enter, out of bounds): the at-rest rung IDENTICAL both
// sides -> the FOCUSED rung — REF {fv true, THE 1px #0a0a0a ring [the
// white lead + rgb(10,10,10) 0px 0px 0px 1px + the transparent tail] +
// the outline form [solid 2px rgba(0,0,0,0), offset 2px] — the shadcn
// focus base} vs CLONE {the UA default outline `auto 1px`, NO ring} —
// THE GAP. THE REPAIR: the zb-row-action class + focus-visible:ring-1
// focus-visible:ring-ring added at calculator-dialog.tsx:138 (the file's
// own sibling family — the row actions at :239/:247 carry the identical
// tokens, the v32-pinned family). The walk is FINDER-BOUNDED and requires
// :focus-visible to match (the clone's Radix auto-focus on dialog open is
// PROGRAMMATIC — fv false — and must not satisfy the landing check; the
// census measured the clone's walk at 4 stops).
// ---------------------------------------------------------------------------
test.describe("calculator X focus-visible ladder at 1280 (v135 — plan F4)", () => {
  test("the Rent calculator's X — the at-rest state, the REAL-Tab focused ring + the outline form, the restore (the never-pinned keyboard path on this file)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/expenses");
    // the settle pattern (the v129 pin's own form): the seeded count
    // subtitle before interacting (the items views' formatMoney — no
    // grouping: "$2235.00").
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();

    // Open the Rent calculator (the v129 pin's form: the hover-revealed
    // Calculate action; the native locator click IS the full pointer
    // sequence — the v46 lesson).
    const rent = page.locator("div.rounded-xl").filter({ hasText: "Rent" }).first();
    await rent.hover();
    await rent.getByRole("button", { name: "Calculate" }).click();
    const dialog = page.getByRole("dialog", { name: "Rent Calculator" });
    await expect(dialog).toBeVisible();
    await page.waitForTimeout(400);

    // The X — the v87 finder family (the v129 pin's own form): the
    // clone's aria-label="Close" superset finder first, the geometric
    // fallback (the 36x36 button in the panel's top band).
    const findX = () =>
      page.evaluate(() => {
        const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
          (d.textContent || "").includes("Rent Calculator"),
        ) as HTMLElement | undefined;
        if (!panel) return null;
        const btns = [...panel.querySelectorAll("button")];
        const close =
          btns.find((b) => (b.getAttribute("aria-label") || "") === "Close") ||
          btns.find((b) => {
            const r = b.getBoundingClientRect();
            return (
              Math.abs(r.width - 36) < 3 &&
              Math.abs(r.height - 36) < 3 &&
              r.top < panel.getBoundingClientRect().top + 80 &&
              !/^add item$/i.test((b.textContent || "").trim())
            );
          });
        if (!close) return null;
        return { tag: close.tagName, label: close.getAttribute("aria-label") };
      });
    const x = await findX();
    expect(x).toEqual({ tag: "BUTTON", label: "Close" });
    const xBtn = page
      .getByRole("dialog", { name: "Rent Calculator" })
      .getByRole("button", { name: "Close" });

    const readState = () =>
      page.evaluate(() => {
        const panel = [...document.querySelectorAll('[role="dialog"]')].find((d) =>
          (d.textContent || "").includes("Rent Calculator"),
        ) as HTMLElement | undefined;
        if (!panel) return null;
        const btns = [...panel.querySelectorAll("button")];
        const close =
          (btns.find((b) => (b.getAttribute("aria-label") || "") === "Close") ||
            btns.find((b) => {
              const r = b.getBoundingClientRect();
              return (
                Math.abs(r.width - 36) < 3 &&
                Math.abs(r.height - 36) < 3 &&
                r.top < panel.getBoundingClientRect().top + 80 &&
                !/^add item$/i.test((b.textContent || "").trim())
              );
            })) as HTMLElement | null;
        if (!close) return null;
        const cs = getComputedStyle(close);
        const onIt = document.activeElement === close;
        return {
          focused: onIt,
          fv: onIt ? close.matches(":focus-visible") : false,
          bg: cs.backgroundColor,
          color: cs.color,
          opacity: cs.opacity,
          outlineStyle: cs.outlineStyle,
          outlineWidth: cs.outlineWidth,
          outlineColor: cs.outlineColor,
          outlineOffset: cs.outlineOffset,
          boxShadow: cs.boxShadow,
        };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson). NOTE the clone's Radix auto-focus artifact:
    // the X may be the activeElement at this moment (programmatic focus,
    // fv false) — no visual effect either way (the focus-visible styles
    // do not apply without :focus-visible; the v72 structural class — the
    // rendered chrome is the axis, never the DOM shape).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toMatchObject({
      fv: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      opacity: "1",
      outlineStyle: "none",
      boxShadow: "none",
    });

    // THE FOCUSED RUNG — a REAL keyboard walk to the X (the v134 form:
    // programmatic .focus() on a BUTTON does not engage :focus-visible; a
    // REAL Tab does). The walk is FINDER-BOUNDED and REQUIRES
    // :focus-visible to match: the clone's Radix auto-focus (fv false)
    // must not satisfy the landing check — the walk presses on until the
    // X receives focus VIA THE KEYBOARD (the census measured 4 stops).
    for (let i = 0; i < 30; i++) {
      await page.keyboard.press("Tab");
      await page.waitForTimeout(120);
      const landed = await xBtn.evaluate(
        (el) => document.activeElement === el && el.matches(":focus-visible"),
      );
      if (landed) break;
    }
    await expect(xBtn).toBeFocused();
    await page.waitForTimeout(450); // the transition settle
    const focusedRead = await readState();
    expect(focusedRead).toMatchObject({
      focused: true,
      fv: true,
      bg: "rgba(0, 0, 0, 0)", // focus != hover — no tint on the focus path
      color: "rgb(10, 10, 10)",
      opacity: "1",
    });
    // THE repaired axes — THE never-pinned ring (the 1px #0a0a0a focus
    // family, the shadcn focus base) + the outline form (the v32
    // zb-row-action family: the transparent outline, offset 2px). The
    // VISIBLE ring asserted via toContain (the lead-slot construct
    // deliberately not pinned — the v37 S1/v95 family discipline).
    const ring = await xBtn.evaluate((el) => getComputedStyle(el).boxShadow);
    expect(ring).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");
    const outline = await xBtn.evaluate((el) => {
      const cs = getComputedStyle(el);
      return {
        style: cs.outlineStyle,
        width: cs.outlineWidth,
        color: cs.outlineColor,
        offset: cs.outlineOffset,
      };
    });
    expect(outline).toEqual({
      style: "solid",
      width: "2px",
      color: "rgba(0, 0, 0, 0)", // transparent — the v32 zb-row-action form
      offset: "2px",
    });

    // The restore rung — blur: the at-rest contract re-established.
    await xBtn.evaluate((el) => (el as HTMLElement).blur());
    await page.waitForTimeout(450);
    const blurred = await readState();
    expect(blurred).toMatchObject({
      fv: false,
      bg: "rgba(0, 0, 0, 0)",
      outlineStyle: "none",
      boxShadow: "none",
    });
  });
});
'''

text += BLOCK
io.open(SPEC, "w", encoding="utf-8").write(text)
print(f"appended the v135 describe block to {SPEC} (+{BLOCK.count(chr(10))} lines)")
