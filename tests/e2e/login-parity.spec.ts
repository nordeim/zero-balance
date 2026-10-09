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
    // Reference text (measured live, session 25): "A user with this email
    // already exists" — the banner chrome is already pinned by the v12
    // mismatch test; here the assertion is the exact 401/409-slot TEXT.
    // v18 G2: assert via a RETRYING, TEXT-FILTERED locator — Next.js's
    // route announcer ALSO renders role="alert" (`__next-route-
    // announcer__`, aria-live, mounts dynamically with EMPTY text), so
    // both the old `waitForSelector("[role='alert']")` and a bare
    // getByRole("alert") can match it (a strict-mode violation) or
    // nothing (a transient unmount — the old one-shot evaluate read
    // null in ~half of the full runs, flake never reproduced in file
    // isolation). Filtering on the expected text scopes the locator to
    // the BANNER; toBeVisible polls through any churn.
    await expect(
      page.getByRole("alert").filter({ hasText: "A user with this email already exists" })
    ).toBeVisible();
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

// ---------------------------------------------------------------------------
// v24 — the auth forms' MOBILE responsive families + the label→input gap
// (docs/remediation-plan-v24.md G1/G2).
//
// Measured live on both sites (fresh-open + settled census, the
// probe-v24-auth-census pattern): the reference runs THREE distinct
// responsive families across its auth forms —
//   sign-in  input `h-11 sm:h-12` (44/48) · `text-base md:text-sm` (16/14)
//   sign-up  input `h-10 sm:h-11` (40/44) · `text-sm sm:text-base md:text-sm`
//            (14/16/14 — 16px only in the 640–768 band)
//   forgot   input `h-10 sm:h-11` (40/44) · `text-base md:text-sm` (16/14)
// with the submit buttons following their state's height family. The
// reference's class list was read off its live DOM as the tie-breaker (one
// shared-tab false-read this session makes the class attribute the arbiter).
// The label→input gap: the reference's v3 space-y-1.5 puts margin-top 6px
// on the input's relative wrapper → a 10px rect gap under an inline
// text-sm/20 label (16px glyph rect + 4px leading + 6px margin). The
// clone's v4 space-y-1.5 puts margin-bottom on the INLINE label — absorbed
// by the line box → 4px. The dialogs were pinned by the v9 globals.css
// space-y-2 fix; these tests pin the auth-card counterpart.

test.describe("auth-form mobile responsive families (v24 — plan G1)", () => {
  test.use({ viewport: { width: 390, height: 844 } });

  test("sign-in keeps its 44px controls at mobile (the family that already matches)", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    const geo = await page.evaluate(() => {
      const submit = [...document.querySelectorAll('button[type="submit"]')][0];
      const email = document.querySelector<HTMLInputElement>('input[type="email"]')!;
      return {
        submitH: Math.round(submit.getBoundingClientRect().height),
        inputH: Math.round(email.getBoundingClientRect().height),
        inputFs: getComputedStyle(email).fontSize,
      };
    });
    // h-11 sm:h-12 renders 44 below 640 — the reference's sign-in family.
    expect(geo.submitH).toBe(44);
    expect(geo.inputH).toBe(44);
    expect(geo.inputFs).toBe("16px");
  });

  test("sign-up renders the reference's 40px h-10 family + 14px input font at mobile", async ({ page }) => {
    await page.goto("/login");
    await page.getByRole("button", { name: "Need an account? Sign up" }).click();
    await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();
    const geo = await page.evaluate(() => {
      const submit = [...document.querySelectorAll('button[type="submit"]')][0];
      const inputs = [...document.querySelectorAll("form input")];
      const email = document.querySelector<HTMLInputElement>('input[type="email"]')!;
      return {
        submitH: Math.round(submit.getBoundingClientRect().height),
        inputHs: inputs.map((i) => Math.round(i.getBoundingClientRect().height)),
        emailFs: getComputedStyle(email).fontSize,
      };
    });
    // h-10 sm:h-11 renders 40 below 640; text-sm sm:text-base renders 14.
    expect(geo.submitH).toBe(40);
    for (const h of geo.inputHs) expect(h).toBe(40);
    expect(geo.emailFs).toBe("14px");
  });

  test("forgot renders the reference's 40px h-10 family at mobile (16px input font)", async ({ page }) => {
    await page.goto("/login");
    await page.getByRole("button", { name: "Forgot password?" }).click();
    await expect(page.getByRole("heading", { name: "Reset your password" })).toBeVisible();
    const geo = await page.evaluate(() => {
      const submit = [...document.querySelectorAll('button[type="submit"]')][0];
      const email = document.querySelector<HTMLInputElement>('input[type="email"]')!;
      return {
        submitH: Math.round(submit.getBoundingClientRect().height),
        inputH: Math.round(email.getBoundingClientRect().height),
        inputFs: getComputedStyle(email).fontSize,
      };
    });
    // h-10 sm:h-11 + text-base md:text-sm: 40px/16px below 640.
    expect(geo.submitH).toBe(40);
    expect(geo.inputH).toBe(40);
    expect(geo.inputFs).toBe("16px");
  });
});

test.describe("auth-form label→input gap (v24 — plan G2)", () => {
  // Desktop viewport (the gap is viewport-invariant — the trap is the v4
  // space-y selector, not a breakpoint): the reference's 10px rect gap =
  // inline label (16px glyph rect inside a 20px line box) + 6px margin on
  // the input's relative wrapper.
  test("the sign-in form's first field renders the reference's 10px label→input gap", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    const gap = await page.evaluate(() => {
      const label = document.querySelector("form label")!;
      const wrap = label.parentElement?.querySelector(":scope > div");
      if (!wrap) return null;
      const lr = label.getBoundingClientRect();
      const wr = wrap.getBoundingClientRect();
      return Math.round(wr.y - (lr.y + lr.height));
    });
    expect(gap).toBe(10);
  });

  test("the sign-up form's fields render the same 10px gap at mobile", async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto("/login");
    await page.getByRole("button", { name: "Need an account? Sign up" }).click();
    await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();
    const gaps = await page.evaluate(() => {
      return [...document.querySelectorAll("form label")]
        .map((label) => {
          const wrap = label.parentElement?.querySelector(":scope > div");
          if (!wrap) return null;
          const lr = label.getBoundingClientRect();
          const wr = wrap.getBoundingClientRect();
          return Math.round(wr.y - (lr.y + lr.height));
        })
        .filter((g) => g !== null);
    });
    expect(gaps.length).toBe(3);
    for (const g of gaps) expect(g).toBe(10);
  });
});

// ---------------------------------------------------------------------------
// v25 — the auth submit ring + the login page's white backdrop
// (docs/remediation-plan-v25.md G1/G3).
//
// Measured live on both sites via REAL Tab presses (kb-auth-ring-v25.sh,
// pointer parked, 350ms settle): the reference's auth submits render
// `box-shadow: #fff 0 0 0 2px, #09090b 0 0 0 4px, rgba(0,0,0,0.05) 0 1px 2px`
// on keyboard focus — the shadcn ring-2/ring-offset-2 family with its
// `--ring` = ZINC-950 #09090b (NOT the inputs' slate-400 #94a3b8 — the
// reference runs the input ring and the button ring as two distinct
// families; the clone had copied the input color onto the button). The
// reference's other focusables: the Google + swap buttons show the
// browser-default auto outline (no custom ring), the inputs the v13
// #94a3b8 family — all already matching.
//
// The reference's <body> styles NO background (class `antialiased` only —
// the browser's white canvas; its warm #fafaf8 paper lives on the
// app-shell wrapper, and its 404 page paints its own #f8fafc root). The
// clone painted #fafaf8 on the body (the v7-era manifest read — a PWA
// splash color, not a rendered surface). VISUALLY invisible (the login
// gradient covers the body), but a real computed-style + layer-structure
// drift: this pin holds the corrected white-canvas body.
test.describe("auth submit ring + login backdrop (v25 — plan G1/G3)", () => {
  test("the submit buttons render the reference's zinc-950 keyboard ring (G1)", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    // focusVisible is a real Chromium FocusOptions member (the v19 dialog
    // probe technique); TS's DOM lib lags it — hence the cast. 350ms settle:
    // the 200ms transition family (the v23 65%-opacity lesson).
    const signin = await page.evaluate(async () => {
      const b = document.querySelector<HTMLButtonElement>("button[type=submit]")!;
      b.focus({ focusVisible: true } as unknown as FocusOptions);
      await new Promise((r) => setTimeout(r, 350));
      return getComputedStyle(b).boxShadow;
    });
    // The reference's composition: white 2px offset + zinc-950 2px ring +
    // the v3 ambient (compared in visible layers; v4's transparent lead
    // layers paint nothing — the v10 lesson).
    expect(signin).toContain("rgb(255, 255, 255) 0px 0px 0px 2px");
    expect(signin).toContain("rgb(9, 9, 11) 0px 0px 0px 4px");
    expect(signin).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // The sign-up state's Create account button — same family (client-side
    // state swap; no register-class API call).
    await page.getByRole("button", { name: "Need an account? Sign up" }).click();
    await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();
    const signup = await page.evaluate(async () => {
      const b = document.querySelector<HTMLButtonElement>("button[type=submit]")!;
      b.focus({ focusVisible: true } as unknown as FocusOptions);
      await new Promise((r) => setTimeout(r, 350));
      return getComputedStyle(b).boxShadow;
    });
    expect(signup).toContain("rgb(255, 255, 255) 0px 0px 0px 2px");
    expect(signup).toContain("rgb(9, 9, 11) 0px 0px 0px 4px");
    expect(signup).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");
  });

  test("the login page's body renders the reference's plain white canvas (G3)", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    const bodyBg = await page.evaluate(() => getComputedStyle(document.body).backgroundColor);
    // The reference styles NO body background — the browser's default white
    // canvas (measured live; its warm #fafaf8 paper lives on the app-shell
    // wrapper — pinned in tokens.spec; the login gradient covers the body,
    // so this is a computed-style pin, byte-identical screenshots).
    expect(bodyBg).toBe("rgb(255, 255, 255)");
  });
});
