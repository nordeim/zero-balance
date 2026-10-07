"use client";

// Add/Edit Liability — Liability Type, Outstanding Balance, Name,
// Institution, Account/Loan Number, Interest Rate, Monthly Payment,
// Last Updated, Notes.

import * as React from "react";
import { Loader2Icon, SaveIcon } from "lucide-react";
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
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
import { ADD_BUTTON_GRADIENTS, LIABILITY_LABELS } from "@/lib/constants";
import type { LiabilityFormData, LiabilityType } from "@/lib/types";

function todayIso(): string {
  const d = new Date();
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

const EMPTY: LiabilityFormData = {
  type: "credit_card",
  name: "",
  institution: "",
  accountNumber: "",
  value: 0,
  interestRate: "",
  monthlyPayment: "",
  lastUpdated: todayIso(),
  notes: "",
};

/** Derive the form state from the modal (create defaults / edit hydration). */
function initialForm(modal: ModalState["liability"]): LiabilityFormData {
  if (modal?.mode === "edit") {
    const l = modal.liability;
    return {
      type: l.type,
      name: l.name,
      institution: l.institution ?? "",
      accountNumber: l.accountNumber ?? "",
      value: l.value,
      interestRate:
        l.interestRate !== null && l.interestRate !== undefined ? String(l.interestRate) : "",
      monthlyPayment:
        l.monthlyPayment !== null && l.monthlyPayment !== undefined ? String(l.monthlyPayment) : "",
      lastUpdated: l.lastUpdated,
      notes: l.notes ?? "",
    };
  }
  return EMPTY;
}

export function LiabilityDialog() {
  const modal = useBudgetStore((s) => s.modal.liability);
  const closeModals = useBudgetStore((s) => s.closeModals);
  const createLiability = useBudgetStore((s) => s.createLiability);
  const updateLiability = useBudgetStore((s) => s.updateLiability);
  const { toast } = useToast();

  // Form derives from the modal AT MOUNT (the ModalHost only mounts this
  // dialog while a modal is open) and re-derives if the modal identity ever
  // changes in place (adjust-during-render — no effect, no cascading render).
  const [form, setForm] = React.useState<LiabilityFormData>(() => initialForm(modal));
  const [saving, setSaving] = React.useState(false);
  const editing = modal?.mode === "edit" ? modal.liability : null;

  const modalKey = modal
    ? modal.mode === "edit"
      ? `edit:${modal.liability.id}`
      : "create"
    : null;
  const [resetKey, setResetKey] = React.useState(modalKey);
  if (resetKey !== modalKey) {
    setResetKey(modalKey);
    setForm(initialForm(modal));
  }

  if (!modal) return null;

  const set = <K extends keyof LiabilityFormData>(key: K, value: LiabilityFormData[K]) =>
    setForm((f) => ({ ...f, [key]: value }));

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (saving) return;
    if (!form.name.trim()) {
      toast({ title: "Name is required", variant: "error" });
      return;
    }
    setSaving(true);
    try {
      const payload: Omit<LiabilityFormData, "interestRate" | "monthlyPayment"> & {
        interestRate: number | null;
        monthlyPayment: number | null;
      } = {
        ...form,
        interestRate: form.interestRate.trim() === "" ? null : Number(form.interestRate),
        monthlyPayment: form.monthlyPayment.trim() === "" ? null : Number(form.monthlyPayment),
      };
      if (editing) {
        await updateLiability(editing.id, payload);
        toast({ title: "Liability updated", variant: "success" });
      } else {
        await createLiability(payload);
        toast({ title: "Liability added", variant: "success" });
      }
      closeModals();
    } catch (error) {
      toast({ title: "Could not save the liability", description: messageOf(error), variant: "error" });
    } finally {
      setSaving(false);
    }
  };

  return (
    <Dialog open onOpenChange={(open) => !open && closeModals()}>
      <DialogContent aria-describedby={undefined}>
        <DialogHeader>
          <DialogTitle>{editing ? "Edit Liability" : "Add Liability"}</DialogTitle>
        </DialogHeader>
        <form className="space-y-6 p-6" onSubmit={onSubmit}>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="liability-type">Liability Type</Label>
              {/* The reference disables the type select while EDITING
                  (asset-dialog pattern — v6 G5). */}
              <Select value={form.type} onValueChange={(v) => set("type", v as LiabilityType)} disabled={!!editing}>
                <SelectTrigger id="liability-type" aria-label="Liability Type">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  {(Object.keys(LIABILITY_LABELS) as LiabilityType[]).map((t) => (
                    <SelectItem key={t} value={t}>
                      {LIABILITY_LABELS[t]}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label htmlFor="liability-value">Outstanding Balance</Label>
              <Input
                id="liability-value"
                type="number"
                step="0.01"
                min="0"
                required
                placeholder="0.00"
                value={form.value === 0 ? "" : form.value}
                onChange={(e) => set("value", Number(e.target.value))}
              />
            </div>
            {/* Name + Last Updated span the full 2-col row on the reference
                (md:col-span-2 → 624px, measured on its Add Liability
                dialog) — v6 G4. */}
            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="liability-name">Name</Label>
              <Input
                id="liability-name"
                required
                placeholder="e.g., NAB Home Loan"
                value={form.name}
                onChange={(e) => set("name", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="liability-institution">Institution</Label>
              <Input
                id="liability-institution"
                placeholder="e.g., NAB"
                value={form.institution}
                onChange={(e) => set("institution", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="liability-account">Account/Loan Number</Label>
              <Input
                id="liability-account"
                placeholder="Optional"
                value={form.accountNumber}
                onChange={(e) => set("accountNumber", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="liability-rate">Interest Rate (%)</Label>
              <Input
                id="liability-rate"
                type="number"
                step="0.01"
                min="0"
                max="100"
                placeholder="e.g., 5.5"
                value={form.interestRate}
                onChange={(e) => set("interestRate", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="liability-monthly">Monthly Payment</Label>
              <Input
                id="liability-monthly"
                type="number"
                step="0.01"
                min="0"
                placeholder="0.00"
                value={form.monthlyPayment}
                onChange={(e) => set("monthlyPayment", e.target.value)}
              />
            </div>
            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="liability-date">Last Updated</Label>
              <Input
                id="liability-date"
                type="date"
                required
                value={form.lastUpdated}
                onChange={(e) => set("lastUpdated", e.target.value)}
              />
            </div>
          </div>
          <div className="space-y-2">
            <Label htmlFor="liability-notes">Notes</Label>
            <Textarea
              id="liability-notes"
              placeholder="Additional details..."
              rows={3}
              value={form.notes}
              onChange={(e) => set("notes", e.target.value)}
            />
          </div>
          {/* Reference footer (plan v8 G1): flex gap-3 pt-4 with both buttons
              at flex-1 (Cancel ≈ 307px + Save Liability ≈ 305px). */}
          <div className="flex gap-3 pt-4">
            <Button type="button" variant="outline" className="flex-1" onClick={closeModals}>
              Cancel
            </Button>
            <button
              type="submit"
              className="zb-btn-add flex-1"
              style={{ background: ADD_BUTTON_GRADIENTS.liability }}
              disabled={saving}
            >
              {saving ? (
                <Loader2Icon className="h-4 w-4 animate-spin" />
              ) : (
                <SaveIcon className="h-4 w-4" />
              )}
              Save Liability
            </button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}
