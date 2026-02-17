import type { Project } from "@/lib/types";

export function ProjectsList({ projects }: { projects: Project[] }) {
  return (
    <ul style={{ display: "grid", gap: 12, padding: 0, listStyle: "none" }}>
      {projects.map((p) => (
        <li key={p.id} style={{ border: "1px solid #ddd", padding: 12 }}>
          <h3 style={{ margin: "0 0 6px" }}>{p.title}</h3>
          <p style={{ margin: "0 0 8px" }}>{p.summary}</p>
          <div style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
            {p.tags.map((t) => (
              <span key={t} style={{ border: "1px solid #eee", padding: "2px 6px" }}>
                {t}
              </span>
            ))}
          </div>
          <div style={{ marginTop: 10, display: "flex", gap: 12 }}>
            {p.url ? <a href={p.url} target="_blank" rel="noreferrer">Live</a> : null}
            {p.source ? <a href={p.source} target="_blank" rel="noreferrer">Source</a> : null}
          </div>
        </li>
      ))}
    </ul>
  );
}
