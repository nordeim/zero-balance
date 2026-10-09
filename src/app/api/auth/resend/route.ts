import { db } from "@/lib/db";
import { fail, ok, parseBody } from "@/lib/api-helpers";
import { authLimiter, clientIp } from "@/lib/rate-limit";
import { generateCode } from "@/lib/verification";
import { resendSchema } from "@/lib/validation";

// v21 G3: "Didn't receive the code? Resend" (measured live on the
// reference — a fresh code + attempts reset + the transient "New
// verification code sent to your email" line). Only works for an existing
// UNVERIFIED account; the register:<ip> limiter bucket covers the budget.
export async function POST(request: Request) {
  const decision = authLimiter.check(`register:${clientIp(request)}`);
  if (!decision.allowed) {
    return fail("Too many attempts. Please try again later.", 429, {
      "Retry-After": String(decision.retryAfterSeconds),
    });
  }
  const body = await parseBody(request, resendSchema);
  if (!body.ok) return fail(body.error, body.status);

  const user = await db.user.findUnique({ where: { email: body.data.email } });
  if (!user || user.emailVerifiedAt) {
    // Neutral message — no account enumeration (the family convention).
    return fail("Invalid email or code", 401);
  }

  const code = generateCode();
  await db.user.update({
    where: { id: user.id },
    data: { verificationCode: code, codeAttempts: 0 },
  });

  // The honest no-mail delivery (the register route's contract).
  return ok({ email: body.data.email, devCode: code });
}
