import { describe, expect, it } from "vitest";
import { AUTH_RATE_LIMIT, RateLimiter, clientIp } from "@/lib/rate-limit";

// The auth rate limiter — an in-memory fixed window, pure and unit-testable.
// The reference's Base44 platform rate-limits its auth endpoints
// (10 attempts/IP/15 min); this reproduces that protection self-hosted.

function makeLimiter(limit = 3, windowMs = 1000) {
  return new RateLimiter({ limit, windowMs });
}

describe("RateLimiter", () => {
  it("allows up to the limit, then blocks for the rest of the window", () => {
    const rl = makeLimiter(3);
    expect(rl.check("ip-1", 0)).toMatchObject({ allowed: true, remaining: 2 });
    expect(rl.check("ip-1", 100)).toMatchObject({ allowed: true, remaining: 1 });
    expect(rl.check("ip-1", 200)).toMatchObject({ allowed: true, remaining: 0 });
    const blocked = rl.check("ip-1", 300);
    expect(blocked.allowed).toBe(false);
    expect(blocked.retryAfterSeconds).toBe(1); // (1000 - 300) / 1000 → 1s
  });

  it("tracks keys independently (per-IP isolation)", () => {
    const rl = makeLimiter(1);
    expect(rl.check("ip-A", 0).allowed).toBe(true);
    expect(rl.check("ip-B", 0).allowed).toBe(true);
    expect(rl.check("ip-A", 1).allowed).toBe(false);
    expect(rl.check("ip-B", 1).allowed).toBe(false);
  });

  it("resets the window after it elapses", () => {
    const rl = makeLimiter(1, 1000);
    expect(rl.check("ip-1", 0).allowed).toBe(true);
    expect(rl.check("ip-1", 999).allowed).toBe(false);
    // At/after resetAt the next check starts a fresh bucket.
    expect(rl.check("ip-1", 1000)).toMatchObject({ allowed: true, remaining: 0 });
  });

  it("reports a sane retryAfterSeconds ceiling", () => {
    const rl = makeLimiter(1, 15 * 60 * 1000);
    rl.check("ip-1", 0);
    const blocked = rl.check("ip-1", 5_000);
    expect(blocked.retryAfterSeconds).toBe(14 * 60 + 55);
  });

  it("reset() drops every bucket (test hook)", () => {
    const rl = makeLimiter(1);
    rl.check("ip-1", 0);
    expect(rl.check("ip-1", 1).allowed).toBe(false);
    rl.reset();
    expect(rl.check("ip-1", 2).allowed).toBe(true);
  });

  it("ships the documented auth budget (10 / 15 min)", () => {
    expect(AUTH_RATE_LIMIT).toEqual({ limit: 10, windowMs: 15 * 60 * 1000 });
  });
});

describe("clientIp", () => {
  it("prefers the first x-forwarded-for hop", () => {
    const req = new Request("https://x.test/", {
      headers: { "x-forwarded-for": "203.0.113.9, 10.0.0.1" },
    });
    expect(clientIp(req)).toBe("203.0.113.9");
  });

  it("falls back to x-real-ip, then 'unknown'", () => {
    expect(clientIp(new Request("https://x.test/", { headers: { "x-real-ip": "198.51.100.7" } }))).toBe(
      "198.51.100.7",
    );
    expect(clientIp(new Request("https://x.test/"))).toBe("unknown");
  });
});
