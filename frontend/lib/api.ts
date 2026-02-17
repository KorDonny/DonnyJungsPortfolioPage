import type { ProjectsResponse } from "./types";

export async function fetchProjects(): Promise<ProjectsResponse> {
  const r = await fetch("/api/projects", { cache: "no-store" });
  const data = (await r.json().catch(() => null)) as ProjectsResponse | null;

  if (!r.ok || !data) {
    throw new Error(JSON.stringify(data ?? { error: "Failed to fetch projects" }));
  }
  return data;
}
