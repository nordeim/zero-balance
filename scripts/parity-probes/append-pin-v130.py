#!/usr/bin/env python3
"""Append the v130 describe block to tests/e2e/networth.spec.ts (the
line-append form — the v112 dashboard.spec + v120/v124 networth + v128
items precedents: the file is ~3.5k lines, the Edit old_str is unwieldy;
the block appended at EOF)."""

BLOCK = r'''

// ---------------------------------------------------------------------------
// v130 — plan F4 (docs/remediation-plan-v130.md): the NETWORTH ASSET-CARD
// KEBAB-TRIGGER's OWN-HOVER END-STATE census at 1280 (the pair's OWN
// surface — the /networth view). The never-pinned TINT PATH of the pinned
// reveal family on the never-pinned networth file: the v46 F2 pin holds
// the trigger's w/h/at-rest opacity + the CARD-hover reveal ladder (the
// group-hover opacity path — the pointer on the CARD's center, the
// own-hover tint never engaged); the v36 S3 pin the keyboard path; the
// v124 pin the OPEN+parked state (the open state's full box chrome
// w/h/radius held there); the v128 pin the SAME own-hover ladder on the
// SAVINGS item-card kebab (item-card.tsx:139 — a DIFFERENT FILE); the v98
// pin the menu panel; the dialog-buttons v27 G1 pin holds the
// hover:bg-accent CLASS TOKEN on the DIALOG X — a DIFFERENT element in a
// different file. The trigger's OWN hover end-state — the hover:bg-accent
// TINT (net-worth-view.tsx:82 the asset twin + :192 the liability twin,
// the identical class string) + the hover:text-accent-foreground COLOR +
// the simultaneous group-hover reveal — held by NO spec at ANY viewport
// on this file. Measured BYTE-IDENTICAL on BOTH sides by the one-shot
// census kebabhover-arbit-v130.sh (the hover-ladder form — READ-ONLY per
// the v46 rule: login + passive navigation + a REAL pointer hover only;
// the hover reveals chrome, it clicks nothing — the menu opens on CLICK,
// the hover alone never opens it — the v125 QA-hover / v127 badge-hover /
// v128 kebab-hover precedent; the net-worth kebab flow is NEVER safe to
// probe past the menu open: the menu's Delete click IS the delete — the
// v124 pin's own note): the at-rest {opacity 0, bg transparent, color
// rgb(10,10,10)} -> the OWN-HOVERED {opacity 1, bg rgb(245,245,245),
// color rgb(23,23,23)} -> the restored at-rest, the hoverMatch +
// cardHover ladders false->true->false, the w/h/radius + transition
// metadata identical (both sites' transition-opacity compiles to the
// single-property list — no v3/v4 computed-form difference on this
// element; the metadata axes recorded in the census, NOT pinned — the
// v95 family discipline, and the w/h/radius held by the v124 open-state
// pin: the V94-COLLISION criterion keeps this spec the SOLE failure
// surface for the tint-family mutation).
// ---------------------------------------------------------------------------
test.describe("networth asset-card kebab-trigger own-hover end-state census at 1280 (v130 — plan F4)", () => {
  test("the Share Portfolio card's trigger own-hover ladder — the at-rest state, the hovered accent tint + accent-foreground color, the restore (the never-pinned tint path on the networth file)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/networth");
    // the settle pattern: the seeded first asset card (the v106/v124
    // pin's own card) before any interaction.
    const card = page.locator("div.rounded-xl").filter({ hasText: "Share Portfolio" }).first();
    await expect(card).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the v46 F3 family, tag-agnostic per the v107
    // lesson): the Share Portfolio h4 -> the rounded-xl card -> the ONLY
    // small square button (w <= 50 && h <= 50 — the 36x36 kebab trigger;
    // the networth asset card renders no other button).
    const readState = () =>
      page.evaluate(() => {
        const h4 = [...document.querySelectorAll("h4")].find((x) =>
          /Share Portfolio/i.test((x.textContent || "").trim()),
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
        /Share Portfolio/i.test((x.textContent || "").trim()),
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

PATH = "tests/e2e/networth.spec.ts"
with open(PATH, "r", encoding="utf-8") as f:
    text = f.read()

# guard: never append twice
if "v130 — plan F4" in text:
    raise SystemExit("the v130 block already present — refusing to append twice")

if not text.endswith("\n"):
    text += "\n"
text += BLOCK.lstrip("\n")

with open(PATH, "w", encoding="utf-8") as f:
    f.write(text)

lines = text.count("\n") + 1
print(f"appended the v130 describe block -> {PATH} ({lines} lines)")
