import { expect, test } from "@playwright/test";

// Login-surface computed chrome (session-13 audit, docs/remediation-plan-v7.md
// G2/G3): the login page was the last surface styled with NAMED slate classes —
// Tailwind v4 computes those in Lab color space while the reference emits plain
// rgb/rgba, and its page gradient ran through v4's oklab conversion. Every
// value below was measured on the live reference (see the plan's ledger):
//   slate-900 #0f172a · slate-800 #1e293b · slate-700 #334155 · slate-600
//   #475569 · slate-500 #64748b · slate-400 #94a3b8 · slate-300 #cbd5e1 ·
//   slate-200 #e2e8f0 · slate-50 #f8fafc.
// Also pins the footer links' text-sm (14px/20px — the reference renders them
// at 14px, not the inherited 16px) and the logo ring's plain-rgba color.
// This file OPTS OUT of the shared storageState (logged-out surface).

test.use({ storageState: { cookies: [], origins: [] } });

test.describe("login surface computed chrome (v7 — plan G2/G3)", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
  });

  test("heading, subtitle and footer links render the reference slate values", async ({ page }) => {
    const styles = await page.evaluate(() => {
      const h1 = document.querySelector("h1");
      const sub = [...document.querySelectorAll("p")].find((p) =>
        /Sign in to continue/.test(p.textContent || ""),
      );
      const forgot = [...document.querySelectorAll("button")].find((b) =>
        /Forgot password\?/.test(b.textContent || ""),
      );
      const label = document.querySelector("label");
      return {
        h1: h1 ? getComputedStyle(h1).color : null,
        sub: sub ? getComputedStyle(sub).color : null,
        forgot: forgot
          ? {
              size: getComputedStyle(forgot).fontSize,
              lineHeight: getComputedStyle(forgot).lineHeight,
              height: Math.round(forgot.getBoundingClientRect().height),
              color: getComputedStyle(forgot).color,
            }
          : null,
        label: label ? getComputedStyle(label).color : null,
      };
    });
    // Reference: slate-900 #0f172a (NOT lab()), slate-500 #64748b, text-sm.
    expect(styles.h1).toBe("rgb(15, 23, 42)");
    expect(styles.sub).toBe("rgb(100, 116, 139)");
    expect(styles.forgot!.size).toBe("14px");
    expect(styles.forgot!.lineHeight).toBe("20px");
    expect(styles.forgot!.height).toBe(20);
    expect(styles.forgot!.color).toBe("rgb(100, 116, 139)");
    expect(styles.label).toBe("rgb(51, 65, 85)");
  });

  test("the card, its top bar and the page gradient compute as plain rgb", async ({ page }) => {
    const styles = await page.evaluate(() => {
      const card = [...document.querySelectorAll("div")].find(
        (d) => /rounded-2xl/.test(d.className) && d.querySelector("h1"),
      );
      const bar = card?.querySelector("div");
      const page = card?.closest(".min-h-screen") ?? null;
      return {
        card: card ? getComputedStyle(card).backgroundColor : null,
        bar: bar ? getComputedStyle(bar).backgroundImage : null,
        page: page ? getComputedStyle(page).backgroundImage : null,
      };
    });
    // Reference: bg-white/95 as rgba, slate-50→100 gradient as plain rgb stops.
    expect(styles.card).toBe("rgba(255, 255, 255, 0.95)");
    expect(styles.bar).toContain("rgb(226, 232, 240)");
    expect(styles.bar).toContain("rgb(203, 213, 225)");
    expect(styles.page).toContain("rgb(248, 250, 252)");
    expect(styles.page).toContain("rgb(241, 245, 249)");
    // v4's Lab conversions must not appear anywhere on the surface.
    expect(styles.page).not.toContain("lab(");
    expect(styles.card).not.toContain("oklab(");
  });

  test("the submit button and inputs render the reference values", async ({ page }) => {
    const styles = await page.evaluate(() => {
      const submit = [...document.querySelectorAll('button[type="submit"]')][0];
      const email = document.querySelector<HTMLInputElement>('input[type="email"]');
      return {
        submit: submit
          ? {
              bg: getComputedStyle(submit).backgroundColor,
              color: getComputedStyle(submit).color,
              height: Math.round(submit.getBoundingClientRect().height),
            }
          : null,
        email: email
          ? {
              border: getComputedStyle(email).borderTopColor,
              bg: getComputedStyle(email).backgroundColor,
            }
          : null,
      };
    });
    // Reference: solid slate-900 (no gradient), 48px tall at ≥640px.
    expect(styles.submit!.bg).toBe("rgb(15, 23, 42)");
    expect(styles.submit!.color).toBe("rgb(255, 255, 255)");
    expect(styles.submit!.height).toBe(48);
    expect(styles.email!.border).toBe("rgb(226, 232, 240)");
    expect(styles.email!.bg).toBe("rgba(248, 250, 252, 0.5)");
  });

  test("the logo ring halo computes as plain rgba white at 4px spread", async ({ page }) => {
    const shadow = await page.evaluate(() => {
      const ring = document.querySelector<HTMLElement>(".zb-logo-ring");
      return ring ? getComputedStyle(ring).boxShadow : null;
    });
    // Reference: rgba(255,255,255,0.5) 0 0 0 4px (v4's ring-white/50 drifts
    // to oklab — pin the color with an explicit layer).
    expect(shadow).toContain("rgba(255, 255, 255, 0.5) 0px 0px 0px 4px");
    expect(shadow).not.toContain("oklab(");
  });

  test("the Google button renders the reference text + border colors", async ({ page }) => {
    const styles = await page.evaluate(() => {
      const g = [...document.querySelectorAll("button")].find((b) =>
        /Continue with Google/.test(b.textContent || ""),
      );
      if (!g) return null;
      const cs = getComputedStyle(g);
      return { color: cs.color, border: cs.borderTopColor, bg: cs.backgroundColor };
    });
    expect(styles).not.toBeNull();
    // Reference: slate-700 text #334155, slate-200 border #e2e8f0, white bg.
    expect(styles!.color).toBe("rgb(51, 65, 85)");
    expect(styles!.border).toBe("rgb(226, 232, 240)");
    expect(styles!.bg).toBe("rgb(255, 255, 255)");
  });
});
