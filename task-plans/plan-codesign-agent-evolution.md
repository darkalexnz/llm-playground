# plan-codesign-agent-evolution

*Task: Rename co-design-agent → codesign-agent + architectural & operational improvements*
*Status: Implemented*

---

## Summary

Renamed the project and added six improvements to address the real interaction problems: no project-level context, no session resume, no skill discovery, no context lifecycle management.

### Changes

**Rename:** `co-design-agent` → `codesign-agent` across directory and all references.

**Architectural improvements:**
1. **Project context file** — `project-context.md` template for shared product/team/stack context across tasks. One file per project, created once, referenced by all task docs.
2. **Cross-task referencing** — during Research, agent checks project context for completed upstream tasks and offers to pull in relevant outputs.
3. **Phase summarisation** — completed phases collapse to 2-4 line summaries in task docs. Assumptions never collapsed. Keeps working context lean.

**Operational improvements:**
1. **Session resume protocol** — defined workflow for picking up existing tasks (read state, report status, present options).
2. **Skill suggestion from intent** — compact lookup table in CLAUDE.md maps natural language to skills. Agent suggests but doesn't auto-invoke.
3. **Output portability hints** — brief footer in skill templates suggesting how to move output into ADO/Figma/SharePoint.

### By the numbers

| Metric | Before | After |
|---|---|---|
| CLAUDE.md | 79 lines | ~130 lines |
| Core system files | ~202 lines | ~290 lines |
| New concepts | 0 | 1 (project context) |
| New files | 0 | 1 (project-context-template.md) |

### Task checklist

- [x] Rename directory (git mv)
- [x] Update all references (5 files)
- [x] Create project-context-template.md
- [x] Rewrite CLAUDE.md (session resume, cross-task, skill activation, phase summarisation)
- [x] Update task-template.md (project link, phase annotations)
- [x] Add portability footer to prd.md
- [x] Update README.md (rename, new capabilities)
- [x] Create this plan file
