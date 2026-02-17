// frontend/app/api/assets/bg/route.ts
import { NextResponse } from "next/server";

export async function GET() {
    const base = process.env.API_BASE_URL;
    const r = await fetch(
        `${base}/api/v1/assets/bg/`,
    { cache: "no-store" }
  );

  const text = await r.text();
  return new NextResponse(text, {
    status: r.status,
    headers: { "content-type": r.headers.get("content-type") ?? "application/json" },
  });
}
