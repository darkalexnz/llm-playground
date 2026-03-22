# design-system-rules.md
<!-- LLM-facing design constitution. Read this before writing or modifying any UI code. This file enforces visual consistency across all AI-assisted UI work. -->
<!-- Referenced in CLAUDE.md. Updated by designer. Consumed by AI agents and developers. -->

---

## Purpose

This file is the single source of truth for visual and component rules.
When building UI, the LLM must follow these rules exactly.
Do not invent tokens, create one-off styles, or use raw values.

---

## Colour Tokens

<!-- Map semantic names to their token variables. No raw hex values in code. Ever. -->

```css
/* tokens.css — use these variables, never hardcode values */

--color-background:       hsl(0 0% 100%);
--color-foreground:       hsl(222 47% 11%);
--color-primary:          hsl(221 83% 53%);   /* Brand blue */
--color-primary-hover:    hsl(221 83% 45%);
--color-secondary:        hsl(210 40% 96%);
--color-muted:            hsl(215 16% 47%);
--color-muted-foreground: hsl(215 16% 60%);
--color-destructive:      hsl(0 72% 51%);
--color-border:           hsl(214 32% 91%);
--color-surface:          hsl(0 0% 98%);
--color-surface-raised:   hsl(0 0% 100%);

/* Status colours */
--color-success:          hsl(142 71% 45%);
--color-warning:          hsl(38 92% 50%);
--color-info:             hsl(199 89% 48%);
```

**Rule:** Every `color:`, `background:`, `border-color:` must reference a token. No raw values.

---

## Spacing Scale

<!-- Tailwind scale — use these class values only. -->

| Token | Value | Tailwind class |
|---|---|---|
| xs | 4px | `p-1`, `gap-1` |
| sm | 8px | `p-2`, `gap-2` |
| md | 16px | `p-4`, `gap-4` |
| lg | 24px | `p-6`, `gap-6` |
| xl | 32px | `p-8`, `gap-8` |
| 2xl | 48px | `p-12`, `gap-12` |

**Rule:** No arbitrary spacing values like `p-[13px]`. Use the scale.

---

## Typography

<!-- Font usage, sizing, and weight rules. -->

- **Font family:** `font-sans` (system stack) for UI. `font-mono` for code/data values only.
- **Heading sizes:** `text-2xl font-semibold` (page), `text-xl font-medium` (section), `text-base font-medium` (subsection)
- **Body:** `text-sm` for dense UI, `text-base` for reading contexts
- **Muted / labels:** `text-sm text-muted-foreground`
- **Never use:** `text-xs` for body content — accessibility minimum is `text-sm`

---

## Component Rules

### Buttons

```tsx
// Primary action — one per view
<Button variant="default">Save offer</Button>

// Secondary / supporting actions
<Button variant="outline">Cancel</Button>

// Destructive
<Button variant="destructive">Delete</Button>

// Ghost — for icon buttons and low-emphasis actions
<Button variant="ghost" size="icon"><Icon /></Button>
```

**Rules:**
- Maximum one `variant="default"` (primary) button per view or modal
- Destructive actions require a confirmation dialog — never fire directly
- Loading state: always disable the button and show a spinner during async actions

---

### Forms

```tsx
// Always use FormField + FormControl pattern from shadcn/ui Form
<FormField
  control={form.control}
  name="fieldName"
  render={({ field }) => (
    <FormItem>
      <FormLabel>Field label</FormLabel>
      <FormControl>
        <Input placeholder="Placeholder text" {...field} />
      </FormControl>
      <FormDescription>Helper text if needed</FormDescription>
      <FormMessage /> {/* Validation error — always include */}
    </FormItem>
  )}
/>
```

**Rules:**
- Never build custom form inputs — always use shadcn/ui form primitives
- Every field must have a `FormLabel` — never label-less inputs
- Always include `<FormMessage />` for validation feedback
- Required fields: mark with `*` in the label, not just validation logic

---

### Tables

```tsx
// Use shadcn Table for all tabular data
<Table>
  <TableHeader>
    <TableRow>
      <TableHead>Offer name</TableHead>
      <TableHead>Status</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    <TableRow>
      <TableCell>iPhone 16 Pro</TableCell>
      <TableCell><Badge variant="outline">Draft</Badge></TableCell>
    </TableRow>
  </TableBody>
</Table>
```

**Rules:**
- Always include empty state (zero rows) — use a centred message, not an empty table body
- Loading state: use skeleton rows, not a spinner over the table
- Action columns go last, right-aligned

---

### Status and Feedback

```tsx
// Status badges — map to these variants only
<Badge variant="default">Live</Badge>      // Active/published
<Badge variant="secondary">Draft</Badge>  // In progress
<Badge variant="outline">Pending</Badge>  // Awaiting action
<Badge variant="destructive">Error</Badge> // Failed/blocked
```

**Rules:**
- Never use colour alone to convey status — always pair with a label
- Toast notifications: use `sonner` via shadcn/ui toast — success, error, info only
- Page-level errors: use `Alert` component, not inline text

---

## Layout Patterns

### Page structure

```tsx
<div className="flex flex-col gap-6 p-6">
  {/* Page header */}
  <div className="flex items-center justify-between">
    <div>
      <h1 className="text-2xl font-semibold">Page title</h1>
      <p className="text-sm text-muted-foreground">Supporting description</p>
    </div>
    <Button>Primary action</Button>
  </div>

  {/* Content */}
  <Card>
    <CardHeader>
      <CardTitle>Section title</CardTitle>
    </CardHeader>
    <CardContent>
      {/* Content here */}
    </CardContent>
  </Card>
</div>
```

### Modal / Dialog structure

```tsx
<Dialog>
  <DialogContent className="max-w-lg">
    <DialogHeader>
      <DialogTitle>Action title</DialogTitle>
      <DialogDescription>Clarifying description</DialogDescription>
    </DialogHeader>
    {/* Form or content */}
    <DialogFooter>
      <Button variant="outline">Cancel</Button>
      <Button>Confirm</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

---

## What Not To Do

<!-- Explicit prohibitions. These are the most important lines in this file. -->

- ❌ Do not use `className="bg-blue-500"` — use `bg-primary` or a token variable
- ❌ Do not create wrapper components that re-implement existing shadcn components
- ❌ Do not use arbitrary Tailwind values: `w-[347px]`, `mt-[13px]`
- ❌ Do not add `style={{}}` inline styles
- ❌ Do not build custom dropdowns, modals, or tooltips — use shadcn/ui equivalents
- ❌ Do not use `text-xs` for anything a user needs to read
- ❌ Do not add new icon libraries — use `lucide-react` only

---

## New Component Protocol

If a required UI pattern doesn't exist in shadcn/ui:
1. Flag it to the designer before building
2. If approved to proceed, build it in `src/components/quarantine/`
3. Add it to the Quarantine section of `component-library-reference.md`
4. Tag the file with `// @quarantine — pending designer review`
5. Do not import quarantined components outside the feature that needs them

---
<!-- Version: 0.1 | Owner: UX Designer | Last updated: [date] | Referenced by: CLAUDE.md -->
