"""RQIR Iteration 043: direct diffusive-measurement information/backaction proxy.

Purpose
-------
Iteration 042 converted the centered D2 mean target to a required standardized
single-cycle sensitivity xi_mu.  This script asks whether such mean information
can be treated as free when the same quantum source copy is also supposed to
retain the ordered-response signal.

Use the standard ideal diffusive measurement proxy for a normalized Hermitian
source observable M:

    dy = 2 sqrt(eta*kappa) <M> dt + dW,
    d rho/dt |_uncond = kappa D[M] rho,

with D[M]rho = M rho M - 1/2 {M^2,rho}.

For a local normalized mean coordinate with d<M>/du = 1 and constant score over
a measurement window T,

    I_u = 4 eta kappa T = xi_mu^2,

so the required dimensionless measurement/dephasing strength is

    zeta = kappa T = xi_mu^2/(4 eta).

Because the two same-time force observables G0,G1 commute, their ideal parallel
monitoring is modeled by applying both commuting dephasing channels with the
same zeta.  This is a deliberately simple backaction proxy, not a full D2
apparatus or stochastic-trajectory calculation.
"""
from __future__ import annotations

import numpy as np

D = 5
E = np.array([1., 2., 3., 4., 6.])
H = np.diag(E).astype(complex)
EPS = 0.08
Y1 = -3.7766873836695947
TIMES = np.array([0., 3.09855988, 3.45849306, 2.93830159,
                  4.13016958, 4.84480925, 4.99085067])
TR = float(TIMES[2])

XI_SHARED_N4 = 1.2452864051788144      # Iteration 041 optimistic shared mean target
XI_MEAN_COV_CROSS = 2.7728040440172337 # Iteration 042 p=.5, dead=1ms crossover


def herm_vec(a):
    out = [a[i, i].real for i in range(D)]
    for i in range(D):
        for j in range(i + 1, D):
            out += [np.sqrt(2.0) * a[i, j].real,
                    np.sqrt(2.0) * a[i, j].imag]
    return np.asarray(out, float)


def mat(v):
    a = np.zeros((D, D), complex)
    k = 0
    for i in range(D):
        a[i, i] = v[k]
        k += 1
    for i in range(D):
        for j in range(i + 1, D):
            a[i, j] = (v[k] + 1j * v[k + 1]) / np.sqrt(2.0)
            a[j, i] = a[i, j].conjugate()
            k += 2
    return a


def evolve(a, t):
    return a * np.exp(1j * (E[:, None] - E[None, :]) * t)


def sym(a, b):
    return (a @ b + b @ a) / 2.0


def source_geometry():
    rng = np.random.default_rng(314159)
    for _ in range(812):
        x = rng.normal(size=(D, D))
        braw = (x + x.T) / 2.0
    ev = np.linalg.eigvalsh(braw)
    bpos = braw + (-ev.min() + 1.0) * np.eye(D)
    vals, v = np.linalg.eigh(bpos)
    return vals, v, float(vals.max())


VALS, V, SCALE = source_geometry()


def probe(y):
    return (V @ np.diag(1.0 / np.abs(SCALE / VALS - y)) @ V.T).astype(complex)


def grad_probe(y):
    r = SCALE / VALS - y
    return (V @ np.diag(1.0 / r**2) @ V.T).astype(complex)


def hidden_operator():
    p = [probe(0.0), probe(Y1)]
    rows = [herm_vec(np.eye(D)), herm_vec(H)]
    for k in (0, 1):
        for t in TIMES:
            rows.append(herm_vec(evolve(p[k], float(t))))
    rows.append(herm_vec(sym(evolve(p[0], TR), p[0])))
    extra = [
        (0, 1, TIMES[1]), (1, 1, TIMES[5]), (1, 0, TR),
        (0, 1, TR), (1, 0, TIMES[3]), (0, 0, TIMES[6]),
        (0, 1, TIMES[6]),
    ]
    for k, l, t in extra:
        rows.append(herm_vec(sym(evolve(p[k], float(t)), p[l])))
    A = np.vstack(rows)
    A /= np.linalg.norm(A, axis=1, keepdims=True)
    _, _, vh = np.linalg.svd(A, full_matrices=True)
    d0 = mat(vh[-1])
    d0 /= np.max(np.abs(np.linalg.eigvalsh(d0)))
    return d0


def harmonic(delta, readout, pump, n):
    rw = np.zeros_like(readout, complex)
    for i in range(D):
        for j in range(D):
            if int(round(E[i] - E[j])) == n:
                rw[i, j] = readout[i, j]
    return 2.0 * np.trace(delta @ ((rw @ pump - pump @ rw) / (2j)))


def detector_matrix(theta0):
    grad = (V @ np.diag((VALS / SCALE)**2) @ V.T).astype(complex)
    p0 = probe(0.0)
    B = np.zeros((4, D * D), float)
    for j in range(D * D):
        e = np.zeros(D * D)
        e[j] = 1.0
        op = mat(e)
        h2 = harmonic(op, grad, p0, 2)
        h4 = harmonic(op, grad, p0, 4)
        B[:, j] = [h2.real, h2.imag, h4.real, h4.imag]
    B /= np.linalg.norm(B @ theta0)
    return B


def dephase(rho, M, zeta):
    # Exact exp[zeta D[M]] for a time-independent Hermitian M.
    w, U = np.linalg.eigh(M)
    rt = U.conj().T @ rho @ U
    gaps = w[:, None] - w[None, :]
    rt *= np.exp(-0.5 * zeta * gaps**2)
    return U @ rt @ U.conj().T


def zeta_for_information(xi, eta=1.0):
    if not (0 < eta <= 1):
        raise ValueError("eta must be in (0,1]")
    return xi * xi / (4.0 * eta)


def response_after_parallel_force_monitoring(xi, eta=1.0):
    d0 = hidden_operator()
    rho0 = np.eye(D) / D
    rp = rho0 + EPS * d0
    rm = rho0 - EPS * d0
    theta0 = herm_vec(rp - rm)
    B = detector_matrix(theta0)
    s0 = B @ theta0

    g0 = grad_probe(0.0)
    g1 = grad_probe(Y1)
    m0 = g0 / np.linalg.norm(g0, ord="fro")
    m1 = g1 / np.linalg.norm(g1, ord="fro")
    assert np.linalg.norm(m0 @ m1 - m1 @ m0, ord="fro") < 1e-12

    zeta = zeta_for_information(xi, eta)
    rpp = dephase(dephase(rp, m0, zeta), m1, zeta)
    rmm = dephase(dephase(rm, m0, zeta), m1, zeta)
    s = B @ herm_vec(rpp - rmm)
    norm_ratio = float(np.linalg.norm(s) / np.linalg.norm(s0))
    alignment = float((s0 @ s) / (np.linalg.norm(s0) * np.linalg.norm(s)))

    # First-order purity-loss coefficient for one normalized channel.
    c0 = np.linalg.norm(m0 @ rp - rp @ m0, ord="fro")**2
    c1 = np.linalg.norm(m1 @ rp - rp @ m1, ord="fro")**2
    return zeta, norm_ratio, alignment, float(c0), float(c1)


def main():
    # Weak shared target from Iteration 041.
    z1, r1, a1, c0, c1 = response_after_parallel_force_monitoring(XI_SHARED_N4, 1.0)
    print("shared-N4 xi,zeta,response ratio,alignment", XI_SHARED_N4, z1, r1, a1)
    print("purity-loss coefficients G0/G1", c0, c1)
    assert abs(z1 - 0.3876845577307936) < 1e-12
    assert abs(r1 - 0.856964482097826) < 1e-12
    assert abs(a1 - 0.9987514942540938) < 1e-12
    assert abs(c0 - 0.004332249390047242) < 1e-15
    assert abs(c1 - 0.0013035508855091815) < 1e-15

    # Mean-vs-covariance wall-time crossover target from Iteration 042.
    z2, r2, a2, _, _ = response_after_parallel_force_monitoring(XI_MEAN_COV_CROSS, 1.0)
    print("mean/cov crossover xi,zeta,response ratio,alignment", XI_MEAN_COV_CROSS, z2, r2, a2)
    assert abs(z2 - 1.9221105666295812) < 1e-12
    assert abs(r2 - 0.4934501192248995) < 1e-12
    assert abs(a2 - 0.9569250475442282) < 1e-12

    # Efficiency penalty at fixed required information.
    expected = {
        0.8: (2.4026382082869766, 0.42595775989813345, 0.9274394282010946),
        0.5: (3.8442211332591625, 0.29953646396568423, 0.7932486611342773),
        0.2: (9.610552833147906, 0.15770892331672834, 0.3311391153022003),
    }
    for eta, vals in expected.items():
        z, r, a, _, _ = response_after_parallel_force_monitoring(XI_MEAN_COV_CROSS, eta)
        print("eta", eta, "zeta", z, "response ratio", r, "alignment", a)
        assert abs(z - vals[0]) < 1e-12
        assert abs(r - vals[1]) < 1e-12
        assert abs(a - vals[2]) < 1e-12


if __name__ == "__main__":
    main()
