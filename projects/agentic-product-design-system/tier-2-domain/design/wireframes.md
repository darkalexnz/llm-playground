# Wireframes
*Document type: Domain | Owner: Design | Tier: 2*
*Status: Not started | Last updated: 15 March 2026 | Version: 0.1*
*Linked agents: Design, Deliver, Orchestrator*
*Linked documents: project-index.md, problem-statements.md, personas.md, component-library-reference.md, user-flows.md, feasibility-notes.md*

---

## Purpose

Structural layout specifications for all screens and states. Written in Markdown using shadcn/ui component names exclusively (see `component-library-reference.md`). Each wireframe documents layout, component usage, and all relevant states.

---

## Wireframes

*Add one section per screen or feature. Use the format below. Reference problem statements and personas explicitly.*

---

### [Screen / Feature Name]

**Solves:** *Link to problem statement(s) in problem-statements.md — e.g. PS-01*
**Primary persona:** *Link to persona in personas.md*
**Status:** Draft / In review / Approved

#### Layout

*Describe the screen layout in structured Markdown. Use exact shadcn/ui component names from component-library-reference.md. Nest components to reflect visual hierarchy.*

```
[Page layout]
  ├── [Component] — purpose / label / key props
  ├── [Component] — purpose / label / key props
  │   └── [Sub-component] — purpose
  └── [Component] — purpose
```

#### States

*Document every meaningful UI state for this screen. Use the table below.*

| State | Trigger | Visual change | Notes |
|---|---|---|---|
| Default | Page load | *Describe layout* | |
| Loading | Data fetch in progress | Skeleton components replace content | Use shadcn Skeleton |
| Empty | No data returned | Empty state illustration + CTA | |
| Error | API error / failed validation | Alert component with error message | Use shadcn Alert (destructive) |
| Disabled | *Condition* | *Visual* | |

#### Interaction notes

*Any interaction detail that isn't self-evident from the layout — hover states, animations, keyboard navigation, etc.*

#### Open questions

*Unresolved design decisions for this screen*

<!-- example — delete before use
### [Screen Name] — [View Type, e.g. List View / Form View / Detail View]

**Solves:** [PS-01 — reference your problem statement]
**Primary persona:** [User Type A]
**Status:** Draft

#### Layout
```
[Page]
  ├── PageHeader — "[Page Title]" + Button ([Primary action])
  ├── Tabs — "[Tab A]" | "[Tab B]" | "[Tab C]"
  ├── DataTable (shadcn Table)
  │   ├── TableHeader — columns: [Record Name] / [Category] / [Status] / [Owner] / [Last Updated] / Actions
  │   ├── TableBody — one TableRow per record
  │   │   ├── Badge (status) — replace with your project's status model: [Status A]=outline, [Status B]=secondary, [Status C]=default
  │   │   └── DropdownMenu (Actions) — [Primary action] / [Secondary action] / [Destructive action]
  │   └── TableFooter — pagination (Button prev/next + Select rows-per-page)
  └── Sheet (detail panel, slides in on row click)
```

#### States
| State | Trigger | Visual change | Notes |
|---|---|---|---|
| [Default] | Page load | Table populated with records | |
| [Loading] | Initial fetch | Skeleton rows (5 rows) | |
| [Empty] | No records match filter | "No [records] found" + Button ([Primary action]) | |
| [Error] | API failure | Alert (destructive) above table | |
| Row selected | Checkbox click | Row highlight + bulk action bar appears | |
-->

---

*Add additional wireframe sections above this line.*

---

*End of Wireframes v0.1*
