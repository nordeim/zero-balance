#!/usr/bin/env python3
"""Append the v148 describe block (the networth tablist trigger's
focus-visible ladder at 390x844 + the LIABILITIES-ACTIVE tablist chrome)
to tests/e2e/networth.spec.ts — the REPAIR + PIN cycle's pin (the plan
docs/remediation-plan-v148.md F4).

TEST A — the focus-visible ladder (the never-pinned KEYBOARD PATH of the
pinned tablist family; the v138/v144 forms combined): the ROLE finder
(button[role=tab] + aria-selected — the v53 form, shared by both Radix
sites); the ladder parks the REAL pointer at (5,5) FIRST (the v22
lesson), reads the at-rest rung (the v53 contract re-asserted: the
outline family none/3px/0px + the active's ambient pair via toContain +
the green pair chrome + the muted inactive twin), then the REAL Chromium
focus({focusVisible: true}) on the ACTIVE Assets trigger (the v35 S2
idiom — the trigger NEVER clicked; the ACTIVE trigger's focus activates
nothing under Radix's onFocus handler [onValueChange only when
!isSelected — the selected trigger's activation path dead], so the rung
is the CLEAN keyboard-entry state), reads the focused rung (fv true +
the v4 outline-none form none/1px/0px + the VISIBLE ring composite via
toContain [rgb(255,255,255) 0px 0px 0px 2px + rgb(10,10,10) 0px 0px 0px
4px — immune to the lead-slot construct, the v45 F4 form] + the ambient
pair + the chrome UNCHANGED — focus != hover), blurs, reads the restored
rung. The outlineColor axes deliberately NOT asserted (the v95 lab()
computed-form discipline). The V53/V138-COLLISION-safe axis set: the
at-rest chrome axes re-asserted in the same family form as the v138
pin's own at-rest rung; the focused axes on a state no other spec
touches at ANY viewport.

TEST B — the LIABILITIES-ACTIVE tablist chrome (the repair's regression
pin): the Liabilities tab CLICKED (Playwright's locator click — the v6
form, the full pointer sequence), the census re-queried post-flip: the
Liabilities trigger carries the reference's ORANGE active pair (bg
rgb(255, 237, 213) + color rgb(124, 45, 18) — #ffedd5/#7c2d12, the
polarity-coded family matching the liability card's own orange) + the
data-[state=active]:shadow ambient pair, the Assets twin the muted pair;
the Assets tab clicked back — the at-rest contract re-established. The
V53-COLLISION-safe form (v53 pins the at-rest states; this pin measures
the FLIPPED state — a state no other spec asserts)."""
import io

SPEC = "tests/e2e/networth.spec.ts"
MARKER = "// v148 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v148 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v148 — plan F4 (docs/remediation-plan-v148.md): the NETWORTH TABLIST
// TRIGGER's FOCUS-VISIBLE LADDER at mobile 390 + the LIABILITIES-ACTIVE
// tablist chrome (the cycle's REPAIR + PIN). The never-pinned KEYBOARD
// PATH of the pinned tablist family (the at-rest chrome pinned at
// 640/390 by v50/v53, the own-hover INERT ladder at 390 by v138, the
// roving arrow-key flip by v30 G2 — the focus-visible END-STATE held by
// NO spec at ANY viewport before this pin [the suite-wide survey: ZERO
// focus-visible/ring matches on the tablist across all 24 spec files]).
// THE CONSTRUCT (measured live on BOTH sides by tablistfocus-discovery-
// v148.sh): the trigger's focus-visible composite — the v4 outline-none
// form (outlineStyle none / width 1px / offset 0px — INVISIBLE) + the
// VISIBLE ring composite (rgb(255,255,255) 0px 0px 0px 2px [the white
// ring-offset] + rgb(10,10,10) 0px 0px 0px 4px [the 2px ring at the 2px
// offset] + the active trigger's ambient pair) with the chrome UNCHANGED
// (focus != hover). The reference's own focused outline reads the v3
// transparent form (solid/2px/2px rgba(0,0,0,0) — ENGAGED but INVISIBLE)
// — the documented v3-transparent-vs-v4-none construct class, never
// pinned; the visible ring composite byte-identical both sides.
//
// THE REPAIR (net-worth-view.tsx, the Liabilities TabsTrigger): the
// reference's per-tab POLARITY THEMING — Assets green / Liabilities
// orange (data-[state=active]:bg-orange-100 text-orange-900 on the
// reference; the computed pair rgb(255,237,213)/rgb(124,45,18)) — was
// LOST in the clone (both triggers the green pair). Surfaced by the
// discovery's inactive-focused rung (the Radix automatic-activation
// onFocus handler flips the tab on a bare focus of the inactive trigger)
// + confirmed by tablistfocus-followup-v148.sh (the deliberate pointer
// sequence). Never pinned/shot/asserted before (every tablist census
// measured the Assets-active default; the VLM shots never showed the
// Liabilities tab; the v30 flip test asserts selection + panel, not
// chrome). The repair adds the ORANGE active pair in the arbitrary-hex
// form (the v5 G3 oklch-drift lesson): data-[state=active]:bg-[#ffedd5]
// data-[state=active]:text-[#7c2d12]. The clone's inactive/at-rest
// states + the Assets path untouched (the cn() last-occurrence rule).
// ---------------------------------------------------------------------------
test.describe("networth tablist trigger focus-visible ladder at 390 (v148 — plan F4)", () => {
  test("the Assets trigger's focus-visible composite — the at-rest chrome, the focused v4 outline-none + the VISIBLE ring composite with the chrome UNCHANGED, the blur restore (the never-pinned keyboard path)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    // The settle pattern (the v138 idiom) + the seeded count line.
    await expect(page.getByRole("tab", { name: /Assets/i })).toBeVisible();
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    await page.waitForTimeout(400);

    // ROLE-BASED finders (the v53 form — button[role=tab] + aria-selected,
    // shared by both Radix sites). The state read: the full focus-ladder
    // axis set per trigger (the focused + :focus-visible flags + the
    // outline family + the full shadow string + the chrome + geometry).
    // The outlineColor axes deliberately NOT read here (the v95 lab()
    // computed-form discipline — never pinned).
    const readState = () =>
      page.evaluate(() => {
        const triggers = [...document.querySelectorAll("button[role=tab]")];
        const active = triggers.find((t) => t.getAttribute("aria-selected") === "true");
        const inactive = triggers.find((t) => t.getAttribute("aria-selected") === "false");
        if (!active || !inactive) return null;
        const grab = (t: Element) => {
          const cs = getComputedStyle(t);
          const r = t.getBoundingClientRect();
          return {
            focused: document.activeElement === t,
            fv: t.matches(":focus-visible"),
            outlineStyle: cs.outlineStyle,
            outlineWidth: cs.outlineWidth,
            outlineOffset: cs.outlineOffset,
            shadow: cs.boxShadow,
            bg: cs.backgroundColor,
            color: cs.color,
            h: Math.round(r.height),
          };
        };
        return { active: grab(active), inactive: grab(inactive) };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the v53-pinned at-rest contract, both
    // triggers (the green active pair + the muted inactive pair).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).not.toBeNull();
    expect(atRest!.active).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      bg: "rgb(220, 252, 231)",
      color: "rgb(20, 83, 45)",
      h: 28,
    });
    expect(atRest!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(atRest!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(atRest!.inactive).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(115, 115, 115)",
      shadow: "none",
      h: 28,
    });

    // THE FOCUSED RUNG — the REAL Chromium focus({focusVisible: true})
    // (the v35 S2 idiom — the REAL FocusOptions member; a programmatic
    // PLAIN focus never engages :focus-visible, the v25 lesson). The
    // ACTIVE Assets trigger is NEVER clicked (focus() dispatches no
    // click; the Radix onFocus activation path fires onValueChange only
    // when !isSelected — the selected trigger's path dead, so the rung is
    // the CLEAN keyboard-entry state). THE COMPOSITE engages: the v4
    // outline-none form (outlineStyle none / width 1px / offset 0px —
    // INVISIBLE, the documented v3-transparent-vs-v4-none construct
    // class; the reference's own engaged outline is 2px-transparent —
    // equally invisible) + the VISIBLE ring composite (the white 2px
    // ring-offset + the 10,10,10 4px ring — toContain, immune to the
    // lead-slot construct) over the ambient pair, while the trigger
    // chrome stays UNCHANGED — focus != hover. The 450ms settle (the
    // v136 discipline). The inactive twin the at-rest control.
    await page.evaluate(() => {
      const active = [...document.querySelectorAll("button[role=tab]")].find(
        (t) => t.getAttribute("aria-selected") === "true",
      );
      (active as HTMLElement).focus({ focusVisible: true } as unknown as FocusOptions);
    });
    await page.waitForTimeout(450);
    const focused = await readState();
    expect(focused).not.toBeNull();
    expect(focused!.active).toMatchObject({
      focused: true,
      fv: true,
      outlineStyle: "none",
      outlineWidth: "1px",
      outlineOffset: "0px",
      bg: atRest!.active!.bg, // UNCHANGED — focus != hover
      color: atRest!.active!.color, // UNCHANGED
      h: 28, // UNCHANGED — the geometry never moves
    });
    expect(focused!.active!.shadow).toContain("rgb(255, 255, 255) 0px 0px 0px 2px");
    expect(focused!.active!.shadow).toContain("rgb(10, 10, 10) 0px 0px 0px 4px");
    expect(focused!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(focused!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(focused!.inactive).toMatchObject({
      focused: false,
      fv: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(115, 115, 115)",
      shadow: "none",
    });

    // The blurred rung — the at-rest contract re-established on every
    // axis (the composite disengages; the chrome never moved).
    await page.evaluate(() => {
      const active = [...document.querySelectorAll("button[role=tab]")].find(
        (t) => t.getAttribute("aria-selected") === "true",
      );
      (active as HTMLElement).blur();
    });
    await page.waitForTimeout(450);
    const blurred = await readState();
    expect(blurred).not.toBeNull();
    expect(blurred!.active).toMatchObject({
      focused: false,
      fv: false,
      outlineStyle: "none",
      outlineWidth: "3px",
      outlineOffset: "0px",
      bg: atRest!.active!.bg,
      color: atRest!.active!.color,
      h: 28,
    });
    expect(blurred!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(blurred!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(blurred!.active!.shadow).not.toContain("rgb(255, 255, 255) 0px 0px 0px 2px");
    expect(blurred!.inactive).toMatchObject({
      fv: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(115, 115, 115)",
      shadow: "none",
    });
  });

  test("the LIABILITIES-ACTIVE tablist chrome — the reference's ORANGE active pair (the repair's regression pin), the muted Assets twin, the restore", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByRole("tab", { name: /Assets/i })).toBeVisible();
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    await page.waitForTimeout(400);

    // The census (the ROLE finder re-queried at each rung — the flip
    // re-marks aria-selected/data-state on both triggers).
    const readTabs = () =>
      page.evaluate(() => {
        const triggers = [...document.querySelectorAll("button[role=tab]")];
        const byTxt = (re: RegExp) =>
          triggers.find((t) => re.test((t.textContent || "").trim()));
        const assets = byTxt(/^Assets$/);
        const liab = byTxt(/^Liabilities$/);
        if (!assets || !liab) return null;
        const grab = (t: Element) => {
          const cs = getComputedStyle(t);
          return {
            sel: t.getAttribute("aria-selected"),
            state: t.getAttribute("data-state"),
            bg: cs.backgroundColor,
            color: cs.color,
            shadow: cs.boxShadow,
          };
        };
        return { assets: grab(assets), liabilities: grab(liab) };
      });

    // THE FLIP — the Liabilities tab CLICKED (the full pointer sequence —
    // the v6 form; the Radix tabs activate on pointerdown): the reference
    // color-codes the polarity — the Liabilities trigger's ACTIVE state
    // carries the ORANGE pair (rgb(255, 237, 213) / rgb(124, 45, 18) —
    // #ffedd5 / #7c2d12, the family matching the liability card's own
    // orange dot/value), the Assets twin the muted pair.
    await page.getByRole("tab", { name: "Liabilities" }).click();
    await expect(page.getByText("2 items · $311,250")).toBeVisible();
    await page.waitForTimeout(400);
    const flipped = await readTabs();
    expect(flipped).not.toBeNull();
    expect(flipped!.liabilities).toMatchObject({
      sel: "true",
      state: "active",
      bg: "rgb(255, 237, 213)", // THE ORANGE PAIR — the repair's own axis
      color: "rgb(124, 45, 18)",
    });
    expect(flipped!.liabilities!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(flipped!.liabilities!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(flipped!.assets).toMatchObject({
      sel: "false",
      state: "inactive",
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(115, 115, 115)",
      shadow: "none",
    });

    // THE RESTORE — the Assets tab clicked back: the at-rest contract
    // re-established (the green pair + the ambient pair on Assets, the
    // muted pair on the Liabilities twin).
    await page.getByRole("tab", { name: "Assets" }).click();
    await expect(page.getByText("3 items · $65,300")).toBeVisible();
    await page.waitForTimeout(400);
    const restored = await readTabs();
    expect(restored).not.toBeNull();
    expect(restored!.assets).toMatchObject({
      sel: "true",
      state: "active",
      bg: "rgb(220, 252, 231)",
      color: "rgb(20, 83, 45)",
    });
    expect(restored!.assets!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(restored!.assets!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(restored!.liabilities).toMatchObject({
      sel: "false",
      state: "inactive",
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(115, 115, 115)",
      shadow: "none",
    });
  });
});
'''

text += BLOCK
io.open(SPEC, "w", encoding="utf-8").write(text)
print(f"appended the v148 describe block to {SPEC} ({len(BLOCK.splitlines())} lines)")
