# Fin_Case_Study_FL2026

Code and resources for a FIN 3010 (Saint Louis University) case-study project:
**What would AI data centers have to earn?** A break-even NPV look at the roughly
$730B that Amazon, Alphabet, Meta and Microsoft plan to spend on capex in 2026.

Project notes, logs and planning live in a separate Obsidian vault, not in this repo.

## Contents
| Path | What |
|---|---|
| `model/breakeven.py` | Break-even cash flow model: scenario tables, blended server/building lives, NPV check, revenue needed |
| `concepts/concepts-sketch.html` | Early sketches of the three deliverable concepts (open in a browser) |
| `resources/sources.md` | Public data sources used to verify every input |

## Run the model
```
python model/breakeven.py
```
No dependencies beyond Python 3.

## Status
Inputs are **draft** (from Q3 2026 earnings coverage, Oct 2026) until each is verified against the companies' own filings. This is a back-of-the-envelope model, not a forecast.
