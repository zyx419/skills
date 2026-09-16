---
name: bug-one-pager
description: Create self-contained HTML presentation previews for technical reports, choosing a format per page. Use for bug-fix reports and table overviews comparing datasets, experiments, runtime states, or before/after results, including multi-page decks mixing these formats. Deliver HTML by default; export other formats only when explicitly requested.
---

# Bug one-pager

Produce a self-contained HTML presentation. Choose the detailed format by
**page type**, not once for the whole deck. This skill defines `bug-fix` and `table-overview` page types. A deck may mix
them; choose each page independently from its communication purpose.

## Shared delivery contract

- Deliver one HTML preview file by default. Use a single 16:9 page unless the
  user requests multiple pages; then place those pages in the same HTML file
  with previous/next buttons and keyboard navigation.
- In a repository, write to `reports/` unless the user names another location.
  Otherwise use an available writable output directory. Return a clickable
  HTML link.
- "PPT", "slide", and "PPT look" describe the visual presentation format.
  Generate PPTX, PDF, or image exports only if the user explicitly requests
  those file formats. Do not add export buttons or export instructions by
  default.
- Keep the HTML self-contained and usable offline. Check navigation and
  render every populated page for clipping and overflow before delivery.

These shared delivery rules do not establish a shared content layout, font
hierarchy, heading set, language rule, or footer format. Those details belong
to the selected page specification.

## Page-type registry

| Page type | Status | When it applies | Specification and template |
|---|---|---|---|
| `bug-fix` (bug correction) | Defined | A concrete bug, its cause, correction, and output/verification | [Bug-fix specification](references/bug-fix.md); `assets/template.html` |
| `table-overview` (table summary) | Defined | Compare many datasets, experiments, or items by common dimensions; emphasize overall progress or status | [Table-overview specification](references/table-overview.md); `assets/table-overview.html` |

All other page types are **not yet defined**. Do not invent their permanent
formats or create placeholder specifications now. Add them separately when
the user provides their requirements. Do not rename the skill or create specifications for hypothetical future types.

## Select a format for each page

1. Identify each requested page's purpose from the user's request and source
   material. Pages in the same deck may have different types.
2. Choose `table-overview` when the central question is "which items work,
   fail, improve, or remain pending?" Read `references/table-overview.md` and
   use `assets/table-overview.html`. Choose `bug-fix` when the central question
   is "what defect occurred, why, and how was it corrected?" Read
   `references/bug-fix.md` and use `assets/template.html`. Explicit user choice
   takes precedence. A repair overview can therefore be a table-overview even
   though it discusses bugs. Load only specifications needed for this request.
3. For an undefined page type, do not borrow the bug-fix format automatically.
   Follow explicit formatting instructions in the current request; if a
   missing format choice materially affects the result, ask a focused
   question while continuing any independently specified pages. An ad hoc
   page does not become a new skill convention without the user's request.
4. In a mixed deck, validate each page against its own specification and the
   shared HTML delivery contract. In particular, do not impose the bug-fix
   four-block structure or Git footer on other page types.

## Current bug-fix contract at a glance

The authoritative details are in [references/bug-fix.md](references/bug-fix.md).
It defines the symptom → root cause → fix → output/verification sequence,
evidence and comparison presentation, typography and density, English authored
content, and the footer **`<branch name> · <git cid>`**. These details belong to `bug-fix` only; do not impose them on table-overview pages.

## Table-overview contract at a glance

Use one dominant comparison table, compact summary figures and an English
legend, with short scope and takeaway text below. For dataset repair status,
group by dataset family, then AFTER status, and sort by log count within each
status group. Single-candidate gray rows come last within their own family.
The full rules and adaptable columns are in
[references/table-overview.md](references/table-overview.md).
