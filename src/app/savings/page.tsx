"use client";

import { AppShell } from "@/components/budget/app-shell";
import { RequireSession } from "@/components/budget/require-session";
import { ItemsView } from "@/components/budget/items-view";

export default function SavingsPage() {
  return (
    <AppShell>
      <RequireSession>
        <ItemsView type="savings" />
      </RequireSession>
    </AppShell>
  );
}
