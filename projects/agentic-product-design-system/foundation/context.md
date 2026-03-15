# Context

## Summary for New Chat Bootstrap

---

### About Me

- UX Designer at a New Zealand telco, sole designer on a 10-person product team
- Background: 6 years running a Design Thinking-led software design/dev company (NLP, RPA projects), wide UI/UX experience across consumer and internal products, Webflow, WordPress, HTML, CSS, JS, Python, one year CS at university
- Strong systems thinker, comfortable with software concepts, below dev team's technical level in practice
- Working on mass gaining, short daily morning resistance training, interest in nutrition optimisation
- Preference for concise, direct communication — feedback applied holistically, not line by line

---

### My Goals

- Reduce the design bottleneck: highest-leverage contribution as sole designer for 8+ developers
- Upskill in AI-augmented design workflow: rapid prototyping, high-fidelity handoff, AI tool integration across the full pipeline
- Build long-term employability as a high-value design practitioner in an AI-native product development environment
- Not a goal to make regular frontend code contributions — code literacy matters as a reading/communication skill only

---

### The Project

- Internal web app replacing a spreadsheet-and-email process for managing promotional device and product offer lifecycles — from brand partner negotiation (e.g. Samsung) through to live on website and CRM
- Stack: React, TypeScript, Azure (dev/test/staging/prod), shadcn, Git/GitHub, Azure DevOps
- Team: PO, CX designer, analyst, UX designer (me), 6–8 developers and architects
- Pre-launch MVP. Three months of discovery and build complete. DeviceOps UAT done. Creative and Catalogue flows in progress.
- Core feature: intelligent editable offer table/editor with variable complexity by offer type
- Primary MVP users: DeviceOps, Creative, Catalogue
- Broader stakeholders: Legal, Finance, Brand, Partnerships, external agencies
- Business mandate to incorporate AI into both the product and the design/dev process

---

### My Workflow

Requirements gathering → discovery → problem/solution framing → user stories + mockups + acceptance criteria → ADO task management → dev briefing (static Figma exports + text descriptions) → UAT → iteration. Responsible for balancing input across devs, architects, PO, CX, analyst, stakeholders, and leadership.

---

### My Real Problems

- I am the funnel — 8+ devs, one designer, whole team slows when I'm slow
- Handoff is low-fidelity — static exports and text leave room for misinterpretation and rework
- No persistent project knowledge layer — context lives across ADO, Figma, email, and memory
- Design system mismatch — designing in Mantine-based Figma system, dev team builds in shadcn
- AI mandate with no clear owner or plan — significant opportunity to lead this
- Role stretch — maintaining full throughput while upskilling simultaneously

---

### Approved Tools

Figma (incl. Make), Miro (incl. AI/Flows), VS Code, GitHub Copilot, Microsoft 365 suite (SharePoint, Teams, 365 Copilot), Claude

---

### Key Concepts Covered This Chat

**Frontend/Dev:**
- React + TypeScript app structure, file conventions, component model
- Git workflow: branching, commits, PRs, merge conflicts
- Azure deployment pipeline: dev → test → staging → prod
- ESLint and Prettier: linting rules, why they matter
- Props down / events up mental model
- Environment variables

**Design workflow and tools:**
- AI-augmented UX workflow end to end
- Figma Make: what it is, what it isn't, file setup, prompting approach, limitations at scale
- shadcn Figma kit options: Obra, Pietro Schirano, shadcn/studio
- v0 by Vercel: how it differs from Make, Figma import, production-closer code output
- Miro AI Flows and MCP connection to GitHub Copilot
- Design system migration: why Mantine → shadcn matters, how to approach it
- Tiered memory architecture for LLM context management

**Frameworks:**
- 4D Design Framework (Discover, Define, Develop, Deliver) with prioritised activities for my context
- Double Diamond as the underlying model

---

### The Agentic Design System We Designed

A group of agents supporting the human design and development team across the full product design pipeline. Key features:

- **Tiered memory architecture:** Tier 1 (project index, always loaded), Tier 2 (domain documents, loaded on demand), Tier 3 (ephemeral task context)
- **Five agents:** Orchestrator, Discover, Define, Design, Deliver — each with specific owned documents, read documents, and input/output contracts per task
- **Shared format:** All documents are `.md` files with a standard header (document type, owner, tier, status, version, linked agents, linked documents)
- **Markdown as design medium:** structured markdown (tables, nested lists, code blocks) for flows and wireframes using actual shadcn component names; Mermaid available for complex conditional flows when rendered output aids comprehension; component library reference as shared vocabulary
- **Project index:** Spine of the system — project snapshot, agent roster table, domain document registry with owner/tier/status per doc

**Documents designed so far:**
- `project-index.md` — complete, Tier 1, owned by Orchestrator
- All other domain documents listed in registry — structure defined, content not yet created

**Next steps agreed:**
1. Populate project index with real current content
2. Build `component-library-reference.md` first among Tier 2 docs
3. Run one end-to-end test on a real upcoming design task

---

### Working Preferences Noted

- One document at a time — agree template before moving on
- Artefacts preferred over inline markdown for documents (copy button, side panel)
- Set up a Claude Project to host this work — paste context brief as project instruction, build each document as an Artifact within project conversations
- Context brief (`design-brief.md`) already built and downloadable from this conversation — use it as the Project's base context document