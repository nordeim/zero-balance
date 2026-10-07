// Row -> API payload serializers. One place translates Prisma's rows into
// the client-facing shape (ISO date strings, null -> undefined elision) so
// every endpoint returns identical field names.

import type { Asset, BudgetItem, ExpenseLineItem, Liability } from "./types";
import type {
  Asset as AssetRow,
  BudgetItem as BudgetItemRow,
  ExpenseLineItem as LineItemRow,
  Liability as LiabilityRow,
} from "@prisma/client";

export function serializeBudgetItem(row: BudgetItemRow): BudgetItem {
  return {
    id: row.id,
    type: row.type as BudgetItem["type"],
    classification: row.classification as BudgetItem["classification"],
    amount: row.amount,
    category: row.category,
    subcategory: row.subcategory ?? undefined,
    paymentMethod: row.paymentMethod ?? undefined,
    frequency: row.frequency as BudgetItem["frequency"],
    date: row.date,
    recurring: row.recurring,
    status: row.status as BudgetItem["status"],
    notes: row.notes ?? undefined,
    createdAt: row.createdAt.toISOString(),
    updatedAt: row.updatedAt.toISOString(),
  };
}

export function serializeLineItem(row: LineItemRow): ExpenseLineItem {
  return {
    id: row.id,
    budgetItemId: row.budgetItemId,
    name: row.name,
    amount: row.amount,
    frequency: row.frequency as ExpenseLineItem["frequency"],
    provider: row.provider ?? undefined,
    policyNumber: row.policyNumber ?? undefined,
    paymentMethod: row.paymentMethod ?? undefined,
    startDate: row.startDate ?? undefined,
    endDate: row.endDate ?? undefined,
    status: row.status as ExpenseLineItem["status"],
    notes: row.notes ?? undefined,
    createdAt: row.createdAt.toISOString(),
    updatedAt: row.updatedAt.toISOString(),
  };
}

export function serializeAsset(row: AssetRow): Asset {
  return {
    id: row.id,
    type: row.type as Asset["type"],
    name: row.name,
    institution: row.institution ?? undefined,
    accountNumber: row.accountNumber ?? undefined,
    value: row.value,
    lastUpdated: row.lastUpdated,
    notes: row.notes ?? undefined,
    createdAt: row.createdAt.toISOString(),
    updatedAt: row.updatedAt.toISOString(),
  };
}

export function serializeLiability(row: LiabilityRow): Liability {
  return {
    id: row.id,
    type: row.type as Liability["type"],
    name: row.name,
    institution: row.institution ?? undefined,
    accountNumber: row.accountNumber ?? undefined,
    value: row.value,
    interestRate: row.interestRate ?? null,
    monthlyPayment: row.monthlyPayment ?? null,
    lastUpdated: row.lastUpdated,
    notes: row.notes ?? undefined,
    createdAt: row.createdAt.toISOString(),
    updatedAt: row.updatedAt.toISOString(),
  };
}
