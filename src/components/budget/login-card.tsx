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
import { ArrowLeftIcon, Loader2Icon, LockIcon, MailIcon } from "lucide-react";
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

type Mode = "signin" | "signup" | "forgot";

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
// Base input chrome (plan v9 G7): h-11 = 44px — the reference's SIGN-UP and
// FORGOT states render 44px controls; only SIGN-IN grows to 48px (sm:h-12),
// appended per-mode inside AuthForm.
const INPUT_CLS =
  "flex h-11 w-full rounded-xl border border-[#e2e8f0] bg-[rgba(248,250,252,0.5)] px-3 py-2 pl-10 text-base text-[#09090b] transition-colors placeholder:text-[#475569] focus:border-[#94a3b8] focus:ring-[#94a3b8] focus:outline-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm";
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
  // Reference per-state geometry (plan v9 G7, measured live): sign-in
  // controls are 48px at >=640px; sign-up/forgot stay 44px (h-11).
  const inputCls = p.mode === "signin" ? `${INPUT_CLS} sm:h-12` : INPUT_CLS;
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
                placeholder="••••••••"
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
                placeholder="••••••••"
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
          className={`inline-flex h-11 w-full items-center justify-center gap-1 rounded-xl bg-[#0f172a] px-3 py-2 text-sm font-medium whitespace-nowrap text-white shadow-sm transition-all duration-200 hover:bg-[#1e293b] focus-visible:ring-2 focus-visible:ring-[#94a3b8] focus-visible:ring-offset-2 focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50${p.mode === "signin" ? " sm:h-12" : ""}`}
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

  // The reference lands on the ROOT route after login (it renders the
  // dashboard there) — plan v7 G1. ?from_url= still wins when present.
  const fromUrl = searchParams.get("from_url") || "/";

  const backToSignin = () => {
    setMode("signin");
    setError(null);
    setResetNotice(false);
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
        await register(email, password);
      } else {
        await login(email, password);
      }
      const target = fromUrl.startsWith("/") ? fromUrl : "/";
      router.push(target);
    } catch (cause) {
      setError(messageOf(cause));
    } finally {
      setBusy(false);
    }
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
                  {resetNotice ? (
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
