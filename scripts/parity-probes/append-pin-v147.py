#!/usr/bin/env python3
"""Append the v147 describe block (the login logo's own-hover ladder at
1280x800) to tests/e2e/login-parity.spec.ts — the PIN-ONLY cycle's pin
(the plan docs/remediation-plan-v147.md F4).

The form mirrors the v141 submit own-hover pin (the same file's own
prior ladder) adapted to the cycle's own candidate (the login logo — the
IDENTITY element, the first thing every user hovers): the STRUCTURAL
finder (img[alt*="logo"] -> the chip = img.parentElement, the group =
chip.parentElement, the halo = the group's first child — the form shared
by both sites, the alt cross-checked in every rung's read); the ladder
parks the REAL pointer at (5,5) FIRST (the v22 lesson), reads the
at-rest rung (the halo 0.3 + blur(24px) + the chip's shadow-lg VISIBLE
ambient pair via toContain [immune to the lead-slot construct, the v45
F4 form] + the geometry + the transition constants), moves the REAL
pointer to the logo group's LIVE-READ center (two-arg mouse move — the
v123 lesson), reads the own-hovered rung (the INTENSIFIED-HALO contract
— the halo opacity 0.3 -> 0.4 + the chip shadow-lg -> shadow-xl ambient
pair with the filter/geometry UNCHANGED), parks back, reads the restored
rung. The V7-G3/V75-COLLISION-safe axis set: the ring's color axes live
on a DIFFERENT element (.zb-logo-ring — the v7 G3 pin); the img's
geometry axes in a DIFFERENT test (the v75 F4 pin); the chip's shadow
asserted via toContain on the VISIBLE ambient pair alone (the lead-slot
construct never pinned — the v37 O1 discipline). The logo is NEVER
clicked — a mouse MOVE only (passive decoration, no handler; the
logged-out surface holds no session, the census cannot mutate state)."""
import io

SPEC = "tests/e2e/login-parity.spec.ts"
MARKER = "// v147 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v147 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v147 — plan F4 (docs/remediation-plan-v147.md): the LOGIN LOGO's
// OWN-HOVER LADDER at 1280 (the cycle's own surface — the /login view,
// the v141-era LOGIN + CALCULATOR pair's FOURTEENTH re-run). The
// never-pinned HOVER PATH of the login logo's decorative micro-interaction
// family: the v7 G3 pin holds the .zb-logo-ring 4px white/50 halo AT-REST
// (a DIFFERENT element — the ring layer); the v75 F4 pin the logo img's
// geometry AT-REST (96x96 + the alt); the v141 pin the submit's own-hover
// ladder (a DIFFERENT element — the submit button); the logo's own-hover
// END-STATE held by NO spec at ANY viewport before this pin (the
// suite-wide survey: every logo match at-rest chrome; auth.spec.ts's own
// comment records the span "keeps its shadow-lg / group-hover:shadow-xl"
// — the construct documented, never pinned). THE CONSTRUCT (the
// discovery-measured DOM, both sides): the logo group (div.group)
// carrying the BLUR HALO layer (opacity-30 blur-xl transition-opacity
// duration-300 group-hover:opacity-40 — login-card.tsx:56) + the CHIP
// span (shadow-lg transition-all duration-300 group-hover:shadow-xl —
// login-card.tsx:68) + the img (96x96). The own-hover end-state: the
// halo opacity 0.3 -> 0.4 + the chip shadow-lg -> shadow-xl with the
// filter/geometry/transition family UNCHANGED — measured byte-identical
// on BOTH sides by logohover-arbit-v147.sh (the logo center REF (640,123)
// / CLONE (640,123); the sole deltas the chip's at-rest INVISIBLE
// lead-layer construct [the reference's v3 form with the inline white/50
// ring vs the clone's TW v4 five-slot form + the separate .zb-logo-ring
// layer — the v7 G3 construct class, the visible ambient pair
// byte-identical, never pinned]). The logo is NEVER clicked — a mouse
// MOVE only (passive decoration, no handler; the logged-out surface
// holds no session).
// ---------------------------------------------------------------------------
test.describe("login logo own-hover ladder at 1280 (v147 — plan F4)", () => {
  test("the logo's own-hover ladder — the at-rest chrome, the hovered INTENSIFIED-HALO contract (opacity 0.4 + shadow-xl), the restore (the never-pinned hover path)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the form shared by both sites): the logo img
    // (the alt carries "logo") -> the chip = img.parentElement, the
    // group = chip.parentElement, the halo = the group's first child.
    // The state read: the hover-ladder axis set (groupHover + the alt
    // cross-check + the halo opacity/filter/transition + the chip's
    // shadow VISIBLE pair + the transition constant + the geometry).
    const readState = () =>
      page.evaluate(() => {
        const img = document.querySelector('img[alt*="logo" i]') as HTMLImageElement | null;
        if (!img) return null;
        const chip = img.parentElement as HTMLElement | null;
        const group = chip ? (chip.parentElement as HTMLElement | null) : null;
        if (!chip || !group) return null;
        const halo = group.children[0] as HTMLElement | null;
        if (!halo) return null;
        const hs = getComputedStyle(halo);
        const cs = getComputedStyle(chip);
        const r = chip.getBoundingClientRect();
        return {
          groupHover: group.matches(":hover"),
          imgAlt: (img.getAttribute("alt") || "").slice(0, 20),
          haloOpacity: hs.opacity,
          haloFilter: hs.filter,
          haloTransition: hs.transitionProperty + " " + hs.transitionDuration,
          chipShadow: cs.boxShadow,
          chipTransition: cs.transitionProperty + " " + cs.transitionDuration,
          chipW: Math.round(r.width),
          chipH: Math.round(r.height),
        };
      });

    // The live-read center of the logo group (never guessed; the rect
    // read AFTER the scrollIntoView, inside the same evaluate — the
    // v132 form).
    const readCenter = () =>
      page.evaluate(() => {
        const img = document.querySelector('img[alt*="logo" i]') as HTMLImageElement | null;
        if (!img) return null;
        const chip = img.parentElement as HTMLElement | null;
        const group = chip ? (chip.parentElement as HTMLElement | null) : null;
        if (!group) return null;
        group.scrollIntoView({ block: "center" });
        const r = group.getBoundingClientRect();
        return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the logo family's at-rest chrome (the halo
    // 0.3 + blur(24px) + the chip's shadow-lg VISIBLE ambient pair +
    // the geometry + the alt cross-check + the transition constants).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).not.toBeNull();
    expect(atRest).toMatchObject({
      groupHover: false,
      imgAlt: "ZeroBudget logo",
      haloOpacity: "0.3",
      haloFilter: "blur(24px)",
      haloTransition: "opacity 0.3s",
      chipTransition: "all 0.3s",
      chipW: 96,
      chipH: 96,
    });
    expect(atRest!.chipShadow).toContain("rgba(0, 0, 0, 0.1) 0px 10px 15px -3px"); // shadow-lg ambient lead
    expect(atRest!.chipShadow).toContain("rgba(0, 0, 0, 0.1) 0px 4px 6px -4px"); // shadow-lg ambient second

    // THE OWN-HOVERED rung — the REAL pointer at the logo group's own
    // live-read center (a mouse MOVE only, NEVER a click — passive
    // decoration, no handler): the INTENSIFIED-HALO contract — the halo
    // opacity 0.3 -> 0.4 + the chip shadow-lg -> shadow-xl ambient pair
    // with the filter/geometry UNCHANGED (the group-hover:opacity-40 +
    // group-hover:shadow-xl utilities — login-card.tsx:56/:68).
    const center = await readCenter();
    expect(center).not.toBeNull();
    await page.mouse.move(center!.x, center!.y);
    await page.waitForTimeout(400);
    const hovered = await readState();
    expect(hovered).toMatchObject({
      groupHover: true,
      imgAlt: "ZeroBudget logo",
      haloOpacity: "0.4", // THE INTENSIFIED HALO — group-hover:opacity-40
      haloFilter: "blur(24px)", // UNCHANGED — the blur radius never moves
      chipW: 96, // UNCHANGED — the geometry never moves
      chipH: 96, // UNCHANGED
    });
    expect(hovered!.chipShadow).toContain("rgba(0, 0, 0, 0.1) 0px 20px 25px -5px"); // shadow-xl ambient lead
    expect(hovered!.chipShadow).toContain("rgba(0, 0, 0, 0.1) 0px 8px 10px -6px"); // shadow-xl ambient second

    // The restore rung — the pointer re-parked at (5,5): the at-rest
    // contract re-established, byte-identical to the first rung.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual(atRest);
  });
});
'''

text += BLOCK
io.open(SPEC, "w", encoding="utf-8").write(text)
print(f"appended the v147 describe block to {SPEC} ({len(BLOCK.splitlines())} lines)")
