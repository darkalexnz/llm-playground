# plan-playground-review

*Task: Comprehensive review and simplification of the llm-playground workspace*
*Status: Implemented*

---

## Summary

Simplified the workspace from ~2000 lines of instruction/protocol across 30+ files to ~550 lines across 16 files.

### What changed

1. **Archived `agentic-product-design-system`** — 1400 lines of framework with zero design outputs, superseded by codesign-agent
2. **Deleted empty projects** — pdr-writer/, test-project/
3. **Collapsed instruction chain** — 3 levels of indirection (CLAUDE.md → WORKSPACE.md → about-user.md) down to 1 (CLAUDE.md → about-user.md). Deleted WORKSPACE.md, rewrote CLAUDE.md and GEMINI.md as self-contained files.
4. **Moved reference docs out of root** — markdown-visuals.md and component-library-reference.md now live in codesign-agent/references/, loaded on demand instead of every session
5. **Trimmed about-user.md** — removed personal/fitness section, added detailed project context from the archived project's context.md
6. **Cleaned settings** — removed stale permission entries from .claude/settings.local.json

### By the numbers

| Metric | Before | After |
|---|---|---|
| Root instruction files | 3 | 2 |
| Root instruction lines | ~133 | ~60 |
| Indirection levels | 3 | 1 |
| Active project directories | 4 (1 real, 1 incomplete, 2 empty) | 1 |
| Total instruction lines | ~2000+ | ~550 |
| Files in active workspace | ~30+ | ~16 |
| Reference docs auto-loaded | 2 | 0 |

### Task Checklist

- [x] 1: Create archive/ at workspace root
- [x] 2: Create projects/codesign-agent/references/
- [x] 3: Copy + clean component-library-reference.md to codesign-agent/references/
- [x] 4: Move markdown-visuals.md to codesign-agent/references/
- [x] 5: Archive agentic-product-design-system (git mv)
- [x] 6: Delete pdr-writer/ and test-project/
- [x] 7: Update about-user.md (trim personal, add project context)
- [x] 8: Rewrite CLAUDE.md (self-contained, ~35 lines)
- [x] 9: Rewrite GEMINI.md (self-contained, ~25 lines)
- [x] 10: Delete WORKSPACE.md
- [x] 11: Update codesign-agent CLAUDE.md (add references line)
- [x] 12: Simplify projects/README.md
- [x] 13: Clean .claude/settings.local.json
- [x] 14: Create task-plans/plan-playground-review.md
- [x] 15: Commit
