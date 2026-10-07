// Dashboard aggregations — pure functions over BudgetItem[] (unit tested in
// tests/dashboard-math.test.ts). All sums run through money.ts's integer-cent
// arithmetic.

import { sumAmounts } from "./money";
import type { Asset, BudgetItem, Classification, Liability } from "./types";

export interface DashboardTotals {
  totalIncome: number;
  totalSavings: number;
  totalExpenses: number;
  netBalance: number;
  /** (savings + expenses) / income, as a percentage number (0-100+). */
  allocationPercent: number;
  /** income - savings - expenses. */
  balance: number;
}

export type GoalStatus = "net-zero" | "under-budget" | "over-budget";

export interface SpendingSlice {
  key: Classification;
  label: string;
  amount: number;
  percent: number;
}

export function computeTotals(items: BudgetItem[]): DashboardTotals {
  const byType = (type: BudgetItem["type"]) =>
    items.filter((i) => i.type === type).map((i) => i.amount);
  const totalIncome = sumAmounts(byType("income"));
  const totalSavings = sumAmounts(byType("savings"));
  const totalExpenses = sumAmounts(byType("expense"));
  const allocationPercent =
    totalIncome > 0 ? ((totalSavings + totalExpenses) / totalIncome) * 100 : 0;
  return {
    totalIncome,
    totalSavings,
    totalExpenses,
    netBalance: totalIncome - totalSavings - totalExpenses,
    allocationPercent,
    balance: totalIncome - totalSavings - totalExpenses,
  };
}

export function goalStatus(balance: number): GoalStatus {
  if (Math.abs(balance) < 0.005) return "net-zero";
  return balance > 0 ? "under-budget" : "over-budget";
}

export function goalStatusLabel(status: GoalStatus): string {
  if (status === "net-zero") return "NET ZERO";
  return status === "under-budget" ? "Under Budget" : "Over Budget";
}

/** Spending Breakdown — amounts grouped by classification over ALL items. */
export function spendingBreakdown(items: BudgetItem[]): SpendingSlice[] {
  const groups: { key: Classification; label: string }[] = [
    { key: "need", label: "Need" },
    { key: "want", label: "Want" },
    { key: "savings", label: "Savings" },
  ];
  const total = sumAmounts(items.map((i) => i.amount));
  return groups.map(({ key, label }) => {
    const amount = sumAmounts(items.filter((i) => i.classification === key).map((i) => i.amount));
    return {
      key,
      label,
      amount,
      percent: total > 0 ? (amount / total) * 100 : 0,
    };
  });
}

export interface NetWorthTotals {
  totalAssets: number;
  totalLiabilities: number;
  netWorth: number;
  /** assets / liabilities; null when liabilities are zero. */
  ratio: number | null;
}

export function computeNetWorth(assets: Asset[], liabilities: Liability[]): NetWorthTotals {
  const totalAssets = sumAmounts(assets.map((a) => a.value));
  const totalLiabilities = sumAmounts(liabilities.map((l) => l.value));
  return {
    totalAssets,
    totalLiabilities,
    netWorth: totalAssets - totalLiabilities,
    ratio: totalLiabilities > 0 ? totalAssets / totalLiabilities : null,
  };
}
