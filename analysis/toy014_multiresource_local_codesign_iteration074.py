"""RQIR Iteration 074: executed Toy014 physical multi-resource local co-design.

Search provenance (executed 2026-08-30):
- exact-spectrum nearest-neighbour Jacobi/Lanczos source family;
- global cheap scan: 30,000 candidates, seed 20260830074;
- local refinement: seed 202608300741 around global anchors
  (7383, 8984, 8503), 1500 mutations per anchor;
- cheap filters protected s_min, physical two-band S_eff, harmonic balance and
  Ramsey accessibility;
- top 120 local survivors by the declared cheap composite were audited with
  Iteration-063 spectral-tilt-profiled centered calibration Fisher;
- retained minimax-balanced point: anchor 8984, local mutation 578.

This file stores the final candidate coordinates and independently rebuilds all
scientific checks using the established repository machinery.  It does not
claim a global optimum of the local source manifold.
"""
from __future__ import annotations

import numpy as np

import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54
import d2_spectral_tilt_profiled_calibration_iteration063 as i63

Q0 = np.array([
    0.276628448462335,
    0.692706589526471,
    0.133811514954169,
    0.242173595051988,
    0.605871859928477,
])
Y1 = -5.776797810075849
TIMES = np.array([
    0.0,
    1.282219941742947,
    1.828517907056411,
    3.566406614507335,
    3.168865574324793,
    4.280901503306583,
    2.751657214339520,
])

# Prior local physical reference factors used only for Pareto checks.
TOY011_RESPONSE = (1.0/0.1558200714788344, 21.7, 1.0/0.2660)
TOY011_CONDITIONING = (1.0/0.08163415302222209, 8.83, 1.0/0.4195)
TOY012_HIGH = (1.0/1.2139856294e-4, 490.0, 1.0/1.150503)  # conservative q_cal
TOY013 = (23.64956630775, 0.1233011369, 330.9066843)


def dominates(a, b):
    return all(x <= y for x, y in zip(a, b)) and any(x < y for x, y in zip(a, b))


def main():
    Q = t11.lanczos_q(Q0)
    assert Q is not None

    pack, B, s, tilt, seff = i63.physical_pack(Q, Y1, TIMES)
    base_pack, base_B, base_s, base_tilt, base_seff = i63.physical_pack(
        t11.V009_SORTED, t11.Y1_BASE, t11.TIMES_BASE
    )

    # Same 900-point group allocation convention as Iteration 063.
    _gu, best = i63.optimize(pack, B, s, tilt)
    _bgu, best_base = i63.optimize(base_pack, base_B, base_s, base_tilt)
    cal_ratio = best[0] / best_base[0]

    fq = i54.qfi_alpha(pack['d0'])
    fe = i54.energy_fisher_alpha(pack['d0'])
    phi, ramsey_coeff = i54.ramsey_rate_optimum(pack['d0'])
    bphi, base_ramsey_coeff = i54.ramsey_rate_optimum(base_pack['d0'])
    ramsey_ratio = ramsey_coeff / base_ramsey_coeff

    seff_ratio = seff / base_seff
    q_science = 1.0 / seff_ratio
    q_source = 1.0 / ramsey_ratio
    resource_vector = (q_science, cal_ratio, q_source)

    print('Toy014 q0', Q0)
    print('Toy014 y1', Y1)
    print('Toy014 phases', TIMES)
    print('S_eff / Toy009', seff_ratio, 'science time factor', q_science)
    print('calibration cost / Toy009', cal_ratio, 'best', best)
    print('FQ, FE', fq, fe)
    print('Ramsey phi/coeff/ratio/source-time', phi, ramsey_coeff, ramsey_ratio, q_source)
    print('resource vector', resource_vector)

    # Exact locality / state / null checks.
    Hsite = Q.T @ np.diag(t11.E) @ Q
    far = Hsite.copy()
    for i in range(t11.D):
        for j in range(t11.D):
            if i == j or abs(i-j) == 1:
                far[i,j] = 0.0
    rho0 = np.eye(t11.D) / t11.D
    rp = rho0 + t11.EPS * pack['d0']
    rm = rho0 - t11.EPS * pack['d0']
    residual = np.max(np.abs(pack['A'] @ t11.herm_vec(rp-rm)))
    ftilt = float(s@s - (s@tilt)**2/(tilt@tilt))

    # Harmonic balance uses the physical hidden-pair response.
    delta = 2.0*t11.EPS*pack['d0']
    g2 = t11.harmonic(delta, pack['g0'], pack['p0'], 2)
    g4 = t11.harmonic(delta, pack['g0'], pack['p0'], 4)
    p2, p4 = abs(g2)**2, abs(g4)**2
    balance = min(p2,p4)/max(p2,p4)

    print('far norm', np.linalg.norm(far))
    print('state minima', np.linalg.eigvalsh(rp).min(), np.linalg.eigvalsh(rm).min())
    print('null residual', residual, 'tilt-only profiled beta Fisher', ftilt)
    print('harmonic balance', balance)

    assert np.linalg.norm(far) < 2e-12
    assert np.linalg.eigvalsh(rp).min() > 0.12
    assert np.linalg.eigvalsh(rm).min() >= 0.12 - 2e-14
    assert residual < 1e-12
    assert abs(ftilt - 1.0) < 2e-9

    # Numerical regressions from the executed search/audit.
    assert abs(pack['sv'][-1] - 0.0014256442475958607) < 3e-14
    assert abs(pack['sv'][0]/pack['sv'][-1] - 3291.87304339187) < 5e-6
    assert abs(balance - 0.6684501117456428) < 3e-10
    assert abs(seff_ratio - 0.2830146574583767) < 3e-10
    assert abs(q_science - 3.5333858994461136) < 3e-9
    assert abs(best[0] - 101236980.16248292) / best[0] < 3e-6
    assert abs(cal_ratio - 3.484828228881006) < 3e-5
    assert abs(fq - 0.10159445627901414) < 3e-10
    assert abs(fe - 0.015323424512552968) < 3e-10
    assert abs(phi - 0.9264295097660072) < 3e-6
    assert abs(ramsey_coeff - 0.0037632915041337926) < 3e-10
    assert abs(ramsey_ratio - 1.4913343179877905) < 3e-6
    assert abs(q_source - 0.6705404602700137) < 3e-6

    # Major Pareto result: the balanced Toy014 point componentwise dominates
    # all pre-Toy013 local physical branches retained in Iteration 073.
    assert dominates(resource_vector, TOY011_RESPONSE)
    assert dominates(resource_vector, TOY011_CONDITIONING)
    assert dominates(resource_vector, TOY012_HIGH)
    assert not dominates(resource_vector, TOY013)
    assert not dominates(TOY013, resource_vector)

    # Toy014 vs unrestricted Toy009 boundary in the projected resource model:
    # q_s + q_c x + q_p y < 1+x+y.
    y0 = (q_science - 1.0) / (1.0 - q_source)
    slope = (cal_ratio - 1.0) / (1.0 - q_source)
    print('Toy014 beats Toy009 if y >', y0, '+', slope, '* x')
    assert abs(y0 - 7.68952969049) < 3e-4
    assert abs(slope - 7.54214367654) < 3e-4

    # Toy013 vs Toy014 local-only crossover:
    # Toy013 wins for x > x0 + m*y under these reference factors.
    x0 = (TOY013[0] - q_science) / (cal_ratio - TOY013[1])
    m = (TOY013[2] - q_source) / (cal_ratio - TOY013[1])
    print('Toy013 beats Toy014 if x >', x0, '+', m, '* y')
    assert abs(x0 - 5.98423866828) < 3e-4
    assert abs(m - 98.2399172792) < 3e-3


if __name__ == '__main__':
    main()
