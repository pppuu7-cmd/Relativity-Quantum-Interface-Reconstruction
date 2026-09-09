#!/usr/bin/env python3
"""RQIR-RES-001: deterministic and randomized resource-conversion certificate.

This script validates the algebra used in RQIR Paper III for a scalar target beta
with setting-wise resource allocations e_k >= 0, whitened per-unit target scores
s_k, nuisance score matrices J_k, and fixed independent nuisance precision Lambda.

The profiled information is
    I_beta(e; Lambda) = min_a sum_k e_k ||s_k - J_k a||^2 + a^T Lambda a.
"""

from __future__ import annotations
import json
from pathlib import Path
import numpy as np

SEED = 20260909
TOL = 1e-9
N_RANDOM = 5000

def profiled_information(e, s_list, J_list, Lambda=None):
    e = np.asarray(e, dtype=float)
    p = J_list[0].shape[1]
    if Lambda is None:
        Lambda = np.zeros((p, p), dtype=float)
    A = np.array(Lambda, dtype=float, copy=True)
    b = np.zeros(p, dtype=float)
    c = 0.0
    for ek, s, J in zip(e, s_list, J_list):
        s = np.asarray(s, dtype=float)
        J = np.asarray(J, dtype=float)
        A += ek * (J.T @ J)
        b += ek * (J.T @ s)
        c += ek * float(s @ s)
    return float(c - b @ np.linalg.pinv(A) @ b)

def nuisance_minimizer(e, s_list, J_list, Lambda=None):
    e = np.asarray(e, dtype=float)
    p = J_list[0].shape[1]
    if Lambda is None:
        Lambda = np.zeros((p, p), dtype=float)
    A = np.array(Lambda, dtype=float, copy=True)
    b = np.zeros(p, dtype=float)
    for ek, s, J in zip(e, s_list, J_list):
        A += ek * (J.T @ J)
        b += ek * (J.T @ s)
    return np.linalg.pinv(A) @ b

def random_problem(rng, K=4, p=2):
    s_list, J_list = [], []
    for _ in range(K):
        m = int(rng.integers(1, 5))
        s_list.append(rng.normal(size=m))
        J_list.append(rng.normal(size=(m, p)))
    return s_list, J_list

def main():
    rng = np.random.default_rng(SEED)
    out = {"certificate": "RQIR-RES-001", "seed": SEED, "tolerance": TOL}

    # A. Positive homogeneity without fixed external prior.
    max_hom = 0.0
    for _ in range(N_RANDOM):
        s, J = random_problem(rng)
        e = rng.uniform(0.05, 3.0, size=len(s))
        alpha = rng.uniform(0.05, 10.0)
        lhs = profiled_information(alpha * e, s, J)
        rhs = alpha * profiled_information(e, s, J)
        max_hom = max(max_hom, abs(lhs - rhs))
    out["A_homogeneity"] = {"max_abs_error": max_hom, "pass": max_hom < 1e-8}

    # B. Componentwise monotonicity with fixed Lambda >= 0.
    min_gain = float("inf")
    for _ in range(N_RANDOM):
        s, J = random_problem(rng)
        e = rng.uniform(0.0, 2.0, size=len(s))
        de = rng.uniform(0.0, 1.0, size=len(s))
        X = rng.normal(size=(J[0].shape[1], J[0].shape[1]))
        Lam = X.T @ X
        gain = profiled_information(e + de, s, J, Lam) - profiled_information(e, s, J, Lam)
        min_gain = min(min_gain, gain)
    out["B_monotonicity"] = {"min_gain": min_gain, "pass": min_gain > -1e-8}

    # C. Concavity in resource allocation.
    min_concavity_gap = float("inf")
    for _ in range(N_RANDOM):
        s, J = random_problem(rng)
        e1 = rng.uniform(0.0, 3.0, size=len(s))
        e2 = rng.uniform(0.0, 3.0, size=len(s))
        t = rng.uniform(0.0, 1.0)
        X = rng.normal(size=(J[0].shape[1], J[0].shape[1]))
        Lam = X.T @ X
        lhs = profiled_information(t * e1 + (1-t) * e2, s, J, Lam)
        rhs = t * profiled_information(e1, s, J, Lam) + (1-t) * profiled_information(e2, s, J, Lam)
        min_concavity_gap = min(min_concavity_gap, lhs-rhs)
    out["C_concavity"] = {"min_gap": min_concavity_gap, "pass": min_concavity_gap > -1e-8}

    # D. Exact shared-nuisance alignment is not repaired by arbitrary resource scaling.
    a0 = np.array([0.4, -0.7])
    J_align = [
        np.array([[1.0, 0.2], [0.1, -0.3]]),
        np.array([[0.5, -0.8]]),
        np.array([[0.2, 0.4], [-0.6, 0.7], [0.9, 0.1]]),
    ]
    s_align = [Jk @ a0 for Jk in J_align]
    aligned_values = {}
    for B in [1.0, 10.0, 1e3, 1e6]:
        weights = np.array([0.2, 0.3, 0.5]) * B
        aligned_values[str(B)] = profiled_information(weights, s_align, J_align)
    max_align = max(abs(v) for v in aligned_values.values())
    out["D_exact_alignment"] = {"values": aligned_values, "max_abs": max_align, "pass": max_align < 1e-8}

    # E. Analytic optimum for the Paper-II two-band example with equal unit costs.
    g2, g4 = 0.3, 0.7
    B = 2.0
    s2 = [np.array([g2]), np.array([g4])]
    J2 = [np.array([[g2]]), np.array([[-g4]])]
    e2_star = B * g4 / (g2 + g4)
    e4_star = B * g2 / (g2 + g4)
    analytic_opt = 4.0 * B * g2**2 * g4**2 / (g2 + g4)**2
    grid = np.linspace(0.0, B, 20001)
    vals = np.array([profiled_information([x, B-x], s2, J2) for x in grid])
    i = int(np.argmax(vals))
    grid_opt = float(vals[i])
    grid_e2 = float(grid[i])
    equal = profiled_information([B/2, B/2], s2, J2)
    out["E_two_band_optimum"] = {
        "budget": B,
        "analytic_allocation": [e2_star, e4_star],
        "analytic_information": analytic_opt,
        "grid_e2": grid_e2,
        "grid_information": grid_opt,
        "equal_allocation_information": equal,
        "relative_gain_over_equal": analytic_opt/equal - 1.0,
        "pass": abs(grid_opt-analytic_opt) < 1e-8 and abs(grid_e2-e2_star) <= B/(len(grid)-1)
    }

    # F. Budget inversion under positive homogeneity.
    sigma_target = 0.2
    I_req = 1.0 / sigma_target**2
    kappa = analytic_opt / B
    B_min = I_req / kappa
    e_star = [B_min * g4/(g2+g4), B_min * g2/(g2+g4)]
    I_check = profiled_information(e_star, s2, J2)
    out["F_budget_inversion"] = {
        "sigma_target": sigma_target,
        "required_information": I_req,
        "optimal_information_per_cost": kappa,
        "minimum_budget": B_min,
        "check_information": I_check,
        "pass": abs(I_check-I_req) < 1e-8
    }

    # G. Envelope derivative / marginal information value.
    e = np.array([1.2, 0.8])
    a_star = nuisance_minimizer(e, s2, J2)
    analytic_grad = np.array([
        float((sk - Jk @ a_star) @ (sk - Jk @ a_star))
        for sk, Jk in zip(s2, J2)
    ])
    h = 1e-6
    base = profiled_information(e, s2, J2)
    fd = np.array([
        (profiled_information(e + h*np.eye(2)[k], s2, J2)-base)/h
        for k in range(2)
    ])
    grad_err = float(np.max(np.abs(analytic_grad-fd)))
    out["G_envelope_gradient"] = {
        "allocation": e.tolist(),
        "nuisance_minimizer": a_star.tolist(),
        "analytic_gradient": analytic_grad.tolist(),
        "finite_difference_gradient": fd.tolist(),
        "max_abs_error": grad_err,
        "pass": grad_err < 1e-6
    }

    # H. Fixed external prior is not exposure resource: it breaks positive homogeneity.
    Lam = np.array([[0.5]])
    I1 = profiled_information([1.0, 1.0], s2, J2, Lam)
    I10 = profiled_information([10.0, 10.0], s2, J2, Lam)
    hom_residual = I10 - 10.0 * I1
    out["H_fixed_prior_nonhomogeneity"] = {
        "I_e": I1,
        "I_10e": I10,
        "I_10e_minus_10_I_e": hom_residual,
        "pass": abs(hom_residual) > 1e-6 and I10 >= I1
    }

    out["all_pass"] = all(v.get("pass", True) for k, v in out.items() if isinstance(v, dict))
    outpath = Path("rqir_resource_certificate.json")
    outpath.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
