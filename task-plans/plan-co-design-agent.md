# plan-co-design-agent.md

**Task:** Define, document, and plan the Co-Design Agent
**Phase:** 1 — Discovery & Definition
**Status:** Planning (awaiting approval)

---

## Research

### Summary

| Question | Answer |
|---|---|
| Who uses it? | You (primary), formatted for designers and engineers too |
| Trigger | Natural language — design it to be obvious given available tools |
| Multi-agent? | Later. For now a design companion. |
| What is "done"? | `task-[name].md` is the living plan/guide doc. Separate output files go in the same folder, referenced from the task doc. |
| Who consumes output? | Primarily you, but formatted for designers and engineers. PRD writing is a named example. |
| Skills source | Draw from `agentic-product-design-system` — take the best tasks |
| Who invokes skills? | User specifies. |
| Are skills composable? | Yes — separate outputs, combined after. |
| Technical form | Templates and instructions in `/projects/codesign-agent` |
| Memory/persistence | Task doc is the memory. Active session is working context. |
| Tool integration | No direct integrations. Outputs usable in Figma, ADO etc. |
| Workspace protocol | Same research → plan → approve → implement loop, task doc as living plan. |

### What exists in agentic-product-design-system

Four domain skills, each with owned documents, output schemas, and activation conditions:

- **Discover** — stakeholder mapping, user journey, assumption register, research synthesis
- **Define** — problem statements, personas, pain point matrix, success metrics, experience principles
- **Design** — wireframes (Markdown), user flows, IA, feasibility notes, iteration log
- **Deliver** — user stories, acceptance criteria, state matrix, handoff doc, UAT plan

Also an **Orchestrator** — not needed here.

The existing system is heavily structured (tiered memory, routing guides, handoff checklists). The codesign agent keeps only: output schemas, activation cues, and one template per skill.

### Mapping original skill names

The README listed six skills. They map as follows — no new skill types needed:

| Original | Maps to |
|---|---|
| Discovery | Discover |
| Design | Design |
| Define | Define |
| Deliver | Deliver |
| Development | → Deliver (handoff doc, feasibility notes) |
| Product | → Define (success metrics, experience principles) |

---

## Plan

### Principles

- One task = one folder = one task doc + any output files
- Skills are templates the user invokes explicitly — no routing logic
- Task doc is always the source of truth; output files are secondary
- No orchestrator, no checklists, no tiered memory — just good prompts and templates

### Folder structure

Each skill is its own file — the four D's are grouping folders, not single files. A skill file serves as both its definition and its output template (copy it into the task folder when invoked).

```
codesign-agent/
  README.md                         ← what this agent is and how to use it
  CLAUDE.md                         ← session instructions Claude loads automatically
  skills/
    discover/
      stakeholder-map.md
      user-journey.md
      assumption-register.md
      research-synthesis.md
    define/
      problem-statements.md
      personas.md
      pain-point-matrix.md
      success-metrics.md
    design/
      wireframes.md
      user-flows.md
      information-architecture.md
      feasibility-notes.md
    deliver/
      user-stories.md
      acceptance-criteria.md
      state-matrix.md
      prd.md
  templates/
    task-template.md                ← base task doc (Research + Planning sections)
```

Task files live outside the agent folder, per workspace convention:
```
[wherever the work lives]/
  task-[name]/
    task-[name].md                  ← living plan
    [copied-skill-file].md          ← e.g. wireframes.md, prd.md (referenced from task doc)
```

### Skills — curated from agentic-product-design-system

| Group | Skill | Activation cues |
|---|---|---|
| **Discover** | stakeholder-map | "who's involved", "stakeholders", "who are the decision makers" |
| | user-journey | "user journey", "current experience", "what does [user] go through" |
| | assumption-register | "assumption", "we're assuming", "needs validation" |
| | research-synthesis | "synthesise research", "key insights", "what did we learn" |
| **Define** | problem-statements | "problem statement", "HMW", "what are we solving", "frame the problem" |
| | personas | "persona", "who is our user", "define [user role]" |
| | pain-point-matrix | "pain points", "friction", "what's not working", "frustrations" |
| | success-metrics | "success metrics", "KPIs", "how do we measure", "what does success look like" |
| **Design** | wireframes | "wireframe", "design the", "what should X look like", "layout for" |
| | user-flows | "user flow", "steps to", "how does a user [action]", "task flow" |
| | information-architecture | "IA", "navigation structure", "how should this be organised" |
| | feasibility-notes | "feasibility", "is this possible", "technical constraints", "can we build" |
| **Deliver** | user-stories | "user stories", "write stories for", "dev handoff", "requirements for" |
| | acceptance-criteria | "acceptance criteria", "AC for", "definition of done", "testable criteria" |
| | state-matrix | "state matrix", "UI states", "all states of", "component states" |
| | prd | "PRD", "product requirements", "build spec", "implementation doc", "hand this off" |

### Phases

#### Phase 1 — Define the agent (current)
- [x] Rewrite `README.md` — full description, usage, skill index, task tracker
- [x] Write `CLAUDE.md` — session instructions: how to start, create task docs, invoke skills

#### Phase 1.5 — Define the agent (current)
- [ ] Write `templates/task-template.md`
- [ ] Write all 16 skill files (4 per group) — each is definition + blank output template

#### Phase 2 — Validate
- [ ] Run a test task end-to-end
- [ ] Refine based on real usage

#### Phase 3 — Validate (future)
- [ ] Run a test task end-to-end
- [ ] Refine based on real usage

### Out of scope (v1)
- Multi-agent handoff
- Figma / ADO integration
- Orchestrator / routing logic
- Automatic skill selection

---

*plan-co-design-agent.md — updated 2026-03-15*
