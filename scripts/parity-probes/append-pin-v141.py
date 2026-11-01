#!/usr/bin/env python3
"""Append the v141 describe block (the login sign-in submit's own-hover
ladder at 1280x800) to tests/e2e/login-parity.spec.ts — the PIN-ONLY
cycle's pin (the plan docs/remediation-plan-v141.md F4).

The form mirrors the v140 search-input pin (items.spec.ts) adapted to
the cycle's own login-pair surface (the /login view at 1280x800, the
file's own storageState opt-out — the logged-out surface) and the
ACTIVE-TINT ladder (the v129 form): the STRUCTURAL finder
(button[type=submit] with the "Sign in" text — the form shared by both
sites, the text cross-checked); the ladder parks the REAL pointer at
(5,5) FIRST (the v22 lesson), reads the at-rest rung (the v7-pinned
at-rest chrome), moves the REAL pointer to the submit's LIVE-READ center
(two-arg mouse move — the v123 lesson), reads the own-hovered rung (the
TINTED contract — bg rgb(15,23,42)->rgb(30,41,59) under the submit's own
hover with the color/shadow family unchanged), parks back, reads the
restored rung. The V94-COLLISION-safe axis set: the end-states alone
({hoverMatch, txt, bg, color, the shadow VISIBLE pair via toContain
[immune to the lead-slot construct]}); the geometry (w/h — held by the
v9 per-state pin) and the transition metadata (the v95 documented
class) deliberately NOT pinned. The submit is NEVER clicked — a mouse
MOVE only (a click would submit the form; the logged-out surface holds
no session, the census cannot mutate state)."""
import io

SPEC = "tests/e2e/login-parity.spec.ts"
MARKER = "// v141 — plan F4"

text = io.open(SPEC, encoding="utf-8").read()
if MARKER in text:
    raise SystemExit("the v141 block already present — refusing to double-append")
if not text.endswith("\n"):
    text += "\n"

BLOCK = '''
// ---------------------------------------------------------------------------
// v141 — plan F4 (docs/remediation-plan-v141.md): the LOGIN SIGN-IN
// SUBMIT's OWN-HOVER LADDER at 1280 (the cycle's own surface — the /login
// view, the v135-era LOGIN + CALCULATOR pair's THIRTEENTH re-run). The
// never-pinned HOVER path of the pinned submit family: the v7 pin holds
// the submit's REST chrome (bg #0f172a, color white, h 48); the v9 pin
// the per-state geometry (h 48/44, fs 14); the v25 pin the focus-visible
// ring family; the v45 F4 pin the REST shadow-sm; the v135 survey
// measured the own-hover tint live on the reference
// (rgb(15,23,42)->rgb(30,41,59)) and confirmed the clone's existing
// class (login-card.tsx hover:bg-[#1e293b]) matches — every submit
// census AT-REST or FOCUS, the submit's own-hover END-STATE held by NO
// spec at ANY viewport before this pin. THE CONSTRUCT: the TINTED
// contract (the v129 active-hover form) — the bg transitioning to
// rgb(30, 41, 59) under the submit's own hover with the color/shadow
// family unchanged — measured byte-identical on BOTH sides by
// submithover-arbit-v141.sh (the submit center REF (640,677) /
// CLONE (640,677); the construct deltas — the shadow LEAD-LAYER count
// [the v37 O1 note: the reference's v3 three-slot construct vs the
// clone's Tailwind v4 five-slot, every lead a 0px-spread shadow
// invisible by construction; the VISIBLE pair byte-identical] + the
// borderColor zero-width computed-color artifact [the card.border
// class — border-width 0px both sides, nothing renders] — the
// documented classes, never pinned; the transition metadata IDENTICAL
// both sides: all / 0.2s).
// ---------------------------------------------------------------------------
test.describe("login sign-in submit own-hover ladder at 1280 (v141 — plan F4)", () => {
  test("the sign-in submit's own-hover ladder — the at-rest chrome, the hovered TINTED contract (the #1e293b tint), the restore (the never-pinned hover path)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    await page.waitForTimeout(400);

    // STRUCTURAL finder (the form shared by both sites): the sign-in
    // submit — button[type=submit] carrying the "Sign in" text (the
    // text cross-checked in every rung's read). The state read: the
    // hover-ladder axis set (hoverMatch + txt + bg + color + the
    // shadow VISIBLE pair).
    const readState = () =>
      page.evaluate(() => {
        const submit = [...document.querySelectorAll("button[type=submit]")].find((b) =>
          /Sign in/i.test((b.textContent || "").trim()),
        ) as HTMLButtonElement | null;
        if (!submit) return null;
        const cs = getComputedStyle(submit);
        return {
          hoverMatch: submit.matches(":hover"),
          txt: (submit.textContent || "").trim().slice(0, 12),
          bg: cs.backgroundColor,
          color: cs.color,
          shadow: cs.boxShadow,
        };
      });

    // The live-read center of the submit (never guessed; the rect read
    // AFTER the scrollIntoView, inside the same evaluate — the v132 form).
    const readCenter = () =>
      page.evaluate(() => {
        const submit = [...document.querySelectorAll("button[type=submit]")].find((b) =>
          /Sign in/i.test((b.textContent || "").trim()),
        ) as HTMLButtonElement | null;
        if (!submit) return null;
        submit.scrollIntoView({ block: "center" });
        const r = submit.getBoundingClientRect();
        return { x: Math.round(r.x + r.width / 2), y: Math.round(r.y + r.height / 2) };
      });

    // The ladder's first rung — AT-REST with the REAL pointer parked at
    // (5,5) (the v22 lesson): the v7-pinned at-rest family's chrome
    // contract (the slate-900 bg + white text + the ambient shadow-sm
    // VISIBLE pair + the text cross-check).
    await page.mouse.move(5, 5);
    await page.waitForTimeout(300);
    const atRest = await readState();
    expect(atRest).not.toBeNull();
    expect(atRest).toMatchObject({
      hoverMatch: false,
      txt: "Sign in",
      bg: "rgb(15, 23, 42)",
      color: "rgb(255, 255, 255)",
    });
    expect(atRest!.shadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // THE OWN-HOVERED rung — the REAL pointer at the submit's own
    // live-read center (a mouse MOVE only, NEVER a click — a click
    // would submit the form): the TINTED contract — the bg transitioning
    // to the reference's slate-800 #1e293b under the submit's own hover
    // with the color/shadow family UNCHANGED (the v129 active-hover
    // form).
    const center = await readCenter();
    expect(center).not.toBeNull();
    await page.mouse.move(center!.x, center!.y);
    await page.waitForTimeout(400);
    const hovered = await readState();
    expect(hovered).toMatchObject({
      hoverMatch: true,
      txt: "Sign in",
      bg: "rgb(30, 41, 59)", // THE TINT — slate-800 #1e293b
      color: "rgb(255, 255, 255)", // UNCHANGED — white text persists
    });
    expect(hovered!.shadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px"); // UNCHANGED

    // The restore rung — the pointer re-parked at (5,5): the at-rest
    // contract re-established, byte-identical to the first rung.
    await page.mouse.move(5, 5);
    await page.waitForTimeout(400);
    const restored = await readState();
    expect(restored).toEqual(atRest);
  });
});
'''

io.open(SPEC, "w", encoding="utf-8").write(text + BLOCK)
print("v141 pin appended to tests/e2e/login-parity.spec.ts")
