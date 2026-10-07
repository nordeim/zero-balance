import { describe, expect, it } from "vitest";
import {
  serializeAsset,
  serializeBudgetItem,
  serializeLiability,
  serializeLineItem,
} from "@/lib/serializers";
import type {
  Asset as AssetRow,
  BudgetItem as BudgetItemRow,
  ExpenseLineItem as LineItemRow,
  Liability as LiabilityRow,
} from "@prisma/client";

// Row → API payload serializers: Prisma's rows become the client-facing
// shape (ISO date strings, null → undefined elision) so every endpoint
// returns identical field names — the reference's camelCase payloads.

const ts = new Date("2026-10-07T12:00:00.000Z");

describe("serializeBudgetItem", () => {
  it("elides null optional fields and ISO-formats timestamps", () => {
    const row = {
      id: "bi-1",
      userId: "u-1",
      type: "expense",
      classification: "need",
      amount: 1850,
      category: "Rent",
      subcategory: null,
      paymentMethod: "Bank Transfer",
      frequency: "monthly",
      date: "2026-10-07",
      recurring: true,
      status: "active",
      notes: null,
      createdAt: ts,
      updatedAt: ts,
    } as BudgetItemRow;

    const out = serializeBudgetItem(row);
    expect(out).toMatchObject({
      id: "bi-1",
      type: "expense",
      classification: "need",
      amount: 1850,
      category: "Rent",
      subcategory: undefined,
      paymentMethod: "Bank Transfer",
      frequency: "monthly",
      recurring: true,
      status: "active",
      notes: undefined,
      createdAt: "2026-10-07T12:00:00.000Z",
      updatedAt: "2026-10-07T12:00:00.000Z",
    });
    expect("userId" in out).toBe(false); // server-only field never leaks
  });

  it("passes through present optional fields", () => {
    const row = {
      id: "bi-2",
      userId: "u-1",
      type: "income",
      classification: "need",
      amount: 5200,
      category: "Salary",
      subcategory: "Main Job",
      paymentMethod: null,
      frequency: "monthly",
      date: "2026-10-07",
      recurring: true,
      status: "active",
      notes: "Net monthly salary",
      createdAt: ts,
      updatedAt: ts,
    } as BudgetItemRow;

    expect(serializeBudgetItem(row).subcategory).toBe("Main Job");
    expect(serializeBudgetItem(row).paymentMethod).toBeUndefined();
  });
});

describe("serializeLineItem", () => {
  it("carries the budgetItemId link and elides nulls", () => {
    const row = {
      id: "li-1",
      budgetItemId: "bi-1",
      name: "Contents Insurance",
      amount: 25,
      frequency: "monthly",
      provider: "AAMI",
      policyNumber: null,
      paymentMethod: null,
      startDate: "2026-10-07",
      endDate: null,
      status: "active",
      notes: null,
      createdAt: ts,
      updatedAt: ts,
    } as unknown as LineItemRow;

    const out = serializeLineItem(row);
    expect(out.budgetItemId).toBe("bi-1");
    expect(out.provider).toBe("AAMI");
    expect(out.policyNumber).toBeUndefined();
    expect(out.endDate).toBeUndefined();
    expect(out.startDate).toBe("2026-10-07");
  });
});

describe("serializeAsset / serializeLiability", () => {
  it("serializes the asset shape", () => {
    const row = {
      id: "as-1",
      userId: "u-1",
      type: "bank_account",
      name: "Everyday Account",
      institution: "Commonwealth Bank",
      accountNumber: "•••• 4821",
      value: 4200,
      lastUpdated: "2026-10-07",
      notes: null,
      createdAt: ts,
      updatedAt: ts,
    } as AssetRow;

    const out = serializeAsset(row);
    expect(out).toMatchObject({ type: "bank_account", value: 4200, notes: undefined });
    expect("userId" in out).toBe(false);
  });

  it("keeps explicit nulls for the liability's optional numerics", () => {
    const row = {
      id: "lb-1",
      userId: "u-1",
      type: "credit_card",
      name: "Credit Card",
      institution: null,
      accountNumber: "•••• 7745",
      value: 1250,
      interestRate: 19.99,
      monthlyPayment: 100,
      lastUpdated: "2026-10-07",
      notes: null,
      createdAt: ts,
      updatedAt: ts,
    } as LiabilityRow;

    const out = serializeLiability(row);
    expect(out.interestRate).toBe(19.99);
    expect(out.monthlyPayment).toBe(100);
    expect(out.institution).toBeUndefined();
    // A liability with no rate serializes null (not undefined) — the
    // reference's optional numerics distinguish "unset".
    const bare = serializeLiability({ ...row, interestRate: null, monthlyPayment: null });
    expect(bare.interestRate).toBeNull();
    expect(bare.monthlyPayment).toBeNull();
  });
});
