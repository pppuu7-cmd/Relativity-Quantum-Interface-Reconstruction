#!/usr/bin/env python3
"""Iteration 489: exact BASE/HALF central4 spectral-ratio audit.

This is a diagnostic/provenance audit only. It does not promote Candidate Gravity.
"""
import json
import math


def rho(theta: float) -> float:
    """Exact one-dimensional HALF/BASE transfer ratio away from BASE zeros."""
    return (4.0 - math.cos(theta / 2.0)) / (
        math.cos(theta / 2.0) * (4.0 - math.cos(theta))
    )


def symbol(theta: float) -> complex:
    return 1j * math.sin(theta) * (4.0 - math.cos(theta)) / 3.0


def main() -> None:
    samples = [0.1, 0.3, 0.7, 1.2, 2.0]
    checks = []
    for t in samples:
        lhs = 2.0 * symbol(t / 2.0) / symbol(t)
        rhs = rho(t)
        checks.append({
            "theta": t,
            "two_Ahalf_over_A": [lhs.real, lhs.imag],
            "rho_closed_form": rhs,
            "abs_difference": abs(lhs - rhs),
        })

    out = {
        "schema": "rqir_iteration489_base_half_spectral_ratio_v1",
        "operator": "central4 c=[1/12,-2/3,2/3,-1/12] nodes=[-2,-1,+1,+2]",
        "exact_1d_ratio": "rho(theta)=2 A(theta/2)/A(theta)=(4-cos(theta/2))/(cos(theta/2)*(4-cos(theta)))",
        "exact_mixed_ratio": "D_half/D_base=rho(theta_x)*rho(theta_y)",
        "small_theta_series": "rho(theta)=1+theta^4/32-theta^6/256+469 theta^8/368640+O(theta^10)",
        "domain_statement": "for 0<|theta|<pi, cos(theta/2)>0 and 4-cos(theta)>0, so rho(theta)>0 and is nonconstant",
        "consequence": "no single mode-independent exact scalar maps BASE to HALF over the resolved spectrum; two-level Richardson promotion is not spectrally identifiable for generic multimode data",
        "classification": "PASS_BASE_HALF_SPECTRAL_TRANSFER_RATIO_EXACT__NON_PROMOTING",
        "scientific_scope": "estimator/provenance only",
        "checks": checks,
        "max_numeric_identity_error": max(c["abs_difference"] for c in checks),
        "MODEL_READINESS": "24%",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
