"""RQIR Iteration 060: Toy012 base-relational-covariance / lambda / source-metrology co-design.

Iteration 057 treated all eight centered relational covariance rows as common
calibration overhead and only varied *added* force-covariance rows.  For total
wall clock this is not legitimate.  This script exposes the eight base
relational-covariance rows, enumerates their subsets, assigns the same natural
shared-endpoint graph lower bound used in Iterations 039--040, and jointly
optimizes

    (relational-covariance subset, calibration scale lambda, C_alpha)

against an independent source-metrology Fisher rate R_alpha.

The 28 mean rows (14 relational + 14 direct force) are kept fixed.  Their
physical time uses the conservative RESOURCE-016 scheduling baseline: the two
mean families are independent campaigns unless a common detector likelihood is
explicitly supplied.

All covariance wall times are lower bounds for the declared phase-referenced
Gaussian endpoint model; NG-011/014/015 remain active.
"""
from __future__ import annotations
import itertools
import math
import numpy as np

import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54
import toy012_complementary_d2_branch_iteration057 as i57

TARGET=0.90
P_ACCEPT=0.5
F_GAP=100.0
DEAD=1e-3

# Natural endpoint graph for the eight centered relational covariance rows.
EDGES=[
    ('P0_TR','P0_0'),
    ('P0_T1','P1_0'),
    ('P1_T5','P1_0'),
    ('P1_TR','P0_0'),
    ('P0_TR','P1_0'),
    ('P1_T3','P0_0'),
    ('P0_T6','P0_0'),
    ('P0_T6','P1_0'),
]

S4=(2,4,5,6)
S6=(1,2,3,4,5,6)
R_BENCH=2.2025278726983266e-5  # Iter057 force-cov best4 break-even


def graph_rho2(inds):
    if not inds:
        return 0.0
    nodes=sorted({x for j in inds for x in EDGES[j]})
    ix={x:i for i,x in enumerate(nodes)}
    A=np.zeros((len(nodes),len(nodes)))
    for j in inds:
        a,b=EDGES[j]
        A[ix[a],ix[b]]=A[ix[b],ix[a]]=1.0
    ev=np.linalg.eigvalsh(A)
    return float(np.max(np.abs(ev))**2)


def build():
    Q=t11.lanczos_q(i57.Q0)
    pack=i54.make_pack(Q,i57.Y1,i57.TIMES)
    p0=i57.probe_at(Q,0.0); p1=i57.probe_at(Q,i57.Y1)
    pref=i57.probe_at(Q,i57.YREF)
    g0=i57.grad_at(Q,0.0); g1=i57.grad_at(Q,i57.Y1)
    rm,rc=i54.operator_rows([p0-pref,p1-pref],i57.TIMES)
    fm,_fc=i54.operator_rows([g0,g1],i57.TIMES)
    means=np.vstack([rm,fm])

    # Detector Fisher for params (beta, alpha, u_1..u_22).
    s=pack['s2']; B=pack['B2']; Zu=pack['Zu']; theta0=pack['theta0']
    Jd=np.column_stack([s,s,B@Zu])
    Fd=Jd.T@Jd

    # Calibration scores only act on (alpha,u).
    Jm=np.column_stack([means@theta0,means@Zu])
    Km=i57.GM*(Jm.T@Jm)
    Kc=[]
    for row in rc:
        j=np.r_[row@theta0,row@Zu]
        Kc.append(i57.GC*np.outer(j,j))
    return pack,rc,Fd,Km,Kc


def effective_beta_alpha(Fd,Km,Kc,inds,lam):
    F=Fd.copy()
    K=Km.copy()
    for j in inds:
        K+=Kc[j]
    F[1:,1:]+=lam*K
    Fuu=F[2:,2:]
    return F[:2,:2]-F[:2,2:]@np.linalg.solve(Fuu,F[2:,:2])


def required_calpha(Fd,Km,Kc,inds,lam,target=TARGET):
    A=effective_beta_alpha(Fd,Km,Kc,inds,lam)
    a,b,c=float(A[0,0]),float(A[0,1]),float(A[1,1])
    # Even perfectly known alpha cannot repair insufficient calibration of the
    # other 22 source nuisances if the beta-beta profiled ceiling is <= target.
    if a<=target+1e-13:
        return math.inf
    return max(0.0,b*b/(a-target)-c)


def fbeta(Fd,Km,Kc,inds,lam,ca=0.0):
    A=effective_beta_alpha(Fd,Km,Kc,inds,lam)
    return float(A[0,0]-A[0,1]**2/(A[1,1]+ca))


def hard_rank(pack,means,rc,inds):
    M=np.vstack([means,rc[list(inds)]]) if inds else means
    sv=np.linalg.svd(M@pack['Z'],compute_uv=False)
    return int(np.sum(sv>1e-12)),float(sv[-1])


def min_lambda_perfect_alpha(Fd,Km,Kc,inds):
    lo,hi=1e-8,1.0
    while effective_beta_alpha(Fd,Km,Kc,inds,hi)[0,0]<TARGET:
        hi*=2.0
        if hi>1e8:
            return math.inf
    for _ in range(70):
        mid=math.sqrt(lo*hi)
        if effective_beta_alpha(Fd,Km,Kc,inds,mid)[0,0]>=TARGET:
            hi=mid
        else:
            lo=mid
    return hi


def mean_family_hours(xi):
    # One 14-row family = seven same-time dual-probe layers.
    te=i57.TIMES/(2.0*math.pi*F_GAP)
    return i57.GM/(xi*xi*P_ACCEPT)*float(np.sum(te+DEAD))/3600.0


def cov_hours_at_lambda1(inds):
    tmax=float(np.max(i57.TIMES))/(2.0*math.pi*F_GAP)
    n=i57.GC*graph_rho2(inds)
    return n/P_ACCEPT*(tmax+DEAD)/3600.0


def objective(Fd,Km,Kc,inds,lam,xi_rel,xi_force,R_alpha):
    ca=required_calpha(Fd,Km,Kc,inds,lam)
    if not np.isfinite(ca):
        return math.inf
    tmean=mean_family_hours(xi_rel)+mean_family_hours(xi_force)
    tcov=cov_hours_at_lambda1(inds)
    return lam*(tmean+tcov)+ca/(R_alpha*3600.0)


def optimize_lambda(Fd,Km,Kc,inds,xi_rel,xi_force,R_alpha):
    # Deterministic log scan; enough to cover underexposure and calibration-only
    # closure.  Refine in log(lambda) around the best bin.
    grid=np.logspace(-3,5,260)
    vals=np.array([objective(Fd,Km,Kc,inds,x,xi_rel,xi_force,R_alpha)
                   for x in grid])
    j=int(np.argmin(vals))
    if not np.isfinite(vals[j]):
        return math.inf,math.nan,math.nan
    lo=math.log(grid[max(0,j-2)]); hi=math.log(grid[min(len(grid)-1,j+2)])

    # Golden minimization on z=log(lambda).
    gr=(math.sqrt(5.0)-1.0)/2.0
    c=hi-gr*(hi-lo); d=lo+gr*(hi-lo)
    fc=objective(Fd,Km,Kc,inds,math.exp(c),xi_rel,xi_force,R_alpha)
    fd=objective(Fd,Km,Kc,inds,math.exp(d),xi_rel,xi_force,R_alpha)
    for _ in range(120):
        if hi-lo<1e-9:
            break
        if fc<fd:
            hi,d,fd=d,c,fc; c=hi-gr*(hi-lo)
            fc=objective(Fd,Km,Kc,inds,math.exp(c),xi_rel,xi_force,R_alpha)
        else:
            lo,c,fc=c,d,fd; d=lo+gr*(hi-lo)
            fd=objective(Fd,Km,Kc,inds,math.exp(d),xi_rel,xi_force,R_alpha)
    lam=math.exp(0.5*(lo+hi))
    ca=required_calpha(Fd,Km,Kc,inds,lam)
    return objective(Fd,Km,Kc,inds,lam,xi_rel,xi_force,R_alpha),lam,ca


def global_optimum(Fd,Km,Kc,xi_rel,xi_force,R_alpha):
    best=(math.inf,(),0.0,math.nan,math.nan)
    for k in range(9):
        for inds in itertools.combinations(range(8),k):
            t,lam,ca=optimize_lambda(Fd,Km,Kc,inds,xi_rel,xi_force,R_alpha)
            if t<best[0]:
                best=(t,inds,graph_rho2(inds),lam,ca)
    return best


def main():
    pack,rc,Fd,Km,Kc=build()
    # Reconstruct fixed 28 means for hard-rank diagnostics.
    Q=t11.lanczos_q(i57.Q0)
    p0=i57.probe_at(Q,0.0); p1=i57.probe_at(Q,i57.Y1); pref=i57.probe_at(Q,i57.YREF)
    g0=i57.grad_at(Q,0.0); g1=i57.grad_at(Q,i57.Y1)
    rm,_=i54.operator_rows([p0-pref,p1-pref],i57.TIMES)
    fm,_=i54.operator_rows([g0,g1],i57.TIMES)
    means=np.vstack([rm,fm])

    print('Toy012 mean-family hours xi=1',mean_family_hours(1.0))
    print('sum/max evolution s',float(np.sum(i57.TIMES/(2*math.pi*F_GAP))),
          float(np.max(i57.TIMES)/(2*math.pi*F_GAP)))

    # Fixed-lambda cardinality audit.
    expected_ca={
        3:113.3907765354,
        4:15.06193955863,
        5:13.81947863555,
        6:13.75430919714,
        7:13.74020233763,
        8:13.66941471905,
    }
    for k in range(9):
        best=(math.inf,())
        for inds in itertools.combinations(range(8),k):
            ca=required_calpha(Fd,Km,Kc,inds,1.0)
            if ca<best[0]: best=(ca,inds)
        print('lambda=1 k',k,'best C_alpha',best)
        if k>=3:
            assert abs(best[0]-expected_ca[k])<3e-7

    # Perfect-source-metrology minimum lambda demonstrates how important base
    # relational covariance is at finite resources.
    exp_lam={
        0:90095.34742,1:8.039240940,2:3.312753228,3:0.8618447902,
        4:0.2703009741,5:0.2576517505,6:0.2519596235,
        7:0.2494361378,8:0.2467065691,
    }
    for k in range(9):
        best=(math.inf,())
        for inds in itertools.combinations(range(8),k):
            x=min_lambda_perfect_alpha(Fd,Km,Kc,inds)
            if x<best[0]: best=(x,inds)
        print('perfect-alpha k',k,'lambda90',best)
        assert abs(best[0]/exp_lam[k]-1.0)<3e-6

    # Natural graph lower-bound examples.
    assert abs(graph_rho2(S4)-2.0)<2e-12
    assert abs(cov_hours_at_lambda1(S4)-19.83028348177)<3e-9
    assert abs(graph_rho2(S6)-3.0)<2e-12
    assert abs(cov_hours_at_lambda1(S6)-29.74542522266)<3e-9
    assert abs(cov_hours_at_lambda1(tuple(range(8)))-59.49085044532)<3e-9

    # Important graph-cost effect: S6 adds a sixth row to the old k5-like block
    # without increasing rho^2=3, and has a smaller source-prior requirement.
    ca6=required_calpha(Fd,Km,Kc,S6,1.0)
    assert abs(ca6-13.80773827175)<3e-8

    # Representative full 256-subset / lambda co-design checks.
    b1=global_optimum(Fd,Km,Kc,1.0,1.0,R_BENCH)
    b15=global_optimum(Fd,Km,Kc,1.5,1.5,R_BENCH)
    b3=global_optimum(Fd,Km,Kc,3.0,3.0,R_BENCH)
    print('global xi=1',b1)
    print('global xi=1.5',b15)
    print('global xi=3',b3)

    assert b1[1]==S6
    assert abs(b1[0]-255.6905557)<2e-3
    assert abs(b1[3]-0.952345)<3e-4
    assert b15[1]==S4
    assert abs(b15[0]-225.6959541)<2e-3
    assert abs(b15[3]-1.374445)<3e-4
    assert b3[1]==S4
    assert abs(b3[0]-199.0186236)<2e-3
    assert abs(b3[3]-1.754638)<3e-4

    # Around the current source-metrology benchmark, the graph-cost winner
    # switches close to xi~1.48 for equal relational/force mean sensitivity.
    lo=global_optimum(Fd,Km,Kc,1.47,1.47,R_BENCH)
    hi=global_optimum(Fd,Km,Kc,1.49,1.49,R_BENCH)
    assert lo[1]==S6 and hi[1]==S4

if __name__=='__main__':
    main()
