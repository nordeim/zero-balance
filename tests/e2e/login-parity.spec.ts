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

// ---------------------------------------------------------------------------
// v9 — per-state control geometry (docs/remediation-plan-v9.md G7).
//
// Measured live on the reference (fresh unauthenticated session, all three
// card states): the primary button text is 14px/500 in EVERY state (the
// Google button is the 16px one); the SIGN-IN state's controls are 48px at
// ≥640px, but the SIGN-UP and FORGOT states' inputs + primary button are
// 44px (h-11) — a per-state geometry the clone flattened to 48 everywhere.
// ---------------------------------------------------------------------------

test.describe("login per-state control geometry (v9)", () => {
  test("sign-in: 14px button text + 48px controls (regression)", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    const geo = await page.evaluate(() => {
      const submit = [...document.querySelectorAll('button[type="submit"]')][0];
      const email = document.querySelector('input[type="email"]')!;
      return {
        fs: getComputedStyle(submit).fontSize,
        h: Math.round(submit.getBoundingClientRect().height),
        inputH: Math.round(email.getBoundingClientRect().height),
      };
    });
    expect(geo.fs).toBe("14px");
    expect(geo.h).toBe(48);
    expect(geo.inputH).toBe(48);
  });

  test("sign-up: 14px button text + 44px controls", async ({ page }) => {
    await page.goto("/login");
    await page.getByRole("button", { name: "Need an account? Sign up" }).click();
    await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();
    const geo = await page.evaluate(() => {
      const submit = [...document.querySelectorAll('button[type="submit"]')][0];
      const inputs = [...document.querySelectorAll("form input")];
      const email = document.querySelector<HTMLInputElement>('input[type="email"]');
      return {
        fs: getComputedStyle(submit).fontSize,
        h: Math.round(submit.getBoundingClientRect().height),
        inputHs: inputs.map((i) => Math.round(i.getBoundingClientRect().height)),
        emailH: email ? Math.round(email.getBoundingClientRect().height) : null,
      };
    });
    expect(geo.fs).toBe("14px");
    expect(geo.h).toBe(44);
    for (const h of geo.inputHs) expect(h).toBe(44);
  });

  test("forgot: 14px button text + 44px controls", async ({ page }) => {
    await page.goto("/login");
    await page.getByRole("button", { name: "Forgot password?" }).click();
    await expect(page.getByRole("heading", { name: "Reset your password" })).toBeVisible();
    const geo = await page.evaluate(() => {
      const submit = [...document.querySelectorAll('button[type="submit"]')][0];
      const inputs = [...document.querySelectorAll("form input")];
      return {
        fs: getComputedStyle(submit).fontSize,
        h: Math.round(submit.getBoundingClientRect().height),
        inputHs: inputs.map((i) => Math.round(i.getBoundingClientRect().height)),
      };
    });
    expect(geo.fs).toBe("14px");
    expect(geo.h).toBe(44);
    for (const h of geo.inputHs) expect(h).toBe(44);
  });
});

// ---------------------------------------------------------------------------
// v12 — login error banner + root landmark + forgot confirmation state
// (docs/remediation-plan-v12.md G1/G3/G4).
//
// Measured live on the reference: the auth error renders as a red-tinted
// bordered banner — a direct child of the form's space-y flow — with bg
// rgba(254,242,242,0.7) (red-50 at 70%), border 1px solid #fecaca
// (red-200), radius 12px, padding 16px, and a CENTERED #b91c1c (red-700)
// 14px/400 lh-20 inner div (the shadcn FormMessage pattern; box 368×54 at
// desktop). The same slot renders "Invalid email or password" (sign-in)
// and "Passwords do not match" (sign-up). The forgot submit transitions
// the card to a centered confirmation state — H2 24px/700 #0f172a, 16px
// descriptions (#475569 / #09090b), a 14px/500 #64748b "Back to sign in"
// — the clone renders the reference LAYOUT with honest copy (no mail
// transport exists on a self-hosted instance; the reference pretends a
// reset link was sent). The login page's root is a <main> landmark on the
// reference (flex min-h-screen centered p-4) — the clone rendered a div.
// ---------------------------------------------------------------------------

test.describe("login error banner + confirmation state (v12)", () => {
  test("the signup mismatch error renders the reference banner chrome (G1)", async ({ page }) => {
    await page.goto("/login");
    await page.getByRole("button", { name: "Need an account? Sign up" }).click();
    await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();
    // Pure client-side validation — no auth API call, no rate-limit budget.
    await page.getByLabel("Email").fill("probe@example.com");
    // exact: the sign-up state carries both "Password" and "Confirm
    // Password" labels (substring matching would resolve two elements).
    await page.getByLabel("Password", { exact: true }).fill("Password123");
    await page.getByLabel("Confirm Password").fill("Password456");
    await page.getByRole("button", { name: "Create account" }).click();
    await expect(page.getByText("Passwords do not match")).toBeVisible();
    const banner = await page.evaluate(() => {
      const alert = document.querySelector("[role='alert']");
      if (!alert) return null;
      const cs = getComputedStyle(alert);
      const r = alert.getBoundingClientRect();
      const inner = alert.firstElementChild;
      const ics = inner ? getComputedStyle(inner) : null;
      return {
        bg: cs.backgroundColor,
        border: `${cs.borderTopWidth} ${cs.borderTopStyle} ${cs.borderTopColor}`,
        radius: cs.borderRadius,
        padding: cs.padding,
        height: Math.round(r.height),
        display: cs.display,
        inner: ics
          ? { color: ics.color, fs: ics.fontSize, fw: ics.fontWeight, lh: ics.lineHeight, align: ics.textAlign }
          : null,
      };
    });
    expect(banner).not.toBeNull();
    // Reference: red-50/70% wash, red-200 border, 12px radius, 16px padding.
    expect(banner!.bg).toBe("rgba(254, 242, 242, 0.7)");
    expect(banner!.border).toBe("1px solid rgb(254, 202, 202)");
    expect(banner!.radius).toBe("12px");
    expect(banner!.padding).toBe("16px");
    // 20px text + 2×16px padding + 2×1px border.
    expect(banner!.height).toBe(54);
    expect(banner!.display).toBe("block");
    // Inner text: red-700 14px/400, centered (v4 computes the named reds
    // in Lab — the values are inline-style pins).
    expect(banner!.inner!.color).toBe("rgb(185, 28, 28)");
    expect(banner!.inner!.fs).toBe("14px");
    expect(banner!.inner!.fw).toBe("400");
    expect(banner!.inner!.lh).toBe("20px");
    expect(banner!.inner!.align).toBe("center");
  });

  test("the login page root is a <main> landmark holding the card (G3)", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    const root = await page.evaluate(() => {
      const main = document.querySelector("main");
      if (!main) return null;
      const cs = getComputedStyle(main);
      return {
        tag: main.tagName,
        display: cs.display,
        // min-h-screen resolves against THIS viewport — compare to
        // innerHeight, not a hardcoded 800px (the reference was measured
        // on a 1280×800 session; Playwright's default is 720).
        minHMatchesViewport: cs.minHeight === `${window.innerHeight}px`,
        pad: cs.padding,
        justify: cs.justifyContent,
        hasCard: !!main.querySelector("h1"),
      };
    });
    // Reference root: <main class="min-h-screen flex items-center
    // justify-center ... p-4"> with the card inside.
    expect(root).not.toBeNull();
    expect(root!.tag).toBe("MAIN");
    expect(root!.display).toBe("flex");
    expect(root!.minHMatchesViewport).toBe(true);
    expect(root!.pad).toBe("16px");
    expect(root!.justify).toBe("center");
    expect(root!.hasCard).toBe(true);
  });

  test("forgot submit transitions to the reference confirmation-state layout with honest copy (G4)", async ({ page }) => {
    await page.goto("/login");
    await page.getByRole("button", { name: "Forgot password?" }).click();
    await expect(page.getByRole("heading", { name: "Reset your password" })).toBeVisible();
    await page.getByLabel("Email").fill("demo@zerobalance.app");
    await page.getByRole("button", { name: "Send reset link" }).click();
    // The reference's state layout, honest copy: this self-hosted instance
    // has no email service — the heading replaces "Check your email".
    await expect(page.getByRole("heading", { name: "Password reset unavailable" })).toBeVisible({
      timeout: 10_000,
    });
    const styles = await page.evaluate(() => {
      const h2 = [...document.querySelectorAll("h2")].find((h) =>
        /Password reset unavailable/.test(h.textContent || ""),
      );
      const desc = [...document.querySelectorAll("p")].find((p) =>
        /no email service/i.test(p.textContent || ""),
      );
      const back = [...document.querySelectorAll("button")].find((b) =>
        /Back to sign in/i.test(b.textContent || ""),
      );
      const m = (el: Element | null | undefined) => {
        if (!el) return null;
        const cs = getComputedStyle(el);
        return { fs: cs.fontSize, fw: cs.fontWeight, color: cs.color, lh: cs.lineHeight, align: cs.textAlign };
      };
      return { h2: m(h2), desc: m(desc), back: m(back) };
    });
    // Reference state typography (measured live on its "Check your email"
    // state): H2 24px/700 #0f172a lh 32; descriptions 16px #475569 lh 24;
    // back link 14px/500 #64748b lh 20 — all centered.
    expect(styles.h2!.fs).toBe("24px");
    expect(styles.h2!.fw).toBe("700");
    expect(styles.h2!.lh).toBe("32px");
    expect(styles.h2!.color).toBe("rgb(15, 23, 42)");
    expect(styles.h2!.align).toBe("center");
    expect(styles.desc!.fs).toBe("16px");
    expect(styles.desc!.lh).toBe("24px");
    expect(styles.desc!.color).toBe("rgb(71, 85, 105)");
    expect(styles.desc!.align).toBe("center");
    expect(styles.back!.fs).toBe("14px");
    expect(styles.back!.fw).toBe("500");
    expect(styles.back!.lh).toBe("20px");
    expect(styles.back!.color).toBe("rgb(100, 116, 139)");
    expect(styles.back!.align).toBe("center");
    // The form is replaced by the state (reference behavior).
    await expect(page.getByLabel("Email")).toHaveCount(0);
    // And "Back to sign in" returns to the sign-in state.
    await page.getByRole("button", { name: "Back to sign in" }).click();
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
  });
});

// ---------------------------------------------------------------------------
// v13 — register error text + sign-up placeholders + input focus ring
// (docs/remediation-plan-v13.md G1/G2/G3).
//
// Measured live on the reference (session 25): the register duplicate-email
// 409 renders the v12 banner chrome with the text "A user with this email
// already exists" (the clone said "An account with this email already
// exists"); the sign-up state's password placeholder is "Min. 8 characters"
// and the confirm field's is "Re-enter password" (sign-in keeps ••••••••);
// and on :focus the login inputs render the shadcn two-layer ring —
// box-shadow "rgb(255,255,255) 0 0 0 2px, rgb(148,163,184) 0 0 0 4px"
// (white 2px offset + slate-400 4px) on top of the slate-400 border —
// while the clone's color-only v4 ring utility emitted NO shadow at all.
// ---------------------------------------------------------------------------

test.describe("register flow + input chrome (v13)", () => {
  test("register duplicate-email error renders the reference text in the v12 banner (G1)", async ({ page }) => {
    await page.goto("/login");
    await page.getByRole("button", { name: "Need an account? Sign up" }).click();
    await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();
    // The seeded demo email — the register API 409s BEFORE any write (the
    // findUnique check precedes user.create), so no fixture restore needed.
    // ONE register call; its rate-limit bucket (register:<ip>) is separate
    // from login's, and the e2e server boots fresh each run.
    await page.getByLabel("Email").fill("demo@zerobalance.app");
    await page.getByLabel("Password", { exact: true }).fill("Password123");
    await page.getByLabel("Confirm Password").fill("Password123");
    await page.getByRole("button", { name: "Create account" }).click();
    // Wait for the async 409 to land before reading the banner text (the
    // fetch resolves after the click returns — the v12 mismatch test waited
    // on its client-side text for the same reason).
    await page.waitForSelector("[role='alert']", { timeout: 10_000 });
    // Reference text (measured live, session 25): "A user with this email
    // already exists" — the banner chrome is already pinned by the v12
    // mismatch test; here the assertion is the exact 401/409-slot TEXT.
    const banner = await page.evaluate(() => {
      const alert = document.querySelector("[role='alert']");
      return alert ? alert.textContent!.trim() : null;
    });
    expect(banner).toBe("A user with this email already exists");
  });

  test("sign-up password placeholders match the reference (G2)", async ({ page }) => {
    await page.goto("/login");
    await page.getByRole("button", { name: "Need an account? Sign up" }).click();
    await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();
    const ph = await page.evaluate(() => {
      const pw = document.querySelector<HTMLInputElement>("input#password");
      const confirm = document.querySelector<HTMLInputElement>("input#confirm");
      return { pw: pw?.placeholder ?? null, confirm: confirm?.placeholder ?? null };
    });
    // Reference sign-up state (measured live): the password field hints the
    // minimum length, the confirm field its purpose.
    expect(ph.pw).toBe("Min. 8 characters");
    expect(ph.confirm).toBe("Re-enter password");
    // Sign-in keeps the dot placeholder (reference re-verified live).
    await page.getByRole("button", { name: "Back to sign in" }).click();
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    const signinPh = await page.evaluate(() => {
      const pw = document.querySelector<HTMLInputElement>("input#password");
      return pw?.placeholder ?? null;
    });
    expect(signinPh).toBe("••••••••");
  });

  test("login inputs render the reference two-layer focus ring (G3)", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    // The reference applies the ring on plain :focus (programmatic focus
    // triggers it — not :focus-visible-gated). transition-colors animates
    // the border color — settle before reading computed styles.
    const email = await page.evaluate(async () => {
      const e = document.querySelector<HTMLInputElement>("input#email")!;
      e.focus();
      await new Promise((r) => setTimeout(r, 350));
      const cs = getComputedStyle(e);
      return { border: cs.borderColor, shadow: cs.boxShadow };
    });
    expect(email.border).toBe("rgb(148, 163, 184)");
    // Visible layers of the reference's ring (white 2px offset + slate-400
    // 4px); v3's trailing transparent 0-layer paints nothing (v10 lesson).
    expect(email.shadow).toContain("rgb(255, 255, 255) 0px 0px 0px 2px");
    expect(email.shadow).toContain("rgb(148, 163, 184) 0px 0px 0px 4px");

    // The sign-up state's password input carries the same INPUT_CLS — spot
    // check it (exact: both Password labels exist in this state).
    await page.getByRole("button", { name: "Need an account? Sign up" }).click();
    await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();
    const pw = await page.evaluate(async () => {
      const e = document.querySelector<HTMLInputElement>("input#password")!;
      e.focus();
      await new Promise((r) => setTimeout(r, 350));
      const cs = getComputedStyle(e);
      return { border: cs.borderColor, shadow: cs.boxShadow };
    });
    expect(pw.border).toBe("rgb(148, 163, 184)");
    expect(pw.shadow).toContain("rgb(255, 255, 255) 0px 0px 0px 2px");
    expect(pw.shadow).toContain("rgb(148, 163, 184) 0px 0px 0px 4px");
  });
});
