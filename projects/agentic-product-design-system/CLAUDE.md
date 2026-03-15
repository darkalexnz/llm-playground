# CLAUDE.md

These instructions are foundational mandates for all Claude Code sessions within the **Agentic Product Design System**. They take absolute precedence over workspace-level defaults.

## Project Snapshot

- **Product:** [Product Name]
- **Org:** [Org]
- **Stack:** [Stack]
- **Stage:** [Current Stage]
- **Active phase:** [Current Phase]
- **Open decisions:** [List open decisions here]

## Tiered Memory Architecture

Load documents in order of tier. Do not load Tier 2 documents speculatively.

| Tier | Location | When to load |
|---|---|---|
| 1 | `tier-1-active/project-index.md` | Every session — read first to establish project state |
| 2 | `tier-2-domain/{agent}/` | On-demand when relevant to the current task |
| 3 | `tier-3-work/` | Ephemeral — archive or delete after task completion |

## Agent-Based Ownership

- Every document has an owner agent: Orchestrator, Discover, Define, Design, or Deliver
- Do not modify a Tier 2 document unless acting as its specified owner
- Only the **Orchestrator** may update `project-index.md` and `decision-log.md`
- Full agent roster and document registry live in `tier-1-active/project-index.md`

## Standard Document Header

Every `.md` file in this system must open with this block:

```
# [Document Title]
*Document type: [Index | Domain | Task Output] | Owner: [Agent Name] | Tier: [1 | 2 | 3]*
*Status: [Draft | Active | Needs Review | Archived] | Last updated: [Date] | Version: [n]*
*Linked agents: [agents that read this document]*
*Linked documents: [related documents by title]*
```

## Design Vocabulary

- Use only component names defined in `tier-2-domain/design/component-library-reference.md` in all wireframes and user flows
- Format flows, state transitions, and diagrams using Markdown-native formats first (tables, nested lists, structured code blocks); use Mermaid when conditional logic or multiple paths genuinely benefit from rendered output and the target tool supports it

## Context Efficiency

- Keep `project-index.md` under 500 tokens — move historical detail to `/archive/` or specific Tier 2 logs
- Load only the Tier 2 documents directly relevant to the current task

## Agent Model

This system uses **role-switching within a single LLM session**. Agents are not separate processes. To switch agents: load the target agent's `skills.md` and the context documents listed in `routing-guide.md` for that task type, then announce the loaded state before executing.

## Session Start

Begin every session by loading in this order:
1. `tier-1-active/project-index.md`
2. `orchestrator/routing-guide.md`
3. `orchestrator/session-protocol.md`

This activates routing capability and the session lifecycle. Do not load any Tier 2 domain documents before classifying the user's first prompt.

## Tier 3 Policy

See `orchestrator/session-protocol.md` section 5 for the full policy. Short form:
- **File-based:** task outputs that span sessions or inform a future Tier 2 document
- **Chat-only (discard):** scratchpads and interim drafts superseded by a Tier 2 update
- **Archive:** completed sprint or phase deliverables — move to `archive/[YYYY-MM-DD]-[label]/`

---
*CLAUDE.md v1.1*
