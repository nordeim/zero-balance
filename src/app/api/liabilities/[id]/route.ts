import { db } from "@/lib/db";
import { fail, ok, parseBody, requireSession } from "@/lib/api-helpers";
import { serializeLiability } from "@/lib/serializers";
import { updateLiabilitySchema } from "@/lib/validation";

type Params = { params: Promise<{ id: string }> };

export async function PATCH(request: Request, { params }: Params) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const { id } = await params;
  const body = await parseBody(request, updateLiabilitySchema);
  if (!body.ok) return fail(body.error, body.status);

  const existing = await db.liability.findFirst({ where: { id, userId: auth.user.id } });
  if (!existing) return fail("Liability not found", 404);

  const d = body.data;
  const row = await db.liability.update({
    where: { id },
    data: {
      ...(d.type !== undefined ? { type: d.type } : {}),
      ...(d.name !== undefined ? { name: d.name } : {}),
      ...(d.institution !== undefined ? { institution: d.institution ?? null } : {}),
      ...(d.accountNumber !== undefined ? { accountNumber: d.accountNumber ?? null } : {}),
      ...(d.value !== undefined ? { value: d.value } : {}),
      ...(d.interestRate !== undefined ? { interestRate: d.interestRate ?? null } : {}),
      ...(d.monthlyPayment !== undefined ? { monthlyPayment: d.monthlyPayment ?? null } : {}),
      ...(d.lastUpdated !== undefined ? { lastUpdated: d.lastUpdated } : {}),
      ...(d.notes !== undefined ? { notes: d.notes ?? null } : {}),
    },
  });
  return ok(serializeLiability(row));
}

export async function DELETE(_request: Request, { params }: Params) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const { id } = await params;

  const existing = await db.liability.findFirst({ where: { id, userId: auth.user.id } });
  if (!existing) return fail("Liability not found", 404);

  await db.liability.delete({ where: { id } });
  return ok({ deleted: true });
}
