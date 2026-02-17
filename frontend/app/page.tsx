"use client";

import { useEffect, useState } from "react";

type BgResponse = { url: string };

export default function Home() {
  const [bgUrl, setBgUrl] = useState<string>("");
  const [err, setErr] = useState<string>("");

  useEffect(() => {
    fetch("/api/assets/bg/", { cache: "no-store" })
      .then(async (r) => {
        const j = (await r.json().catch(() => null)) as BgResponse | null;
        if (!r.ok || !j?.url) throw new Error(JSON.stringify(j ?? { error: "fetch failed" }));
        return j;
      })
      .then((j) => setBgUrl(j.url))
      .catch((e) => setErr(String(e?.message ?? e)));
  }, []);

  if (err) return <pre style={{ padding: 24 }}>{err}</pre>;

  return (
    <div
      className="min-h-screen bg-center bg-no-repeat bg-cover"
      style={{
              backgroundImage: bgUrl ? `url(${bgUrl})` : "none",
              backgroundSize: "contain",
              backgroundColor: "black",
          }}
    >
      {/* 필요하면 오버레이/컨텐츠 */}
      {/* <div className="min-h-screen bg-black/20" /> */}
    </div>
  );
}
