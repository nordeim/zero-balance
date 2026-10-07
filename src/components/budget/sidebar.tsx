"use client";

import * as React from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  LayoutDashboardIcon,
  MenuIcon,
  PiggyBankIcon,
  ReceiptIcon,
  TrendingUpIcon,
  WalletIcon,
} from "lucide-react";
import { Dialog, DialogContent, SheetContent, DialogTitle } from "@/components/ui/dialog";
import { useBudgetStore } from "./store";
import { cn } from "@/lib/utils";

const NAV_ITEMS = [
  { href: "/dashboard", label: "Dashboard", icon: LayoutDashboardIcon },
  { href: "/income", label: "Income", icon: WalletIcon },
  { href: "/expenses", label: "Expenses", icon: ReceiptIcon },
  { href: "/savings", label: "Savings", icon: PiggyBankIcon },
  { href: "/networth", label: "Net Worth", icon: TrendingUpIcon },
] as const;

function isActive(pathname: string, href: string): boolean {
  if (href === "/dashboard") return pathname === "/" || pathname === "/dashboard";
  return pathname.startsWith(href);
}

function BrandMark() {
  return (
    <div className="flex items-center gap-3">
      <div
        className="flex h-10 w-10 items-center justify-center rounded-xl"
        style={{ background: "linear-gradient(135deg, var(--forest-dark), var(--forest-medium))" }}
      >
        <svg
          width="20"
          height="20"
          viewBox="0 0 24 24"
          fill="none"
          stroke="white"
          strokeWidth="2"
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
        >
          <circle cx="12" cy="12" r="10" />
          <circle cx="12" cy="12" r="6" />
          <circle cx="12" cy="12" r="2" />
        </svg>
      </div>
      <div>
        <h2 className="text-base font-bold" style={{ color: "var(--forest-dark)" }}>
          ZeroBalance
        </h2>
        <p className="text-xs" style={{ color: "var(--forest-medium)" }}>
          Budget Planner
        </p>
      </div>
    </div>
  );
}

function NavList({ onNavigate, highlightActive = true }: { onNavigate?: () => void; highlightActive?: boolean }) {
  const pathname = usePathname();
  return (
    <nav aria-label="Primary">
      <div
        className="flex h-8 shrink-0 items-center rounded-md px-3 py-2 text-xs font-semibold uppercase tracking-wider"
        style={{ color: "var(--forest-medium)" }}
      >
        Navigation
      </div>
      <ul className="flex w-full min-w-0 flex-col gap-1">
        {NAV_ITEMS.map(({ href, label, icon: Icon }) => {
          const active = isActive(pathname, href);
          return (
            <li key={href} className="relative">
              <Link
                href={href}
                onClick={onNavigate}
                aria-current={active ? "page" : undefined}
                className={cn(
                  "flex w-full items-center gap-3 rounded-lg px-3 py-2.5 text-sm transition-all duration-200 mb-1 outline-none focus-visible:ring-2 focus-visible:ring-ring",
                  active && highlightActive
                    ? "font-medium text-white hover:opacity-90"
                    : "text-zinc-700 hover:bg-sidebar-accent hover:text-sidebar-accent-foreground",
                )}
                style={
                  active && highlightActive
                    ? {
                        background:
                          "linear-gradient(135deg, var(--forest-medium), var(--lime-green))",
                      }
                    : undefined
                }
              >
                <Icon className="h-4 w-4 shrink-0" aria-hidden="true" />
                <span className="truncate">{label}</span>
              </Link>
            </li>
          );
        })}
      </ul>
    </nav>
  );
}

function UserFooter() {
  const user = useBudgetStore((s) => s.user);
  // The reference renders "U" for a nameless account — derive from the
  // name only, defaulting to the same "U" fallback.
  const initial = user?.name?.trim() ? user.name.trim().charAt(0).toUpperCase() : "U";
  return (
    <div className="flex flex-col gap-2 border-t p-4" style={{ borderColor: "rgb(229, 231, 227)" }}>
      <div
        className="flex items-center gap-3 rounded-lg p-3"
        style={{ backgroundColor: "rgb(245, 248, 245)" }}
      >
        <div
          className="flex h-9 w-9 items-center justify-center rounded-full font-semibold text-sm text-white"
          style={{ backgroundColor: "var(--lime-green)" }}
        >
          {initial}
        </div>
        <div className="min-w-0 flex-1">
          <p className="truncate text-sm font-medium" style={{ color: "var(--forest-dark)" }}>
            Budget Pro
          </p>
          <p className="truncate text-xs" style={{ color: "var(--forest-medium)" }}>
            Track your finances
          </p>
        </div>
      </div>
    </div>
  );
}

function SidebarBody({ onNavigate, highlightActive = true }: { onNavigate?: () => void; highlightActive?: boolean }) {
  return (
    <div className="flex h-full w-full flex-col bg-sidebar">
      <div
        className="flex flex-col gap-2 border-b p-6"
        style={{ borderColor: "rgb(229, 231, 227)" }}
      >
        <BrandMark />
      </div>
      <div className="flex min-h-0 flex-1 flex-col gap-2 overflow-auto p-3">
        <div className="relative flex w-full min-w-0 flex-col p-2">
          <NavList onNavigate={onNavigate} highlightActive={highlightActive} />
        </div>
      </div>
      <UserFooter />
    </div>
  );
}

/** Desktop sidebar (fixed 16rem rail) + mobile top bar + sheet navigation. */
export function AppSidebar() {
  const [open, setOpen] = React.useState(false);
  const pathname = usePathname();

  // Route changes close the sheet — the reference leaves it open after a nav
  // click (its menu traps the user behind the overlay); closing is the
  // documented superset fix. Resetting during render (the React "adjust
  // state when a value changes" pattern) instead of in an effect avoids the
  // cascading-render lint error.
  const [prevPathname, setPrevPathname] = React.useState(pathname);
  if (prevPathname !== pathname) {
    setPrevPathname(pathname);
    setOpen(false);
  }

  return (
    <>
      {/* Desktop rail */}
      <aside className="fixed inset-y-0 left-0 z-10 hidden h-svh w-(--sidebar-width) border-r md:flex">
        <SidebarBody />
      </aside>

      {/* Mobile top bar */}
      <header
        className="border-b bg-white px-6 py-4 md:hidden"
        style={{ borderColor: "rgb(229, 231, 227)" }}
      >
        <div className="flex items-center gap-3">
          <button
            type="button"
            aria-label="Toggle Sidebar"
            className="inline-flex h-9 w-9 items-center justify-center rounded-md transition-colors hover:bg-accent"
            onClick={() => setOpen(true)}
          >
            <MenuIcon className="h-5 w-5" style={{ color: "var(--forest-dark)" }} />
          </button>
          <h1 className="text-lg font-bold" style={{ color: "var(--forest-dark)" }}>
            ZeroBalance
          </h1>
        </div>
      </header>

      {/* Mobile sheet */}
      <Dialog open={open} onOpenChange={setOpen}>
        <SheetContent>
          <DialogTitle className="sr-only">Navigation</DialogTitle>
          <SidebarBody onNavigate={() => setOpen(false)} highlightActive={false} />
        </SheetContent>
      </Dialog>
    </>
  );
}
