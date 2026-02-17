import { NextResponse } from "next/server";

export async function GET() {
  const base = process.env.API_BASE_URL;
  if (!base) {
    return NextResponse.json({ error: "API_BASE_URL missing" }, { status: 500 });
  }

  const r = await fetch(`${base}/api/v1/assets/resume`, { cache: "no-store" });

  // 백엔드가 JSON 주는 게 정상이라 json 우선
  const data = await r.json().catch(() => null);

  if (!r.ok) {
    return NextResponse.json(
      { error: "Backend error", detail: data ?? (await r.text()) },
      { status: r.status }
    );
  }

  return NextResponse.json(data, { status: 200 });
}
