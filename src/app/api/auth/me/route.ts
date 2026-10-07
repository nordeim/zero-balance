import { ok } from "@/lib/api-helpers";
import { getSessionUser } from "@/lib/auth";

export async function GET() {
  const user = await getSessionUser();
  return ok({ user });
}
