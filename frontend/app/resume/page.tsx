"use client";
import { useEffect, useState } from "react";

export default function ResumePage() {
  const [url, setUrl] = useState<string>("");
  const [err, setErr] = useState<string>("");

  useEffect(() => {
    fetch("https://api.donnyjungsweb.dedyn.io/api/v1/assets/resume")
      .then(async (r) => {
        const t = await r.text();
        if (!r.ok) throw new Error(t);
        return JSON.parse(t);
      })
      .then((j) => setUrl(j.url))
      .catch((e) => setErr(String(e?.message ?? e)));
  }, []);

  if (err) return <pre style={{ padding: 24 }}>{err}</pre>;
  if (!url) return <div style={{ padding: 24 }}>Loading...</div>;

  return (
    <main style={{ padding: 24 }}>
      <h1>Resume</h1>
      <p><a href={url} target="_blank" rel="noreferrer">Open in new tab</a></p>
      <iframe src={url} style={{ width: "100%", height: "80vh", border: "1px solid #ddd" }} />
    </main>
  );
}
