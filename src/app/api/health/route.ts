import { ok } from "@/lib/api-helpers";

// Liveness probe — the Playwright webServer waits on this endpoint.
export async function GET() {
  return ok({ status: "ok", app: "zero-balance" });
}
