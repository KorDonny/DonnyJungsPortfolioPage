import { NextResponse } from "next/server";

export async function GET() {
  const base = process.env.API_BASE_URL;
  if (!base) return NextResponse.json({ error: "API_BASE_URL missing" }, { status: 500 });

  const r = await fetch(`${base}/api/v1/projects`, { cache: "no-store" });
  const data = await r.json().catch(() => null);

  if (!r.ok) {
    return NextResponse.json(
      { error: "Backend error", detail: data ?? (await r.text()) },
      { status: r.status }
    );
  }

  return NextResponse.json(data, { status: 200 });
}
