---
type: concepts
owner: Both
status: pick one hero + one webpage
tags: [fin3010, deliverable]
---

# Deliverable Concepts

The rubric wants **a visual in the post** *and* **a link to a webpage**. So the deliverable is two pieces:

1. **Hero chart** (PNG in the post) — the one picture a recruiter sees while scrolling.
2. **Tool page** (link in the post) — an interactive calculator anyone can play with.

## Concept A — "The Break-even Dial" (tool page) ⭐ recommended webpage
An interactive one-page calculator.
- **Inputs (sliders):** capex ($B, default 730), required return (6–14%), server useful life (3–7 yrs), server share of capex (0–100%), building life (15–40 yrs), EBITDA margin.
- **Outputs (big numbers):** break-even annual cash flow; incremental revenue needed per year; side-by-side with Q3 2026 cloud revenue run rate.
- **Small print:** sources + "as of Oct 2026 earnings" + "back-of-the-envelope, not a forecast."
- **Why:** lets the reader test our assumptions — strong "show your work" signal.

## Concept B — "The Gap Chart" (hero chart) ⭐ recommended visual
A horizontal bar chart: break-even cash flow under 3–4 scenarios (e.g., 4-yr servers @12%, 6-yr @10%, blended @10%, 25-yr buildings @8%) with a reference line for today's cloud operating income run rate.
- **Why:** one glance answers the question. Reads well on a phone.

## Concept C — "Life vs. Return heatmap" (secondary visual)
Grid: required return (rows) × useful life (columns), each cell = break-even CF. Highlights the column the companies actually use (5–6 yrs) and the column a skeptic would use (3–4 yrs).
- **Why:** makes the depreciation-life point visible — the most interesting finding.

## Concept D — "Annotated earnings-release screenshot" (verification visual)
A cropped screenshot of one primary source with the capex line circled, next to the number a news article / the AI gave us.
- **Why:** doubles as proof for the "where AI got it wrong" section.

## Decision
- [ ] Hero chart: B (default) or C
- [ ] Webpage: A
- [ ] Optional second image: D

Claude builds A and B from the verified numbers in [[04 Data Sources & Verification Log]]; we review every output against [[05 Model — Break-even Cash Flow]].
