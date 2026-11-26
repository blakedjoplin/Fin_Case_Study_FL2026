---
type: log
owner: Both
as_of: "Q3 2026 earnings (late Oct 2026)"
tags: [fin3010, data, verification]
---

# Data Sources & Verification Log

**Rule:** a number goes in a post only if `Verified` is ✅ — meaning one of us opened the **primary source** (earnings release, 8-K Ex. 99.1, 10-Q/10-K, or call transcript) and saw the number ourselves. News articles are for leads only.

Status key: ⬜ not checked · 🟡 lead from news, not yet in primary source · ✅ verified in primary source · ❌ wrong / doesn't exist

## A. 2026 capex guidance (owner: Partner)
| Company | Lead figure | Basis (cash? incl. finance leases? CY or FY?) | Lead source | Primary source to check | Verified |
|---|---|---|---|---|---|
| Amazon | ~$220B | cash capex, CY2026 | walnutinvest.com tracker quoting Oct 29 release | Q3 2026 earnings release (ir.aboutamazon.com) | 🟡 |
| Alphabet | $195–205B | CY2026 | walnutinvest.com quoting Oct 28 call | Q3 2026 earnings call transcript (abc.xyz/investor) | 🟡 |
| Meta | $135–145B | incl. finance lease principal? — check | walnutinvest.com quoting Oct 21 | Q3 2026 earnings release (investor.atmeta.com) | 🟡 |
| Microsoft | ~$170B | **calendar** 2026 (FY ends June) | walnutinvest.com quoting Oct 28 call | FY26 Q1 earnings call transcript (microsoft.com/investor) | 🟡 |
| **Total (midpoints)** | **~$730B** | mixed definitions | sum of above | — | ⬜ |

Note: the brainstorm says "roughly $725B". Published totals for the same four companies ranged from ~$630B (Feb 2026) to ~$745B depending on date and definition — see [[07 AI Error Log]].

## B. Cloud revenue & operating income, Q3 2026 (owner: Blake)
| Segment | Lead revenue | Lead op. income | Lead source | Primary source to check | Verified |
|---|---|---|---|---|---|
| AWS | $45.98B (+39%) | ? | mitrade.com, computing.co.uk | Amazon Q3 2026 release, segment table | 🟡 |
| Google Cloud | $30.71B (+103%) | ~$11.1B | mitrade.com, tech-insider.org | Alphabet Q3 2026 release, segment table | 🟡 |
| Microsoft Azure | "$33.2B"?? | n/a | mitrade.com | **Microsoft does not disclose Azure revenue in dollars** — only growth %. Use Intelligent Cloud / new segment instead | ❌ suspected |
| Microsoft Cloud (total) | $63.9B (+30%) | — | computing.co.uk | MSFT FY26 Q1 release | 🟡 |
| Meta | no cloud segment | — | — | AI revenue sits inside ads; treat separately | — |

## C. Useful lives of servers & network equipment (owner: Partner)
| Company | Current life (lead) | History (lead) | Primary source | Verified |
|---|---|---|---|---|
| Amazon | 5 yrs (subset of servers, from 6, eff. 1/1/2025) | 4→5 (2022), 5→6 (2024), 6→5 (2025) | FY2024 10-K, Note 1 | 🟡 (seen in 10-K excerpt) |
| Alphabet | 6 yrs | 3→4 (2021), →6 (2023) | latest 10-K, Note 1 | 🟡 |
| Meta | 5.5 yrs | 4–5 → 5.5 (2025) | FY2024 10-K | 🟡 |
| Microsoft | 6 yrs | 4→6 (2022) | FY2025 10-K | 🟡 |
| Buildings | 25–40 yrs typical | — | each 10-K PP&E note | ⬜ |

## D. Other inputs
| Input | Value | Source | Verified |
|---|---|---|---|
| Required return (WACC) range | 8% / 10% / 12% | Damodaran WACC by industry (pages.stern.nyu.edu/~adamodar) — check software/internet | ⬜ |
| Share of capex that is servers/chips vs. buildings/power | assume 60/40 — **needs a source** | 10-K PP&E breakdown, call commentary | ⬜ |
| Tax rate | 21% federal | statutory | ✅ |

## Check log
| Date | Who | What we checked | Result |
|---|---|---|---|
| | | | |
