import { db } from "@/lib/db";
import { fail, ok, parseBody, requireSession } from "@/lib/api-helpers";
import { serializeAsset } from "@/lib/serializers";
import { createAssetSchema } from "@/lib/validation";

export async function GET() {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const rows = await db.asset.findMany({
    where: { userId: auth.user.id },
    orderBy: { createdAt: "desc" },
  });
  return ok(rows.map(serializeAsset));
}

export async function POST(request: Request) {
  const auth = await requireSession();
  if (auth.response) return auth.response;
  const body = await parseBody(request, createAssetSchema);
  if (!body.ok) return fail(body.error, body.status);

  const d = body.data;
  const row = await db.asset.create({
    data: {
      userId: auth.user.id,
      type: d.type,
      name: d.name,
      institution: d.institution ?? null,
      accountNumber: d.accountNumber ?? null,
      value: d.value,
      lastUpdated: d.lastUpdated,
      notes: d.notes ?? null,
    },
  });
  return ok(serializeAsset(row), { status: 201 });
}
