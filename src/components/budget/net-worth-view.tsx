"use client";

// Net Worth — the forest→lime gradient summary card (Total Net Worth, Total
// Assets, Total Liabilities, Asset-to-Liability Ratio) and the Assets /
// Liabilities tabs with their cards, add buttons and empty states.

import * as React from "react";
import {
  BanknoteIcon,
  Building2Icon,
  CarIcon,
  CreditCardIcon,
  EllipsisVerticalIcon,
  GraduationCapIcon,
  HandCoinsIcon,
  HomeIcon,
  LandmarkIcon,
  LineChartIcon,
  PencilIcon,
  PlusIcon,
  Trash2Icon,
  TrendingUpIcon,
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
import { formatMoney, formatMoneyShort, formatRatio } from "@/lib/money";
import { ASSET_LABELS, LIABILITY_LABELS, rgb } from "@/lib/constants";
import { hexToRgba } from "@/lib/utils";
import type { Asset, AssetType, Liability, LiabilityType } from "@/lib/types";

const ASSET_ICONS: Record<AssetType, React.ComponentType<{ className?: string; style?: React.CSSProperties }>> = {
  bank_account: BanknoteIcon,
  superannuation: HandCoinsIcon,
  property: HomeIcon,
  investment: LineChartIcon,
  vehicle: CarIcon,
  other: Building2Icon,
};

const LIABILITY_ICONS: Record<LiabilityType, React.ComponentType<{ className?: string; style?: React.CSSProperties }>> = {
  home_loan: HomeIcon,
  personal_loan: HandCoinsIcon,
  credit_card: CreditCardIcon,
  car_loan: CarIcon,
  student_loan: GraduationCapIcon,
  other: LandmarkIcon,
};

function formatDate(iso: string): string {
  const d = new Date(`${iso}T00:00:00`);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
}

function AssetCard({ asset }: { asset: Asset }) {
  const openAssetModal = useBudgetStore((s) => s.openAssetModal);
  const deleteAsset = useBudgetStore((s) => s.deleteAsset);
  const [confirming, setConfirming] = React.useState(false);
  const Icon = ASSET_ICONS[asset.type] ?? Building2Icon;
  return (
    <div
      className="rounded-xl bg-white p-5 transition-all duration-200 hover:shadow-lg"
      style={{ border: `1px solid ${rgb.border}`, boxShadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px" }}
    >
      <div className="mb-3 flex items-start justify-between">
        <div className="flex items-center gap-3">
          <div
            className="flex h-10 w-10 items-center justify-center rounded-lg"
            style={{ backgroundColor: hexToRgba("#8fbc3f", 0.125) }}
          >
            <Icon className="h-5 w-5" style={{ color: "#8fbc3f" }} />
          </div>
          <div>
            <h3 className="text-sm font-semibold" style={{ color: rgb.forestMedium }}>
              {ASSET_LABELS[asset.type]}
            </h3>
            <h4 className="font-semibold" style={{ color: rgb.forestDark }}>
              {asset.name}
            </h4>
          </div>
        </div>
        <DropdownMenu>
          <DropdownMenuTrigger
            className="inline-flex h-8 w-8 items-center justify-center rounded-md transition-colors hover:bg-accent"
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
      <p className="mb-2 text-2xl font-bold" style={{ color: "#8fbc3f" }}>
        {formatMoney(asset.value)}
      </p>
      <div className="flex items-center justify-between text-xs" style={{ color: rgb.gray }}>
        <span>{asset.institution ?? ""}</span>
        <span>Updated {formatDate(asset.lastUpdated)}</span>
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
  const Icon = LIABILITY_ICONS[liability.type] ?? LandmarkIcon;
  return (
    <div
      className="rounded-xl bg-white p-5 transition-all duration-200 hover:shadow-lg"
      style={{ border: `1px solid ${rgb.border}`, boxShadow: "rgba(0, 0, 0, 0.04) 0px 2px 8px" }}
    >
      <div className="mb-3 flex items-start justify-between">
        <div className="flex items-center gap-3">
          <div
            className="flex h-10 w-10 items-center justify-center rounded-lg"
            style={{ backgroundColor: hexToRgba("#e07a3b", 0.125) }}
          >
            <Icon className="h-5 w-5" style={{ color: "#e07a3b" }} />
          </div>
          <div>
            <h3 className="text-sm font-semibold" style={{ color: rgb.forestMedium }}>
              {LIABILITY_LABELS[liability.type]}
            </h3>
            <h4 className="font-semibold" style={{ color: rgb.forestDark }}>
              {liability.name}
            </h4>
          </div>
        </div>
        <DropdownMenu>
          <DropdownMenuTrigger
            className="inline-flex h-8 w-8 items-center justify-center rounded-md transition-colors hover:bg-accent"
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
      <p className="mb-2 text-2xl font-bold" style={{ color: "#e07a3b" }}>
        {formatMoney(liability.value)}
      </p>
      <div className="flex items-center justify-between text-xs" style={{ color: rgb.gray }}>
        <span>{liability.institution ?? ""}</span>
        <span>
          Updated {formatDate(liability.lastUpdated)}
          {liability.interestRate !== null && liability.interestRate !== undefined
            ? ` · ${liability.interestRate}%`
            : ""}
        </span>
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

export function NetWorthView() {
  const assets = useBudgetStore((s) => s.assets);
  const liabilities = useBudgetStore((s) => s.liabilities);
  const openAssetModal = useBudgetStore((s) => s.openAssetModal);
  const openLiabilityModal = useBudgetStore((s) => s.openLiabilityModal);
  const totals = computeNetWorth(assets, liabilities);
  const totalAssetsStr = formatMoney(totals.totalAssets);
  const totalLiabilitiesStr = formatMoney(totals.totalLiabilities);

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
          background: `linear-gradient(135deg, ${"#2d5a4a"} 0%, ${"#8fbc3f"} 100%)`,
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
          <div className="mb-8 flex items-center justify-between">
            <div>
              <p className="mb-2 text-sm text-white/80">Total Net Worth</p>
              <h2 className="text-4xl font-bold text-white md:text-5xl">
                {formatMoney(totals.netWorth)}
              </h2>
            </div>
            <div
              className="flex h-16 w-16 items-center justify-center rounded-full"
              style={{ backgroundColor: "rgba(255, 255, 255, 0.2)" }}
            >
              <TrendingUpIcon className="h-8 w-8 text-white" />
            </div>
          </div>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-3">
            <div className="rounded-xl p-4" style={{ backgroundColor: "rgba(255,255,255,0.1)" }}>
              <p className="mb-1 text-sm text-white/80">Total Assets</p>
              <p className="text-xl font-bold text-white">{totalAssetsStr}</p>
            </div>
            <div className="rounded-xl p-4" style={{ backgroundColor: "rgba(255,255,255,0.1)" }}>
              <p className="mb-1 text-sm text-white/80">Total Liabilities</p>
              <p className="text-xl font-bold text-white">{totalLiabilitiesStr}</p>
            </div>
            <div className="rounded-xl p-4" style={{ backgroundColor: "rgba(255,255,255,0.1)" }}>
              <p className="mb-1 text-sm text-white/80">Asset to Liability Ratio</p>
              <p className="text-xl font-bold text-white">
                {formatRatio(totals.ratio)} : 1
              </p>
            </div>
          </div>
        </div>
      </div>

      <Tabs defaultValue="assets">
        <TabsList className="mb-4">
          <TabsTrigger value="assets">Assets</TabsTrigger>
          <TabsTrigger value="liabilities">Liabilities</TabsTrigger>
        </TabsList>

        <TabsContent value="assets">
          <div className="mb-4 flex items-center justify-between">
            <div>
              <h2 className="text-xl font-bold" style={{ color: rgb.forestDark }}>
                Assets
              </h2>
              <p style={{ color: rgb.gray }}>
                {assets.length} {assets.length === 1 ? "item" : "items"} ·{" "}
                {formatMoneyShort(totals.totalAssets)}
              </p>
            </div>
            <button
              type="button"
              className="zb-btn-primary"
              onClick={() => openAssetModal({ mode: "create" })}
            >
              <PlusIcon className="h-4 w-4" />
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
                style={{ backgroundColor: hexToRgba("#8fbc3f", 0.125) }}
              >
                <TrendingUpIcon className="h-8 w-8" style={{ color: "#8fbc3f" }} />
              </div>
              <h3 className="mb-1 text-lg font-semibold" style={{ color: rgb.forestDark }}>
                No assets yet
              </h3>
              <p className="mb-6 text-sm" style={{ color: rgb.gray }}>
                Start by adding your first asset
              </p>
              <button
                type="button"
                className="zb-btn-primary"
                onClick={() => openAssetModal({ mode: "create" })}
              >
                <PlusIcon className="h-4 w-4" />
                Add Asset
              </button>
            </div>
          ) : (
            <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
              {assets.map((a) => (
                <AssetCard key={a.id} asset={a} />
              ))}
            </div>
          )}
        </TabsContent>

        <TabsContent value="liabilities">
          <div className="mb-4 flex items-center justify-between">
            <div>
              <h2 className="text-xl font-bold" style={{ color: rgb.forestDark }}>
                Liabilities
              </h2>
              <p style={{ color: rgb.gray }}>
                {liabilities.length} {liabilities.length === 1 ? "item" : "items"} ·{" "}
                {formatMoneyShort(totals.totalLiabilities)}
              </p>
            </div>
            <button
              type="button"
              className="zb-btn-primary"
              onClick={() => openLiabilityModal({ mode: "create" })}
            >
              <PlusIcon className="h-4 w-4" />
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
                style={{ backgroundColor: hexToRgba("#e07a3b", 0.125) }}
              >
                <CreditCardIcon className="h-8 w-8" style={{ color: "#e07a3b" }} />
              </div>
              <h3 className="mb-1 text-lg font-semibold" style={{ color: rgb.forestDark }}>
                No liabilities yet
              </h3>
              <p className="mb-6 text-sm" style={{ color: rgb.gray }}>
                Add any outstanding debts or loans
              </p>
              <button
                type="button"
                className="zb-btn-primary"
                onClick={() => openLiabilityModal({ mode: "create" })}
              >
                <PlusIcon className="h-4 w-4" />
                Add Liability
              </button>
            </div>
          ) : (
            <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
              {liabilities.map((l) => (
                <LiabilityCard key={l.id} liability={l} />
              ))}
            </div>
          )}
        </TabsContent>
      </Tabs>
    </div>
  );
}
