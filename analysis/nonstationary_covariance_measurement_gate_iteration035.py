"""RQIR Iteration 035: nonstationary/ordered covariance measurement gate.

Iteration 034 corrected the centered covariance derivative and source-QFI
coordinate. This iteration asks whether the remaining D2 covariance rows may be
assigned the stationary scalar PSD Fisher rate used as a screening formula in
Iteration 033.

For the current Toy009 hidden source the answer is no without an additional
measurement model: rho_+/- do not commute with H, the centered two-time
correlators are not stationary, and the high-value covariance operator pairs
are noncommuting. A physical rate must therefore come from an explicit
phase-referenced/cyclostationary detector-output likelihood or another declared
quantum correlation measurement protocol.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import numpy as np

# Preferred centered D2 benchmark from Iteration 034.
GAMMA_COV_CENTERED = 590127.2924902999
Q_OVER_RP_FIRST4 = 523969.5182744001
Q_OVER_RP_FIFTH = 11788061.012375014


def load(name: str, filename: str):
    path = Path(__file__).resolve().parent / filename
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def centered_covariance(i26, rho, a, b) -> float:
    ma = np.trace(rho @ a)
    mb = np.trace(rho @ b)
    da = a - ma * np.eye(i26.D)
    db = b - mb * np.eye(i26.D)
    return float(np.real(np.trace(rho @ i26.sym(da, db))))


def gaussian_vector_fisher(mean_deriv, sigma, sigma_deriv) -> float:
    """Per independent real-Gaussian vector sample Fisher for one parameter."""
    mean_deriv = np.asarray(mean_deriv, float)
    sigma = np.asarray(sigma, float)
    sigma_deriv = np.asarray(sigma_deriv, float)
    inv = np.linalg.inv(sigma)
    mean_term = float(mean_deriv @ inv @ mean_deriv)
    cov_term = 0.5 * float(np.trace(inv @ sigma_deriv @ inv @ sigma_deriv))
    return mean_term + cov_term


def cross_covariance_fisher(v1: float, v2: float, c: float, dc_du: float) -> float:
    """Per real bivariate-Gaussian sample Fisher when only cross-covariance varies."""
    det = v1 * v2 - c * c
    if det <= 0:
        raise ValueError("covariance matrix must be positive definite")
    return dc_du * dc_du * (v1 * v2 + c * c) / (det * det)


def paired_rate(i_shot: float, cycle_time_s: float,
                acceptance: float = 1.0, efficiency: float = 1.0) -> float:
    if cycle_time_s <= 0:
        raise ValueError("cycle_time_s must be positive")
    return acceptance * efficiency * i_shot / cycle_time_s


def break_even_shot_product(q_over_rp: float, fq_alpha: float) -> float:
    """Required I_cov,shot * (pC etaC/pP etaP) * (tP/tC)."""
    return q_over_rp * fq_alpha


def main():
    i26 = load("rqir_i26", "d2_calibration_branch_fisher_iteration026.py")
    i20 = load("rqir_i20", "source_preparation_qfi_iteration020.py")
    pack = i26.build()
    _A, _labels, _G, theta0, _B, _s, _Z, _Zu, _sv = pack

    d0 = i26.mat(theta0 / (2.0 * i26.EPS))
    rho0 = np.eye(i26.D) / i26.D
    rp = rho0 + i26.EPS * d0
    rm = rho0 - i26.EPS * d0

    # Stationarity test: [rho,H] must vanish for time-translation-invariant
    # two-time correlators under this closed source Hamiltonian.
    comm_plus = float(np.linalg.norm(rp @ i26.H - i26.H @ rp, ord="fro"))
    comm_minus = float(np.linalg.norm(rm @ i26.H - i26.H @ rm, ord="fro"))
    print("||[rho+,H]||F", comm_plus)
    print("||[rho-,H]||F", comm_minus)

    force_ops = [i26.grad_probe(0.0), i26.grad_probe(i26.Y1)]
    g0 = force_ops[0]

    def delta_n(t1: float, t2: float) -> float:
        a = i26.evolve(g0, t1)
        b = i26.evolve(g0, t2)
        return centered_covariance(i26, rp, a, b) - centered_covariance(i26, rm, a, b)

    base = delta_n(i26.TR, 0.0)
    shifted = delta_n(i26.TR + 1.0, 1.0)
    print("DeltaN(TR,0)", base)
    print("DeltaN(TR+1,1)", shifted)
    print("common-shift difference", shifted - base)

    # Ordering audit for the eight force-covariance pairs. The high-value rows
    # from Iterations 032/034 are 0,1,3,7.
    extra = [
        (0, 1, i26.TIMES[1]),
        (1, 1, i26.TIMES[5]),
        (1, 0, i26.TR),
        (0, 1, i26.TR),
        (1, 0, i26.TIMES[3]),
        (0, 0, i26.TIMES[6]),
        (0, 1, i26.TIMES[6]),
    ]
    pairs = [(0, 0, i26.TR)] + extra
    comm_norms = []
    for idx, (k, l, t) in enumerate(pairs):
        a = i26.evolve(force_ops[k], float(t))
        b = force_ops[l]
        c = a @ b - b @ a
        cn = float(np.linalg.norm(c, ord="fro"))
        comm_norms.append(cn)
        print("row", idx, "commutator Frobenius norm", cn)

    # Coordinate-correct source preparation Fisher per accepted single branch.
    fq_a = i20.amplitude_qfi(i26.EPS)
    fq_alpha = i26.EPS**2 * fq_a
    first4_product = break_even_shot_product(Q_OVER_RP_FIRST4, fq_alpha)
    fifth_product = break_even_shot_product(Q_OVER_RP_FIFTH, fq_alpha)
    print("FQ_alpha per accepted single branch", fq_alpha)
    print("first4 required Ishot*(eff ratio)*(tP/tC)", first4_product)
    print("fifth required Ishot*(eff ratio)*(tP/tC)", fifth_product)

    # Equal-efficiency transparent cycle-ratio examples. These are not
    # apparatus forecasts; they show what the break-even inequality asks of a
    # phase-referenced covariance measurement once I_shot is known.
    for ratio in (1e2, 1e3, 1e4, 1e5):
        print("tP/tC", ratio,
              "Ishot_first4_min", first4_product / ratio,
              "Ishot_fifth_min", fifth_product / ratio)

    # Verify the general Gaussian covariance Fisher formula against the closed
    # bivariate cross-covariance expression.
    v1, v2, c, dc = 2.0, 3.0, 0.4, 0.7
    sig = np.array([[v1, c], [c, v2]])
    dsig = np.array([[0.0, dc], [dc, 0.0]])
    fmat = gaussian_vector_fisher(np.zeros(2), sig, dsig)
    fclosed = cross_covariance_fisher(v1, v2, c, dc)
    print("Gaussian pair Fisher matrix/closed", fmat, fclosed)

    # Regression guards defining the physical gate.
    assert abs(comm_plus - 0.2406721120761444) < 2e-12
    assert abs(comm_minus - 0.2406721120761444) < 2e-12
    assert abs(base - (-0.0008450628522024828)) < 2e-15
    assert abs(shifted - (-0.004791833785887066)) < 2e-15
    assert abs(shifted - base) > 3e-3

    expected_high = {
        0: 0.5211898218591998,
        1: 0.006054857625693356,
        3: 0.01571662338718758,
        7: 0.011633270965998588,
    }
    for idx, val in expected_high.items():
        assert abs(comm_norms[idx] - val) < 2e-12
        assert comm_norms[idx] > 0.0

    assert abs(fq_alpha - 0.0849323916) < 3e-9
    assert 4.44e4 < first4_product < 4.46e4
    assert 1.00e6 < fifth_product < 1.01e6
    assert abs(fmat - fclosed) < 1e-14


if __name__ == "__main__":
    main()
