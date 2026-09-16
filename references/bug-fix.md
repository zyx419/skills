# Page type: bug-fix (bug correction)

## Scope

Apply this specification only to a page explaining a concrete bug and its
correction: symptom, root cause, patch, and observed output/verification.
A proposed correction may use this format if its unimplemented or unverified
status is explicit. It does not define the format of other page types.

All details below are local to `bug-fix`: the content blocks, evidence layout,
font sizes and density, English copy, comparison colors, text budget, and
`<branch name> · <git cid>` footer. Do not promote them to deck-wide defaults
or apply them to another page merely because it appears in the same deck.
The associated starter template is `../assets/template.html`.

## The governing principle

Prose describing a bug is almost always weaker than the bug itself. So the job
is to find the smallest concrete artifact that makes the defect self-evident,
put it at the largest size on the page, and let sentences do only the work the
artifact cannot do (why it happens, what it costs).

Two failure modes to avoid, both common:

- **Burying the key fact.** If the single most important thing on the slide
  (usually a one-token transformation, or one changed line) is not immediately
  findable, the slide has failed regardless of how complete it is.
- **Showing two long strings side by side and expecting the reader to diff
  them.** The eye cannot do this. Always mark the divergence.

## Workflow

1. **Gather.** From the conversation, extract: what was expected, what actually
   happened, why, the fix (if any), and how it was verified. Ask only for what
   is genuinely missing and load-bearing — usually the verification numbers.
   If the fix or verification does not exist yet, say so on the slide
   (block 3 becomes a proposed fix, block 4 becomes expected impact); do not
   invent results.
2. **Minimize.** Reduce the failing case to the shortest input that still
   reproduces it. This is the highest-value step — see below.
3. **Fill the template** at `../assets/template.html`, replacing every placeholder.
4. Follow the HTML delivery rules in `../SKILL.md`.
5. Validate evidence references and overflow on each bug-fix page. In a mixed
   deck, apply the four-block requirement only to pages classified `bug-fix`.
   Check the combined HTML navigation and rendering separately.

## Minimizing the failing case

Take the real artifact and strip everything that is not required to reproduce.

```
Real:     hdfs://deimos26:9000/tmp/hadoop-yarn/staging/james/.staging/
          job_1514189261604_0001/job.jar(->/tmp/hadoop-james/nm-local-dir/…)
Minimal:  a.jar(->b)   →   .*
```

The minimal form goes in block 2 as the mechanism. The real form still belongs
on the slide (in block 1) because it proves the bug is real and not a toy — but
it is presented with the divergence marked, not as a wall of characters.

If the minimal example needs more than about 60 characters, or the mechanism
needs more than four rows in the rules table, the reduction is not finished.

## Layout: 2/3 argument column, 1/3 evidence rail

The page is two columns, not a quadrant grid. Blocks 1–4 stack vertically down
the **left two-thirds** in reading order, so the argument runs top to bottom the
way a person actually reads. The **right third** is an evidence rail.

A quadrant grid forces every block to the same size regardless of how much it
deserves, and it breaks reading order — the eye has to jump. The stacked column
lets block 1 be tall and block 3 be four lines, which is usually the truth.

### What goes in the left column

Only what carries the argument: the divergent strings, the offending line, the
diff, the before/after output. Keep each block short enough that all four fit
at the specified font sizes without clipping.

### What goes in the evidence rail

Material that supports the argument but would bloat it — this is where you put
things rather than cutting them:

- the minimal transformation table (`.*)` → `.*`), keyed to block 2
- **untruncated** raw artifacts whose folded form appears on the left, so a
  reviewer can check the real string against their system
- a screenshot of the failing run or test output, embedded as a base64 data URI
- affected file paths, config values, environment details

The rail is reference, not narrative. Nobody should need to read it to follow
the bug — it exists so the left column can stay short and so a skeptical reader
has somewhere to look.

### The reference contract

The left column is the subject; the rail is subordinate to it. That relation
has to be visible on the page, not merely intended, so the two sides are bound
by explicit citation:

- Every rail item carries a label — `<span class="id">A</span>` in its caption,
  lettered A, B, C… in source order.
- Wherever the left column depends on a rail item, it cites the label with
  `<span class="ref">A</span>`, placed in the block heading when the whole
  block leans on it, or after a row label when only that row does.
- **Every rail item must be cited at least once.** An uncited item is material
  no part of the argument needs; delete it, or write the citation that makes it
  load-bearing. This is the rule that keeps the rail from silently becoming a
  dumping ground.
- **Every citation must resolve.** A `[C]` with no C sends the reader hunting
  for something that isn't there, which costs more attention than the item
  would ever have saved.

Verify with the bundled script rather than by eye — it is easy to delete a rail
item and forget the citation still pointing at it:

```bash
python3 <skill-directory>/scripts/check_refs.py <output>.html
```

It prints the labels on each side and fails on dangling citations, uncited
items, and duplicate labels. Fix what it reports before presenting the file.
Note that a rail item can be cited from several places; only zero is a defect.


## The four blocks

Keep this order and these roles. Write the headings in English; the semantics
are fixed.

| # | Role | Contains |
|---|------|----------|
| 1 | **Symptom** | Expected vs. actual, as literal artifacts, divergence highlighted |
| 2 | **Root cause** | The offending line of code, plus one sentence on the mechanism |
| 3 | **Fix** | A code diff (`-` / `+`). Never prose describing a code change. |
| 4 | **Before / after output** | The actual artifact the system emits, pre-fix and post-fix |

### Block 4 shows output, not judgement

Block 4 exists to prove the patch changed the thing it claimed to change. That
proof is the **literal output** — the template string, the log line, the return
value — as it looked before the fix and as it looks after.

What kills this block is substituting a verdict for the artifact.
`BEFORE: FAIL / AFTER: PASS`, `wrong → correct`, `merged → separated` are
blocks 1 and 3 restated backwards; a reader who has read those learns nothing.
`PASS`, `FAIL`, `OK`, `fixed`, `broken` are therefore banned as content here.

Resist the other temptation too: an "impact / scope" block full of counts and
metric deltas is worse than useless before those numbers exist. Empty cells
awaiting measurement occupy the most valuable quarter of the page and say
nothing. If you have real numbers, one of them can ride along as a caption
under the after-output. If you do not, the before/after artifact alone is
sufficient — it is evidence either way.

Use the same visual grammar as block 1: monospace, divergence highlighted, red
for the broken output and green for the corrected one. The reader should be
able to compare block 1 and block 4 at a glance and see the defect close.

## Marking divergence — the important part

Every string comparison in block 1 uses these spans:

- `<span class="same">` — identical portion, rendered gray so it recedes
- `<span class="fold">…</span>` — a long identical prefix, collapsed entirely
- `<span class="bad">` — the wrong part (red)
- `<span class="good">` — the correct/expected part (green)
- `<span class="mark">` — the trigger character(s) that cause the bug (amber)

Collapse aggressively. If two strings share a 70-character prefix, that prefix
is noise and should become `<span class="fold">…</span>` or a short stub.

```html
<!-- weak: reader must scan 90 chars to find the difference -->
<div class="code">hdfs://deimos26:9000/tmp/hadoop-yarn/staging/james/.staging/job_…/job.splitmetainfo</div>

<!-- strong: prefix folded, divergence and trigger both marked -->
<div class="code"><span class="fold">…/job_1514189261604_0001/</span>job.<span class="good">splitmetainfo</span></div>
<div class="code"><span class="fold">…/job_1514189261604_0001/</span>job.jar<span class="mark">(</span>-&gt;<span class="bad">/tmp/…/job.jar</span><span class="mark">)</span></div>
```

## Large-screen typography and density

Use the technical pages of `crude two-part MDL (3).pdf` as the default
reference, rather than taking the introductory page's typography as the deck
standard. PDF pages are 720×405 pt. Compare at the same displayed dimensions:
on a 1280×720 canvas, font_px = PDF_font_pt × 1280 / 720.

Measured reference scales:
- Pages 13–14: main title approximately 17.8 px; small text mostly 7.1–10.7 px.
- Pages 15–18: main title approximately 21.3 px; dense table text 5.3–8.9 px.
- Page 3: section text approximately 14.2 px; explanatory/code text 10.7 px.
- Page 1 is a different style: title 44.8 px and body 17.8 px. Do not use this
  introductory-page scale for technical slides unless explicitly requested.

For a technical bug report, default to a 21.3 px main title, 12.4 px section
headings, 10.7 px prose/code/diffs, and 8.9 px supporting evidence and metadata.
Use 1.4 body line height, a compact 36 px header, 24 px vertical / 50 px
horizontal page padding, and 10 px between blocks. Use the smaller table
sizes only when following an explicitly selected dense reference page.
These values are a technical-page adaptation, not an exact copy of one page.
A large presentation screen alone is not a reason to enlarge the fonts.

If a supplied deck contains different styles, identify the reference page
before declaring a match. When the user has not selected a page, disclose
which technical-page style is being used. Compare rendered slides with the
reference at equal canvas size, checking actual text height, title width,
weight, and content footprint; nominal font size alone is insufficient.

- Increase useful content density with compact tables, aligned comparisons,
  and short explanations next to code. Use `.pair` for expected/actual or
  before/after rows when both artifacts fit their half-widths; otherwise stack
  them. Fill available space with relevant evidence, not repeated prose.
- The 2:1 argument/rail split is the default. Adjust it for long code or tables
  while preserving the four-block reading order and the rail citation contract.
  Avoid equal-height cards that leave large empty areas around short content.
- Do not shrink the entire slide or hide overflow to make it fit. First reduce
  redundant text and decorative spacing, then reorganize comparisons and fold
  shared log prefixes. Keep the main text at the sizes above.
- Render a populated slide at 1280×720 and inspect wrapping, title clearance,
  footer position, and every panel for overflow. The template marks
  `data-overflow="true"` and logs a warning if content does not fit; fix it
  before delivery. A template with placeholders is not a layout check.

## Text budget

- Title: one line, states the defect, not the topic.
  Good: `Tokens ending in ) or ] collapse to a bare .* wildcard`
  Weak: `Lognroll bug fix`
- Each `.note` paragraph: **two lines maximum**. Needing more means block 2's
  example is not minimal enough.
- No nested bullet lists anywhere. The four blocks are the structure; adding
  hierarchy inside them recreates the problem this format exists to solve.
- Bold (`<b>`) at most one phrase per block, on the causal claim.

## Bug-fix footer

For a bug-fix slide, set the source/footer-left text to exactly
`<branch name> · <git cid>` (for example, `fix/parser · 6be0fb3`).
Use the relevant branch name and the abbreviated commit ID of the fix shown
on that slide, verified from Git or explicit user-provided metadata. Do not
substitute the current HEAD when presenting a different fix, or infer a
historical branch name from a commit alone. If either value is unavailable,
mark that field as `uncommitted` or `unknown`, as applicable.

This replaces footer prose such as `Evidence: Git patch + <report>.html ·
historical results, not rerun`. Keep necessary verification limits beside
the verification evidence, rather than in this footer. Use each slide's own
fix commit in a multi-page report. Preserve branch names verbatim.

## Language and fidelity

Write all authored slide content in English, even when the request or source
material is in another language. This includes titles, headings, labels
(`EXPECTED` / `ACTUAL` / `BEFORE` / `AFTER`), explanations, evidence captions,
and footers. Set the generated HTML document language to `en`.

Preserve quoted logs, code, template strings, identifiers, and other raw
evidence in their original language; explain them in English when needed.

Never alter the user's actual log text, template strings, identifiers, or code
to make them tidier. Truncation with `…` is fine; rewriting is not — a reviewer
may be checking these against the real system.

## Technical constraints

- Single file, no CDN links, no external fonts or images. It must render
  offline, survive being emailed, and paste cleanly into a deck.
- Fixed 1280×720 canvas. Preserve the font hierarchy above; resolve any
  overflow flagged by the template before exporting or presenting.
- If the user supplies a screenshot as evidence, embed it as a base64 data URI
  inside block 4 so the file stays self-contained.
