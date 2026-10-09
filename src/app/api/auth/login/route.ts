import { db } from "@/lib/db";
import { fail, ok, parseBody } from "@/lib/api-helpers";
import { setSessionCookie, verifyPassword } from "@/lib/auth";
import { authLimiter, clientIp } from "@/lib/rate-limit";
import { UNVERIFIED_LOGIN_MESSAGE } from "@/lib/verification";
import { loginSchema } from "@/lib/validation";

export async function POST(request: Request) {
  const decision = authLimiter.check(`login:${clientIp(request)}`);
  if (!decision.allowed) {
    return fail("Too many attempts. Please try again later.", 429, {
      "Retry-After": String(decision.retryAfterSeconds),
    });
  }
  const body = await parseBody(request, loginSchema);
  if (!body.ok) return fail(body.error, body.status);

  const user = await db.user.findUnique({ where: { email: body.data.email } });
  // Same error for unknown email and wrong password — no account enumeration.
  if (!user || !verifyPassword(body.data.password, user.passwordHash)) {
    return fail("Invalid email or password", 401);
  }
  // v21 G3 (measured live on the reference): signing in with an UNVERIFIED
  // account is rejected with its exact banner text — the account exists,
  // the credentials match, but the email gate comes first.
  if (!user.emailVerifiedAt) {
    return fail(UNVERIFIED_LOGIN_MESSAGE, 403);
  }
  const session = { id: user.id, email: user.email, name: user.name };
  await setSessionCookie(user.id);
  return ok({ user: session });
}
