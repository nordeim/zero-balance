#!/usr/bin/env python3
"""Append the v127 describe block to tests/e2e/items.spec.ts (the
line-append form — the v112 dashboard.spec + v120 networth + v121 items
precedents: the file is ~4.9k lines, the Edit old_str is unwieldy; the
block appended at EOF)."""

BLOCK = r'''

// ---------------------------------------------------------------------------
// v127 — plan F4 (docs/remediation-plan-v127.md): the ITEM-CARD BADGE's
// HOVER END-STATE census at 1280 (the pair's OWN first surface — the
// /income view). The never-pinned HOVER PATH of the pinned badge family:
// the v57 pin holds the badge ROW + badge0's AT-REST chrome; the v1-era
// + v28 G1/v29 G1 pins hold the zb-badge-hover CLASS TOKEN + the at-rest
// computed bg; the hovered tint — globals.css:421
// .zb-badge-hover:hover { background-color: rgba(245,245,245,0.8) } —
// held by NO spec at ANY viewport (every zb-badge-hover assertion in the
// suite is a class-token check or an at-rest read; the hovered value
// appears only in comments). Measured BYTE-IDENTICAL on BOTH sides by
// the one-shot census badgehover-arbit-v127.sh (the hover-ladder form —
// READ-ONLY per the v46 rule: login + passive navigation + a REAL
// pointer hover only, the v125 QA-hover precedent): the at-rest bg
// rgb(248,250,252) -> the hovered rgba(245,245,245,0.8) -> the restored
// at-rest, the color/w/h/duration identical, the hoverMatch ladder
// false->true->false. The transitionProperty computed form differs by
// construction (the reference's TW v3 shorter list vs the clone's v4
// extended list — the v95 transition-property documented class) and is
// deliberately NOT asserted.
// ---------------------------------------------------------------------------
test.describe("item-card badge hover end-state census at 1280 (v127 — plan F4)", () => {
  test("the income card's active-badge hover ladder — the at-rest bg, the hovered rgba(245,245,245,0.8) tint, the restore (the never-pinned hover path)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/income");
    // the settle pattern: wait for the seeded card before interacting
    await expect(page.getByText("Salary").first()).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the v46 F3 family, tag-agnostic per the v107
    // lesson): the "active" text LEAF in the grid's first card — the
    // status badge (the clone's bg-[#f8fafc] member of the badge row).
    const readState = () =>
      page.evaluate(() => {
        const grid = [...document.querySelectorAll("div")].find(
          (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
        );
        if (!grid) return null;
        const card = grid.children[0] as HTMLElement | null;
        if (!card) return null;
        const badge = [...card.querySelectorAll("span, div")].find((s) => {
          const t = (s.textContent || "").trim();
          return t === "active" && s.children.length === 0;
        });
        if (!badge) return null;
        const cs = getComputedStyle(badge);
        return {
          hoverMatch: badge.matches(":hover"),
          bg: cs.backgroundColor,
        };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the status badge's utility-class bg
    // rgb(248,250,252), the contrast the hover axis needs.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({ hoverMatch: false, bg: "rgb(248, 250, 252)" });

    // THE HOVER END-STATE — the REAL pointer on the badge's OWN live-read
    // center (never guessed; page.mouse.move takes x y as TWO args — the
    // v123 lesson; the same coords-read-live form as the census): the
    // zb-badge-hover:hover tint rgba(245,245,245,0.8), THE never-pinned
    // axis.
    const center = await page.evaluate(() => {
      const grid = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("grid-cols-3"),
      );
      if (!grid) return null;
      const card = grid.children[0] as HTMLElement | null;
      if (!card) return null;
      const badge = [...card.querySelectorAll("span, div")].find((s) => {
        const t = (s.textContent || "").trim();
        return t === "active" && s.children.length === 0;
      });
      if (!badge) return null;
      const r = badge.getBoundingClientRect();
      return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
    });
    expect(center).not.toBeNull();
    await page.mouse.move(center!.x, center!.y);
    await page.waitForTimeout(400); // the transition-colors 150ms settle
    const hovered = await readState();
    expect(hovered).toEqual({ hoverMatch: true, bg: "rgba(245, 245, 245, 0.8)" });

    // The restore rung — the pointer re-parked at (5,5): the tint
    // disengaged, the at-rest contract re-established.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual({ hoverMatch: false, bg: "rgb(248, 250, 252)" });
  });
});
'''

path = "tests/e2e/items.spec.ts"
text = open(path, encoding="utf-8").read()
if "item-card badge hover end-state census at 1280 (v127" in text:
    raise SystemExit("the v127 block already present — refusing to append twice")
open(path, "a", encoding="utf-8").write(BLOCK)
print(f"appended the v127 describe block to {path}")
