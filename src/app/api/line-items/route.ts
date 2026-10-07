// Line-item routes. Creating, updating or deleting a line item recalculates
// the parent BudgetItem's amount from the remaining line items — the
// reference's "Total Calculated … will update category total" behavior.

import { db } from "@/lib/db";
import { fail, ok, parseBody, requireSession } from "@/lib/api-helpers";
import { serializeLineItem } from "@/lib/serializers";
import { sumAmounts } from "@/lib/money";
import { createLineItemSchema } from "@/lib/validation";
import { recalcParentAmount } from "@/lib/line-item-service";

export async function GET(request: Request) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const budgetItemId = new URL(request.url).searchParams.get("budgetItemId");
  if (!budgetItemId) return fail("budgetItemId query parameter is required", 400);

  const parent = await db.budgetItem.findFirst({
    where: { id: budgetItemId, userId: auth.user.id },
  });
  if (!parent) return fail("Budget item not found", 404);

  const rows = await db.expenseLineItem.findMany({
    where: { budgetItemId },
    orderBy: { createdAt: "desc" },
  });
  return ok(rows.map(serializeLineItem));
}

export async function POST(request: Request) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const body = await parseBody(request, createLineItemSchema);
  if (!body.ok) return fail(body.error, body.status);

  const parent = await db.budgetItem.findFirst({
    where: { id: body.data.budgetItemId, userId: auth.user.id },
  });
  if (!parent) return fail("Budget item not found", 404);

  const d = body.data;
  const row = await db.expenseLineItem.create({
    data: {
      userId: auth.user.id,
      budgetItemId: d.budgetItemId,
      name: d.name,
      amount: d.amount,
      frequency: d.frequency,
      provider: d.provider ?? null,
      policyNumber: d.policyNumber ?? null,
      paymentMethod: d.paymentMethod ?? null,
      startDate: d.startDate ?? null,
      endDate: d.endDate ?? null,
      status: d.status,
      notes: d.notes ?? null,
    },
  });
  const updatedParent = await recalcParentAmount(row.budgetItemId);
  return ok({ lineItem: serializeLineItem(row), parentAmount: updatedParent?.amount ?? null }, { status: 201 });
}
