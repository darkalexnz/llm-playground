# GEMINI.md

These instructions are foundational mandates for all Gemini CLI sessions within the **Agentic Product Design System**. They take absolute precedence over general workflows.

## Core Operational Mandates

### 1. Tiered Memory Architecture
- **Tier 1 (Always Loaded):** `tier-1-active/project-index.md` must be read at the start of every session to establish project state and document locations.
- **Tier 2 (On-Demand):** Load domain-specific documents from `/tier-2-domain/` only when relevant to the task.
- **Tier 3 (Ephemeral):** Use `/tier-3-work/` for task outputs, brainstorming, and scratchpad files. Archive or delete after completion.

### 2. Standard Document Headers
All markdown files (.md) in this system MUST begin with the standard header block:
```markdown
# [Document Title]
*Document type: [Index | Domain | Task Output] | Owner: [Agent Name] | Tier: [1 | 2 | 3]*
*Status: [Draft | Active | Needs Review | Archived] | Last updated: [Date] | Version: [n]*
*Linked agents: [agents that read this document]*
*Linked documents: [related documents by title]*
```

### 3. Agent-Based Ownership
- Do not modify a Tier 2 document unless acting as its specified owner (e.g., Design agent for `wireframes.md`).
- The **Orchestrator** is the only agent permitted to update `project-index.md` and `decision-log.md`.

### 4. High-Fidelity Design Communication
- **Standard Vocabulary:** Use only component names defined in `tier-2-domain/design/component-library-reference.md` in all wireframes and user flows.
- **Format preference:** Prefer Markdown-native formats (tables, nested lists) for flows and state transitions. Use Mermaid only when conditional branching genuinely requires rendered output.

### 5. Context Efficiency
- Minimize token usage by loading only the necessary Tier 2 documents.
- Keep `project-index.md` concise (under 500 tokens). Move detailed historical context to `/archive/` or specific Tier 2 logs.

### 6. Agent Model
This system uses **role-switching within a single session**. Agents are not separate processes. To switch agents: load the target agent's `skills.md` and the context documents listed in `routing-guide.md` for that task type, then announce the loaded state before executing.

### 7. Session Start
Begin every session by loading in this order:
1. `tier-1-active/project-index.md`
2. `orchestrator/routing-guide.md`
3. `orchestrator/session-protocol.md`

Do not load any Tier 2 domain documents before classifying the user's first prompt.

### 8. Tier 3 Policy
See `orchestrator/session-protocol.md` section 5 for the full policy. Short form:
- **File-based:** task outputs that span sessions or inform a future Tier 2 document
- **Chat-only (discard):** scratchpads and interim drafts superseded by a Tier 2 update
- **Archive:** completed sprint or phase deliverables — move to `archive/[YYYY-MM-DD]-[label]/`

---
*End of GEMINI.md v1.1*
