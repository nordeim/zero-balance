// v68 — the dev DB seed-state check before the screenshot capture.
// The capture protocol requires the exact seed state: 7 budget items,
// Rent $1850, expenses $2235, 0 line items, 3 assets, 2 liabilities.
const { PrismaClient } = require("@prisma/client");
const p = new PrismaClient();

(async () => {
  const items = await p.budgetItem.count();
  const rent = await p.budgetItem.findFirst({ where: { category: "Rent" } });
  const exps = await p.budgetItem.aggregate({ where: { type: "expense" }, _sum: { amount: true } });
  const lines = await p.expenseLineItem.count();
  const assets = await p.asset.count();
  const liabs = await p.liability.count();
  console.log(JSON.stringify({
    items,
    rentAmount: rent?.amount,
    expensesTotal: exps._sum.amount,
    lineItems: lines,
    assets,
    liabilities: liabs,
  }, null, 2));
  await p.$disconnect();
})();
