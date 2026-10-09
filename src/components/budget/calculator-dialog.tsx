"use client";

// The {Category} Calculator — breaks an expense category into line items; the
// "Total Calculated" updates the category's amount (recalculated server-side
// on every line-item mutation, mirroring the reference).
//
// Chrome pinned by the session-3 audit (live DOM + bundle):
//   - wide panel (max-w-3xl) with a border-b header carrying an orange
//     gradient icon chip, the h2 title + description, and a Close X button
//   - an orange-tinted total card: "Total Calculated" left, amount right in
//     #e07a3b, "Based on N item(s)" + a conditional orange "• Will update
//     category total" (shown while total !== the category's amount)
//   - line-item rows: gray rounded-[9999px] pills (frequency + conditional
//     status), "#policy" line, hover-revealed ghost edit/delete, orange
//     text-xl amount — no "From date"

import * as React from "react";
import {
  CalculatorIcon,
  PenIcon,
  PlusIcon,
  Trash2Icon,
  XIcon,
} from "lucide-react";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogTitle,
} from "@/components/ui/dialog";
import { useToast } from "@/components/ui/toast";
import { messageOf, useBudgetStore } from "./store";
import { formatMoney, sumAmounts } from "@/lib/money";
import { ADD_BUTTON_GRADIENTS, COLORS, rgb } from "@/lib/constants";
import { cn } from "@/lib/utils";
import type { ExpenseLineItem, LineItemStatus } from "@/lib/types";

/**
 * Line-item status pills — the reference's own conditional map: active →
 * green, pending → yellow, cancelled → gray. Line items carry their own
 * Active/Pending/Cancelled enum (NOT the budget-item planned/completed
 * trio) — see docs/remediation-plan-v3.md F4.
 */
function statusPill(status: LineItemStatus): string {
  // Arbitrary hex pins — v4 computes the named green/yellow/gray classes
  // as oklab (reference: green-50 #f0fdf4 / green-700 #15803d etc., v6 G11).
  if (status === "active") return "bg-[#f0fdf4] text-[#15803d]";
  if (status === "pending") return "bg-[#fefce0] text-[#a16207]";
  return "bg-[#f9fafb] text-[#374151]";
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
    // v17 G1: the load failure must be CAUGHT, not swallowed — the
    // pre-fix `void loadLineItems(item.id)` left the rejection unhandled
    // and silent. The reference renders the same scenario as its SILENT
    // empty-state (a dead API indistinguishable from an empty category —
    // measured live, plan v17); the clone keeps those surfaces (the
    // `?? []` fallback below renders the reference's empty state) and
    // adds the honest error toast, the same superset class as the v16
    // boot toast and the dialogs' mutation-failure toasts. Per-open
    // semantics (a fresh user action each time), NOT a one-shot flag.
    if (item) {
      loadLineItems(item.id).catch((error: unknown) => {
        toast({
          title: "Could not load the line items",
          description: messageOf(error),
          variant: "error",
        });
      });
    }
  }, [item, loadLineItems, toast]);

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
      <DialogContent
        aria-describedby={undefined}
        style={{
          maxWidth: "48rem" /* max-w-3xl — wider than the form dialogs */,
          maxHeight: "85vh",
          overflow: "hidden",
          display: "flex",
          flexDirection: "column",
        }}
      >
        {/* Header: gradient chip + title/description + Close X (flex child). */}
        <div
          className="flex items-center justify-between border-b px-6 py-4"
          style={{ borderColor: rgb.border }}
        >
          <div className="flex items-center gap-3">
            <div
              className="flex h-10 w-10 items-center justify-center rounded-xl"
              style={{ background: ADD_BUTTON_GRADIENTS.calculator }}
            >
              <CalculatorIcon className="h-5 w-5 text-white" />
            </div>
            <div>
              {/* Category-adaptive chrome, measured on the reference: the Rent
                  card opens "Rent Calculator / Break down your rent into
                  individual items" — the title carries the category's case,
                  the description lowercases it. */}
              <DialogTitle className="text-lg font-bold" style={{ color: rgb.forestDark }}>
                {item.category} Calculator
              </DialogTitle>
              <DialogDescription className="text-sm" style={{ color: rgb.gray }}>
                Break down your {item.category.toLowerCase()} into individual items
              </DialogDescription>
            </div>
          </div>
          <button
            type="button"
            aria-label="Close"
            className="inline-flex h-9 w-9 items-center justify-center rounded-md text-[#0a0a0a] transition-colors hover:bg-accent"
            onClick={closeModals}
          >
            {/* Reference calculator X (measured live): 36×36 button, 16px
                lucide-x in #0a0a0a — plan v9 G2. */}
            <XIcon className="h-4 w-4" />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-6">
          <div
            className="mb-6 rounded-xl p-4"
            style={{ backgroundColor: "#fff7f5", border: "1px solid #fcddd5" }}
          >
            <div className="mb-2 flex items-center justify-between">
              <span className="text-sm font-medium" style={{ color: rgb.gray }}>
                Total Calculated
              </span>
              <span className="text-2xl font-bold" style={{ color: COLORS.orangeDark }}>
                {formatMoney(total)}
              </span>
            </div>
            <div className="flex items-center justify-between text-xs" style={{ color: rgb.gray }}>
              <span>
                Based on {lineItems.length} {lineItems.length === 1 ? "item" : "items"}
              </span>
              {total !== item.amount && (
                <span className="text-[#ea580c]">• Will update category total</span>
              )}
            </div>
          </div>

          <div className="mb-4 flex items-center justify-between">
            <h3 className="font-semibold" style={{ color: rgb.forestDark }}>
              Line Items
            </h3>
            <button
              type="button"
              className="zb-btn-add zb-btn-add-sm text-white"
              style={{ background: ADD_BUTTON_GRADIENTS.calculator }}
              onClick={() => openLineItemModal({ mode: "create", budgetItemId: item.id })}
            >
              <PlusIcon className="mr-2 h-4 w-4" />
              Add Item
            </button>
          </div>

          {lineItems.length === 0 ? (
            <div className="py-12 text-center">
              <CalculatorIcon className="mx-auto mb-3 h-12 w-12 text-[#0a0a0a] opacity-20" />
              <p className="mb-4 text-sm" style={{ color: rgb.gray }}>
                No line items yet. Start by adding individual items that make up this category.
              </p>
              <button
                type="button"
                className="zb-btn-add zb-btn-add-sm zb-btn-add-outline"
                onClick={() => openLineItemModal({ mode: "create", budgetItemId: item.id })}
              >
                <PlusIcon className="mr-2 h-4 w-4" />
                Add First Item
              </button>
            </div>
          ) : (
            <div className="space-y-3">
              {lineItems.map((li: ExpenseLineItem) => (
                <div
                  key={li.id}
                  className="group rounded-xl border bg-white p-4 transition-all hover:shadow-md"
                  style={{ borderColor: rgb.border }}
                >
                  <div className="mb-2 flex items-start justify-between">
                    <div className="flex-1">
                      <h4 className="mb-1 font-semibold" style={{ color: rgb.forestDark }}>
                        {li.name}
                      </h4>
                      {li.provider && (
                        <p className="text-sm" style={{ color: rgb.gray }}>
                          {li.provider}
                        </p>
                      )}
                    </div>
                    {/* Reference row actions (v21 re-measure): HOVER-REVEALED —
                        the live reference wraps the pair in opacity-0
                        group-hover:opacity-100 (measured at rest; the v6-era
                        always-visible chrome predates the reference's change).
                        32px buttons, 16px icons, edit near-black, delete red
                        (v6 G10 geometry/colors hold). The globals.css
                        @variant group-hover pin keeps the reveal working on
                        hover:none devices — never remove it. */}
                    <div className="flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                      <button
                        type="button"
                        aria-label={`Edit ${li.name}`}
                        className="inline-flex h-8 w-8 items-center justify-center rounded-md text-[#0a0a0a] transition-colors hover:bg-accent"
                        onClick={() => openLineItemModal({ mode: "edit", lineItem: li })}
                      >
                        <PenIcon className="h-4 w-4" />
                      </button>
                      <button
                        type="button"
                        aria-label={`Delete ${li.name}`}
                        className="inline-flex h-8 w-8 items-center justify-center rounded-md text-[#dc2626] transition-colors hover:bg-accent"
                        onClick={() => setConfirmingId(confirmingId === li.id ? null : li.id)}
                      >
                        <Trash2Icon className="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                  <div className="flex items-end justify-between">
                    <div className="space-y-1">
                      <div className="flex items-center gap-2 text-xs" style={{ color: rgb.gray }}>
                        <span
                          className="rounded-[9999px] px-2 py-0.5"
                          style={{ backgroundColor: "#f3f4f6" }}
                        >
                          {li.frequency}
                        </span>
                        <span className={cn("rounded-[9999px] px-2 py-0.5", statusPill(li.status))}>
                          {li.status}
                        </span>
                      </div>
                      {li.policyNumber && (
                        <p className="text-xs" style={{ color: "rgb(156, 163, 175)" }}>
                          #{li.policyNumber}
                        </p>
                      )}
                    </div>
                    <p className="text-xl font-bold" style={{ color: COLORS.orangeDark }}>
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
