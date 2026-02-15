// frontend/app/items/route.ts
import { NextResponse } from "next/server";

export async function GET() {
  const base = process.env.NEXT_PUBLIC_API_BASE_URL;
  if (!base) {
    return NextResponse.json({ error: "NEXT_PUBLIC_API_BASE_URL is missing" }, { status: 500 });
  }

  const r = await fetch(`${base}/api/v1/projects`, {
    headers: { "Content-Type": "application/json" },
    cache: "no-store",
  });

  const text = await r.text(); // 에러도 그대로 보기 좋게
  return new NextResponse(text, {
    status: r.status,
    headers: { "Content-Type": r.headers.get("content-type") ?? "application/json" },
  });
}
