"""RQIR Iteration 015: hard-constraint Fisher audit.

Corrects a numerical pathology in Iterations 013-014. Trace and energy were
implemented there by a 1e12 penalty and then inverted with np.linalg.pinv.
For strongly heterogeneous gamma_mean/gamma_cov this scale separation can
truncate genuine weak nuisance directions and artificially inflate profiled
F_beta.

This script eliminates trace+energy constraints exactly by restricting the
24-dimensional source-nuisance coordinates to null(A_fixed Q). It then
recomputes heterogeneous allocation, correlated-covariance stress tests, and
conservative timing-drift bounds.

Scope: finite-dimensional Toy009/Iteration-011 model. This is a correction of
resource-allocation numerics, not a change to the exact NP3 construction.
"""
from __future__ import annotations
import numpy as np
import physical_resource_budget_iteration012 as r
import heterogeneous_calibration_allocation_iteration013 as h
import correlated_calibration_drift_iteration014 as d

TARGET=0.90
N_MEAN=14
N_COV=8


def reduced_model():
    m=h.extended_model()
    labels=np.asarray(m['labels'])
    im=np.where(labels=='mean')[0]
    ic=np.where(labels=='cov')[0]
    ix=np.where(np.isin(labels,['trace','energy']))[0]

    # m['Ac'] maps the 24 orthogonal source nuisance coordinates into
    # row-normalized calibration observables. Enforce trace+energy exactly.
    c=m['Ac'][ix]
    _,s,vh=np.linalg.svd(c,full_matrices=True)
    rank=int(np.sum(s>1e-12))
    z=vh[rank:].T
    assert rank==2 and z.shape==(24,22)
    assert np.max(np.abs(c@z))<1e-12

    return m,im,ic,z,m['Ac']@z,m['Bu']@z


def d2_reduced(m,z):
    s,bu=h.d2_model(m)
    return s,bu@z


def profiled(s,bu,am,av,gm,gc,rho=0.0):
    if rho==0:
        mm=am.T@am; mc=av.T@av
    else:
        mm=am.T@d.compound_inverse(len(am),rho)@am
        mc=av.T@d.compound_inverse(len(av),rho)@av
    fuu=bu.T@bu+gm*mm+gc*mc
    cross=s@bu
    return float(s@s-cross@np.linalg.solve(fuu,cross))


def required_cov(s,bu,am,av,gm,rho=0.0,target=TARGET):
    lo,hi=1e1,1e12
    if profiled(s,bu,am,av,gm,hi,rho)<target:
        return np.inf
    for _ in range(65):
        mid=np.sqrt(lo*hi)
        if profiled(s,bu,am,av,gm,mid,rho)>=target: hi=mid
        else: lo=mid
    return hi


def uniform_threshold(s,bu,am,av,target=TARGET):
    lo,hi=1e2,1e12
    for _ in range(65):
        mid=np.sqrt(lo*hi)
        if profiled(s,bu,am,av,mid,mid,0.0)>=target: hi=mid
        else: lo=mid
    return hi


def optimize(s,bu,am,av,rho=0.0,qratio=1.0,target=TARGET):
    gu=uniform_threshold(s,bu,am,av,target)
    best=((N_MEAN+N_COV/qratio)*gu,gu,gu)
    for gm in np.logspace(4,10,900):
        gc=required_cov(s,bu,am,av,float(gm),rho,target)
        if np.isfinite(gc):
            cost=N_MEAN*gm+N_COV*gc/qratio
            if cost<best[0]: best=(float(cost),float(gm),float(gc))
    return gu,best,(N_MEAN+N_COV/qratio)*gu/best[0]


def drift_bounds(m,gm,gc,fraction=0.1):
    labels=np.asarray(m['labels'])
    im=np.where(labels=='mean')[0]; ic=np.where(labels=='cov')[0]
    vy,vt=d.drift_vectors(m)
    sm=1/np.sqrt(gm); sc=1/np.sqrt(gc)
    def one(v):
        return min(fraction*sm/np.max(np.abs(v[im])),
                   fraction*sc/np.max(np.abs(v[ic])))
    return one(vy),one(vt),vy,vt


def main():
    m,im,ic,z,acz,bu1=reduced_model()
    am=acz[im]; av=acz[ic]
    branches={'D1':(m['s'],bu1),'D2':d2_reduced(m,z)}

    print('Hard-constraint dimension:',z.shape[1])
    print('Old Iteration-013 points evaluated with exact constraints:')
    for name,(s,bu) in branches.items():
        old=(1.82e5,3.49e5) if name=='D1' else (1.70e5,1.00e6)
        print(name,'old retained F=',profiled(s,bu,am,av,*old))

    corrected={}
    for name,(s,bu) in branches.items():
        gu,best,gain=optimize(s,bu,am,av)
        corrected[name]=best
        print('\n',name)
        print('uniform gamma=',gu)
        print('corrected optimal cost/gm/gc=',best)
        print('uniform/optimal cost gain=',gain)
        base=best[0]
        for rho in [0.01,0.05,0.10]:
            _,b,_=optimize(s,bu,am,av,rho=rho)
            print('rho=',rho,'cost ratio=',b[0]/base,'gm/gc=',b[1],b[2])

    for name,(cost,gm,gc) in corrected.items():
        by,bt,vy,vt=drift_bounds(m,gm,gc)
        print('\n',name,'corrected 10%-sigma bounds dy=',by,'dtau=',bt,
              'timing_us_at_100Hz=',bt/(2*np.pi*100)*1e6)
        print('drift derivative norms=',np.linalg.norm(vy),np.linalg.norm(vt))

    # Regression guards for corrected headline results.
    f1=profiled(branches['D1'][0],branches['D1'][1],am,av,1.82e5,3.49e5)
    f2=profiled(branches['D2'][0],branches['D2'][1],am,av,1.70e5,1.00e6)
    assert 0.56<f1<0.59
    assert 0.47<f2<0.50
    g1,b1,k1=optimize(*branches['D1'],am,av)
    g2,b2,k2=optimize(*branches['D2'],am,av)
    assert 1.50e6<g1<1.58e6 and 1.03<k1<1.11
    assert 2.10e6<g2<2.20e6 and 1.08<k2<1.20

if __name__=='__main__': main()
