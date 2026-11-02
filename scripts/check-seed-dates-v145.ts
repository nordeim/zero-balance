// check-seed-dates-v145.ts — what date did today's fresh re-seed stamp (the canonical state is Oct 31)?
import { PrismaClient } from '@prisma/client';

const db = new PrismaClient();

async function main() {
  const items = await db.budgetItem.findMany({ select: { category: true, subcategory: true, date: true }, orderBy: { date: 'asc' } });
  const assets = await db.asset.findMany({ select: { name: true, lastUpdated: true } });
  const liabilities = await db.liability.findMany({ select: { name: true, lastUpdated: true } });
  console.log(
    JSON.stringify({
      items: items.map((i) => [i.category, i.date]),
      assets: assets.map((a) => [a.name, a.lastUpdated]),
      liabilities: liabilities.map((l) => [l.name, l.lastUpdated]),
    })
  );
  await db.$disconnect();
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
