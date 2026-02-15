// frontend/app/items/page.tsx
"use client";

import { useEffect, useState } from "react";

export default function ItemsPage() {
  const [data, setData] = useState<any>(null);
  const [err, setErr] = useState<string | null>(null);

  useEffect(() => {
    fetch("/items")
      .then(async (r) => {
        const t = await r.text();
        if (!r.ok) throw new Error(t);
        return JSON.parse(t);
      })
      .then(setData)
      .catch((e) => setErr(String(e.message ?? e)));
  }, []);

  return (
    <main style={{ padding: 24 }}>
      <h1>Projects</h1>
      {err && <pre>{err}</pre>}
      <pre>{data ? JSON.stringify(data, null, 2) : "loading..."}</pre>
    </main>
  );
}
