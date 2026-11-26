---
type: plan
owner: Blake
updated: 2026-11-26
tags: [fin3010, plan]
---

# Project Plan

**Goal:** a public webpage (interactive break-even calculator) + one hero chart, and two LinkedIn posts (one each) live by **Wed Dec 2, 11:59 PM**.

**Effort:** ~6–8 hrs of build/verify for the pair, plus ~1–2 hrs each to write the post.

## Workstreams and owners
| Workstream | Owner | Output |
|---|---|---|
| A. Capex data (4 companies, 2026 guidance) | Partner | Rows in [[04 Data Sources & Verification Log]] |
| B. Cloud revenue + operating income (Q3 2026) | Blake | Rows in [[04 Data Sources & Verification Log]] |
| C. Useful-life notes from 10-Ks | Partner | Rows in [[04 Data Sources & Verification Log]] |
| D. Model + hand-check with financial calculator | Blake | [[05 Model — Break-even Cash Flow]] |
| E. Tool page + hero chart (Claude builds, we review) | Blake | Webpage link + PNG in `assets/` |
| F. AI error log | Both | [[07 AI Error Log]] |
| G. Posts | Each writes own | [[08 LinkedIn Post Outline]] → our own drafts |

## Schedule
| Day | What | Done when |
|---|---|---|
| **Thu 11/26** | Pick idea, plan, concepts | This vault is pushed ✅ |
| **Fri 11/27** | Pull data (A, B, C) straight from earnings releases / 8-Ks / 10-Ks — **not** from news articles | Every row has a primary-source link |
| **Sat 11/28** | Build model (D). Check one scenario by hand on a BA II Plus / Excel `PMT` | Hand number = model number |
| **Sun 11/29** | Build tool page + hero chart (E). Claude writes the code; we test sliders and check 3 outputs against the model | Webpage link works logged-out |
| **Mon 11/30** | Each of us drafts our own post from the outline (G). Fill AI error log (F) | Two drafts, 300–600 words |
| **Tue 12/1** | Swap drafts, typo pass, re-verify every number in the posts | Every number ✅ in the log |
| **Wed 12/2** | Post on LinkedIn, tag Prof. Painter + SLU Finance, credit each other, submit URLs on Canvas | Both URLs on Canvas before 11:59 PM |

## Definition of done (maps to the 40-pt rubric)
- [ ] Post opens with the question and ties it to the Unit 6 case (VP of Marketing's "$150M in vs $100M out" mistake ↔ comparing AI revenue to capex)
- [ ] Names the AI tool and the specific prompts/iterations
- [ ] Hero chart + link to the tool page
- [ ] One specific AI error and how we caught it
- [ ] What's next
- [ ] Tags + partner credit
- [ ] Zero unverified numbers

## Risks
- **Numbers move.** Capex guidance changed every quarter in 2026. Freeze our inputs on a date ("as of Q3 2026 earnings, Oct 2026") and say so in the post.
- **Apples vs. oranges.** Fiscal vs calendar years (Microsoft's FY ends June), cash capex vs capex incl. finance leases, Meta has no cloud segment. Document every choice in [[05 Model — Break-even Cash Flow]].
- **Overclaiming.** This is a back-of-the-envelope NPV, not a forecast. Say so.
- **Holiday weekend.** Fri–Sun are the build days; if we slip, cut the tool page to a static chart + table (still meets the rubric).
