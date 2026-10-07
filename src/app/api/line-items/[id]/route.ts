import { db } from "@/lib/db";
import { fail, ok, parseBody, requireSession } from "@/lib/api-helpers";
import { serializeLineItem } from "@/lib/serializers";
import { updateLineItemSchema } from "@/lib/validation";
import { recalcParentAmount } from "@/lib/line-item-service";

type Params = { params: Promise<{ id: string }> };

export async function PATCH(request: Request, { params }: Params) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const { id } = await params;
  const body = await parseBody(request, updateLineItemSchema);
  if (!body.ok) return fail(body.error, body.status);

  const existing = await db.expenseLineItem.findFirst({ where: { id, userId: auth.user.id } });
  if (!existing) return fail("Line item not found", 404);

  const d = body.data;
  const row = await db.expenseLineItem.update({
    where: { id },
    data: {
      ...(d.name !== undefined ? { name: d.name } : {}),
      ...(d.amount !== undefined ? { amount: d.amount } : {}),
      ...(d.frequency !== undefined ? { frequency: d.frequency } : {}),
      ...(d.provider !== undefined ? { provider: d.provider ?? null } : {}),
      ...(d.policyNumber !== undefined ? { policyNumber: d.policyNumber ?? null } : {}),
      ...(d.paymentMethod !== undefined ? { paymentMethod: d.paymentMethod ?? null } : {}),
      ...(d.startDate !== undefined ? { startDate: d.startDate ?? null } : {}),
      ...(d.endDate !== undefined ? { endDate: d.endDate ?? null } : {}),
      ...(d.status !== undefined ? { status: d.status } : {}),
      ...(d.notes !== undefined ? { notes: d.notes ?? null } : {}),
    },
  });
  const updatedParent = await recalcParentAmount(row.budgetItemId);
  return ok({ lineItem: serializeLineItem(row), parentAmount: updatedParent?.amount ?? null });
}

export async function DELETE(_request: Request, { params }: Params) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const { id } = await params;

  const existing = await db.expenseLineItem.findFirst({ where: { id, userId: auth.user.id } });
  if (!existing) return fail("Line item not found", 404);

  const budgetItemId = existing.budgetItemId;
  await db.expenseLineItem.delete({ where: { id } });
  const updatedParent = await recalcParentAmount(budgetItemId);
  return ok({ deleted: true, parentAmount: updatedParent?.amount ?? null });
}
