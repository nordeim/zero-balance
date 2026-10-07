"use client";

import { Suspense } from "react";
import { LoginCard } from "@/components/budget/login-card";

// The auth card renders for EVERY visitor — authenticated ones included
// (reference behavior; signing in from that state lands on the workspace).
export default function LoginPage() {
  return (
    <Suspense>
      <LoginCard />
    </Suspense>
  );
}
