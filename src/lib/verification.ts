// v21 G3 (docs/remediation-plan-v21.md): the register flow's email-
// verification gate — measured live on the reference ("Verify your email",
// a 6-digit numeric code, and a 5-attempt countdown before re-send).
// Pure seam, unit-testable without a database; the API routes own the
// Prisma writes and the session cookie.

/** Maximum wrong-code attempts before a re-send is required (the reference
 *  counts down "Invalid verification code. 4 attempts remaining." from 5). */
export const MAX_CODE_ATTEMPTS = 5;

/** Generate a fresh 6-digit numeric code (crypto-backed, leading zeros ok). */
export function generateCode(): string {
  const buf = new Uint32Array(1);
  crypto.getRandomValues(buf);
  // 0..999_999, zero-padded to exactly 6 digits — matches the reference's
  // "6-digit code" contract and its six single-char inputs.
  return String(buf[0] % 1_000_000).padStart(6, "0");
}

export function codeMatches(code: string, expected: string | null): boolean {
  if (!expected) return false;
  return code === expected;
}

/** The remaining attempts AFTER a wrong try (the countdown's number). */
export function remainingAttempts(attempts: number): number {
  return Math.max(0, MAX_CODE_ATTEMPTS - attempts);
}

/** True when the wrong-attempt budget is exhausted — the API must refuse
 *  further verify tries until a re-send resets the counter. */
export function attemptsExhausted(attempts: number): boolean {
  return attempts >= MAX_CODE_ATTEMPTS;
}

/** The reference's exact wrong-code text (measured live). */
export function invalidCodeMessage(attempts: number): string {
  const remaining = remainingAttempts(attempts);
  const plural = remaining === 1 ? "" : "s";
  return `Invalid verification code. ${remaining} attempt${plural} remaining.`;
}

/** The reference's exact unverified-login rejection (measured live). */
export const UNVERIFIED_LOGIN_MESSAGE =
  "Please verify your email before logging in. Check your email for the verification code.";
