import { db } from "@/lib/db";
import { fail, ok, parseBody, requireSession } from "@/lib/api-helpers";
import { serializeBudgetItem } from "@/lib/serializers";
import { updateBudgetItemSchema } from "@/lib/validation";

type Params = { params: Promise<{ id: string }> };

export async function PATCH(request: Request, { params }: Params) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const { id } = await params;
  const body = await parseBody(request, updateBudgetItemSchema);
  if (!body.ok) return fail(body.error, body.status);

  const existing = await db.budgetItem.findFirst({ where: { id, userId: auth.user.id } });
  if (!existing) return fail("Budget item not found", 404);

  const d = body.data;
  const row = await db.budgetItem.update({
    where: { id },
    data: {
      ...(d.type !== undefined ? { type: d.type } : {}),
      ...(d.classification !== undefined ? { classification: d.classification } : {}),
      ...(d.amount !== undefined ? { amount: d.amount } : {}),
      ...(d.category !== undefined ? { category: d.category } : {}),
      ...(d.subcategory !== undefined ? { subcategory: d.subcategory ?? null } : {}),
      ...(d.paymentMethod !== undefined ? { paymentMethod: d.paymentMethod ?? null } : {}),
      ...(d.frequency !== undefined ? { frequency: d.frequency } : {}),
      ...(d.date !== undefined ? { date: d.date } : {}),
      ...(d.recurring !== undefined ? { recurring: d.recurring } : {}),
      ...(d.status !== undefined ? { status: d.status } : {}),
      ...(d.notes !== undefined ? { notes: d.notes ?? null } : {}),
    },
  });
  return ok(serializeBudgetItem(row));
}

export async function DELETE(_request: Request, { params }: Params) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const { id } = await params;

  const existing = await db.budgetItem.findFirst({ where: { id, userId: auth.user.id } });
  if (!existing) return fail("Budget item not found", 404);

  await db.budgetItem.delete({ where: { id } });
  return ok({ deleted: true });
}
