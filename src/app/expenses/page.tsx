"use client";

import { AppShell } from "@/components/budget/app-shell";
import { RequireSession } from "@/components/budget/require-session";
import { ItemsView } from "@/components/budget/items-view";

export default function ExpensesPage() {
  return (
    <AppShell>
      <RequireSession>
        <ItemsView type="expense" />
      </RequireSession>
    </AppShell>
  );
}
