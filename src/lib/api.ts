// Typed client for the JSON API — unwraps the { ok, data } | { ok, error }
// envelope and turns network/HTTP failures into thrown Errors the store's
// actions catch for toast surfaces.

export class ApiError extends Error {
  constructor(
    message: string,
    public readonly status: number,
    options?: ErrorOptions,
  ) {
    super(message, options);
    this.name = "ApiError";
  }
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  let response: Response;
  try {
    response = await fetch(path, {
      ...init,
      headers: {
        "Content-Type": "application/json",
        ...(init?.headers ?? {}),
      },
      credentials: "same-origin",
    });
  } catch (cause) {
    throw new ApiError("Network error — check your connection and try again", 0, { cause });
  }
  let body: unknown;
  try {
    body = await response.json();
  } catch {
    throw new ApiError(`Unexpected response from server (${response.status})`, response.status);
  }
  if (body && typeof body === "object" && "ok" in body) {
    const envelope = body as { ok: boolean; data?: unknown; error?: string };
    if (envelope.ok) {
      return envelope.data as T;
    }
    throw new ApiError(envelope.error ?? "Request failed", response.status);
  }
  throw new ApiError(`Unexpected response from server (${response.status})`, response.status);
}

export const api = {
  get: <T>(path: string) => request<T>(path),
  post: <T>(path: string, body: unknown) =>
    request<T>(path, { method: "POST", body: JSON.stringify(body) }),
  patch: <T>(path: string, body: unknown) =>
    request<T>(path, { method: "PATCH", body: JSON.stringify(body) }),
  delete: <T>(path: string) => request<T>(path, { method: "DELETE" }),
};
