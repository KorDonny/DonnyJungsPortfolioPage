import { NextResponse } from "next/server";

export async function GET() {
  const base = process.env.API_BASE_URL;
  if (!base) return NextResponse.json({ error: "API_BASE_URL missing" }, { status: 500 });

  const r = await fetch(`${base}/api/v1/assets/resume/`, {
    cache: "no-store",
    redirect: "follow",
  });

  const text = await r.text();
  let data: any = null;
  try { data = JSON.parse(text); } catch {}

  if (!r.ok) {
    return NextResponse.json(
      { error: "Backend error", detail: data ?? text },
      { status: r.status }
    );
  }

  return NextResponse.json(data, { status: 200 });
}
