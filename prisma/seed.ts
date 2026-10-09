// Idempotent demo seed — mirrors a realistic budget so a fresh checkout has
// data on every view. Safe to re-run: it upserts the demo user and reuses
// its items by natural keys (type + category + subcategory).

import { PrismaClient } from "@prisma/client";
import { randomBytes, scryptSync } from "node:crypto";
import { resolveProcessDatabaseUrl } from "../src/lib/db-path";

process.env.DATABASE_URL = resolveProcessDatabaseUrl();

const db = new PrismaClient();

function hashPassword(password: string): string {
  const salt = randomBytes(16).toString("hex");
  const hash = scryptSync(password, salt, 64).toString("hex");
  return `${salt}:${hash}`;
}

function isoDate(offsetDays = 0): string {
  const d = new Date();
  d.setDate(d.getDate() + offsetDays);
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

const DEMO_EMAIL = "demo@zerobalance.app";
const DEMO_PASSWORD = "Demo1234!";

const ITEMS = [
  {
    type: "income",
    classification: "need",
    amount: 5200,
    category: "Salary",
    subcategory: "Main Job",
    paymentMethod: "Bank Account",
    frequency: "monthly",
    recurring: true,
    status: "active",
    date: isoDate(-10),
    notes: "Net monthly salary",
  },
  {
    type: "income",
    classification: "want",
    amount: 350,
    category: "Freelance",
    subcategory: "Side Projects",
    paymentMethod: "PayPal",
    frequency: "monthly",
    recurring: false,
    status: "active",
    date: isoDate(-5),
    notes: "",
  },
  {
    type: "expense",
    classification: "need",
    amount: 1850,
    category: "Rent",
    subcategory: "Apartment",
    paymentMethod: "Bank Transfer",
    frequency: "monthly",
    recurring: true,
    status: "active",
    date: isoDate(-9),
    notes: "",
  },
  {
    type: "expense",
    classification: "need",
    amount: 320,
    category: "Groceries",
    subcategory: "Weekly Shop",
    paymentMethod: "Credit Card",
    frequency: "weekly",
    recurring: true,
    status: "active",
    date: isoDate(-3),
    notes: "",
  },
  {
    type: "expense",
    classification: "want",
    amount: 65,
    category: "Entertainment",
    subcategory: "Streaming",
    paymentMethod: "Credit Card",
    frequency: "monthly",
    recurring: true,
    status: "active",
    date: isoDate(-2),
    notes: "",
  },
  {
    type: "savings",
    classification: "savings",
    amount: 800,
    category: "Emergency Fund",
    subcategory: "Safety Net",
    paymentMethod: "Bank Account",
    frequency: "monthly",
    recurring: true,
    status: "active",
    date: isoDate(-8),
    notes: "6 months of expenses",
  },
  {
    type: "savings",
    classification: "savings",
    amount: 450,
    category: "Investments",
    subcategory: "Index Funds",
    paymentMethod: "Brokerage",
    frequency: "monthly",
    recurring: true,
    status: "active",
    date: isoDate(-7),
    notes: "",
  },
] as const;

const ASSETS = [
  {
    type: "bank_account",
    name: "Everyday Account",
    institution: "Commonwealth Bank",
    accountNumber: "•••• 4821",
    value: 4200,
    lastUpdated: isoDate(0),
    notes: "",
  },
  {
    type: "superannuation",
    name: "Superannuation",
    institution: "Australian Super",
    accountNumber: "•••• 9930",
    value: 48500,
    lastUpdated: isoDate(0),
    notes: "",
  },
  {
    type: "investment",
    name: "Share Portfolio",
    institution: "SelfWealth",
    accountNumber: "",
    value: 12600,
    lastUpdated: isoDate(0),
    notes: "",
  },
] as const;

const LIABILITIES = [
  {
    type: "home_loan",
    name: "Home Loan",
    institution: "NAB",
    accountNumber: "•••• 1102",
    value: 310000,
    interestRate: 5.75,
    monthlyPayment: 2050,
    lastUpdated: isoDate(0),
    notes: "",
  },
  {
    type: "credit_card",
    name: "Credit Card",
    institution: "CBA",
    accountNumber: "•••• 7745",
    value: 1250,
    interestRate: 19.99,
    monthlyPayment: 100,
    lastUpdated: isoDate(0),
    notes: "",
  },
] as const;

async function main() {
  const user = await db.user.upsert({
    where: { email: DEMO_EMAIL },
    update: {
      // v21 G3: existing demo DBs upgraded in place — a demo user that
      // predates the verification gate must stay loggable (the gate only
      // applies to fresh registrations).
      emailVerifiedAt: new Date(),
    },
    create: {
      email: DEMO_EMAIL,
      passwordHash: hashPassword(DEMO_PASSWORD),
      name: "Demo User",
      // v21 G3: the seeded demo account ships PRE-VERIFIED — the reference
      // platform's demo/login flows assume a usable account, and every
      // login-dependent spec (auth setup, smoke) uses it.
      emailVerifiedAt: new Date(),
    },
  });

  for (const item of ITEMS) {
    const existing = await db.budgetItem.findFirst({
      where: {
        userId: user.id,
        type: item.type,
        category: item.category,
        subcategory: item.subcategory,
      },
    });
    if (!existing) {
      await db.budgetItem.create({ data: { ...item, userId: user.id } });
    }
  }

  for (const asset of ASSETS) {
    const existing = await db.asset.findFirst({
      where: { userId: user.id, type: asset.type, name: asset.name },
    });
    if (!existing) {
      await db.asset.create({ data: { ...asset, userId: user.id } });
    }
  }

  for (const liability of LIABILITIES) {
    const existing = await db.liability.findFirst({
      where: { userId: user.id, type: liability.type, name: liability.name },
    });
    if (!existing) {
      await db.liability.create({ data: { ...liability, userId: user.id } });
    }
  }

  const itemCount = await db.budgetItem.count({ where: { userId: user.id } });
  const assetCount = await db.asset.count({ where: { userId: user.id } });
  const liabilityCount = await db.liability.count({ where: { userId: user.id } });
  console.log(
    `Seeded demo workspace: ${itemCount} budget items, ${assetCount} assets, ${liabilityCount} liabilities (user ${DEMO_EMAIL})`,
  );
}

main()
  .catch((error) => {
    console.error(error);
    process.exit(1);
  })
  .finally(() => db.$disconnect());
