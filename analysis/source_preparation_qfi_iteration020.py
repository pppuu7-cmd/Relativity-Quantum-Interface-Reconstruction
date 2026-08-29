"""RQIR Iteration 020: quantum Fisher rate for hidden source-preparation amplitude.

Uses the accepted Iteration-011 Toy009 exact-null direction Delta0 and the
commuting family rho(a)=I/5+a Delta0.  Because [rho(a),Delta0]=0, the quantum
Fisher information for amplitude a is saturated by projective measurement in
the Delta0 eigenbasis:

    F_Q(a)=sum_i d_i^2 / p_i(a),  p_i=1/5+a d_i.

This is a fundamental per-copy upper bound / saturable toy-model benchmark,
not a claim that the required eigenbasis measurement has been physically
implemented for a gravitational source.
"""
from __future__ import annotations

import math
import numpy as np

from toy009_joint_calibration_geometry import (
    D, E, H, EPS, ACCEPT_Y1, ACCEPT_TIMES,
    herm_vec, mat, evolve, sym, probe,
)


def accepted_null_operator() -> np.ndarray:
    times = np.asarray(ACCEPT_TIMES, float)
    tR = times[2]
    p = [probe(0.0), probe(ACCEPT_Y1)]
    rows = [herm_vec(np.eye(D)), herm_vec(H)]
    for k in (0, 1):
        for t in times:
            rows.append(herm_vec(evolve(p[k], float(t))))
    rows.append(herm_vec(sym(evolve(p[0], tR), p[0])))
    extra = [
        (0, 1, times[1]), (1, 1, times[5]), (1, 0, tR),
        (0, 1, tR), (1, 0, times[3]), (0, 0, times[6]),
        (0, 1, times[6]),
    ]
    for k, l, t in extra:
        rows.append(herm_vec(sym(evolve(p[k], float(t)), p[l])))
    A = np.vstack(rows)
    _, s, vh = np.linalg.svd(A, full_matrices=True)
    assert int(np.sum(s > 1e-10)) == 24
    d0 = mat(vh[-1])
    d0 /= np.max(np.abs(np.linalg.eigvalsh(d0)))
    assert np.max(np.abs(A @ herm_vec(d0))) < 1e-12
    return d0


DELTA0 = accepted_null_operator()
D_EIG = np.linalg.eigvalsh(DELTA0)


def probabilities(a: float) -> np.ndarray:
    return np.ones(D)/D + a * D_EIG


def amplitude_qfi(a: float) -> float:
    p = probabilities(a)
    if np.min(p) <= 0:
        raise ValueError("rho(a) is not positive")
    return float(np.sum(D_EIG**2 / p))


def copies_for_information(target_information: float, a: float = EPS,
                           efficiency: float = 1.0) -> float:
    """Accepted copies for a measurement carrying efficiency*QFI per copy."""
    if not (0 < efficiency <= 1):
        raise ValueError("efficiency must be in (0,1]")
    return target_information / (efficiency * amplitude_qfi(a))


def prep_information_rate(a: float, cycle_time_s: float,
                          acceptance: float = 1.0,
                          efficiency: float = 1.0) -> float:
    return acceptance * efficiency * amplitude_qfi(a) / cycle_time_s


def prep_information_for_retention(detector_information: float, retention: float) -> float:
    return detector_information * retention / (1.0 - retention)


def main():
    fq = amplitude_qfi(EPS)
    print("Delta0 eigenvalues:", D_EIG)
    print("rho+(a=0.08) eigenvalues:", probabilities(EPS))
    print("QFI per accepted copy at a=0.08:", fq)

    detector_info = 25.0
    for r in (0.8, 0.9, 0.95, 0.99):
        c = prep_information_for_retention(detector_info, r)
        n = copies_for_information(c)
        print("retention", r, "C_a", c, "QFI-limited accepted copies", n,
              "integer ceiling", math.ceil(n))

    print("\nEfficiency penalty for 90% retention")
    c90 = prep_information_for_retention(detector_info, 0.9)
    for eta in (1.0, 0.5, 0.1, 0.01):
        print("eta_meas", eta, "accepted copies", copies_for_information(c90, efficiency=eta))

    print("\nExample preparation Fisher rates")
    for cycle_ms in (1.0, 10.0, 100.0):
        rate = prep_information_rate(EPS, cycle_ms*1e-3, acceptance=0.5, efficiency=0.5)
        print("cycle", cycle_ms, "ms, p=0.5, eta=0.5 -> F_a/s", rate,
              "time for C_a=225 [s]", 225.0/rate)

    # Regression checks from deterministic Iteration-011 reconstruction.
    assert np.allclose(D_EIG,
                       [-0.97233836, -0.36204793, -0.16708132, 0.50146762, 1.0],
                       atol=2e-8)
    assert abs(fq - 13.27068619) < 2e-7
    assert abs(copies_for_information(225.0) - 16.95466209) < 2e-7


if __name__ == "__main__":
    main()
