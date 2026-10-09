"use client";

// The application shell: boots the session store, renders the sidebar +
// mobile chrome, and hosts every store-driven modal ONCE (no per-page wiring
// — pages only render their views and open modals through the store).

import * as React from "react";
import { useBudgetStore } from "./store";
import { useToast } from "@/components/ui/toast";
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
  const bootError = useBudgetStore((s) => s.bootError);
  const clearBootError = useBudgetStore((s) => s.clearBootError);
  const { toast } = useToast();
  // The mobile nav-sheet state lives here so the mobile top bar can sit
  // INSIDE <main> (reference structure) while the sheet itself renders from
  // the sidebar fragment — see sidebar.tsx for why the top bar must not be
  // a row-flex sibling of <main>.
  const [navOpen, setNavOpen] = React.useState(false);

  React.useEffect(() => {
    void boot();
  }, [boot]);

  // v16 G1: the honest superset for a DATA failure at boot (the session
  // probe succeeded, refresh() threw). The reference renders its silent
  // zero-state here — no error surface at all (a transient network
  // failure looks like an empty budget); the clone keeps the zero-state
  // surfaces (parity) but tells the truth once. One-shot: the flag clears
  // when fired, so a later successful refresh never re-toasts. The toast
  // chrome is the established error variant (XCircle icon, 4s duration).
  React.useEffect(() => {
    if (booted && bootError) {
      toast({
        title: "Could not load your data",
        description: "Network error — check your connection and try again",
        variant: "error",
      });
      clearBootError();
    }
  }, [booted, bootError, toast, clearBootError]);

  // v15 G1 (measured live on the reference): a full-page load renders a
  // DOM-replacing loading state — #root holds ONLY a fixed inset-0 flex
  // centered overlay (the body behind is white; the app's warm background
  // mounts with the shell) wrapping the reference's slate spinner
  // (32×32 border-box, 4px borders: slate-200 #e2e8f0 on three sides +
  // slate-800 #1e293b on top, radius 9999px, spin 1s linear infinite).
  // NO rail, NO header, NO main while `!booted` — the shell doesn't
  // half-render around the spinner. Client-side navigations never hit
  // this branch (the store persists; booted stays true). The hex pins
  // follow the v8 named-palette lesson (the reference's slates compute
  // as plain rgb in its v3 build; v4 would emit lab()), 9999px the v9
  // radius lesson. role="status" + aria-label stay (a11y superset, the
  // documented class — the reference has no aria).
  if (!booted) {
    return (
      <div
        className="fixed inset-0 flex items-center justify-center"
        style={{ background: "#ffffff" }}
      >
        <div
          className="h-8 w-8 animate-spin rounded-[9999px] border-4 border-[#e2e8f0] border-t-[#1e293b]"
          role="status"
          aria-label="Loading"
        />
      </div>
    );
  }

  return (
    // v25 G3 (measured live on the reference): its app shell paints the
    // warm #fafaf8 paper HERE — on the shell wrapper, not the body (its
    // body renders the browser's white canvas; the login gradient and
    // the 404 root cover it elsewhere). The clone had the paper on the
    // body (a v7-era manifest read) — visually invisible but a
    // layer-structure drift; --neutral-warm paints it at the reference's
    // layer.
    <div className="flex min-h-svh w-full bg-(--neutral-warm)">
      <AppSidebar navOpen={navOpen} onNavOpenChange={setNavOpen} />
      {/* min-w-0: as a flex-1 item, main's automatic minimum size is its
          content's min-content width — an unbreakable string (e.g. a long
          net-worth figure) would stretch main past the mobile viewport
          exactly like the reference's own 464px overflow (reference bug R4,
          remediation-plan-v4 G5). min-w-0 pins main to the available space;
          inner overflow-hidden cards clip gracefully instead. */}
      <main className="flex min-w-0 flex-1 flex-col md:pl-(--sidebar-width)">
        <MobileTopbar onOpenNav={() => setNavOpen(true)} />
        {children}
      </main>
      <ModalHost />
    </div>
  );
}
