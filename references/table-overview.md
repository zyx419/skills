# Page type: table-overview

## Purpose and scope

Use this format for a page whose main evidence is a comparison across many
items: dataset repair progress, experiment coverage, benchmark status, or
before/after outcomes. Use `../assets/table-overview.html` as the starting
layout. It is derived from the user-approved Lognroll dataset overview.

Adapt titles, columns, group names, metrics, and status vocabulary to the
actual subject. Do not force dataset-specific columns onto unrelated tables.
Do not use a bug-fix four-block layout or a large evidence side rail here.
Authored visible content is English; preserve identifiers verbatim.

## Page composition

- One 1280×720 canvas with a compact running header, left-aligned title and
  subtitle, and optional summary figures at the upper right.
- A concise legend above one dominant full-width table. The table occupies
  most of the page. Group header bands, aligned numbers, and restrained row
  colors make the comparison readable.
- Below the table, retain a short scope line and, when useful, one concise
  takeaway. Do not append paragraphs explaining each metric, methodology,
  historical caveat, local verification process, or user instruction by
  default. Put detailed provenance in HTML comments/data or cell tooltips;
  surface a material uncertainty concisely in its relevant cell.
- A short footer fully inside the canvas. Reserve its height, keep each side
  concise, and allow wrapping if necessary. It must not overlap the takeaway
  or touch the lower border. A Git branch/commit footer is not required for
  this page type. Do not present one revision as the source of mixed runs.

## Dataset repair overview: approved column contract

| Column | Display |
|---|---|
| Dataset | Dataset name |
| Log lines | Comma-separated integer |
| Log file size (MiB) | File size with unit clearly named in the header |
| GT templates | Ground-truth template count for the corresponding corpus |
| BEFORE / HISTORICAL STATE | Compact state badge followed by useful historical description |
| AFTER / LATEST VERIFIED STATE | Compact state badge followed by current outcome |
| OBSERVED RESULT | Outcome or the completed-run metrics below |
| STATE | One status symbol |

For OK rows, use `Templates = 15 · Candidates = 1 · Runtime = 8.50 s`.
Templates means the selected template count, Candidates the reported count
of candidate template sets, and Runtime the elapsed run time. Use `−` for a
missing value. Use `GT templates`, not an unexplained `GT T`, and the full
file-size label, not `MiB` alone.

For pending rows, use a short result such as `Full run still unverified`;
do not fill the cell with three unavailable metrics. Prefer `OK` over `DONE`
or `HISTORY`. For historical completed rows, BEFORE can read
`OK · Historical full completion`, while AFTER can read `OK · -`.
Preserve the useful BEFORE description when simplifying AFTER wording.

## Dataset repair overview: grouping and visual semantics

1. Separate dataset families, for example Loghub and original Lognroll.
2. Within each family, group by AFTER status, not historical failure mode.
   Put OK rows first and pending/no-result rows together. Within each subgroup,
   sort by ascending log count.
3. Put single-candidate rows at the bottom of their own family, also sorted
   by ascending log count. Do not move them into a separate cross-family table.
4. Green fill and a green left marker mean **datasets available for scoring**.
   Gray fill and a gray left marker mean **candidate count = 1**. Gray takes
   precedence even if a row is OK. Explain both in the upper legend.
5. Final-column symbols: `○` normal/OK; `×` unresolved bug; `↓` dataset results
   not yet available. The arrow is not restricted to OOM. Keep this distinction
   from any OOM label in BEFORE. Use these meanings consistently in tooltips.
6. Summary figures must agree with the displayed groups and their labels.
   Use `BUG FIXES` for a fix count; do not conflate that with all OK datasets.
   Omit a count if the evidence does not establish what it is counting.

These mappings apply to dataset repair overviews. For other comparison
subjects, adapt the semantics and explicitly label them in the legend.

## Reporting basis

Keep selected template counts, candidate counts, and runtime tied to the
intended reporting basis. Raw exported candidates, deduplicated candidates,
and user-selected candidates can have different counts. Respect an explicit
user-specified reporting basis; preserve the raw source evidence separately
and do not invent missing metrics. Do not silently combine unrelated run
measurements as if they described one run.

When the user says server runs determine final outcomes, local/WSL checks do
not upgrade a pending server result to OK. Local subset completion does not
establish full-dataset completion. Keep these evidence checks in the authoring
workflow; avoid verbose disclaimers on the slide. Actual dataset names,
counts, timings, and overrides from the example are not reusable defaults.

## Typography, spacing, and validation

Use approximately 24 px for the title, 9–10 px for table text and headers,
8–9 px for legends, and 7.6–8 px for a compact footer on the 1280×720 canvas.
Starting column widths for the eight-column dataset table are
10%, 8%, 7%, 5%, 20.5%, 19.5%, 26.5%, 3.5%. Adapt to actual content.
Use roughly 10 px horizontal cell padding, right-align numerical columns,
and slightly larger gutters before the BEFORE and OBSERVED RESULT columns.
Wrap long headers intentionally; keep status badges distinct from their text.

For the sixteen-row example, roughly 4.5 px vertical cell padding fits the
whole page. Rebalance widths and spacing before reducing fonts. Do not clip
content or shrink only the table to conceal overflow; uniform viewport scaling
of the complete slide is allowed. If the required data cannot fit legibly,
raise the page-count tradeoff rather than silently omit rows.

Replace every template placeholder, render with actual content, and check:
all rows included once, group/order rules, metrics and symbols, horizontal
cell overflow, table height, and footer bounds. The footer bottom must remain
above the slide's bottom padding, not merely within scrollHeight. For mixed
decks, namespace this template's styles so its table rules do not alter other
page types. No bug-fix citation chips are required unless actually used.
