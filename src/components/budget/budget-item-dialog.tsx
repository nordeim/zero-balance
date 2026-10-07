"use client";

// Add/Edit Budget Item — the reference's two-column form: Type, Amount,
// Classification radios, Category, Subcategory, Frequency, Date, Payment
// Method, Status, Recurring switch, Notes. Creating opens with the modal's
// preset type; editing loads the item's values.

import * as React from "react";
import { CalendarIcon, CreditCardIcon, Loader2Icon, Trash2Icon } from "lucide-react";
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Switch } from "@/components/ui/switch";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { useToast } from "@/components/ui/toast";
import { messageOf, useBudgetStore, type ModalState } from "./store";
import { CLASSIFICATION_LABELS, CLASSIFICATION_TILES, rgb } from "@/lib/constants";
import type { BudgetItemFormData, Classification, Frequency, ItemStatus, ItemType } from "@/lib/types";

/** Derive the form state from the modal (create preset / edit hydration). */
function initialForm(modal: ModalState["item"]): BudgetItemFormData {
  if (modal?.mode === "edit") {
    const i = modal.item;
    return {
      type: i.type,
      classification: i.classification,
      amount: i.amount,
      category: i.category,
      subcategory: i.subcategory ?? "",
      paymentMethod: i.paymentMethod ?? "",
      frequency: i.frequency,
      date: i.date,
      recurring: i.recurring,
      status: i.status,
      notes: i.notes ?? "",
    };
  }
  return EMPTY_FORM(modal?.type ?? "expense");
}

function todayIso(): string {
  const d = new Date();
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

const EMPTY_FORM = (type: ItemType): BudgetItemFormData => ({
  type,
  classification: "need",
  amount: 0,
  category: "",
  subcategory: "",
  paymentMethod: "",
  frequency: "monthly",
  date: todayIso(),
  recurring: false,
  status: "active",
  notes: "",
});

export function BudgetItemDialog() {
  const modal = useBudgetStore((s) => s.modal.item);
  const closeModals = useBudgetStore((s) => s.closeModals);
  const createItem = useBudgetStore((s) => s.createItem);
  const updateItem = useBudgetStore((s) => s.updateItem);
  const deleteItem = useBudgetStore((s) => s.deleteItem);
  const { toast } = useToast();

  // The form derives from the modal AT MOUNT (the ModalHost only mounts
  // this dialog while a modal is open — every open is a fresh mount) and
  // re-derives if the modal identity ever changes in place (adjust-state-
  // during-render — no effect, no cascading render).
  const [form, setForm] = React.useState<BudgetItemFormData>(() => initialForm(modal));
  const [saving, setSaving] = React.useState(false);
  const [confirmingDelete, setConfirmingDelete] = React.useState(false);
  const editing = modal?.mode === "edit" ? modal.item : null;

  const modalKey = modal
    ? modal.mode === "edit"
      ? `edit:${modal.item.id}`
      : `create:${modal.type}`
    : null;
  const [resetKey, setResetKey] = React.useState(modalKey);
  if (resetKey !== modalKey) {
    setResetKey(modalKey);
    setForm(initialForm(modal));
  }

  if (!modal) return null;

  const set = <K extends keyof BudgetItemFormData>(key: K, value: BudgetItemFormData[K]) =>
    setForm((f) => ({ ...f, [key]: value }));

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (saving) return;
    if (!form.category.trim()) {
      toast({ title: "Category is required", variant: "error" });
      return;
    }
    setSaving(true);
    try {
      if (editing) {
        await updateItem(editing.id, form);
        toast({ title: "Budget item updated", variant: "success" });
      } else {
        await createItem(form);
        toast({ title: "Budget item added", variant: "success" });
      }
      closeModals();
    } catch (error) {
      toast({ title: "Could not save the item", description: messageOf(error), variant: "error" });
    } finally {
      setSaving(false);
    }
  };

  const onDelete = async () => {
    if (!editing) return;
    try {
      await deleteItem(editing.id);
      toast({ title: "Budget item deleted", variant: "success" });
      closeModals();
    } catch (error) {
      toast({ title: "Could not delete the item", description: messageOf(error), variant: "error" });
    }
  };

  return (
    <Dialog open onOpenChange={(open) => !open && closeModals()}>
      <DialogContent aria-describedby={undefined}>
        <DialogHeader>
          <DialogTitle>{editing ? "Edit Budget Item" : "Add Budget Item"}</DialogTitle>
        </DialogHeader>
        <form className="space-y-6 p-6" onSubmit={onSubmit}>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="item-type">Type</Label>
              <Select
                value={form.type}
                onValueChange={(v) => set("type", v as ItemType)}
                disabled={!!editing}
              >
                <SelectTrigger id="item-type" aria-label="Type">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="income">Income</SelectItem>
                  <SelectItem value="savings">Savings</SelectItem>
                  <SelectItem value="expense">Expense</SelectItem>
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label htmlFor="item-amount">Amount</Label>
              <Input
                id="item-amount"
                type="number"
                step="0.01"
                min="0"
                required
                placeholder="0.00"
                value={form.amount === 0 ? "" : form.amount}
                onChange={(e) => set("amount", Number(e.target.value))}
              />
            </div>
          </div>

          <div className="space-y-2">
            <Label>Classification</Label>
            {/* Reference tiles (live DOM): flex gap-4 row of flex-1 p-4
                border-2 tiles; the SELECTED tile carries its own accent
                border + tint bg (inline), unselected tiles keep the default
                border so the per-tile hover:border-*-300 still applies. */}
            <RadioGroup
              value={form.classification}
              onValueChange={(v) => set("classification", v as Classification)}
              className="flex gap-4"
            >
              {(["need", "want", "savings"] as const).map((c) => {
                const tile = CLASSIFICATION_TILES[c];
                const selected = form.classification === c;
                return (
                  <Label
                    key={c}
                    className={`flex flex-1 cursor-pointer items-center space-x-2 rounded-lg border-2 bg-white p-4 transition-all ${tile.hoverBorder}`}
                    style={
                      selected
                        ? { borderColor: tile.accent, backgroundColor: tile.tint }
                        : undefined
                    }
                  >
                    <RadioGroupItem value={c} />
                    <span className="text-sm font-medium">{CLASSIFICATION_LABELS[c]}</span>
                  </Label>
                );
              })}
            </RadioGroup>
          </div>

          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="item-category">Category</Label>
              <Input
                id="item-category"
                required
                placeholder="e.g., Salary, Emergency Fund, Rent"
                value={form.category}
                onChange={(e) => set("category", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="item-subcategory">Subcategory</Label>
              <Input
                id="item-subcategory"
                placeholder="e.g., Main Job, Home Savings"
                value={form.subcategory}
                onChange={(e) => set("subcategory", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="item-frequency">Frequency</Label>
              <Select
                value={form.frequency}
                onValueChange={(v) => set("frequency", v as Frequency)}
              >
                <SelectTrigger id="item-frequency" aria-label="Frequency">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="one-time">One-time</SelectItem>
                  <SelectItem value="weekly">Weekly</SelectItem>
                  <SelectItem value="bi-weekly">Bi-weekly</SelectItem>
                  <SelectItem value="monthly">Monthly</SelectItem>
                  <SelectItem value="quarterly">Quarterly</SelectItem>
                  <SelectItem value="annually">Annually</SelectItem>
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label htmlFor="item-date">Date</Label>
              <Input
                id="item-date"
                type="date"
                required
                value={form.date}
                onChange={(e) => set("date", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="item-payment">Payment Method</Label>
              <Input
                id="item-payment"
                placeholder="e.g., Bank Account, Credit Card"
                value={form.paymentMethod}
                onChange={(e) => set("paymentMethod", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="item-status">Status</Label>
              <Select value={form.status} onValueChange={(v) => set("status", v as ItemStatus)}>
                <SelectTrigger id="item-status" aria-label="Status">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="planned">Planned</SelectItem>
                  <SelectItem value="active">Active</SelectItem>
                  <SelectItem value="completed">Completed</SelectItem>
                </SelectContent>
              </Select>
            </div>
          </div>

          <div className="flex items-center justify-between rounded-lg border p-4" style={{ borderColor: rgb.border }}>
            <div className="flex items-center gap-3">
              <CalendarIcon className="h-5 w-5" style={{ color: rgb.gray }} />
              <div>
                <Label htmlFor="item-recurring" className="cursor-pointer">
                  Recurring Item
                </Label>
                <p className="text-xs" style={{ color: rgb.gray }}>
                  This item repeats based on the frequency
                </p>
              </div>
            </div>
            <Switch
              id="item-recurring"
              checked={form.recurring}
              onCheckedChange={(v) => set("recurring", v)}
            />
          </div>

          <div className="space-y-2">
            <Label htmlFor="item-notes">Notes</Label>
            <Textarea
              id="item-notes"
              placeholder="Additional details..."
              rows={3}
              value={form.notes}
              onChange={(e) => set("notes", e.target.value)}
            />
          </div>

          {/* Superset affordance: the reference has NO delete on expense
              cards (only income/savings carry the ellipsis menu), so the
              edit dialog gains a delete path — visible in edit mode only,
              keeping the card chrome identical to the reference. */}
          {editing && confirmingDelete ? (
            <div
              className="flex items-center justify-between rounded-lg p-3"
              style={{ backgroundColor: "rgb(254, 242, 242)" }}
            >
              <p className="text-sm text-red-700">Delete this item?</p>
              <div className="flex gap-2">
                <button
                  type="button"
                  className="rounded-md bg-white px-3 py-1 text-xs font-medium text-slate-700 shadow-sm"
                  onClick={() => setConfirmingDelete(false)}
                >
                  Cancel
                </button>
                <button
                  type="button"
                  className="rounded-md bg-red-600 px-3 py-1 text-xs font-medium text-white"
                  onClick={() => void onDelete()}
                >
                  Delete
                </button>
              </div>
            </div>
          ) : (
            <div className="flex items-center justify-end gap-3">
              {editing && (
                <button
                  type="button"
                  className="mr-auto inline-flex items-center gap-2 rounded-lg px-3 py-2 text-sm font-medium text-red-600 transition-colors hover:bg-red-50"
                  onClick={() => setConfirmingDelete(true)}
                >
                  <Trash2Icon className="h-4 w-4" />
                  Delete
                </button>
              )}
              <button
                type="button"
                className="rounded-lg px-4 py-2 text-sm font-medium transition-colors hover:bg-accent"
                style={{ color: rgb.gray }}
                onClick={closeModals}
              >
                Cancel
              </button>
              <button type="submit" className="zb-btn-primary" disabled={saving}>
                {saving && <Loader2Icon className="h-4 w-4 animate-spin" />}
                Save Item
              </button>
            </div>
          )}
        </form>
      </DialogContent>
    </Dialog>
  );
}
