"""RQIR Iteration 031: finite-reference D2 hard-constrained profiled Fisher audit.

Tests whether the finite-reference relational-potential calibration introduced in
Iteration 030 actually cures beta/source non-identifiability for the *fixed*
Toy009 physical hidden state.  The source is not redefined together with the
calibration observable.

Key question: B(y)-B(y_ref) generally sees the old hidden amplitude, but does
that make beta identifiable after profiling all hard-constrained source
nuisances?  Answer for the present finite Toy009 model: no.  The exact null
rotates and remains almost perfectly detector aligned.
"""
from __future__ import annotations
import importlib.util
from pathlib import Path
import numpy as np

GM=2.414e6
GC=0.929e6
TARGET=0.90


def load(name, filename):
    path=Path(__file__).resolve().parent/filename
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def relational_matrix(i30,yref):
    return i30.calibration_matrix(float(yref))


def pack_fixed_source(i26):
    A,labels,G,theta0,B,s,Z,Zu,sv=i26.build()
    return A,labels,theta0,B,s,Z,Zu


def profiled(i26,i30,pack,yref,c_a=0.0,scale=1.0):
    A,labels,theta0,B,s,Z,Zu=pack
    R=relational_matrix(i30,yref)
    im=np.where(labels=='mean')[0]
    ic=np.where(labels=='cov')[0]
    M=np.vstack([R[im],R[ic]])
    W=np.r_[np.full(len(im),GM),np.full(len(ic),GC)]*scale

    # Parameters: beta, fractional amplitude of the fixed Toy009 hidden state,
    # and 22 hard-constrained source nuisances orthogonal to that state.
    Jd=np.column_stack([s,s,B@Zu])
    F=Jd.T@Jd
    Jc=np.column_stack([M@theta0,M@Zu])
    F[1:,1:]+=Jc.T@(W[:,None]*Jc)
    F[1,1]+=c_a
    N=F[1:,1:]
    c=F[0,1:]
    fb=float(F[0,0]-c@np.linalg.pinv(N,rcond=1e-13)@c)

    amp_info=float((M@theta0)@(W*(M@theta0)))
    MR=M@Z
    _,ss,vh=np.linalg.svd(MR,full_matrices=True)
    znull=Z@vh[-1]
    znull/=np.linalg.norm(znull)
    old=theta0/np.linalg.norm(theta0)
    bz=B@znull
    align=float(abs(s@bz)/np.linalg.norm(bz))
    return fb,amp_info,float(abs(znull@old)),align,float(ss[-1])


def min_ca(i26,i30,pack,yref,scale=1.0,target=TARGET):
    f=lambda ca: profiled(i26,i30,pack,yref,ca,scale)[0]
    if f(0.0)>=target:
        return 0.0
    if f(1e12)<target:
        return np.inf
    lo,hi=0.0,1.0
    while f(hi)<target:
        hi*=10.0
    for _ in range(100):
        mid=0.5*(lo+hi)
        if f(mid)>=target: hi=mid
        else: lo=mid
    return hi


def min_lambda_strong_prep(i26,i30,pack,yref,target=TARGET):
    f=lambda lam: profiled(i26,i30,pack,yref,1e12,lam)[0]
    lo,hi=1e-6,100.0
    assert f(hi)>=target
    for _ in range(100):
        mid=np.sqrt(lo*hi)
        if f(mid)>=target: hi=mid
        else: lo=mid
    return hi


def main():
    i26=load('rqir_i26','d2_calibration_branch_fisher_iteration026.py')
    i30=load('rqir_i30','d2_finite_reference_potential_iteration030.py')
    pack=pack_fixed_source(i26)

    refs=[-4.,-5.,-7.5,-10.,-20.,-50.,-100.,-1000.]
    for yr in refs:
        fb,ia,ov,al,smin=profiled(i26,i30,pack,yr)
        ca=min_ca(i26,i30,pack,yr)
        lam=min_lambda_strong_prep(i26,i30,pack,yr)
        print(f'yref={yr:8.1f} Fbeta(Ca=0)={fb:.12g} I_amp={ia:.12g} '
              f'null_overlap={ov:.12g} detector_align={al:.12g} '
              f'smin_hard={smin:.12g} Ca90={ca:.12g} lambda90_strongprep={lam:.12g}')

    # Regression values defining the Iteration-031 result.
    f5=profiled(i26,i30,pack,-5.)
    f10=profiled(i26,i30,pack,-10.)
    f100=profiled(i26,i30,pack,-100.)
    assert abs(f5[0]-8.174185251319521e-05)<2e-12
    assert abs(f10[0]-1.2329171416358697e-05)<2e-12
    assert abs(f100[0]-1.2490432133027696e-08)<2e-12
    assert f5[1]>3.0 and f10[1]>0.6 and f100[1]<3e-4
    assert f5[3]>0.9999 and f10[3]>0.99999 and f100[3]>0.9999999

    ca5=min_ca(i26,i30,pack,-5.)
    ca10=min_ca(i26,i30,pack,-10.)
    ca100=min_ca(i26,i30,pack,-100.)
    assert 16.5<ca5<16.8
    assert 21.7<ca10<22.2
    assert 105.<ca100<108.

    lam5=min_lambda_strong_prep(i26,i30,pack,-5.)
    lam10=min_lambda_strong_prep(i26,i30,pack,-10.)
    assert 0.49<lam5<0.50
    assert 0.59<lam10<0.61


if __name__=='__main__':
    main()
