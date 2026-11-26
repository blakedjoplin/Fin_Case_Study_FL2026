---
type: log
owner: Both
tags: [fin3010, ai-errors]
---

# AI Error Log

The post needs **one** specific thing AI got wrong or oversimplified, and how we caught it. Log every candidate here; pick the best one for the post.

| # | What AI / a source said | What's actually true | How we caught it | Use in post? |
|---|---|---|---|---|
| 1 | "Big Tech will spend $725B in 2026" (brainstorm) vs. $630B, $650B, $700B, $730B, $745B in other sources | All can be "right" — totals depend on **when** they were compiled (guidance rose every quarter) and **what's counted** (cash capex vs. incl. finance leases; Microsoft fiscal vs. calendar year) | Compared four dated articles, then went to each company's own Q3 2026 release | ⬜ strong candidate |
| 2 | Some outlets print Azure Q3 revenue as "$33.2B" | Microsoft reports Azure **growth %**, not dollars (to confirm in the FY26 Q1 release) — the dollar figure appears to be an estimate presented as fact | Searched the primary release for an Azure dollar line | ⬜ strong candidate — confirm first |
| 3 | First-pass model compared $730B capex directly to annual cloud revenue | That's the Apex VP-of-Marketing mistake: ignores timing, required return, and that revenue ≠ cash flow | Rebuilt as a break-even annuity (PMT) and hand-checked on a BA II Plus | ⬜ good tie-in to the case |
| 4 | | | | |

## Prompts that worked / didn't
| Prompt | What happened | What we changed |
|---|---|---|
| | | |
