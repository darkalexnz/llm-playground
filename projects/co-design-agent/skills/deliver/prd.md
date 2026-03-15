# Skill: PRD Writer

**Group:** Deliver
**Output file:** `prd.md`
**Activation cues:** "PRD", "product requirements", "build spec", "write this up for engineers", "dev-ready", "hand this off", "implementation doc"

## What this skill does

Produces a product requirements document structured for engineering handoff. Covers the problem being solved, who it affects, what the system needs to do, design references, and constraints. It is not a design doc — it is the translation layer between design intent and engineering work.

## When to invoke

- You have completed Research and Planning and are ready to produce an engineering-facing document
- A developer or team needs a written spec to build from
- You need to formalise scope before development begins

## Inputs needed

Before running this skill, ensure the task doc has:
- A clear brief and problem statement
- Known user types or personas
- Design references (wireframes, flows, or Figma links) if available
- Any known constraints or technical considerations

---

## Output template

Copy this section into `task-[name]/prd.md` and populate it.

---

# PRD: [Feature or initiative name]

**Task:** [Link to task-[name].md]
**Author:** [Name]
**Date:** [YYYY-MM-DD]
**Status:** Draft | In Review | Approved
**Consumers:** Engineering, [other stakeholders]

---

## Overview

[2–4 sentences. What is being built, why now, and what problem it solves.]

---

## Background

[Context that helps engineers understand the why. Reference relevant research, prior decisions, or existing systems. Link to external docs if useful.]

---

## Problem statement

[What is broken or missing today? Who is affected and how? Keep this user-centred.]

---

## Users

| User type | Description | Impact |
|---|---|---|
| | | |

---

## Requirements

### Must have

| # | Requirement | Notes |
|---|---|---|
| 1 | | |

### Should have

| # | Requirement | Notes |
|---|---|---|
| 1 | | |

### Out of scope

- [List explicitly what this initiative does not cover]

---

## Design references

| Artefact | Link / location | Notes |
|---|---|---|
| Wireframes | | |
| User flows | | |
| Figma | | |

---

## Constraints and considerations

[Technical constraints, platform limitations, accessibility requirements, dependencies on other teams or systems.]

---

## Open questions

| # | Question | Owner | Status |
|---|---|---|---|
| 1 | | | Open |
