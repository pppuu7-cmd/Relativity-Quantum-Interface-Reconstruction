"""RQIR Iteration 047: QND energy-basis source-metrology escape audit.

After reciprocal linear shared monitoring was strongly constrained, test the
simplest exact-QND alternative in the current five-level Toy009 source.
Because H has a nondegenerate spectrum, every Hermitian observable commuting
with H is diagonal in the energy basis.  The hard trace+energy constrained
diagonal tangent therefore has dimension 3.

This script checks three questions:
1. Can a complete diagonal/QND calibration basis close the remaining relational
   hard source null?
2. How much Fisher about the hidden amplitude alpha is available from a simple
   projective energy-basis population measurement?
3. Is such a QND measurement response-preserving on the *same* science copy?

The answer is: yes to (1), finite/useful information for (2), but no to (3).
Thus energy-basis metrology is attractive on independent/sacrificial copies,
not as a free same-copy science monitor.
"""
from __future__ import annotations

import numpy as np

import physical_coordinate_centered_covariance_audit_iteration034 as i34
import d2_information_backaction_proxy_iteration043 as i43
import source_preparation_qfi_iteration020 as i20

EPS = 0.08
C_BEST4 = 0.05006143859980483
C_NO_EXTRA_FORCE_COV = 4.55511


def qnd_diagonal_basis(i26) -> np.ndarray:
    # H is nondegenerate.  Hermitian QND observables [M,H]=0 are diagonal.
    # Remove identity and energy directions, leaving three hard-space rows.
    c = np.vstack([np.ones(i26.D), i26.E.astype(float)])
    _u, _s, vh = np.linalg.svd(c, full_matrices=True)
    d3 = vh[2:]
    rows = np.zeros((i26.D - 2, i26.D * i26.D), float)
    rows[:, :i26.D] = d3
    return rows


def energy_population_fisher(d0: np.ndarray, a: float) -> float:
    diag = np.real(np.diag(d0))
    p = np.ones(len(diag)) / len(diag) + a * diag
    if np.min(p) <= 0:
        raise ValueError("state not positive")
    return float(np.sum(diag * diag / p))


def energy_dephase(rho: np.ndarray) -> np.ndarray:
    return np.diag(np.diag(rho))


def main() -> None:
    i26 = i34.load("rqir_i26_for_i47", "d2_calibration_branch_fisher_iteration026.py")
    pack = i26.build()
    _A, _labels, _G, theta0, B, _s, Z, _Zu, _sv = pack

    # Relational centered branch at y_ref=-4 without force observables.
    yref = -4.0
    rm, rc = i34.operator_rows(
        i26,
        [i26.probe(0.0) - i26.probe(yref),
         i26.probe(i26.Y1) - i26.probe(yref)],
        centered=True,
    )
    rel = np.vstack([rm, rc])
    qnd = qnd_diagonal_basis(i26)
    rank_rel = int(np.linalg.matrix_rank(rel @ Z, 1e-12))
    rank_rel_qnd = int(np.linalg.matrix_rank(np.vstack([rel, qnd]) @ Z, 1e-12))
    print("relational hard rank", rank_rel, "/23")
    print("relational + complete QND diagonal rank", rank_rel_qnd, "/23")
    assert rank_rel == 22
    assert rank_rel_qnd == 23

    # QND diagonal rows do see the current hidden direction.
    qnd_hidden = qnd @ theta0
    print("QND hidden row vector", qnd_hidden, "norm", np.linalg.norm(qnd_hidden))
    assert abs(np.linalg.norm(qnd_hidden) - 0.08640472801687135) < 2e-12

    # Simple projective energy-basis population Fisher.
    d0 = i43.hidden_operator()
    fpa = energy_population_fisher(d0, +EPS)
    fma = energy_population_fisher(d0, -EPS)
    fp_alpha = EPS * EPS * fpa
    fm_alpha = EPS * EPS * fma
    fpair_alpha = fp_alpha + fm_alpha
    fq_a = i20.amplitude_qfi(EPS)
    fq_alpha = EPS * EPS * fq_a

    print("energy-basis F_a plus/minus", fpa, fma)
    print("energy-basis F_alpha plus/minus/pair", fp_alpha, fm_alpha, fpair_alpha)
    print("full QFI alpha", fq_alpha, "plus energy/QFI fraction", fp_alpha / fq_alpha)

    assert abs(fpa - 1.4674819318930217) < 2e-12
    assert abs(fma - 1.49673892898528) < 2e-12
    assert abs(fp_alpha - 0.00939188436411534) < 2e-14
    assert abs(fm_alpha - 0.009579129145505792) < 2e-14
    assert abs(fpair_alpha - 0.01897101350962113) < 3e-14
    assert abs(fp_alpha / fq_alpha - 0.1105807107) < 2e-9

    # Current preparation costs in accepted-copy equivalents.
    for c in (C_BEST4, C_NO_EXTRA_FORCE_COV, 9.0):
        n_plus = c / fp_alpha
        n_pair = c / fpair_alpha
        print("C_alpha", c, "energy-basis plus copies", n_plus,
              "plus/minus pair equivalents", n_pair)

    assert abs(C_BEST4 / fp_alpha - 5.330286943383) < 5e-9
    assert abs(C_BEST4 / fpair_alpha - 2.638838382274) < 5e-9
    assert 484.9 < C_NO_EXTRA_FORCE_COV / fp_alpha < 485.1
    assert 958.1 < 9.0 / fp_alpha < 958.4

    # Same-copy projective energy measurement is QND relative to H but fully
    # dephases energy coherences.  Quantify the ordered-response damage.
    rho0 = np.eye(i26.D) / i26.D
    rp = rho0 + EPS * d0
    rm_state = rho0 - EPS * d0
    s0 = B @ i26.herm_vec(rp - rm_state)
    sd = B @ i26.herm_vec(energy_dephase(rp) - energy_dephase(rm_state))
    retention = float(np.linalg.norm(sd) / np.linalg.norm(s0))
    alignment = float((s0 @ sd) / (np.linalg.norm(s0) * np.linalg.norm(sd)))
    print("same-copy projective energy readout response retention", retention,
          "alignment", alignment)
    assert abs(retention - 0.29848076260656375) < 2e-12
    assert abs(alignment - 0.8205247404963089) < 2e-12


if __name__ == "__main__":
    main()
