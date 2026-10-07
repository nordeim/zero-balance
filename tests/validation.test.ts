import { describe, expect, it } from "vitest";
import {
  createAssetSchema,
  createBudgetItemSchema,
  createLineItemSchema,
  createLiabilitySchema,
  loginSchema,
  registerSchema,
  updateBudgetItemSchema,
} from "@/lib/validation";

// The validation boundary: unknown input is rejected with a field-level
// message; nothing reaches Prisma unvalidated. Every enum mirrors the
// reference app's option sets (recon-verified).

const VALID_ITEM = {
  type: "income",
  classification: "need",
  amount: 5200,
  category: "Salary",
  subcategory: "Main Job",
  paymentMethod: "Bank Account",
  frequency: "monthly",
  date: "2026-10-07",
  recurring: true,
  status: "active",
  notes: "Net monthly salary",
};

describe("createBudgetItemSchema", () => {
  it("accepts the reference-shaped payload", () => {
    const parsed = createBudgetItemSchema.parse(VALID_ITEM);
    expect(parsed.amount).toBe(5200);
    expect(parsed.type).toBe("income");
  });

  it("defaults recurring=false and status=active", () => {
    const { recurring, status, ...rest } = VALID_ITEM;
    void recurring;
    void status;
    const parsed = createBudgetItemSchema.parse(rest);
    expect(parsed.recurring).toBe(false);
    expect(parsed.status).toBe("active");
  });

  it("trims and elides blank optional text (empty string → undefined)", () => {
    const parsed = createBudgetItemSchema.parse({ ...VALID_ITEM, subcategory: "  ", notes: "" });
    expect(parsed.subcategory).toBeUndefined();
    expect(parsed.notes).toBeUndefined();
  });

  it("rejects unknown enum values with a 400-grade error", () => {
    expect(
      createBudgetItemSchema.safeParse({ ...VALID_ITEM, type: "windfall" }).success,
    ).toBe(false);
    expect(
      createBudgetItemSchema.safeParse({ ...VALID_ITEM, frequency: "sometimes" }).success,
    ).toBe(false);
    expect(
      createBudgetItemSchema.safeParse({ ...VALID_ITEM, classification: "luxury" }).success,
    ).toBe(false);
  });

  it("rejects negative and non-finite amounts", () => {
    expect(createBudgetItemSchema.safeParse({ ...VALID_ITEM, amount: -1 }).success).toBe(false);
    expect(createBudgetItemSchema.safeParse({ ...VALID_ITEM, amount: Infinity }).success).toBe(
      false,
    );
    expect(createBudgetItemSchema.safeParse({ ...VALID_ITEM, amount: "5,200" }).success).toBe(
      false,
    );
  });

  it("rejects malformed dates and impossible calendar dates", () => {
    expect(createBudgetItemSchema.safeParse({ ...VALID_ITEM, date: "07/10/2026" }).success).toBe(
      false,
    );
    expect(createBudgetItemSchema.safeParse({ ...VALID_ITEM, date: "2026-02-30" }).success).toBe(
      false,
    );
  });

  it("rejects a blank category", () => {
    expect(createBudgetItemSchema.safeParse({ ...VALID_ITEM, category: "   " }).success).toBe(
      false,
    );
  });
});

describe("updateBudgetItemSchema", () => {
  it("accepts partial payloads (PATCH semantics)", () => {
    const parsed = updateBudgetItemSchema.parse({ amount: 99.99 });
    expect(parsed.amount).toBe(99.99);
    expect(parsed.category).toBeUndefined();
  });

  it("still validates the provided fields", () => {
    expect(updateBudgetItemSchema.safeParse({ amount: -5 }).success).toBe(false);
    expect(updateBudgetItemSchema.safeParse({ status: "paused" }).success).toBe(false);
  });
});

describe("createLineItemSchema", () => {
  it("accepts the calculator payload and defaults frequency/status", () => {
    const parsed = createLineItemSchema.parse({
      budgetItemId: "item-1",
      name: "Contents Insurance",
      amount: 25,
    });
    expect(parsed.frequency).toBe("monthly");
    expect(parsed.status).toBe("active");
  });

  it("line items carry their OWN status enum (active/pending/cancelled — the reference's calculator form)", () => {
    // The reference's Add Line Item dialog offers Active / Pending /
    // Cancelled — distinct from BudgetItem's planned/active/completed.
    for (const status of ["active", "pending", "cancelled"]) {
      const parsed = createLineItemSchema.parse({
        budgetItemId: "item-1",
        name: "Policy",
        amount: 10,
        status,
      });
      expect(parsed.status).toBe(status);
    }
    // BudgetItem-only statuses are INVALID for line items.
    for (const status of ["planned", "completed"]) {
      expect(
        createLineItemSchema.safeParse({
          budgetItemId: "item-1",
          name: "Policy",
          amount: 10,
          status,
        }).success,
      ).toBe(false);
    }
    // …while they stay valid for budget items.
    expect(createBudgetItemSchema.safeParse({ ...VALID_ITEM, status: "planned" }).success).toBe(true);
  });

  it("accepts empty-string optional dates (the native date inputs send \"\" when cleared)", () => {
    const parsed = createLineItemSchema.parse({
      budgetItemId: "item-1",
      name: "Contents Insurance",
      amount: 25,
      startDate: "",
      endDate: "",
    });
    expect(parsed.startDate).toBeUndefined();
    expect(parsed.endDate).toBeUndefined();
    // A real date still passes through.
    const dated = createLineItemSchema.parse({
      budgetItemId: "item-1",
      name: "Contents Insurance",
      amount: 25,
      startDate: "2026-10-07",
    });
    expect(dated.startDate).toBe("2026-10-07");
    // But a malformed one is still rejected.
    expect(
      createLineItemSchema.safeParse({
        budgetItemId: "item-1",
        name: "X",
        amount: 1,
        startDate: "2026-13-01",
      }).success,
    ).toBe(false);
  });

  it("requires a name and a budgetItemId", () => {
    expect(createLineItemSchema.safeParse({ budgetItemId: "x", name: "", amount: 1 }).success).toBe(
      false,
    );
    expect(createLineItemSchema.safeParse({ name: "Y", amount: 1 }).success).toBe(false);
  });
});

describe("asset and liability schemas", () => {
  const VALID_ASSET = {
    type: "bank_account",
    name: "Everyday Account",
    value: 4200,
    lastUpdated: "2026-10-07",
  };

  it("accepts the asset payload and rejects unknown asset types", () => {
    expect(createAssetSchema.safeParse(VALID_ASSET).success).toBe(true);
    expect(createAssetSchema.safeParse({ ...VALID_ASSET, type: "crypto" }).success).toBe(false);
  });

  const VALID_LIABILITY = {
    type: "home_loan",
    name: "NAB Home Loan",
    value: 310000,
    lastUpdated: "2026-10-07",
    interestRate: 5.75,
    monthlyPayment: 2050,
  };

  it("accepts the liability payload with its optional numeric fields", () => {
    const parsed = createLiabilitySchema.parse(VALID_LIABILITY);
    expect(parsed.interestRate).toBe(5.75);
    expect(parsed.monthlyPayment).toBe(2050);
  });

  it("caps interest rates at 100 and rejects unknown liability types", () => {
    expect(
      createLiabilitySchema.safeParse({ ...VALID_LIABILITY, interestRate: 101 }).success,
    ).toBe(false);
    expect(createLiabilitySchema.safeParse({ ...VALID_LIABILITY, type: "tax_debt" }).success).toBe(
      false,
    );
  });
});

describe("auth schemas", () => {
  it("normalizes the email (trim + lowercase)", () => {
    const parsed = loginSchema.parse({ email: "  Demo@ZeroBalance.APP ", password: "Demo1234!" });
    expect(parsed.email).toBe("demo@zerobalance.app");
  });

  it("requires 8+ char passwords at register but only non-empty at login", () => {
    expect(registerSchema.safeParse({ email: "a@b.co", password: "short" }).success).toBe(false);
    expect(loginSchema.safeParse({ email: "a@b.co", password: "short" }).success).toBe(true);
    expect(loginSchema.safeParse({ email: "a@b.co", password: "" }).success).toBe(false);
  });

  it("rejects malformed emails", () => {
    expect(registerSchema.safeParse({ email: "not-an-email", password: "Demo1234!" }).success).toBe(
      false,
    );
  });
});
