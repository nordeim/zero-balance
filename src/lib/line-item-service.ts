// The calculator's recalculation rule: the parent BudgetItem's amount is the
// sum of its line items (integer-cent arithmetic via money.ts). Pure domain
// seam — unit tested in tests/line-item-service.test.ts.

import { db } from "./db";
import { sumAmounts } from "./money";

/**
 * Recalculate a budget item's amount from its line items.
 * Returns the updated parent, or null when the item no longer exists.
 */
export async function recalcParentAmount(budgetItemId: string) {
  const lineItems = await db.expenseLineItem.findMany({
    where: { budgetItemId },
    select: { amount: true },
  });
  const total = sumAmounts(lineItems.map((li) => li.amount));
  const parent = await db.budgetItem.update({
    where: { id: budgetItemId },
    data: { amount: total },
  });
  return parent;
}

/** Pure form of the rule (unit-testable without a database). */
export function sumLineItemAmounts(amounts: number[]): number {
  return sumAmounts(amounts);
}
