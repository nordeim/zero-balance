"use client";

// The /login auth card — sign in / sign up / forgot password states on the
// slate gradient page. Visual chrome mirrors the reference per state:
// sign-in keeps the logo + Google + OR block; sign-up/forgot carry a
// left-aligned "← Back to sign in" button at the TOP, an H2 heading, NO
// logo, NO Google, NO OR divider (remediation-plan-v3 F5). "Continue with
// Google" renders for parity and degrades to an explanatory toast (no OAuth
// credentials in a self-hosted clone). ?from_url= return handling included.

import * as React from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { ArrowLeftIcon, Loader2Icon, LockIcon, MailIcon, ShieldCheckIcon } from "lucide-react";
import { useToast } from "@/components/ui/toast";
import { messageOf, useBudgetStore } from "./store";

// Parity pins (docs/remediation-plan-v7.md G2): the login page is a measured
// parity surface, and Tailwind v4 computes every NAMED slate class in Lab
// color space while the reference emits plain rgb/rgba. All slate values
// below are arbitrary-hex pins of the reference's computed styles:
//   900 #0f172a · 800 #1e293b · 700 #334155 · 600 #475569 · 500 #64748b
//   400 #94a3b8 · 300 #cbd5e1 · 200 #e2e8f0 · 50 #f8fafc
// (Applied as literal class hexes / inline styles — Tailwind's scanner
// reads source text, so classes must never interpolate variables.)

type Mode = "signin" | "signup" | "forgot" | "verify";

const GOOGLE_SVG = (
  <svg className="h-5 w-5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path
      d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"
      fill="#4285F4"
    />
    <path
      d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"
      fill="#34A853"
    />
    <path
      d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"
      fill="#FBBC05"
    />
    <path
      d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"
      fill="#EA4335"
    />
  </svg>
);

function LogoMark() {
  return (
    <div className="group relative">
      <div
        className="absolute inset-0 rounded-[9999px] opacity-30 blur-xl transition-opacity duration-300 group-hover:opacity-40"
        style={{
          background: "linear-gradient(to bottom right, #e2e8f0, #cbd5e1)",
        }}
      />
      {/* The 4px white/50 halo (plan v7 G3) as a sibling layer: v4's
          ring-white/50 computes it in oklab, and inlining boxShadow on the
          span itself would override its shadow-lg / group-hover:shadow-xl. */}
      <div
        className="zb-logo-ring absolute inset-0 rounded-[9999px]"
        style={{ boxShadow: "0 0 0 4px rgba(255, 255, 255, 0.5)" }}
      />
      <span className="relative flex h-20 w-20 shrink-0 overflow-hidden rounded-[9999px] shadow-lg transition-all duration-300 group-hover:shadow-xl sm:h-24 sm:w-24">
        <img
          src="/zerobalance-logo.png"
          alt="ZeroBudget logo"
          className="aspect-square h-full w-full object-cover"
        />
      </span>
    </div>
  );
}

/** v21 G3 — the verify-email state's six single-digit code inputs (measured
 *  live on the reference): each 40×44 (`w-10 h-11`), radius 8 (`rounded-lg`),
 *  border `#e4e4e7`, white bg, 14px/600 centered digits, `inputmode=numeric`,
 *  in a `flex items-center justify-center gap-1.5` row. Typing a digit
 *  advances; Backspace on an empty cell steps back. */
function CodeInputs({
  digits,
  onSetDigit,
  disabled,
}: {
  digits: string[];
  onSetDigit: (index: number, value: string) => void;
  disabled?: boolean;
}) {
  const refs = React.useRef<(HTMLInputElement | null)[]>([]);
  const focusAt = (i: number) => {
    const el = refs.current[Math.max(0, Math.min(5, i))];
    el?.focus();
  };
  return (
    <div className="flex items-center justify-center gap-1.5">
      {digits.map((d, i) => (
        <input
          key={i}
          ref={(el) => {
            refs.current[i] = el;
          }}
          type="text"
          inputMode="numeric"
          // v26 — plan G2 (measured live): the reference runs
          // autocomplete="one-time-code" on the FIRST box only and "off"
          // on the rest (the standard OTP convention — the browser's
          // code offer targets the first box). The clone had it on all
          // six, making every box an autofill target.
          autoComplete={i === 0 ? "one-time-code" : "off"}
          aria-label={`Digit ${i + 1}`}
          value={d}
          disabled={disabled}
          onChange={(e) => {
            const v = e.target.value.replace(/\D/g, "");
            if (!v) {
              onSetDigit(i, "");
              return;
            }
            // Land the (last typed) digit, then advance.
            onSetDigit(i, v.slice(-1));
            if (i < 5) focusAt(i + 1);
          }}
          onKeyDown={(e) => {
            if (e.key === "Backspace" && !digits[i] && i > 0) {
              e.preventDefault();
              onSetDigit(i - 1, "");
              focusAt(i - 1);
            }
            if (e.key === "ArrowLeft" && i > 0) focusAt(i - 1);
            if (e.key === "ArrowRight" && i < 5) focusAt(i + 1);
          }}
          onPaste={(e) => {
            e.preventDefault();
            const pasted = e.clipboardData.getData("text").replace(/\D/g, "").slice(0, 6);
            if (!pasted) return;
            pasted.split("").forEach((ch, j) => {
              if (i + j <= 5) onSetDigit(i + j, ch);
            });
            focusAt(Math.min(5, i + pasted.length));
          }}
          className="h-11 w-10 rounded-lg border border-[#e4e4e7] bg-white text-center text-sm font-semibold text-[#0f172a] transition-colors focus:border-[#94a3b8] focus:outline-none disabled:cursor-not-allowed disabled:opacity-50 sm:h-11"
        />
      ))}
    </div>
  );
}

/** Sign-in-only Google button + OR divider (reference keeps these OFF the
 * sign-up/forgot states). Degrades to an explanatory toast — no OAuth
 * credentials in a self-hosted clone. */
function GoogleBlock({ onUnavailable }: { onUnavailable: () => void }) {
  return (
    <>
      <div className="space-y-3">
        <button
          type="button"
          className="group flex w-full items-center justify-center gap-3 rounded-xl border border-[#e2e8f0] bg-white px-5 py-3.5 font-medium text-[16px] text-[#334155] transition-all duration-200 hover:border-[#cbd5e1] hover:bg-[#f8fafc] hover:shadow-sm"
          onClick={onUnavailable}
        >
          <span className="-ml-4 transition-transform duration-200">
            {GOOGLE_SVG}
          </span>
          Continue with Google
        </button>
      </div>

      <div className="relative my-6">
        <div className="absolute inset-0 flex items-center">
          <span className="h-px w-full bg-[#e2e8f0]" aria-hidden="true" />
        </div>
        <div className="relative flex justify-center text-xs uppercase">
          <span
            className="bg-white px-3 font-medium tracking-wider"
            style={{ color: "#64748b" }}
          >
            or
          </span>
        </div>
      </div>
    </>
  );
}

// NOTE: literal hexes, not template interpolation — Tailwind's scanner
// reads source text; a `border-[${VAR}]` class would never be generated.
// Base input chrome (plan v9 G7 + v24 G1): the reference runs THREE
// distinct responsive families across its auth forms (measured live on
// its DOM at 390×844 and 1280×800, the class list as tie-breaker) —
//   sign-in  h-11 sm:h-12 (44/48) · text-base md:text-sm (16/14)
//   sign-up  h-10 sm:h-11 (40/44) · text-sm sm:text-base md:text-sm
//            (14 mobile, 16 in the 640–768 band, 14 at ≥768)
//   forgot   h-10 sm:h-11 (40/44) · text-base md:text-sm (16/14)
// Height/font tokens live in the per-mode branches below; this constant
// carries only the viewport-invariant chrome.
// v13 G3 (measured live on the reference): on :focus the inputs render the
// shadcn two-layer ring — white 0 0 0 2px + slate-400 0 0 0 4px — on top of
// the slate-400 border. v4's color-only ring utility emits NO shadow without
// a width class, so the ring is an arbitrary box-shadow (hex = the exact
// measured rgb values; v3's trailing transparent layer paints nothing).
const INPUT_CLS =
  "flex w-full rounded-xl border border-[#e2e8f0] bg-[rgba(248,250,252,0.5)] px-3 py-2 pl-10 text-[#09090b] transition-colors placeholder:text-[#475569] focus:border-[#94a3b8] focus:shadow-[0_0_0_2px_#fff,0_0_0_4px_#94a3b8] focus:outline-none disabled:cursor-not-allowed disabled:opacity-50";
const LABEL_CLS = "text-sm font-medium text-[#334155] peer-disabled:cursor-not-allowed peer-disabled:opacity-70";

interface AuthFormProps {
  mode: Mode;
  email: string;
  password: string;
  confirm: string;
  busy: boolean;
  error: string | null;
  onEmail: (v: string) => void;
  onPassword: (v: string) => void;
  onConfirm: (v: string) => void;
  onSubmit: (e: React.FormEvent) => void;
  onForgot: () => void;
  onSignUp: () => void;
}

/** The email/password/(confirm) form + submit. Sign-in keeps the footer
 * switchers (Forgot / Sign up); sign-up/forgot carry their own top back
 * button instead (reference structure). Spacing follows the reference:
 * sign-up form space-y-3 sm:space-y-4, others space-y-4 sm:space-y-5. */
function AuthForm(p: AuthFormProps) {
  // Reference per-state geometry (plan v9 G7 + v24 G1, measured live): the
  // height/font families are per-mode — sign-in h-11 sm:h-12 (48 at ≥640);
  // sign-up/forgot h-10 sm:h-11 (40 at mobile, 44 at ≥640); sign-up's font
  // drops to 14px at mobile (text-sm sm:text-base md:text-sm) while the
  // other two keep 16px (text-base md:text-sm).
  const sizeCls =
    p.mode === "signin"
      ? "h-11 sm:h-12 text-base md:text-sm"
      : p.mode === "signup"
        ? "h-10 sm:h-11 text-sm sm:text-base md:text-sm"
        : "h-10 sm:h-11 text-base md:text-sm";
  const inputCls = `${INPUT_CLS} ${sizeCls}`;
  return (
    <form
      className={p.mode === "signup" ? "space-y-3 sm:space-y-4" : "space-y-4 sm:space-y-5"}
      onSubmit={p.onSubmit}
    >
      <div className="space-y-3 sm:space-y-4">
        <div className="space-y-1.5">
          <label htmlFor="email" className={LABEL_CLS}>
            Email
          </label>
          <div className="relative">
            <MailIcon className="absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2 text-[#64748b]" />
            <input
              id="email"
              type="email"
              required
              autoComplete="email"
              placeholder="you@example.com"
              value={p.email}
              onChange={(e) => p.onEmail(e.target.value)}
              className={inputCls}
            />
          </div>
        </div>

        {p.mode !== "forgot" && (
          <div className="space-y-1.5">
            <label htmlFor="password" className={LABEL_CLS}>
              Password
            </label>
            <div className="relative">
              <LockIcon className="absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2 text-[#64748b]" />
              <input
                id="password"
                type="password"
                required
                minLength={p.mode === "signup" ? 8 : undefined}
                autoComplete={p.mode === "signup" ? "new-password" : "current-password"}
                placeholder={p.mode === "signup" ? "Min. 8 characters" : "••••••••"}
                value={p.password}
                onChange={(e) => p.onPassword(e.target.value)}
                className={inputCls}
              />
            </div>
          </div>
        )}

        {p.mode === "signup" && (
          <div className="space-y-1.5">
            <label htmlFor="confirm" className={LABEL_CLS}>
              Confirm Password
            </label>
            <div className="relative">
              <LockIcon className="absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2 text-[#64748b]" />
              <input
                id="confirm"
                type="password"
                required
                minLength={8}
                autoComplete="new-password"
                // v13 G2 (measured live on the reference's sign-up state):
                // the confirm field hints its purpose, not dots.
                placeholder="Re-enter password"
                value={p.confirm}
                onChange={(e) => p.onConfirm(e.target.value)}
                className={inputCls}
              />
            </div>
          </div>
        )}
      </div>

      {p.error && (
        <div
          role="alert"
          style={{
            // v12 G1 (measured live on the reference): the auth error is a
            // red-tinted bordered banner — red-50 at 70%, red-200 border,
            // 12px radius, 16px padding — a direct child of the form's
            // space-y flow (the gaps come from the form, not the banner).
            backgroundColor: "rgba(254, 242, 242, 0.7)",
            border: "1px solid rgb(254, 202, 202)",
            borderRadius: "12px",
            padding: "16px",
          }}
        >
          <div
            style={{
              // The shadcn FormMessage pattern: centered red-700 14px/400
              // (inline styles — v4 computes the named reds in Lab).
              color: "rgb(185, 28, 28)",
              fontSize: "14px",
              fontWeight: 400,
              lineHeight: "20px",
              textAlign: "center",
            }}
          >
            {p.error}
          </div>
        </div>
      )}

      <div className="space-y-3">
        <button
          type="submit"
          disabled={p.busy}
          className={`inline-flex w-full items-center justify-center gap-1 rounded-xl bg-[#0f172a] px-3 py-2 text-sm font-medium whitespace-nowrap text-white shadow-sm transition-all duration-200 hover:bg-[#1e293b] focus-visible:ring-2 focus-visible:ring-[#09090b] focus-visible:ring-offset-2 focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 ${
            p.mode === "signin" ? "h-11 sm:h-12" : "h-10 sm:h-11"
          }`}
        >
          {p.busy && <Loader2Icon className="h-4 w-4 animate-spin" />}
          {p.mode === "signin" && "Sign in"}
          {p.mode === "signup" && "Create account"}
          {p.mode === "forgot" && "Send reset link"}
        </button>
        {p.mode === "signin" && (
          <div className="flex flex-col items-center justify-between gap-2 sm:flex-row sm:gap-0">
            <button
              type="button"
              className="text-sm font-medium text-[#64748b] transition-colors hover:text-[#334155]"
              onClick={p.onForgot}
            >
              Forgot password?
            </button>
            <button
              type="button"
              className="text-sm text-[#64748b] transition-colors hover:text-[#334155]"
              onClick={p.onSignUp}
            >
              Need an account?{" "}
              <span className="font-medium text-[#334155]">Sign up</span>
            </button>
          </div>
        )}
      </div>
    </form>
  );
}

export function LoginCard() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const login = useBudgetStore((s) => s.login);
  const register = useBudgetStore((s) => s.register);
  const verifyEmailAction = useBudgetStore((s) => s.verifyEmail);
  const resendCode = useBudgetStore((s) => s.resendCode);
  const { toast } = useToast();
  const [mode, setMode] = React.useState<Mode>("signin");
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [confirm, setConfirm] = React.useState("");
  const [busy, setBusy] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);
  // v12 G4: the forgot submit transitions to a confirmation-style state
  // (the reference renders "Check your email" here — measured live).
  const [resetNotice, setResetNotice] = React.useState(false);
  // v21 G3: the register flow's email-verification state (measured live on
  // the reference — "Verify your email", a 6-digit code, a 5-attempt
  // countdown, and a Resend link). The devCode is the HONEST no-mail
  // delivery: a self-hosted instance has no SMTP, so the code rides the
  // register/resend response and renders here with explicit copy (the
  // v12 forgot-password precedent class).
  const [verifyTarget, setVerifyTarget] = React.useState<string | null>(null);
  const [devCode, setDevCode] = React.useState<string | null>(null);
  const [digits, setDigits] = React.useState<string[]>(() => Array.from({ length: 6 }, () => ""));
  const [resentNotice, setResentNotice] = React.useState(false);

  // The reference lands on the ROOT route after login (it renders the
  // dashboard there) — plan v7 G1. ?from_url= still wins when present.
  const fromUrl = searchParams.get("from_url") || "/";

  const backToSignin = () => {
    setMode("signin");
    setError(null);
    setResetNotice(false);
    setVerifyTarget(null);
    setDevCode(null);
    setDigits(Array.from({ length: 6 }, () => ""));
    setResentNotice(false);
  };
  const notifyGoogleUnavailable = () =>
    toast({
      title: "Google sign-in unavailable",
      description: "This self-hosted clone has no OAuth credentials configured.",
    });

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (busy) return;
    setError(null);
    if (mode === "forgot") {
      // v12 G4: the reference transitions the card to a "Check your
      // email" confirmation state (measured live). This self-hosted
      // instance has no mail transport — render the reference's state
      // LAYOUT with honest copy instead of pretending a link was sent.
      setResetNotice(true);
      return;
    }
    if (mode === "signup" && password !== confirm) {
      setError("Passwords do not match");
      return;
    }
    setBusy(true);
    try {
      if (mode === "signup") {
        // v21 G3: the reference lands registration on the email-verification
        // gate (measured live) — no session until the code is confirmed.
        const payload = await register(email, password);
        setVerifyTarget(payload.email);
        setDevCode(payload.devCode);
        setDigits(Array.from({ length: 6 }, () => ""));
        setError(null);
        setResentNotice(false);
        setMode("verify");
        return;
      }
      await login(email, password);
      const target = fromUrl.startsWith("/") ? fromUrl : "/";
      router.push(target);
    } catch (cause) {
      setError(messageOf(cause));
    } finally {
      setBusy(false);
    }
  };

  // v21 G3: submit the 6-digit code — a correct code verifies + opens the
  // session + lands on the app (the natural post-verify landing, "/").
  const onVerifySubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (busy || !verifyTarget) return;
    setError(null);
    const code = digits.join("");
    if (!/^\d{6}$/.test(code)) {
      setError("Enter the 6-digit code from your email");
      return;
    }
    setBusy(true);
    try {
      await verifyEmailAction(verifyTarget, code);
      const target = fromUrl.startsWith("/") ? fromUrl : "/";
      router.push(target);
    } catch (cause) {
      setError(messageOf(cause));
    } finally {
      setBusy(false);
    }
  };

  // v21 G3: "Didn't receive the code? Resend" (the reference re-issues the
  // code and resets the attempts — measured live).
  const onResend = async () => {
    if (busy || !verifyTarget) return;
    setBusy(true);
    setError(null);
    try {
      const code = await resendCode(verifyTarget);
      setDevCode(code);
      setDigits(Array.from({ length: 6 }, () => ""));
      setResentNotice(true);
    } catch (cause) {
      setError(messageOf(cause));
    } finally {
      setBusy(false);
    }
  };

  const onSetDigit = (index: number, value: string) => {
    setDigits((prev) => {
      const next = [...prev];
      next[index] = value;
      return next;
    });
  };

  const formProps = {
    email,
    password,
    confirm,
    busy,
    error,
    onEmail: setEmail,
    onPassword: setPassword,
    onConfirm: setConfirm,
    onSubmit,
    onForgot: () => {
      setMode("forgot");
      setError(null);
      setResetNotice(false);
    },
    onSignUp: () => {
      setMode("signup");
      setError(null);
      setResetNotice(false);
    },
  };

  return (
    // v12 G3: the reference's login root is a <main> landmark (min-h-screen
    // flex items-center justify-center … p-4) — tag swap only; the classes
    // and the inline gradient stay exactly as pinned in v7.
    <main
      className="flex min-h-screen items-center justify-center p-4"
      style={{
        background: "linear-gradient(to bottom right, rgb(248, 250, 252), rgb(241, 245, 249))",
      }}
    >
      <div className="w-full max-w-md">
        <div
          className="relative overflow-hidden rounded-2xl border-0 text-card-foreground shadow-2xl backdrop-blur-sm"
          style={{ backgroundColor: "rgba(255, 255, 255, 0.95)" }}
        >
          <div
            className="absolute top-0 right-0 left-0 h-1"
            style={{
              background:
                "linear-gradient(to right, rgb(226, 232, 240), rgb(203, 213, 225), rgb(226, 232, 240))",
            }}
          />
          <div className="p-8 sm:p-10 md:px-10 md:pt-12 md:pb-10">
            {mode === "signin" ? (
              <div className="flex flex-col items-center space-y-6 text-center sm:space-y-8">
                <LogoMark />
                <div className="space-y-2 sm:space-y-3">
                  <h1 className="text-2xl font-bold tracking-tight text-[#0f172a] sm:text-3xl">
                    Welcome to ZeroBudget
                  </h1>
                  <p className="text-sm font-medium text-[#64748b] sm:text-base">
                    Sign in to continue
                  </p>
                </div>
                <div className="w-full">
                  <GoogleBlock onUnavailable={notifyGoogleUnavailable} />
                  <AuthForm
                    mode="signin"
                    {...formProps}
                  />
                </div>
              </div>
            ) : (
              <div className="flex flex-col items-center space-y-6 text-center sm:space-y-8">
                <div className="w-full">
                  {mode === "verify" ? (
                    // v21 G3: the reference's register post-success landing
                    // (measured live): a top-left "Back to sign in", a 64px
                    // slate-100 circle carrying a 32px lucide-shield-check
                    // in #334155, the h2 "Verify your email" (the same
                    // text-xl/700/#0f172a family), "We've sent a 6-digit
                    // code to {email}" on two lines, six 40×44 numeric code
                    // inputs (gap 6), the 12px #64748b hint, the 44px
                    // #0f172a "Verify email" button, and "Didn't receive
                    // the code? Resend". The wrong-code line renders the
                    // reference's exact countdown text in 14px #b91c1c.
                    // The dev-code box is the HONEST no-mail delivery (the
                    // v12 forgot-password precedent).
                    <div className="space-y-4">
                      <button
                        type="button"
                        className="-mb-2 flex items-center gap-2 text-sm font-medium text-[#64748b] transition-colors hover:text-[#334155]"
                        onClick={backToSignin}
                      >
                        <ArrowLeftIcon className="h-4 w-4" />
                        Back to sign in
                      </button>
                      <div className="flex flex-col items-center space-y-4 text-center">
                        <div className="mx-auto flex h-14 w-14 items-center justify-center rounded-[9999px] bg-[#f1f5f9] sm:h-16 sm:w-16">
                          <ShieldCheckIcon className="h-7 w-7 text-[#334155] sm:h-8 sm:w-8" />
                        </div>
                        <h2 className="text-xl font-bold text-[#0f172a] sm:text-2xl">
                          Verify your email
                        </h2>
                        <p className="text-sm text-[#475569] sm:text-base">
                          We&apos;ve sent a 6-digit code to
                          <br />
                          {verifyTarget}
                        </p>
                        <div className="w-full rounded-lg bg-[#f8fafc] px-3 py-2 text-xs text-[#475569]">
                          No mail transport is configured on this self-hosted
                          instance — your verification code is{" "}
                          <span className="font-semibold text-[#0f172a]">{devCode}</span>
                        </div>
                        <form onSubmit={onVerifySubmit} className="w-full">
                          <CodeInputs digits={digits} onSetDigit={onSetDigit} disabled={busy} />
                          <p className="mt-2 text-xs text-[#64748b]">
                            Enter the verification code sent to your email
                          </p>
                          {error && (
                            <p className="mt-2 text-sm font-normal text-[#b91c1c]">{error}</p>
                          )}
                          <button
                            type="submit"
                            disabled={busy}
                            className="mt-4 inline-flex h-11 w-full items-center justify-center gap-1 rounded-xl bg-[#0f172a] px-3 py-2 text-sm font-medium whitespace-nowrap text-white shadow-sm transition-all duration-200 hover:bg-[#1e293b] focus-visible:ring-2 focus-visible:ring-[#09090b] focus-visible:ring-offset-2 focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50"
                          >
                            {busy && <Loader2Icon className="h-4 w-4 animate-spin" />}
                            Verify email
                          </button>
                          {resentNotice && (
                            <p className="mt-3 text-sm text-[#475569]">
                              New verification code sent to your email
                            </p>
                          )}
                          <p className="mt-4 text-sm text-[#475569]">
                            Didn&apos;t receive the code?{" "}
                            <button
                              type="button"
                              className="font-medium text-[#334155] transition-colors hover:text-[#0f172a] disabled:pointer-events-none disabled:opacity-50"
                              onClick={onResend}
                              disabled={busy}
                            >
                              Resend
                            </button>
                          </p>
                        </form>
                      </div>
                    </div>
                  ) : resetNotice ? (
                    // v12 G4: the reference's forgot-confirmation state
                    // (measured live on its "Check your email" view): a
                    // centered H2 24px/700 #0f172a lh 32, a 16px/400
                    // #475569 lh 24 description at mt 8, a 16px #09090b
                    // secondary line at mt 24, and a 14px/500 #64748b
                    // "Back to sign in" at mt 24 — the form is replaced.
                    // The copy is the honest variant (no mail transport).
                    <div className="flex flex-col items-center text-center">
                      <h2 className="text-xl font-bold text-[#0f172a] sm:text-2xl">
                        Password reset unavailable
                      </h2>
                      <p className="mt-2 text-sm text-[#475569] sm:text-base">
                        This self-hosted instance has no email service
                        configured, so reset instructions cannot be sent.
                      </p>
                      <div className="mt-6 text-sm text-[#09090b] sm:text-base">
                        Password reset links would normally be emailed for this
                        address. Configure a mail transport to enable them.
                      </div>
                      <button
                        type="button"
                        className="mt-6 text-sm font-medium text-[#64748b] transition-colors hover:text-[#334155]"
                        onClick={backToSignin}
                      >
                        Back to sign in
                      </button>
                    </div>
                  ) : (
                  <div className="space-y-4">
                    <button
                      type="button"
                      className="-mb-2 flex items-center gap-2 text-sm font-medium text-[#64748b] transition-colors hover:text-[#334155]"
                      onClick={backToSignin}
                    >
                      <ArrowLeftIcon className="h-4 w-4" />
                      Back to sign in
                    </button>
                    {mode === "signup" ? (
                      <h2 className="text-xl font-bold text-[#0f172a] sm:text-2xl">
                        Create your account
                      </h2>
                    ) : (
                      <div className="space-y-2 text-center">
                        <h2 className="text-xl font-bold text-[#0f172a] sm:text-2xl">
                          Reset your password
                        </h2>
                        <p className="text-sm text-[#475569] sm:text-base">
                          Enter your email and we&apos;ll send you a link to reset your password
                        </p>
                      </div>
                    )}
                    <AuthForm mode={mode} {...formProps} />
                  </div>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}
