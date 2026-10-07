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
  EllipsisVerticalIcon,
  PencilIcon,
  PlusIcon,
  PercentIcon,
  Trash2Icon,
  TrendingUpIcon,
  CreditCardIcon,
} from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { useBudgetStore } from "./store";
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
  const [confirming, setConfirming] = React.useState(false);
  return (
    <div
      className="group rounded-xl border bg-white p-5 transition-all duration-200 hover:shadow-lg"
      style={{ borderColor: rgb.border, boxShadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px" }}
    >
      <div className="mb-3 flex items-start justify-between">
        <div className="flex-1">
          <div className="mb-1 flex items-center gap-2">
            <div className="h-2 w-2 rounded-full" style={{ backgroundColor: ASSET_COLOR }} />
            <h4 className="font-semibold" style={{ color: rgb.forestDark }}>
              {asset.name}
            </h4>
          </div>
          <span className="inline-flex items-center rounded-md border border-transparent bg-gray-100 px-2.5 py-0.5 text-xs font-semibold text-gray-700">
            {ASSET_LABELS[asset.type]}
          </span>
        </div>
        <DropdownMenu>
          <DropdownMenuTrigger
            className="inline-flex h-9 w-9 items-center justify-center rounded-md opacity-0 transition-opacity hover:bg-accent focus-visible:opacity-100 group-hover:opacity-100 data-[state=open]:opacity-100"
            aria-label={`Actions for ${asset.name}`}
          >
            <EllipsisVerticalIcon className="h-4 w-4" />
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuItem onSelect={() => openAssetModal({ mode: "edit", asset })}>
              <PencilIcon />
              Edit
            </DropdownMenuItem>
            <DropdownMenuItem
              className="text-red-600 focus:text-red-600"
              onSelect={() => setConfirming(true)}
            >
              <Trash2Icon />
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
              onClick={() => void deleteAsset(asset.id)}
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
  const [confirming, setConfirming] = React.useState(false);
  return (
    <div
      className="group rounded-xl border bg-white p-5 transition-all duration-200 hover:shadow-lg"
      style={{ borderColor: rgb.border, boxShadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px" }}
    >
      <div className="mb-3 flex items-start justify-between">
        <div className="flex-1">
          <div className="mb-1 flex items-center gap-2">
            <div className="h-2 w-2 rounded-full" style={{ backgroundColor: LIABILITY_COLOR }} />
            <h4 className="font-semibold" style={{ color: rgb.forestDark }}>
              {liability.name}
            </h4>
          </div>
          <span className="inline-flex items-center rounded-md border border-transparent bg-gray-100 px-2.5 py-0.5 text-xs font-semibold text-gray-700">
            {LIABILITY_LABELS[liability.type]}
          </span>
        </div>
        <DropdownMenu>
          <DropdownMenuTrigger
            className="inline-flex h-9 w-9 items-center justify-center rounded-md opacity-0 transition-opacity hover:bg-accent focus-visible:opacity-100 group-hover:opacity-100 data-[state=open]:opacity-100"
            aria-label={`Actions for ${liability.name}`}
          >
            <EllipsisVerticalIcon className="h-4 w-4" />
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuItem onSelect={() => openLiabilityModal({ mode: "edit", liability })}>
              <PencilIcon />
              Edit
            </DropdownMenuItem>
            <DropdownMenuItem
              className="text-red-600 focus:text-red-600"
              onSelect={() => setConfirming(true)}
            >
              <Trash2Icon />
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
              onClick={() => void deleteLiability(liability.id)}
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

  return (
    <div className="mx-auto w-full max-w-7xl p-4 md:p-8">
      <div className="mb-6">
        <h1 className="text-3xl font-bold" style={{ color: rgb.forestDark }}>
          Net Worth
        </h1>
        <p style={{ color: rgb.gray }}>Track your assets and liabilities</p>
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
          className="absolute top-0 right-0 h-64 w-64 rounded-full opacity-10"
          style={{
            background: "radial-gradient(circle, white 0%, transparent 70%)",
            transform: "translate(30%, -30%)",
          }}
        />
        <div className="relative z-10">
          <div className="mb-8 flex items-center justify-between gap-4">
            <div className="min-w-0">
              <p className="mb-2 text-sm text-white/80">Total Net Worth</p>
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
              className="flex h-16 w-16 shrink-0 items-center justify-center rounded-full"
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
              <p className="mb-1 text-xs text-white/70">Total Assets</p>
              <p className="text-2xl font-bold text-white">{formatMoneyGrouped(totals.totalAssets)}</p>
            </div>
            <div
              className="rounded-xl p-4"
              style={{ backgroundColor: "rgba(255,255,255,0.1)", backdropFilter: "blur(10px)" }}
            >
              <p className="mb-1 text-xs text-white/70">Total Liabilities</p>
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
              <span className="text-sm text-white/80">Asset to Liability Ratio</span>
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
        <TabsList className="mb-4">
          <TabsTrigger value="assets">Assets</TabsTrigger>
          <TabsTrigger value="liabilities">Liabilities</TabsTrigger>
        </TabsList>

        <TabsContent value="assets" className="mt-2 space-y-6">
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
              <PlusIcon className="mr-2 h-5 w-5" />
              Add Asset
            </button>
          </div>
          {assets.length === 0 ? (
            <div
              className="flex flex-col items-center justify-center rounded-2xl bg-white py-16 text-center"
              style={{ border: `1px solid ${rgb.border}` }}
            >
              <div
                className="mb-4 flex h-16 w-16 items-center justify-center rounded-full"
                style={{ backgroundColor: "rgba(143, 188, 63, 0.125)" }}
              >
                <TrendingUpIcon className="h-8 w-8" style={{ color: ASSET_COLOR }} />
              </div>
              <h3 className="mb-1 text-lg font-semibold" style={{ color: rgb.forestDark }}>
                No assets yet
              </h3>
              <p className="mb-6 text-sm" style={{ color: rgb.gray }}>
                Start by adding your first asset
              </p>
              <button
                type="button"
                className="zb-btn-add"
                style={{ background: ADD_BUTTON_GRADIENTS.asset }}
                onClick={() => openAssetModal({ mode: "create" })}
              >
                <PlusIcon className="mr-2 h-5 w-5" />
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

        <TabsContent value="liabilities" className="mt-2 space-y-6">
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
              <PlusIcon className="mr-2 h-5 w-5" />
              Add Liability
            </button>
          </div>
          {liabilities.length === 0 ? (
            <div
              className="flex flex-col items-center justify-center rounded-2xl bg-white py-16 text-center"
              style={{ border: `1px solid ${rgb.border}` }}
            >
              <div
                className="mb-4 flex h-16 w-16 items-center justify-center rounded-full"
                style={{ backgroundColor: "rgba(224, 122, 59, 0.125)" }}
              >
                <CreditCardIcon className="h-8 w-8" style={{ color: LIABILITY_COLOR }} />
              </div>
              <h3 className="mb-1 text-lg font-semibold" style={{ color: rgb.forestDark }}>
                No liabilities yet
              </h3>
              <p className="mb-6 text-sm" style={{ color: rgb.gray }}>
                Add any outstanding debts or loans
              </p>
              <button
                type="button"
                className="zb-btn-add"
                style={{ background: ADD_BUTTON_GRADIENTS.liability }}
                onClick={() => openLiabilityModal({ mode: "create" })}
              >
                <PlusIcon className="mr-2 h-5 w-5" />
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
  );
}
