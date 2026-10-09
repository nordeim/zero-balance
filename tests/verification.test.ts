import { describe, expect, it } from "vitest";

import {
  MAX_CODE_ATTEMPTS,
  UNVERIFIED_LOGIN_MESSAGE,
  attemptsExhausted,
  codeMatches,
  generateCode,
  invalidCodeMessage,
  remainingAttempts,
} from "@/lib/verification";

// v21 G3: the register flow's email-verification seam — the reference's
// measured contract is a 6-digit numeric code with a 5-attempt countdown
// ("Invalid verification code. 4 attempts remaining.") and an
// unverified-login rejection banner. Pure logic only; the API routes own
// the writes.

describe("generateCode", () => {
  it("produces exactly 6 numeric digits", () => {
    for (let i = 0; i < 200; i++) {
      const code = generateCode();
      expect(code).toMatch(/^\d{6}$/);
    }
  });
});

describe("codeMatches", () => {
  it("matches the exact code", () => {
    expect(codeMatches("123456", "123456")).toBe(true);
  });
  it("rejects a wrong code", () => {
    expect(codeMatches("123456", "654321")).toBe(false);
  });
  it("rejects when no code is on file (null)", () => {
    expect(codeMatches("123456", null)).toBe(false);
  });
});

describe("attempt countdown", () => {
  it("counts down from 5 the reference's way", () => {
    // After 1 wrong try the message reads "4 attempts remaining."
    expect(remainingAttempts(1)).toBe(4);
    expect(invalidCodeMessage(1)).toBe("Invalid verification code. 4 attempts remaining.");
  });
  it("pluralizes the single remaining attempt", () => {
    expect(invalidCodeMessage(4)).toBe("Invalid verification code. 1 attempt remaining.");
  });
  it("exhausts at exactly the max", () => {
    expect(MAX_CODE_ATTEMPTS).toBe(5);
    expect(attemptsExhausted(4)).toBe(false);
    expect(attemptsExhausted(5)).toBe(true);
  });
  it("clamps the remaining count at zero", () => {
    expect(remainingAttempts(7)).toBe(0);
  });
});

describe("unverified login message", () => {
  it("carries the reference's measured banner text verbatim", () => {
    expect(UNVERIFIED_LOGIN_MESSAGE).toBe(
      "Please verify your email before logging in. Check your email for the verification code.",
    );
  });
});
