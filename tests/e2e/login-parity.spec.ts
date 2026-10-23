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

test.describe("forgot-state focus-walk contract (v34 — plan S1)", () => {
  test("the forgot state renders the reference's focus families + walk contract", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();

    // Enter the forgot state (a STATE on /login — the reference's own
    // register/forgot routes 404; the button swap is the entry).
    await page.getByRole("button", { name: "Forgot password?" }).click();
    await expect(page.getByRole("heading", { name: "Reset your password" })).toBeVisible();

    // (1) NO auto-focus on landing — the reference leaves focus on the
    // body (unlike the verify state's first-box auto-focus, v33 G1).
    //   — the session-69 surface #1, measured live on both sites.
    const landing = await page.evaluate(() => ({
      tag: document.activeElement?.tagName,
      // The card's ONLY focusable app stops, in DOM order.
      census: [...document.querySelectorAll("main button, main input")]
        .filter((e) => e.getClientRects().length > 0)
        .map((e) =>
          e.tagName === "INPUT"
            ? "INPUT:" + (e.getAttribute("type") || "text")
            : "BUTTON:" + (e.textContent?.trim().slice(0, 16) || "?"),
        ),
    }));
    expect(landing.tag).toBe("BODY");
    // Exactly THREE stops: Back to sign in → Email input → Send reset link.
    expect(landing.census).toEqual([
      "BUTTON:Back to sign in",
      "INPUT:email",
      "BUTTON:Send reset link",
    ]);

    // (2) The email input's focus family — the v13 SLATE family (white
    // 2px offset + slate-400 4px ring + the tinted #94a3b8 border). The
    // reference runs the SAME family here as its register inputs (each
    // surface measured separately — the v33 zinc-vs-slate lesson).
    const email = await page.evaluate(async () => {
      const e = document.querySelector<HTMLInputElement>("form input#email")!;
      e.focus();
      await new Promise((r) => setTimeout(r, 350));
      const cs = getComputedStyle(e);
      return { border: cs.borderColor, shadow: cs.boxShadow };
    });
    expect(email.border).toBe("rgb(148, 163, 184)");
    expect(email.shadow).toContain("rgb(255, 255, 255) 0px 0px 0px 2px");
    expect(email.shadow).toContain("rgb(148, 163, 184) 0px 0px 0px 4px");

    // (3) The submit's focus family — the v25 ZINC family (white 2px +
    // zinc-950 4px + the ambient shadow layer), identical to the other
    // auth submits. The ring is focus-VISIBLE-gated: programmatic focus
    // never engages it — a REAL Tab from the email input does (the v25
    // methodology lesson).
    await page.evaluate(() => {
      document.querySelector<HTMLInputElement>("form input#email")!.focus();
    });
    await page.keyboard.press("Tab");
    await page.waitForTimeout(350);
    const submit = await page.evaluate(() => {
      const b = [...document.querySelectorAll("form button[type=submit]")][0];
      const cs = getComputedStyle(b);
      return { shadow: cs.boxShadow, bg: cs.backgroundColor, focused: document.activeElement === b };
    });
    expect(submit.focused).toBe(true);
    expect(submit.bg).toBe("rgb(15, 23, 42)");
    expect(submit.shadow).toContain("rgb(255, 255, 255) 0px 0px 0px 2px");
    expect(submit.shadow).toContain("rgb(9, 9, 11) 0px 0px 0px 4px");
    expect(submit.shadow).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // (4) The Back button stays a RAW button — no focus utilities (the
    // browser-default outline family on both sites). The class attribute
    // is the arbiter (the v27 precedent — computed :focus chrome is
    // focus-path dependent; the classes are the contract).
    const backClasses = await page.evaluate(() => {
      const b = [...document.querySelectorAll("main button")].find((x) =>
        /Back to sign in/.test(x.textContent || ""),
      );
      return (b?.className || "").toString();
    });
    expect(backClasses).not.toMatch(/focus/i);
    expect(backClasses).toContain("text-[#64748b]");
  });
});

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
// The reference's <body> styles NO background (its body carried only
// `antialiased` at v25; the reference has since dropped that class too —
// the v26 G1 pin below — leaving a fully classless white-canvas body; its
// warm #fafaf8 paper lives on the
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

  // v26 — plan G1 (measured live on both sites, three page families, fresh
  // opens): the reference's <body> now carries NO class — the `antialiased`
  // class v25 measured is GONE (a reference-side change; its body class is
  // "" on /login, /, and the 404, -webkit-font-smoothing auto). The clone
  // still rendered className="antialiased". On this Linux Chromium the class
  // renders byte-identically either way (the A/B pixel test in the plan);
  // on macOS it flips text to grayscale AA — the reference's subpixel
  // rendering is the target, so the clone drops the class.
  test("the body carries no class — the reference's classless body (v26 — plan G1)", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();
    const body = await page.evaluate(() => ({
      cls: document.body.className,
      // webkitFontSmoothing is a WebKit-only CSSStyleDeclaration member TS
      // doesn't know — the same cast family as the v25 focusVisible one.
      fs: (getComputedStyle(document.body) as unknown as { webkitFontSmoothing: string })
        .webkitFontSmoothing,
    }));
    expect(body.cls).toBe("");
    expect(body.fs).toBe("auto");
  });
});

// ---------------------------------------------------------------------------
// v45 — the shadow-scale regression pins (plan F4,
// docs/remediation-plan-v45.md).
//
// The v45 sweep census'd every live shadow-* utility on BOTH sites: the
// VISIBLE layers match everywhere (the `--shadow-sm` theme pin is
// load-bearing for the small end — v4 renamed the scale: its native
// shadow-sm = v3's "shadow"; the pin restores v3's 0 1px 2px 0 0.05).
// The md/lg/xl/2xl values were NOT renamed (v4 kept v3's numerics) and
// were UNPINNED — a future Tailwind upgrade changing the scale would
// drift silently. These pins hold the login card's three shadow sites:
// the slate submit button's REST shadow-sm, the panel's shadow-2xl, and
// the Google button's REAL-hover shadow-sm. The assertions use the
// toContain idiom on the visible layers — the accepted-leads convention
// (v4's transparent composition leads paint nothing — the v10 lesson).
test.describe("shadow-scale regression pins (v45 — plan F4)", () => {
  test("the slate button's shadow-sm + the panel's shadow-2xl + the Google button's hover shadow-sm (v45 F4)", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();

    // The slate submit button (Sign in) — its REST shadow-sm: the theme
    // pin's value (guards the --shadow-sm pin against removal/upgrade).
    const slate = await page.evaluate(() => {
      const b = document.querySelector<HTMLButtonElement>("button[type=submit]")!;
      return getComputedStyle(b).boxShadow;
    });
    expect(slate).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");

    // The login panel — shadow-2xl's visible layer (v4 kept v3's
    // 25px 50px -12px @ 0.25; measured identical on both sites).
    const panel = await page.evaluate(() => {
      const p = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && d.className.includes("backdrop-blur") && d.getBoundingClientRect().width > 300,
      );
      return p ? getComputedStyle(p).boxShadow : null;
    });
    expect(panel).not.toBeNull();
    expect(panel).toContain("rgba(0, 0, 0, 0.25) 0px 25px 50px -12px");

    // The Google button — a REAL pointer hover engages its hover:shadow-sm
    // (the visible layer = the same theme-pinned 0 1px 2px 0 0.05; the
    // border/bg hover states were already pinned by the v13 family).
    const google = page.getByRole("button", { name: /Google/i });
    await google.hover();
    await page.waitForTimeout(400);
    const googleHover = await page.evaluate(() => {
      const b = [...document.querySelectorAll("button")].find((x) =>
        /Google/i.test((x.textContent || "").trim()),
      )!;
      return getComputedStyle(b).boxShadow;
    });
    expect(googleHover).toContain("rgba(0, 0, 0, 0.05) 0px 1px 2px 0px");
    expect(googleHover).not.toBe("none");
  });
});

test.describe("login panel mobile census (v49 — plan F1)", () => {
  test.use({ viewport: { width: 390, height: 844 } });

  test("the mobile-only &nbsp; spacer lifts the card stack to the reference's y 57 (v49 F1)", async ({ page }) => {
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();

    // The reference's measured 390 contract (ref-v49.sh, sign-in AND
    // sign-up states): the w-full max-w-md wrapper carries TWO children —
    // the panel (682) + a mobile-only &nbsp; spacer (mt-8, h 16) = 730
    // tall, centered in the 812 inner height → the panel y 57 (24px
    // ABOVE the geometric center the pre-fix clone rendered at y 81).
    const census = await page.evaluate(() => {
      const panel = [...document.querySelectorAll("div")].find(
        (d) =>
          /rounded-2xl/.test(d.className) && d.querySelector("h1"),
      );
      if (!panel) return null;
      const wrapper = panel.parentElement!;
      const spacer = [...wrapper.children].find((c) => c !== panel) as HTMLElement | undefined;
      const pr = panel.getBoundingClientRect();
      const wr = wrapper.getBoundingClientRect();
      const scs = spacer ? getComputedStyle(spacer) : null;
      const sr = spacer ? spacer.getBoundingClientRect() : null;
      const p = spacer?.querySelector("p");
      const main = wrapper.parentElement!;
      const mcs = getComputedStyle(main);
      return {
        main: {
          minH: mcs.minHeight,
          alignItems: mcs.alignItems,
          pad: mcs.padding,
        },
        wrapper: { w: Math.round(wr.width), h: Math.round(wr.height) },
        panel: { y: Math.round(pr.y), h: Math.round(pr.height), w: Math.round(pr.width) },
        spacer: scs
          ? {
              present: true,
              h: Math.round(sr!.height),
              mt: scs.marginTop,
              fs: scs.fontSize,
              color: scs.color,
              ta: scs.textAlign,
              display: scs.display,
              text: p ? p.textContent : null,
            }
          : { present: false },
      };
    });
    expect(census).not.toBeNull();
    // The root contract (both sites): the centered flex main with p-4.
    expect(census!.main).toEqual({
      minH: "844px",
      alignItems: "center",
      pad: "16px",
    });
    // THE v49 F1 FIX: the wrapper is 730 (682 + 32 + 16), NOT the
    // pre-fix 682 — the spacer is what the reference renders.
    expect(census!.wrapper.h).toBe(730);
    expect(census!.panel.h).toBe(682);
    expect(census!.panel.w).toBe(358);
    // The panel sits at the reference's y 57 — NOT the pre-fix 81.
    expect(census!.panel.y).toBe(57);
    // The spacer census (the reference's mt-8 text-center text-xs
    // text-slate-400 sm:hidden with a bare &nbsp;): the color pinned as
    // the #94a3b8 hex (Tailwind v4's named slate computes as oklab() —
    // the v7 login-family rule; the content is invisible anyway).
    expect(census!.spacer).toEqual({
      present: true,
      h: 16,
      mt: "32px",
      fs: "12px",
      color: "rgb(148, 163, 184)",
      ta: "center",
      display: "block",
      text: "\u00A0",
    });

    // The sm:hidden contract (re-verified live on the reference): at
    // 640 the spacer is display none and the panel re-centers — every
    // desktop pin (v12/v13) is unchanged by the fix.
    await page.setViewportSize({ width: 640, height: 960 });
    await page.waitForTimeout(300);
    const at640 = await page.evaluate(() => {
      const panel = [...document.querySelectorAll("div")].find(
        (d) => /rounded-2xl/.test(d.className) && d.querySelector("h1"),
      );
      if (!panel) return null;
      const wrapper = panel.parentElement!;
      const spacer = [...wrapper.children].find((c) => c !== panel) as HTMLElement | undefined;
      const pr = panel.getBoundingClientRect();
      return {
        spacerDisplay: spacer ? getComputedStyle(spacer).display : "absent",
        panelY: Math.round(pr.y),
        panelH: Math.round(pr.height),
        centeredY: Math.round((960 - pr.height) / 2),
      };
    });
    expect(at640).not.toBeNull();
    expect(at640!.spacerDisplay).toBe("none");
    expect(at640!.panelY).toBe(at640!.centeredY);
  });
});

// ---------------------------------------------------------------------------
// v50 — plan F1 (docs/remediation-plan-v50.md): the auth-MODE panels' 16px
// shortfall. The reference's sign-up/forgot containers run v3-era space-y
// semantics (margin-top on `> * + *`), so the back button's OWN `-mb-2`
// (-8px) STACKS with the heading's mt 16 (collapsed net gap 8px). The
// clone's v4 space-y emits zero-specificity margin-block-end on
// `:not(:last-child)` — the `-mb-2` utility OVERRIDES the container gap
// (the heading overlaps the button by 8px, the panel 16px short at every
// viewport). The fix: the scoped `.zb-auth-mode` restore (the v9 G3 /
// v24 G2 SPACE-Y V3 SEMANTICS family's third member) + the forgot
// container's sm tier (the reference's `space-y-4 sm:space-y-6` — 24px
// at >=640). Measured live on the reference at 390x844 (ref-v50.sh):
//   sign-up:  the wrapper 470 / the panel 422 / y 187 (the centered stack)
//   forgot:   the wrapper 358 / the panel 310 / y 243
//   the junction: the button (h 20) -> the heading at +28 (net gap 8),
//   the heading -> the form +16 (the form heights IDENTICAL: 286 / 126).
// ---------------------------------------------------------------------------
test.describe("auth-mode panel census (v50 — plan F1)", () => {
  test.use({ viewport: { width: 390, height: 844 } });

  test("the sign-up panel renders the reference's 422 stack (the v4 space-y × -mb-2 fix)", async ({ page }) => {
    await page.goto("/login");
    await page.getByRole("button", { name: "Need an account? Sign up" }).click();
    await expect(page.getByRole("heading", { name: "Create your account" })).toBeVisible();

    const census = await page.evaluate(() => {
      const wrapper = [...document.querySelectorAll("div")].find((d) =>
        (d.className || "").toString().includes("max-w-md"),
      );
      if (!wrapper) return null;
      const panel = wrapper.firstElementChild as HTMLElement;
      const pr = panel.getBoundingClientRect();
      const wr = wrapper.getBoundingClientRect();
      // the mode stack: the back button + the heading + the form
      const content = [...panel.querySelectorAll("div")].find(
        (d) => parseFloat(getComputedStyle(d).paddingTop) > 0 && d.querySelector("form"),
      );
      // the mode stack: the container whose DIRECT children are the back
      // button + the heading (h2) + the form — walk down the single-child
      // chain from the content block (an ancestor-match finder would
      // return the content div itself).
      const stack = (() => {
        if (!content) return null;
        let node: Element | null = content;
        for (let i = 0; i < 6 && node; i++) {
          const btn = [...node.children].find((c) => c.tagName === "BUTTON" && /back/i.test(c.textContent || ""));
          const form = [...node.children].find((c) => c.tagName === "FORM");
          // the heading child: a direct h2 (sign-up) or a wrapping div
          // carrying the h2 (forgot: h2 + the description p).
          const heading = [...node.children].find((c) =>
            c.tagName === "H2" || (c.querySelector && c.querySelector("h2")),
          );
          if (btn && form && heading) return node as HTMLElement;
          node = node.firstElementChild;
        }
        return null;
      })();
      const kids = stack ? [...stack.children].map((c) => {
        const el = c as HTMLElement;
        const cs = getComputedStyle(el);
        return {
          tag: el.tagName,
          h: Math.round(el.getBoundingClientRect().height),
          y: Math.round(el.getBoundingClientRect().y - (stack as HTMLElement).getBoundingClientRect().y),
          mt: cs.marginTop,
          mb: cs.marginBottom,
        };
      }) : [];
      return {
        wrapperH: Math.round(wr.height),
        panel: { w: Math.round(pr.width), h: Math.round(pr.height), y: Math.round(pr.y) },
        stackH: stack ? Math.round(stack.getBoundingClientRect().height) : null,
        kids,
      };
    });
    expect(census).not.toBeNull();
    // THE v50 F1 FIX: the panel is 422 (NOT the pre-fix 406 — the v4
    // space-y margin-block-end override left it 16px short), the wrapper
    // 470 (422 + the spacer's mt 32 + h 16), the panel y 187 (the
    // reference's centered stack).
    expect(census!.wrapperH).toBe(470);
    expect(census!.panel.h).toBe(422);
    expect(census!.panel.w).toBe(358);
    expect(census!.panel.y).toBe(187);
    // The junction contract: the button h 20 (y 0), the heading at y 28
    // (the net gap 8 — the -mb-2 stacked with the v3-style mt, NOT the
    // pre-fix overlap at y 12), the form at heading.y + 28 + 16.
    expect(census!.kids).toHaveLength(3);
    expect(census!.kids[0]).toMatchObject({ tag: "BUTTON", h: 20, y: 0, mb: "-8px" });
    expect(census!.kids[1]).toMatchObject({ tag: "H2", h: 28, y: 28 });
    expect(census!.kids[2]).toMatchObject({ tag: "FORM", y: 72 });
  });

  test("the forgot panel renders the reference's 310 stack + the sm:space-y-6 tier at 640", async ({ page }) => {
    await page.goto("/login");
    await page.getByRole("button", { name: "Forgot password?" }).click();
    await expect(page.getByRole("heading", { name: "Reset your password" })).toBeVisible();

    const census = await page.evaluate(() => {
      const wrapper = [...document.querySelectorAll("div")].find((d) =>
        (d.className || "").toString().includes("max-w-md"),
      );
      if (!wrapper) return null;
      const panel = wrapper.firstElementChild as HTMLElement;
      const pr = panel.getBoundingClientRect();
      const wr = wrapper.getBoundingClientRect();
      const content = [...panel.querySelectorAll("div")].find(
        (d) => parseFloat(getComputedStyle(d).paddingTop) > 0 && d.querySelector("form"),
      );
      // the mode stack: the container whose DIRECT children are the back
      // button + the heading (h2) + the form — walk down the single-child
      // chain from the content block (an ancestor-match finder would
      // return the content div itself).
      const stack = (() => {
        if (!content) return null;
        let node: Element | null = content;
        for (let i = 0; i < 6 && node; i++) {
          const btn = [...node.children].find((c) => c.tagName === "BUTTON" && /back/i.test(c.textContent || ""));
          const form = [...node.children].find((c) => c.tagName === "FORM");
          // the heading child: a direct h2 (sign-up) or a wrapping div
          // carrying the h2 (forgot: h2 + the description p).
          const heading = [...node.children].find((c) =>
            c.tagName === "H2" || (c.querySelector && c.querySelector("h2")),
          );
          if (btn && form && heading) return node as HTMLElement;
          node = node.firstElementChild;
        }
        return null;
      })();
      const kids = stack ? [...stack.children].map((c) => {
        const el = c as HTMLElement;
        return {
          tag: el.tagName,
          h: Math.round(el.getBoundingClientRect().height),
          y: Math.round(el.getBoundingClientRect().y - (stack as HTMLElement).getBoundingClientRect().y),
          mt: getComputedStyle(el).marginTop,
        };
      }) : [];
      return {
        wrapperH: Math.round(wr.height),
        panel: { w: Math.round(pr.width), h: Math.round(pr.height), y: Math.round(pr.y) },
        kids,
      };
    });
    expect(census).not.toBeNull();
    // THE v50 F1 FIX: the forgot panel is 310 (NOT the pre-fix 294),
    // the wrapper 358, the panel y 243.
    expect(census!.wrapperH).toBe(358);
    expect(census!.panel.h).toBe(310);
    expect(census!.panel.w).toBe(358);
    expect(census!.panel.y).toBe(243);
    expect(census!.kids).toHaveLength(3);
    // The heading block (h2 + the description p) h 76 at y 28 (the net
    // gap 8); the form at y 120 (28 + 76 + 16).
    expect(census!.kids[1]).toMatchObject({ h: 76, y: 28 });
    expect(census!.kids[2]).toMatchObject({ tag: "FORM", y: 120 });

    // The sm tier (the reference's `space-y-4 sm:space-y-6`): at 640 the
    // heading block's margin-top is 24px (NOT the sign-up's 16).
    await page.setViewportSize({ width: 640, height: 960 });
    await page.waitForTimeout(300);
    const at640 = await page.evaluate(() => {
      const wrapper = [...document.querySelectorAll("div")].find((d) =>
        (d.className || "").toString().includes("max-w-md"),
      );
      if (!wrapper) return null;
      const panel = wrapper.firstElementChild as HTMLElement;
      const content = [...panel.querySelectorAll("div")].find(
        (d) => parseFloat(getComputedStyle(d).paddingTop) > 0 && d.querySelector("form"),
      );
      // the mode stack: the container whose DIRECT children are the back
      // button + the heading (h2) + the form — walk down the single-child
      // chain from the content block (an ancestor-match finder would
      // return the content div itself).
      const stack = (() => {
        if (!content) return null;
        let node: Element | null = content;
        for (let i = 0; i < 6 && node; i++) {
          const btn = [...node.children].find((c) => c.tagName === "BUTTON" && /back/i.test(c.textContent || ""));
          const form = [...node.children].find((c) => c.tagName === "FORM");
          // the heading child: a direct h2 (sign-up) or a wrapping div
          // carrying the h2 (forgot: h2 + the description p).
          const heading = [...node.children].find((c) =>
            c.tagName === "H2" || (c.querySelector && c.querySelector("h2")),
          );
          if (btn && form && heading) return node as HTMLElement;
          node = node.firstElementChild;
        }
        return null;
      })();
      if (!stack) return null;
      const heading = stack.children[1] as HTMLElement;
      return { headingMt: getComputedStyle(heading).marginTop };
    });
    expect(at640).not.toBeNull();
    expect(at640!.headingMt).toBe("24px");
  });
});

// ---------------------------------------------------------------------------
// v75 — the login card's geometry + typography census at 1280
// (docs/remediation-plan-v75.md F4). The v59-era login pair's second
// re-run (vlm-compare-v75.mjs: VERDICT IDENTICAL, zero style flags) with
// the both-sides DOM census (arbit-v75.sh + login-census-ref-v75.sh):
// byte-identical on every axis. The v7 G2/G3 pins lock this surface's
// COLORS (the slate family, the card bg, the bar/page gradients, the
// submit bg/color/h, the email border/bg) and the v9 pins its per-state
// control heights — the card's WIDTH + RADIUS, the h1's TYPOGRAPHY
// family (fs/fw/lh — only its color was pinned), the subtitle's fs, the
// Sign in button's FULL chrome (w/radius/fs/fw), the logo's geometry,
// and the input radius/fs family at desktop were never pinned. This pin
// locks the arbitration's own measured values — the pin-only line
// continues (no production-code change).
test.describe("login card geometry + typography census at 1280 (v75 — plan F4)", () => {
  test("the card + h1 + subtitle + inputs + signIn + logo chrome (v75 F4)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();

    const census = await page.evaluate(() => {
      // The card: the rounded-2xl container holding the h1 (the v7 pin's
      // own finder — the inline rgba(255,255,255,0.95) background).
      const card = [...document.querySelectorAll("div")].find(
        (d) => typeof d.className === "string" && /rounded-2xl/.test(d.className) && d.querySelector("h1"),
      );
      const h1 = document.querySelector("h1");
      const sub = [...document.querySelectorAll("p")].find((p) =>
        /Sign in to continue/.test(p.textContent || ""),
      );
      const form = document.querySelector("form");
      const em = form?.querySelector<HTMLInputElement>('input[type="email"]');
      const pw = form?.querySelector<HTMLInputElement>('input[type="password"]');
      const signIn = form?.querySelector<HTMLButtonElement>('button[type="submit"]');
      const logo = document.querySelector("img");
      const inputCensus = (i: HTMLInputElement | null | undefined) => {
        if (!i) return null;
        const cs = getComputedStyle(i);
        const r = i.getBoundingClientRect();
        return {
          h: Math.round(r.height),
          radius: cs.borderRadius,
          fs: cs.fontSize,
          border: `${cs.borderTopWidth} ${cs.borderTopColor}`,
        };
      };
      const btnCs = signIn ? getComputedStyle(signIn) : null;
      const btnR = signIn ? signIn.getBoundingClientRect() : null;
      return {
        card: card
          ? {
              w: Math.round(card.getBoundingClientRect().width),
              radius: getComputedStyle(card).borderRadius,
              bg: getComputedStyle(card).backgroundColor,
            }
          : null,
        h1: h1
          ? {
              fs: getComputedStyle(h1).fontSize,
              fw: getComputedStyle(h1).fontWeight,
              lh: getComputedStyle(h1).lineHeight,
              color: getComputedStyle(h1).color,
            }
          : null,
        subtitle: sub
          ? {
              fs: getComputedStyle(sub).fontSize,
              color: getComputedStyle(sub).color,
            }
          : null,
        emailInput: inputCensus(em),
        pwInput: inputCensus(pw),
        signIn: signIn && btnCs && btnR
          ? {
              w: Math.round(btnR.width),
              h: Math.round(btnR.height),
              radius: btnCs.borderRadius,
              fs: btnCs.fontSize,
              fw: btnCs.fontWeight,
              bg: btnCs.backgroundColor,
              color: btnCs.color,
            }
          : null,
        logo: logo
          ? {
              w: Math.round(logo.getBoundingClientRect().width),
              h: Math.round(logo.getBoundingClientRect().height),
              alt: (logo.getAttribute("alt") || "").slice(0, 20),
            }
          : null,
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();

    // The card's geometry: the max-w-md wrapper (448) + rounded-2xl (16px)
    // + the inline white/95 background — byte-identical on both sides.
    expect(census!.card).toEqual({
      w: 448,
      radius: "16px",
      bg: "rgba(255, 255, 255, 0.95)",
    });
    // The h1's typography family (the sm:text-3xl state — 30/700/36) —
    // the color was v7-pinned, the fs/fw/lh never were.
    expect(census!.h1).toEqual({
      fs: "30px",
      fw: "700",
      lh: "36px",
      color: "rgb(15, 23, 42)",
    });
    // The subtitle: 16px slate-500 (the color v7-pinned, the fs never).
    expect(census!.subtitle).toEqual({
      fs: "16px",
      color: "rgb(100, 116, 139)",
    });
    // The input pair: 48px controls, rounded-xl (12px), 14px text, the
    // v7-pinned slate-200 border.
    expect(census!.emailInput).toEqual({
      h: 48,
      radius: "12px",
      fs: "14px",
      border: "1px rgb(226, 232, 240)",
    });
    expect(census!.pwInput).toEqual({
      h: 48,
      radius: "12px",
      fs: "14px",
      border: "1px rgb(226, 232, 240)",
    });
    // The Sign in button's full chrome: the content width 448 − 2×40
    // (md:px-10) = 368, h 48, rounded-xl, 14px/500, solid slate-900.
    expect(census!.signIn).toEqual({
      w: 368,
      h: 48,
      radius: "12px",
      fs: "14px",
      fw: "500",
      bg: "rgb(15, 23, 42)",
      color: "rgb(255, 255, 255)",
    });
    // The logo image: 96x96 (the sm:h-24 sm:w-24 state), the alt text.
    expect(census!.logo).toEqual({
      w: 96,
      h: 96,
      alt: "ZeroBudget logo",
    });
    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);
  });
});

// ---------------------------------------------------------------------------
// v99 — plan F4 (docs/remediation-plan-v99.md): the login card's
// SOCIAL-LOGIN ROW census at 1280x800 — the never-pinned family. The v75
// F4 pin walked the card/h1/subtitle/inputs/signIn/logo; the v7 G3 pin
// holds the Google button's COLORS and the v45 F4 pin its HOVER shadow;
// the auth.spec pins hold the OR divider's PRESENCE per state — but the
// OR divider's computed chrome (the "or" text's typography + tracking +
// padding + the rule line) and the Google button's GEOMETRY/typography
// (w/h/radius/fs/lh/pad/gap + the svg glyph) were never pinned at ANY
// viewport in ANY spec.
//
// Measured live on BOTH sites (social-arbit-v99.sh + social-clone-v99.sh
// via build-social-v99.py — the census JS byte-identical across the
// halves, the md5 line-block contract d7add89b; the logged-out /login
// surface needs no session — READ-ONLY passive navigation):
//   the google button: {w 368, h 54, radius 12px, fs 16px, fw 500,
//             lh 24px, color rgb(51,65,85), bg white,
//             border 1px rgb(226,232,240), pad 14px 20px, gap 12px,
//             svg 20x20} — the w-full content row (448 − 2×40 md:px-10)
//             + the py-3.5/px-5 + text-[16px]/font-medium family
//   the "or" text: {fs 12px, fw 500, color rgb(100,116,139), lh 16px,
//             uppercase, ls 0.6px, pad 0px 12px, bg white, h 16, w 43}
//   the rule: exactly ONE hairline {h 1px, bg rgb(226,232,240), w 368}
//             (DIV on the reference, SPAN on the clone — the inert tag
//             construct class; the pin asserts chrome + count, not tag)
//   the rhythm: the OR-text center 32px below the google bottom (the
//             my-6 margin + the 16px row's half)
// Every axis is DATA-INDEPENDENT (the static logged-out surface) — the
// v98 data-independent-panel strength class: the census values assert
// directly.
// ---------------------------------------------------------------------------
test.describe("login social-row census at 1280 (v99 — plan F4)", () => {
  test("the OR divider + the Google button + the row rhythm (the never-pinned family)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();

    const census = await page.evaluate(() => {
      // The finders modeled on the v99 arbitration's own census
      // (social-arbit-v99.sh / social-clone-v99.sh).
      const form = document.querySelector("form");
      if (!form) return null;
      let card: HTMLElement | null = form;
      while (card && card !== document.body) {
        const c = getComputedStyle(card);
        if (
          parseFloat(c.borderRadius) > 8 &&
          c.backgroundColor !== "rgba(0, 0, 0, 0)" &&
          card.getBoundingClientRect().width > 300 &&
          card.getBoundingClientRect().width < 700
        )
          break;
        card = card.parentElement;
      }
      if (!card || card === document.body) return null;
      // THE GOOGLE BUTTON (the card's only Google-texted button).
      const g = [...card.querySelectorAll("button")].find((b) =>
        /Continue with Google/i.test(b.textContent || ""),
      );
      if (!g) return null;
      const gs = getComputedStyle(g);
      const gr = g.getBoundingClientRect();
      const svg = g.querySelector("svg");
      const sr = svg ? svg.getBoundingClientRect() : null;
      // THE OR DIVIDER TEXT: any leaf element whose trimmed text is "or".
      const orEl = [...card.querySelectorAll("span,p,div,h1,h2,h3,h4,button")]
        .filter((e) => e.children.length === 0)
        .find((e) => /^or$/i.test((e.textContent || "").trim()));
      if (!orEl) return null;
      const os = getComputedStyle(orEl);
      const orr = orEl.getBoundingClientRect();
      // THE RULE LINES: every element <= 2px tall, wider than 150px, with
      // a non-transparent bg, inside the card.
      const rules = [...card.querySelectorAll("*")]
        .filter((e) => {
          const r = e.getBoundingClientRect();
          const s = getComputedStyle(e);
          return r.width > 150 && r.height > 0 && r.height <= 2 && s.backgroundColor !== "rgba(0, 0, 0, 0)";
        })
        .map((e) => {
          const s = getComputedStyle(e);
          const r = e.getBoundingClientRect();
          return { h: s.height, bg: s.backgroundColor, w: Math.round(r.width) };
        });
      return {
        google: {
          w: Math.round(gr.width),
          h: Math.round(gr.height),
          radius: gs.borderRadius,
          fs: gs.fontSize,
          fw: gs.fontWeight,
          lh: gs.lineHeight,
          color: gs.color,
          bg: gs.backgroundColor,
          border: gs.borderTopWidth + " " + gs.borderTopColor,
          pad: gs.padding,
          gap: gs.columnGap,
          svgW: sr ? Math.round(sr.width) : 0,
          svgH: sr ? Math.round(sr.height) : 0,
        },
        orText: {
          fs: os.fontSize,
          fw: os.fontWeight,
          color: os.color,
          lh: os.lineHeight,
          tt: os.textTransform,
          ls: os.letterSpacing,
          pad: os.padding,
          bg: os.backgroundColor,
          h: Math.round(orr.height),
          w: Math.round(orr.width),
        },
        rules,
        rhythm: Math.round(orr.y + orr.height / 2 - gr.bottom),
        docSW: document.documentElement.scrollWidth,
      };
    });
    expect(census).not.toBeNull();
    // The Google button's full resting chrome — the geometry/typography
    // axes the v7 G3 (colors) + v45 F4 (hover shadow) pins never held.
    expect(census!.google).toEqual({
      w: 368,
      h: 54,
      radius: "12px",
      fs: "16px",
      fw: "500",
      lh: "24px",
      color: "rgb(51, 65, 85)",
      bg: "rgb(255, 255, 255)",
      border: "1px rgb(226, 232, 240)",
      pad: "14px 20px",
      gap: "12px",
      svgW: 20,
      svgH: 20,
    });
    // The "or" text — the divider's computed chrome (never pinned before
    // in any spec, any viewport).
    expect(census!.orText).toEqual({
      fs: "12px",
      fw: "500",
      color: "rgb(100, 116, 139)",
      lh: "16px",
      tt: "uppercase",
      ls: "0.6px",
      pad: "0px 12px",
      bg: "rgb(255, 255, 255)",
      h: 16,
      w: 43,
    });
    // The rule line: exactly ONE hairline, the slate-200 1px full row.
    expect(census!.rules).toEqual([{ h: "1px", bg: "rgb(226, 232, 240)", w: 368 }]);
    // The rhythm: the OR-text center 32px below the google bottom (the
    // my-6 24px margin + the 16px row's half).
    expect(census!.rhythm).toBe(32);
    // The no-overflow guard on the same surface.
    expect(census!.docSW).toBe(1280);
  });
});

test.describe("login auth-mode action row census at 1280 (v105 — plan F4)", () => {
  test("the action row + the forgot context + the signup-side button + the emphasis span (the never-pinned family)", async ({ page }) => {
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto("/login");
    await expect(page.getByRole("heading", { name: "Welcome to ZeroBudget" })).toBeVisible();

    const census = await page.evaluate(() => {
      // The finders modeled on the v105 arbitration's own one-shot
      // census (moderow-arbit-v105.sh). The mode switchers are BUTTONS
      // on both sides — never a[href] (the v105 finder lesson).
      const form = document.querySelector("form");
      if (!form) return null;
      const forgot = [...form.querySelectorAll("button")].find((b) =>
        /Forgot password\?/i.test((b.textContent || "").trim()),
      );
      const signup = [...form.querySelectorAll("button")].find((b) =>
        /Need an account\?/i.test((b.textContent || "").trim()),
      );
      if (!forgot || !signup) return null;
      // The ROW: the buttons' common ancestor (the walk-up finder).
      let row: HTMLElement | null = forgot.parentElement;
      while (row && row !== document.body && !row.contains(signup)) row = row.parentElement;
      if (!row || row === document.body) return null;
      const rcs = getComputedStyle(row);
      const fcs = getComputedStyle(forgot);
      const scs = getComputedStyle(signup);
      const span = signup.querySelector("span");
      const spcs = span ? getComputedStyle(span) : null;
      return {
        row: {
          display: rcs.display,
          align: rcs.alignItems,
          justify: rcs.justifyContent,
          gap: rcs.gap,
          w: Math.round(row.getBoundingClientRect().width),
          h: Math.round(row.getBoundingClientRect().height),
        },
        forgot: {
          text: (forgot.textContent || "").trim().slice(0, 24),
          fs: fcs.fontSize,
          lh: fcs.lineHeight,
          fw: fcs.fontWeight,
          color: fcs.color,
          h: Math.round(forgot.getBoundingClientRect().height),
        },
        signup: {
          text: (signup.textContent || "").trim().slice(0, 32),
          fs: scs.fontSize,
          lh: scs.lineHeight,
          fw: scs.fontWeight,
          color: scs.color,
          h: Math.round(signup.getBoundingClientRect().height),
        },
        span: span
          ? {
              text: (span.textContent || "").trim().slice(0, 16),
              fs: spcs!.fontSize,
              fw: spcs!.fontWeight,
              color: spcs!.color,
            }
          : null,
      };
    });
    expect(census).not.toBeNull();
    // The action row's flex chrome (the sm:flex-row sm:gap-0 state at
    // 1280) — never pinned at ANY viewport in ANY spec before v105.
    expect(census!.row).toEqual({
      display: "flex",
      align: "center",
      justify: "space-between",
      gap: "0px",
      w: 368,
      h: 20,
    });
    // The forgot-side context controls — the v7 {fs, lh, h, color} set
    // re-walked + the NEW fw axis.
    expect(census!.forgot).toEqual({
      text: "Forgot password?",
      fs: "14px",
      lh: "20px",
      fw: "500",
      color: "rgb(100, 116, 139)",
      h: 20,
    });
    // The signup-side button — the family's primary target: its computed
    // chrome was never asserted anywhere despite 8+ click usages.
    expect(census!.signup).toEqual({
      text: "Need an account? Sign up",
      fs: "14px",
      lh: "20px",
      fw: "400",
      color: "rgb(100, 116, 139)",
      h: 20,
    });
    // The "Sign up" emphasis span (font-medium text-[#334155]).
    expect(census!.span).toEqual({
      text: "Sign up",
      fs: "14px",
      fw: "500",
      color: "rgb(51, 65, 85)",
    });
  });
});
