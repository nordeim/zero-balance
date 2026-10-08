"use client";

// Budget Dashboard — the NET ZERO GOAL hero card, the Net Zero Breakdown
// (a 3-level expandable drill-down: section → category → subcategory → item),
// the three stat cards, the Spending Breakdown donut, Budget Guidelines and
// the quick-action card buttons.
//
// Every visual decision below is pinned by the session-3 deep audit
// (docs/remediation-plan-v2.md) against the live reference DOM + JS bundle:
// plain toFixed(2) money (no commas), status-conditional hero chip/fill
// ("✓ NET ZERO" / orange under / blue over), the [Savings, Want, Need] donut
// order with per-classification legend icons, tinted bordered guideline
// cards, and per-surface 135deg add-button gradients.

import * as React from "react";
import { useRouter } from "next/navigation";
import {
  BarChart3Icon,
  ChevronDownIcon,
  ChevronRightIcon,
  CircleAlertIcon,
  HeartIcon,
  PiggyBankIcon,
  PlusIcon,
  ReceiptIcon,
  TargetIcon,
  TrendingDownIcon,
  TrendingUpIcon,
  WalletIcon,
} from "lucide-react";
import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip } from "recharts";
import { useBudgetStore } from "./store";
import { computeTotals, goalStatus, goalStatusLabel, spendingBreakdown } from "@/lib/dashboard";
import { formatMoney, formatSignedMoney, percentValue } from "@/lib/money";
import {
  ADD_BUTTON_GRADIENTS,
  COLORS,
  GUIDELINE_ROWS,
  TYPE_COLORS,
  rgb,
} from "@/lib/constants";
import { cn, hexToRgba } from "@/lib/utils";
import type { BudgetItem, Classification, ItemType } from "@/lib/types";

const CLASSIFICATION_COLORS: Record<Classification, string> = {
  need: COLORS.orangeDark,
  want: COLORS.blueMedium,
  savings: COLORS.limeGreen,
};

/** Donut legend icons (live reference DOM): piggy-bank / heart / circle-alert. */
const LEGEND_ICONS: Record<Classification, React.ComponentType<{ className?: string; style?: React.CSSProperties }>> = {
  savings: PiggyBankIcon,
  want: HeartIcon,
  need: CircleAlertIcon,
};

// ---------------------------------------------------------------------------
// NET ZERO GOAL hero
// ---------------------------------------------------------------------------

function NetZeroGoalCard() {
  const items = useBudgetStore((s) => s.items);
  const totals = computeTotals(items);
  const status = goalStatus(totals.balance);
  const pct = percentValue(totals.totalSavings + totals.totalExpenses, totals.totalIncome);

  // Allocation fill is status-conditional (reference bundle):
  // net-zero → lime→limeLight, under → orange, over → blueDark→blue.
  const fill =
    status === "net-zero"
      ? `linear-gradient(90deg, ${COLORS.limeGreen} 0%, ${COLORS.limeLight} 100%)`
      : status === "under-budget"
        ? `linear-gradient(90deg, ${COLORS.orangeDark} 0%, ${COLORS.orangeLight} 100%)`
        : `linear-gradient(90deg, ${COLORS.blueDark} 0%, ${COLORS.blueMedium} 100%)`;

  return (
    <div
      className="relative overflow-hidden rounded-2xl p-8"
      style={{
        background: `linear-gradient(135deg, ${COLORS.forestDark} 0%, ${COLORS.forestMedium} 100%)`,
        boxShadow: `${hexToRgba(COLORS.forestDark, 0.3)} 0px 20px 60px`,
      }}
    >
      <div
        aria-hidden="true"
        className="absolute top-0 right-0 h-64 w-64 rounded-[9999px] opacity-10"
        style={{
          background: `radial-gradient(circle, ${COLORS.limeGreen} 0%, transparent 70%)`,
          transform: "translate(30%, -30%)",
        }}
      />
      <div className="relative z-10">
        <div className="mb-6 flex items-center gap-3">
          <div
            className="flex h-12 w-12 items-center justify-center rounded-[9999px]"
            style={{ backgroundColor: hexToRgba(COLORS.limeGreen, 0.2) }}
          >
            <TargetIcon className="h-6 w-6" style={{ color: COLORS.limeGreen }} />
          </div>
          <div>
            <h3 className="text-lg font-bold text-white">NET ZERO GOAL</h3>
            <p className="text-sm" style={{ color: "rgba(255, 255, 255, 0.6)" }}>Income = Savings + Expenses</p>
          </div>
        </div>
        <div className="mb-6">
          <div className="mb-2 flex items-baseline justify-between">
            <span className="text-sm" style={{ color: "rgba(255, 255, 255, 0.8)" }}>Budget Allocation</span>
            <span className="text-lg font-semibold text-white">
              {totals.allocationPercent.toFixed(1)}%
            </span>
          </div>
          <div className="h-3 overflow-hidden rounded-[9999px]" style={{ backgroundColor: "rgba(255,255,255,0.1)" }}>
            <div
              className="h-full rounded-[9999px] transition-all duration-500"
              style={{ background: fill, width: `${pct}%` }}
            />
          </div>
        </div>
        <div
          className="flex items-center justify-between rounded-xl p-6"
          style={{ backgroundColor: "rgba(255,255,255,0.05)", backdropFilter: "blur(10px)" }}
        >
          <div>
            <p className="mb-1 text-sm" style={{ color: "rgba(255, 255, 255, 0.6)" }}>Balance</p>
            {/* Reference: "$" + Math.abs(balance).toFixed(2) — the sign is
                carried by the status chip, never the amount. */}
            <p className="text-3xl font-bold text-white">{formatMoney(Math.abs(totals.balance))}</p>
          </div>
          {status === "net-zero" ? (
            <div
              className="rounded-lg px-4 py-2 text-sm font-semibold"
              style={{ backgroundColor: COLORS.limeGreen, color: "white" }}
            >
              ✓ NET ZERO
            </div>
          ) : status === "under-budget" ? (
            <span className="flex items-center gap-2">
              <TrendingUpIcon className="h-5 w-5" style={{ color: COLORS.orangeLight }} />
              <span className="font-semibold" style={{ color: COLORS.orangeLight }}>
                {goalStatusLabel(status)}
              </span>
            </span>
          ) : (
            <span className="flex items-center gap-2">
              <TrendingDownIcon className="h-5 w-5" style={{ color: COLORS.blueMedium }} />
              <span className="font-semibold" style={{ color: COLORS.blueMedium }}>
                {goalStatusLabel(status)}
              </span>
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Net Zero Breakdown — 3-level expandable drill-down
// ---------------------------------------------------------------------------

interface SubcategoryNode {
  name: string;
  amount: number;
  items: BudgetItem[];
}

interface CategoryNode {
  name: string;
  amount: number;
  subcategories: SubcategoryNode[];
}

/**
 * The reference's grouping (bundle): items fold into
 * category → subcategory (literal "Other" when unset), both levels sorted by
 * amount desc. The item label is `notes` truncated to 30 chars (with "...")
 * or the literal "Item".
 */
function buildCategoryTree(items: BudgetItem[]): CategoryNode[] {
  const cats = new Map<string, { total: number; subs: Map<string, { total: number; items: BudgetItem[] }> }>();
  for (const item of items) {
    let cat = cats.get(item.category);
    if (!cat) {
      cat = { total: 0, subs: new Map() };
      cats.set(item.category, cat);
    }
    cat.total += item.amount;
    const key = item.subcategory?.trim() ? item.subcategory : "Other";
    let sub = cat.subs.get(key);
    if (!sub) {
      sub = { total: 0, items: [] };
      cat.subs.set(key, sub);
    }
    sub.total += item.amount;
    sub.items.push(item);
  }
  return [...cats.entries()]
    .map(([name, { total, subs }]) => ({
      name,
      amount: total,
      subcategories: [...subs.entries()]
        .map(([subName, { total: subTotal, items }]) => ({ name: subName, amount: subTotal, items }))
        .sort((a, b) => b.amount - a.amount),
    }))
    .sort((a, b) => b.amount - a.amount);
}

/** Item-row label: notes truncated to 30 chars, else the literal "Item". */
function itemLabel(item: BudgetItem): string {
  const notes = item.notes?.trim();
  if (!notes) return "Item";
  return notes.length > 30 ? `${notes.slice(0, 30)}...` : notes;
}

const OTHER_SUBCATEGORY = "Other";

function BreakdownSection({
  label,
  icon: Icon,
  color,
  items,
  expanded,
  onToggle,
  expandedCategories,
  onToggleCategory,
}: {
  label: string;
  icon: React.ComponentType<{ className?: string; style?: React.CSSProperties }>;
  color: string;
  items: BudgetItem[];
  expanded: boolean;
  onToggle: () => void;
  expandedCategories: Record<string, boolean>;
  onToggleCategory: (name: string) => void;
}) {
  const total = items.reduce((acc, i) => acc + i.amount, 0);
  const categories = React.useMemo(() => buildCategoryTree(items), [items]);
  const prefix = label === "Total Income" ? "" : "- ";
  return (
    <div>
      <button
        type="button"
        aria-expanded={expanded}
        onClick={onToggle}
        className="flex w-full -mx-2 cursor-pointer items-center justify-between rounded-lg p-2 transition-colors hover:bg-gray-50"
      >
        <span className="flex items-center gap-2">
          <span
            className="flex h-8 w-8 items-center justify-center rounded-lg"
            style={{ backgroundColor: hexToRgba(color, 0.125) }}
          >
            <Icon className="h-4 w-4" style={{ color }} />
          </span>
          <span className="text-sm font-medium" style={{ color: rgb.gray }}>
            {label}
          </span>
          <span className="ml-1">
            <ChevronDownIcon
              className={cn("h-3.5 w-3.5 transition-transform", expanded && "rotate-180")}
              style={{ color: "rgb(156, 163, 175)" }}
              aria-hidden="true"
            />
          </span>
        </span>
        <span className="font-semibold" style={{ color }}>
          {prefix}
          {formatMoney(total)}
        </span>
      </button>
      {expanded && (
        <div className="overflow-hidden">
          <div className="ml-10 mt-2 space-y-2 pb-2">
            {categories.map((cat) => {
              const catOpen = !!expandedCategories[cat.name];
              return (
                <div key={cat.name}>
                  <button
                    type="button"
                    aria-expanded={catOpen}
                    onClick={() => onToggleCategory(cat.name)}
                    className="flex w-full cursor-pointer items-center justify-between rounded-lg px-3 py-1.5 transition-colors hover:bg-gray-100"
                    style={{ backgroundColor: "rgb(249, 250, 251)" }}
                  >
                    <span className="flex items-center gap-2">
                      <span className="h-1.5 w-1.5 rounded-[9999px]" style={{ backgroundColor: color }} />
                      <span className="text-xs font-medium" style={{ color: rgb.forestDark }}>
                        {cat.name}
                      </span>
                      <span className="ml-1">
                        <ChevronDownIcon
                          className={cn("h-3 w-3 transition-transform", catOpen && "rotate-180")}
                          style={{ color: "rgb(156, 163, 175)" }}
                          aria-hidden="true"
                        />
                      </span>
                    </span>
                    <span className="text-xs font-medium" style={{ color: rgb.forestDark }}>
                      {formatMoney(cat.amount)}
                    </span>
                  </button>
                  {catOpen && (
                    <div className="overflow-hidden">
                      <div className="mt-1 ml-4 space-y-1">
                        {cat.subcategories.map((sub) => (
                          <div key={sub.name}>
                            <div
                              className="flex items-center justify-between rounded px-2 py-1"
                              style={{ backgroundColor: "rgb(250, 250, 250)" }}
                            >
                              <span className="flex items-center gap-2">
                                <span
                                  className="h-1 w-1 rounded-[9999px]"
                                  style={{ backgroundColor: color, opacity: 0.6 }}
                                />
                                <span className="text-xs" style={{ color: rgb.gray }}>
                                  {sub.name}
                                </span>
                              </span>
                              <span className="text-xs font-medium" style={{ color: rgb.gray }}>
                                {formatMoney(sub.amount)}
                              </span>
                            </div>
                            <div className="mt-0.5 ml-4 space-y-0.5">
                              {sub.items.map((item) => (
                                <div
                                  key={item.id}
                                  className="flex items-center justify-between px-2 py-1 text-xs"
                                  style={{ color: "rgb(156, 163, 175)" }}
                                >
                                  <span className="flex items-center gap-1.5">
                                    <span
                                      className="h-0.5 w-0.5 rounded-[9999px]"
                                      style={{ backgroundColor: color, opacity: 0.4 }}
                                    />
                                    <span className="max-w-[120px] truncate">{itemLabel(item)}</span>
                                  </span>
                                  <span className="font-medium">{formatMoney(item.amount)}</span>
                                </div>
                              ))}
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              );
            })}
            <div
              className="flex items-center justify-between border-t px-3 py-1.5"
              style={{ borderColor: rgb.border }}
            >
              <span className="text-xs font-semibold" style={{ color: rgb.gray }}>
                {categories.length} {categories.length === 1 ? "category" : "categories"}
              </span>
              <span className="text-xs font-bold" style={{ color }}>
                {formatMoney(total)}
              </span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

const Divider = () => (
  <div className="my-3 border-t" style={{ borderColor: rgb.border }} aria-hidden="true" />
);

function NetZeroBreakdownCard() {
  const items = useBudgetStore((s) => s.items);
  const totals = computeTotals(items);
  const [openSection, setOpenSection] = React.useState<ItemType | null>(null);
  const [openCategories, setOpenCategories] = React.useState<Record<string, boolean>>({});

  const toggleSection = (type: ItemType | null) => {
    setOpenSection(type);
    setOpenCategories({});
  };
  const toggleCategory = (name: string) =>
    setOpenCategories((prev) => ({ ...prev, [name]: !prev[name] }));

  const sections: { type: ItemType; label: string; icon: React.ComponentType<{ className?: string; style?: React.CSSProperties }>; color: string; prefix: string }[] = [
    { type: "income", label: "Total Income", icon: TrendingUpIcon, color: COLORS.limeGreen, prefix: "" },
    { type: "savings", label: "Total Savings", icon: PiggyBankIcon, color: COLORS.blueMedium, prefix: "- " },
    { type: "expense", label: "Total Expenses", icon: ReceiptIcon, color: COLORS.orangeDark, prefix: "- " },
  ];

  // Net Balance colors are sign-conditional (reference live DOM):
  // zero → lime, positive → orangeLight, negative → blueMedium.
  const netColor =
    totals.netBalance === 0
      ? COLORS.limeGreen
      : totals.netBalance > 0
        ? COLORS.orangeLight
        : COLORS.blueMedium;
  const NetIcon = totals.netBalance < 0 ? TrendingDownIcon : TrendingUpIcon;

  return (
    <div className="rounded-2xl p-6" style={{ backgroundColor: "white", border: `1px solid ${rgb.border}` }}>
      <h3 className="mb-4 text-sm font-medium" style={{ color: rgb.gray }}>
        Net Zero Breakdown
      </h3>
      <div className="space-y-3">
        {sections.map(({ type, label, icon, color }, i) => (
          <React.Fragment key={type}>
            {i > 0 && <Divider />}
            <BreakdownSection
              label={label}
              icon={icon}
              color={color}
              items={items.filter((it) => it.type === type)}
              expanded={openSection === type}
              onToggle={() => toggleSection(openSection === type ? null : type)}
              expandedCategories={openCategories}
              onToggleCategory={toggleCategory}
            />
          </React.Fragment>
        ))}
        <div className="mt-3 border-t pt-3" style={{ borderColor: rgb.border }}>
          <div className="flex items-center justify-between">
            <span className="flex items-center gap-2">
              <span
                className="flex h-8 w-8 items-center justify-center rounded-lg"
                style={{ backgroundColor: hexToRgba(netColor, 0.125) }}
              >
                <NetIcon className="h-4 w-4" style={{ color: netColor }} />
              </span>
              <span className="text-sm font-semibold" style={{ color: rgb.gray }}>
                Net Balance
              </span>
            </span>
            <span className="text-lg font-bold" style={{ color: netColor }}>
              {formatSignedMoney(totals.netBalance)}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Stat cards
// ---------------------------------------------------------------------------

function StatCard({
  title,
  amount,
  count,
  icon: Icon,
  color,
  href,
}: {
  title: string;
  amount: string;
  count: number;
  icon: React.ComponentType<{ className?: string; style?: React.CSSProperties }>;
  color: string;
  href: string;
}) {
  const router = useRouter();
  const IconComp = Icon;
  return (
    <div
      role="button"
      tabIndex={0}
      onClick={() => router.push(href)}
      onKeyDown={(e) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          router.push(href);
        }
      }}
      className="group relative cursor-pointer overflow-hidden rounded-2xl border p-6 transition-all duration-200 hover:shadow-lg"
      style={{
        backgroundColor: "white",
        boxShadow: "rgba(0, 0, 0, 0.06) 0px 4px 20px",
        borderColor: rgb.border,
      }}
    >
      <div
        aria-hidden="true"
        className="absolute top-0 right-0 h-32 w-32 rounded-[9999px] opacity-0 transition-opacity duration-300 group-hover:opacity-10"
        style={{
          background: `radial-gradient(circle, ${color} 0%, transparent 70%)`,
          transform: "translate(30%, -30%)",
        }}
      />
      <div className="relative z-10">
        <div className="mb-4 flex items-start justify-between">
          <div
            className="flex h-12 w-12 items-center justify-center rounded-xl"
            style={{ backgroundColor: hexToRgba(color, 0.125) }}
          >
            <IconComp className="h-6 w-6" style={{ color }} />
          </div>
          <ChevronRightIcon
            className="h-5 w-5 opacity-0 transition-opacity duration-200 group-hover:opacity-100"
            style={{ color: rgb.gray }}
            aria-hidden="true"
          />
        </div>
        <h3 className="mb-1 text-sm font-medium" style={{ color: rgb.gray }}>
          {title}
        </h3>
        {/* Reference: text-3xl forestDark (not type-colored text-2xl). */}
        <p className="mb-4 text-3xl font-bold" style={{ color: rgb.forestDark }}>
          {amount}
        </p>
        <div className="flex items-center gap-2 text-sm">
          <span style={{ color: rgb.gray }}>
            {count} {count === 1 ? "item" : "items"}
          </span>
          <div className="h-px flex-1" style={{ backgroundColor: rgb.border }} aria-hidden="true" />
          <TrendingUpIcon className="h-4 w-4" style={{ color }} aria-hidden="true" />
        </div>
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Spending Breakdown donut (shadcn card shell, value-DESC slice order)
// ---------------------------------------------------------------------------

function SpendingBreakdownCard() {
  const items = useBudgetStore((s) => s.items);
  // The reference renders its donut data sorted by value DESCENDING — its
  // pie sectors AND legend rows share the sorted array (measured live:
  // [Need $6025, Savings $300, Want $200], biggest slice anchored at
  // recharts' 3-o'clock start). The aggregation's [S, W, N] order stays the
  // domain model; the presentation sorts (docs/remediation-plan-v9.md G1).
  const slices = [...spendingBreakdown(items)].sort((a, b) => b.amount - a.amount);
  const hasData = items.length > 0;
  const data = slices.map((s) => ({ name: s.label, value: s.amount, color: CLASSIFICATION_COLORS[s.key] }));

  return (
    <div
      className="rounded-xl border bg-card text-card-foreground shadow"
      style={{ border: `1px solid ${rgb.border}` }}
    >
      <div className="flex flex-col space-y-1.5 p-6">
        <div className="font-semibold leading-none tracking-tight" style={{ color: rgb.forestDark }}>
          Spending Breakdown
        </div>
        <p className="text-sm" style={{ color: rgb.gray }}>
          Needs vs Wants vs Savings
        </p>
      </div>
      <div className="p-6 pt-0">
        {hasData ? (
          <>
            <div style={{ width: "100%", height: 300 }}>
              <ResponsiveContainer>
                <PieChart>
                  <Pie
                    data={data}
                    dataKey="value"
                    nameKey="name"
                    cx="50%"
                    cy="50%"
                    outerRadius={100}
                    stroke="#fff"
                    isAnimationActive={false}
                    // The reference renders its percentage labels with NO
                    // connector lines (measured: labelLineCount 0) — recharts
                    // draws one .recharts-pie-label-line per labeled sector
                    // unless labelLine is explicitly false (plan v9 G1b).
                    labelLine={false}
                    label={({ percent }: { percent?: number }) =>
                      `${((percent ?? 0) * 100).toFixed(1)}%`
                    }
                  >
                    {data.map((entry) => (
                      <Cell key={entry.name} fill={entry.color} />
                    ))}
                  </Pie>
                  {/* v14 G1 (measured live on the reference): hovering a
                      sector renders the recharts DEFAULT tooltip with the
                      item row "Need : $6025.00" — the value carries the
                      dollar sign and two decimals (the dashboard's plain
                      money format, no thousands separators). The reference
                      also overrides the default tooltip chrome: border
                      #e5e7e3 (its CARD border token), radius 8, and the
                      soft rgba(0,0,0,0.1) 0 4px 12px shadow — recharts 3's
                      bare default (#cccccc border, square corners, no
                      shadow) drifts, so pin all three via contentStyle. */}
                  <Tooltip
                    formatter={(value) => `$${Number(value).toFixed(2)}`}
                    contentStyle={{
                      borderRadius: 8,
                      borderColor: "#e5e7e3",
                      boxShadow: "rgba(0, 0, 0, 0.1) 0px 4px 12px",
                    }}
                    // recharts 2 (the reference) renders the item row in
                    // black; recharts 3 defaults it to the sector's fill
                    // color (the "Need : $…" row renders ORANGE) — pin the
                    // reference's black item text.
                    itemStyle={{ color: "#000000" }}
                  />
                </PieChart>
              </ResponsiveContainer>
            </div>
            <div className="mt-6 flex flex-col gap-3">
              {slices.map((slice) => {
                const LegendIcon = LEGEND_ICONS[slice.key];
                return (
                  <div
                    key={slice.key}
                    className="flex items-center justify-between rounded-lg p-3"
                    style={{ backgroundColor: "rgb(245, 248, 245)" }}
                  >
                    <div className="flex items-center gap-3">
                      <div
                        className="h-4 w-4 rounded"
                        style={{ backgroundColor: CLASSIFICATION_COLORS[slice.key] }}
                        aria-hidden="true"
                      />
                      <LegendIcon
                        className="h-4 w-4"
                        style={{ color: CLASSIFICATION_COLORS[slice.key] }}
                        aria-hidden="true"
                      />
                      <span className="font-medium" style={{ color: rgb.forestDark }}>
                        {slice.label}
                      </span>
                    </div>
                    <div className="text-right">
                      <p className="font-bold" style={{ color: CLASSIFICATION_COLORS[slice.key] }}>
                        {formatMoney(slice.amount)}
                      </p>
                      <p className="text-xs" style={{ color: rgb.gray }}>
                        {slice.percent.toFixed(1)}%
                      </p>
                    </div>
                  </div>
                );
              })}
            </div>
          </>
        ) : (
          <div className="flex flex-col items-center justify-center py-12 text-center">
            <BarChart3Icon className="mb-3 h-10 w-10" style={{ color: "rgb(203, 213, 225)" }} />
            <p className="font-medium" style={{ color: "rgb(156, 163, 175)" }}>
              No data to display
            </p>
            <p className="text-sm" style={{ color: "rgb(156, 163, 175)" }}>
              Add budget items to see the breakdown
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Budget Guidelines — tinted, bordered cards
// ---------------------------------------------------------------------------

function BudgetGuidelinesCard() {
  return (
    <div
      className="rounded-xl border bg-card text-card-foreground shadow"
      style={{ border: `1px solid ${rgb.border}` }}
    >
      <div className="flex flex-col space-y-1.5 p-6">
        <div className="font-semibold leading-none tracking-tight" style={{ color: rgb.forestDark }}>
          Budget Guidelines
        </div>
      </div>
      <div className="space-y-3 p-6 pt-0">
        {GUIDELINE_ROWS.map((g) => (
          <div
            key={g.label}
            className="rounded-lg p-4"
            style={{ backgroundColor: g.bgColor, border: `1px solid ${g.borderColor}` }}
          >
            <div className="mb-1 flex items-center justify-between">
              <span className="font-medium" style={{ color: g.color }}>
                {g.label}
              </span>
              <span className="text-sm" style={{ color: g.color }}>
                {g.percent}
              </span>
            </div>
            <p className="text-xs" style={{ color: rgb.gray }}>
              {g.description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Quick actions — card buttons (wallet / piggy-bank / receipt)
// ---------------------------------------------------------------------------

function QuickActionCard({
  label,
  icon: Icon,
  color,
  onClick,
}: {
  label: string;
  icon: React.ComponentType<{ className?: string; style?: React.CSSProperties }>;
  color: string;
  onClick: () => void;
}) {
  const IconComp = Icon;
  return (
    <button
      type="button"
      onClick={onClick}
      className="group rounded-2xl border p-6 text-left transition-all duration-200 hover:shadow-lg"
      style={{ backgroundColor: "white", borderColor: rgb.border }}
    >
      <span className="flex items-center gap-3">
        <span
          className="flex h-10 w-10 items-center justify-center rounded-xl transition-transform duration-200 group-hover:scale-110"
          style={{ backgroundColor: hexToRgba(color, 0.125) }}
        >
          <IconComp className="h-5 w-5" style={{ color }} />
        </span>
        <span className="font-medium" style={{ color: rgb.forestDark }}>
          {label}
        </span>
        <PlusIcon
          className="ml-auto h-4 w-4 opacity-50 transition-opacity group-hover:opacity-100"
          style={{ color }}
          aria-hidden="true"
        />
      </span>
    </button>
  );
}

// ---------------------------------------------------------------------------
// View
// ---------------------------------------------------------------------------

export function DashboardView() {
  const items = useBudgetStore((s) => s.items);
  const openItemModal = useBudgetStore((s) => s.openItemModal);
  const totals = computeTotals(items);
  const counts = {
    income: items.filter((i) => i.type === "income").length,
    savings: items.filter((i) => i.type === "savings").length,
    expense: items.filter((i) => i.type === "expense").length,
  };

  // G13: padding OUTSIDE the max-w-7xl cap (reference structure) — see
  // net-worth-view.tsx.
  return (
    <div className="min-h-screen p-4 md:p-8">
    <div className="mx-auto w-full max-w-7xl">
      <div className="mb-8 flex flex-col justify-between items-start gap-4 md:flex-row md:items-center">
        <div>
          <h1 className="mb-2 text-3xl font-bold md:text-4xl" style={{ color: rgb.forestDark }}>
            Budget Dashboard
          </h1>
          <p style={{ color: rgb.gray }}>
            Track your income, savings, and expenses to achieve net zero
          </p>
        </div>
        <button
          type="button"
          className="zb-btn-add shrink-0"
          style={{ background: ADD_BUTTON_GRADIENTS.dashboard }}
          onClick={() => openItemModal({ mode: "create", type: "expense" })}
        >
          <PlusIcon className="mr-2 h-4 w-4" />
          Add Item
        </button>
      </div>

      <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2">
          <NetZeroGoalCard />
        </div>
        <NetZeroBreakdownCard />
      </div>

      <div className="mt-8 grid grid-cols-1 gap-6 md:grid-cols-3">
        <StatCard
          title="Total Income"
          amount={formatMoney(totals.totalIncome)}
          count={counts.income}
          icon={WalletIcon}
          color={TYPE_COLORS.income}
          href="/income"
        />
        <StatCard
          title="Total Savings"
          amount={formatMoney(totals.totalSavings)}
          count={counts.savings}
          icon={PiggyBankIcon}
          color={TYPE_COLORS.savings}
          href="/savings"
        />
        <StatCard
          title="Total Expenses"
          amount={formatMoney(totals.totalExpenses)}
          count={counts.expense}
          icon={ReceiptIcon}
          color={TYPE_COLORS.expense}
          href="/expenses"
        />
      </div>

      <div className="mt-8 grid grid-cols-1 gap-6 lg:grid-cols-2">
        <SpendingBreakdownCard />
        <BudgetGuidelinesCard />
      </div>

      <div className="mt-8 grid grid-cols-1 gap-6 md:grid-cols-3">
        <QuickActionCard
          label="Add Income"
          icon={WalletIcon}
          color={TYPE_COLORS.income}
          onClick={() => openItemModal({ mode: "create", type: "income" })}
        />
        <QuickActionCard
          label="Add Savings"
          icon={PiggyBankIcon}
          color={TYPE_COLORS.savings}
          onClick={() => openItemModal({ mode: "create", type: "savings" })}
        />
        <QuickActionCard
          label="Add Expense"
          icon={ReceiptIcon}
          color={TYPE_COLORS.expense}
          onClick={() => openItemModal({ mode: "create", type: "expense" })}
        />
      </div>
    </div>
    </div>
  );
}
