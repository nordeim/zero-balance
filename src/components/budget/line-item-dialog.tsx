"use client";

// Add/Edit Line Item — the calculator's nested form: Item Name, Amount,
// Frequency, Provider, Policy Number, Start/Renewal Date, End Date, Notes.

import * as React from "react";
import { Loader2Icon } from "lucide-react";
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { useToast } from "@/components/ui/toast";
import { messageOf, useBudgetStore, type ModalState } from "./store";
import { rgb } from "@/lib/constants";
import type { Frequency, ItemStatus, LineItemFormData } from "@/lib/types";

const EMPTY: LineItemFormData = {
  name: "",
  amount: 0,
  frequency: "monthly",
  provider: "",
  policyNumber: "",
  paymentMethod: "",
  startDate: "",
  endDate: "",
  status: "active",
  notes: "",
};

/** Derive the form state from the modal (create defaults / edit hydration). */
function initialForm(modal: ModalState["lineItem"]): LineItemFormData {
  if (modal?.mode === "edit") {
    const li = modal.lineItem;
    return {
      name: li.name,
      amount: li.amount,
      frequency: li.frequency,
      provider: li.provider ?? "",
      policyNumber: li.policyNumber ?? "",
      paymentMethod: li.paymentMethod ?? "",
      startDate: li.startDate ?? "",
      endDate: li.endDate ?? "",
      status: li.status,
      notes: li.notes ?? "",
    };
  }
  return EMPTY;
}

export function LineItemDialog() {
  const modal = useBudgetStore((s) => s.modal.lineItem);
  const closeLineItemModal = useBudgetStore((s) => s.closeLineItemModal);
  const createLineItem = useBudgetStore((s) => s.createLineItem);
  const updateLineItem = useBudgetStore((s) => s.updateLineItem);
  const { toast } = useToast();

  // Form derives from the modal AT MOUNT (the ModalHost only mounts this
  // dialog while a modal is open) and re-derives if the modal identity ever
  // changes in place (adjust-during-render — no effect, no cascading render).
  const [form, setForm] = React.useState<LineItemFormData>(() => initialForm(modal));
  const [saving, setSaving] = React.useState(false);
  const editing = modal?.mode === "edit" ? modal.lineItem : null;

  const modalKey = modal
    ? modal.mode === "edit"
      ? `edit:${modal.lineItem.id}`
      : "create"
    : null;
  const [resetKey, setResetKey] = React.useState(modalKey);
  if (resetKey !== modalKey) {
    setResetKey(modalKey);
    setForm(initialForm(modal));
  }

  if (!modal) return null;

  const set = <K extends keyof LineItemFormData>(key: K, value: LineItemFormData[K]) =>
    setForm((f) => ({ ...f, [key]: value }));

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (saving) return;
    if (!form.name.trim()) {
      toast({ title: "Item name is required", variant: "error" });
      return;
    }
    setSaving(true);
    try {
      if (editing) {
        await updateLineItem(editing.id, form);
        toast({ title: "Line item updated", variant: "success" });
      } else {
        await createLineItem({ ...form, budgetItemId: (modal as { mode: "create"; budgetItemId: string }).budgetItemId });
        toast({ title: "Line item added", variant: "success" });
      }
      closeLineItemModal();
    } catch (error) {
      toast({ title: "Could not save the line item", description: messageOf(error), variant: "error" });
    } finally {
      setSaving(false);
    }
  };

  return (
    <Dialog open onOpenChange={(open) => !open && closeLineItemModal()}>
      <DialogContent aria-describedby={undefined}>
        <DialogHeader>
          <DialogTitle>{editing ? "Edit Line Item" : "Add Line Item"}</DialogTitle>
        </DialogHeader>
        <form className="space-y-6 p-6" onSubmit={onSubmit}>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="line-name">Item Name *</Label>
              <Input
                id="line-name"
                required
                placeholder="e.g., Car Insurance Policy, Health Insurance"
                value={form.name}
                onChange={(e) => set("name", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="line-amount">Amount *</Label>
              <Input
                id="line-amount"
                type="number"
                step="0.01"
                min="0"
                required
                placeholder="0.00"
                value={form.amount === 0 ? "" : form.amount}
                onChange={(e) => set("amount", Number(e.target.value))}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="line-frequency">Frequency</Label>
              <Select value={form.frequency} onValueChange={(v) => set("frequency", v as Frequency)}>
                <SelectTrigger id="line-frequency" aria-label="Frequency">
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
              <Label htmlFor="line-provider">Provider / Company</Label>
              <Input
                id="line-provider"
                placeholder="e.g., Insurance Company Name"
                value={form.provider}
                onChange={(e) => set("provider", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="line-policy">Policy / Account Number</Label>
              <Input
                id="line-policy"
                placeholder="e.g., POL-123456"
                value={form.policyNumber}
                onChange={(e) => set("policyNumber", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="line-status">Status</Label>
              <Select value={form.status} onValueChange={(v) => set("status", v as ItemStatus)}>
                <SelectTrigger id="line-status" aria-label="Status">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="planned">Planned</SelectItem>
                  <SelectItem value="active">Active</SelectItem>
                  <SelectItem value="completed">Completed</SelectItem>
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label htmlFor="line-start">Start / Renewal Date</Label>
              <Input
                id="line-start"
                type="date"
                value={form.startDate}
                onChange={(e) => set("startDate", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="line-end">End Date</Label>
              <Input
                id="line-end"
                type="date"
                value={form.endDate}
                onChange={(e) => set("endDate", e.target.value)}
              />
            </div>
          </div>
          <div className="space-y-2">
            <Label htmlFor="line-notes">Notes</Label>
            <Textarea
              id="line-notes"
              placeholder="Additional details..."
              rows={3}
              value={form.notes}
              onChange={(e) => set("notes", e.target.value)}
            />
          </div>
          <div className="flex items-center justify-end gap-3">
            <button
              type="button"
              className="rounded-lg px-4 py-2 text-sm font-medium transition-colors hover:bg-accent"
              style={{ color: rgb.gray }}
              onClick={closeLineItemModal}
            >
              Cancel
            </button>
            <button type="submit" className="zb-btn-primary" disabled={saving}>
              {saving && <Loader2Icon className="h-4 w-4 animate-spin" />}
              Save Item
            </button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}
