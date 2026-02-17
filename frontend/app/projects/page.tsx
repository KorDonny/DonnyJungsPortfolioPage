// export default async function ProjectsPage() {
//   const r = await fetch(`${process.env.NEXT_PUBLIC_SITE_URL ?? ""}/api/projects`, {
//     cache: "no-store",
//   });

//   const data = await r.json().catch(() => null);

//   if (!r.ok) {
//     return (
//       <main style={{ padding: 24 }}>
//         <h1>Projects</h1>
//         <pre>{JSON.stringify(data, null, 2)}</pre>
//       </main>
//     );
//   }

//   return (
//     <main style={{ padding: 24 }}>
//       <h1>Projects</h1>
//       <pre>{JSON.stringify(data, null, 2)}</pre>
//     </main>
//   );
// }


"use client";

import { useEffect, useState } from "react";
import type { ProjectsResponse } from "@/lib/types";
import { ProjectsList } from "@/components/ProjectsList";

export default function ProjectsPage() {
  const [data, setData] = useState<ProjectsResponse | null>(null);
  const [err, setErr] = useState<string>("");

  useEffect(() => {
    fetch("/api/projects", { cache: "no-store" })
      .then(async (r) => {
        const j = (await r.json().catch(() => null)) as ProjectsResponse | null;
        if (!r.ok || !j) throw new Error(JSON.stringify(j ?? { error: "fetch failed" }));
        return j;
      })
      .then(setData)
      .catch((e) => setErr(String(e?.message ?? e)));
  }, []);

  if (err) return <pre style={{ padding: 24 }}>{err}</pre>;
  if (!data) return <div style={{ padding: 24 }}>Loading...</div>;

  return (
    <main style={{ padding: 24 }}>
      <h1>Projects</h1>
      <ProjectsList projects={data.projects} />
    </main>
  );
}
