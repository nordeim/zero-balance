import { db } from "@/lib/db";
import { fail, ok, parseBody } from "@/lib/api-helpers";
import { hashPassword } from "@/lib/auth";
import { authLimiter, clientIp } from "@/lib/rate-limit";
import { generateCode } from "@/lib/verification";
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
  if (existing?.emailVerifiedAt) {
    // v13 G1 (measured live on the reference): its 409 banner reads
    // "A user with this email already exists" — match the text exactly.
    return fail("A user with this email already exists", 409);
  }

  // v21 G3 (measured live on the reference): registration lands on an
  // email-verification gate, and re-registering an existing UNVERIFIED
  // email re-issues the code (no 409 — its re-send semantics). No session
  // cookie is set here; /api/auth/verify-email opens the session.
  const code = generateCode();
  if (existing) {
    await db.user.update({
      where: { id: existing.id },
      data: { verificationCode: code, codeAttempts: 0 },
    });
  } else {
    await db.user.create({
      data: {
        email: body.data.email,
        passwordHash: hashPassword(body.data.password),
        name: body.data.name ?? null,
        verificationCode: code,
        codeAttempts: 0,
      },
      select: { id: true },
    });
  }

  // The honest no-mail delivery (the v12 forgot-password precedent): a
  // self-hosted instance has no SMTP, so the code rides the response and
  // the verify state displays it with explicit copy. With SMTP configured
  // in a real deployment this field would be dropped — the UI copy
  // explains the fallback either way.
  return ok(
    { email: body.data.email, devCode: code },
    { status: 201 },
  );
}
