// v68 — the dev DB seed-state check before the screenshot capture.
// The capture protocol requires the exact seed state: 7 budget items,
// Rent $1850, expenses $2235, 0 line items, 3 assets, 2 liabilities.
// v69: the repo's only .cjs — CommonJS require() by design (the Prisma
// CJS runtime); the single-file disable keeps the lint gate green without
// weakening it for the rest of scripts/ (the v68 ship missed this — the
// file was created after the final lint run; the v69 audit's F0 repair).
/* eslint-disable @typescript-eslint/no-require-imports */
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
