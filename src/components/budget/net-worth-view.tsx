"use client";

// Net Worth — the forest→lime gradient summary card (Total Net Worth, Total
// Assets, Total Liabilities, Asset-to-Liability Ratio "0.21:1" / "∞:1") and
// the Assets / Liabilities tabs. Lists are grouped BY TYPE under capitalize
// h3 headers; cards carry the dot + name + gray type badge structure, grouped
// amounts and stacked footer lines (institution / % interest / Updated).
// Pinned by the session-3 audit (docs/remediation-plan-v2.md F12).

import * as React from "react";
import {
  Building2Icon,
  CalendarIcon,
  CircleArrowDownIcon,
  CircleArrowUpIcon,
  EllipsisVerticalIcon,
  PlusIcon,
  PercentIcon,
  TrendingUpIcon,
} from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { useToast } from "@/components/ui/toast";
import { messageOf, useBudgetStore } from "./store";
import { computeNetWorth } from "@/lib/dashboard";
import { formatMoneyGrouped, formatMoneyShort, formatRatio } from "@/lib/money";
import {
  ADD_BUTTON_GRADIENTS,
  ASSET_LABELS,
  COLORS,
  LIABILITY_LABELS,
  rgb,
} from "@/lib/constants";
import type { Asset, Liability } from "@/lib/types";

const ASSET_COLOR = COLORS.limeGreen;
const LIABILITY_COLOR = COLORS.orangeDark;

function formatDate(iso: string): string {
  const d = new Date(`${iso}T00:00:00`);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
}

/** Type-group key: the raw type with underscores → spaces (the reference's
 *  h3 headers rely on the CSS `capitalize` class for visual casing). */
function groupLabel(type: string): string {
  return type.replace(/_/g, " ");
}

function AssetCard({ asset }: { asset: Asset }) {
  const openAssetModal = useBudgetStore((s) => s.openAssetModal);
  const deleteAsset = useBudgetStore((s) => s.deleteAsset);
  const { toast } = useToast();
  const [confirming, setConfirming] = React.useState(false);
  return (
    <div
      className="group rounded-xl border bg-white p-5 transition-all duration-200 hover:shadow-lg"
      style={{ borderColor: rgb.border, boxShadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px" }}
    >
      <div className="mb-3 flex items-start justify-between">
        <div className="flex-1">
          <div className="mb-1 flex items-center gap-2">
            <div className="h-2 w-2 rounded-[9999px]" style={{ backgroundColor: ASSET_COLOR }} />
            <h4 className="font-semibold" style={{ color: rgb.forestDark }}>
              {asset.name}
            </h4>
          </div>
          <span className="inline-flex items-center rounded-md border border-transparent bg-[#f3f4f6] px-2.5 py-0.5 text-xs font-semibold text-[#374151] transition-colors zb-badge-hover">
            {ASSET_LABELS[asset.type]}
          </span>
        </div>
        <DropdownMenu>
          <DropdownMenuTrigger
            className="inline-flex h-9 w-9 items-center justify-center rounded-md opacity-0 transition-opacity hover:bg-accent hover:text-accent-foreground focus-visible:opacity-100 group-hover:opacity-100 data-[state=open]:opacity-100"
            aria-label={`Actions for ${asset.name}`}
          >
            <EllipsisVerticalIcon className="h-4 w-4" />
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            {/* Plain-text items + hex-pinned red (reference — v6 G1/G2). */}
            <DropdownMenuItem onSelect={() => openAssetModal({ mode: "edit", asset })}>
              Edit
            </DropdownMenuItem>
            <DropdownMenuItem
              className="text-[#dc2626] focus:text-[#dc2626]"
              onSelect={() => setConfirming(true)}
            >
              Delete
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
      <p className="mb-2 text-2xl font-bold" style={{ color: ASSET_COLOR }}>
        {formatMoneyGrouped(asset.value)}
      </p>
      <div className="space-y-2 text-xs" style={{ color: rgb.gray }}>
        {asset.institution && (
          <div className="flex items-center gap-2">
            <Building2Icon className="h-3 w-3" />
            {asset.institution}
          </div>
        )}
        <div className="flex items-center gap-2">
          <CalendarIcon className="h-3 w-3" />
          Updated {formatDate(asset.lastUpdated)}
        </div>
      </div>
      {confirming && (
        <div
          className="mt-4 flex items-center justify-between rounded-lg p-3"
          style={{ backgroundColor: "rgb(254, 242, 242)" }}
        >
          <p className="text-sm text-red-700">Delete this asset?</p>
          <div className="flex gap-2">
            <button
              type="button"
              className="rounded-md bg-white px-3 py-1 text-xs font-medium text-slate-700 shadow-sm"
              onClick={() => setConfirming(false)}
            >
              Cancel
            </button>
            <button
              type="button"
              className="rounded-md bg-red-600 px-3 py-1 text-xs font-medium text-white"
              onClick={() =>
                // v18 G1: the delete failure must be CAUGHT, not swallowed
                // — the pre-fix `void deleteAsset(asset.id)` left the
                // rejection unhandled and silent. The reference's failed
                // delete is a silent no-op (card stays, no feedback —
                // measured live, plan v18); the clone keeps the surfaces
                // (the card stays, the confirm bar stays — the store only
                // filters state AFTER the API resolves) and adds the
                // honest error toast, the same superset class as the
                // dialogs' catch toasts and the v16/v17 tiers. Per-click
                // semantics (a fresh user action each time).
                deleteAsset(asset.id).catch((error: unknown) => {
                  toast({
                    title: "Could not delete the asset",
                    description: messageOf(error),
                    variant: "error",
                  });
                })
              }
            >
              Delete
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

function LiabilityCard({ liability }: { liability: Liability }) {
  const openLiabilityModal = useBudgetStore((s) => s.openLiabilityModal);
  const deleteLiability = useBudgetStore((s) => s.deleteLiability);
  const { toast } = useToast();
  const [confirming, setConfirming] = React.useState(false);
  return (
    <div
      className="group rounded-xl border bg-white p-5 transition-all duration-200 hover:shadow-lg"
      style={{ borderColor: rgb.border, boxShadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px" }}
    >
      <div className="mb-3 flex items-start justify-between">
        <div className="flex-1">
          <div className="mb-1 flex items-center gap-2">
            <div className="h-2 w-2 rounded-[9999px]" style={{ backgroundColor: LIABILITY_COLOR }} />
            <h4 className="font-semibold" style={{ color: rgb.forestDark }}>
              {liability.name}
            </h4>
          </div>
          <span className="inline-flex items-center rounded-md border border-transparent bg-[#f3f4f6] px-2.5 py-0.5 text-xs font-semibold text-[#374151] transition-colors zb-badge-hover">
            {LIABILITY_LABELS[liability.type]}
          </span>
        </div>
        <DropdownMenu>
          <DropdownMenuTrigger
            className="inline-flex h-9 w-9 items-center justify-center rounded-md opacity-0 transition-opacity hover:bg-accent hover:text-accent-foreground focus-visible:opacity-100 group-hover:opacity-100 data-[state=open]:opacity-100"
            aria-label={`Actions for ${liability.name}`}
          >
            <EllipsisVerticalIcon className="h-4 w-4" />
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuItem onSelect={() => openLiabilityModal({ mode: "edit", liability })}>
              Edit
            </DropdownMenuItem>
            <DropdownMenuItem
              className="text-[#dc2626] focus:text-[#dc2626]"
              onSelect={() => setConfirming(true)}
            >
              Delete
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
      <p className="mb-2 text-2xl font-bold" style={{ color: LIABILITY_COLOR }}>
        {formatMoneyGrouped(liability.value)}
      </p>
      <div className="space-y-2 text-xs" style={{ color: rgb.gray }}>
        {liability.institution && (
          <div className="flex items-center gap-2">
            <Building2Icon className="h-3 w-3" />
            {liability.institution}
          </div>
        )}
        {liability.interestRate !== null && liability.interestRate !== undefined && (
          <div className="flex items-center gap-2">
            <PercentIcon className="h-3 w-3" />
            {liability.interestRate}% interest
          </div>
        )}
        <div className="flex items-center gap-2">
          <CalendarIcon className="h-3 w-3" />
          Updated {formatDate(liability.lastUpdated)}
        </div>
      </div>
      {confirming && (
        <div
          className="mt-4 flex items-center justify-between rounded-lg p-3"
          style={{ backgroundColor: "rgb(254, 242, 242)" }}
        >
          <p className="text-sm text-red-700">Delete this liability?</p>
          <div className="flex gap-2">
            <button
              type="button"
              className="rounded-md bg-white px-3 py-1 text-xs font-medium text-slate-700 shadow-sm"
              onClick={() => setConfirming(false)}
            >
              Cancel
            </button>
            <button
              type="button"
              className="rounded-md bg-red-600 px-3 py-1 text-xs font-medium text-white"
              onClick={() =>
                // v18 G1 (liability twin): same caught-rejection + honest
                // toast as the asset path above.
                deleteLiability(liability.id).catch((error: unknown) => {
                  toast({
                    title: "Could not delete the liability",
                    description: messageOf(error),
                    variant: "error",
                  });
                })
              }
            >
              Delete
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

/** Group entries by type, preserving first-occurrence order (the reference
 *  iterates Object.entries over its grouping accumulator). */
function groupByType<T extends { type: string }>(items: T[]): [string, T[]][] {
  const groups = new Map<string, T[]>();
  for (const it of items) {
    const list = groups.get(it.type);
    if (list) list.push(it);
    else groups.set(it.type, [it]);
  }
  return [...groups.entries()];
}

export function NetWorthView() {
  const assets = useBudgetStore((s) => s.assets);
  const liabilities = useBudgetStore((s) => s.liabilities);
  const openAssetModal = useBudgetStore((s) => s.openAssetModal);
  const openLiabilityModal = useBudgetStore((s) => s.openLiabilityModal);
  const totals = computeNetWorth(assets, liabilities);

  // G13: the reference wraps `max-w-7xl mx-auto` INSIDE `min-h-screen
  // p-4 md:p-8` — padding OUTSIDE the 1280px cap, so the column is
  // min(vw − 256 − 64, 1280) at every viewport.
  return (
    <div className="min-h-screen p-4 md:p-8">
    <div className="mx-auto w-full max-w-7xl">
      {/* v14 G3 (measured live, both viewports): the reference's /networth
          header is a flex items-center gap-3 row — a 48×48 gradient chip
          (radius 12, forest-medium→lime 135deg) wrapping a 24×24 white
          lucide-trending-up, then the h1+p block. Same pattern as the
          items-view chips (HEADER_CHIP_GRADIENTS); the reference renders NO
          chip on the dashboard. */}
      <div className="mb-6 flex items-center gap-3">
        <div
          className="flex h-12 w-12 items-center justify-center rounded-xl"
          style={{ background: "linear-gradient(135deg, #2d5a4a, #8fbc3f)" }}
        >
          <TrendingUpIcon className="h-6 w-6 text-white" />
        </div>
        <div>
          <h1 className="text-3xl font-bold" style={{ color: rgb.forestDark }}>
            Net Worth
          </h1>
          <p style={{ color: rgb.gray }}>Track your assets and liabilities</p>
        </div>
      </div>

      <div
        className="relative mb-6 overflow-hidden rounded-2xl p-8"
        style={{
          background: `linear-gradient(135deg, ${COLORS.forestMedium} 0%, ${COLORS.limeGreen} 100%)`,
          boxShadow: "rgba(26, 58, 46, 0.3) 0px 20px 60px",
        }}
      >
        <div
          aria-hidden="true"
          className="absolute top-0 right-0 h-64 w-64 rounded-[9999px] opacity-10"
          style={{
            background: "radial-gradient(circle, white 0%, transparent 70%)",
            transform: "translate(30%, -30%)",
          }}
        />
        <div className="relative z-10">
          <div className="mb-8 flex items-center justify-between gap-4">
            <div className="min-w-0">
              <p className="mb-2 text-sm" style={{ color: "rgba(255, 255, 255, 0.8)" }}>Total Net Worth</p>
              {/* text-2xl on phones so long figures fit beside the icon in
                 the 390px content box (the reference's fixed text-5xl
                 overflows its mobile viewport by 74px — reference bug R4,
                 superset fix #6); 48px from sm up = reference parity.
                 break-words guards pathological figures. */}
              <h2 className="break-words text-2xl font-bold text-white sm:text-5xl">
                {formatMoneyGrouped(totals.netWorth)}
              </h2>
            </div>
            <div
              className="flex h-16 w-16 shrink-0 items-center justify-center rounded-[9999px]"
              style={{ backgroundColor: "rgba(255, 255, 255, 0.2)" }}
            >
              <TrendingUpIcon className="h-8 w-8 text-white" />
            </div>
          </div>
          {/* Reference layout (session-7 audit, remediation-plan-v4 G4):
              TWO stat cards (Assets, Liabilities) in a 2-col grid — labels
              text-xs text-white/70, amounts text-2xl, backdrop blur — with
              the ratio in a separate border-t footer row (text-lg). The
              grid stacks to 1 col on phones so the amounts never crush
              (the reference's fixed 2-col grid overflows at 390px). */}
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div
              className="rounded-xl p-4"
              style={{ backgroundColor: "rgba(255,255,255,0.1)", backdropFilter: "blur(10px)" }}
            >
              <p className="mb-1 text-xs" style={{ color: "rgba(255, 255, 255, 0.7)" }}>Total Assets</p>
              <p className="text-2xl font-bold text-white">{formatMoneyGrouped(totals.totalAssets)}</p>
            </div>
            <div
              className="rounded-xl p-4"
              style={{ backgroundColor: "rgba(255,255,255,0.1)", backdropFilter: "blur(10px)" }}
            >
              <p className="mb-1 text-xs" style={{ color: "rgba(255, 255, 255, 0.7)" }}>Total Liabilities</p>
              <p className="text-2xl font-bold text-white">{formatMoneyGrouped(totals.totalLiabilities)}</p>
            </div>
          </div>
          {/* Inline border color — Tailwind v4 emits border-white/20 as
              oklab(...) (the oklch-drift trap); the inline rgba matches the
              reference's computed rgba(255,255,255,0.2) byte-for-byte. */}
          <div
            className="mt-6 pt-6"
            style={{ borderTop: "1px solid rgba(255, 255, 255, 0.2)" }}
          >
            <div className="flex items-center justify-between">
              <span className="text-sm" style={{ color: "rgba(255, 255, 255, 0.8)" }}>Asset to Liability Ratio</span>
              {/* Reference: ".toFixed(2)" + ":1" with no spaces, "∞" when
                  debt-free (bundle: [t>0?(e/t).toFixed(2):"∞",":1"]). */}
              <span className="text-lg font-bold text-white">
                {formatRatio(totals.ratio)}:1
              </span>
            </div>
          </div>
        </div>
      </div>

      <Tabs defaultValue="assets">
        <TabsList className="grid w-full max-w-md grid-cols-2">
          {/* v14 G2 (measured live): the reference's triggers carry 16px
              lucide icons (circle-arrow-up / circle-arrow-down, mr-2,
              stroke=currentColor) that inherit the tab's text color. */}
          <TabsTrigger value="assets">
            <CircleArrowUpIcon className="mr-2 h-4 w-4" />
            Assets
          </TabsTrigger>
          <TabsTrigger value="liabilities">
            <CircleArrowDownIcon className="mr-2 h-4 w-4" />
            Liabilities
          </TabsTrigger>
        </TabsList>

        <TabsContent value="assets" className="mt-6 space-y-6">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-2xl font-bold" style={{ color: rgb.forestDark }}>
                Assets
              </h2>
              <p style={{ color: rgb.gray }}>
                {assets.length} items · {formatMoneyShort(totals.totalAssets)}
              </p>
            </div>
            <button
              type="button"
              className="zb-btn-add"
              style={{ background: ADD_BUTTON_GRADIENTS.asset }}
              onClick={() => openAssetModal({ mode: "create" })}
            >
              <PlusIcon className="mr-2 h-4 w-4" />
              Add Asset
            </button>
          </div>
          {assets.length === 0 ? (
            <div
              className="rounded-2xl bg-white py-16 text-center"
              style={{ border: `1px solid ${rgb.border}` }}
            >
              {/* Reference empty state: a BARE icon (circle-arrow-up) w-16
                  h-16 mx-auto mb-4 opacity-20 in the near-black foreground —
                  no tinted circle wrapper (v6 G6). */}
              <CircleArrowUpIcon className="mx-auto mb-4 h-16 w-16 text-[#0a0a0a] opacity-20" />
              <h3 className="mb-2 text-xl font-semibold" style={{ color: rgb.forestDark }}>
                No assets yet
              </h3>
              <p className="mb-6 text-base" style={{ color: rgb.gray }}>
                Start by adding your first asset
              </p>
              <button
                type="button"
                className="zb-btn-add"
                style={{ background: ADD_BUTTON_GRADIENTS.asset }}
                onClick={() => openAssetModal({ mode: "create" })}
              >
                <PlusIcon className="mr-2 h-4 w-4" />
                Add Asset
              </button>
            </div>
          ) : (
            groupByType(assets).map(([type, list]) => (
              <div key={type}>
                <h3
                  className="mb-3 text-lg font-semibold capitalize"
                  style={{ color: COLORS.forestMedium }}
                >
                  {groupLabel(type)}
                </h3>
                <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
                  {list.map((a) => (
                    <AssetCard key={a.id} asset={a} />
                  ))}
                </div>
              </div>
            ))
          )}
        </TabsContent>

        <TabsContent value="liabilities" className="mt-6 space-y-6">
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-2xl font-bold" style={{ color: rgb.forestDark }}>
                Liabilities
              </h2>
              <p style={{ color: rgb.gray }}>
                {liabilities.length} items · {formatMoneyShort(totals.totalLiabilities)}
              </p>
            </div>
            <button
              type="button"
              className="zb-btn-add"
              style={{ background: ADD_BUTTON_GRADIENTS.liability }}
              onClick={() => openLiabilityModal({ mode: "create" })}
            >
              <PlusIcon className="mr-2 h-4 w-4" />
              Add Liability
            </button>
          </div>
          {liabilities.length === 0 ? (
            <div
              className="rounded-2xl bg-white py-16 text-center"
              style={{ border: `1px solid ${rgb.border}` }}
            >
              {/* Reference empty state: a BARE circle-arrow-down icon —
                  no tinted circle wrapper (v6 G6). */}
              <CircleArrowDownIcon className="mx-auto mb-4 h-16 w-16 text-[#0a0a0a] opacity-20" />
              <h3 className="mb-2 text-xl font-semibold" style={{ color: rgb.forestDark }}>
                No liabilities yet
              </h3>
              <p className="mb-6 text-base" style={{ color: rgb.gray }}>
                Add any outstanding debts or loans
              </p>
              <button
                type="button"
                className="zb-btn-add"
                style={{ background: ADD_BUTTON_GRADIENTS.liability }}
                onClick={() => openLiabilityModal({ mode: "create" })}
              >
                <PlusIcon className="mr-2 h-4 w-4" />
                Add Liability
              </button>
            </div>
          ) : (
            groupByType(liabilities).map(([type, list]) => (
              <div key={type}>
                <h3
                  className="mb-3 text-lg font-semibold capitalize"
                  style={{ color: LIABILITY_COLOR }}
                >
                  {groupLabel(type)}
                </h3>
                <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
                  {list.map((l) => (
                    <LiabilityCard key={l.id} liability={l} />
                  ))}
                </div>
              </div>
            ))
          )}
        </TabsContent>
      </Tabs>
    </div>
    </div>
  );
}
