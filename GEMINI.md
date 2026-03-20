# GEMINI.md

Foundational mandates for all Gemini CLI sessions in the **LLM Playground** workspace. Takes absolute precedence over general defaults.

## User Profile

Senior UX Designer, sole designer at a New Zealand telco, supporting 8+ developers. Medium code literacy (React, TypeScript, HTML, CSS, JS, Python). Code is a communication and architecture tool, not a contribution medium. Treat as a senior peer — skip beginner-level explanations, default to high-signal architectural framing. See `about-user.md` for full profile.

## Communication Style

- Concise and direct — no filler, no trailing summaries
- Prefer structured Markdown artifacts over conversational prose
- Do not suggest changes, refactors, or improvements beyond what was explicitly asked

## Task Execution Protocol

**Before any non-trivial task, create `task-plans/plan-[task-name].md`.** Plan files live at the workspace root in `task-plans/`.

1. **Research** — explore thoroughly, write findings into the plan file. Stop and surface to user. Wait.
2. **Plan** — append approach, steps, trade-offs, and a task checklist. Stop and surface. Wait for approval.
3. **Implement** — execute only after explicit approval. If blocked, stop and surface options.

## Gemini-Specific Mandates

- Prioritise fast, high-signal tools (`grep_search`, `glob`) to map the workspace
- Proactively identify shell commands or scripts that automate repetitive tasks
- Maintain machine-readable logs and plans for cross-LLM continuity (Claude Code + Gemini CLI)
- Provide technical rationale and intent for every major action

---
*GEMINI.md v3.0*
