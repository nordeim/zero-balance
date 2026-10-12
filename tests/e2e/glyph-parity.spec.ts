import { expect, test, type Page } from "@playwright/test";

// v55 F1 (docs/remediation-plan-v55.md): the ICON-GLYPH parity census.
// The full glyph audit (24 lucide glyphs across the five views + the
// login page, measured live on BOTH sites via glyph-audit-v55.sh +
// glyph-diff-v55.mjs) found lucide-react 0.525 REDESIGNED four glyphs
// the reference still renders in its older lucide geometry: piggy-bank
// (the savings family's every surface — the nav rail link, the stat
// rows, the donut legend, the quick actions, the classification chips),
// trending-up (the reference renders the OLD two-POLYLINE glyph — the
// redesign turned it into paths), search (the handle 4.3 vs 4.34), and
// mail (the login email input's envelope flap). The v44 chevron-swap
// family: parity is the SHAPE DATA, not just the computed chrome — a
// computed-style census cannot see a glyph swap; read the svg's shapes.
//
// The already-identical glyphs the audit measured byte-parity on get
// pin-locked here too: calendar (the goal card's date span), heart +
// circle-alert (the /expenses classification chips — the same-glyph
// control census), repeat (the clone-only Recurring badge — the
// superset's own chrome), lock, and the receipt/legend families.
//
// This spec ran RED first (the lucide-react 0.525 glyphs FAIL the shape
// assertions), then GREEN via src/components/ui/legacy-icons.tsx (the
// reference's exact svg markup — path/polyline/rect/circle children
// byte-identical, the class prefix kept for the svg.lucide-* selectors).

// The reference's exact shape children (measured live — glyph-exact-v55.sh).
const PIGGY = [
  "P:M19 5c-1.5 0-2.8 1.4-3 2-3.5-1.5-11-.3-11 5 0 1.8 0 3 2 4.5V20h4v-2h3v2h4v-4c1-.5 1.7-1 2-2h2v-4h-2c0-1-.5-1.5-1-2V5z",
  "P:M2 9v1c0 1.1.9 2 2 2h1",
  "P:M16 11h.01",
];
const TRENDING = [
  "PL:22 7 13.5 15.5 8.5 10.5 2 17",
  "PL:16 7 22 7 22 13",
];
const SEARCH = ["C:11,11,r8", "P:m21 21-4.3-4.3"];
const MAIL = [
  "R:2,4,20x16,rx2",
  "P:m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7",
];
const CALENDAR = [
  "P:M8 2v4",
  "P:M16 2v4",
  "R:3,4,18x18,rx2",
  "P:M3 10h18",
];
const REPEAT = [
  "P:m17 2 4 4-4 4",
  "P:M3 11v-1a4 4 0 0 1 4-4h14",
  "P:m7 22-4-4 4-4",
  "P:M21 13v1a4 4 0 0 1-4 4H3",
];
const HEART = [
  "P:M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z",
];
const CIRCLE_ALERT = [
  "C:12,12,r10",
  "L:12,8,12,12",
  "L:12,16,12.01,16",
];
const LOCK = [
  "R:3,11,18x11,rx2",
  "P:M7 11V7a5 5 0 0 1 10 0v4",
];

/** Read every shape child of every svg carrying the lucide class. */
const readGlyphs = (page: Page, lucideClass: string) =>
  page.locator(`svg.${lucideClass}`).evaluateAll((nodes) =>
    nodes.map((n) => {
      const shapes = [
        ...n.querySelectorAll("path,circle,rect,line,polyline,polygon"),
      ];
      return shapes.map((s) => {
        const tag = s.tagName.toLowerCase();
        if (tag === "path") return `P:${s.getAttribute("d") ?? ""}`;
        if (tag === "circle")
          return `C:${s.getAttribute("cx")},${s.getAttribute("cy")},r${s.getAttribute("r")}`;
        if (tag === "polyline" || tag === "polygon")
          return `${tag === "polyline" ? "PL" : "PG"}:${s.getAttribute("points") ?? ""}`;
        if (tag === "rect")
          return `R:${s.getAttribute("x")},${s.getAttribute("y")},${s.getAttribute("width")}x${s.getAttribute("height")},rx${s.getAttribute("rx")}`;
        return `L:${s.getAttribute("x1")},${s.getAttribute("y1")},${s.getAttribute("x2")},${s.getAttribute("y2")}`;
      });
    }),
  );

/** The svg's base attrs (viewBox + stroke family — shared by every lucide). */
const readBaseAttrs = (page: Page, lucideClass: string) =>
  page.locator(`svg.${lucideClass}`).first().evaluate((el) => ({
    viewBox: el.getAttribute("viewBox"),
    fill: el.getAttribute("fill"),
    stroke: el.getAttribute("stroke"),
    sw: el.getAttribute("stroke-width"),
    slc: el.getAttribute("stroke-linecap"),
    slj: el.getAttribute("stroke-linejoin"),
  }));

test.describe("goal-card glyph census at 390 (v55 — plan F1)", () => {
  test("the classification chip's piggy + the date-span calendar + the Recurring repeat (v55 F1)", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/savings");
    await expect(page.getByText("2 items · $1250.00")).toBeVisible();

    const census = await page.evaluate(() => {
      // The goal card: the Emergency Fund h4's rounded-xl ancestor in
      // the grid (the v51/v54 walk).
      const h4 = [...document.querySelectorAll("h4")].find((x) =>
        /Emergency Fund/i.test((x.textContent || "").trim()),
      );
      if (!h4) return null;
      let card: HTMLElement | null =
        (h4.closest("div.rounded-xl") as HTMLElement | null) ?? h4.parentElement;
      for (let i = 0; card && i < 5; i++) {
        const cs = getComputedStyle(card!.parentElement!);
        if (cs.display === "grid") break;
        card = card!.parentElement as HTMLElement;
      }
      if (!card) return null;
      // The badge row (the v54 finder — the chips compute to "flex",
      // blockified flex items).
      const badgeRow = [...card.querySelectorAll("div")].find((d) => {
        const cs = getComputedStyle(d);
        return (
          cs.display === "flex" &&
          cs.flexWrap === "wrap" &&
          d.children.length >= 2 &&
          [...d.children].every(
            (c) => getComputedStyle(c as HTMLElement).display === "flex",
          )
        );
      }) as HTMLElement | null;
      if (!badgeRow) return null;
      const chipGlyph = (text: string) => {
        const chip = [...badgeRow.children].find(
          (c) => (c.textContent || "").trim().toLowerCase() === text,
        ) as HTMLElement | undefined;
        if (!chip) return null;
        const svg = chip.querySelector("svg");
        if (!svg) return null;
        const shapes = [
          ...svg.querySelectorAll("path,circle,rect,line,polyline,polygon"),
        ].map((s) => {
          const tag = s.tagName.toLowerCase();
          if (tag === "path") return `P:${s.getAttribute("d") ?? ""}`;
          if (tag === "circle")
            return `C:${s.getAttribute("cx")},${s.getAttribute("cy")},r${s.getAttribute("r")}`;
          if (tag === "rect")
            return `R:${s.getAttribute("x")},${s.getAttribute("y")},${s.getAttribute("width")}x${s.getAttribute("height")},rx${s.getAttribute("rx")}`;
          return `L:${s.getAttribute("x1")},${s.getAttribute("y1")},${s.getAttribute("x2")},${s.getAttribute("y2")}`;
        });
        const r = svg.getBoundingClientRect();
        return {
          cls: (svg.getAttribute("class") || "").slice(0, 40),
          shapes,
          w: Math.round(r.width),
          h: Math.round(r.height),
          color: getComputedStyle(svg).color,
          mr: getComputedStyle(svg).marginRight,
          chipColor: getComputedStyle(chip).color,
        };
      };
      // The footer: the LAST justify-between direct child WITHOUT an
      // h4 (the v54 footer-locator lesson).
      const footer = [...card.children]
        .filter((d) => {
          const cs = getComputedStyle(d as HTMLElement);
          return (
            cs.display === "flex" &&
            cs.justifyContent === "space-between" &&
            !d.querySelector("h4")
          );
        })
        .pop() as HTMLElement | undefined;
      const dateSpan = footer?.children[0] as HTMLElement | undefined;
      const dateSvg = dateSpan?.querySelector("svg") ?? null;
      const dateGlyph = dateSvg
        ? {
            shapes: [...dateSvg.querySelectorAll("path,rect,circle,line")].map(
              (s) => {
                const tag = s.tagName.toLowerCase();
                if (tag === "path") return `P:${s.getAttribute("d") ?? ""}`;
                if (tag === "rect")
                  return `R:${s.getAttribute("x")},${s.getAttribute("y")},${s.getAttribute("width")}x${s.getAttribute("height")},rx${s.getAttribute("rx")}`;
                return `L:${s.getAttribute("x1")},${s.getAttribute("y1")},${s.getAttribute("x2")},${s.getAttribute("y2")}`;
              },
            ),
            w: Math.round(dateSvg.getBoundingClientRect().width),
            color: getComputedStyle(dateSvg).color,
          }
        : null;
      return {
        savings: chipGlyph("savings"),
        recurring: chipGlyph("recurring"),
        date: dateGlyph,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The classification chip's icon: the reference's OLD piggy glyph.
    expect(census!.savings!.cls).toContain("lucide-piggy-bank");
    expect(census!.savings!.shapes).toEqual(PIGGY);
    expect(census!.savings!.w).toBe(12);
    expect(census!.savings!.h).toBe(12);
    expect(census!.savings!.mr).toBe("4px");
    // The icon inherits the chip's savings green (currentColor).
    expect(census!.savings!.color).toBe("rgb(21, 128, 61)");
    expect(census!.savings!.chipColor).toBe("rgb(21, 128, 61)");

    // The Recurring chip (the clone-only superset badge): the repeat
    // glyph at the same chrome (12×12, mr 4, the chip green).
    expect(census!.recurring!.cls).toContain("lucide-repeat");
    expect(census!.recurring!.shapes).toEqual(REPEAT);
    expect(census!.recurring!.w).toBe(12);
    expect(census!.recurring!.mr).toBe("4px");

    // The date span's calendar glyph: byte-parity on both sites (the
    // audit's identical set — 3 paths + the 18×18 rx-2 rect).
    expect(census!.date!.shapes).toEqual(CALENDAR);
    expect(census!.date!.w).toBe(12);
    expect(census!.date!.color).toBe("rgb(107, 114, 128)");

    // The savings page fits the mobile viewport (the superset fix).
    expect(census!.docSW).toBe(390);
  });
});

test.describe("dashboard + networth glyph census (v55 — plan F1)", () => {
  test("every piggy-bank and trending-up svg carries the reference's old glyphs (v55 F1)", async ({ page }) => {
    await page.goto("/");
    await expect(page.getByText("+$2065.00")).toBeVisible();

    // EVERY piggy surface on the dashboard (the nav rail's Savings link,
    // the Total-Savings stat row, the donut legend's Savings row, the
    // quick-actions' Add Savings) renders the OLD 3-path glyph — the
    // reference's every piggy svg measured the same shape data
    // (piggy-sweep-v55.sh).
    const piggies = await readGlyphs(page, "lucide-piggy-bank");
    expect(piggies.length).toBeGreaterThanOrEqual(3);
    for (const shapes of piggies) expect(shapes).toEqual(PIGGY);

    // EVERY trending-up surface (the nav rail's Net Worth link, the
    // Total-Income stat row, the breakdown's net row) renders the OLD
    // two-POLYLINE glyph — the redesign turned it into paths.
    const trendings = await readGlyphs(page, "lucide-trending-up");
    expect(trendings.length).toBeGreaterThanOrEqual(3);
    for (const shapes of trendings) expect(shapes).toEqual(TRENDING);

    // The donut legend's circle-alert + heart glyphs (the audit's
    // identical set — pin-locked).
    const alerts = await readGlyphs(page, "lucide-circle-alert");
    expect(alerts.length).toBeGreaterThanOrEqual(1);
    for (const shapes of alerts) expect(shapes).toEqual(CIRCLE_ALERT);
    const hearts = await readGlyphs(page, "lucide-heart");
    expect(hearts.length).toBeGreaterThanOrEqual(1);
    for (const shapes of hearts) expect(shapes).toEqual(HEART);

    // The base attrs (every lucide svg — measured on both sites):
    // viewBox 0 0 24 24, fill none, stroke currentColor, sw 2, round
    // caps/joins.
    const base = await readBaseAttrs(page, "lucide-piggy-bank");
    expect(base.viewBox).toBe("0 0 24 24");
    expect(base.fill).toBe("none");
    expect(base.stroke).toBe("currentColor");
    expect(base.sw).toBe("2");
    expect(base.slc).toBe("round");
    expect(base.slj).toBe("round");
  });

  test("the networth hero + summary trend icons carry the old glyph (v55 F1)", async ({ page }) => {
    await page.goto("/networth");
    await expect(page.getByText("Total Net Worth")).toBeVisible();

    const trendings = await readGlyphs(page, "lucide-trending-up");
    expect(trendings.length).toBeGreaterThanOrEqual(2);
    for (const shapes of trendings) expect(shapes).toEqual(TRENDING);
  });
});

test.describe("items-view search glyph census (v55 — plan F1)", () => {
  test("the search input's icon carries the reference's old handle (v55 F1)", async ({ page }) => {
    await page.goto("/income");
    await expect(page.getByText("2 items · $5550.00")).toBeVisible();

    const searches = await readGlyphs(page, "lucide-search");
    expect(searches.length).toBeGreaterThanOrEqual(1);
    for (const shapes of searches) expect(shapes).toEqual(SEARCH);
  });
});

test.describe("expenses classification glyph census (v55 — plan F1)", () => {
  test("the want heart + the need circle-alert glyphs (the same-glyph control, v55 F1)", async ({ page }) => {
    await page.goto("/expenses");
    await expect(page.getByText("3 items · $2235.00")).toBeVisible();

    // The audit's same-glyph control: the reference's Netflix (want)
    // and its Miscellaneous/Rent (need) chips measured byte-identical
    // to the clone's — the redesigned glyphs were ONLY piggy/trending/
    // search/mail. Pin the heart + circle-alert shape data.
    const hearts = await readGlyphs(page, "lucide-heart");
    expect(hearts.length).toBeGreaterThanOrEqual(1);
    for (const shapes of hearts) expect(shapes).toEqual(HEART);

    const alerts = await readGlyphs(page, "lucide-circle-alert");
    expect(alerts.length).toBeGreaterThanOrEqual(2);
    for (const shapes of alerts) expect(shapes).toEqual(CIRCLE_ALERT);
  });
});

// The login-page glyphs: logged-out surface (the auth.spec.ts pattern).
test.describe("login mail glyph census (v55 — plan F1)", () => {
  test.use({ storageState: { cookies: [], origins: [] } });

  test("the email input's mail icon carries the reference's old envelope (v55 F1)", async ({ page }) => {
    await page.goto("/login");
    await expect(
      page.getByRole("heading", { name: "Welcome to ZeroBudget" }),
    ).toBeVisible();

    // The mail glyph: the OLD rect + flap (the redesign re-tuned the
    // flap's arc — a1.94 1.94 vs a2 2).
    const mails = await readGlyphs(page, "lucide-mail");
    expect(mails.length).toBeGreaterThanOrEqual(1);
    for (const shapes of mails) expect(shapes).toEqual(MAIL);

    // The lock glyph (the audit's identical set — pin-locked).
    const locks = await readGlyphs(page, "lucide-lock");
    expect(locks.length).toBeGreaterThanOrEqual(1);
    for (const shapes of locks) expect(shapes).toEqual(LOCK);
  });
});
