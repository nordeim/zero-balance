// verify-seed-dates-v154.ts — the canonical Oct-31 stamp check (the v152 alignment held?)
import { PrismaClient } from '@prisma/client';

const db = new PrismaClient();

async function main() {
  const items = await db.budgetItem.findMany({ orderBy: { date: 'asc' } });
  const assets = await db.asset.findMany();
  const liab = await db.liability.findMany();
  console.log('items.dates:', items.map((i) => `${i.category}:${String(i.date).slice(0, 10)}`).join(' | '));
  console.log('assets.lastUpdated:', assets.map((a) => `${a.name}:${String(a.lastUpdated).slice(0, 10)}`).join(' | '));
  console.log('liabilities.lastUpdated:', liab.map((l) => `${l.name}:${String(l.lastUpdated).slice(0, 10)}`).join(' | '));
  await db.$disconnect();
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
