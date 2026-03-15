# Agentic Product Design System

## Overview

The Agentic Product Design System is a structured framework for managing product design projects using AI-augmented workflows. It organizes knowledge into a tiered memory architecture, with specialized agents handling different phases of the design process. This system ensures scalability, clear ownership, and efficient collaboration between human designers and AI agents.

## Key Features

- **Tiered Memory Architecture**: Documents are organized into tiers based on their purpose and lifecycle.
- **Agent-Based Ownership**: Each document is owned by a specific agent, ensuring clear responsibilities.
- **Standard Document Format**: All documents follow a consistent header structure for easy parsing and navigation.
- **Scalable Structure**: Designed to grow with the project without becoming cluttered.

## Folder Structure

- **`foundation/`**: Core system documents, templates, and shared references.
  - `context.md`: Project background, user goals, and system design.
  - `project-index-template.md`: Template for creating new project indices.
  - `component-library-reference.md` (when created): Shared vocabulary for UI components.

- **`tier-1-active/`**: Always-loaded documents essential for every agent task.
  - `project-index.md`: The spine of the system, containing project snapshot, agent roster, and document registry.

- **`tier-2-domain/`**: Domain-specific documents organized by agent ownership.
  - `orchestrator/`: Orchestration documents (phase plans, decision logs, etc.).
  - `discover/`: Research and discovery documents (stakeholder maps, user journeys, etc.).
  - `define/`: Problem definition documents (personas, problem statements, etc.).
  - `design/`: Design artifacts (wireframes, user flows, component references, etc.).
  - `deliver/`: Delivery and handoff documents (user stories, UAT plans, etc.).

- **`tier-3-work/`**: Ephemeral task outputs and working files.
  - `current-sprint/`: Temporary documents for ongoing work (may be chat-only or persisted).
  - `planning.md`: Moved here as it's work-in-progress.

- **`archive/`**: Historical documents and completed phases.
  - Subfolders like `phase-0/`, `phase-1/` for organizing old content.

## Agents

| Agent | Phase | Responsibility |
|---|---|---|
| **Orchestrator** | All | Oversees the entire process, maintains project index, manages decisions and conflicts. |
| **Discover** | Discover | Conducts research, maps stakeholders, analyzes current processes. |
| **Define** | Define | Defines problems, creates personas, sets success metrics. |
| **Design** | Develop | Creates wireframes, user flows, feasibility notes, iterations. |
| **Deliver** | Deliver | Writes user stories, plans UAT, handles post-launch logging. |

## Document Lifecycle

- **Tier 1**: Evolving in place, updated after significant decisions.
- **Tier 2**: Created as placeholders, populated as needed, may be versioned or archived.
- **Tier 3**: Created during tasks, discarded or moved to archive after completion.

## How to Use

1. **Initialization**: Use the `project-index-template.md` to create a new `project-index.md` in `tier-1-active/` for each project.

2. **Agent Tasks**: Agents load the project index and relevant domain documents from their folders.

3. **Document Creation**: When creating new documents, use the standard header format and place in the appropriate agent folder.

4. **Updates**: Update the project index registry and snapshot after significant changes.

5. **Archival**: Move completed phases or superseded documents to `archive/`.

6. **Scaling**: For multiple projects, create separate repositories; for shared templates, consider a system repo.

## Getting Started

- Read `foundation/context.md` for project background.
- Review `tier-1-active/project-index.md` for current state.
- Start populating domain documents as tasks arise.

## Contributing

- Follow the standard document header for all new files.
- Update the project index after creating or modifying documents.
- Use the tiered structure to maintain organization.