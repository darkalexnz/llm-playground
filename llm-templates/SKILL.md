# SKILL.md — [Skill Name]
<!-- Reusable task methodology. Loaded on demand when this skill is invoked — not at every session start. One skill = one repeatable task type. Keep it executable, not descriptive. -->

---

## Skill

<!-- One line. What this skill does when invoked. -->
Scaffold a new feature module from a VMS spec file, following project conventions.

## Trigger

<!-- How Claude knows to use this skill. What the user says, or what condition activates it. -->
User says: "build this feature", "scaffold from spec", or references a `.vms.md` file with a request to implement.

## Inputs Required

<!-- What Claude needs before starting. If missing, ask — don't assume. -->
| Input | Source | Required |
|---|---|---|
| VMS spec file | `@specs/{domain}/feature-name.vms.md` | Yes |
| Target directory | User confirms or infers from spec context | Yes |
| Offer type / user role context | `src/types/offers.ts` + `src/types/roles.ts` | Yes |
| Existing related components | `src/components/` or `src/features/` | Recommended |

## Process

<!-- Step-by-step. Explicit ordering matters. -->

### Step 1 — Read the spec
- Load the referenced `.vms.md` file in full
- Identify: layout sections, component list, states and behaviour, data requirements, acceptance criteria
- Flag any open questions in the spec before proceeding — do not make assumptions about unspecified behaviour

### Step 2 — Audit existing components
- Check `src/components/` and `@specs/component-library-reference.md`
- List which spec components map to existing shadcn/ui components
- Note any gaps that require new components (flag for designer review before building)

### Step 3 — Scaffold the feature module
- Create `src/features/{feature-name}/` with:
  - `index.tsx` — main feature component
  - `components/` — feature-scoped sub-components
  - `hooks/` — feature-scoped hooks if needed
  - `types.ts` — local types if not already in `src/types/`
- Wire to routing and permissions as specified in the spec

### Step 4 — Implement states
- Build each state defined in the spec: default, loading, empty, error, edge cases
- Use the state matrix from the spec — do not invent states not listed
- Validate against acceptance criteria before marking complete

### Step 5 — Output summary
- List files created or modified
- Flag any spec ambiguities encountered during build
- List any components added to quarantine (new, not yet designer-reviewed)

## Output

<!-- What this skill produces. Be specific. -->
- Working feature module in `src/features/{feature-name}/`
- Summary comment listing: files created, open questions, quarantined components
- No new packages installed without flagging

## Rules

<!-- Constraints specific to this skill. -->
- Never build UI that isn't in the spec — if it's not specced, flag it and ask
- New components go into `Quarantine` section of `component-library-reference.md` until reviewed
- Do not modify shared components in `src/components/` — create feature-scoped versions instead
- Always check the role permission model before rendering actions

## References

<!-- Files this skill reads. -->
- @specs/design-system-rules.md
- @specs/component-library-reference.md
- @src/types/offers.ts
- @src/types/roles.ts

---
<!-- Skill version: 0.1 | Owner: [agent or person] | Last updated: [date] -->
