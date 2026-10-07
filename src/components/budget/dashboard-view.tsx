"use client";

// Budget Dashboard — the NET ZERO GOAL hero card, the Net Zero Breakdown,
// the three stat cards, the Spending Breakdown donut, Budget Guidelines and
// the quick-action buttons. Layout and inline colors mirror the reference
// (Tailwind for structure, inline styles for the palette — engine-independent).

import * as React from "react";
import { useRouter } from "next/navigation";
import {
  ArrowRightIcon,
  BarChart3Icon,
  CheckCircle2Icon,
  ChevronDownIcon,
  PiggyBankIcon,
  PlusIcon,
  ReceiptTextIcon,
  TargetIcon,
  TrendingDownIcon,
  TrendingUpIcon,
  WalletIcon,
} from "lucide-react";
import { Cell, Pie, PieChart, ResponsiveContainer, Tooltip } from "recharts";
import { useBudgetStore } from "./store";
import { computeTotals, goalStatus, goalStatusLabel, spendingBreakdown } from "@/lib/dashboard";
import { formatMoney, formatPercent, formatSignedMoney, percentValue } from "@/lib/money";
import { COLORS, rgb } from "@/lib/constants";
import { cn, hexToRgba } from "@/lib/utils";
import type { Classification } from "@/lib/types";

const CLASSIFICATION_COLORS: Record<Classification, string> = {
  need: COLORS.orangeDark,
  want: COLORS.blueMedium,
  savings: COLORS.limeGreen,
};

function NetZeroGoalCard() {
  const items = useBudgetStore((s) => s.items);
  const totals = computeTotals(items);
  const status = goalStatus(totals.balance);
  const pct = percentValue(totals.totalSavings + totals.totalExpenses, totals.totalIncome);

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
        className="absolute top-0 right-0 h-64 w-64 rounded-full opacity-10"
        style={{
          background: `radial-gradient(circle, ${COLORS.limeGreen} 0%, transparent 70%)`,
          transform: "translate(30%, -30%)",
        }}
      />
      <div className="relative z-10">
        <div className="mb-6 flex items-center gap-3">
          <div
            className="flex h-12 w-12 items-center justify-center rounded-full"
            style={{ backgroundColor: hexToRgba(COLORS.limeGreen, 0.2) }}
          >
            <TargetIcon className="h-6 w-6" style={{ color: COLORS.limeGreen }} />
          </div>
          <div>
            <h3 className="text-lg font-bold text-white">NET ZERO GOAL</h3>
            <p className="text-sm text-white/60">Income = Savings + Expenses</p>
          </div>
        </div>
        <div className="mb-6">
          <div className="mb-2 flex items-baseline justify-between">
            <span className="text-sm text-white/80">Budget Allocation</span>
            <span className="text-lg font-semibold text-white">
              {totals.allocationPercent.toFixed(1)}%
            </span>
          </div>
          <div className="h-3 overflow-hidden rounded-full" style={{ backgroundColor: "rgba(255,255,255,0.1)" }}>
            <div
              className="h-full rounded-full transition-all duration-500"
              style={{
                background: `linear-gradient(90deg, ${COLORS.orangeDark} 0%, ${COLORS.orangeLight} 100%)`,
                width: `${pct}%`,
              }}
            />
          </div>
        </div>
        <div
          className="flex items-center justify-between rounded-xl p-6"
          style={{ backgroundColor: "rgba(255,255,255,0.05)", backdropFilter: "blur(10px)" }}
        >
          <div>
            <p className="mb-1 text-sm text-white/60">Balance</p>
            <p className="text-3xl font-bold text-white">{formatMoney(totals.balance)}</p>
          </div>
          {status === "net-zero" ? (
            <span
              className="inline-flex items-center gap-1.5 rounded-md px-2.5 py-1 text-xs font-semibold text-white"
              style={{ backgroundColor: COLORS.limeGreen }}
            >
              <CheckCircle2Icon className="h-3.5 w-3.5" />
              NET ZERO
            </span>
          ) : status === "under-budget" ? (
            <span className="flex items-center gap-2">
              <TrendingUpIcon className="h-5 w-5" style={{ color: COLORS.orangeLight }} />
              <span className="font-semibold" style={{ color: COLORS.orangeLight }}>
                {goalStatusLabel(status)}
              </span>
            </span>
          ) : (
            <span className="flex items-center gap-2">
              <TrendingDownIcon className="h-5 w-5" style={{ color: COLORS.orangeLight }} />
              <span className="font-semibold" style={{ color: COLORS.orangeLight }}>
                {goalStatusLabel(status)}
              </span>
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

function BreakdownRow({
  label,
  icon: Icon,
  color,
  value,
  href,
  disabled,
}: {
  label: string;
  icon: React.ComponentType<{ className?: string; style?: React.CSSProperties }>;
  color: string;
  value: string;
  href: string;
  disabled: boolean;
}) {
  const router = useRouter();
  const IconComp = Icon;
  return (
    <div>
      <button
        type="button"
        disabled={disabled}
        onClick={() => router.push(href)}
        className={cn(
          "flex w-full items-center justify-between rounded-lg p-2 transition-colors -mx-2",
          disabled ? "cursor-default opacity-60" : "cursor-pointer hover:bg-gray-50",
        )}
      >
        <span className="flex items-center gap-2">
          <span
            className="flex h-8 w-8 items-center justify-center rounded-lg"
            style={{ backgroundColor: hexToRgba(color, 0.125) }}
          >
            <IconComp className="h-4 w-4" style={{ color }} />
          </span>
          <span className="text-sm font-medium" style={{ color: rgb.gray }}>
            {label}
          </span>
          <ChevronDownIcon
            className="h-3.5 w-3.5"
            style={{ color: "rgb(156, 163, 175)" }}
            aria-hidden="true"
          />
        </span>
        <span className="font-semibold" style={{ color }}>
          {value}
        </span>
      </button>
    </div>
  );
}

const Divider = () => (
  <div className="my-3 border-t" style={{ borderColor: rgb.border }} aria-hidden="true" />
);

function NetZeroBreakdownCard() {
  const items = useBudgetStore((s) => s.items);
  const totals = computeTotals(items);
  return (
    <div
      className="rounded-2xl p-6"
      style={{ backgroundColor: "white", border: `1px solid ${rgb.border}` }}
    >
      <h3 className="mb-4 text-sm font-medium" style={{ color: rgb.gray }}>
        Net Zero Breakdown
      </h3>
      <div className="space-y-3">
        <BreakdownRow
          label="Total Income"
          icon={TrendingUpIcon}
          color={COLORS.limeGreen}
          value={formatMoney(totals.totalIncome)}
          href="/income"
          disabled={totals.totalIncome === 0}
        />
        <Divider />
        <BreakdownRow
          label="Total Savings"
          icon={PiggyBankIcon}
          color={COLORS.blueMedium}
          value={`- ${formatMoney(totals.totalSavings)}`}
          href="/savings"
          disabled={totals.totalSavings === 0}
        />
        <Divider />
        <BreakdownRow
          label="Total Expenses"
          icon={ReceiptTextIcon}
          color={COLORS.orangeDark}
          value={`- ${formatMoney(totals.totalExpenses)}`}
          href="/expenses"
          disabled={totals.totalExpenses === 0}
        />
        <Divider />
        <div className="flex items-center justify-between">
          <span className="flex items-center gap-2">
            <span
              className="flex h-8 w-8 items-center justify-center rounded-lg"
              style={{ backgroundColor: hexToRgba(COLORS.limeGreen, 0.125) }}
            >
              <TrendingUpIcon className="h-4 w-4" style={{ color: COLORS.limeGreen }} />
            </span>
            <span className="text-sm font-medium" style={{ color: rgb.gray }}>
              Net Balance
            </span>
          </span>
          <span className="font-semibold" style={{ color: COLORS.limeGreen }}>
            {formatSignedMoney(totals.netBalance)}
          </span>
        </div>
      </div>
    </div>
  );
}

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
        className="absolute top-0 right-0 h-32 w-32 rounded-full opacity-0 transition-opacity duration-300 group-hover:opacity-10"
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
          <ChevronDownIcon
            className="h-5 w-5 -rotate-90 opacity-0 transition-opacity duration-200 group-hover:opacity-100"
            style={{ color: rgb.gray }}
            aria-hidden="true"
          />
        </div>
        <h3 className="mb-1 text-sm font-medium" style={{ color: rgb.gray }}>
          {title}
        </h3>
        <p className="text-2xl font-bold" style={{ color }}>
          {amount}
        </p>
        <div className="mt-2 flex items-center justify-between">
          <p className="text-xs" style={{ color: rgb.gray }}>
            {count} {count === 1 ? "item" : "items"}
          </p>
          <TrendingUpIcon className="h-3.5 w-3.5" style={{ color }} aria-hidden="true" />
        </div>
      </div>
    </div>
  );
}

function SpendingBreakdownCard() {
  const items = useBudgetStore((s) => s.items);
  const slices = spendingBreakdown(items);
  const hasData = items.length > 0;
  const data = slices.map((s) => ({ name: s.label, value: s.amount, color: CLASSIFICATION_COLORS[s.key] }));

  return (
    <div
      className="rounded-2xl p-6"
      style={{ backgroundColor: "white", border: `1px solid ${rgb.border}` }}
    >
      <h3 className="mb-1 text-base font-semibold" style={{ color: rgb.forestDark }}>
        Spending Breakdown
      </h3>
      <p className="mb-4 text-sm" style={{ color: rgb.gray }}>
        Needs vs Wants vs Savings
      </p>
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
                  label={({ percent }: { percent?: number }) =>
                    `${((percent ?? 0) * 100).toFixed(1)}%`
                  }
                >
                  {data.map((entry) => (
                    <Cell key={entry.name} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
          <div className="mt-6 flex flex-col gap-3">
            {slices.map((slice) => (
              <div
                key={slice.key}
                className="flex items-center justify-between rounded-lg p-3"
                style={{ backgroundColor: rgb.cardTint }}
              >
                <div className="flex items-center gap-3">
                  <div
                    className="h-4 w-4 rounded"
                    style={{ backgroundColor: CLASSIFICATION_COLORS[slice.key] }}
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
            ))}
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
  );
}

const GUIDELINES = [
  {
    label: "Needs",
    percent: "~50%",
    description: "Essential expenses like rent, utilities, groceries",
    chip: "bg-red-50",
    title: "text-red-700",
  },
  {
    label: "Wants",
    percent: "~30%",
    description: "Discretionary spending like entertainment, dining out",
    chip: "bg-blue-50",
    title: "text-blue-700",
  },
  {
    label: "Savings",
    percent: "~20%",
    description: "Emergency fund, retirement, investments",
    chip: "bg-green-50",
    title: "text-green-700",
  },
] as const;

function BudgetGuidelinesCard() {
  return (
    <div
      className="rounded-2xl p-6"
      style={{ backgroundColor: "white", border: `1px solid ${rgb.border}` }}
    >
      <h3 className="mb-4 text-base font-semibold" style={{ color: rgb.forestDark }}>
        Budget Guidelines
      </h3>
      <div className="space-y-3">
        {GUIDELINES.map((g) => (
          <div key={g.label} className={cn("rounded-lg p-4", g.chip)}>
            <div className="flex items-center justify-between">
              <span className={cn("font-semibold", g.title)}>{g.label}</span>
              <span className={cn("font-semibold", g.title)}>{g.percent}</span>
            </div>
            <p className="mt-1 text-sm" style={{ color: rgb.gray }}>
              {g.description}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export function DashboardView() {
  const items = useBudgetStore((s) => s.items);
  const openItemModal = useBudgetStore((s) => s.openItemModal);
  const totals = computeTotals(items);
  const counts = {
    income: items.filter((i) => i.type === "income").length,
    savings: items.filter((i) => i.type === "savings").length,
    expense: items.filter((i) => i.type === "expense").length,
  };

  return (
    <div className="mx-auto w-full max-w-7xl p-4 md:p-8">
      <div className="mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <div>
          <h1 className="text-3xl font-bold" style={{ color: rgb.forestDark }}>
            Budget Dashboard
          </h1>
          <p className="mt-1" style={{ color: rgb.gray }}>
            Track your income, savings, and expenses to achieve net zero
          </p>
        </div>
        <button
          type="button"
          className="zb-btn-primary shrink-0"
          onClick={() => openItemModal({ mode: "create", type: "expense" })}
        >
          <PlusIcon className="h-4 w-4" />
          Add Item
        </button>
      </div>

      <div className="space-y-6">
        <div className="grid grid-cols-1 gap-6 lg:grid-cols-3">
          <div className="lg:col-span-2">
            <NetZeroGoalCard />
          </div>
          <NetZeroBreakdownCard />
        </div>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
          <StatCard
            title="Total Income"
            amount={formatMoney(totals.totalIncome)}
            count={counts.income}
            icon={WalletIcon}
            color={COLORS.limeGreen}
            href="/income"
          />
          <StatCard
            title="Total Savings"
            amount={formatMoney(totals.totalSavings)}
            count={counts.savings}
            icon={PiggyBankIcon}
            color={COLORS.blueMedium}
            href="/savings"
          />
          <StatCard
            title="Total Expenses"
            amount={formatMoney(totals.totalExpenses)}
            count={counts.expense}
            icon={ReceiptTextIcon}
            color={COLORS.orangeDark}
            href="/expenses"
          />
        </div>

        <div className="grid grid-cols-1 gap-6 lg:grid-cols-2">
          <SpendingBreakdownCard />
          <BudgetGuidelinesCard />
        </div>

        <div className="flex flex-wrap gap-3">
          <button
            type="button"
            className="zb-btn-primary"
            onClick={() => openItemModal({ mode: "create", type: "income" })}
          >
            <PlusIcon className="h-4 w-4" />
            Add Income
          </button>
          <button
            type="button"
            className="zb-btn-primary"
            onClick={() => openItemModal({ mode: "create", type: "savings" })}
          >
            <PlusIcon className="h-4 w-4" />
            Add Savings
          </button>
          <button
            type="button"
            className="zb-btn-primary"
            onClick={() => openItemModal({ mode: "create", type: "expense" })}
          >
            <PlusIcon className="h-4 w-4" />
            Add Expense
          </button>
        </div>
      </div>
    </div>
  );
}

