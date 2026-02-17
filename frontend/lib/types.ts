export type Project = {
  id: number;
  title: string;
  summary: string;
  tags: string[];
  url?: string;
  source?: string;
};

export type ProjectsResponse = {
  projects: Project[];
};
