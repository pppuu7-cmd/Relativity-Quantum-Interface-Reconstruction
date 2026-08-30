#!/usr/bin/env python3
"""RQIR Iteration 096 — characterization-time value of information.

This is a deterministic resource/decision regression.  The Iteration-094 box
is synthetic and is reused only to verify the new formulas; no apparatus
performance is inferred from it.
"""
from math import inf, isclose

# Exact local contraction leverages reproduced from the Iteration-094
# regression box.  They are dimensionless d ln(W)/d eta values.
LEVERAGE = {
    "14.Rsrc": 0.5191102104601385,
    "09.Rsrc": 0.4273712599258450,
    "14.A": 0.18109516727283034,
    "14.duty": 0.15899646329385492,
    "09.duty": 0.10243207461665434,
    "09.A": 0.035279501184403525,
}


def fractional_decision_shrink_rate(lam, r_char, h):
    """Local -(1/W)dW/dt for Fisher-limited characterization.

    h is the present 1-sigma/half-width in the same primitive coordinate and
    r_char is the independent characterization Fisher rate for that coordinate.
    With h=I^{-1/2}, dh/dt=-(1/2) r_char h^3, giving

        Xi = 0.5 * Lambda * r_char * h^2.
    """
    assert lam >= 0.0 and r_char >= 0.0 and h > 0.0
    return 0.5 * lam * r_char * h * h


def characterization_time(h0, h1, r_char, h_floor=0.0):
    """Extra time to contract h0 -> h1 with an irreducible floor.

    Model: h(t)^2 = h_floor^2 + 1/(I0+r_char t), with
    I0=1/(h0^2-h_floor^2).
    """
    assert r_char > 0.0
    assert h0 > h_floor >= 0.0
    if h1 <= h_floor:
        return inf
    assert h1 < h0
    return (
        1.0 / (h1*h1 - h_floor*h_floor)
        - 1.0 / (h0*h0 - h_floor*h_floor)
    ) / r_char


def break_even_speed(lam_ref, lam_other):
    """Required ratio (R h^2)_other/(R h^2)_ref to match Xi."""
    assert lam_ref > 0.0 and lam_other > 0.0
    return lam_ref / lam_other


def main():
    # Equal normalized characterization speed G=R_char*h^2 recovers the
    # Iteration-094 leverage ranking exactly.
    ranked = sorted(LEVERAGE, key=LEVERAGE.get, reverse=True)
    assert ranked == [
        "14.Rsrc", "09.Rsrc", "14.A", "14.duty", "09.duty", "09.A"
    ]

    ref = "14.Rsrc"
    thresholds = {
        name: break_even_speed(LEVERAGE[ref], lam)
        for name, lam in LEVERAGE.items() if name != ref
    }

    # NG-049 counterexample: a lower raw decision leverage can be the better
    # measurement per second if its characterization channel is sufficiently
    # faster.  A14 needs only ~2.8665x larger G than Rsrc14 to overtake it.
    xi_ref = fractional_decision_shrink_rate(LEVERAGE[ref], 1.0, 1.0)
    xi_a14 = fractional_decision_shrink_rate(LEVERAGE["14.A"], 3.0, 1.0)
    assert xi_a14 > xi_ref
    assert isclose(thresholds["14.A"], 2.866505044157633, rel_tol=2e-13)

    # Closed-form contraction law, no floor: halving an uncertainty requires
    # three times the present Fisher-equivalent exposure 1/(R h0^2).
    t_half = characterization_time(1.0, 0.5, 1.0)
    assert isclose(t_half, 3.0, rel_tol=1e-14)

    # A nonzero floor makes any target at/below the floor impossible.
    assert characterization_time(1.0, 0.2, 1.0, h_floor=0.2) == inf
    t_floor = characterization_time(1.0, 0.5, 2.0, h_floor=0.1)
    assert t_floor > 0.0

    print("PASS Iteration 096 characterization-time VOI")
    print("equal-G leverage ranking:", ranked)
    print("G=(R_char h^2) break-even vs Toy014 Rsrc:")
    for name in ranked[1:]:
        print(f"  {name}: {thresholds[name]:.12g}x")
    print("half-width contraction time at R=1,h0=1:", t_half)
    print("floor-aware example time:", t_floor)


if __name__ == "__main__":
    main()
