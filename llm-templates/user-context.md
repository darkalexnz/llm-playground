# User Context
*LLM input document — updated March 2026*

---

## About Me

- **Role:** UX/UI Designer, New Zealand telco. Sole designer on a 12-person product squad.
- **Background:** 6 years running a Design Thinking-led software design/dev company (NLP, RPA). Wide UI/UX experience across consumer and internal products. Webflow, WordPress, HTML, CSS, JS, Python. One year CS at university.
- **Position on team:** All design flows through me — I am the primary bottleneck between product thinking and development execution. Scoping a new feature takes days to weeks; dev takes two days. Design pace sets the team's pace.
- **Code literacy:** Medium reading proficiency. Understands React, TypeScript, HTML, CSS, JS, Python. Code literacy matters as a reading/communication skill, not as a primary output.
- **Communication style:** Concise, direct. Prefers holistic feedback over line-by-line. Structured artifacts and markdown over conversational filler. Expects a senior peer approach from AI — high-level partner, not just a tool.

---

## Goals

1. **Reduce the bottleneck.** Highest-leverage contribution as sole designer for 7+ engineers. Throughput and clarity, not code output.
2. **Upskill in AI-augmented design workflow.** Rapid prototyping, high-fidelity handoff, AI tool integration across the full design pipeline.
3. **Build long-term employability.** Position as a high-value design practitioner in an AI-native product development environment.
4. **Persistent knowledge layer.** Move from fragmented context (memory, email, Figma, ADO) toward structured, machine-readable project knowledge.

---

## Real Problems

- **I am the funnel.** 7 engineers, one designer. When I'm slow or unclear, the whole team slows.
- **Handoff is low-fidelity.** Static Figma exports plus text descriptions leave room for misinterpretation, missing states, and rework.
- **No persistent project knowledge layer.** Decisions, rationale, and context live across ADO, Figma, email, and memory. No single source of truth for design intent.
- **Design system mismatch.** Designing in Figma with a Mantine-based system; dev team builds in shadcn. Translation loss at every handoff.
- **AI mandate without a plan.** Business wants AI in both the product and the process. No clear owner or approach yet — significant opportunity to lead this.
- **Role stretch.** Maintaining full design throughput while upskilling in new tools and approaches simultaneously.

---

## Tools

**Work (approved):**
Figma (incl. Make), Miro (incl. AI/Flows), VS Code, GitHub Copilot, Microsoft 365 suite (SharePoint, Teams, 365 Copilot), Azure DevOps

**Personal / home:**
Obsidian, Claude Code, Google Drive, Gemini — not approved at work

---

## Workflow

Requirements gathering → discovery → problem/solution framing → user stories + mockups + acceptance criteria → ADO task management → dev briefing (static Figma exports + text descriptions) → UAT → iteration. Also responsible for balancing input from devs, architects, PO, CX designer, analyst, stakeholders, and leadership.

---

## The Agentic Design System

A structured set of AI agents, document templates, and a tiered memory architecture supporting design work across the 4D process (Discover, Define, Design, Deliver).

### Architecture

- **Tiered memory:** Tier 1 (project index, always loaded), Tier 2 (domain documents, loaded on demand), Tier 3 (ephemeral task context)
- **Five agents:** Orchestrator, Discover, Define, Design, Deliver — each with owned documents, read documents, and input/output contracts
- **Shared format:** All documents are `.md` with a standard header (type, owner, tier, status, version, linked agents, linked documents)
- **Markdown as design medium:** Mermaid diagrams for flows, structured markdown for wireframes using actual shadcn component names, component library reference as shared vocabulary

### Visual Markdown Spec (VMS) Framework (v0.2)

A reusable format for LLM-readable, visually annotated design handoff documents:
- Markdown-primary with ASCII wireframes (Unicode box-drawing characters) and keyed annotation blocks
- Library-agnostic component references
- `.vms.md` file extension, `/specs/{domain}/` directory structure
- Diff-friendly one-sentence-per-line prose
- Four-point annotation hierarchy: What → Behaviour → Constraints → Edge cases
- Fixed skeleton: Context, Layout, Components, States & Behaviour, Data, Acceptance Criteria, Open Questions, Changelog

### Tooling architecture

- GitHub repo of markdown files as single source of truth
- VS Code as desktop interface (with GitHub Copilot and Claude model access)
- Termux + Claude Code on Android as mobile interface
- Both pointed at the same synced vault

### Current state

- `project-index.md` complete (Tier 1, Orchestrator-owned)
- All other domain documents listed in registry — structure defined, content not yet created

### Next steps

1. Populate project index with real current content
2. Build `component-library-reference.md` first among Tier 2 docs
3. Run one end-to-end test on a real upcoming design task
4. Propose Code Connect setup to dev team to close the handoff gap

---

## Foundations Covered

These concepts have been discussed and don't need re-explaining unless specifically asked:

**Frontend/Dev:** React + TypeScript app structure, Git workflow, Azure deployment pipeline, ESLint/Prettier, props down / events up, environment variables

**Design workflow and tools:** AI-augmented UX workflow, Figma Make (capabilities and limitations), shadcn Figma kit options (Obra, Pietro Schirano, shadcn/studio), v0 by Vercel, Miro AI Flows, design system migration (Mantine → shadcn), tiered memory architecture

**Frameworks:** 4D Design Framework (Discover, Define, Develop, Deliver), Double Diamond

---

## Working Preferences

- One document at a time — agree template before moving on
- Artifacts preferred over inline markdown for documents
- Claude Project hosts this work — context brief as project instruction, documents built as artifacts within project conversations
- Conversation history does not carry over between sessions; project documents are the persistent knowledge layer
- Practitioners/resources followed: Nikita Samutin, Paul Boag, Jakob Nielsen, Mizko/Michael Wong; Smashing Magazine workflow category

---

## Open Questions — My Role

- What does a significantly improved handoff look like for this team — and what would it save per sprint?
- Who owns the AI product mandate and is there appetite for a designer-led brief?
- Which developer is best placed as a technical thought partner for design decisions?
- What would the team consider a meaningful improvement in design throughput?
