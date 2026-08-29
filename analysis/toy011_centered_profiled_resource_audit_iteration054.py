"""RQIR Iteration 054: centered profiled Fisher/resource audit for local Toy011.

Purpose
-------
Toy011 (Iteration 053) proved that the finite NP3 mean/noise null and a nonzero
ordered-response split survive an exactly nearest-neighbour five-site source
Hamiltonian.  This script asks whether the two retained local candidates remain
statistically/resource competitive after the same centered hard-constrained
Fisher machinery used for Toy009.

The audit deliberately separates:
  (i) normalized nuisance/calibration geometry, where the detector beta signal
      is normalized to unit norm; and
  (ii) absolute two-band detector signal power before that normalization.
This prevents a normalized Fisher calculation from hiding the physical signal
penalty induced by locality.
"""
from __future__ import annotations

import math
import numpy as np
import toy011_local_nearest_neighbor_source as t11

D=t11.D
E=t11.E
H=t11.H
EPS=t11.EPS
TARGET=0.90
N_MEAN=14
N_COV=8


def candidate_at_trial(index: int):
    rng=np.random.default_rng(t11.SEED)
    out=None
    for trial in range(index+1):
        q0=np.exp(rng.normal(0.0,0.8,size=D)); q0/=np.linalg.norm(q0)
        y1=-rng.uniform(1.0,12.0)
        times=np.r_[0.0,rng.uniform(0.0,2.0*math.pi,6)]
        if trial==index:
            out=t11.evaluate(q0,y1,times)
    assert out is not None
    return out


def centered_sym(a,b):
    rho0=np.eye(D)/D
    ma=np.trace(rho0@a); mb=np.trace(rho0@b)
    return t11.sym(a,b)-mb*a-ma*b


def operator_rows(ops,times):
    means=[]
    for k in (0,1):
        for tt in times:
            means.append(t11.herm_vec(t11.evolve(ops[k],float(tt))))
    tr=float(times[2])
    cov=[t11.herm_vec(centered_sym(t11.evolve(ops[0],tr),ops[0]))]
    extra=[
        (0,1,times[1]),(1,1,times[5]),(1,0,tr),(0,1,tr),
        (1,0,times[3]),(0,0,times[6]),(0,1,times[6]),
    ]
    for k,l,tt in extra:
        cov.append(t11.herm_vec(centered_sym(t11.evolve(ops[k],float(tt)),ops[l])))
    means=np.vstack(means); cov=np.vstack(cov)
    means/=np.linalg.norm(means,axis=1,keepdims=True)
    cov/=np.linalg.norm(cov,axis=1,keepdims=True)
    return means,cov


def hard_bases(theta0):
    fixed=np.vstack([t11.herm_vec(np.eye(D)),t11.herm_vec(H)])
    _u,s,vh=np.linalg.svd(fixed,full_matrices=True)
    Z=vh[int(np.sum(s>1e-12)):].T
    q=theta0/np.linalg.norm(theta0)
    P=Z-np.outer(q,q@Z)
    U,sp,_=np.linalg.svd(P,full_matrices=False)
    Zu=U[:,sp>1e-10]
    assert Z.shape==(25,23) and Zu.shape==(25,22)
    return Z,Zu


def detector_matrix(readout,pump,theta0):
    B=np.zeros((4,D*D),float)
    for j in range(D*D):
        e=np.zeros(D*D); e[j]=1.0
        op=t11.mat(e)
        h2=t11.harmonic(op,readout,pump,2)
        h4=t11.harmonic(op,readout,pump,4)
        B[:,j]=[h2.real,h2.imag,h4.real,h4.imag]
    sraw=B@theta0
    norm=float(np.linalg.norm(sraw))
    return B,sraw,norm


def make_pack(qbasis,y1,times):
    p0,p1,g0=t11.operators(qbasis,y1)
    # second gradient probe is not needed for the present NP3 audit
    A=t11.calibration_rows(p0,p1,times)
    An=A/np.linalg.norm(A,axis=1,keepdims=True)
    _u,sv,vh=np.linalg.svd(An,full_matrices=True)
    d0=t11.mat(vh[-1]); d0/=np.max(np.abs(np.linalg.eigvalsh(d0)))
    theta0=2.0*EPS*t11.herm_vec(d0)
    Z,Zu=hard_bases(theta0)
    pm,pc=operator_rows([p0,p1],times)
    B1raw,s1raw,n1=detector_matrix(p0,p0,theta0)
    B2raw,s2raw,n2=detector_matrix(g0,p0,theta0)
    B1=B1raw/n1; B2=B2raw/n2
    return dict(
        p0=p0,p1=p1,g0=g0,A=A,sv=sv,d0=d0,theta0=theta0,Z=Z,Zu=Zu,
        pm=pm,pc=pc,
        B1raw=B1raw,s1raw=s1raw,n1=n1,B1=B1,s1=B1@theta0,bu1=B1@Zu,
        B2raw=B2raw,s2raw=s2raw,n2=n2,B2=B2,s2=B2@theta0,bu2=B2@Zu,
    )


def profiled_known(s,bu,mm,mc,gm,gc):
    fuu=bu.T@bu+gm*mm+gc*mc
    cross=s@bu
    return float(s@s-cross@np.linalg.solve(fuu,cross))


def required_cov(s,bu,mm,mc,gm,target=TARGET):
    lo,hi=1e1,1e12
    if profiled_known(s,bu,mm,mc,gm,hi)<target:
        return np.inf
    for _ in range(55):
        mid=np.sqrt(lo*hi)
        if profiled_known(s,bu,mm,mc,gm,mid)>=target: hi=mid
        else: lo=mid
    return hi


def uniform_threshold(s,bu,mm,mc,target=TARGET):
    lo,hi=1e2,1e12
    for _ in range(55):
        mid=np.sqrt(lo*hi)
        if profiled_known(s,bu,mm,mc,mid,mid)>=target: hi=mid
        else: lo=mid
    return hi


def optimize_groups(pack,detector='D2'):
    s=pack['s2'] if detector=='D2' else pack['s1']
    bu=pack['bu2'] if detector=='D2' else pack['bu1']
    Zu=pack['Zu']; am=pack['pm']@Zu; ac=pack['pc']@Zu
    mm=am.T@am; mc=ac.T@ac
    gu=uniform_threshold(s,bu,mm,mc)
    best=((N_MEAN+N_COV)*gu,gu,gu)
    # same deterministic scan convention as centered Iteration 034
    for gm in np.logspace(4,10,900):
        gc=required_cov(s,bu,mm,mc,float(gm))
        if np.isfinite(gc):
            cost=N_MEAN*gm+N_COV*gc
            if cost<best[0]: best=(float(cost),float(gm),float(gc))
    return gu,best,(N_MEAN+N_COV)*gu/best[0]


def fisher_profile(pack,gm,gc,c_alpha,scale=1.0):
    M=np.vstack([pack['pm'],pack['pc']])
    W=np.r_[np.full(N_MEAN,gm),np.full(N_COV,gc)]*scale
    s=pack['s2']; B=pack['B2']; Zu=pack['Zu']; theta0=pack['theta0']
    Jd=np.column_stack([s,s,B@Zu])
    F=Jd.T@Jd
    Jc=np.column_stack([M@theta0,M@Zu])
    F[1:,1:]+=Jc.T@(W[:,None]*Jc)
    F[1,1]+=c_alpha
    N=F[1:,1:]; c=F[0,1:]
    return float(F[0,0]-c@np.linalg.solve(N,c))


def min_calpha(pack,gm,gc,scale,target=TARGET):
    f=lambda ca: fisher_profile(pack,gm,gc,ca,scale)
    if f(1e-12)>=target: return 0.0
    if f(1e12)<target: return np.inf
    lo,hi=1e-12,1.0
    while f(hi)<target: hi*=10.0
    for _ in range(90):
        mid=np.sqrt(lo*hi)
        if f(mid)>=target: hi=mid
        else: lo=mid
    return hi


def qfi_alpha(d0,alpha=1.0):
    de=np.linalg.eigvalsh(d0)
    p=np.ones(D)/D+EPS*alpha*de
    return EPS**2*float(np.sum(de**2/p))


def energy_fisher_alpha(d0,alpha=1.0):
    d=np.real(np.diag(d0))
    p=np.ones(D)/D+EPS*alpha*d
    return EPS**2*float(np.sum(d*d/p))


def ramsey_fisher(phi,alpha,dpop,visibility=1.0):
    p=np.ones(D)/D+EPS*alpha*dpop
    z=np.exp(-1j*phi*E)
    c=np.sum(p*z); dc=EPS*np.sum(dpop*z)
    cv=visibility*np.array([c.real,c.imag]); dv=visibility*np.array([dc.real,dc.imag])
    metric=np.eye(2)-np.outer(cv,cv)
    return float(dv@np.linalg.pinv(metric,rcond=1e-14)@dv)


def golden_max(f,a,b,tol=1e-12):
    gr=(math.sqrt(5.0)-1.0)/2.0
    c=b-gr*(b-a); d=a+gr*(b-a); fc=f(c); fd=f(d)
    for _ in range(200):
        if b-a<tol: break
        if fc>fd:
            b,d,fd=d,c,fc; c=b-gr*(b-a); fc=f(c)
        else:
            a,c,fc=c,d,fd; d=a+gr*(b-a); fd=f(d)
    x=0.5*(a+b)
    return x,f(x)


def ramsey_rate_optimum(d0):
    dpop=np.real(np.diag(d0))
    grid=np.linspace(1e-6,2.0*math.pi-1e-6,16001)
    vals=np.array([ramsey_fisher(x,1.0,dpop)/x for x in grid])
    j=int(np.argmax(vals)); step=grid[1]-grid[0]
    lo=max(1e-8,grid[j]-4*step); hi=min(2.0*math.pi-1e-8,grid[j]+4*step)
    return golden_max(lambda x: ramsey_fisher(x,1.0,dpop)/x,lo,hi)


def main():
    local_r=candidate_at_trial(6304)
    local_c=candidate_at_trial(3811)
    base=make_pack(t11.V009_SORTED,t11.Y1_BASE,t11.TIMES_BASE)
    pr=make_pack(local_r['Q'],local_r['y1'],local_r['times'])
    pc=make_pack(local_c['Q'],local_c['y1'],local_c['times'])
    packs={'Toy009':base,'Toy011-response':pr,'Toy011-conditioning':pc}

    results={}
    for name,p in packs.items():
        d1=optimize_groups(p,'D1'); d2=optimize_groups(p,'D2')
        _cost2,gm2,gc2=d2[1]
        fq=qfi_alpha(p['d0']); fe=energy_fisher_alpha(p['d0'])
        phi,cr=ramsey_rate_optimum(p['d0'])
        cals=[min_calpha(p,gm2,gc2,x) for x in (1.05,1.10,1.20,1.50,2.00)]
        results[name]=dict(
            D1raw=p['n1']**2,D2raw=p['n2']**2,
            D1cost=d1[1][0],D1gm=d1[1][1],D1gc=d1[1][2],
            D2cost=d2[1][0],D2gm=gm2,D2gc=gc2,
            FQ=fq,FE=fe,phi=phi,cR=cr,Cprofile=cals,
        )
        print(name,results[name])

    b=results['Toy009']
    for name in ('Toy011-response','Toy011-conditioning'):
        r=results[name]
        print(name,'ratios',{
            'D1raw':r['D1raw']/b['D1raw'],
            'D2raw':r['D2raw']/b['D2raw'],
            'D1calcost':r['D1cost']/b['D1cost'],
            'D2calcost':r['D2cost']/b['D2cost'],
            'FQ':r['FQ']/b['FQ'],
            'FE':r['FE']/b['FE'],
            'RamseyRateCoeff':r['cR']/b['cR'],
        })

    # Regression guards from deterministic reconstruction.
    assert abs(b['D2gm']-1.830264703e6)<3e0
    assert abs(b['D2gc']-5.901272925e5)<3e0
    assert abs(results['Toy011-response']['D2cost']/b['D2cost']-34.59822)<3e-4
    assert abs(results['Toy011-conditioning']['D2cost']/b['D2cost']-10.09526)<3e-4
    assert abs(results['Toy011-response']['D2raw']/b['D2raw']-0.17069168)<3e-7
    assert abs(results['Toy011-conditioning']['D2raw']/b['D2raw']-0.08416564)<3e-7
    assert abs(results['Toy011-response']['FQ']-0.0908139711)<3e-10
    assert abs(results['Toy011-conditioning']['FQ']-0.0811577560)<3e-10
    assert abs(results['Toy011-response']['FE']-0.0031938080)<3e-10
    assert abs(results['Toy011-conditioning']['FE']-0.0028281622)<3e-10
    assert abs(results['Toy011-response']['cR']/b['cR']-0.2659931)<3e-6
    assert abs(results['Toy011-conditioning']['cR']/b['cR']-0.4194763)<3e-6
    assert abs(results['Toy011-response']['Cprofile'][1]-108.51793)<2e-3
    assert abs(results['Toy011-conditioning']['Cprofile'][1]-110.75458)<2e-3


if __name__=='__main__':
    main()
