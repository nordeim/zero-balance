"use client";

import { AppShell } from "@/components/budget/app-shell";
import { RequireSession } from "@/components/budget/require-session";
import { NetWorthView } from "@/components/budget/net-worth-view";

export default function NetWorthPage() {
  return (
    <AppShell>
      <RequireSession>
        <NetWorthView />
      </RequireSession>
    </AppShell>
  );
}
