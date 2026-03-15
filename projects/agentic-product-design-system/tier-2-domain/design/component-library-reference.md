# Component Library Reference
*Document type: Domain | Owner: Design | Tier: 2*
*Status: Active | Last updated: 14 March 2026 | Version: 1.0*
*Linked agents: Design, Orchestrator, Deliver*
*Linked documents: project-index.md, wireframes.md, user-flows.md*

---

## Introduction
This document defines the shared UI vocabulary for the active project. It aligns the Design agent's wireframing process with the development team's implementation using the **shadcn/ui** library. All wireframes and user flows should use these component names to ensure a high-fidelity handoff and reduce rework.

---

## Component List (shadcn/ui)

- **Button**
  - Description: Standard interactive element for triggers.
  - Use Case: Submitting form edits, cancelling actions, opening modals.
  - Props/Variables: `variant="default|destructive|outline|secondary|ghost|link"`, `size="default|sm|lg|icon"`

- **Input**
  - Description: Single-line text field.
  - Use Case: Entering names, codes, or simple text values.
  - Props/Variables: `type="text|number|email|password"`, `placeholder="string"`

- **Table**
  - Description: A set of data displayed in rows and columns.
  - Use Case: Viewing and managing multiple records in a [Table View].
  - Props/Variables: `header`, `body`, `row`, `cell`, `caption`

- **Select**
  - Description: A dropdown list for selecting a single value from a set.
  - Use Case: Choosing item types, categories, or status transitions.
  - Props/Variables: `options`, `value`, `onValueChange`

- **Checkbox**
  - Description: A control that allows the user to select one or more options.
  - Use Case: Selecting multiple records for bulk actions.
  - Props/Variables: `checked="true|false|indeterminate"`, `disabled="true|false"`

- **Dialog** (Modal)
  - Description: A window overlaid on the primary window, requiring user interaction.
  - Use Case: Confirming destructive actions, editing complex record details without leaving the current view.
  - Props/Variables: `title`, `description`, `footer`

- **Card**
  - Description: A container for grouping related information.
  - Use Case: Individual record summary views, dashboard widgets grouped by status or category.
  - Props/Variables: `header`, `content`, `footer`

- **Badge**
  - Description: A small visual indicator for status or categories.
  - Use Case: Displaying item status or category. Example states: Draft, Live, Expired — replace with your project's status model.
  - Props/Variables: `variant="default|secondary|destructive|outline"`

- **Tabs**
  - Description: A set of layered sections of content, one displayed at a time.
  - Use Case: Switching between filtered views of a dataset (e.g., active, draft, archived).
  - Props/Variables: `defaultValue`, `value`, `onValueChange`

- **Popover**
  - Description: A small overlay that appears when an element is clicked.
  - Use Case: Quick actions menu for a table row, tooltip-like info for complex fields.
  - Props/Variables: `content`, `side="top|bottom|left|right"`

- **Form** / **Label** / **FormControl**
  - Description: A collection of related fields and their labels.
  - Use Case: A [Form View] for detailed record creation or editing.
  - Props/Variables: `name`, `label`, `description`, `error`

- **DatePicker** / **Calendar**
  - Description: A control for selecting a single date or a range of dates.
  - Use Case: Setting start and end dates, scheduling, or any date-ranged fields.
  - Props/Variables: `mode="single|range"`, `selected`, `onSelect`

- **Accordion**
  - Description: A vertically stacked set of interactive headings that each reveal a section of content.
  - Use Case: Organizing complex record metadata into collapsible sections within a form or detail view.
  - Props/Variables: `type="single|multiple"`, `collapsible="true|false"`

- **Switch**
  - Description: A control that allows the user to toggle between on and off states.
  - Use Case: Enabling/disabling features, settings, or notification preferences.
  - Props/Variables: `checked="true|false"`, `onCheckedChange`

- **Toast**
  - Description: A succinct message that provides feedback about an operation.
  - Use Case: Confirming "[Action] completed successfully" or reporting "[Action] failed".
  - Props/Variables: `title`, `description`, `action`, `variant="default|destructive"`

- **ScrollArea**
  - Description: A custom scrollbar for overflow content.
  - Use Case: Wrapping a table or content-dense panel to handle horizontal overflow on smaller screens.
  - Props/Variables: `orientation="vertical|horizontal"`

- **Skeleton**
  - Description: A placeholder to show while content is loading.
  - Use Case: Improving perceived performance during initial data fetches or page transitions.
  - Props/Variables: `className` (for dimensions)

- **Alert**
  - Description: A banner for high-priority messages.
  - Use Case: Warning users about time-sensitive conditions, validation errors, or critical system messages.
  - Props/Variables: `variant="default|destructive"`, `title`, `description`

---

## Domain-Specific Patterns

- **[Table View] (DataTable)**
  - Components Used: `Table`, `Checkbox`, `Badge`, `Popover`, `ScrollArea`.
  - Context: The primary interface for the main user workflow. Must support multi-select, inline status badges, and quick-action popovers for each row.

- **[Form View]**
  - Components Used: `Form`, `Input`, `Select`, `DatePicker`, `Accordion`, `Button`.
  - Context: The detailed view for creating or modifying a record. Complex metadata should be organized within `Accordion` sections.

- **Status Indicator**
  - Components Used: `Badge`.
  - Context: A standardized set of colors mapped to your project's status model. Replace the example states below with your actual states.
    - **[State 1 — e.g. Draft]**: `variant="outline"` (Gray/Secondary)
    - **[State 2 — e.g. Review]**: `variant="secondary"` (Blue/Info)
    - **[State 3 — e.g. Live]**: `variant="default"` (Green/Primary)
    - **[State 4 — e.g. Expired/Archived]**: `variant="destructive"` (Red/Warning)

---

*End of Component Library Reference v1.0*
