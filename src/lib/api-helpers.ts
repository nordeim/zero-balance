// API route helpers — the typed JSON envelope and the session guard shared
// by every handler.
//
// Envelope: { ok: true, data } | { ok: false, error: string }.

import { NextResponse } from "next/server";
import { z } from "zod";
import type { SessionUser } from "./auth";
import { getSessionUser } from "./auth";

export function ok<T>(data: T, init?: ResponseInit): NextResponse {
  return NextResponse.json({ ok: true as const, data }, init);
}

export function fail(error: string, status: number, headers?: HeadersInit): NextResponse {
  return NextResponse.json({ ok: false as const, error }, { status, headers });
}

/** Parse and validate a JSON body. Returns a discriminated result. */
export async function parseBody<S extends z.ZodTypeAny>(
  request: Request,
  schema: S,
): Promise<{ ok: true; data: z.infer<S> } | { ok: false; error: string; status: number }> {
  let raw: unknown;
  try {
    raw = await request.json();
  } catch {
    return { ok: false, error: "Request body must be valid JSON", status: 400 };
  }
  const parsed = schema.safeParse(raw);
  if (!parsed.success) {
    const first = parsed.error.issues[0];
    const message = first ? `${first.path.join(".") || "body"}: ${first.message}` : "Invalid request body";
    return { ok: false, error: message, status: 400 };
  }
  return { ok: true, data: parsed.data };
}

/** Require a session; returns the user or a 401 response. */
export async function requireSession(): Promise<
  { user: SessionUser; response: null } | { user: null; response: NextResponse }
> {
  const user = await getSessionUser();
  if (!user) {
    return { user: null, response: fail("You must be logged in to access this app", 401) };
  }
  return { user, response: null };
}
