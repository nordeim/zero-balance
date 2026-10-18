// v84 — the dev DB seed-state check (the v68 discipline's ESM twin, run
// under `env -u DATABASE_URL` from the repo root). The capture protocol
// requires the exact seed state: 7 budget items, Rent $1850, expenses
// $2235, 0 line items, 3 assets, 2 liabilities.
import { PrismaClient } from "@prisma/client";
const p = new PrismaClient();
const items = await p.budgetItem.findMany({ select: { type: true, amount: true, category: true, subcategory: true } });
const rent = items.find(i => (i.category + " " + (i.subcategory || "")).toLowerCase().includes("rent"));
const expenses = items.filter(i => i.type === "expense");
const lineItems = await p.expenseLineItem.count();
const assets = await p.asset.count();
const liabilities = await p.liability.count();
console.log(JSON.stringify({
  items: items.length,
  rent: rent ? rent.amount : null,
  expensesTotal: expenses.reduce((s, i) => s + i.amount, 0),
  lineItems, assets, liabilities
}));
await p.$disconnect();
