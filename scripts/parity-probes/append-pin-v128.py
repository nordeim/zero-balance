#!/usr/bin/env python3
"""Append the v128 describe block to tests/e2e/items.spec.ts (the
line-append form — the v112 dashboard.spec + v120 networth + v121/v127
items precedents: the file is ~4.9k lines, the Edit old_str is unwieldy;
the block appended at EOF)."""

BLOCK = r'''

// ---------------------------------------------------------------------------
// v128 — plan F4 (docs/remediation-plan-v128.md): the SAVINGS GOAL-CARD
// KEBAB-TRIGGER's OWN-HOVER END-STATE census at 1280 (the pair's OWN
// surface — the /savings view). The never-pinned TINT PATH of the pinned
// reveal family: the v45 F1a pin holds the trigger's w/h/at-rest opacity
// (on /income, the shared component); the v116 pin holds the at-rest box
// chrome + the CARD-hover reveal ladder (the group-hover opacity path —
// the pointer on the CARD's center, the own-hover tint never engaged);
// the v36 pin the keyboard path; the v122 pin the OPEN+parked state; the
// v98 pin the menu panel; the dialog-buttons v27 G1 pin holds the
// hover:bg-accent CLASS TOKEN on the DIALOG X — a DIFFERENT element in a
// different file. The trigger's OWN hover end-state — the hover:bg-accent
// TINT (item-card.tsx:139, the file's sole occurrence) + the
// hover:text-accent-foreground COLOR + the simultaneous group-hover
// reveal — held by NO spec at ANY viewport. Measured BYTE-IDENTICAL on
// BOTH sides by the one-shot census kebabhover-arbit-v128.sh (the
// hover-ladder form — READ-ONLY per the v46 rule: login + passive
// navigation + a REAL pointer hover only; the menu opens on CLICK, the
// hover alone never opens it — the v125 QA-hover / v127 badge-hover
// precedent): the at-rest {opacity 0, bg transparent, color
// rgb(10,10,10)} -> the OWN-HOVERED {opacity 1, bg rgb(245,245,245),
// color rgb(23,23,23)} -> the restored at-rest, the hoverMatch +
// cardHover ladders false->true->false, the w/h/radius + transition
// metadata identical (both sites' transition-opacity compiles to the
// single-property list — no v3/v4 computed-form difference on this
// element; the metadata axes recorded in the census, NOT pinned — the
// v95 family discipline, and the w/h/radius held by the v122 open-state
// pin: the V94-COLLISION criterion keeps this spec the SOLE failure
// surface for the tint-family mutation).
// ---------------------------------------------------------------------------
test.describe("savings goal-card kebab-trigger own-hover end-state census at 1280 (v128 — plan F4)", () => {
  test("the Emergency Fund card's trigger own-hover ladder — the at-rest state, the hovered accent tint + accent-foreground color, the restore (the never-pinned tint path)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/savings");
    // the settle pattern: wait for the seeded subtitle before interacting
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the v46 F3 family, tag-agnostic per the v107
    // lesson): the Emergency Fund h4 -> the rounded-xl card -> the ONLY
    // small square button (w <= 50 && h <= 50 — the 36x36 kebab trigger;
    // the savings cards render NO action row [item.type === "expense"
    // only], so the trigger is the card's sole small button).
    const readState = () =>
      page.evaluate(() => {
        const h4 = [...document.querySelectorAll("h4")].find((x) =>
          /Emergency Fund/i.test((x.textContent || "").trim()),
        );
        if (!h4) return null;
        const card =
          (h4.closest("div.rounded-xl") as HTMLElement | null) ?? h4.parentElement;
        if (!card) return null;
        const trigger = [...card.querySelectorAll("button")].find((b) => {
          const r = b.getBoundingClientRect();
          return r.width <= 50 && r.height <= 50;
        });
        if (!trigger) return null;
        const cs = getComputedStyle(trigger);
        return {
          hoverMatch: trigger.matches(":hover"),
          cardHover: card.matches(":hover"),
          opacity: cs.opacity,
          bg: cs.backgroundColor,
          color: cs.color,
        };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the trigger invisible (opacity 0, bg
    // transparent), the contrast the tint axes need.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({
      hoverMatch: false,
      cardHover: false,
      opacity: "0",
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
    });

    // THE OWN-HOVER END-STATE — the REAL pointer at the trigger's OWN
    // live-read center (never guessed — the coords read after the
    // scrollIntoView; page.mouse.move takes x y as TWO args — the v123
    // lesson; the same coords-read-live form as the census): the
    // group-hover reveal (the trigger sits INSIDE the card) + THE
    // never-pinned axes — the hover:bg-accent tint rgb(245,245,245) and
    // the hover:text-accent-foreground color rgb(23,23,23).
    const center = await page.evaluate(() => {
      const h4 = [...document.querySelectorAll("h4")].find((x) =>
        /Emergency Fund/i.test((x.textContent || "").trim()),
      );
      if (!h4) return null;
      const card =
        (h4.closest("div.rounded-xl") as HTMLElement | null) ?? h4.parentElement;
      if (!card) return null;
      const trigger = [...card.querySelectorAll("button")].find((b) => {
        const r = b.getBoundingClientRect();
        return r.width <= 50 && r.height <= 50;
      });
      if (!trigger) return null;
      trigger.scrollIntoView({ block: "center" });
      return new Promise<{ x: number; y: number } | null>((resolve) => {
        setTimeout(() => {
          const r = trigger.getBoundingClientRect();
          resolve({ x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) });
        }, 300);
      });
    });
    expect(center).not.toBeNull();
    await page.mouse.move(center!.x, center!.y);
    await page.waitForTimeout(400); // the transition-opacity 150ms settle
    const hovered = await readState();
    expect(hovered).toEqual({
      hoverMatch: true,
      cardHover: true,
      opacity: "1",
      bg: "rgb(245, 245, 245)",
      color: "rgb(23, 23, 23)",
    });

    // The restore rung — the pointer re-parked at (5,5): the tint
    // disengaged, the reveal retired, the at-rest contract
    // re-established.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual({
      hoverMatch: false,
      cardHover: false,
      opacity: "0",
      bg: "rgba(0, 0, 0, 0)",
      color: "rgb(10, 10, 10)",
    });
  });
});
'''

PATH = "tests/e2e/items.spec.ts"
with open(PATH, "r", encoding="utf-8") as f:
    text = f.read()

# guard: never append twice
if "v128 — plan F4" in text:
    raise SystemExit("the v128 block already present — refusing to append twice")

if not text.endswith("\n"):
    text += "\n"
text += BLOCK.lstrip("\n")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(text)

lines = text.count("\n") + 1
print(f"appended the v128 describe block -> {PATH} ({lines} lines)")
