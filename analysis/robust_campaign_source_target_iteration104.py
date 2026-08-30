#!/usr/bin/env python3
"""RQIR Iteration 104 — robust campaign simplex and source-target consistency.

Deterministic algebra/regression certificate. Synthetic uncertainty scenarios are
used only to verify the exact robust identities; they are not apparatus forecasts.
"""
from math import sqrt, isclose
import numpy as np


def source_profile(A,C):
    assert A>=0 and C>=0 and A+C>0
    return A*C/(A+C)


def source_rates_profile(x,Rs,Ra):
    assert 0<x<1 and Rs>0 and Ra>0
    return source_profile(Rs*x,Ra*(1-x))


def source_optimum(Rs,Ra):
    """Optimal science fraction, retained fraction and profiled rate."""
    a=sqrt(Rs); b=sqrt(Ra)
    x=b/(a+b)
    r=x
    R=1.0/(1.0/a+1.0/b)**2
    return x,r,R


def campaign_matrices(Rs,Ra):
    Js=Rs*np.array([[1.0,1.0],[1.0,1.0]])
    Ja=Ra*np.array([[0.0,0.0],[0.0,1.0]])
    return Js,Ja


def profile_matrix(J):
    a=J[0,0]; b=J[0,1]; N=J[1,1]
    return float(a-b*b/N)


def marginal_rates(J, campaigns):
    q=J[0,1]/J[1,1]
    w=np.array([1.0,-q])
    return np.array([float(w@K@w) for K in campaigns])


def main():
    # NUM-006: old 90%-retention raw-Z=5 convention is not a final-Z=5 certificate.
    A_raw=25.0; C_old=225.0
    Fold=source_profile(A_raw,C_old)
    assert isclose(Fold,22.5,rel_tol=0,abs_tol=1e-14)
    assert isclose(sqrt(Fold),4.743416490252569,rel_tol=1e-15)

    # To retain 90% and still finish at F=25, raw detector and source Fisher must be larger.
    r=0.90; Fstar=25.0
    Areq=Fstar/r
    Creq=Fstar/(1-r)
    assert isclose(Areq,27.77777777777778,rel_tol=1e-15)
    assert isclose(Creq,250.0,rel_tol=1e-14)
    assert isclose(source_profile(Areq,Creq),Fstar,rel_tol=1e-15)

    # RESOURCE-060: fixed retention is generally not wall-clock optimal.
    for Rs,Ra in ((1.0,1.0),(1.0,81.0),(4.0,9.0)):
        x,rstar,R=source_optimum(Rs,Ra)
        # dense regression against direct profile rate
        grid=np.linspace(1e-5,1-1e-5,200001)
        vals=np.array([source_rates_profile(xx,Rs,Ra) for xx in grid])
        im=int(np.argmax(vals))
        assert abs(grid[im]-x)<1.2e-5
        assert abs(vals[im]-R)<2e-10
        assert isclose(rstar,x,rel_tol=0,abs_tol=1e-15)
    assert isclose(source_optimum(1.0,81.0)[1],0.9,rel_tol=0,abs_tol=1e-15)

    # RESOURCE-059 robust max-min regression with two active worst-case vertices.
    scenarios=[(1.0,9.0),(9.0,1.0)]
    x=0.5
    Fv=np.array([source_rates_profile(x,*s) for s in scenarios])
    assert np.allclose(Fv,[0.45,0.45],rtol=0,atol=2e-15)

    # Exact vertex certificate for the affine uncertainty segment.
    xis=np.linspace(0.0,1.0,1001)
    Fseg=np.array([source_rates_profile(x,1+8*z,9-8*z) for z in xis])
    assert isclose(Fseg.min(),min(Fv),rel_tol=0,abs_tol=2e-15)
    assert Fseg.max()>1.24

    # Brute robust fraction regression.
    grid=np.linspace(1e-4,1-1e-4,20001)
    robust=np.array([min(source_rates_profile(xx,*s) for s in scenarios) for xx in grid])
    im=int(np.argmax(robust))
    assert abs(grid[im]-0.5)<6e-5
    assert abs(robust[im]-0.45)<2e-8

    # Robust KKT: active-scenario mixture of marginal campaign rates equalizes.
    grads=[]
    for Rs,Ra in scenarios:
        Js,Ja=campaign_matrices(Rs,Ra)
        J=x*Js+(1-x)*Ja
        assert isclose(profile_matrix(J),0.45,rel_tol=0,abs_tol=2e-15)
        grads.append(marginal_rates(J,[Js,Ja]))
    grads=np.array(grads)
    assert np.allclose(grads,[[0.81,0.09],[0.09,0.81]],rtol=0,atol=2e-15)
    mixed=0.5*grads[0]+0.5*grads[1]
    assert np.allclose(mixed,[0.45,0.45],rtol=0,atol=2e-15)

    print('PASS Iteration 104 robust campaign/source target')
    print('old raw-5sigma 90%-retention final Fisher/sigma =',Fold,sqrt(Fold))
    print('final-5sigma 90%-retention A,C =',Areq,Creq)
    print('90% is time-optimal only at Ra/Rs = 81')
    print('robust two-vertex optimum fraction/rate =',x,min(Fv))
    print('active-scenario marginal gradients =',grads,'mixed =',mixed)


if __name__=='__main__':
    main()
