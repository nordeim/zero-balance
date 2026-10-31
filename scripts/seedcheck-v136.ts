// seedcheck-v136.ts — the F0 seedcheck (the v108 discipline: exact before any gate)
// Expected: 7 items / 1850 rent / 2235 expensesTotal / 0 lineItems / 3 assets / 2 liabilities
import { PrismaClient } from '@prisma/client';

const db = new PrismaClient();

async function main() {
  const items = await db.budgetItem.count();
  const rent = await db.budgetItem.findFirst({ where: { category: 'Rent' } });
  const allItems = await db.budgetItem.findMany();
  const expensesTotal = allItems
    .filter((i) => i.type === 'expense')
    .reduce((s, i) => s + i.amount, 0);
  const lineItems = await db.expenseLineItem.count();
  const assets = await db.asset.count();
  const liabilities = await db.liability.count();
  console.log(
    JSON.stringify({
      items,
      rent: rent?.amount,
      expensesTotal,
      lineItems,
      assets,
      liabilities,
    })
  );
  await db.$disconnect();
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
