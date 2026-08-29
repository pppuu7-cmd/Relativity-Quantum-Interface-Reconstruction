"""RQIR Iteration 017: second-order nonlinear calibration-bias audit.

Uses the corrected hard-constrained 22D source-nuisance basis from Iteration
015 and the explicit low-rank systematics model from Iteration 016.

Audits three terms that are absent from the first-order Fisher model:
  (1) 0.5 * delta_tau^2 * A_{tau tau} theta0,
  (2) delta_g * A * delta_theta,
  (3) delta_g * delta_tau * A_tau theta0.

The reported gain-state RMS uses the *linear posterior covariance* of the 22
orthogonal source nuisance coordinates. It is therefore a local design
quantity, not a global bound for arbitrary preparation error.
"""
from __future__ import annotations
import numpy as np
import hard_constraint_fisher_audit_iteration015 as a
import correlated_calibration_drift_iteration014 as d
import low_rank_systematics_fisher_iteration016 as l


def timing_second_derivative(m, step=1e-4):
    """Return d^2[A(theta0)]/d tau^2 in row-normalized coordinates."""
    _,_,vh=np.linalg.svd(m['A'],full_matrices=True)
    n=vh[-1]
    d0=d.r.mat(n)
    d0/=np.max(np.abs(np.linalg.eigvalsh(d0)))
    theta0=2*d.r.EPS*d.r.herm_vec(d0)
    ap=d.normalized_A(d.r.Y1,+step)
    a0=d.normalized_A(d.r.Y1,0.0)
    am=d.normalized_A(d.r.Y1,-step)
    return ((ap-2*a0+am)/(step*step))@theta0


def joint_system(s,bu,acz,v,im,ic,gm,gc,sigsys):
    """Linearized joint beta/source/systematics Fisher and calibration Jacobian."""
    ww=np.zeros(acz.shape[0]); ww[im]=gm; ww[ic]=gc
    jd=np.column_stack([s,bu,np.zeros((len(s),v.shape[1]))])
    jc=np.column_stack([np.zeros(acz.shape[0]),acz,v])
    f=jd.T@jd + jc.T@(ww[:,None]*jc)
    f[1+bu.shape[1]:,1+bu.shape[1]:]+=np.diag(1/np.asarray(sigsys,float)**2)
    return f,ww,jc


def audit_branch(s,bu,acz,v,im,ic,gm,gc,sigsys,vtt):
    f,ww,jc=joint_system(s,bu,acz,v,im,ic,gm,gc,sigsys)
    c=np.linalg.inv(f)
    sigma_beta=float(np.sqrt(c[0,0]))
    retained=float(1/c[0,0])

    # Unmodeled quadratic timing residual.
    qcoef=0.5*vtt
    beta_tau2=float((c@(jc.T@(ww*qcoef)))[0])  # bias = beta_tau2 * delta_tau^2
    dt=float(sigsys[1])
    bias_tau2=beta_tau2*dt*dt
    dt_01=float(np.sqrt(0.1*sigma_beta/abs(beta_tau2)))

    # Bilinear common-gain x source-nuisance term.  For a true reduced source
    # nuisance u, q_gain = delta_g * Acz u.  Convert this into beta bias.
    m=jc.T@(ww[:,None]*acz)
    lvec=(c@m)[0]
    cu=c[1:1+bu.shape[1],1:1+bu.shape[1]]
    rms_gain_coeff=float(np.sqrt(lvec@cu@lvec))
    dg_01=float(0.1*sigma_beta/rms_gain_coeff)

    # Gain x timing cross-term q = delta_g * delta_tau * v_tau.
    vt=v[:,1]
    beta_gt=float((c@(jc.T@(ww*vt)))[0])
    gain1pct_timing_sigma=float(abs(beta_gt*0.01*dt)/sigma_beta)

    return dict(retained=retained,sigma_beta=sigma_beta,
                beta_tau2_coeff=beta_tau2,
                timing_bias_at_prior=bias_tau2,
                timing_bias_sigma=abs(bias_tau2)/sigma_beta,
                timing_01sigma_tau=dt_01,
                timing_01sigma_us_100Hz=dt_01/(2*np.pi*100)*1e6,
                timing_limit_over_prior=dt_01/dt,
                gain_state_rms_coeff=rms_gain_coeff,
                gain_01sigma=dg_01,
                gain_timing_1pct_bias_sigma=gain1pct_timing_sigma)


def main():
    m,im,ic,z,acz,v,d1,d2=l.model()
    vtt=timing_second_derivative(m)
    print('||v_tau_tau||=',np.linalg.norm(vtt))
    print('max mean/cov |v_tau_tau|=',np.max(np.abs(vtt[im])),np.max(np.abs(vtt[ic])))

    branches={
      'D1':(d1,1.7219876e6,9.3814709e5,[0.472,5.95e-3,7.62e-5,1.03e-4]),
      'D2':(d2,2.4144544e6,9.2943956e5,[0.399,5.03e-3,6.44e-5,1.04e-4]),
    }
    out={}
    for name,((s,bu),gm,gc,sig) in branches.items():
        r=audit_branch(s,bu,acz,v,im,ic,gm,gc,np.asarray(sig),vtt)
        out[name]=r
        print('\n'+name)
        for k,val in r.items(): print(k,val)

    # Regression guards for the recorded current baseline.
    assert 0.899 < out['D1']['retained'] < 0.901
    assert 0.899 < out['D2']['retained'] < 0.901
    assert out['D1']['timing_bias_sigma'] < 5e-5
    assert out['D2']['timing_bias_sigma'] < 2e-5
    assert out['D1']['timing_limit_over_prior'] > 50
    assert out['D2']['timing_limit_over_prior'] > 100
    assert 0.30 < out['D1']['gain_01sigma'] < 0.35
    assert 0.30 < out['D2']['gain_01sigma'] < 0.35
    assert out['D1']['gain_timing_1pct_bias_sigma'] < 3e-5
    assert out['D2']['gain_timing_1pct_bias_sigma'] < 5e-5

if __name__=='__main__': main()
