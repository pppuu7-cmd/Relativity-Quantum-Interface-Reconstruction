"""RQIR Paper III — atom-interferometer calibration hierarchy audit.

Purpose
-------
Refine the physical self-calibration gate by separating two questions:
(1) are all apparatus metrology parameters identifiable? and
(2) is the RQIR science amplitude theta identifiable after profiling them?

Leading light-pulse scalings used here are structural, not an apparatus forecast:

    acceleration science: phi_s ~ n * k * T^2 * theta
    known acceleration reference: phi_a ~ n * k * T^2 * a_ref
    recoil calibration: phi_r ~ n^2 * k^2 * T * C_rec

The acceleration and recoil exponent vectors in fractional k,T errors are
(1,2) and (2,1), respectively. Published Ramsey-Borde/LMT geometries contain
both gravity- and recoil-sensitive phases with precisely these distinct leading
powers (sequence-dependent prefactors omitted here).

The key RQIR result is subtler than full-rank apparatus calibration:
- science only: theta is non-identifiable;
- science + recoil only: total rank rises, but the remaining null direction
  contains theta, so absolute theta is still non-identifiable if k and T are
  both free;
- science + a known modulated acceleration reference: the remaining null
  direction is purely internal to (k,T), so theta IS identifiable even though
  k and T are not individually separated;
- science + acceleration reference + recoil: theta, k and T are all locally
  identifiable at first order.

Thus Paper III resource closure should require identifiability of the exact
calibration combination multiplying the science observable, not necessarily
individual identifiability of every apparatus parameter.

Physical scaling references:
- Hogan, Johnson & Kasevich, Light-pulse atom interferometry, arXiv:0806.3261.
- Lan et al., Phys. Rev. Lett. 108, 090402 (2012): simultaneous conjugate
  Ramsey-Borde/LMT geometry with gravity phase proportional to n k g times a
  quadratic time combination and recoil phase proportional to n^2 k^2 T.
- Practical Limits for Large-Momentum-Transfer Clock Atom Interferometers,
  PRX Quantum 3, 030348 (2022): leading inertial phase ~ n k g T^2.

This file is a local structural/rank audit. It does not claim apparatus-specific
covariance/resource closure.
"""
from __future__ import annotations

import numpy as np

PARAMETERS = ("theta", "eps_k", "eps_T")


def science_row(theta: float = 0.2) -> np.ndarray:
    """Linearized normalized science phase derivatives [theta, eps_k, eps_T]."""
    return np.array([1.0, theta, 2.0 * theta], dtype=float)


def recoil_row() -> np.ndarray:
    """Known recoil calibration observable: fractional direction 2 eps_k+eps_T."""
    return np.array([0.0, 2.0, 1.0], dtype=float)


def acceleration_reference_row(amplitude: float = 1.0) -> np.ndarray:
    """Known reference acceleration probes the exact science scale eps_k+2 eps_T."""
    return np.array([0.0, amplitude, 2.0 * amplitude], dtype=float)


def nullspace(matrix: np.ndarray, rtol: float = 1e-12) -> np.ndarray:
    """Return an orthonormal basis for the right nullspace."""
    _, singular, vh = np.linalg.svd(matrix, full_matrices=True)
    if singular.size == 0:
        return np.eye(matrix.shape[1])
    tol = rtol * singular[0]
    rank = int(np.sum(singular > tol))
    return vh[rank:].T


def theta_identifiable(matrix: np.ndarray, tol: float = 1e-10) -> bool:
    """Theta is identifiable iff every local null direction has zero theta component."""
    ns = nullspace(matrix)
    if ns.size == 0:
        return True
    return bool(np.all(np.abs(ns[0, :]) <= tol))


def audit_case(name: str, rows: list[np.ndarray]) -> dict[str, object]:
    matrix = np.vstack(rows)
    rank = int(np.linalg.matrix_rank(matrix, tol=1e-12))
    ns = nullspace(matrix)
    identifiable = theta_identifiable(matrix)
    return {
        "name": name,
        "rank": rank,
        "n_parameters": matrix.shape[1],
        "theta_identifiable": identifiable,
        "nullity": int(ns.shape[1]),
        "nullspace": ns,
    }


def hierarchy(theta: float = 0.2) -> list[dict[str, object]]:
    s = science_row(theta)
    r = recoil_row()
    a = acceleration_reference_row()
    return [
        audit_case("science_only", [s]),
        audit_case("science_plus_recoil", [s, r]),
        audit_case("science_plus_acceleration_reference", [s, a]),
        audit_case("science_plus_reference_plus_recoil", [s, a, r]),
    ]


def structural_assertions() -> None:
    results = {case["name"]: case for case in hierarchy()}

    assert results["science_only"]["rank"] == 1
    assert not results["science_only"]["theta_identifiable"]

    # Recoil adds an independent metrology direction but leaves one null mode
    # whose theta component is nonzero. Therefore it does not by itself close
    # the absolute science-amplitude gate when k and T are both free.
    assert results["science_plus_recoil"]["rank"] == 2
    assert not results["science_plus_recoil"]["theta_identifiable"]

    # A known acceleration reference probes exactly k*T^2. The residual null
    # mode is proportional to (0,-2,+1): k and T can trade against each other,
    # but theta cannot move along that null mode.
    ref_case = results["science_plus_acceleration_reference"]
    assert ref_case["rank"] == 2
    assert ref_case["theta_identifiable"]
    ns = ref_case["nullspace"]
    assert ns.shape == (3, 1)
    assert abs(float(ns[0, 0])) < 1e-10
    assert abs(float(ns[1, 0] + 2.0 * ns[2, 0])) < 1e-10

    # Adding recoil to the known reference resolves k and T separately too.
    full_case = results["science_plus_reference_plus_recoil"]
    assert full_case["rank"] == 3
    assert full_case["theta_identifiable"]
    assert full_case["nullity"] == 0

    # Exponent vectors are independent: det [[1,2],[2,1]] = -3.
    exponent_matrix = np.array([[1.0, 2.0], [2.0, 1.0]])
    assert abs(float(np.linalg.det(exponent_matrix)) + 3.0) < 1e-12


def print_audit() -> None:
    print("RQIR atom-interferometer calibration hierarchy")
    print("parameters: theta, eps_k, eps_T")
    print("case                                  rank nullity theta-identifiable")
    for case in hierarchy():
        print(
            f"{case['name']:38s} "
            f"{case['rank']:4d} {case['nullity']:7d} "
            f"{str(case['theta_identifiable']):>18s}"
        )
        if case["nullity"]:
            ns = case["nullspace"]
            for j in range(ns.shape[1]):
                vec = ns[:, j]
                print("  null:", " ".join(f"{x:+.8f}" for x in vec))

    print("\nInterpretation:")
    print("science only:                         FAIL absolute-amplitude identifiability")
    print("science + recoil:                    FAIL absolute-amplitude identifiability")
    print("science + known acceleration ref:    PASS theta identifiability; k/T internal null remains")
    print("science + reference + recoil:        PASS full local theta/k/T identifiability")
    print("Paper-III rule: calibrate the science scale combination, not necessarily every knob.")


def main() -> None:
    structural_assertions()
    print_audit()


if __name__ == "__main__":
    main()
