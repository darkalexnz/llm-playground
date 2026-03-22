# CLAUDE.md
<!-- Project-level AI operating manual. Loaded automatically at the start of every Claude Code session. Keep under 150 lines. Heavy detail belongs in imported files. -->

---

## Project

<!-- One paragraph. What the app does, who uses it, current stage. -->
Internal offer management platform replacing a spreadsheet/email process for promotional device and product lifecycle management. Users: DeviceOps, Creative, Catalogue. Pre-launch MVP — DeviceOps UAT complete, Creative and Catalogue flows in progress.

## Stack

<!-- List the key technologies. Be explicit — the LLM should never guess. -->
- **Framework:** React 18, TypeScript
- **Styling:** Tailwind CSS
- **Component library:** shadcn/ui (Radix primitives)
- **State:** [e.g. Zustand / React Query / Context]
- **Backend:** [e.g. REST API / tRPC / Supabase]
- **Deployment:** Azure (dev / test / staging / prod)
- **Repo:** Git/GitHub — branch naming: `feature/`, `fix/`, `chore/`

## Directory Structure

<!-- Top-level only. Enough for orientation. -->
```
src/
  components/     # Shared UI — import from here, don't create inline
  features/       # Feature-scoped modules
  lib/            # Utilities, helpers
  types/          # Shared TypeScript types
specs/            # Design specs and system rules
.claude/
  skills/         # Task-specific skill files
```

## Coding Standards

<!-- Non-negotiable rules. Keep this list short — only things Claude gets wrong without them. -->
- Use TypeScript strictly — no `any`
- Components: functional only, named exports
- Styling: Tailwind utility classes only — no inline styles, no CSS modules
- Always use existing shadcn components — never create one-off UI primitives inline
- Imports: absolute paths via `@/` alias
- No hardcoded colour values — use design tokens from `@/styles/tokens.css`

## Design System

<!-- Point to the authoritative files. Don't duplicate content here. -->
Before writing or modifying any UI code:
- Read @specs/design-system-rules.md for tokens, spacing, and visual rules
- Read @specs/component-library-reference.md for available components and usage

## Key Conventions

<!-- Things that would surprise a new developer. Decisions that aren't obvious from the code. -->
- Offer types have variable field structures — use the discriminated union pattern in `src/types/offers.ts`
- Permission model is role-based: DeviceOps / Creative / Catalogue — always check before rendering actions
- Do not modify `/migrations` directly — schema changes go through the migration script process
- All user-facing strings must go through the i18n helper even for MVP

## Active Tasks

<!-- Optional. Update this to give Claude a running orientation on current work. Clear when done. -->
- [ ] Creative flow: offer content editing UI (in progress)
- [ ] Catalogue flow: publish to web/CRM handoff (not started)
- [ ] Design system: Mantine → shadcn migration (ongoing)

## What Claude Should Not Do

- Do not install new packages without flagging it first
- Do not write new UI components when an existing shadcn component can be composed
- Do not push directly to `main`
- Do not assume offer field structure — read the type definitions

---
<!-- Last updated: [date] | Owner: [name] -->
