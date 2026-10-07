"use client";

// The application shell: boots the session store, renders the sidebar +
// mobile chrome, and hosts every store-driven modal ONCE (no per-page wiring
// — pages only render their views and open modals through the store).

import * as React from "react";
import { useBudgetStore } from "./store";
import { AppSidebar, MobileTopbar } from "./sidebar";
import { BudgetItemDialog } from "./budget-item-dialog";
import { CalculatorDialog } from "./calculator-dialog";
import { LineItemDialog } from "./line-item-dialog";
import { AssetDialog } from "./asset-dialog";
import { LiabilityDialog } from "./liability-dialog";

function ModalHost() {
  const modal = useBudgetStore((s) => s.modal);
  return (
    <>
      {modal.item && <BudgetItemDialog key="item" />}
      {modal.calculator && <CalculatorDialog key="calculator" />}
      {modal.lineItem && <LineItemDialog key="line-item" />}
      {modal.asset && <AssetDialog key="asset" />}
      {modal.liability && <LiabilityDialog key="liability" />}
    </>
  );
}

export function AppShell({ children }: { children: React.ReactNode }) {
  const boot = useBudgetStore((s) => s.boot);
  const booted = useBudgetStore((s) => s.booted);
  // The mobile nav-sheet state lives here so the mobile top bar can sit
  // INSIDE <main> (reference structure) while the sheet itself renders from
  // the sidebar fragment — see sidebar.tsx for why the top bar must not be
  // a row-flex sibling of <main>.
  const [navOpen, setNavOpen] = React.useState(false);

  React.useEffect(() => {
    void boot();
  }, [boot]);

  return (
    <div className="flex min-h-svh w-full">
      <AppSidebar navOpen={navOpen} onNavOpenChange={setNavOpen} />
      {/* min-w-0: as a flex-1 item, main's automatic minimum size is its
          content's min-content width — an unbreakable string (e.g. a long
          net-worth figure) would stretch main past the mobile viewport
          exactly like the reference's own 464px overflow (reference bug R4,
          remediation-plan-v4 G5). min-w-0 pins main to the available space;
          inner overflow-hidden cards clip gracefully instead. */}
      <main className="flex min-w-0 flex-1 flex-col md:pl-(--sidebar-width)">
        <MobileTopbar onOpenNav={() => setNavOpen(true)} />
        {booted ? (
          children
        ) : (
          <div className="flex flex-1 items-center justify-center p-8">
            <div
              className="h-8 w-8 animate-spin rounded-full border-2 border-t-transparent"
              style={{ borderColor: "var(--lime-green)", borderTopColor: "transparent" }}
              role="status"
              aria-label="Loading"
            />
          </div>
        )}
      </main>
      <ModalHost />
    </div>
  );
}
