"""RQIR Iteration 075: Toy014 physical detector/control-systematics revalidation.

Rebuild geometry/timing/additive calibration nuisances for the executed Toy014
candidate inside the Iteration-063 spectral-tilt-profiled D2 detector metric.
No Toy009/Toy012 control prior is imported as a physical tolerance.
"""
from __future__ import annotations

import numpy as np

import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54
import d2_spectral_tilt_profiled_calibration_iteration063 as i63
import toy014_multiresource_local_codesign_iteration074 as i74

F_GAP_HZ = 100.0
DEAD_S = 1e-3
ACCEPTANCE = 0.5


def groups(Q, y1, times, dt=0.0, return_raw=False):
    p0, p1, _g0 = t11.operators(Q, y1)
    tt = np.asarray(times, float) + dt
    if not return_raw:
        return i54.operator_rows([p0, p1], tt)

    raw_m = []
    for op in (p0, p1):
        for t in tt:
            raw_m.append(t11.herm_vec(t11.evolve(op, float(t))))
    tr = float(tt[2])
    raw_c = [t11.herm_vec(i54.centered_sym(t11.evolve(p0, tr), p0))]
    ops = [p0, p1]
    extra = [
        (0,1,tt[1]), (1,1,tt[5]), (1,0,tr), (0,1,tr),
        (1,0,tt[3]), (0,0,tt[6]), (0,1,tt[6]),
    ]
    for k,l,t in extra:
        raw_c.append(t11.herm_vec(i54.centered_sym(t11.evolve(ops[k], float(t)), ops[l])))
    return np.vstack(raw_m), np.vstack(raw_c)


def drift_vectors(Q, y1, times, theta0, step=1e-5):
    mp, cp = groups(Q, y1+step, times)
    mm, cm = groups(Q, y1-step, times)
    dy_m = (mp-mm)/(2.0*step)
    dy_c = (cp-cm)/(2.0*step)

    mp, cp = groups(Q, y1, times, dt=step)
    mm, cm = groups(Q, y1, times, dt=-step)
    dt_m = (mp-mm)/(2.0*step)
    dt_c = (cp-cm)/(2.0*step)

    return np.r_[dy_m@theta0, dy_c@theta0], np.r_[dt_m@theta0, dt_c@theta0]


def conservative_sigmas(vy, vt, gm, gc, fraction=0.1):
    sm = 1.0/np.sqrt(gm)
    sc = 1.0/np.sqrt(gc)

    def one(col):
        return min(
            fraction*sm/np.max(np.abs(col[:14])),
            fraction*sc/np.max(np.abs(col[14:])),
        )

    return np.array([one(vy), one(vt), fraction*sm, fraction*sc])


def retained(s, B, tilt, Zu, Azu, Vsys, gm, gc, prior_precision, scale=1.0):
    # params: beta, 22 source nuisances, detector tilt, 4 calibration systematics
    n = 1+22+1+4
    F = np.zeros((n,n))

    Jd = np.zeros((4,n))
    Jd[:,0] = s
    Jd[:,1:23] = B@Zu
    Jd[:,23] = tilt
    F += Jd.T@Jd

    w = np.r_[np.full(14, gm*scale), np.full(8, gc*scale)]
    Jc = np.zeros((22,n))
    Jc[:,1:23] = Azu
    Jc[:,24:28] = Vsys
    F += Jc.T@(w[:,None]*Jc)
    F[24:28,24:28] += np.diag(prior_precision)

    N = F[1:,1:]
    cross = F[0,1:]
    return float(F[0,0] - cross@np.linalg.solve(N, cross))


def timing_reference_block_s(target_us, cycle_s, sigma_event_us=10.0,
                             acceptance=ACCEPTANCE):
    sigma_ref = target_us/3.0
    return cycle_s/acceptance*(sigma_event_us/sigma_ref)**2


def cadence_hours(target_us, diffusion_us2_per_h, sigma_ref_fraction=1.0/3.0,
                  floor_us=0.0):
    sigma_ref = sigma_ref_fraction*target_us
    numerator = target_us**2-floor_us**2-sigma_ref**2
    if numerator <= 0:
        return 0.0
    return 2.0*numerator/diffusion_us2_per_h


def main():
    Q = t11.lanczos_q(i74.Q0)
    pack, B, s, tilt, _seff = i63.physical_pack(Q, i74.Y1, i74.TIMES)
    _gu, best = i63.optimize(pack, B, s, tilt)
    _cost, gm, gc = best

    means, covs = groups(Q, i74.Y1, i74.TIMES)
    Azu = np.vstack([means,covs])@pack['Zu']
    vy, vt = drift_vectors(Q, i74.Y1, i74.TIMES, pack['theta0'])
    bmean = np.r_[np.ones(14), np.zeros(8)]
    bcov = np.r_[np.zeros(14), np.ones(8)]
    Vsys = np.column_stack([vy,vt,bmean,bcov])

    sig = conservative_sigmas(vy,vt,gm,gc)
    no_prior = [retained(s,B,tilt,pack['Zu'],Azu,Vsys,gm,gc,np.zeros(4),scale=x)
                for x in (1.0,2.0,10.0,100.0)]
    f = retained(s,B,tilt,pack['Zu'],Azu,Vsys,gm,gc,1.0/sig**2,scale=1.0)

    timing_us = sig[1]/(2.0*np.pi*F_GAP_HZ)*1e6
    t_coh = float(np.max(i74.TIMES))/(2.0*np.pi*F_GAP_HZ)
    cycle = t_coh + DEAD_S

    print('Toy014 physical gm/gc',gm,gc)
    print('no-prior retained F at exposure 1,2,10,100',no_prior)
    print('10% control sigmas [dy1,dtau,bmean,bcov]',sig)
    print('retained with bundle',f)
    print('timing target us @100Hz',timing_us)
    print('coherence/evolution max ms',1e3*t_coh)
    print('10us-event timing reference block s',timing_reference_block_s(timing_us,cycle))
    print('timing drift cadence h D=100/1000',cadence_hours(timing_us,100.0),cadence_hours(timing_us,1000.0))

    raw_m, raw_c = groups(Q,i74.Y1,i74.TIMES,return_raw=True)
    mnorm = np.linalg.norm(raw_m,axis=1)
    cnorm = np.linalg.norm(raw_c,axis=1)
    print('raw mean offset range',mnorm.min()*sig[2],mnorm.max()*sig[2])
    print('raw cov offset range',cnorm.min()*sig[3],cnorm.max()*sig[3])

    # Regression and structural gate checks.
    assert max(abs(x) for x in no_prior) < 3e-8
    assert abs(f-0.8999685964993578) < 3e-8
    assert abs(sig[0]-0.7413171761880402) < 3e-7
    assert abs(sig[1]-0.002498918767312161) < 3e-9
    assert abs(sig[2]-4.196762080936634e-5) < 3e-11
    assert abs(sig[3]-6.064869563042808e-5) < 3e-11
    assert abs(timing_us-3.9771527420283626) < 3e-6
    assert abs(t_coh-0.006813266351407684) < 3e-12
    assert abs(timing_reference_block_s(timing_us,cycle)-0.8891204391554294) < 3e-8
    assert abs(cadence_hours(timing_us,100.0)-0.2812043365941995) < 3e-8


if __name__ == '__main__':
    main()
