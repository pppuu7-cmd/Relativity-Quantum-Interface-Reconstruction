#!/usr/bin/env python3
"""Iteration 171: linked/amputated CTP cubic-vertex protocol.

This is a structural validator.  It freezes two facts used by the next RQIR
post-Gaussian search:

1. Connected three-point functions must be compared after conditioning on / 
   amputating the same measured two-point CTP kernel.  In a fixed source/field
   convention, spectral dressing of external legs cannot create a new 1PI cubic
   relation.

2. For any ordinary closed unitary cubic action S3=B(h,h,h)/3!, the r/a change
   h_+=r+a/2, h_-=r-a/2 yields

       S3[h_+]-S3[h_-] = 1/2 B(a,r,r) + 1/24 B(a,a,a).

   With vertex normalisations Gamma_arr/2! and Gamma_aaa/3!, this gives

       Gamma_aaa = Gamma_arr/4,   Gamma_aar = 0.

This is a generic closed-quantum CTP identity, not a gravity-specific one.
"""
from fractions import Fraction
from pathlib import Path
import json
import numpy as np

# Exact coefficient audit for a symmetric trilinear form B.
coef_arr_action = Fraction(1, 2)
coef_aaa_action = Fraction(1, 24)
Gamma_arr = coef_arr_action * 2  # coefficient convention: Gamma_arr / 2!
Gamma_aaa = coef_aaa_action * 6 # coefficient convention: Gamma_aaa / 3!
ratio = Gamma_aaa / Gamma_arr

assert Gamma_arr == 1
assert Gamma_aaa == Fraction(1, 4)
assert ratio == Fraction(1, 4)

# Scalar projected illustration of two-point dressing removal.
# Six pre-frozen row-like kinematic values; no target was used in choosing them.
p2 = np.array([0.7473,0.6157,0.4418,0.6120,0.6682,0.4239])
q2 = np.array([0.5076,0.3854,0.4260,0.3153,0.4004,0.2882])
r2 = np.array([0.3313,0.2935,0.2746,0.2773,0.2278,0.2321])

# Arbitrary deterministic source-completed cubic kernel used only to test algebra.
Gamma_phys = np.array([0.7,-0.4,1.2,0.3,-0.8,0.55])
G0p, G0q, G0r = 1/p2, 1/q2, 1/r2
chi0 = -(G0p * G0q * G0r) * Gamma_phys
amp0 = -chi0/(G0p*G0q*G0r)

# Apply nontrivial positive spectral/form-factor dressing to all external legs.
fp = np.exp(-0.37*p2) * (1+0.11*p2)
fq = np.exp(-0.37*q2) * (1+0.11*q2)
fr = np.exp(-0.37*r2) * (1+0.11*r2)
G1p, G1q, G1r = fp*G0p, fq*G0q, fr*G0r
chi1 = -(G1p * G1q * G1r) * Gamma_phys
amp1 = -chi1/(G1p*G1q*G1r)

max_amp_error = float(max(np.max(np.abs(amp0-Gamma_phys)), np.max(np.abs(amp1-Gamma_phys))))
raw_response_change_fraction = float(np.linalg.norm(chi1-chi0)/np.linalg.norm(chi0))

out = {
    "iteration": 171,
    "scope": "linked post-Gaussian CTP cubic protocol; source-completed convention inherited from Iterations 148-149",
    "closed_unitary_cubic_ra_identity": {
        "Gamma_arr": str(Gamma_arr),
        "Gamma_aar": "0",
        "Gamma_aaa": str(Gamma_aaa),
        "Gamma_aaa_over_Gamma_arr": str(ratio),
    },
    "external_leg_dressing_illustration": {
        "raw_response_relative_change": raw_response_change_fraction,
        "max_amputated_vertex_reconstruction_error": max_amp_error,
    },
    "classification": {
        "two_point_spectral_dressing": "CALIBRATED_SHARED_LAYER_NOT_NOVELTY",
        "closed_quantum_aaa_over_arr_ratio": "GENERIC_C4_AND_C5_UNITARY_IDENTITY_NOT_GRAVITY_SPECIFIC",
        "bare_classical_statistical_missing_quantum_vertex": "USEFUL_QUANTUM_VS_CLASSICAL_CONTROL_ONLY",
        "fixed_C3_full_ra_vertex": "BLOCKED",
        "fixed_C4_full_ra_vertex": "PARTIAL_TREE_UNITARY_STRUCTURE_SUPPORTED",
        "fixed_C5_full_ra_vertex": "PARTIAL_TREE_UNITARY_STRUCTURE_SUPPORTED",
        "ANSATZ_003": "NOT_CREATED",
        "Fisher_resources": "FORBIDDEN",
    },
    "retained_results": [
        "CTP-NG-001 — CLOSED_UNITARY_CUBIC_AAA_OVER_ARR_RATIO_IS_NOT_GRAVITY_SPECIFIC",
        "CTP-NG-002 — TWO_POINT_EXTERNAL_LEG_DRESSING_DISAPPEARS_AFTER_FIXED_CONVENTION_THREE_POINT_AMPUTATION",
        "NG-FUNNEL-031 — CANDIDATE_RESIDUAL_MUST_BE_A_LINKED_CTP_VERTEX_RELATION_AFTER_TWO_POINT_AMPUTATION",
    ],
    "model_readiness_percent": 24,
    "readiness_change": "unchanged: linked protocol is frozen and two false-positive relations are removed, but no residual survives fixed multi-point comparators",
}

Path("results/linked_ctp_vertex_protocol_iteration171.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(out, indent=2, sort_keys=True))
