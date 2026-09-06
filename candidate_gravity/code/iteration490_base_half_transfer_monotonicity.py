#!/usr/bin/env python3
"""Iteration 490: exact monotonicity audit for frozen central4 BASE/HALF spectral transfer.

Non-promoting estimator/provenance calculation.  No Candidate-Gravity dynamics,
thresholds, source ordering, or parameter conventions are changed.
"""
import json
import sympy as sp

th = sp.symbols('theta', positive=True, real=True)
t = sp.symbols('t', positive=True, real=True)

rho_theta = sp.simplify((4-sp.cos(th/2))/(sp.cos(th/2)*(4-sp.cos(th))))
rho_t = sp.simplify((4-t)/(t*(5-2*t**2)))
dr_dt = sp.factor(sp.diff(rho_t, t))

expected_dr_dt = -4*(t-1)*(t**2-5*t-5)/(t**2*(2*t**2-5)**2)
assert sp.simplify(dr_dt-expected_dr_dt) == 0
assert sp.limit(rho_theta, th, 0, dir='+') == 1
assert sp.limit(rho_theta, th, sp.pi, dir='-') == sp.oo

# On 0<t<1: (t-1)<0 and (t^2-5t-5)<0, so their product is positive;
# denominator is positive; therefore drho/dt<0.  Since t=cos(theta/2)
# strictly decreases on 0<theta<pi, drho/dtheta>0 there.

series = sp.series(rho_theta, th, 0, 10)

out = {
    "iteration": 490,
    "classification": "PASS_BASE_HALF_TRANSFER_STRICT_MONOTONICITY_EXACT__NON_PROMOTING",
    "rho_theta": str(rho_theta),
    "rho_t": str(rho_t),
    "drho_dt_factorized": str(dr_dt),
    "domain": "0 < |theta| < pi",
    "proof_signs": {
        "t_range": "0 < t=cos(theta/2) < 1",
        "t_minus_1": "negative",
        "t2_minus_5t_minus_5": "negative",
        "denominator": "positive",
        "drho_dt": "negative",
        "dt_dtheta": "negative",
        "drho_dtheta": "positive"
    },
    "limits": {"theta_to_0": "1", "theta_to_pi_minus": "+infinity"},
    "consequence_1d": "1 < rho(theta) < infinity for 0<|theta|<pi",
    "consequence_mixed_single_mode": "D_half/D_base=rho(theta_x)rho(theta_y)>1 whenever both BASE factors are nonzero in the open Nyquist cell",
    "series": str(series),
    "scope": "estimator/provenance only; not gravity consistency, comparator identity, non-identifiability, near-degeneracy, or novelty certificate"
}
print(json.dumps(out, indent=2, sort_keys=True))
