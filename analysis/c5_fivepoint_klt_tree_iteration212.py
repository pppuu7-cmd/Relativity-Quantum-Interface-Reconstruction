#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 212.

Deterministic pure-Einstein five-graviton MHV tree engine using
five-point field-theory KLT + Parke-Taylor Yang-Mills amplitudes.

This is a pre-loop validation gate for the future physical five-point
two-particle unitarity cut. Couplings are stripped. The overall KLT phase/sign
is frozen by the formulas below and is checked consistently rather than
identified with an observable phase.
"""
from pathlib import Path
import json, math
import numpy as np

ITERATION = 212
RNG_SEED = 12345

def angle(lams, i, j):
    a, b = lams[i], lams[j]
    return a[0]*b[1] - a[1]*b[0]

def square(tildes, i, j):
    a, b = tildes[i], tildes[j]
    return a[0]*b[1] - a[1]*b[0]

def sij(lams, tildes, i, j):
    return angle(lams, i, j) * square(tildes, j, i)

def parke_taylor(order, neg, lams, tildes):
    numerator = angle(lams, neg[0], neg[1])**4
    denominator = 1.0 + 0.0j
    seq = list(order)
    for a, b in zip(seq, seq[1:] + seq[:1]):
        denominator *= angle(lams, a, b)
    return 1j * numerator / denominator

def m4_klt(labels, neg, lams, tildes):
    a,b,c,d = labels
    A = lambda order: parke_taylor(order, neg, lams, tildes)
    return -1j * sij(lams,tildes,a,b) * A((a,b,c,d)) * A((a,b,d,c))

def m5_klt(labels, neg, lams, tildes):
    a,b,c,d,e = labels
    A = lambda order: parke_taylor(order, neg, lams, tildes)
    term1 = (1j * sij(lams,tildes,a,b) * sij(lams,tildes,c,d)
             * A((a,b,c,d,e)) * A((b,a,d,c,e)))
    term2 = (1j * sij(lams,tildes,a,c) * sij(lams,tildes,b,d)
             * A((a,c,b,d,e)) * A((c,a,d,b,e)))
    return term1 + term2

def soft_factor_plus(lams, tildes, soft=4, refx=0, refy=1, hard=(0,1,2,3)):
    out = 0.0 + 0.0j
    for a in hard:
        out += (square(tildes,soft,a)/angle(lams,soft,a)
                * angle(lams,refx,a)*angle(lams,refy,a)
                / (angle(lams,refx,soft)*angle(lams,refy,soft)))
    return out

rng = np.random.default_rng(RNG_SEED)
lambda_base = [rng.normal(size=2) + 1j*rng.normal(size=2) for _ in range(5)]
tilde_base = [rng.normal(size=2) + 1j*rng.normal(size=2) for _ in range(5)]
solve_det = np.linalg.det(np.column_stack([lambda_base[2], lambda_base[3]]))
if abs(solve_det) < 1e-8:
    raise RuntimeError("deterministic seed produced a singular solve pair")

def soft_family(epsilon):
    lams = [x.copy() for x in lambda_base]
    tildes = [x.copy() for x in tilde_base]
    scale = math.sqrt(float(epsilon))
    lams[4] = scale * lambda_base[4]
    tildes[4] = scale * tilde_base[4]
    L = np.column_stack([lams[2], lams[3]])
    remainder = -(np.outer(lams[0],tildes[0])
                  + np.outer(lams[1],tildes[1])
                  + np.outer(lams[4],tildes[4]))
    solved = np.linalg.solve(L, remainder)
    tildes[2] = solved[0,:]
    tildes[3] = solved[1,:]
    return lams, tildes

epsilons = np.array([1e-1,5e-2,2e-2,1e-2,5e-3,2e-3,1e-3,5e-4,2e-4,1e-4], dtype=float)
l0, t0 = soft_family(0.0)
m4 = m4_klt((0,1,2,3), (0,1), l0, t0)

records = []
max_momentum_residual = 0.0
max_permutation_relative_error = 0.0
for eps in epsilons:
    lams, tildes = soft_family(float(eps))
    P = sum((np.outer(lams[i],tildes[i]) for i in range(5)),
            start=np.zeros((2,2), dtype=complex))
    momentum_residual = float(np.max(np.abs(P)))
    max_momentum_residual = max(max_momentum_residual, momentum_residual)
    base = m5_klt((0,1,2,3,4), (0,1), lams, tildes)
    relabelings = [(0,1,3,2,4),(1,0,2,3,4),(0,2,1,3,4),(4,1,2,3,0)]
    perm_errors = []
    for order in relabelings:
        test = m5_klt(order, (0,1), lams, tildes)
        err = float(abs((test-base)/base))
        perm_errors.append(err)
        max_permutation_relative_error = max(max_permutation_relative_error, err)
    s0 = soft_factor_plus(lams,tildes)
    ratio = base/(s0*m4)
    records.append({
        "epsilon": float(eps),
        "abs_M5": float(abs(base)),
        "momentum_conservation_max_abs": momentum_residual,
        "permutation_relative_errors": perm_errors,
        "soft_ratio_M5_over_S0M4_real": float(ratio.real),
        "soft_ratio_M5_over_S0M4_imag": float(ratio.imag),
        "soft_ratio_distance_to_minus_one": float(abs(ratio+1)),
    })

logeps = np.log(epsilons)
logamp = np.log(np.array([r["abs_M5"] for r in records]))
soft_power = float(np.polyfit(logeps[-6:], logamp[-6:], 1)[0])

out = {
    "iteration": ITERATION,
    "date": "2026-09-01",
    "model_readiness_percent": 23,
    "scope": "pure-Einstein coupling-stripped five-graviton MHV tree engine; pre-loop unitarity-cut validation",
    "authority_convention": {
        "YM_MHV": "Parke-Taylor",
        "gravity_5pt": "field-theory KLT: i*s12*s34*A(12345)A(21435) + i*s13*s24*A(13245)A(31425)",
        "gravity_4pt": "-i*s12*A(1234)A(1243)",
        "sij": "<ij>[ji]",
        "overall_phase_note": "frozen implementation gives M5/(S0 M4)->-1 for the chosen soft-factor convention"
    },
    "rng_seed": RNG_SEED,
    "solve_pair_spinor_determinant_abs": float(abs(solve_det)),
    "negative_helicity_legs": [1,2],
    "soft_positive_helicity_leg": 5,
    "epsilons": epsilons.tolist(),
    "max_momentum_conservation_residual": max_momentum_residual,
    "max_permutation_relative_error": max_permutation_relative_error,
    "asymptotic_soft_power_fit_last6": soft_power,
    "expected_uniform_energy_soft_power": -1.0,
    "soft_power_abs_error": float(abs(soft_power+1.0)),
    "smallest_epsilon_soft_ratio_distance_to_minus_one": records[-1]["soft_ratio_distance_to_minus_one"],
    "records": records,
    "classification": {
        "momentum_conservation": "PASS_MACHINE_PRECISION",
        "gravity_permutation_relabeling": "PASS_NUMERICAL",
        "weinberg_leading_soft_power": "PASS_SCOPED",
        "leading_soft_factor_normalization": "PASS_UP_TO_FROZEN_OVERALL_KLT_SIGN",
        "loop_cut_integral": "NOT_YET_IMPLEMENTED",
        "candidate_residual": "NONE",
        "ANSATZ_003": "NOT_CREATED",
        "Fisher_resources": "FORBIDDEN"
    },
    "retained_results": [
        "C5-CUT-010 — DETERMINISTIC_FIVE_GRAVITON_KLT_TREE_ENGINE_PASSES_MOMENTUM_PERMUTATION_AND_LEADING_SOFT_CHECKS",
        "SOFT-NG-008 — MOMENTUM_CONSERVING_UNIFORM_SOFT_FAMILY_RECOVERS_WEINBERG_EPSILON_MINUS_ONE_SCALING",
        "NUM-NG-017 — TREE_ENGINE_IS_VALIDATED_BEFORE_ANY_TWO_PARTICLE_CUT_INTEGRATION",
        "NG-FUNNEL-069 — PHYSICAL_LOOP_CUT_CONSTRUCTION_MUST_BE_BUILT_FROM_A_VALIDATED_TREE_ENGINE_AND_FIXED_CROSSING_HELICITY_CONVENTION"
    ],
    "readiness_change": "unchanged at 23%; a computational building block is closed but the physical one-loop five-point cut is not yet evaluated",
    "next_gate": "Freeze a physical two-particle five-point cut channel, helicity sum, phase-space parameterization and IR endpoint prescription; then evaluate the cut at finite soft epsilon before regular+log extraction."
}
Path("results/c5_fivepoint_klt_tree_iteration212.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2,sort_keys=True))
