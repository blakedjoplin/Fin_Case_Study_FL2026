---
type: model
owner: Blake
status: draft — inputs not yet verified
tags: [fin3010, model, npv]
---

# Model — Break-even Cash Flow

## The finance idea (Unit 6)
The VP of Marketing in the Apex case says: *"We're investing $100M and getting $150M back — why wouldn't we?"* That ignores **when** the cash arrives and **what return investors require**. The NPV rule fixes that.

The AI-capex headline makes the same mistake in reverse: people compare **one year of capex** to **one quarter or year of cloud revenue**. Revenue isn't cash flow, and a server bought in 2026 has to pay for itself before it's obsolete.

So we flip the NPV question around: **what level annual after-tax cash flow, over the asset's useful life, makes NPV = 0?**

$$
NPV = -I + \sum_{t=1}^{n} \frac{CF}{(1+r)^t} = 0
\quad\Rightarrow\quad
CF^{*} = I \cdot \frac{r}{1-(1+r)^{-n}}
$$

- $I$ = 2026 capex (~$730B, see [[04 Data Sources & Verification Log]])
- $r$ = required return (WACC)
- $n$ = useful life in years
- $CF^{*}$ = break-even annual after-tax cash flow

This is the same calculation as a loan payment: Excel `=PMT(r, n, -I)`.

## Hand-check (do this on a BA II Plus before trusting any code)
`N = 6, I/Y = 10, PV = −730, FV = 0, CPT PMT` → **167.6** ($B per year)
NPV check in Python with the same inputs: 0.00 ✅ (run Nov 26)

## Scenario table — $730B, single useful life ($B of after-tax cash flow per year)
| Required return | 4 yrs | 5 yrs | 6 yrs | 25 yrs |
|---|---|---|---|---|
| 8% | 220.4 | 182.8 | 157.9 | 68.4 |
| 10% | 230.3 | 192.6 | **167.6** | 80.4 |
| 12% | 240.3 | 202.5 | 177.6 | 93.1 |

**Takeaway:** useful life matters more than the required return. Going from 6 years to 4 years adds ~$63B a year; going from 8% to 12% adds ~$20B a year. That's why the companies' depreciation-life changes (3→6 years) are such a big deal — see section C of the data log.

## Blended version (more realistic, needs a sourced split)
Capex isn't all servers. Assume **60% servers/chips (5.5-yr life)** and **40% buildings/power (25-yr life)** — ⚠️ this split is an assumption we still need to source.

| Required return | Servers part | Buildings part | **Total CF\*** |
|---|---|---|---|
| 8% | 101.5 | 27.4 | **128.9** |
| 10% | 107.4 | 32.2 | **139.5** |
| 12% | 113.3 | 37.2 | **150.5** |

(5.5-yr annuity uses the formula with fractional n — fine as an approximation; say so.)

## From cash flow to revenue (optional second step)
Cash flow ≈ (Revenue − cash costs) × (1 − t) + t × Depreciation. Solving for revenue at an EBITDA margin $m$:

$$
Revenue^{*} = \frac{CF^{*} - t \cdot D}{m(1-t)}, \qquad D = I/n
$$

At 10%, 6 yrs, t = 21%, straight-line D = $121.7B:
| EBITDA margin (assumed) | Incremental revenue needed per year |
|---|---|
| 40% | $449.6B |
| 50% | $359.7B |
| 60% | $299.7B |

Compare with: AWS + Google Cloud + Microsoft Cloud Q3 2026 run rate (×4) — **but** that's *total* revenue, built by *all prior years'* capex too, and Meta has no cloud segment. Don't claim "they're short by $X" — say "2026's spending alone would need roughly this much new revenue."

## Choices to document in the post
- Which capex total and as-of date we used
- Single-life vs. blended
- Required return range and where it came from
- That this treats 2026 spending as one project (simplification)
- That Meta's AI payoff shows up as ad revenue, not cloud revenue
