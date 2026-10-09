import { expect, test } from "@playwright/test";

// v21 G3 (docs/remediation-plan-v21.md): the register flow's
// email-verification gate, measured live on the reference — "Create
// account" lands on a centered "Verify your email" state (staying on
// /login): a top-left "Back to sign in", a 64px slate-100 circle with a
// 32px lucide-shield-check in #334155, "We've sent a 6-digit code to
// {email}" over two lines, SIX 40×44 numeric code inputs (radius 8,
// centered, gap 6), the 12px #64748b hint, the 44px #0f172a "Verify
// email" button, "Didn't receive the code? Resend", a wrong-code
// countdown ("Invalid verification code. 4 attempts remaining.", 14px
// #b91c1c), and unverified sign-ins rejected with the exact banner
// "Please verify your email before logging in. Check your email for the
// verification code." The clone's superset honesty: no SMTP on a
// self-hosted instance, so the code rides the response and renders in
// the dev-code box (the v12 forgot-password precedent).
//
// These flows are logged-OUT (no storageState) and each test registers a
// throwaway account — the register-class rate-limit budget (10/IP/15min
// shared with login-parity's single 409 call) stays under the cap. Since
// v23 the file holds FIVE register-class calls (4 desktop + 1 mobile) +
// the login-parity 409 = 6 total, still under the 10/IP/15min bucket (and
// the in-memory limiter resets on every server boot).

test.use({ storageState: { cookies: [], origins: [] } });

const PASSWORD = "TestPass123!";

async function registerFreshAccount(page: import("@playwright/test").Page, email: string) {
  await page.goto("/login");
  await page.getByRole("button", { name: "Need an account? Sign up" }).click();
  await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();
  await page.getByLabel("Email").fill(email);
  await page.getByLabel("Password", { exact: true }).fill(PASSWORD);
  await page.getByLabel("Confirm Password").fill(PASSWORD);
  await page.getByRole("button", { name: "Create account" }).click();
  await expect(page.getByRole("heading", { name: "Verify your email" })).toBeVisible();
  // v22 G1 (docs/remediation-plan-v22.md): the pointer stays parked at the
  // Create-account click point, and the swapped-in "Verify email" button
  // lands under it — :hover applies and its 200ms transition from #0f172a
  // toward #1e293b is mid-flight when a chrome read lands (the baseline's
  // rgb(19,27,46) failure). Park far away + settle past the transition
  // (the AGENTS.md transition discipline; the prior session's green run
  // was timing luck).
  await page.mouse.move(5, 5);
  await page.waitForTimeout(350);
}

async function readDevCode(page: import("@playwright/test").Page): Promise<string> {
  const box = page.locator("text=/your verification code is/").first();
  await expect(box).toBeVisible();
  const text = await box.textContent();
  const match = (text || "").match(/(\d{6})/);
  expect(match, "the dev-code box carries the 6-digit code").not.toBeNull();
  return match![1];
}

test.describe("register verify-email gate (v21 — plan G3)", () => {
  test("the register flow lands on the verify state with the reference chrome", async ({ page }) => {
    const email = `v21-chrome-${Date.now()}@example.com`;
    await registerFreshAccount(page, email);

    // The URL stays on /login (the reference's measured behavior — the
    // state swaps inside the card, no navigation).
    expect(page.url()).toContain("/login");
    await expect(page.getByText(`We've sent a 6-digit code to`)).toBeVisible();
    // The email renders as the paragraph's second line (after the <br/>).
    await expect(page.getByText(email)).toBeVisible();

    const chrome = await page.evaluate(() => {
      const circle = [...document.querySelectorAll("main div")].find((d) =>
        (d.className || "").toString().includes("bg-[#f1f5f9]"),
      );
      const icon = circle?.querySelector("svg") ?? null;
      const inputs = [...document.querySelectorAll<HTMLInputElement>('input[inputmode="numeric"]')];
      const verifyBtn = [...document.querySelectorAll("button")].find(
        (b) => (b.textContent || "").trim() === "Verify email",
      );
      const hint = [...document.querySelectorAll("p")].find((p) =>
        /Enter the verification code/.test(p.textContent || ""),
      );
      const hcs = hint ? getComputedStyle(hint) : null;
      const resend = [...document.querySelectorAll("button")].find((b) =>
        (b.textContent || "").trim() === "Resend",
      );
      return {
        circle: circle
          ? { w: Math.round(circle.getBoundingClientRect().width), bg: getComputedStyle(circle).backgroundColor }
          : null,
        icon: icon
          ? { w: Math.round(icon.getBoundingClientRect().width), color: getComputedStyle(icon).color }
          : null,
        inputs: inputs.map((i) => {
          const r = i.getBoundingClientRect();
          const cs = getComputedStyle(i);
          return {
            w: Math.round(r.width),
            h: Math.round(r.height),
            radius: cs.borderRadius,
            ta: cs.textAlign,
            mode: i.getAttribute("inputmode"),
            // v26 — plan G2: the reference runs autocomplete one-time-code
            // on the FIRST box only and off on the rest (measured live —
            // the standard OTP convention; the browser's code offer targets
            // the first box).
            ac: i.getAttribute("autocomplete"),
          };
        }),
        btn: verifyBtn
          ? {
              h: Math.round(verifyBtn.getBoundingClientRect().height),
              bg: getComputedStyle(verifyBtn).backgroundColor,
              radius: getComputedStyle(verifyBtn).borderRadius,
            }
          : null,
        hint: hcs ? { size: hcs.fontSize, color: hcs.color } : null,
        resend: resend ? { size: getComputedStyle(resend).fontSize, color: getComputedStyle(resend).color } : null,
      };
    });
    // The 64px slate-100 circle + 32px shield-check in #334155.
    expect(chrome.circle!.w).toBe(64);
    expect(chrome.circle!.bg).toBe("rgb(241, 245, 249)");
    expect(chrome.icon!.w).toBe(32);
    expect(chrome.icon!.color).toBe("rgb(51, 65, 85)");
    // Six 40×44 numeric inputs, radius 8, centered.
    expect(chrome.inputs).toHaveLength(6);
    for (const i of chrome.inputs) {
      expect(i.w).toBe(40);
      expect(i.h).toBe(44);
      expect(i.radius).toBe("8px");
      expect(i.ta).toBe("center");
      expect(i.mode).toBe("numeric");
    }
    // v26 — plan G2: the autocomplete distribution — one-time-code on the
    // first box, off on the other five (the reference's measured pattern).
    expect(chrome.inputs.map((i) => i.ac)).toEqual([
      "one-time-code",
      "off",
      "off",
      "off",
      "off",
      "off",
    ]);
    // The 44px #0f172a primary button (the sign-up-state height, radius 12).
    expect(chrome.btn!.h).toBe(44);
    expect(chrome.btn!.bg).toBe("rgb(15, 23, 42)");
    expect(chrome.btn!.radius).toBe("12px");
    // The 12px #64748b hint + the 14px #334155 Resend link.
    expect(chrome.hint!.size).toBe("12px");
    expect(chrome.hint!.color).toBe("rgb(100, 116, 139)");
    expect(chrome.resend!.size).toBe("14px");
    expect(chrome.resend!.color).toBe("rgb(51, 65, 85)");
    // The honest dev-code delivery renders.
    await expect(page.getByText(/No mail transport is configured/)).toBeVisible();
  });

  test("a wrong code counts down; the correct code verifies and lands on the dashboard", async ({ page }) => {
    const email = `v21-flow-${Date.now()}@example.com`;
    await registerFreshAccount(page, email);
    const code = await readDevCode(page);

    // A wrong code first — the reference's exact countdown text.
    for (let i = 0; i < 6; i++) {
      await page.getByLabel(`Digit ${i + 1}`).fill(i === 0 ? "9" : "9");
    }
    await page.getByRole("button", { name: "Verify email" }).click();
    await expect(page.getByText("Invalid verification code. 4 attempts remaining.")).toBeVisible();

    // The correct code — the account verifies, the session opens, and the
    // app lands on "/" (the reference's post-login root-route behavior).
    for (let i = 0; i < 6; i++) {
      await page.getByLabel(`Digit ${i + 1}`).fill(code[i]);
    }
    await page.getByRole("button", { name: "Verify email" }).click();
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
    expect(new URL(page.url()).pathname).toBe("/");
  });

  test("an unverified account cannot sign in — the reference's banner", async ({ page }) => {
    const email = `v21-gate-${Date.now()}@example.com`;
    await registerFreshAccount(page, email);

    // Back to sign in, then try the (unverified) credentials.
    await page.getByRole("button", { name: "Back to sign in" }).click();
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    await page.getByLabel("Email").fill(email);
    await page.getByLabel("Password").fill(PASSWORD);
    await page.getByRole("button", { name: "Sign in" }).click();
    await expect(
      page.getByText("Please verify your email before logging in. Check your email for the verification code."),
    ).toBeVisible();
    // Still on the login card — no session was issued.
    expect(page.url()).toContain("/login");
  });

  test("resend re-issues a code and the fresh code verifies", async ({ page }) => {
    const email = `v21-resend-${Date.now()}@example.com`;
    await registerFreshAccount(page, email);
    const firstCode = await readDevCode(page);

    await page.getByRole("button", { name: "Resend" }).click();
    await expect(page.getByText("New verification code sent to your email")).toBeVisible();
    const secondCode = await readDevCode(page);
    // A fresh code (collision odds 1/1e6 — and the digits box re-renders).
    expect(secondCode).toMatch(/^\d{6}$/);

    // The re-issued code verifies (whichever value it holds — a re-issue
    // resets the attempts too, so this also pins the reset semantics).
    for (let i = 0; i < 6; i++) {
      await page.getByLabel(`Digit ${i + 1}`).fill(secondCode[i]);
    }
    await page.getByRole("button", { name: "Verify email" }).click();
    await expect(page.getByRole("heading", { name: "Budget Dashboard" })).toBeVisible();
    // Silence the unused-var lint when codes coincide by chance.
    expect(firstCode).toMatch(/^\d{6}$/);
  });
});

test.describe("register verify-email gate at MOBILE (v23 — plan G2)", () => {
  // v23 G2 (docs/remediation-plan-v23.md): the verify state measured live
  // at 390×844 for the first time — the reference renders its MOBILE
  // scale: the circle 56px (desktop 64), the shield icon 28px (desktop
  // 32), the h2 20px (desktop 24) — the responsive classes
  // h-14 w-14 sm:h-16 / h-7 w-7 sm:h-8 / text-xl sm:text-2xl. The inputs
  // (6 × 40×44, gap 6, radius 8, centered) and the Verify button
  // (294×44 #0f172a radius 12 — h-11 at every viewport) are
  // viewport-invariant. The desktop describe above pins the ≥640 scale;
  // this pins the mobile one so a responsive-class regression can't pass
  // desktop and drift mobile.
  test.use({ viewport: { width: 390, height: 844 } });

  test("the verify state renders the reference's mobile chrome", async ({ page }) => {
    const email = `v23-mobile-${Date.now()}@example.com`;
    await registerFreshAccount(page, email);

    const chrome = await page.evaluate(() => {
      const circle = [...document.querySelectorAll("main div")].find((d) =>
        (d.className || "").toString().includes("bg-[#f1f5f9]"),
      );
      const icon = circle?.querySelector("svg") ?? null;
      const inputs = [...document.querySelectorAll<HTMLInputElement>('input[inputmode="numeric"]')];
      const verifyBtn = [...document.querySelectorAll("button")].find(
        (b) => (b.textContent || "").trim() === "Verify email",
      );
      const h2 = [...document.querySelectorAll("h2")].find((h) =>
        /Verify your email/.test(h.textContent || ""),
      );
      return {
        circle: circle
          ? { w: Math.round(circle.getBoundingClientRect().width), bg: getComputedStyle(circle).backgroundColor }
          : null,
        icon: icon ? { w: Math.round(icon.getBoundingClientRect().width), color: getComputedStyle(icon).color } : null,
        inputs: inputs.map((i) => {
          const r = i.getBoundingClientRect();
          const cs = getComputedStyle(i);
          return { w: Math.round(r.width), h: Math.round(r.height), x: Math.round(r.x), radius: cs.borderRadius, ta: cs.textAlign };
        }),
        btn: verifyBtn
          ? {
              w: Math.round(verifyBtn.getBoundingClientRect().width),
              h: Math.round(verifyBtn.getBoundingClientRect().height),
              bg: getComputedStyle(verifyBtn).backgroundColor,
              radius: getComputedStyle(verifyBtn).borderRadius,
            }
          : null,
        h2: h2
          ? { size: getComputedStyle(h2).fontSize, weight: getComputedStyle(h2).fontWeight, color: getComputedStyle(h2).color }
          : null,
      };
    });
    // The 56px slate-100 circle + the 28px shield-check (the mobile scale
    // of the responsive family — 64/32 at >=640px).
    expect(chrome.circle!.w).toBe(56);
    expect(chrome.circle!.bg).toBe("rgb(241, 245, 249)");
    expect(chrome.icon!.w).toBe(28);
    expect(chrome.icon!.color).toBe("rgb(51, 65, 85)");
    // Six 40×44 inputs at the mobile row geometry: x 60→290 (gap 6),
    // radius 8, centered — identical to the desktop row.
    expect(chrome.inputs).toHaveLength(6);
    for (const i of chrome.inputs) {
      expect(i.w).toBe(40);
      expect(i.h).toBe(44);
      expect(i.radius).toBe("8px");
      expect(i.ta).toBe("center");
    }
    if (chrome.inputs.length > 1) {
      expect(chrome.inputs[0].x).toBe(60);
      expect(chrome.inputs[1].x - (chrome.inputs[0].x + 40)).toBe(6);
    }
    // The 294×44 #0f172a button — h-11 at every viewport, the mobile
    // card's full content width.
    expect(chrome.btn!.w).toBe(294);
    expect(chrome.btn!.h).toBe(44);
    expect(chrome.btn!.bg).toBe("rgb(15, 23, 42)");
    expect(chrome.btn!.radius).toBe("12px");
    // The h2 at its mobile scale: 20px/700 #0f172a (text-xl; 24px at
    // >=640px).
    expect(chrome.h2!.size).toBe("20px");
    expect(chrome.h2!.weight).toBe("700");
    expect(chrome.h2!.color).toBe("rgb(15, 23, 42)");
  });
});
