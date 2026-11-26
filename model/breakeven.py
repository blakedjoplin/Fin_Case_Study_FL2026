"""Break-even cash flow for Big Tech's 2026 AI capex.

Question: what level annual after-tax cash flow, over the assets' useful
life, makes NPV = 0 on ~$730B of 2026 capex?

    CF* = I * r / (1 - (1 + r) ** -n)        (same as Excel =PMT(r, n, -I))

Run:  python model/breakeven.py
Inputs are DRAFT leads (as of Q3 2026 earnings, Oct 2026) until each one is
verified against the companies' own filings.
"""

CAPEX_B = 730.0          # $B, sum of 2026 guidance midpoints (draft)
TAX = 0.21               # US federal statutory rate
BUILDING_LIFE = 25       # years, assumption
SERVER_SHARE = 0.60      # share of capex in servers/chips, assumption (needs a source)


def breakeven_cf(capex: float, r: float, n: float) -> float:
    """Level annual cash flow with NPV = 0 at required return r over n years."""
    return capex * r / (1 - (1 + r) ** -n)


def npv(capex: float, r: float, cf: float, n: int) -> float:
    return -capex + sum(cf / (1 + r) ** t for t in range(1, n + 1))


def blended_cf(capex: float, r: float, server_life: float,
               server_share: float = SERVER_SHARE,
               building_life: float = BUILDING_LIFE) -> float:
    """Servers and buildings depreciate on different lives; sum the two annuities."""
    return (breakeven_cf(capex * server_share, r, server_life)
            + breakeven_cf(capex * (1 - server_share), r, building_life))


def revenue_needed(cf: float, capex: float, life: float, margin: float,
                   tax: float = TAX) -> float:
    """Incremental revenue at an EBITDA margin that yields cf after tax.

    cf = (Rev * margin) * (1 - tax) + tax * D,  D = straight-line depreciation
    """
    dep = capex / life
    return (cf - tax * dep) / (margin * (1 - tax))


def main() -> None:
    rates = (0.08, 0.10, 0.12)
    lives = (4, 5, 6, 25)

    print(f"Break-even annual after-tax cash flow on ${CAPEX_B:.0f}B ($B/yr)")
    print("rate  " + "  ".join(f"{n:>5}y" for n in lives))
    for r in rates:
        print(f"{r:>4.0%}  " + "  ".join(f"{breakeven_cf(CAPEX_B, r, n):6.1f}" for n in lives))

    print(f"\nBlended ({SERVER_SHARE:.0%} servers @ 5.5y, rest @ {BUILDING_LIFE}y)")
    for r in rates:
        print(f"{r:>4.0%}  {blended_cf(CAPEX_B, r, 5.5):6.1f}")

    base = breakeven_cf(CAPEX_B, 0.10, 6)
    print(f"\nHand-check target (BA II Plus N=6, I/Y=10, PV=-730, CPT PMT): {base:.1f}")
    print(f"NPV at that cash flow: {npv(CAPEX_B, 0.10, base, 6):.6f}")

    print("\nIncremental revenue needed per year (10%, 6y, straight-line dep)")
    for m in (0.40, 0.50, 0.60):
        print(f"EBITDA margin {m:.0%}: ${revenue_needed(base, CAPEX_B, 6, m):.1f}B")


if __name__ == "__main__":
    main()
