import path from "node:path";
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  output: "standalone",
  // Pin file tracing to this project so the standalone server always lands
  // at .next/standalone/server.js — even when the repo is cloned inside a
  // parent workspace that has its own lockfile.
  outputFileTracingRoot: path.join(import.meta.dirname, "."),
  // Next 16's dev-origin protection silently blocks dev chunks when the app
  // is reached via 127.0.0.1 instead of localhost (unhydrated page, native
  // form GET fallbacks) — allow both origins (trap log, session 12c).
  allowedDevOrigins: ["127.0.0.1", "localhost"],
  reactStrictMode: false,
};

export default nextConfig;
