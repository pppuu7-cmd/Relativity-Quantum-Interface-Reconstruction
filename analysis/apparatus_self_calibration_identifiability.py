"""RQIR apparatus self-calibration identifiability criterion.

This audit answers whether multiple measurement configurations can remove the
science-amplitude / multiplicative-scale degeneracy without an external prior.
It is analytic and model-agnostic; no hardware performance values are assumed.

For configuration c, after profiling its additive nuisances and covariance, let
A_c > 0 denote the remaining statistical Fisher information for its science
shape.  Linearise the response as

    mu_c = theta * (1 + a_c * kappa) * g_c + additive nuisances,

where a_c is the known sensitivity of configuration c to the common scale
parameter kappa.  At kappa=0, the 2x2 Fisher block for (theta,kappa) is

    F_tt = sum A_c
    F_tk = theta * sum a_c A_c
    F_kk = theta**2 * sum a_c**2 A_c.

Therefore

    det(F) = theta**2 * [(sum A_c)(sum a_c**2 A_c) - (sum a_c A_c)**2]
           = theta**2 * (sum A_c)**2 * Var_w(a_c),

with weights w_c=A_c/sum A_c.

Consequences:
* Merely repeating measurements, or adding configurations with the same scale
  response a_c, does NOT break the degeneracy.
* External calibration is not mathematically mandatory if the apparatus can
  realize at least two informative configurations with genuinely different,
  known a_c.  Then Var_w(a_c)>0 and the Fisher block is identifiable.
* An auxiliary calibration channel is the limiting case of adding information
  about kappa that is not proportional to the theta channel.
"""
from __future__ import annotations

import math


def fisher_block(theta: float, A: list[float], a: list[float]) -> tuple[tuple[float, float], tuple[float, float]]:
    if theta == 0.0:
        raise ValueError("local multiplicative-scale identification requires nonzero fiducial theta")
    if len(A) != len(a) or not A:
        raise ValueError("A and a must be non-empty and have equal length")
    if any(x <= 0.0 for x in A):
        raise ValueError("all profiled information weights A_c must be positive")

    s0 = sum(A)
    s1 = sum(x * y for x, y in zip(A, a))
    s2 = sum(x * y * y for x, y in zip(A, a))
    return ((s0, theta * s1), (theta * s1, theta * theta * s2))


def determinant(theta: float, A: list[float], a: list[float]) -> float:
    f = fisher_block(theta, A, a)
    return f[0][0] * f[1][1] - f[0][1] * f[1][0]


def weighted_variance_identity(theta: float, A: list[float], a: list[float]) -> float:
    s0 = sum(A)
    mean = sum(x * y for x, y in zip(A, a)) / s0
    var = sum(x * (y - mean) ** 2 for x, y in zip(A, a)) / s0
    return theta * theta * s0 * s0 * var


def profiled_theta_variance(theta: float, A: list[float], a: list[float]) -> float:
    """Variance after profiling free kappa; inf if kappa is not self-identifiable."""
    f = fisher_block(theta, A, a)
    det = f[0][0] * f[1][1] - f[0][1] ** 2
    scale = max(abs(f[0][0] * f[1][1]), abs(f[0][1] ** 2), 1.0)
    if det <= 1e-12 * scale:
        return math.inf
    # (F^-1)_theta,theta = F_kk / det
    return f[1][1] / det


def main() -> None:
    theta = 1.0

    # One configuration: exact amplitude/scale degeneracy.
    assert math.isinf(profiled_theta_variance(theta, [100.0], [1.0]))

    # More data with identical scale response does not help identifiability.
    assert math.isinf(profiled_theta_variance(theta, [100.0, 250.0, 900.0], [1.0, 1.0, 1.0]))

    # Different signal shapes or statistical weights alone still do not help if
    # their multiplicative scale response is the same.
    assert math.isinf(profiled_theta_variance(theta, [3.0, 70.0], [0.4, 0.4]))

    # Genuine differential scale response makes the block full rank.
    A = [100.0, 100.0]
    a = [0.5, 1.5]
    det = determinant(theta, A, a)
    assert det > 0.0
    assert math.isclose(det, weighted_variance_identity(theta, A, a), rel_tol=1e-14)
    assert math.isfinite(profiled_theta_variance(theta, A, a))

    # The determinant grows continuously with scale-response separation.
    det_small = determinant(theta, A, [0.95, 1.05])
    det_medium = determinant(theta, A, [0.75, 1.25])
    det_large = determinant(theta, A, [0.5, 1.5])
    assert 0.0 < det_small < det_medium < det_large

    print("single common-scale configuration: NON_IDENTIFIABLE")
    print("multiple same-response configurations: NON_IDENTIFIABLE")
    print("differential known scale response: SELF_CALIBRATING")
    print("det(F) = theta^2 (sum A)^2 Var_w(a): PASS")
    print("RQIR apparatus self-calibration identifiability audit: PASS")


if __name__ == "__main__":
    main()
