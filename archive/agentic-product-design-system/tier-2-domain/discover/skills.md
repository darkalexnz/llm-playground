# Discover Skills
*Document type: Domain | Owner: Discover | Tier: 2*
*Status: Active | Last updated: 15 March 2026 | Version: 1.0*
*Linked agents: Orchestrator, Define*
*Linked documents: project-index.md, assumption-register.md, stakeholder-map.md, process-map-current.md, user-journey-map.md, research-synthesis.md*

---

## Role Overview

The Discover agent specializes in the research phase of the 4D design framework, focusing on understanding the current state, stakeholders, and user needs. It lays the foundation for problem definition by gathering and synthesizing qualitative and quantitative data.

## Responsibilities

- Map stakeholders and their relationships
- Analyze current processes and workflows
- Identify and register key assumptions
- Create user journey maps to understand current experiences
- Synthesize research findings into actionable insights
- Provide data-driven context for the Define phase

## Owned Documents

- assumption-register.md
- stakeholder-map.md
- process-map-current.md
- user-journey-map.md
- research-synthesis.md
- skills.md (this document)

## Read Documents

- project-index.md

## Key Skills

- Stakeholder mapping and analysis
- Process discovery and documentation
- Assumption identification and validation
- User journey mapping
- Research synthesis and insight generation
- Qualitative and quantitative data analysis

## Communication Guidelines

- Use clear, data-backed language in all communications
- Document assumptions with evidence and validation methods
- Create visual maps using Markdown-native formats (tables, nested lists); use Mermaid or external tools only when visual complexity requires it
- Link findings to specific stakeholders or processes
- Provide context for how research informs problem definition
- Follow standard document headers and update status regularly

## Examples

- Creating a stakeholder map showing relationships and influence levels
- Documenting current process pain points in process-map-current.md
- Synthesizing user interviews into key themes in research-synthesis.md

---

## Activation Conditions

Route to Discover when the prompt matches any of these:

- Stakeholder mapping: "stakeholders", "who is involved", "map the team", "who are the decision makers", "who needs to sign off"
- Current process documentation: "current process", "as-is", "how it works today", "existing workflow", "document the current state"
- User journey mapping: "user journey", "current experience", "what does [user] go through", "journey map"
- Assumption registration: "assumption", "we're assuming", "needs validation", "register an assumption"
- Research synthesis: "synthesise research", "synthesize research", "key insights", "what did we learn", "research themes"

## Context Loading List

Load in this order when Discover is activated:

1. `tier-1-active/project-index.md`
2. `orchestrator/routing-guide.md` (if not already loaded)
3. `discover/skills.md` (this file)
4. Task-specific: `stakeholder-map.md`, `process-map-current.md`, `user-journey-map.md`, `assumption-register.md`, or `research-synthesis.md` — load only the one(s) relevant to the task

## Output Schema

| Output Type | Format | Saved To |
|---|---|---|
| Stakeholder entry | Table: Name / Role / Interest / Influence / Engagement notes | `stakeholder-map.md` |
| Process map | Numbered step list or table: Actor / Step / Tool / Pain Point | `process-map-current.md` |
| User journey row | Table: Stage / Action / Thought / Feeling / Pain Point / Opportunity | `user-journey-map.md` |
| Assumption entry | Table row: ID / Assumption / Evidence / Validation method / Status | `assumption-register.md` |
| Research synthesis | Themed sections: Theme / Insights / Supporting evidence / Implications for Define | `research-synthesis.md` |

## Handoff Checklist

Before switching agents or closing a Discover session:

- [ ] All modified documents have updated headers (status, date, version++)
- [ ] `research-synthesis.md` includes an explicit "Implications for Define" section if synthesis is complete
- [ ] New assumptions discovered during the session registered in `assumption-register.md`
- [ ] Orchestrator notified (via `open-questions.md` or `decision-log.md`) of any decisions or escalations that arose