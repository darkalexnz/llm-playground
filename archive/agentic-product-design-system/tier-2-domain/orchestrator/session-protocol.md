# Session Protocol
*Document type: Domain | Owner: Orchestrator | Tier: 2*
*Status: Active | Last updated: 15 March 2026 | Version: 1.0*
*Linked agents: All*
*Linked documents: project-index.md, routing-guide.md*

---

## Purpose

This document defines the session lifecycle for every LLM session within this system. It covers how to start, how to switch between agents, how to close, and how to manage Tier 3 files. Read it alongside `routing-guide.md` at session start.

---

## 1. Cold Start Checklist

Use when opening a brand new session with no prior context in the window.

| Step | Action |
|---|---|
| 1 | Load `tier-1-active/project-index.md` — read snapshot, note active phase and open decisions |
| 2 | Load `orchestrator/routing-guide.md` — activates routing capability |
| 3 | Announce system ready state (see format below) |
| 4 | Receive first prompt → classify intent → follow routing-guide activation sequence |

**Announce ready state format:**
```
Orchestrator active.
Project index loaded. Routing ready.
Current phase: [phase from snapshot]
Open decisions: [decisions from snapshot]
What's the task?
```

---

## 2. Warm Start / Resume Protocol

Use when resuming mid-task in a continuing session, or when user provides a context brief.

| Step | Action |
|---|---|
| 1 | Load `project-index.md` and `routing-guide.md` |
| 2 | Load Tier 2 docs active in the prior session — user states which, or infer from document registry status column in project-index.md |
| 3 | Announce resumed state (format below) |
| 4 | Ask user to confirm or correct resumed state before proceeding |

**Announce resumed state format:**
```
[Agent] resuming.
Previously loaded: [docs]
Last known status: [status from header of most relevant doc]
Continuing: [task description]
— confirm or correct before I proceed?
```

---

## 3. Agent Role-Switching Mechanics

**Load sequence (strict order):**

1. `tier-1-active/project-index.md` — always first
2. `orchestrator/routing-guide.md` — always second (skip only if already loaded in current session)
3. Target agent's `skills.md`
4. Task-specific Tier 2 docs, in the order listed in routing-guide.md Task Taxonomy for that task type

**Context economy rule:** Only load docs explicitly listed in routing-guide.md for the active task. Never speculatively load Tier 2 documents that aren't on the task's list.

**Unload sequence (on agent switch):**

1. Run the outgoing agent's Handoff Checklist (in their `skills.md`)
2. Update modified document headers: status field, last updated date, version number
3. Confirm with user: `"Output saved to [filename]. Switching to [Agent]?"`
4. Load new agent's `skills.md` + task-specific docs per routing-guide
5. Announce new agent state (format in routing-guide.md section 2)

---

## 4. Session Close Housekeeping

Run at the end of any session where documents were modified or decisions were made.

**Checklist:**

- [ ] All modified Tier 2 documents have updated headers (status, last updated, version++)
- [ ] `project-index.md` domain registry status column reflects any document changes
- [ ] New open questions surfaced during the session added to `open-questions.md`
- [ ] Decisions made during the session logged to `decision-log.md`
- [ ] Tier 3 files reviewed and given a disposition (keep / archive / delete — see section 5)
- [ ] Project snapshot in `project-index.md` updated if phase advanced or key decisions made

**Announce close format:**
```
Session close complete.
Documents updated: [list]
Decisions logged: [yes / none]
Tier 3 files: [list with disposition]
Project index: [updated / no change needed]
```

---

## 5. Tier 3 Persistence Policy

Files in `tier-3-work/` are ephemeral task outputs. Apply this policy at session close.

| Disposition | When to use | Action |
|---|---|---|
| **Keep (file-based)** | Output spans sessions, informs a Tier 2 doc but isn't ready to merge, or needs review before promoting | Leave in `tier-3-work/`. Name: `YYYY-MM-DD-[task-slug].md` |
| **Delete (chat-only)** | Brainstorming scratchpad, interim draft superseded by a Tier 2 update, one-session ideation not referenced again | Discard — do not save to disk |
| **Archive** | Completed sprint or phase deliverable, no longer active but worth keeping for reference | Move to `archive/[YYYY-MM-DD]-[label]/` before clearing the working folder |

**Promote to Tier 2:** When a Tier 3 file reaches a state of sufficient quality to become permanent, merge its content into the appropriate Tier 2 document, update the Tier 2 header, and delete the Tier 3 file.

---

*End of Session Protocol v1.0*
