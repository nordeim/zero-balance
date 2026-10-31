#!/usr/bin/env python3
"""Append the v136 describe block (the networth asset-card kebab trigger's
focus-visible ladder at 1280x800) to tests/e2e/networth.spec.ts — the
PIN-ONLY cycle's pin (the plan docs/remediation-plan-v136.md F4).

The form mirrors the v130 pin's own card finder (the Share Portfolio h4 ->
the rounded-xl card -> the ONLY small square button — the file's
established structural family, tag-agnostic per the v107 lesson; the
trigger is UNLABELLED on the reference, and the pin must survive data
changes, so the aria-label is never the finder) + the v134/v135 pins'
REAL keyboard walk: the ladder parks the REAL pointer at (5,5) FIRST (the
v22 lesson), reads the at-rest rung, walks the REAL Tabs to the trigger
(FINDER-BOUNDED at 40 stops, NEVER Enter — the menu opens on click/Enter,
both out of bounds, and the net-worth kebab flow is NEVER safe to probe
past the menu open: the menu's Delete click IS the delete, the v124
rule), reads the focused rung (the keyboard-reveal superset opacity + THE
1px #0a0a0a ring via toContain + the outline-none contract), blurs, reads
the restored rung. The walk's landing check requires :focus-visible to
match (the v135 lesson — programmatic focus must not satisfy it). The
V94-COLLISION-safe axis set: the end-states alone; the transition
metadata + the lead-slot construct deliberately NOT pinned."""
import io

SPEC = "tests/e2e/networth.spec.ts"
MARKER = "// v136 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v136 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v136 — plan F4 (docs/remediation-plan-v136.md): the NETWORTH ASSET-CARD
// KEBAB-TRIGGER's FOCUS-VISIBLE LADDER at 1280 (the cycle's own surface —
// the /networth view, the v130-era NETWORTH + drill-down pair's TWELFTH
// re-run). The never-pinned KEYBOARD path of the pinned reveal family on
// this file: the v46 F2 pin the AT-REST opacity-0 + the CARD-hover
// group-hover reveal (640/390); the v124 pin the OPEN+parked state at
// 1280; the v130 pin the OWN-HOVER tint ladder at 1280; the v132 pin the
// BADGE own-hover at 390; the v36 S3 pin the keyboard reveal on /INCOME —
// a DIFFERENT FILE (item-card.tsx:139, {fv, opacity} alone, never the
// ring); the v134 pin the focus ladder on /savings (item-card.tsx again —
// the different-file immunity precedent). The networth twins
// (net-worth-view.tsx:82 asset + :192 liability — the identical class
// string carrying focus-visible:outline-none focus-visible:ring-1
// focus-visible:ring-ring focus-visible:opacity-100) held by NO spec at
// ANY viewport on this file before this pin.
//
// The both-sides one-shot census (focusnw-arbit-v136.sh) measured the
// ladder CLEAN: the visible focused chrome — the 1px #0a0a0a ring —
// IDENTICAL both sides (both walks landed after exactly 9 Tabs); the
// deltas the documented classes (the clone's keyboard-reveal opacity-1
// SUPERSET [the reference's trigger stays invisible under keyboard
// focus]; the TW v4 5-slot boxShadow construct vs the reference's 3-slot
// [the 0-width leads inert, the v37 S1/v95 class]; the reference's
// transparent 2px outline vs the clone's outline-none [both visually
// inert]). NO GAP, NO REPAIR — a PIN-ONLY cycle.
// ---------------------------------------------------------------------------
test.describe("networth asset-card kebab-trigger focus-visible ladder at 1280 (v136 — plan F4)", () => {
  test("the Share Portfolio card's trigger — the at-rest state, the REAL-Tab focused reveal + the 1px ring, the restore (the never-pinned keyboard path on the networth file)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    // the settle pattern: the seeded first asset card (the v106/v124/v130
    // pin's own card) before any interaction.
    const card = page.locator("div.rounded-xl").filter({ hasText: "Share Portfolio" }).first();
    await expect(card).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the v130 pin's own family, tag-agnostic per the
    // v107 lesson): the Share Portfolio h4 -> the rounded-xl card -> the
    // ONLY small square button (w <= 50 && h <= 50 — the 36x36 kebab
    // trigger; the networth asset card renders no other button).
    const readState = () =>
      page.evaluate(() => {
        const h4 = [...document.querySelectorAll("h4")].find((x) =>
          /Share Portfolio/i.test((x.textContent || "").trim()),
        );
        if (!h4) return null;
        const trigger =
          (h4.closest("div.rounded-xl") as HTMLElement | null) ?? h4.parentElement;
        if (!trigger) return null;
        const btn = [...trigger.querySelectorAll("button")].find((b) => {
          const r = b.getBoundingClientRect();
          return r.width <= 50 && r.height <= 50;
        });
        if (!btn) return null;
        const cs = getComputedStyle(btn);
        const isFocused = document.activeElement === btn;
        return {
          focused: isFocused,
          fv: isFocused ? btn.matches(":focus-visible") : false,
          opacity: cs.opacity,
          bg: cs.backgroundColor,
          boxShadow: cs.boxShadow,
          outlineStyle: cs.outlineStyle,
        };
      });

    // The landing probe: a PLAIN boolean (the v134 lesson — immune to the
    // bash-quoted-JSON escaping; inside Playwright the direct boolean
    // suffices).
    const landed = () =>
      page.evaluate(() => {
        const h4 = [...document.querySelectorAll("h4")].find((x) =>
          /Share Portfolio/i.test((x.textContent || "").trim()),
        );
        if (!h4) return false;
        const trigger =
          (h4.closest("div.rounded-xl") as HTMLElement | null) ?? h4.parentElement;
        if (!trigger) return false;
        const btn = [...trigger.querySelectorAll("button")].find((b) => {
          const r = b.getBoundingClientRect();
          return r.width <= 50 && r.height <= 50;
        });
        return !!btn && document.activeElement === btn;
      });

    // The at-rest rung — the REAL pointer parked at (5,5) FIRST (the v22
    // lesson): the trigger invisible (opacity 0), no tint, no ring.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const atRest = await readState();
    expect(atRest).toMatchObject({
      focused: false,
      fv: false,
      opacity: "0",
      bg: "rgba(0, 0, 0, 0)",
      boxShadow: "none",
      outlineStyle: "none",
    });

    // The REAL keyboard walk — FINDER-BOUNDED at 40 stops, NEVER Enter
    // (the menu opens on click/Enter, both out of bounds — the v124
    // rule). The landing requires the ACTIVE element to BE the trigger.
    let stops = 0;
    for (let i = 1; i <= 40; i++) {
      await page.keyboard.press("Tab");
      stops = i;
      if (await landed()) break;
    }
    expect(await landed(), `the walk must land on the trigger (stopped after ${stops} Tabs)`).toBe(true);

    // The focused rung — the keyboard-reveal SUPERSET (opacity 1 — the
    // clone's focus-visible:opacity-100; the reference's own trigger
    // stays invisible under keyboard focus) + THE 1px #0a0a0a ring (the
    // focus family's visible chrome — via toContain, immune to the lead-
    // slot construct) + the outline-none contract (the ring replaces the
    // outline) + NO tint (focus != hover — the accent tint is :hover
    // only).
    const focused = await readState();
    expect(focused).toMatchObject({
      focused: true,
      fv: true,
      opacity: "1",
      bg: "rgba(0, 0, 0, 0)",
      outlineStyle: "none",
    });
    expect(focused!.boxShadow).toContain("rgb(10, 10, 10) 0px 0px 0px 1px");

    // The blurred rung — the at-rest contract re-established.
    await page.evaluate(() => (document.activeElement as HTMLElement | null)?.blur());
    await page.waitForTimeout(450);
    const blurred = await readState();
    expect(blurred).toMatchObject({
      focused: false,
      fv: false,
      opacity: "0",
      bg: "rgba(0, 0, 0, 0)",
      boxShadow: "none",
      outlineStyle: "none",
    });
  });
});
'''

text += BLOCK
io.open(SPEC, "w", encoding="utf-8").write(text)
print(f"appended the v136 describe block to {SPEC} (+{BLOCK.count(chr(10))} lines)")
