import { expect, test } from "@playwright/test";

// Custom 404 + document-head parity (session-13 audit,
// docs/remediation-plan-v7.md G7/G8). The reference ships a branded
// not-found page — h1 "404" (text-7xl font-light text-slate-300), a 2×64px
// slate-200 divider bar, h2 "Page Not Found" (text-2xl font-medium
// text-slate-800), the message 'The page "X" could not be found in this
// application.' with the quoted path in font-medium slate-700, and a white
// outline "Go Home" button → the dashboard. Its title is
// "Nonexistent Page Xyz | ZeroBudget" and its head carries the reference
// description, OG/Twitter cards, canonical, manifest and apple meta.
// This file OPTS OUT of the shared storageState (head assertions are
// session-independent; the 404 renders logged-out too).

test.use({ storageState: { cookies: [], origins: [] } });

test.describe("custom not-found page (v7 — plan G7)", () => {
  test("renders the reference 404 structure with the quoted path", async ({ page }) => {
    await page.goto("/nonexistent-page-xyz");
    await expect(page.getByRole("heading", { name: "404", exact: true })).toBeVisible();
    await expect(page.getByRole("heading", { name: "Page Not Found" })).toBeVisible();
    await expect(page.getByText('The page "nonexistent-page-xyz" could not be found')).toBeVisible();
    await expect(page.getByText("in this application.")).toBeVisible();

    // Computed chrome: slate-300 figure, slate-800 heading, slate-600 body,
    // slate-700 quoted path, slate-50 page wash (hex-pinned — v4 computes
    // the named slates in Lab).
    const styles = await page.evaluate(() => {
      const h1 = document.querySelector("h1");
      const h2 = document.querySelector("h2");
      const p = document.querySelector("main p, p");
      const span = p?.querySelector("span");
      const wash = [...document.querySelectorAll("div")].find((d) =>
        /min-h-screen/.test(d.className),
      );
      return {
        h1: h1 ? { size: getComputedStyle(h1).fontSize, weight: getComputedStyle(h1).fontWeight, color: getComputedStyle(h1).color } : null,
        h2: h2 ? { size: getComputedStyle(h2).fontSize, weight: getComputedStyle(h2).fontWeight, color: getComputedStyle(h2).color } : null,
        p: p ? { color: getComputedStyle(p).color } : null,
        span: span ? { color: getComputedStyle(span).color, weight: getComputedStyle(span).fontWeight } : null,
        wash: wash ? getComputedStyle(wash).backgroundColor : null,
      };
    });
    expect(styles.h1!.size).toBe("72px");
    expect(styles.h1!.weight).toBe("300");
    expect(styles.h1!.color).toBe("rgb(203, 213, 225)");
    expect(styles.h2!.size).toBe("24px");
    expect(styles.h2!.weight).toBe("500");
    expect(styles.h2!.color).toBe("rgb(30, 41, 59)");
    expect(styles.p!.color).toBe("rgb(71, 85, 105)");
    expect(styles.span!.color).toBe("rgb(51, 65, 85)");
    expect(styles.span!.weight).toBe("500");
    expect(styles.wash).toBe("rgb(248, 250, 252)");
  });

  test("Go Home navigates to the dashboard", async ({ page }) => {
    await page.goto("/nonexistent-page-xyz");
    await page.getByRole("link", { name: /Go Home/i }).click();
    await expect(page).toHaveURL(/\/$/);
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
  });

  // v25 G2: the reference's Go Home button carries `focus:outline-none
  // focus:ring-2 focus:ring-offset-2 focus:ring-slate-500` — a plain
  // `focus:` (engages on ANY focus, not keyboard-only) with a SLATE-500
  // #64748b ring (measured live: white 2px offset + rgb(100,116,139) 4px).
  // The clone had the keyboard-gated slate-400 #94a3b8 family. Every other
  // 404 value was already pinned (structure v21; geometry/title/meta below).
  test("the Go Home button renders the reference's slate-500 focus ring (v25 G2)", async ({ page }) => {
    await page.goto("/nonexistent-page-xyz");
    await expect(page.getByRole("link", { name: /Go Home/i })).toBeVisible();
    const ring = await page.evaluate(async () => {
      const b = [...document.querySelectorAll("a")].find((x) =>
        /Go Home/i.test((x.textContent || "").trim()),
      )!;
      // Plain programmatic focus — the reference's ring is `focus:`-gated,
      // not `focus-visible:` (no focusVisible option needed; the contrast
      // with the v19 dialog-button test's focusVisible cast is the point).
      b.focus();
      await new Promise((r) => setTimeout(r, 350));
      return getComputedStyle(b).boxShadow;
    });
    expect(ring).toContain("rgb(255, 255, 255) 0px 0px 0px 2px");
    expect(ring).toContain("rgb(100, 116, 139) 0px 0px 0px 4px");
  });

  test("the tab title mirrors the reference's page-name | ZeroBudget format", async ({ page }) => {
    await page.goto("/nonexistent-page-xyz");
    // The reference sets "Nonexistent Page Xyz | ZeroBudget" — a client-side
    // title component Title-Cases the path segment.
    await expect(page).toHaveTitle(/Nonexistent Page Xyz \| ZeroBudget$/);
  });
});

test.describe("document head parity (v7 — plan G8)", () => {
  test("the root document ships the reference description, OG card and canonical", async ({ page }) => {
    await page.goto("/");
    const head = await page.evaluate(() => {
      const meta = (name: string) =>
        document.querySelector(`meta[name="${name}"]`)?.getAttribute("content") ??
        document.querySelector(`meta[property="${name}"]`)?.getAttribute("content") ??
        null;
      return {
        description: meta("description"),
        ogTitle: meta("og:title"),
        ogType: meta("og:type"),
        ogUrl: meta("og:url"),
        twitterCard: meta("twitter:card"),
        twitterTitle: meta("twitter:title"),
        canonical: document.querySelector('link[rel="canonical"]')?.getAttribute("href") ?? null,
        manifest: document.querySelector('link[rel="manifest"]')?.getAttribute("href") ?? null,
        appleTitle: meta("apple-mobile-web-app-title"),
        title: document.title,
      };
    });
    // The reference's description, verbatim.
    expect(head.description).toBe(
      "Your personal zero-budget planner to manage income, savings, and expenses effortlessly. Achieve financial clarity and meet your goals with intuitive tools and a clear net zero overview. Also features a handy Net Worth Calculator.",
    );
    expect(head.ogTitle).toBe("ZeroBudget");
    expect(head.ogType).toBe("website");
    expect(head.ogUrl).toContain("http");
    expect(head.twitterCard).toBe("summary_large_image");
    expect(head.twitterTitle).toBe("ZeroBudget");
    expect(head.canonical).toContain("http");
    expect(head.manifest).toContain("manifest");
    expect(head.appleTitle).toBe("ZeroBudget");
    expect(head.title).toBe("ZeroBudget");
  });
});

test.describe("sitemap + robots (v21 — plan G1)", () => {
  test("robots.txt allows all and links the sitemap; sitemap.xml lists the five routes", async ({ page }) => {
    // The reference serves both files (measured live): robots.txt is a
    // two-line allow-all + Sitemap link, and sitemap.xml carries five URLs
    // — the origin at priority 1.0 and its four app routes at 0.8, all
    // changefreq weekly (its own capitalized paths; /login excluded). The
    // clone serves the same structure with its own lowercase routes.
    const robots = await page.request.get("/robots.txt");
    expect(robots.status()).toBe(200);
    const robotsText = await robots.text();
    // Next's generator emits the canonical "User-Agent" casing (the
    // reference writes "User-agent"); robots directives are case-
    // insensitive per RFC 9309 — match case-insensitively.
    expect(robotsText.toLowerCase()).toContain("user-agent: *");
    expect(robotsText).toMatch(/Allow:\s*\//);
    expect(robotsText).toMatch(/Sitemap:\s*https?:\/\/\S+\/sitemap\.xml/);

    const sitemap = await page.request.get("/sitemap.xml");
    expect(sitemap.status()).toBe(200);
    const xml = await sitemap.text();
    // The five routes at the reference's priorities/changefreq — /login
    // (and /api/*) never listed: the sitemap mirrors the reference's
    // public-surface choices, not the auth gate.
    const urls = [...xml.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
    expect(urls).toHaveLength(5);
    const paths = urls.map((u) => new URL(u).pathname);
    expect(paths).toEqual(["/", "/income", "/savings", "/expenses", "/networth"]);
    for (const u of urls) {
      expect(u).toMatch(/^https?:\/\/[^\/]+/);
    }
    // Next serializes the number 1.0 as "1" (numeric equivalence holds).
    expect((xml.match(/<priority>1(?:\.0)?<\/priority>/g) || [])).toHaveLength(1);
    expect((xml.match(/<priority>0\.8<\/priority>/g) || [])).toHaveLength(4);
    expect((xml.match(/<changefreq>weekly<\/changefreq>/g) || [])).toHaveLength(5);
    // The reference's sitemap carries exactly loc + changefreq + priority
    // — no <lastmod> (measured live); a per-build timestamp would be
    // shape drift, not SEO value.
    expect(xml).not.toContain("<lastmod>");
  });
});
