#!/usr/bin/env python3
"""Append the v132 describe block (the networth asset-card type badge's
own-hover ladder at 390x844) to tests/e2e/networth.spec.ts — the PIN-ONLY
cycle's pin (the plan docs/remediation-plan-v132.md F4).

The form mirrors the v127 item-card badge pin (items.spec.ts) adapted to
the networth surface + the mobile viewport: the STRUCTURAL tag-agnostic
finder (the white rounded dollar card, then the label-set leaf with the
radius-6px/fs-12px chrome guards — the reference's badge is a DIV, the
clone's a SPAN, the v107 lesson); the ladder parks the REAL pointer at
(5,5) FIRST (the v22 lesson), reads the at-rest rung, moves the REAL
pointer to the badge's LIVE-READ center (two-arg mouse move — the v123
lesson), reads the own-hovered rung, parks back, reads the restored rung.
The V94-COLLISION-safe axis set: the end-states alone ({hoverMatch, bg});
the transition metadata (the v95 documented class) and the label-dependent
w/h deliberately NOT pinned."""
import io

SPEC = "tests/e2e/networth.spec.ts"
MARKER = "// v132 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v132 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v132 — plan F4 (docs/remediation-plan-v132.md): the NETWORTH ASSET-CARD
// TYPE BADGE's OWN-HOVER ladder at MOBILE 390x844 (the cycle's own surface
// — the mobile /networth twin). The never-pinned HOVER PATH of the pinned
// networth badge family: the v29 G1 pins hold the zb-badge-hover CLASS
// TOKEN + the AT-REST computed bg/color (networth.spec.ts:193-198 the
// asset badge, :229-234 the liability badge); the v127 pin holds the
// ITEM-CARD badge's hover end-state (item-card.tsx — a DIFFERENT file
// with a DIFFERENT at-rest family [rgb(248,250,252) vs this file's
// rgb(243,244,246)]); the v130 pin the SAME CARD's kebab trigger (a
// different component). The hovered tint — globals.css's
// .zb-badge-hover:hover { background-color: rgba(245,245,245,0.8) }, the
// reference's own measured value (the v28 G1 family) — held on THIS FILE
// by NO spec at ANY viewport. Measured BYTE-IDENTICAL on BOTH sides by
// the one-shot census badgehover-arbit-v132.sh (the "Bank Account"
// same-label target: at-rest bg rgb(243,244,246) -> the hovered
// rgba(245,245,245,0.8) -> the restored at-rest, the color
// rgb(55,65,81)/w 115/h 22/transitionDuration 0.15s identical, the
// hoverMatch ladder false->true->false; the transitionProperty computed
// form differs by construction — the v95 transition-property documented
// class — and is deliberately NOT asserted; the w/h label-dependent axes
// deliberately NOT pinned). READ-ONLY per the v46 rule: the badge's only
// behavior is the tint — no click path exists on either site's badge.
// ---------------------------------------------------------------------------
test.describe("networth asset-card badge own-hover ladder at 390 (v132 — plan F4)", () => {
  test("the first asset card's type badge — the at-rest bg, the hovered rgba(245,245,245,0.8) tint, the restore (the never-pinned hover path on the networth file)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/networth");
    // the settle pattern: wait for the seeded asset card before interacting
    // (the mobile view's first card = the Share Portfolio investment card).
    await expect(page.getByText("Share Portfolio").first()).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the v107 tag-agnostic lesson): the first white
    // rounded dollar card, then its TYPE-BADGE leaf — the label-set text
    // with the radius-6px/fs-12px chrome guards (state-independent).
    const TYPE_LABELS = ["Bank Account", "Superannuation", "Property", "Investment", "Vehicle", "Other"];
    const readState = () =>
      page.evaluate((labels: string[]) => {
        const cards = [...document.querySelectorAll("div")].filter((d) => {
          const cs = getComputedStyle(d);
          const r = d.getBoundingClientRect();
          return cs.backgroundColor === "rgb(255, 255, 255)" && r.width > 150 && r.width < 500
            && r.height > 80 && r.height < 300 && cs.borderRadius !== "0px"
            && (d.textContent || "").includes("$");
        });
        if (!cards.length) return null;
        const card = cards[0];
        card.scrollIntoView({ block: "center" });
        const badge = [...card.querySelectorAll("span, div")].find((s) => {
          const t = (s.textContent || "").trim();
          if (!labels.includes(t) || s.children.length !== 0) return false;
          const cs = getComputedStyle(s);
          return cs.borderRadius === "6px" && cs.fontSize === "12px";
        });
        if (!badge) return null;
        const cs = getComputedStyle(badge);
        return {
          hoverMatch: badge.matches(":hover"),
          bg: cs.backgroundColor,
        };
      }, TYPE_LABELS);

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the networth badge family's hex-pinned
    // #f3f4f6 at-rest bg, the contrast the hover axis needs.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).toEqual({ hoverMatch: false, bg: "rgb(243, 244, 246)" });

    // THE HOVER END-STATE — the REAL pointer on the badge's OWN live-read
    // center (never guessed; page.mouse.move takes x y as TWO args — the
    // v123 lesson; the same coords-read-live form as the census): the
    // zb-badge-hover:hover tint rgba(245,245,245,0.8), THE never-pinned
    // axis on this file.
    const center = await page.evaluate((labels: string[]) => {
      const cards = [...document.querySelectorAll("div")].filter((d) => {
        const cs = getComputedStyle(d);
        const r = d.getBoundingClientRect();
        return cs.backgroundColor === "rgb(255, 255, 255)" && r.width > 150 && r.width < 500
          && r.height > 80 && r.height < 300 && cs.borderRadius !== "0px"
          && (d.textContent || "").includes("$");
      });
      if (!cards.length) return null;
      const card = cards[0];
      card.scrollIntoView({ block: "center" });
      const badge = [...card.querySelectorAll("span, div")].find((s) => {
        const t = (s.textContent || "").trim();
        if (!labels.includes(t) || s.children.length !== 0) return false;
        const cs = getComputedStyle(s);
        return cs.borderRadius === "6px" && cs.fontSize === "12px";
      });
      if (!badge) return null;
      const r = badge.getBoundingClientRect();
      return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
    }, TYPE_LABELS);
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
    expect(restored).toEqual({ hoverMatch: false, bg: "rgb(243, 244, 246)" });
  });
});
'''

io.open(SPEC, "w", encoding="utf-8").write(text + BLOCK)
print("appended the v132 describe block to", SPEC)
