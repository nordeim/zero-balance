import { describe, expect, it } from "vitest";
import {
  computeNetWorth,
  computeTotals,
  goalStatus,
  goalStatusLabel,
  spendingBreakdown,
} from "@/lib/dashboard";
import type { Asset, BudgetItem, Liability } from "@/lib/types";

// Dashboard aggregations over BudgetItem[] — the seed's exact arithmetic is
// the reference fixture:
//   income 5550 · savings 1250 · expenses 2235 → balance +2065 (Under
//   Budget), allocation 62.8%; spending: need 7370 (81.6%), want 415
//   (4.6%), savings 1250 (13.8%) over a 9035 total.

function item(partial: Partial<BudgetItem> & Pick<BudgetItem, "type" | "amount">): BudgetItem {
  return {
    id: crypto.randomUUID(),
    classification: "need",
    category: "Cat",
    frequency: "monthly",
    date: "2026-10-07",
    recurring: false,
    status: "active",
    createdAt: "2026-10-07T00:00:00.000Z",
    updatedAt: "2026-10-07T00:00:00.000Z",
    ...partial,
  };
}

const SEED: BudgetItem[] = [
  item({ type: "income", amount: 5200, classification: "need", category: "Salary" }),
  item({ type: "income", amount: 350, classification: "want", category: "Freelance" }),
  item({ type: "expense", amount: 1850, classification: "need", category: "Rent" }),
  item({ type: "expense", amount: 320, classification: "need", category: "Groceries" }),
  item({ type: "expense", amount: 65, classification: "want", category: "Entertainment" }),
  item({ type: "savings", amount: 800, classification: "savings", category: "Emergency Fund" }),
  item({ type: "savings", amount: 450, classification: "savings", category: "Investments" }),
];

describe("computeTotals", () => {
  it("computes the seed's reference numbers", () => {
    const t = computeTotals(SEED);
    expect(t.totalIncome).toBe(5550);
    expect(t.totalSavings).toBe(1250);
    expect(t.totalExpenses).toBe(2235);
    expect(t.netBalance).toBe(2065);
    expect(t.balance).toBe(2065);
    expect(t.allocationPercent).toBeCloseTo(62.79, 1);
  });

  it("treats an empty workspace as all zeros (the empty dashboard)", () => {
    const t = computeTotals([]);
    expect(t).toMatchObject({
      totalIncome: 0,
      totalSavings: 0,
      totalExpenses: 0,
      netBalance: 0,
      allocationPercent: 0,
    });
  });

  it("runs in integer-cent space — float drift never reaches a total", () => {
    const t = computeTotals([
      item({ type: "expense", amount: 0.1, classification: "need" }),
      item({ type: "expense", amount: 0.2, classification: "need" }),
      item({ type: "income", amount: 0.3, classification: "need" }),
    ]);
    expect(t.totalExpenses).toBe(0.3);
    expect(t.netBalance).toBe(0);
  });
});

describe("goalStatus", () => {
  it("classifies positive balances as under-budget", () => {
    expect(goalStatus(2065)).toBe("under-budget");
    expect(goalStatusLabel("under-budget")).toBe("Under Budget");
  });

  it("classifies sub-cent dust as net-zero (|balance| < 0.005)", () => {
    expect(goalStatus(0)).toBe("net-zero");
    expect(goalStatus(0.004)).toBe("net-zero");
    expect(goalStatus(-0.004)).toBe("net-zero");
    expect(goalStatusLabel("net-zero")).toBe("NET ZERO");
  });

  it("classifies negative balances as over-budget", () => {
    expect(goalStatus(-0.5)).toBe("over-budget");
    expect(goalStatus(-3485)).toBe("over-budget");
    expect(goalStatusLabel("over-budget")).toBe("Over Budget");
  });
});

describe("spendingBreakdown", () => {
  it("groups by classification in the reference's legend order [Savings, Want, Need]", () => {
    const rows = spendingBreakdown(SEED);
    // The reference's donut sectors + legend render Savings first (live DOM:
    // sector fills ['#8fbc3f','#3b7ea1','#e07a3b'] = [Savings, Want, Need]).
    expect(rows.map((r) => r.label)).toEqual(["Savings", "Want", "Need"]);
    expect(rows[0]).toMatchObject({ amount: 1250 });
    expect(rows[0].percent).toBeCloseTo(13.83, 1);
    expect(rows[1]).toMatchObject({ amount: 415 });
    expect(rows[1].percent).toBeCloseTo(4.59, 1);
    expect(rows[2]).toMatchObject({ amount: 7370 });
    expect(rows[2].percent).toBeCloseTo(81.57, 1);
  });

  it("zeroes every slice when there are no items", () => {
    expect(spendingBreakdown([])).toEqual([
      { key: "savings", label: "Savings", amount: 0, percent: 0 },
      { key: "want", label: "Want", amount: 0, percent: 0 },
      { key: "need", label: "Need", amount: 0, percent: 0 },
    ]);
  });
});

describe("computeNetWorth", () => {
  const assets: Asset[] = [
    { id: "a1", type: "bank_account", name: "Everyday", value: 4200, lastUpdated: "2026-10-07", createdAt: "", updatedAt: "" },
    { id: "a2", type: "superannuation", name: "Super", value: 48500, lastUpdated: "2026-10-07", createdAt: "", updatedAt: "" },
    { id: "a3", type: "investment", name: "Shares", value: 12600, lastUpdated: "2026-10-07", createdAt: "", updatedAt: "" },
  ];
  const liabilities: Liability[] = [
    { id: "l1", type: "home_loan", name: "Home Loan", value: 310000, lastUpdated: "2026-10-07", createdAt: "", updatedAt: "", interestRate: 5.75, monthlyPayment: 2050 },
    { id: "l2", type: "credit_card", name: "Card", value: 1250, lastUpdated: "2026-10-07", createdAt: "", updatedAt: "", interestRate: 19.99, monthlyPayment: 100 },
  ];

  it("computes the seed's net worth (negative) and ratio", () => {
    const t = computeNetWorth(assets, liabilities);
    expect(t.totalAssets).toBe(65300);
    expect(t.totalLiabilities).toBe(311250);
    expect(t.netWorth).toBe(-245950);
    expect(t.ratio).toBeCloseTo(0.2099, 3);
  });

  it("returns a null ratio (the ∞ : 1 case) when liabilities are zero", () => {
    const t = computeNetWorth(assets, []);
    expect(t.ratio).toBeNull();
    expect(t.netWorth).toBe(65300);
  });
});
