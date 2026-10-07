// Per-IP login/register rate limiting — an in-memory fixed window, pure and
// unit-testable. The reference app's Base44 platform rate-limits its auth
// endpoints; this reproduces that protection self-hosted. State is
// per-process (fine for the single-server SQLite deployment model this app
// ships with; a multi-instance deploy would move this to shared storage).

export interface RateLimiterConfig {
  limit: number;
  windowMs: number;
}

export interface RateLimitDecision {
  allowed: boolean;
  remaining: number;
  retryAfterSeconds: number;
}

interface Bucket {
  count: number;
  resetAt: number;
}

export const AUTH_RATE_LIMIT: RateLimiterConfig = { limit: 10, windowMs: 15 * 60 * 1000 };

export class RateLimiter {
  private buckets = new Map<string, Bucket>();

  constructor(private readonly config: RateLimiterConfig) {}

  check(key: string, now: number = Date.now()): RateLimitDecision {
    const bucket = this.buckets.get(key);
    if (!bucket || bucket.resetAt <= now) {
      this.buckets.set(key, { count: 1, resetAt: now + this.config.windowMs });
      return { allowed: true, remaining: this.config.limit - 1, retryAfterSeconds: 0 };
    }
    if (bucket.count >= this.config.limit) {
      return {
        allowed: false,
        remaining: 0,
        retryAfterSeconds: Math.max(1, Math.ceil((bucket.resetAt - now) / 1000)),
      };
    }
    bucket.count += 1;
    return { allowed: true, remaining: this.config.limit - bucket.count, retryAfterSeconds: 0 };
  }

  /** Test-only: drop every bucket. */
  reset(): void {
    this.buckets.clear();
  }
}

/** The process-wide limiter for auth endpoints. */
export const authLimiter = new RateLimiter(AUTH_RATE_LIMIT);

/** Client IP for rate limiting: the socket address, unaffected by spoofable headers. */
export function clientIp(request: Request): string {
  return (
    request.headers.get("x-forwarded-for")?.split(",")[0]?.trim() ||
    request.headers.get("x-real-ip") ||
    "unknown"
  );
}
