#!/usr/bin/env python3
"""append-pin-v126.py — append the v126 pin (the Spending Breakdown DONUT'S
GEOMETRY census at 390) to tests/e2e/dashboard.spec.ts as the v126 describe
block, following the v125 pin's own append form. The axes are the one-shot
census's measured values (donut-arbit-v126.sh, measured cleanly on both
sides on the FIRST run): the card {w 358, h 656} + the wrap {w 308, h 300,
relative} + the svg {w 308, h 300} + the pie circle {200x200, r 100,
centered in the svg at 154/150} + the sectorCount 3 settle guard — the
rendered diameter/centering byte-identical on both sites (the width family
the documented DASH width-guard class alone: the reference's own 395px
overflow)."""
import sys

PIN = '''
test.describe("Spending Breakdown donut geometry census at 390 (v126 — plan F4)", () => {
  test("the donut's rendered geometry — the card/wrap/svg boxes + the pie circle's bbox/center/radius (the never-pinned family at any viewport)", async ({ page }) => {
    // The v126 F4 pin: the mobile twin #2's own surface — the Spending
    // Breakdown DONUT'S RENDERED GEOMETRY, held by NO spec at ANY
    // viewport before this pin (the coverage map, read per the
    // SPEC-ALIAS lesson: the v9/v14 pins hold the donut's DATA order +
    // the hover tooltip's sector FILL; the v31 pin the keyboard
    // semantics; the v44 F3 + v49 pins the LEGEND at 1280/390; the v76
    // pin the LABEL CHROME at 1280 [count/fs/lineCount — never the
    // geometry]; the v101 pin the CARD BOX + header at 1280 — the 390
    // header twin rejected as the collision). The both-sides census
    // (donut-arbit-v126.sh): the pie circle 200x200 / r 100
    // byte-identical both sides; the card/wrap/svg heights identical;
    // the width family the documented width-guard class alone (the
    // reference's own 395px overflow vs the clone's fitting 390).
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/dashboard");
    // The settle pattern (the v42 idiom: the card title is a plain div,
    // never a role=heading) + the seeded net-balance text.
    await expect(page.getByText("Spending Breakdown")).toBeVisible();
    await expect(page.getByText("+$2065.00")).toBeVisible();
    await page.waitForTimeout(600);

    const census = await page.evaluate(() => {
      // The card finder — the v78 radius/white walk from the text leaf,
      // TAG-AGNOSTIC (the title is a plain div on both sites).
      const title = [...document.querySelectorAll("div, h1, h2, h3, h4, span, p")].find(
        (e) => (e.textContent || "").trim() === "Spending Breakdown" && e.children.length === 0,
      );
      if (!title) return null;
      let card = title as HTMLElement;
      for (let i = 0; i < 8; i++) {
        card = card.parentElement as HTMLElement | null;
        if (!card) break;
        const cs = getComputedStyle(card);
        if ((cs.borderRadius && cs.borderRadius !== "0px") || cs.backgroundColor === "rgb(255, 255, 255)") break;
      }
      if (!card) return null;
      const cr = card.getBoundingClientRect();
      const svg = card.querySelector("svg.recharts-surface, svg") as SVGSVGElement | null;
      if (!svg) return null;
      const wrap = svg.parentElement as HTMLElement;
      const wr = wrap.getBoundingClientRect();
      const wcs = getComputedStyle(wrap);
      const sr = svg.getBoundingClientRect();
      const sectors = [...card.querySelectorAll(".recharts-pie-sector path, path.recharts-pie-sector")];
      if (!sectors.length) return null;
      // The pie circle — the UNION BBOX of the sector paths (the
      // rendered diameter/center, never the svg's outer box); the
      // center recomputed RELATIVE TO THE SVG (the v107 local-geometry
      // discipline — never the absolute page position).
      let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
      for (const p of sectors) {
        const r = p.getBoundingClientRect();
        x0 = Math.min(x0, r.x); y0 = Math.min(y0, r.y);
        x1 = Math.max(x1, r.x + r.width); y1 = Math.max(y1, r.y + r.height);
      }
      const bbW = Math.round(x1 - x0);
      const bbH = Math.round(y1 - y0);
      return {
        docSW: document.documentElement.scrollWidth,
        card: { w: Math.round(cr.width), h: Math.round(cr.height) },
        wrap: { w: Math.round(wr.width), h: Math.round(wr.height), pos: wcs.position },
        svg: { w: Math.round(sr.width), h: Math.round(sr.height) },
        pieCircle: {
          w: bbW,
          h: bbH,
          r: Math.round(bbW / 2),
          cxInSvg: Math.round(x0 + bbW / 2 - sr.x),
          cyInSvg: Math.round(y0 + bbH / 2 - sr.y),
        },
        sectorCount: sectors.length,
      };
    });
    expect(census, "the donut census finder (the text leaf -> the radius/white walk)").not.toBeNull();
    if (!census) throw new Error("donut census found no card/svg/sectors");

    // The docSW guard — the clone FITS at 390 (the reference's own 395px
    // overflow the documented width-guard class, the superset invariant).
    expect(census.docSW).toBe(390);

    // The CARD BOX — the 390 width axis (358 = 390 - 2*16 wrapper pad)
    // + the full height (the header + the fixed 300 donut + the legend
    // stack + the p-6 paddings, the seeded 3-slice state).
    expect(census.card).toEqual({ w: 358, h: 656 });

    // The DONUT WRAPPER — the fixed-height ResponsiveContainer box (the
    // width:100% style riding the card's content width; the height the
    // literal 300; the relative position the keyboard-parity anchor).
    expect(census.wrap).toEqual({ w: 308, h: 300, pos: "relative" });

    // The SVG — the recharts surface filling the wrapper exactly (the
    // ResponsiveContainer's fill contract at 390: 308x300).
    expect(census.svg).toEqual({ w: 308, h: 300 });

    // THE PIE CIRCLE — the rendered diameter (200 = outerRadius 100 x 2,
    // the reference's recharts 2.15 and the clone's 3.10 agreeing
    // byte-for-byte) + the CENTERED contract (cxInSvg = svg.w/2 = 154,
    // cyInSvg = svg.h/2 = 150 — the local-geometry discipline).
    expect(census.pieCircle).toEqual({ w: 200, h: 200, r: 100, cxInSvg: 154, cyInSvg: 150 });

    // The settle guard — the seeded 3-slice state (Need/Savings/Want all
    // non-zero). The labelCount/labelLineCount axes are NOT pinned here
    // (the v76 1280 collision discipline — the viewport-invariant count
    // tokens held by the v76 label-chrome pin).
    expect(census.sectorCount).toBe(3);
  });
});
'''

path = "tests/e2e/dashboard.spec.ts"
text = open(path, encoding="utf-8").read()
if "v126 — plan F4" in text:
    print("FAIL: the v126 pin already present")
    sys.exit(1)
if not text.endswith("\n"):
    text += "\n"
open(path, "w", encoding="utf-8").write(text + PIN.lstrip("\n"))
print(f"OK: appended the v126 pin ({len(PIN.lstrip(chr(10)).splitlines())} lines) to {path}")
