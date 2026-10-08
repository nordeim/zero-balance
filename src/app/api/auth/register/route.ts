import { db } from "@/lib/db";
import { fail, ok, parseBody } from "@/lib/api-helpers";
import { hashPassword, setSessionCookie } from "@/lib/auth";
import { authLimiter, clientIp } from "@/lib/rate-limit";
import { registerSchema } from "@/lib/validation";

export async function POST(request: Request) {
  const decision = authLimiter.check(`register:${clientIp(request)}`);
  if (!decision.allowed) {
    return fail("Too many attempts. Please try again later.", 429, {
      "Retry-After": String(decision.retryAfterSeconds),
    });
  }
  const body = await parseBody(request, registerSchema);
  if (!body.ok) return fail(body.error, body.status);

  const existing = await db.user.findUnique({ where: { email: body.data.email } });
  if (existing) {
    // v13 G1 (measured live on the reference): its 409 banner reads
    // "A user with this email already exists" — match the text exactly.
    return fail("A user with this email already exists", 409);
  }
  const user = await db.user.create({
    data: {
      email: body.data.email,
      passwordHash: hashPassword(body.data.password),
      name: body.data.name ?? null,
    },
    select: { id: true, email: true, name: true },
  });
  await setSessionCookie(user.id);
  return ok({ user }, { status: 201 });
}
