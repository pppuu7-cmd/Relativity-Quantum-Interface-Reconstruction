"""RQIR Iteration 016: explicit low-rank calibration-systematics Fisher.

Runs only in the exact hard-constrained nuisance basis introduced in Iteration
015. Adds four calibration-systematics nuisance columns:
  dy      second-probe position drift,
  dtau    common source phase/time drift,
  b_mean  common additive offset on potential-mean rows,
  b_cov   common additive offset on covariance rows.

Shows that unconstrained low-rank systematics create a structural calibration
ambiguity that cannot be cured by more calibration shots alone, and tests a
finite control-prior bundle tied to statistical row uncertainty.

Second-order multiplicative gain-state coupling is intentionally not forced
into first-order Fisher; it belongs to the next nonlinear/bias audit.
"""
from __future__ import annotations
import numpy as np
import hard_constraint_fisher_audit_iteration015 as a
import correlated_calibration_drift_iteration014 as d


def model():
    m,im,ic,z,acz,bu1=a.reduced_model()
    s2,bu2=a.d2_reduced(m,z)
    vy,vt=d.drift_vectors(m)
    bm=np.zeros(len(m['labels'])); bm[im]=1.0
    bc=np.zeros(len(m['labels'])); bc[ic]=1.0
    v=np.column_stack([vy,vt,bm,bc])
    return m,im,ic,z,acz,v,(m['s'],bu1),(s2,bu2)


def retained(s,bu,acz,v,im,ic,gm,gc,prior_precision):
    w=np.zeros(len(im)+len(ic)+2)  # 24 rows total in current model
    # Build weight from actual row indices rather than assuming ordering.
    ww=np.zeros(acz.shape[0]); ww[im]=gm; ww[ic]=gc
    fuu=bu.T@bu+acz.T@(ww[:,None]*acz)
    fuz=acz.T@(ww[:,None]*v)
    fzz=v.T@(ww[:,None]*v)+np.diag(prior_precision)
    n=np.block([[fuu,fuz],[fuz.T,fzz]])
    cross=np.concatenate([s@bu,np.zeros(v.shape[1])])
    return float(s@s-cross@np.linalg.solve(n,cross))


def conservative_sigmas(v,im,ic,gm,gc,fraction=0.1):
    sm=1/np.sqrt(gm); sc=1/np.sqrt(gc)
    def drift_sigma(col):
        return min(fraction*sm/np.max(np.abs(col[im])),
                   fraction*sc/np.max(np.abs(col[ic])))
    # Common additive offset is already in row-normalized output units.
    return np.array([drift_sigma(v[:,0]),drift_sigma(v[:,1]),
                     fraction*sm,fraction*sc],float)


def main():
    m,im,ic,z,acz,v,d1,d2=model()
    # Corrected q=1 90% allocations from Iteration 015.
    branches={
        'D1':(d1,1.7219876e6,9.3814709e5),
        'D2':(d2,2.4144544e6,9.2943956e5),
    }
    for name,((s,bu),gm,gc) in branches.items():
        print('\n',name)
        # Unbounded systematics: no finite prior information.
        for scale in [1.0,2.0,10.0,100.0]:
            f=retained(s,bu,acz,v,im,ic,scale*gm,scale*gc,[0,0,0,0])
            print('calibration scale',scale,'no-prior retained F=',f)

        sig=conservative_sigmas(v,im,ic,gm,gc,0.1)
        prec=1/sig**2
        f=retained(s,bu,acz,v,im,ic,gm,gc,prec)
        print('10%-sigma control sigmas [dy,dtau,bmean,bcov]=',sig)
        print('retained F with bundle=',f)
        print('timing sigma us at 100 Hz=',sig[1]/(2*np.pi*100)*1e6)

        sig2=conservative_sigmas(v,im,ic,2*gm,2*gc,0.1)
        f2=retained(s,bu,acz,v,im,ic,2*gm,2*gc,1/sig2**2)
        print('2x calibration + matched control retained F=',f2)

        assert abs(f-0.9)<3e-4
        assert f2>0.94

    # Structural ambiguity: arbitrary systematics keep F_beta essentially zero
    # even when the calibration exposure is scaled by 100x.
    for (s,bu),gm,gc in [(d1,1.7219876e6,9.3814709e5),
                          (d2,2.4144544e6,9.2943956e5)]:
        assert abs(retained(s,bu,acz,v,im,ic,100*gm,100*gc,[0,0,0,0]))<1e-6

if __name__=='__main__': main()
