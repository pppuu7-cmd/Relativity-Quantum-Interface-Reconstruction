#!/usr/bin/env python3
"""Iteration 583: frozen MSSC-001 h^2 phi^2 / source-K2 expansion audit.

This gate consumes the parent scalar action frozen in Iteration 218,

  S_phi = -1/2 int sqrt(-g) [ g^{mu nu} d_mu phi d_nu phi + m^2 phi^2 ],
  g_{mu nu} = eta_{mu nu} + kappa h_{mu nu}.

No source/Born subtraction is performed here.  The purpose is only to make the
quadratic source/contact kernel K2 explicit from the SAME covariant action,
with no independently tunable contact coefficient.

For mixed-index H^mu_nu = eta^{mu alpha} h_{alpha nu} and h=Tr(H),

 sqrt(-g) = 1 + kappa h/2
              + kappa^2 [h^2/8 - Tr(H^2)/4] + O(kappa^3),

 sqrt(-g) g^{-1} = eta^{-1}
   + kappa [ (h/2) eta^{-1} - eta^{-1} h eta^{-1} ]
   + kappa^2 [ eta^{-1} h eta^{-1} h eta^{-1}
               - (h/2) eta^{-1} h eta^{-1}
               + (h^2/8-Tr(H^2)/4) eta^{-1} ] + O(kappa^3).

These coefficients define the frozen K2 source contact.  A deterministic
numerical regression checks O(kappa^3) remainder scaling against the exact
matrix determinant/inverse expression for several nontrivial symmetric h.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import numpy as np

ETA = np.diag([1.0, -1.0, -1.0, -1.0])
ETA_INV = ETA.copy()


def coeffs(hcov: np.ndarray):
    H = ETA_INV @ hcov
    trH = float(np.trace(H))
    trH2 = float(np.trace(H @ H))
    s1 = 0.5 * trH
    s2 = 0.125 * trH * trH - 0.25 * trH2
    a0 = ETA_INV
    a1 = s1 * ETA_INV - ETA_INV @ hcov @ ETA_INV
    a2 = (
        ETA_INV @ hcov @ ETA_INV @ hcov @ ETA_INV
        - 0.5 * trH * (ETA_INV @ hcov @ ETA_INV)
        + s2 * ETA_INV
    )
    return trH, trH2, s1, s2, a0, a1, a2


def exact_objects(hcov: np.ndarray, kappa: float):
    g = ETA + kappa * hcov
    detg = float(np.linalg.det(g))
    if detg >= 0:
        raise RuntimeError(f"signature/determinant left Lorentzian branch: det(g)={detg}")
    sq = float(np.sqrt(-detg))
    return sq, sq * np.linalg.inv(g)


def main():
    rng = np.random.default_rng(583218)
    hs = []
    for _ in range(6):
        a = rng.normal(size=(4, 4))
        h = 0.12 * (a + a.T) / 2.0
        hs.append(h)

    kappas = [2.0e-2, 1.0e-2, 5.0e-3, 2.5e-3]
    records = []
    failures = []
    max_scaled_scalar = 0.0
    max_scaled_tensor = 0.0

    for ih, hcov in enumerate(hs):
        trH, trH2, s1, s2, a0, a1, a2 = coeffs(hcov)
        scalar_scaled = []
        tensor_scaled = []
        for k in kappas:
            sq, dens_inv = exact_objects(hcov, k)
            sq2 = 1.0 + k * s1 + (k * k) * s2
            a2approx = a0 + k * a1 + (k * k) * a2
            se = abs(sq - sq2)
            te = float(np.max(np.abs(dens_inv - a2approx)))
            ss = se / (abs(k) ** 3)
            ts = te / (abs(k) ** 3)
            scalar_scaled.append(ss)
            tensor_scaled.append(ts)
            max_scaled_scalar = max(max_scaled_scalar, ss)
            max_scaled_tensor = max(max_scaled_tensor, ts)
            records.append({
                "sample": ih,
                "kappa": k,
                "sqrt_det_abs_error": se,
                "densitized_inverse_max_abs_error": te,
                "sqrt_det_error_over_kappa3": ss,
                "densitized_inverse_error_over_kappa3": ts,
            })

        # Fail closed if reducing kappa by 8x does not reduce absolute error by
        # at least 100x. Ideal cubic scaling gives 512x; 100x leaves generous
        # floating-point margin while still rejecting a wrong quadratic term.
        first = [r for r in records if r["sample"] == ih and r["kappa"] == kappas[0]][0]
        last = [r for r in records if r["sample"] == ih and r["kappa"] == kappas[-1]][0]
        if not (last["sqrt_det_abs_error"] <= first["sqrt_det_abs_error"] / 100.0):
            failures.append(f"sample {ih}: scalar remainder failed cubic-scaling gate")
        if not (last["densitized_inverse_max_abs_error"] <= first["densitized_inverse_max_abs_error"] / 100.0):
            failures.append(f"sample {ih}: tensor remainder failed cubic-scaling gate")

    result = {
        "iteration": 583,
        "date": "2026-09-08",
        "parent_source_authority": "MSSC-001 / Iteration218",
        "parent_action": "S_phi=-1/2 int sqrt(-g)[g^{mu nu} partial_mu phi partial_nu phi + m^2 phi^2]",
        "metric_convention": "g_{mu nu}=eta_{mu nu}+kappa h_{mu nu}; eta=diag(+---)",
        "k2_contact": {
            "sqrt_minus_g_kappa2": "h^2/8 - Tr(H^2)/4",
            "sqrt_minus_g_ginv_kappa2": "eta^-1 h eta^-1 h eta^-1 -(h/2)eta^-1 h eta^-1 +(h^2/8-Tr(H^2)/4)eta^-1",
            "rule": "all h^2 phi^2 contact coefficients are fixed by MSSC-001; independent tuning forbidden",
        },
        "regression": {
            "samples": len(hs),
            "kappas": kappas,
            "max_sqrt_det_error_over_kappa3": max_scaled_scalar,
            "max_densitized_inverse_error_over_kappa3": max_scaled_tensor,
            "records": records,
        },
        "failures": failures,
        "raw_result_integrity_valid": len(failures) == 0,
        "classification": (
            "PASS_SOURCE_K2_QUADRATIC_CONTACT_FROM_FROZEN_MSSC001__NON_RESIDUAL"
            if not failures else
            "FAIL_SOURCE_K2_QUADRATIC_CONTACT_REGRESSION"
        ),
        "scientific_scope": "source/contact prerequisite only; not comparator residual, not Candidate-Gravity model PASS",
        "source_born_subtraction": "NOT_PERFORMED",
        "ANSATZ_003": "FORBIDDEN",
        "Fisher_resources": "FORBIDDEN",
        "model_readiness_percent": 24,
        "next_gate_if_pass": "derive the matched conserved-source tree/Ward object using hphi2 plus this frozen h2phi2 K2 contact, classify pole/cut origin, then map to Iter582 q2-resolved operator coordinate before comparator subtraction",
    }

    outdir = Path("results/iteration583_source_k2")
    outdir.mkdir(parents=True, exist_ok=True)
    result_path = outdir / "result.json"
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    digest = hashlib.sha256(result_path.read_bytes()).hexdigest()
    audit = {
        "iteration": 583,
        "result_sha256": digest,
        "classification": "PASS_RAW_AUTHORITY_AUDIT_ITER583_SOURCE_K2" if not failures else "FAIL_RAW_AUTHORITY_AUDIT_ITER583_SOURCE_K2",
        "failures": failures,
    }
    (outdir / "authority_audit.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if failures:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
