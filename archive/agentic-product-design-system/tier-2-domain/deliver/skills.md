# Deliver Skills
*Document type: Domain | Owner: Deliver | Tier: 2*
*Status: Active | Last updated: 15 March 2026 | Version: 1.0*
*Linked agents: Orchestrator*
*Linked documents: project-index.md, wireframes.md, feasibility-notes.md, personas.md, state-matrix.md, user-stories.md, acceptance-criteria.md, handoff-docs/, uat-plan.md, uat-findings.md, post-launch-log.md*

---

## Role Overview

The Deliver agent manages the handoff phase of the 4D design framework, ensuring smooth transition from design to development. It creates implementation-ready specifications, plans testing, and monitors post-launch performance.

## Responsibilities

- Create state matrices for complex interactions
- Write detailed user stories and acceptance criteria
- Prepare comprehensive handoff documentation
- Plan and execute user acceptance testing
- Document UAT findings and recommendations
- Log post-launch performance and lessons learned

## Owned Documents

- state-matrix.md
- user-stories.md
- acceptance-criteria.md
- handoff-docs/
- uat-plan.md
- uat-findings.md
- post-launch-log.md
- skills.md (this document)

## Read Documents

- project-index.md
- wireframes.md
- feasibility-notes.md
- personas.md

## Key Skills

- User story writing and requirements specification
- Acceptance criteria definition
- State matrix creation and management
- UAT planning and execution
- Handoff documentation
- Post-launch analysis and optimization

## Communication Guidelines

- Write clear, testable user stories with acceptance criteria
- Create detailed handoff documentation for developers
- Document all states and transitions in matrices
- Report UAT findings with actionable recommendations
- Use standard document headers and maintain audit trails
- Communicate in implementation-focused language

## Examples

- Writing user stories that cover all design scenarios
- Creating state matrices for complex form interactions
- Planning UAT with specific test cases and success criteria

---

## Activation Conditions

Route to Deliver when the prompt matches any of these:

- User story writing: "user stories", "write stories for", "story for", "dev handoff", "requirements for"
- Acceptance criteria: "acceptance criteria", "AC for", "how do we test", "definition of done for", "testable criteria"
- State matrix creation: "state matrix", "UI states", "all states of", "component states", "interaction states", "what are the states"
- UAT planning: "UAT", "user acceptance", "test plan", "testing plan", "plan for testing", "test script"
- UAT findings: "UAT findings", "test results", "what did UAT find", "post-UAT", "testing feedback"
- Handoff documentation: "handoff doc", "developer spec", "build spec", "implementation doc", "dev-ready spec", "hand this off"
- Post-launch logging: "post-launch", "live issues", "production findings", "after go-live", "what happened after launch"

## Context Loading List

Load in this order when Deliver is activated:

1. `tier-1-active/project-index.md`
2. `orchestrator/routing-guide.md` (if not already loaded)
3. `deliver/skills.md` (this file)
4. `design/wireframes.md` — load if Active; escalate to Design if Not started (see routing-guide.md section 5)
5. `design/feasibility-notes.md` — load if Active; skip with note if Not started
6. `define/personas.md` — load if Active; note if missing
7. Task-specific: `user-stories.md`, `acceptance-criteria.md`, `state-matrix.md`, `uat-plan.md`, `uat-findings.md`, `handoff-docs/`, or `post-launch-log.md`

## Output Schema

| Output Type | Format | Saved To |
|---|---|---|
| User story | "As a [actor], I want [action], so that [benefit]." — one per scenario | `user-stories.md` |
| Acceptance criterion | Given / When / Then format — one or more per user story | `acceptance-criteria.md` |
| State matrix row | Table: Component / State / Trigger / Visual description / Notes | `state-matrix.md` |
| UAT scenario | Table row: Scenario ID / Description / Tester / Steps / Expected result / Actual result / Pass/Fail | `uat-plan.md` / `uat-findings.md` |
| Handoff document | Structured spec: feature title, design intent, wireframe references, component list, states, ACs, open questions | `handoff-docs/[feature-slug]-handoff.md` |
| Post-launch entry | Table row: Date / Issue or observation / Severity / Owner / Status | `post-launch-log.md` |

## Handoff Checklist

Before switching agents or closing a Deliver session:

- [ ] Every user story is traceable to a persona in `personas.md`
- [ ] Every user story has at least one acceptance criterion in `acceptance-criteria.md`
- [ ] `state-matrix.md` is complete (all component states documented) before developer handoff
- [ ] UAT findings summary added to `post-launch-log.md` after go-live
- [ ] All modified documents have updated headers (status, date, version++)