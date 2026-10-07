import { db } from "@/lib/db";
import { fail, ok, parseBody, requireSession } from "@/lib/api-helpers";
import { serializeLiability } from "@/lib/serializers";
import { createLiabilitySchema } from "@/lib/validation";

export async function GET() {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const rows = await db.liability.findMany({
    where: { userId: auth.user.id },
    orderBy: { createdAt: "desc" },
  });
  return ok(rows.map(serializeLiability));
}

export async function POST(request: Request) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const body = await parseBody(request, createLiabilitySchema);
  if (!body.ok) return fail(body.error, body.status);

  const d = body.data;
  const row = await db.liability.create({
    data: {
      userId: auth.user.id,
      type: d.type,
      name: d.name,
      institution: d.institution ?? null,
      accountNumber: d.accountNumber ?? null,
      value: d.value,
      interestRate: d.interestRate ?? null,
      monthlyPayment: d.monthlyPayment ?? null,
      lastUpdated: d.lastUpdated,
      notes: d.notes ?? null,
    },
  });
  return ok(serializeLiability(row), { status: 201 });
}
