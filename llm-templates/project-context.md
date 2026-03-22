# Project Context
*LLM input document — updated March 2026*

---

## The Project

- **What it is:** Internal web app replacing a spreadsheet-and-email process for managing promotional device and product offer lifecycles — from brand partner negotiation through to live on website and CRM.
- **Org:** New Zealand telco
- **Stack:** React, TypeScript, Tailwind, shadcn, Azure (dev/test/staging/prod), Git/GitHub, Azure DevOps
- **Stage:** Pre-launch MVP. Three months of discovery and build completed. DeviceOps UAT done. Creative and Catalogue flows in progress.
- **Process:** Agile, two-week sprints. Constant battle of quick delivery vs considered design and dev. Spec-driven AI development is heavy — new features are scoped over days or weeks, then dev takes roughly two days.

---

## The Team

| # | Role | Hours/week | Top focuses |
|---|---|---|---|
| 1 | Product Owner | 40 | Team management, discovery, stakeholder alignment |
| 2 | Business Analyst | 40 | Discovery, documentation, some development |
| 3 | CX Designer | 16 | Discovery, documentation |
| 4 | UX/UI Designer (me) | 40 | Discovery, documentation, UX/UI and handoff |
| 5–8 | Full Stack Engineer ×4 | 30–40 each | Development, PR review, solution design |
| 9–10 | Data Engineer ×2 | 30–40 each | Development, PR review, solution design |
| 11 | AI Engineer ×1 | 40 | Development, PR review, solution design |
| 12 | Solution Architect | 30 | System leadership, CI/CD, planning |

---

## Core Feature

An intelligent editable offer table/editor. Offers are created, enriched, and approved as they move through a pipeline toward publication.

### Offer complexity spectrum

- **High:** Pay monthly device offers (plan types, discounts, interest-free terms, trade-in boosts, bundled gifts)
- **Medium:** Accessories and general merchandise
- **Bespoke:** New product launches with custom field combinations

### Primary MVP users

DeviceOps (create and own offer data), Creative (add content), Catalogue (publish to web and CRM)

### Broader stakeholders (post-MVP)

Legal, Finance, Brand, Partnerships, external agencies

---

## Project's Real Problems

- **Complex, variable data model.** Offer types differ significantly in structure. The editor must handle this without overwhelming users or fragmenting the experience.
- **Multi-team, multi-role pipeline.** DeviceOps, Creative, and Catalogue each touch offers at different stages with different permissions and needs. Workflow handoff between these teams is a core UX and logic challenge.
- **Change communication at speed.** The old process broke down on last-minute changes. The new system needs to make change visibility reliable and low-effort.
- **AI integration undefined.** Mandate exists but no clear brief. Natural candidates: field validation, change conflict detection, auto-population from historical data, offer completeness checking.
- **Post-MVP scope risk.** Broader stakeholders (Legal, Finance, etc.) not yet in scope. Their eventual inclusion will stress the current data model and workflow design.

---

## Open Questions — The Project

- What are the known gaps from DeviceOps UAT and the current remediation plan?
- Have Creative and Catalogue workflows been designed and validated yet?
- How will offer type variability be handled in the editor UI — one adaptive form, multiple templates, or something else?
- What is the plan for migrating the Figma design system from Mantine to shadcn-aligned components?
- What does success look like for AI integration at MVP specifically?
