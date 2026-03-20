# Codesign Agent

A lightweight design companion for structuring, researching, and executing design tasks. It works through a task document as a living plan, invokes modular skills to produce specific outputs, and keeps everything in one folder per task.

---

## How it works

1. **Start a task** — give the agent a design problem, brief, or question. If the task belongs to a project, the agent loads `project-context.md` for shared context.
2. **Research** — the agent checks for relevant upstream task outputs, gathers context, and surfaces assumptions in the task doc
3. **Plan** — the agent outlines the approach, identifies skills to invoke, and lists open questions — you review
4. **Iterate** — answer open questions or add feedback; the agent updates the task doc and re-presents the plan until you approve
5. **Execute** — approved skills run; each produces an output file in the task folder, linked from the task doc. Completed phases are summarised to keep the task doc lean.

**Resuming a task:** Reference an existing task doc and the agent reads it, reports current status, and picks up where you left off.

---

## Project context

For work spanning multiple tasks (e.g., the Offer Management Platform), create a `project-context.md` from `templates/project-context-template.md`. It carries product, team, stack, and decision context across all tasks — so you never re-explain the basics.

The agent uses the project context to discover relevant upstream outputs when starting new tasks.

---

## Task folder structure

Each task lives in its own folder. The task doc is the source of truth. All skill outputs go alongside it, linked from the task doc.

```
task-[name]/
  task-[name].md          <- living plan: brief, context, Research, Planning, output links
  wireframes.md           <- skill output (example)
  prd.md                  <- skill output (example)
```

Task folders live wherever the work belongs — not inside this agent folder.

---

## Skill catalogue

Skills are grouped by design phase. Invoke by name or describe what you need — the agent will suggest the right skill.

| Group | Skill | Use when |
|---|---|---|
| **Discover** | stakeholder-map | Mapping who is involved, their roles and influence |
| | user-journey | Documenting the current experience step by step |
| | assumption-register | Capturing and tracking unvalidated assumptions |
| | research-synthesis | Synthesising research into themes and insights |
| **Define** | problem-statements | Framing what problem is being solved and for whom |
| | personas | Defining the key user types and their needs |
| | pain-point-matrix | Cataloguing pain points by severity and frequency |
| | success-metrics | Defining how success will be measured |
| **Design** | wireframes | Sketching screens and layouts in structured Markdown |
| | user-flows | Mapping step-by-step flows through an experience |
| | information-architecture | Structuring navigation and content hierarchy |
| | feasibility-notes | Documenting constraints and implementation risks |
| **Deliver** | user-stories | Writing stories for development: As a / I want / So that |
| | acceptance-criteria | Writing Given / When / Then criteria per story |
| | state-matrix | Documenting all UI states for a component or flow |
| | prd | Writing a product requirements document for engineering handoff |

Skills are composable — a task can invoke multiple skills, each producing a separate output file.

---

## Project tracker

### Phase 1 — Define the agent
- [x] Design sessions: define skills, architecture, and scope
- [x] Rewrite `README.md`
- [x] Write `CLAUDE.md`
- [x] Write `templates/task-template.md`
- [x] Add project context template and cross-task referencing
- [x] Add skill activation table and session resume protocol
- [ ] Write remaining skill files — 1/16 done (`skills/deliver/prd.md`)

### Phase 2 — Validate
- [ ] Run a test task end-to-end
- [ ] Refine based on real usage
