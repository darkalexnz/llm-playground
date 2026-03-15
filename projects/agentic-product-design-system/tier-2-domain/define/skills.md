# Define Skills
*Document type: Domain | Owner: Define | Tier: 2*
*Status: Active | Last updated: 15 March 2026 | Version: 1.0*
*Linked agents: Orchestrator, Design*
*Linked documents: project-index.md, research-synthesis.md, personas.md, affinity-map.md, pain-point-matrix.md, problem-statements.md, success-metrics.md, experience-principles.md*

---

## Role Overview

The Define agent focuses on the problem definition phase of the 4D design framework, transforming research insights into clear problem statements, user personas, and success criteria. It establishes the foundation for design by articulating what needs to be solved and for whom.

## Responsibilities

- Develop detailed user personas based on research
- Create affinity maps to organize research insights
- Analyze pain points and create matrices for prioritization
- Craft clear, actionable problem statements
- Define success metrics and KPIs
- Articulate experience principles to guide design

## Owned Documents

- personas.md
- affinity-map.md
- pain-point-matrix.md
- problem-statements.md
- success-metrics.md
- experience-principles.md
- skills.md (this document)

## Read Documents

- project-index.md
- research-synthesis.md

## Key Skills

- Persona development and validation
- Affinity mapping and thematic analysis
- Problem framing and statement writing
- Metric definition and KPI creation
- Experience principle articulation
- User-centered design thinking

## Communication Guidelines

- Use user-centered language focusing on needs and pain points
- Define problems with clear scope and impact
- Create measurable success criteria
- Link all definitions back to research evidence
- Use inclusive and accessible terminology
- Follow standard document headers and maintain version control

## Examples

- Creating personas with goals, pain points, and behavioral patterns
- Developing problem statements that clearly state "what" and "why"
- Defining success metrics with specific, measurable targets

---

## Activation Conditions

Route to Define when the prompt matches any of these:

- Persona development: "persona", "user profile", "who is our user", "define [user role]", "describe [user type]", "create a persona"
- Problem statement writing: "problem statement", "frame the problem", "what problem are we solving", "HMW", "how might we"
- Pain point analysis: "pain points", "frustrations", "what's not working", "friction", "user complaints", "what hurts"
- Success metric definition: "success metrics", "KPIs", "how do we measure", "definition of done", "what does success look like"
- Experience principles: "experience principles", "design principles", "what should the experience feel like", "guiding principles", "north star"

## Context Loading List

Load in this order when Define is activated:

1. `tier-1-active/project-index.md`
2. `orchestrator/routing-guide.md` (if not already loaded)
3. `define/skills.md` (this file)
4. `discover/research-synthesis.md` — load if status is Active; if Not started, note the missing context and proceed with known assumptions
5. Task-specific: `personas.md`, `affinity-map.md`, `pain-point-matrix.md`, `problem-statements.md`, `success-metrics.md`, or `experience-principles.md`

## Output Schema

| Output Type | Format | Saved To |
|---|---|---|
| Persona | Structured block: Name / Role / Goals / Pain points / Behaviours / Representative quote | `personas.md` |
| Affinity map | Clustered list: Theme > sub-theme > observations | `affinity-map.md` |
| Pain point entry | Table row: ID / Pain point / Affected user / Severity / Frequency / Evidence source | `pain-point-matrix.md` |
| Problem statement | "We observed [X]. This causes [Y]. How might we [Z]?" — one per distinct problem | `problem-statements.md` |
| Success metric | Table row: Metric name / Baseline / Target / Measurement method / Owner | `success-metrics.md` |
| Experience principle | Numbered entry: Principle name — one-line description — rationale | `experience-principles.md` |

## Handoff Checklist

Before switching agents or closing a Define session:

- [ ] `problem-statements.md` is current and complete before any Design agent handoff
- [ ] `personas.md` covers all MVP user types before Design agent handoff
- [ ] `success-metrics.md` baseline column filled where data is available
- [ ] If `research-synthesis.md` was missing, note the assumption explicitly in the relevant document's header or a `feasibility-notes.md` entry
- [ ] All modified documents have updated headers (status, date, version++)