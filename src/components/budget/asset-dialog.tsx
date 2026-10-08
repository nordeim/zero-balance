"use client";

// Add/Edit Asset — Asset Type, Current Value, Name, Institution,
// Account/Reference Number, Last Updated, Notes.

import * as React from "react";
import { Loader2Icon, SaveIcon } from "lucide-react";
import { Dialog, DialogCloseButton, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";
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
import { ADD_BUTTON_GRADIENTS, ASSET_LABELS } from "@/lib/constants";
import type { AssetFormData, AssetType } from "@/lib/types";

function todayIso(): string {
  const d = new Date();
  const pad = (n: number) => String(n).padStart(2, "0");
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

const EMPTY: AssetFormData = {
  type: "bank_account",
  name: "",
  institution: "",
  accountNumber: "",
  value: 0,
  lastUpdated: todayIso(),
  notes: "",
};

/** Derive the form state from the modal (create defaults / edit hydration). */
function initialForm(modal: ModalState["asset"]): AssetFormData {
  if (modal?.mode === "edit") {
    const a = modal.asset;
    return {
      type: a.type,
      name: a.name,
      institution: a.institution ?? "",
      accountNumber: a.accountNumber ?? "",
      value: a.value,
      lastUpdated: a.lastUpdated,
      notes: a.notes ?? "",
    };
  }
  return EMPTY;
}

export function AssetDialog() {
  const modal = useBudgetStore((s) => s.modal.asset);
  const closeModals = useBudgetStore((s) => s.closeModals);
  const createAsset = useBudgetStore((s) => s.createAsset);
  const updateAsset = useBudgetStore((s) => s.updateAsset);
  const { toast } = useToast();

  // Form derives from the modal AT MOUNT (the ModalHost only mounts this
  // dialog while a modal is open) and re-derives if the modal identity ever
  // changes in place (adjust-during-render — no effect, no cascading render).
  const [form, setForm] = React.useState<AssetFormData>(() => initialForm(modal));
  const [saving, setSaving] = React.useState(false);
  const editing = modal?.mode === "edit" ? modal.asset : null;

  const modalKey = modal
    ? modal.mode === "edit"
      ? `edit:${modal.asset.id}`
      : "create"
    : null;
  const [resetKey, setResetKey] = React.useState(modalKey);
  if (resetKey !== modalKey) {
    setResetKey(modalKey);
    setForm(initialForm(modal));
  }

  if (!modal) return null;

  const set = <K extends keyof AssetFormData>(key: K, value: AssetFormData[K]) =>
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
      if (editing) {
        await updateAsset(editing.id, form);
        toast({ title: "Asset updated", variant: "success" });
      } else {
        await createAsset(form);
        toast({ title: "Asset added", variant: "success" });
      }
      closeModals();
    } catch (error) {
      toast({ title: "Could not save the asset", description: messageOf(error), variant: "error" });
    } finally {
      setSaving(false);
    }
  };

  return (
    <Dialog open onOpenChange={(open) => !open && closeModals()}>
      <DialogContent aria-describedby={undefined}>
        <DialogHeader>
          <DialogTitle>{editing ? "Edit Asset" : "Add Asset"}</DialogTitle>
          <DialogCloseButton />
        </DialogHeader>
        <form className="space-y-6 p-6" onSubmit={onSubmit}>
          <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
            <div className="space-y-2">
              <Label htmlFor="asset-type">Asset Type</Label>
              {/* The reference disables the type select while EDITING an
                  asset (enabled on create) — v6 G5. */}
              <Select value={form.type} onValueChange={(v) => set("type", v as AssetType)} disabled={!!editing}>
                <SelectTrigger id="asset-type" aria-label="Asset Type">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent>
                  {(Object.keys(ASSET_LABELS) as AssetType[]).map((t) => (
                    <SelectItem key={t} value={t}>
                      {ASSET_LABELS[t]}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>
            <div className="space-y-2">
              <Label htmlFor="asset-value">Current Value</Label>
              <Input
                id="asset-value"
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
                (md:col-span-2 → 624px) — v6 G4. */}
            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="asset-name">Name</Label>
              <Input
                id="asset-name"
                required
                placeholder="e.g., Commonwealth Savings Account"
                value={form.name}
                onChange={(e) => set("name", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="asset-institution">Institution</Label>
              <Input
                id="asset-institution"
                placeholder="e.g., Commonwealth Bank"
                value={form.institution}
                onChange={(e) => set("institution", e.target.value)}
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="asset-account">Account/Reference Number</Label>
              <Input
                id="asset-account"
                placeholder="Optional"
                value={form.accountNumber}
                onChange={(e) => set("accountNumber", e.target.value)}
              />
            </div>
            <div className="space-y-2 md:col-span-2">
              <Label htmlFor="asset-date">Last Updated</Label>
              <Input
                id="asset-date"
                type="date"
                required
                value={form.lastUpdated}
                onChange={(e) => set("lastUpdated", e.target.value)}
              />
            </div>
          </div>
          <div className="space-y-2">
            <Label htmlFor="asset-notes">Notes</Label>
            <Textarea
              id="asset-notes"
              placeholder="Additional details..."
              rows={3}
              value={form.notes}
              onChange={(e) => set("notes", e.target.value)}
            />
          </div>
          {/* Reference footer (plan v8 G1): flex gap-3 pt-4 with both buttons
              at flex-1 (Cancel ≈ 307px + Save Asset ≈ 305px). */}
          <div className="flex gap-3 pt-4">
            <Button type="button" variant="outline" className="flex-1" onClick={closeModals}>
              Cancel
            </Button>
            <button
              type="submit"
              className="zb-btn-add flex-1"
              style={{ background: ADD_BUTTON_GRADIENTS.asset }}
              disabled={saving}
            >
              {saving ? (
                <Loader2Icon className="h-4 w-4 animate-spin" />
              ) : (
                <SaveIcon className="h-4 w-4" />
              )}
              Save Asset
            </button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  );
}
