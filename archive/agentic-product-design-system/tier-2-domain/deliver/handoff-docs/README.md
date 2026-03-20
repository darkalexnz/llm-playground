# Handoff Docs
*Document type: Index | Owner: Deliver | Tier: 2*
*Status: Active | Last updated: 15 March 2026 | Version: 1.0*
*Linked agents: Deliver, Design*
*Linked documents: deliver/skills.md, wireframes.md, state-matrix.md, acceptance-criteria.md*

---

Feature-level handoff specifications live here. Each file is a developer-ready spec for one feature or screen.

## Naming convention

`[YYYY-MM-DD]-[feature-slug]-handoff.md`

Example: `2026-03-15-offer-editor-form-handoff.md`

## Expected sections in each handoff doc

```
# [Feature Name] Handoff
*Document type: Domain | Owner: Deliver | Tier: 2*
*Status: Draft | Last updated: [Date] | Version: 0.1*
*Linked agents: Deliver, Design*
*Linked documents: wireframes.md, state-matrix.md, acceptance-criteria.md*

## Design Intent
One paragraph: what this feature does, who it's for, key design decisions.

## Wireframe References
Links to relevant sections in wireframes.md. Include screen names and state variants.

## Component List
Table: Component name (shadcn) / Usage / Props/configuration / Notes

## States
Reference the relevant rows in state-matrix.md. List default, loading, error, empty, disabled states.

## Acceptance Criteria
Link to the relevant stories and ACs in user-stories.md and acceptance-criteria.md.

## Open Questions
Anything unresolved that developers need clarity on before building.
```

## Who creates these

Deliver agent, during handoff documentation tasks. Triggered by intent signals: "handoff doc", "developer spec", "build spec", "hand this off".
