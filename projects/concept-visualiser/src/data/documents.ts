export interface Document {
  id: string;
  title: string;
  summary: string;
  tag: string;
  lastModified: string;
  previewColor: string;
  x: number;
  y: number;
}

export const documents: Document[] = [
  {
    id: "design-system",
    title: "Design System Guidelines",
    summary:
      "Comprehensive documentation covering component patterns, typography tokens, and accessibility standards across the product suite.",
    tag: "Design",
    lastModified: "14 Mar 2026",
    previewColor: "#6366f1",
    x: 180,
    y: 120,
  },
  {
    id: "api-spec",
    title: "API Integration Spec",
    summary:
      "Technical specification for third-party API integrations, including authentication flows, rate limiting, and error handling.",
    tag: "Engineering",
    lastModified: "11 Mar 2026",
    previewColor: "#22c55e",
    x: 500,
    y: 60,
  },
  {
    id: "roadmap",
    title: "Q1 Product Roadmap",
    summary:
      "Strategic overview of feature deliverables and milestones for Q1, aligned with OKRs and stakeholder commitments.",
    tag: "Product",
    lastModified: "18 Mar 2026",
    previewColor: "#f97316",
    x: 820,
    y: 180,
  },
  {
    id: "research",
    title: "User Research Synthesis",
    summary:
      "Aggregated findings from 12 user interviews exploring pain points in the onboarding experience and feature discoverability.",
    tag: "Research",
    lastModified: "7 Mar 2026",
    previewColor: "#a855f7",
    x: 140,
    y: 450,
  },
  {
    id: "a11y",
    title: "Accessibility Audit Report",
    summary:
      "WCAG 2.1 AA compliance audit covering contrast ratios, keyboard navigation, and screen reader compatibility for all core flows.",
    tag: "QA",
    lastModified: "3 Mar 2026",
    previewColor: "#ef4444",
    x: 480,
    y: 390,
  },
  {
    id: "wireframes",
    title: "Onboarding Flow Wireframes",
    summary:
      "Low-fidelity wireframes for the revised onboarding sequence, incorporating research insights and A/B test results.",
    tag: "Design",
    lastModified: "20 Mar 2026",
    previewColor: "#0ea5e9",
    x: 800,
    y: 490,
  },
];
