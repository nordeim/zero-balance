import { expect, test } from "@playwright/test";
import { DEMO_EMAIL, DEMO_PASSWORD } from "./helpers";

// Login surface: the /login route renders the reference auth card, rejects
// bad credentials, signs the demo user in, and honors authenticated visits.
// This file OPTS OUT of the shared storageState (empty cookies) because it
// tests the logged-out surface. (Deliberately does NOT probe the rate
// limiter — 10 attempts/IP/15 min would poison the whole suite.)

test.use({ storageState: { cookies: [], origins: [] } });

test.describe("login route", () => {
  test("renders the auth card with the circular logo chip", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    await expect(page.getByText("Sign in to continue")).toBeVisible();

    // The logo is a white CIRCULAR chip (rounded-full + ring-4
    // ring-white/50 + shadow-lg). Tailwind v4 computes rounded-full as
    // calc(infinity * 1px) → Chrome reports 33554432px, and ring-white/50
    // serializes in oklab() — so the assertions check the geometry and the
    // 4px ring, not exact strings.
    const chip = page.locator("span.rounded-full.ring-4").first();
    await expect(chip).toBeVisible();
    const radius = await chip.evaluate((el) => parseFloat(getComputedStyle(el).borderRadius));
    expect(radius).toBeGreaterThan(1000);
    const shadow = await chip.evaluate((el) => getComputedStyle(el).boxShadow);
    expect(shadow).toMatch(/0\.5\) 0px 0px 0px 4px/);

    // The card's slate top bar + the Google button (parity chrome).
    await expect(page.getByRole("button", { name: /Continue with Google/i })).toBeVisible();
  });

  test("the card swaps to the sign-up and forgot-password states", async ({ page }) => {
    await page.goto("/login");

    // The footer switchers are BUTTONS (the reference's pattern), not links.
    await page.getByRole("button", { name: /Sign up/ }).click();
    await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();
    await expect(page.getByRole("button", { name: "Back to sign in" })).toBeVisible();

    await page.getByRole("button", { name: "Back to sign in" }).click();
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();

    await page.getByRole("button", { name: "Forgot password?" }).click();
    await expect(page.getByRole("heading", { name: "Reset your password" })).toBeVisible();
    await expect(page.getByRole("button", { name: "Send reset link" })).toBeVisible();
  });

  test("sign-up and forgot states match the reference structure (F5)", async ({ page }) => {
    await page.goto("/login");

    // --- signup state ---
    await page.getByRole("button", { name: /Sign up/ }).click();
    const signup = await page.evaluate(() => {
      const card = [...document.querySelectorAll("div")]
        .filter(
          (d) => /Create your account/.test(d.textContent || "") && d.querySelector("input"),
        )
        .pop();
      if (!card) return null;
      const back = [...card.querySelectorAll("button")].find((b) =>
        (b.textContent || "").includes("Back to sign in"),
      );
      const h2 = card.querySelector("h2");
      return {
        cardChildren: [...card.children].map((c) => c.tagName),
        backFirst: card.firstElementChild?.contains(back ?? card.firstElementChild),
        backLeftAligned: (() => {
          if (!back) return false;
          const cr = card.getBoundingClientRect();
          const br = back.getBoundingClientRect();
          return br.x - cr.x < 40;
        })(),
        backIcon: back?.querySelector("svg")?.getAttribute("class") ?? null,
        h2Cls: h2?.className ?? null,
        hasLogo: !!card.querySelector("img"),
        hasGoogle: (card.textContent || "").includes("Continue with Google"),
        hasOrDivider: [...card.querySelectorAll("span")].some((s) => (s.textContent || "").trim() === "or"),
        hasSubtitle: !!card.querySelector("h2")?.nextElementSibling?.textContent?.match(/budget|link/i),
        fields: [...card.querySelectorAll("label")].map((l) => l.textContent?.trim()),
      };
    });
    expect(signup).not.toBeNull();
    // Back-to-sign-in button at the TOP, left-aligned, arrow-left icon.
    expect(signup!.backFirst).toBe(true);
    expect(signup!.backLeftAligned).toBe(true);
    expect(signup!.backIcon).toContain("lucide-arrow-left");
    // H2 heading (not H1), NO logo, NO Google, NO OR divider, NO subtitle.
    expect(signup!.h2Cls).toContain("text-xl");
    expect(signup!.hasLogo).toBe(false);
    expect(signup!.hasGoogle).toBe(false);
    expect(signup!.hasOrDivider).toBe(false);
    expect(signup!.hasSubtitle).toBe(false);
    expect(signup!.fields).toEqual(["Email", "Password", "Confirm Password"]);

    // --- forgot state ---
    await page.getByRole("button", { name: "Back to sign in" }).click();
    await page.getByRole("button", { name: "Forgot password?" }).click();
    const forgot = await page.evaluate(() => {
      const card = [...document.querySelectorAll("div")]
        .filter(
          (d) => /Reset your password/.test(d.textContent || "") && d.querySelector("input"),
        )
        .pop();
      if (!card) return null;
      return {
        desc: [...card.querySelectorAll("p")].map((p) => p.textContent?.trim() ?? ""),
        hasLogo: !!card.querySelector("img"),
        hasGoogle: (card.textContent || "").includes("Continue with Google"),
        hasOrDivider: [...card.querySelectorAll("span")].some((s) => (s.textContent || "").trim() === "or"),
        fields: [...card.querySelectorAll("label")].map((l) => l.textContent?.trim()),
      };
    });
    expect(forgot).not.toBeNull();
    // Reference desc wording (F5): "…we'll send you a link to reset your password".
    expect(forgot!.desc).toContain("Enter your email and we'll send you a link to reset your password");
    expect(forgot!.hasLogo).toBe(false);
    expect(forgot!.hasGoogle).toBe(false);
    expect(forgot!.hasOrDivider).toBe(false);
    expect(forgot!.fields).toEqual(["Email"]);

    // --- NO guest affordance in ANY state (the old "Continue as guest" was a
    //     dead link — /dashboard is session-gated — and a visual deviation). */
    await page.getByRole("button", { name: "Back to sign in" }).click();
    await expect(page.getByText("Continue as guest")).toHaveCount(0);
  });

  test("wrong password is rejected without a session", async ({ page }) => {
    await page.goto("/login");
    await page.getByLabel("Email").fill(DEMO_EMAIL);
    await page.getByLabel("Password").fill("definitely-wrong");
    await page.getByRole("button", { name: "Sign in" }).click();
    await expect(page.getByText("Invalid email or password").first()).toBeVisible({
      timeout: 15_000,
    });
    await expect(page).toHaveURL(/\/login/);
  });

  test("valid credentials sign in and land on the dashboard", async ({ page }) => {
    await page.goto("/login");
    await page.getByLabel("Email").fill(DEMO_EMAIL);
    await page.getByLabel("Password").fill(DEMO_PASSWORD);
    await page.getByRole("button", { name: "Sign in" }).click();
    await expect(page).toHaveURL(/\/dashboard$/, { timeout: 15_000 });
    // Desktop chrome: the fixed sidebar (not the mobile app bar) is the
    // visible landmark once signed in.
    await expect(page.locator("aside")).toBeVisible();
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
  });

  test("the root route serves the dashboard for a signed-in session", async ({ page }) => {
    // This file opted out of the storageState, so sign in via the API to
    // prove the authenticated root behavior: "/" and "/dashboard" both
    // render the dashboard (the reference's dual route), no redirect.
    const res = await page.request.post("/api/auth/login", {
      data: { email: DEMO_EMAIL, password: DEMO_PASSWORD },
    });
    expect(res.ok()).toBeTruthy();
    await page.goto("/");
    await expect(page).toHaveURL(/\/$/);
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
  });
});
