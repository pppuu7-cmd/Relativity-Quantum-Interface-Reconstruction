"""RQIR Iteration 014: correlated calibration covariance and slow-drift diagnostics.

Builds on Iterations 012-013.  Two tasks are separated deliberately:
1) replace diagonal calibration covariance by class-wise equicorrelated blocks;
2) compute first-order coupling of probe-position and source-phase drift to the
   exact-null source direction.

The equicorrelation model is a design stress test, not a hardware covariance
forecast.  Drift bounds are standardized to the row-normalized calibration
coordinates used by the current Toy009/Iteration-011 likelihood.
"""
from __future__ import annotations
import numpy as np
import physical_resource_budget_iteration012 as r
import heterogeneous_calibration_allocation_iteration013 as h

TARGET=0.90
N_MEAN=14
N_COV=8


def compound_inverse(n:int,rho:float)->np.ndarray:
    c=(1-rho)*np.eye(n)+rho*np.ones((n,n))
    return np.linalg.inv(c)


def correlated_group_matrices(m,rho_mean=0.0,rho_cov=0.0):
    labels=m['labels']; ac=m['Ac']
    im=[i for i,x in enumerate(labels) if x=='mean']
    ic=[i for i,x in enumerate(labels) if x=='cov']
    ix=[i for i,x in enumerate(labels) if x in ('trace','energy')]
    am=ac[im]; av=ac[ic]; af=ac[ix]
    mf=1e12*(af.T@af)
    mm=am.T@compound_inverse(len(im),rho_mean)@am
    mc=av.T@compound_inverse(len(ic),rho_cov)@av
    return mf,mm,mc


def profiled(ss,bu,mats,gm,gc):
    mf,mm,mc=mats
    fuu=bu.T@bu+mf+gm*mm+gc*mc
    cross=ss@bu
    return float(ss@ss-cross@np.linalg.pinv(fuu,rcond=1e-12)@cross)


def required_cov(ss,bu,mats,gm,target=TARGET):
    lo,hi=1e1,1e10
    if profiled(ss,bu,mats,gm,hi)<target: return np.inf
    for _ in range(40):
        mid=np.sqrt(lo*hi)
        if profiled(ss,bu,mats,gm,mid)>=target: hi=mid
        else: lo=mid
    return hi


def optimize(ss,bu,mats,qratio=1.0):
    best=(np.inf,np.nan,np.nan)
    for gm in np.logspace(3,8,550):
        gc=required_cov(ss,bu,mats,float(gm))
        if np.isfinite(gc):
            cost=N_MEAN*gm+N_COV*gc/qratio
            if cost<best[0]: best=(float(cost),float(gm),float(gc))
    return best


def normalized_A(y1=r.Y1,dt=0.0):
    p=[r.probe(0.0),r.probe(y1)]
    tt=r.TIMES+dt; tr=r.TR+dt
    rows=[r.herm_vec(np.eye(r.D)),r.herm_vec(r.H)]
    for k in (0,1):
        for t in tt: rows.append(r.herm_vec(r.evolve(p[k],float(t))))
    rows.append(r.herm_vec(r.sym(r.evolve(p[0],tr),p[0])))
    extra=[(0,1,tt[1]),(1,1,tt[5]),(1,0,tr),(0,1,tr),
           (1,0,tt[3]),(0,0,tt[6]),(0,1,tt[6])]
    for k,l,t in extra:
        rows.append(r.herm_vec(r.sym(r.evolve(p[k],float(t)),p[l])))
    a=np.vstack(rows)
    return a/np.linalg.norm(a,axis=1,keepdims=True)


def drift_vectors(m,step=1e-5):
    # Reconstruct the physical exact-null state direction used in Iteration 012.
    _,_,vh=np.linalg.svd(m['A'],full_matrices=True)
    n=vh[-1]; d0=r.mat(n)
    d0/=np.max(np.abs(np.linalg.eigvalsh(d0)))
    theta0=2*r.EPS*r.herm_vec(d0)
    dy=(normalized_A(r.Y1+step,0)-normalized_A(r.Y1-step,0))/(2*step)
    dt=(normalized_A(r.Y1,step)-normalized_A(r.Y1,-step))/(2*step)
    return dy@theta0,dt@theta0


def conservative_drift_bounds(m,gm,gc,fraction=0.1):
    labels=m['labels']; im=[i for i,x in enumerate(labels) if x=='mean']; ic=[i for i,x in enumerate(labels) if x=='cov']
    vy,vt=drift_vectors(m)
    sm=1/np.sqrt(gm); sc=1/np.sqrt(gc)
    by=min(fraction*sm/np.max(np.abs(vy[im])),fraction*sc/np.max(np.abs(vy[ic])))
    bt=min(fraction*sm/np.max(np.abs(vt[im])),fraction*sc/np.max(np.abs(vt[ic])))
    return by,bt,vy,vt


def main():
    m=h.extended_model(); d1=(m['s'],m['Bu']); d2=h.d2_model(m)
    base={}
    for name,branch in [('D1',d1),('D2',d2)]:
        print(name)
        for rho in [0.0,0.01,0.05,0.10]:
            mats=correlated_group_matrices(m,rho,rho)
            best=optimize(*branch,mats)
            if rho==0: base[name]=best[0]
            print(' rho=',rho,'cost=',best[0],'gm=',best[1],'gc=',best[2],
                  'ratio_to_uncorrelated=',best[0]/base[name])

    # Use recorded q_mean=q_cov=1 optimized allocations for drift scale diagnostics.
    for name,gm,gc in [('D1',1.82e5,3.49e5),('D2',1.70e5,1.00e6)]:
        by,bt,vy,vt=conservative_drift_bounds(m,gm,gc,0.1)
        print(name,'10pct-noise drift bounds: dy=',by,'d_tau=',bt)
        print(' derivative norms position/time=',np.linalg.norm(vy),np.linalg.norm(vt))
        for f in [1.,100.,1000.]:
            print('  gap_Hz=',f,'timing_bound_s=',bt/(2*np.pi*f))

    # First-order multiplicative gain drift is zero at the exact null because
    # d[g(A theta)]/dg = A theta = 0 for theta=theta0.
    assert np.max(np.abs(m['A'] @ (2*r.EPS*r.herm_vec(r.mat(np.linalg.svd(m['A'],full_matrices=True)[2][-1]))))) < 1e-12

if __name__=='__main__': main()
