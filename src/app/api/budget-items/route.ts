import { db } from "@/lib/db";
import { fail, ok, parseBody, requireSession } from "@/lib/api-helpers";
import { serializeBudgetItem } from "@/lib/serializers";
import { createBudgetItemSchema } from "@/lib/validation";

export async function GET() {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const rows = await db.budgetItem.findMany({
    where: { userId: auth.user.id },
    orderBy: { createdAt: "desc" },
  });
  return ok(rows.map(serializeBudgetItem));
}

export async function POST(request: Request) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const body = await parseBody(request, createBudgetItemSchema);
  if (!body.ok) return fail(body.error, body.status);

  const row = await db.budgetItem.create({
    data: {
      userId: auth.user.id,
      type: body.data.type,
      classification: body.data.classification,
      amount: body.data.amount,
      category: body.data.category,
      subcategory: body.data.subcategory ?? null,
      paymentMethod: body.data.paymentMethod ?? null,
      frequency: body.data.frequency,
      date: body.data.date,
      recurring: body.data.recurring,
      status: body.data.status,
      notes: body.data.notes ?? null,
    },
  });
  return ok(serializeBudgetItem(row), { status: 201 });
}
