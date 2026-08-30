"""RQIR Iteration 118: exact calibration-span audit for Toy009 and Toy014.

Uses the established hard-constrained 22D source-nuisance basis.  Checks the
rank contribution of the seven same-time mean dual-probe layers and the eight
centered-covariance calibration rows.  No apparatus forecast/new-physics claim.
"""
from __future__ import annotations

import numpy as np

import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54
import toy014_multiresource_local_codesign_iteration074 as i74

TOL = 1e-10


def rank(a: np.ndarray) -> int:
    return int(np.linalg.matrix_rank(a, tol=TOL))


def pack_009():
    return i54.make_pack(t11.V009_SORTED, t11.Y1_BASE, t11.TIMES_BASE)


def pack_014():
    q = t11.lanczos_q(i74.Q0)
    assert q is not None
    return i54.make_pack(q, i74.Y1, i74.TIMES)


def audit(name: str, pack: dict) -> dict:
    zu = pack["Zu"]
    am = pack["pm"] @ zu   # 14 x 22 = seven same-time two-row mean layers
    ac = pack["pc"] @ zu   # 8 x 22 centered-covariance rows

    assert am.shape == (14, 22)
    assert ac.shape == (8, 22)

    mean_rank = rank(am)
    cov_rank = rank(ac)
    full = np.vstack([am, ac])
    full_rank = rank(full)

    # Sequential same-time mean-pair rank increments.
    kmat = np.zeros((22, 22))
    increments_mean = []
    rprev = 0
    for j in range(7):
        rows = np.vstack([am[j], am[7 + j]])
        assert rank(rows) == 2
        kmat += rows.T @ rows
        rnow = rank(kmat)
        increments_mean.append(rnow - rprev)
        rprev = rnow

    # Each covariance row is tested after the entire mean span is present.
    increments_cov = []
    for j in range(8):
        kmat += np.outer(ac[j], ac[j])
        rnow = rank(kmat)
        increments_cov.append(rnow - rprev)
        rprev = rnow

    # Conditioning of the complementary covariance directions.
    _u, sm, vh = np.linalg.svd(am, full_matrices=True)
    null_mean = vh[mean_rank:].T
    ac_null = ac @ null_mean
    sc = np.linalg.svd(ac_null, compute_uv=False)
    sall = np.linalg.svd(full, compute_uv=False)

    out = dict(
        mean_rank=mean_rank,
        cov_rank=cov_rank,
        full_rank=full_rank,
        increments_mean=increments_mean,
        increments_cov=increments_cov,
        mean_smin=float(sm[-1]),
        cov_null_smin=float(sc[-1]),
        full_smin=float(sall[-1]),
        full_cond=float(sall[0] / sall[-1]),
    )
    print(name, out)
    return out


def main() -> None:
    r9 = audit("Toy009", pack_009())
    r14 = audit("Toy014", pack_014())

    for r in (r9, r14):
        assert r["mean_rank"] == 14
        assert r["cov_rank"] == 8
        assert r["full_rank"] == 22
        assert r["increments_mean"] == [2] * 7
        assert r["increments_cov"] == [1] * 8

    # Deterministic conditioning regressions.
    assert abs(r9["mean_smin"] - 0.0033759149870998353) < 2e-12
    assert abs(r9["cov_null_smin"] - 0.0042337667) < 2e-8
    assert abs(r9["full_smin"] - 0.00212667906656026) < 2e-12
    assert abs(r9["full_cond"] - 409.92601352874055) < 2e-7

    assert abs(r14["mean_smin"] - 0.002125424583243324) < 2e-12
    assert abs(r14["cov_null_smin"] - 0.0023647500) < 2e-8
    assert abs(r14["full_smin"] - 0.0015010578878777172) < 2e-12
    assert abs(r14["full_cond"] - 650.5822168754169) < 3e-7


if __name__ == "__main__":
    main()
