"use client";

// The Rent Calculator — breaks an expense category into line items; the
// "Total Calculated" updates the category's amount (recalculated server-side
// on every line-item mutation, mirroring the reference).

import * as React from "react";
import {
  CalculatorIcon,
  PencilIcon,
  PlusIcon,
  Trash2Icon,
} from "lucide-react";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { useToast } from "@/components/ui/toast";
import { messageOf, useBudgetStore } from "./store";
import { formatMoney, sumAmounts } from "@/lib/money";
import { rgb } from "@/lib/constants";
import type { ExpenseLineItem } from "@/lib/types";

function formatDate(iso: string | null | undefined): string {
  if (!iso) return "";
  const d = new Date(`${iso}T00:00:00`);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" });
}

export function CalculatorDialog() {
  const modal = useBudgetStore((s) => s.modal.calculator);
  const closeModals = useBudgetStore((s) => s.closeModals);
  const lineItemsMap = useBudgetStore((s) => s.lineItems);
  const loadLineItems = useBudgetStore((s) => s.loadLineItems);
  const openLineItemModal = useBudgetStore((s) => s.openLineItemModal);
  const deleteLineItem = useBudgetStore((s) => s.deleteLineItem);
  const { toast } = useToast();
  const [confirmingId, setConfirmingId] = React.useState<string | null>(null);
  const item = modal?.item ?? null;

  React.useEffect(() => {
    if (item) void loadLineItems(item.id);
  }, [item, loadLineItems]);

  if (!modal || !item) return null;
  const lineItems = lineItemsMap[item.id] ?? [];
  const total = sumAmounts(lineItems.map((li) => li.amount));

  const onDelete = async (id: string) => {
    try {
      await deleteLineItem(id);
      setConfirmingId(null);
      toast({ title: "Line item removed", description: "Category total recalculated", variant: "success" });
    } catch (error) {
      toast({ title: "Could not remove the line item", description: messageOf(error), variant: "error" });
    }
  };

  return (
    <Dialog open onOpenChange={(open) => !open && closeModals()}>
      <DialogContent>
        <DialogHeader>
          {/* Category-adaptive chrome, measured on the reference: the Rent
              card opens "Rent Calculator / Break down your rent into
              individual items", the Investments card "Investments
              Calculator / Break down your investments into individual
              items" — the title carries the category's case, the
              description lowercases it. */}
          <DialogTitle>{item.category} Calculator</DialogTitle>
          <DialogDescription>
            Break down your {item.category.toLowerCase()} into individual items
          </DialogDescription>
        </DialogHeader>
        <div className="p-6">
          <div
            className="mb-6 flex items-center justify-between rounded-xl p-4"
            style={{ backgroundColor: rgb.cardTint }}
          >
            <div className="flex items-center gap-3">
              <div
                className="flex h-10 w-10 items-center justify-center rounded-lg"
                style={{ backgroundColor: "rgba(224, 122, 59, 0.125)" }}
              >
                <CalculatorIcon className="h-5 w-5" style={{ color: rgb.orangeDark }} />
              </div>
              <div>
                <p className="text-sm" style={{ color: rgb.gray }}>
                  Total Calculated
                </p>
                <p className="text-2xl font-bold" style={{ color: rgb.forestDark }}>
                  {formatMoney(total)}
                </p>
              </div>
            </div>
            <p className="max-w-[220px] text-right text-xs" style={{ color: rgb.gray }}>
              Based on {lineItems.length} {lineItems.length === 1 ? "item" : "items"} · Will update
              category total
            </p>
          </div>

          <div className="mb-3 flex items-center justify-between">
            <h3 className="font-semibold" style={{ color: rgb.forestDark }}>
              Line Items
            </h3>
            <button
              type="button"
              className="zb-btn-primary"
              onClick={() => openLineItemModal({ mode: "create", budgetItemId: item.id })}
            >
              <PlusIcon className="h-4 w-4" />
              Add Item
            </button>
          </div>

          {lineItems.length === 0 ? (
            <div className="flex flex-col items-center justify-center py-12 text-center">
              <CalculatorIcon className="mb-3 h-10 w-10" style={{ color: "rgb(203, 213, 225)" }} />
              <p className="mb-1 font-medium" style={{ color: "rgb(156, 163, 175)" }}>
                No line items yet.
              </p>
              <p className="mb-6 max-w-sm text-sm" style={{ color: "rgb(156, 163, 175)" }}>
                Start by adding individual items that make up this category.
              </p>
              <button
                type="button"
                className="zb-btn-primary"
                onClick={() => openLineItemModal({ mode: "create", budgetItemId: item.id })}
              >
                <PlusIcon className="h-4 w-4" />
                Add First Item
              </button>
            </div>
          ) : (
            <div className="space-y-3">
              {lineItems.map((li: ExpenseLineItem) => (
                <div
                  key={li.id}
                  className="rounded-xl bg-white p-4"
                  style={{ border: `1px solid ${rgb.border}` }}
                >
                  <div className="mb-2 flex items-start justify-between">
                    <div>
                      <h4 className="font-semibold" style={{ color: rgb.forestDark }}>
                        {li.name}
                      </h4>
                      {li.provider && (
                        <p className="text-sm" style={{ color: rgb.gray }}>
                          {li.provider}
                          {li.policyNumber ? ` · ${li.policyNumber}` : ""}
                        </p>
                      )}
                    </div>
                    <div className="flex items-center gap-1">
                      <button
                        type="button"
                        aria-label={`Edit ${li.name}`}
                        className="inline-flex h-8 w-8 items-center justify-center rounded-md transition-colors hover:bg-accent"
                        onClick={() => openLineItemModal({ mode: "edit", lineItem: li })}
                      >
                        <PencilIcon className="h-4 w-4" style={{ color: rgb.gray }} />
                      </button>
                      <button
                        type="button"
                        aria-label={`Delete ${li.name}`}
                        className="inline-flex h-8 w-8 items-center justify-center rounded-md transition-colors hover:bg-red-50"
                        onClick={() => setConfirmingId(confirmingId === li.id ? null : li.id)}
                      >
                        <Trash2Icon className="h-4 w-4 text-red-500" />
                      </button>
                    </div>
                  </div>
                  <div className="mb-2 flex flex-wrap gap-2">
                    <span className="inline-flex items-center rounded-md border border-transparent bg-purple-50 px-2.5 py-0.5 text-xs font-semibold text-purple-700">
                      {li.frequency}
                    </span>
                    <span className="inline-flex items-center rounded-md border border-transparent bg-slate-50 px-2.5 py-0.5 text-xs font-semibold text-slate-700">
                      {li.status}
                    </span>
                  </div>
                  <div className="flex items-center justify-between">
                    <p className="text-sm" style={{ color: rgb.gray }}>
                      {li.startDate ? `From ${formatDate(li.startDate)}` : ""}
                    </p>
                    <p className="text-xl font-bold" style={{ color: rgb.orangeDark }}>
                      {formatMoney(li.amount)}
                    </p>
                  </div>
                  {confirmingId === li.id && (
                    <div
                      className="mt-3 flex items-center justify-between rounded-lg p-3"
                      style={{ backgroundColor: "rgb(254, 242, 242)" }}
                    >
                      <p className="text-sm text-red-700">Delete this line item?</p>
                      <div className="flex gap-2">
                        <button
                          type="button"
                          className="rounded-md bg-white px-3 py-1 text-xs font-medium text-slate-700 shadow-sm"
                          onClick={() => setConfirmingId(null)}
                        >
                          Cancel
                        </button>
                        <button
                          type="button"
                          className="rounded-md bg-red-600 px-3 py-1 text-xs font-medium text-white"
                          onClick={() => void onDelete(li.id)}
                        >
                          Delete
                        </button>
                      </div>
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}
