# Project Index Template
*Document type: Index | Owner: Orchestrator Agent | Tier: 1 — Always Loaded*
*Status: Draft | Last updated: 14 March 2026 | Version: 0.1*
*Linked agents: All*
*Linked documents: All domain documents*

---

## Purpose

This document is the spine of the agentic design system. It is the first document loaded into every agent's context on every task. It must remain concise — under 500 tokens of active content — with all detail living in linked Tier 2 domain documents.

The Project Index does four things:
1. Orients any agent or human to the current state of the project instantly
2. Acts as a registry of all domain documents, their owners, and their status
3. Defines the agent roster, their responsibilities, and their input/output contracts
4. Enforces structural consistency across all documents via the standard document header

---

## Standard Document Header

Every document in this system must open with this header block:

# [Document Title]
*Document type: [Index | Domain | Task Output] | Owner: [Agent Name] | Tier: [1 | 2 | 3]*
*Status: [Draft | Active | Needs Review | Archived] | Last updated: [Date] | Version: [n]*
*Linked agents: [agents that read this document]*
*Linked documents: [related documents by title]*

---

## Project Snapshot
*Maximum five lines. Updated by Orchestrator after every significant decision.*

- **Project:** Offer Management Platform — internal web app replacing spreadsheet/email offer lifecycle process
- **Org:** New Zealand telco
- **Stage:** Pre-launch MVP. DeviceOps designs built and UAT complete. Creative and Catalogue flows in progress.
- **Active phase:** Define → Design transition
- **Open decisions:** Offer type variability in editor UI. Figma design system migration to shadcn. AI integration scope at MVP.

---

## Agent Roster

| Agent | Phase | Owns | Reads |
|---|---|---|---|
| Orchestrator | All | project-index.md, decision-log.md, open-questions.md, conflict-register.md, phase-plan.md | All documents |
| Discover | Discover | assumption-register.md, stakeholder-map.md, process-map-current.md, user-journey-map.md, research-synthesis.md | project-index.md |
| Define | Define | personas.md, affinity-map.md, pain-point-matrix.md, problem-statements.md, success-metrics.md, experience-principles.md | project-index.md, research-synthesis.md |
| Design | Develop | wireframes.md, user-flows.md, component-library-reference.md, feasibility-notes.md, iteration-log.md, prototype-log.md | project-index.md, problem-statements.md, personas.md, component-library-reference.md |
| Deliver | Deliver | state-matrix.md, user-stories.md, acceptance-criteria.md, handoff-docs/, uat-plan.md, uat-findings.md, post-launch-log.md | project-index.md, wireframes.md, feasibility-notes.md, personas.md |

---

## Domain Document Registry

| Document | Owner | Tier | Status |
|---|---|---|---|
| `project-index.md` | Orchestrator | 1 | Draft |
| `phase-plan.md` | Orchestrator | 2 | Not started |
| `decision-log.md` | Orchestrator | 2 | Not started |
| `open-questions.md` | Orchestrator | 2 | Not started |
| `conflict-register.md` | Orchestrator | 2 | Not started |
| `assumption-register.md` | Discover | 2 | Not started |
| `stakeholder-map.md` | Discover | 2 | Not started |
| `process-map-current.md` | Discover | 2 | Not started |
| `user-journey-map.md` | Discover | 2 | Not started |
| `research-synthesis.md` | Discover | 2 | Not started |
| `personas.md` | Define | 2 | Not started |
| `affinity-map.md` | Define | 2 | Not started |
| `pain-point-matrix.md` | Define | 2 | Not started |
| `problem-statements.md` | Define | 2 | Not started |
| `success-metrics.md` | Define | 2 | Not started |
| `experience-principles.md` | Define | 2 | Not started |
| `information-architecture.md` | Design | 2 | Not started |
| `user-flows.md` | Design | 2 | Not started |
| `wireframes.md` | Design | 2 | Not started |
| `component-library-reference.md` | Design | 2 | Not started |
| `feasibility-notes.md` | Design | 2 | Not started |
| `iteration-log.md` | Design | 2 | Not started |
| `prototype-log.md` | Design | 2 | Not started |
| `state-matrix.md` | Deliver | 2 | Not started |
| `user-stories.md` | Deliver | 2 | Not started |
| `acceptance-criteria.md` | Deliver | 2 | Not started |
| `handoff-docs/` | Deliver | 2 | Not started |
| `uat-plan.md` | Deliver | 2 | Not started |
| `uat-findings.md` | Deliver | 2 | Not started |
| `post-launch-log.md` | Deliver | 2 | Not started |

---

*End of Project Index v0.1*
*Next update triggered by: first domain document created or first agent task completed*
