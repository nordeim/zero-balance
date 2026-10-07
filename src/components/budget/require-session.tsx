"use client";

// Auth gate for workspace pages: once the session probe resolves, an
// unauthenticated visitor is sent to /login with ?from_url= return handling
// — the reference's redirect behavior.

import * as React from "react";
import { usePathname, useRouter } from "next/navigation";
import { useBudgetStore } from "./store";

export function RequireSession({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const pathname = usePathname();
  const booted = useBudgetStore((s) => s.booted);
  const user = useBudgetStore((s) => s.user);

  React.useEffect(() => {
    if (booted && !user) {
      const from = encodeURIComponent(pathname === "/" ? "/" : pathname);
      router.replace(`/login?from_url=${from}`);
    }
  }, [booted, user, pathname, router]);

  return <>{children}</>;
}
