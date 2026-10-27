#!/usr/bin/env python3
"""append-pin-v124.py — append the v124 pin (the networth asset-card
kebab-trigger's OPEN-MENU reveal census at 1280) to tests/e2e/networth.spec.ts
as the v124 describe block, following the v122 pin's own form (the family
twin on the never-pinned networth file). The axes are the one-shot census's
measured values (kebabopen-arbit-v124.sh, measured cleanly on the first
run): the open+parked {opacity "1" / dataState "open" / w 36 / h 36 /
radius "6px" / bg transparent / color rgb(10,10,10) / cardTop 21 /
cardRight 21} with the at-rest baseline {opacity "0" / "closed"} and the
REAL-Escape fixture-restore."""
import sys

PIN = '''
test.describe("networth kebab-trigger OPEN-MENU reveal census at 1280 (v124 — plan F4)", () => {
  test("the trigger's open+parked reveal — the data-[state=open] path holds opacity 1 with the pointer off the card (the reveal family's open path on the never-pinned networth file)", async ({ page }) => {
    // The v124 F4 pin: the kebab reveal family's OPEN path on the NETWORTH
    // twins (net-worth-view.tsx:82 asset + :192 liability) — held by NO
    // spec before this pin. The coverage map (read per the SPEC-ALIAS
    // lesson against the specs' own assertions): the v46 F2 census holds
    // the networth kebab's AT-REST opacity-0 + the REAL-HOVER group-hover
    // reveal; the v36 S3 census the KEYBOARD focus-visible reveal; the
    // v122 pin the OPEN path on the SAVINGS item-card (item-card.tsx:139
    // — a DIFFERENT FILE whose pin-sanity mutation left these networth
    // twins green, the different-file immunity proven live in the v122
    // cycle). The CLONE-ONLY form (the v46 F3 adapted precedent + the
    // v122 twin): the reference's trigger stays INVISIBLE when its menu
    // is opened (its own superset-#7 bug), and a reference-side
    // measurement would require a CLICK on the reference's net-worth
    // kebab (the v46 read-only rule — and the net-worth kebab flow is
    // NEVER safe to probe past the menu open: the menu's Delete click IS
    // the delete). The family chrome = the v122 pinned contract BY
    // CONSTRUCTION (the identical class string, net-worth-view.tsx:82/192
    // <-> item-card.tsx:139).
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    // The settle pattern: the seeded Share Portfolio asset card (the v106
    // pin's own card — the first networth asset).
    const card = page.locator("div.rounded-xl").filter({ hasText: "Share Portfolio" }).first();
    await expect(card).toBeVisible();
    // STRUCTURAL finder (the v72 discipline + the v122 pin's own live-red
    // discovery): the aria-label CSS form, NOT getByRole — while the menu
    // is OPEN Radix marks the app aria-hidden (the modal layer), which
    // EXCLUDES the trigger from the accessibility tree and makes the
    // role-name locator unresolvable mid-open.
    const trigger = card.locator('button[aria-label="Actions for Share Portfolio"]');

    // Park the REAL pointer off-card, then read the at-rest baseline (the
    // v45/v46 contract: opacity 0, data-state closed — the ladder's
    // first rung, establishing the contrast the axis needs).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await trigger.evaluate((el) => ({
      opacity: getComputedStyle(el).opacity,
      state: el.getAttribute("data-state"),
    }));
    expect(atRest).toEqual({ opacity: "0", state: "closed" });

    // The native click opens the Radix menu (Playwright's locator click
    // IS the full pointer sequence — the v46 lesson), then the REAL
    // pointer parks at (5,5): the group-hover path disengages and the
    // focus path is unengaged (Radix holds focus in the menu content) —
    // the open-state token must ALONE hold the reveal (THE AXIS).
    await card.hover();
    await trigger.click();
    const menu = page.getByRole("menu");
    await expect(menu).toBeVisible();
    await expect(menu.getByRole("menuitem")).toHaveCount(2);
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400); // the transition-opacity settle
    const census = await trigger.evaluate((el) => {
      const cs = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      const host = el.closest("div.rounded-xl") as HTMLElement | null;
      const cr = host ? host.getBoundingClientRect() : null;
      return {
        opacity: cs.opacity,
        state: el.getAttribute("data-state"),
        w: Math.round(r.width),
        h: Math.round(r.height),
        radius: cs.borderRadius,
        bg: cs.backgroundColor,
        color: cs.color,
        cardTop: cr ? Math.round(r.top - cr.top) : null,
        cardRight: cr ? Math.round(cr.right - r.right) : null,
      };
    });
    // THE AXIS + the unchanged box chrome (the v46/v116/v122 pinned
    // family contract — the reveal costs no geometry; the insets 21/21 =
    // the p-5 20px + the 1px border).
    expect(census).toEqual({
      opacity: "1",
      state: "open",
      w: 36,
      h: 36,
      radius: "6px",
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
      cardTop: 21,
      cardRight: 21,
    });

    // The fixture-restore: the REAL Escape press dismisses the menu (the
    // v98 form; no menuitem ever clicked — the data never touched).
    await page.keyboard.press("Escape");
    await expect(menu).not.toBeVisible();
    const closed = await trigger.evaluate((el) => el.getAttribute("data-state"));
    expect(closed).toBe("closed");
  });
});
'''

path = "tests/e2e/networth.spec.ts"
text = open(path, encoding="utf-8").read()
if "v124 — plan F4" in text:
    print("FAIL: the v124 pin already present")
    sys.exit(1)
if not text.endswith("\n"):
    text += "\n"
open(path, "w", encoding="utf-8").write(text + PIN.lstrip("\n"))
print(f"OK: appended the v124 pin ({len(PIN.lstrip(chr(10)).splitlines())} lines) to {path}")
