"use client";

import { AppShell } from "@/components/budget/app-shell";
import { RequireSession } from "@/components/budget/require-session";
import { DashboardView } from "@/components/budget/dashboard-view";

export default function DashboardPage() {
  return (
    <AppShell>
      <RequireSession>
        <DashboardView />
      </RequireSession>
    </AppShell>
  );
}
