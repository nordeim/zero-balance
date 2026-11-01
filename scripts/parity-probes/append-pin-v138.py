#!/usr/bin/env python3
"""Append the v138 describe block (the NETWORTH TABLIST TRIGGER's
OWN-HOVER LADDER at mobile 390x844) to tests/e2e/networth.spec.ts — the
PIN-ONLY cycle's pin (the plan docs/remediation-plan-v138.md F4).

The form mirrors the v132 badge-hover pin's own ladder idiom (the same
file, the same 390 viewport): the REAL pointer parked at (5,5) FIRST (the
v22 lesson), the at-rest rung read, the REAL hover at each trigger's OWN
live-read center (never guessed; page.mouse.move takes x y as TWO args —
the v123 lesson), the hovered rung read, the pointer moved to the second
trigger, read, the pointer re-parked, the restored rung read. The
triggers are NEVER clicked — the Radix tabs activate on pointerdown (the
v120 lesson) and a mouse MOVE dispatches no pointerdown, so the ladder
can never flip the tab (the READ-ONLY rule).

THE CONTRACT BEING PINNED (measured byte-identical both sides by
tabhover-arbit-v138.sh): the trigger carries NO hover: utility
(tabs.tsx:24-38 — the focus-visible + data-[state=active] classes alone),
so the own-hover end-state is the INERT-HOVER contract — the at-rest
chrome PERSISTING under each trigger's own hover (the bg/color/shadow
unchanged across the ladder's rungs). The V94-COLLISION-safe axis set:
the hover rungs' end-states alone (hoverMatch + bg + color + the shadow
VISIBLE pair via toContain [immune to the lead-slot construct — the v53
pin's own accepted lead-divergence form] + iconColor); the border token
(the 0px-width preflight default — an invisible construct) and the
transition metadata deliberately NOT pinned — the v89 family's own form."""
import io

SPEC = "tests/e2e/networth.spec.ts"
MARKER = "// v138 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v138 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v138 — plan F4 (docs/remediation-plan-v138.md): the NETWORTH TABLIST
// TRIGGER's OWN-HOVER LADDER at mobile 390 (the cycle's own surface — the
// /networth view, the v132-era MOBILE-TWINS pair's TWELFTH re-run). The
// never-pinned HOVER path of the pinned tablist family: the v5 G3 pin the
// at-rest 2-col grid + the active green state; the v30 G2 the ROVING
// keyboard; the v50 F2 the full chrome at 640; the v53 F1 the full chrome
// at 390 — every tab census AT-REST, the trigger's own-hover END-STATE
// held by NO spec at ANY viewport before this pin. THE CONSTRUCT: the
// trigger carries NO hover: utility (tabs.tsx:24-38 — the focus-visible +
// data-[state=active] classes alone), so the own-hover end-state is the
// INERT-HOVER contract — the at-rest chrome persisting under each
// trigger's own hover — measured byte-identical on BOTH sides by
// tabhover-arbit-v138.sh (the Assets center REF (126,472) / CLONE
// (108,422), the Liabilities center REF (284,472) / CLONE (283,422); the
// construct deltas — the trigger WIDTH family [the reference's own
// 432-wide list inside its 464-overflow page, the v53-documented class],
// the shadow LEAD-LAYER count [the v66 invisible class], the 0px border
// token [the preflight default, renders nothing] — the documented
// classes, never pinned).
test.describe("networth tablist trigger own-hover ladder at 390 (v138 — plan F4)", () => {
  test("the Assets + Liabilities triggers' own-hover ladders — the at-rest chrome, the hovered INERT-HOVER contract (no tint on either trigger), the restore (the never-pinned hover path)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    await expect(page.getByRole("tab", { name: /Assets/i })).toBeVisible();
    await page.waitForTimeout(400);

    // ROLE-BASED finders (the v53 form — button[role=tab] + aria-selected,
    // shared by both Radix sites). The state read: the full hover-ladder
    // axis set per trigger (hoverMatch + bg + color + the full shadow
    // string + the icon's currentColor).
    const readState = () =>
      page.evaluate(() => {
        const triggers = [...document.querySelectorAll("button[role=tab]")];
        const active = triggers.find((t) => t.getAttribute("aria-selected") === "true");
        const inactive = triggers.find((t) => t.getAttribute("aria-selected") === "false");
        if (!active || !inactive) return null;
        const grab = (t: Element) => {
          const cs = getComputedStyle(t);
          const icon = t.querySelector("svg");
          return {
            hoverMatch: t.matches(":hover"),
            bg: cs.backgroundColor,
            color: cs.color,
            shadow: cs.boxShadow,
            iconColor: icon ? getComputedStyle(icon).color : null,
          };
        };
        return { active: grab(active), inactive: grab(inactive) };
      });

    // The live-read center of a trigger (never guessed; the rect read
    // AFTER the scrollIntoView, inside the same evaluate — the v132 form).
    const readCenter = (which: "active" | "inactive") =>
      page.evaluate((w: "active" | "inactive") => {
        const triggers = [...document.querySelectorAll("button[role=tab]")];
        const t = triggers.find((x) =>
          x.getAttribute("aria-selected") === (w === "active" ? "true" : "false"),
        );
        if (!t) return null;
        t.scrollIntoView({ block: "center" });
        const r = t.getBoundingClientRect();
        return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
      }, which);

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the v53-pinned at-rest contract, both
    // triggers (the green active pair + the muted inactive pair).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).not.toBeNull();
    expect(atRest!.active).toMatchObject({
      hoverMatch: false,
      bg: "rgb(220, 252, 231)",
      color: "rgb(20, 83, 45)",
      iconColor: "rgb(20, 83, 45)",
    });
    expect(atRest!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(atRest!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(atRest!.inactive).toMatchObject({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(115, 115, 115)",
      shadow: "none",
      iconColor: "rgb(115, 115, 115)",
    });

    // THE ACTIVE-HOVERED rung — the REAL pointer at the Assets trigger's
    // own live-read center (a mouse MOVE only, NEVER a click — the Radix
    // tabs activate on pointerdown, the v120 lesson): the INERT-HOVER
    // contract — the at-rest chrome PERSISTS under the trigger's own
    // hover (no tint on either site), the inactive twin untouched.
    const ac = await readCenter("active");
    expect(ac).not.toBeNull();
    await page.mouse.move(ac!.x, ac!.y);
    await page.waitForTimeout(400); // the transition-all 150ms settle
    const activeHovered = await readState();
    expect(activeHovered!.active).toMatchObject({
      hoverMatch: true,
      bg: "rgb(220, 252, 231)", // UNCHANGED — the inert-hover contract
      color: "rgb(20, 83, 45)",
      iconColor: "rgb(20, 83, 45)",
    });
    expect(activeHovered!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(activeHovered!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(activeHovered!.inactive).toMatchObject({
      hoverMatch: false,
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(115, 115, 115)",
      shadow: "none",
      iconColor: "rgb(115, 115, 115)",
    });

    // THE INACTIVE-HOVERED rung — the pointer at the Liabilities
    // trigger's own live-read center: the muted twin's own inert-hover
    // contract (transparent bg + muted color persisting, no tint), the
    // active twin back at rest.
    const ic = await readCenter("inactive");
    expect(ic).not.toBeNull();
    await page.mouse.move(ic!.x, ic!.y);
    await page.waitForTimeout(400);
    const inactiveHovered = await readState();
    expect(inactiveHovered!.active).toMatchObject({
      hoverMatch: false,
      bg: "rgb(220, 252, 231)",
      color: "rgb(20, 83, 45)",
      iconColor: "rgb(20, 83, 45)",
    });
    expect(inactiveHovered!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 3px 0px");
    expect(inactiveHovered!.active!.shadow).toContain("rgba(0, 0, 0, 0.1) 0px 1px 2px -1px");
    expect(inactiveHovered!.inactive).toMatchObject({
      hoverMatch: true,
      bg: "rgba(0, 0, 0, 0)", // UNCHANGED — the inert-hover contract
      color: "rgb(115, 115, 115)",
      shadow: "none",
      iconColor: "rgb(115, 115, 115)",
    });

    // The restore rung — the pointer re-parked at (5,5): both triggers'
    // at-rest contracts re-established, byte-identical to the first rung.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual(atRest);
  });
});
'''

text += BLOCK
io.open(SPEC, "w", encoding="utf-8").write(text)
print(f"appended the v138 describe block to {SPEC} (+{BLOCK.count(chr(10))} lines)")
