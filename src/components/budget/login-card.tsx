"use client";

// The /login auth card — sign in / sign up / forgot password states on the
// slate gradient page. Visual chrome mirrors the reference: the 4px top
// gradient bar, blurred halo behind the ringed logo, Google button, icon
// inputs and the slate-900 submit. "Continue with Google" renders for
// parity and degrades to an explanatory toast (no OAuth credentials in a
// self-hosted clone). ?from_url= return handling included.

import * as React from "react";
import { useRouter, useSearchParams } from "next/navigation";
import Link from "next/link";
import { Loader2Icon, LockIcon, MailIcon } from "lucide-react";
import { useToast } from "@/components/ui/toast";
import { messageOf, useBudgetStore } from "./store";

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
      <div className="absolute inset-0 rounded-full bg-gradient-to-br from-slate-200 to-slate-300 opacity-30 blur-xl transition-opacity duration-300 group-hover:opacity-40" />
      <span className="relative flex h-20 w-20 shrink-0 overflow-hidden rounded-full shadow-lg ring-4 ring-white/50 transition-all duration-300 group-hover:shadow-xl sm:h-24 sm:w-24">
        <img
          src="/zerobalance-logo.png"
          alt="ZeroBudget logo"
          className="aspect-square h-full w-full object-cover"
        />
      </span>
    </div>
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

  const fromUrl = searchParams.get("from_url") || "/dashboard";

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (busy) return;
    setError(null);
    if (mode === "forgot") {
      // Self-hosted: no mail transport is configured; surface that honestly
      // instead of pretending a reset link was sent.
      toast({
        title: "Password reset unavailable",
        description: "This self-hosted clone has no email service configured.",
      });
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
      const target = fromUrl.startsWith("/") ? fromUrl : "/dashboard";
      router.push(target);
    } catch (cause) {
      setError(messageOf(cause));
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-slate-50 to-slate-100 p-4">
      <div className="w-full max-w-md">
        <div className="relative overflow-hidden rounded-2xl border-0 bg-white/95 text-card-foreground shadow-2xl backdrop-blur-sm">
          <div className="absolute top-0 right-0 left-0 h-1 bg-gradient-to-r from-slate-200 via-slate-300 to-slate-200" />
          <div className="p-8 sm:p-10 md:px-10 md:pt-12 md:pb-10">
            <div className="flex flex-col items-center space-y-6 text-center sm:space-y-8">
              <LogoMark />
              <div className="space-y-2 sm:space-y-3">
                <h1 className="text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">
                  {mode === "signin" && "Welcome to ZeroBudget"}
                  {mode === "signup" && "Create your account"}
                  {mode === "forgot" && "Reset your password"}
                </h1>
                <p className="text-sm font-medium text-slate-500 sm:text-base">
                  {mode === "signin" && "Sign in to continue"}
                  {mode === "signup" && "Start planning your budget"}
                  {mode === "forgot" && "Enter your email and we'll send a reset link"}
                </p>
              </div>

              <div className="w-full">
                <div className="space-y-3">
                  <button
                    type="button"
                    className="group flex w-full items-center justify-center gap-3 rounded-xl border border-slate-200 bg-white px-5 py-3.5 font-medium text-slate-700 text-[16px] transition-all duration-200 hover:border-slate-300 hover:bg-slate-50 hover:shadow-sm"
                    onClick={() =>
                      toast({
                        title: "Google sign-in unavailable",
                        description: "This self-hosted clone has no OAuth credentials configured.",
                      })
                    }
                  >
                    <span className="-ml-4 transition-transform duration-200">
                      {GOOGLE_SVG}
                    </span>
                    Continue with Google
                  </button>
                </div>

                <div className="relative my-6">
                  <div className="absolute inset-0 flex items-center">
                    <span className="h-px w-full bg-slate-200" aria-hidden="true" />
                  </div>
                  <div className="relative flex justify-center text-xs uppercase">
                    <span className="bg-white px-3 font-medium tracking-wider text-slate-500">
                      or
                    </span>
                  </div>
                </div>

                <form className="space-y-4 sm:space-y-5" onSubmit={onSubmit}>
                  <div className="space-y-3 sm:space-y-4">
                    <div className="space-y-1.5">
                      <label
                        htmlFor="email"
                        className="text-sm font-medium text-slate-700 peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                      >
                        Email
                      </label>
                      <div className="relative">
                        <MailIcon className="absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2 text-slate-500" />
                        <input
                          id="email"
                          type="email"
                          required
                          autoComplete="email"
                          placeholder="you@example.com"
                          value={email}
                          onChange={(e) => setEmail(e.target.value)}
                          className="flex h-11 w-full rounded-xl border border-slate-200 bg-slate-50/50 px-3 py-2 pl-10 text-base transition-colors placeholder:text-slate-600 focus:border-slate-400 focus:ring-slate-400 focus:outline-none disabled:cursor-not-allowed disabled:opacity-50 sm:h-12 md:text-sm"
                        />
                      </div>
                    </div>

                    {mode !== "forgot" && (
                      <div className="space-y-1.5">
                        <label
                          htmlFor="password"
                          className="text-sm font-medium text-slate-700 peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                        >
                          Password
                        </label>
                        <div className="relative">
                          <LockIcon className="absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2 text-slate-500" />
                          <input
                            id="password"
                            type="password"
                            required
                            minLength={mode === "signup" ? 8 : undefined}
                            autoComplete={mode === "signup" ? "new-password" : "current-password"}
                            placeholder="••••••••"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            className="flex h-11 w-full rounded-xl border border-slate-200 bg-slate-50/50 px-3 py-2 pl-10 text-base transition-colors placeholder:text-slate-600 focus:border-slate-400 focus:ring-slate-400 focus:outline-none disabled:cursor-not-allowed disabled:opacity-50 sm:h-12 md:text-sm"
                          />
                        </div>
                      </div>
                    )}

                    {mode === "signup" && (
                      <div className="space-y-1.5">
                        <label
                          htmlFor="confirm"
                          className="text-sm font-medium text-slate-700 peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
                        >
                          Confirm Password
                        </label>
                        <div className="relative">
                          <LockIcon className="absolute top-1/2 left-3 h-4 w-4 -translate-y-1/2 text-slate-500" />
                          <input
                            id="confirm"
                            type="password"
                            required
                            minLength={8}
                            autoComplete="new-password"
                            placeholder="••••••••"
                            value={confirm}
                            onChange={(e) => setConfirm(e.target.value)}
                            className="flex h-11 w-full rounded-xl border border-slate-200 bg-slate-50/50 px-3 py-2 pl-10 text-base transition-colors placeholder:text-slate-600 focus:border-slate-400 focus:ring-slate-400 focus:outline-none disabled:cursor-not-allowed disabled:opacity-50 sm:h-12 md:text-sm"
                          />
                        </div>
                      </div>
                    )}
                  </div>

                  {error && (
                    <p role="alert" className="text-sm font-medium text-red-600">
                      {error}
                    </p>
                  )}

                  <div className="space-y-3">
                    <button
                      type="submit"
                      disabled={busy}
                      className="inline-flex h-11 w-full items-center justify-center gap-1 rounded-xl bg-slate-900 px-3 py-2 font-medium whitespace-nowrap text-white shadow-sm transition-all duration-200 hover:bg-slate-800 focus-visible:ring-2 focus-visible:ring-slate-400 focus-visible:ring-offset-2 focus-visible:outline-none disabled:pointer-events-none disabled:opacity-50 sm:h-12"
                    >
                      {busy && <Loader2Icon className="h-4 w-4 animate-spin" />}
                      {mode === "signin" && "Sign in"}
                      {mode === "signup" && "Create account"}
                      {mode === "forgot" && "Send reset link"}
                    </button>
                    <div className="flex flex-col items-center justify-between gap-2 sm:flex-row sm:gap-0">
                      {mode === "signin" ? (
                        <>
                          <button
                            type="button"
                            className="font-medium text-slate-500 transition-colors hover:text-slate-700"
                            onClick={() => {
                              setMode("forgot");
                              setError(null);
                            }}
                          >
                            Forgot password?
                          </button>
                          <button
                            type="button"
                            className="text-slate-500 transition-colors hover:text-slate-700"
                            onClick={() => {
                              setMode("signup");
                              setError(null);
                            }}
                          >
                            Need an account?{" "}
                            <span className="font-medium text-slate-700">Sign up</span>
                          </button>
                        </>
                      ) : (
                        <button
                          type="button"
                          className="mx-auto text-slate-500 transition-colors hover:text-slate-700 sm:mx-0"
                          onClick={() => {
                            setMode("signin");
                            setError(null);
                          }}
                        >
                          <span className="font-medium text-slate-700">Back to sign in</span>
                        </button>
                      )}
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
        <div className="mt-8 hidden text-center text-xs text-slate-400 sm:block">
          <p>
            <Link href="/dashboard" className="hover:text-slate-600">
              Continue as guest
            </Link>
          </p>
        </div>
        <div className="mt-8 text-center text-xs text-slate-400 sm:hidden">
          <p>&nbsp;</p>
        </div>
      </div>
    </div>
  );
}
