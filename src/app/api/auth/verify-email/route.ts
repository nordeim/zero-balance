import { db } from "@/lib/db";
import { fail, ok, parseBody } from "@/lib/api-helpers";
import { setSessionCookie } from "@/lib/auth";
import { authLimiter, clientIp } from "@/lib/rate-limit";
import {
  attemptsExhausted,
  codeMatches,
  invalidCodeMessage,
} from "@/lib/verification";
import { verifyEmailSchema } from "@/lib/validation";

// v21 G3: the register flow's email-verification step (measured live on
// the reference — "Verify your email" state, 6-digit code, 5-attempt
// countdown). A correct code verifies the account AND opens the session
// (the natural post-verify landing: the app at "/").
export async function POST(request: Request) {
  const decision = authLimiter.check(`verify:${clientIp(request)}`);
  if (!decision.allowed) {
    return fail("Too many attempts. Please try again later.", 429, {
      "Retry-After": String(decision.retryAfterSeconds),
    });
  }
  const body = await parseBody(request, verifyEmailSchema);
  if (!body.ok) return fail(body.error, body.status);

  const user = await db.user.findUnique({ where: { email: body.data.email } });
  if (!user || user.emailVerifiedAt) {
    // Unknown email or already-verified account: the same neutral message,
    // no account enumeration (the login route's convention).
    return fail("Invalid email or code", 401);
  }

  if (attemptsExhausted(user.codeAttempts)) {
    return fail("Too many wrong codes. Request a new code.", 429);
  }

  if (!codeMatches(body.data.code, user.verificationCode)) {
    const attempts = user.codeAttempts + 1;
    await db.user.update({
      where: { id: user.id },
      data: { codeAttempts: attempts },
    });
    // The reference's measured countdown text (14px #b91c1c centered).
    return fail(invalidCodeMessage(attempts), 400);
  }

  const verified = await db.user.update({
    where: { id: user.id },
    data: { emailVerifiedAt: new Date(), verificationCode: null, codeAttempts: 0 },
    select: { id: true, email: true, name: true },
  });
  await setSessionCookie(verified.id);
  return ok({ user: verified });
}
