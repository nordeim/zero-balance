#!/usr/bin/env python3
"""Append the v122 describe block to tests/e2e/items.spec.ts (the
line-append form — the v112 dashboard.spec precedent + the v120/v121
items.spec precedents: the file is ~4.8k lines, the Edit old_str is
unwieldy; the block appended at EOF)."""

BLOCK = r'''

// ---------------------------------------------------------------------------
// v122 — plan F4 (docs/remediation-plan-v122.md): the SAVINGS goal-card
// kebab-trigger's OPEN-MENU reveal census at 1280 — the never-pinned PATH
// of the pinned reveal family (the v116 pin holds the HOVER path; the v36
// S3 pin the KEYBOARD path; the OPEN path — data-[state=open]:opacity-100,
// superset fix #7's "stays revealed while its menu is open" clause — held
// by NO spec: the v98 pin opens the menu but censuses the PANEL + the
// menuitem interior only). The CLONE-ONLY form (the v46 F3 adapted
// precedent): the reference's trigger stays INVISIBLE (opacity 0) when
// its menu is opened (its own superset-#7 bug), and a reference-side
// measurement would require a CLICK (the v46 read-only rule) — the pin
// locks the CLONE's own superset chrome. The family chrome = the v116
// pinned contract BY CONSTRUCTION (the identical class string:
// item-card.tsx:139).
// The pin's world is the REAL-Event world (the one-shot census's
// synthetic-pointer artifacts documented in the plan): the REAL pointer
// parks at (5,5) — the group-hover path disengaged — and the
// data-[state=open] token ALONE must hold the reveal.
// ---------------------------------------------------------------------------
test.describe("savings goal-card kebab-trigger OPEN-MENU reveal census at 1280 (v122 — plan F4)", () => {
  test("the trigger's open+parked reveal — the data-[state=open] path holds opacity 1 with the pointer off the card (superset #7's stays-revealed clause)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    // the settle pattern: the seeded Emergency Fund card (the census's
    // own card — the 309x230 savings goal card).
    const card = page.locator("div.rounded-xl").filter({ hasText: "Emergency Fund" }).first();
    await expect(card).toBeVisible();
    const trigger = card.getByRole("button", { name: "Actions for Emergency Fund" });

    // Park the REAL pointer off-card, then read the at-rest baseline (the
    // v45/v116 contract: opacity 0, data-state closed — the ladder's
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
    // THE AXIS + the unchanged box chrome (the v116 pinned family
    // contract — the reveal costs no geometry).
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

path = "tests/e2e/items.spec.ts"
text = open(path, encoding="utf-8").read()
if "kebab-trigger OPEN-MENU reveal census at 1280 (v122" in text:
    raise SystemExit("the v122 block already present — refusing to append twice")
open(path, "a", encoding="utf-8").write(BLOCK)
print(f"appended the v122 describe block to {path}")
