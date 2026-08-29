"""RQIR Iteration 057: complementary D2 branch on balanced local Toy012.

Rebuild the physically preferred finite-reference relational + direct-force D2
calibration architecture on the balanced exact-nearest-neighbour Toy012 source.
The question is whether Toy009's dramatic force-covariance completion survives
source localization/resource-aware redesign.

Primary comparison uses y_ref=-4 to match the mature Toy009 branch.  All noise
rows are centered and trace+energy are eliminated exactly.  Detector beta
signal is normalized for nuisance-geometry comparison; absolute Toy012 signal
penalty is retained separately from Iteration 055.
"""
from __future__ import annotations

import itertools
import numpy as np
import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54

TARGET=0.90
YREF=-4.0
Q0=np.array([0.182446543760,0.684368939221,0.165591352865,
             0.679324856717,0.097209344214])
Y1=-2.948786569910398
TIMES=np.array([0.,1.038867458294,2.985962997881,4.875819177097,
                4.150899563476,1.623915172581,5.275220686287])

# Iteration-055 balanced Toy012 centered NP3 D2 optimum.
GM=1208686.5290376
GC=1899498.031721214

# Source metrology / transparent covariance benchmark.
RAMSEY_RATE_COEFF=0.002134292844  # max F_alpha(phi)/phi for Toy012
P_ACCEPT=0.5
F_GAP_HZ=100.0
DEAD_S=1e-3


def probe_at(Q,y):
    return (Q@np.diag(1.0/np.abs(t11.RADII-y))@Q.T).astype(complex)


def grad_at(Q,y):
    r=t11.RADII-y
    return (Q@np.diag(1.0/r**2)@Q.T).astype(complex)


def fisher_profile(pack,means,covs,c_alpha=0.0,scale=1.0):
    M=np.vstack([means,covs])
    W=np.r_[np.full(len(means),GM),np.full(len(covs),GC)]*scale
    s=pack['s2']; B=pack['B2']; Zu=pack['Zu']; theta0=pack['theta0']
    Jd=np.column_stack([s,s,B@Zu])
    F=Jd.T@Jd
    Jc=np.column_stack([M@theta0,M@Zu])
    F[1:,1:]+=Jc.T@(W[:,None]*Jc)
    F[1,1]+=c_alpha
    N=F[1:,1:]; c=F[0,1:]
    return float(F[0,0]-c@np.linalg.solve(N,c))


def min_calpha(pack,means,covs,target=TARGET):
    f=lambda ca:fisher_profile(pack,means,covs,ca,1.0)
    if f(0.0)>=target:
        return 0.0
    if f(1e12)<target:
        return np.inf
    lo,hi=0.0,1.0
    while f(hi)<target:
        hi*=10.0
    for _ in range(90):
        mid=0.5*(lo+hi)
        if f(mid)>=target: hi=mid
        else: lo=mid
    return hi


def min_lambda(pack,means,covs,c_alpha=0.0,target=TARGET):
    f=lambda lam:fisher_profile(pack,means,covs,c_alpha,lam)
    lo,hi=1e-6,1.0
    while f(hi)<target and hi<1e6:
        hi*=2.0
    if f(hi)<target:
        return np.inf
    for _ in range(80):
        mid=np.sqrt(lo*hi)
        if f(mid)>=target: hi=mid
        else: lo=mid
    return hi


def hard_rank(pack,means,covs):
    M=np.vstack([means,covs])
    ss=np.linalg.svd(M@pack['Z'],compute_uv=False)
    return int(np.sum(ss>1e-12)),float(ss[-1])


# Force-cov row endpoint graph inherited from the declared row pattern.
EDGES=[
    ('G0_TR','G0_0'),
    ('G0_T1','G1_0'),
    ('G1_T5','G1_0'),
    ('G1_TR','G0_0'),
    ('G0_TR','G1_0'),
    ('G1_T3','G0_0'),
    ('G0_T6','G0_0'),
    ('G0_T6','G1_0'),
]


def graph_rho2(indices):
    if not indices:
        return 0.0
    nodes=sorted({x for j in indices for x in EDGES[j]})
    index={x:i for i,x in enumerate(nodes)}
    A=np.zeros((len(nodes),len(nodes)))
    for j in indices:
        a,b=EDGES[j]
        A[index[a],index[b]]=A[index[b],index[a]]=1.0
    ev=np.linalg.eigvalsh(A)
    return float(np.max(np.abs(ev))**2)


def main():
    Q=t11.lanczos_q(Q0)
    assert Q is not None
    p0=probe_at(Q,0.0); p1=probe_at(Q,Y1)
    g0=grad_at(Q,0.0); g1=grad_at(Q,Y1)

    pack=i54.make_pack(Q,Y1,TIMES)
    # Check retained Toy012 NP3 D2 weights.
    d2opt=i54.optimize_groups(pack,'D2')[1]
    print('Toy012 NP3 D2 opt',d2opt)
    assert abs(d2opt[1]-GM)<3.0
    assert abs(d2opt[2]-GC)<3.0

    pref=probe_at(Q,YREF)
    rm,rc=i54.operator_rows([p0-pref,p1-pref],TIMES)
    fm,fc=i54.operator_rows([g0,g1],TIMES)
    means=np.vstack([rm,fm])

    # Source-metrology-efficient subset choice: minimize C_alpha at lambda=1.
    table=[]
    for k in range(9):
        best=(np.inf,(),np.nan,np.nan,np.nan)
        combos=[()] if k==0 else ([tuple(range(8))] if k==8 else itertools.combinations(range(8),k))
        for inds in combos:
            cov=np.vstack([rc]+[fc[j][None,:] for j in inds]) if inds else rc
            ca=min_calpha(pack,means,cov)
            if ca<best[0]:
                f0=fisher_profile(pack,means,cov,0.0,1.0)
                lam=min_lambda(pack,means,cov,0.0)
                rank,smin=hard_rank(pack,means,cov)
                best=(ca,tuple(inds),f0,lam,(rank,smin))
        table.append(best)
        print('k',k,'best-by-Ca',best)

    # Regression values at the common Toy009 reference y_ref=-4.
    expected_ca=[
        13.669414719044303,13.135585392126181,12.309076282213292,
        12.152510708961103,12.097051643728117,12.009587523008655,
        11.972118143637239,11.934827061348988,11.891637660035794,
    ]
    expected_sets=[(),(1,),(1,3),(1,3,5),(1,3,4,5),(0,1,3,4,5),
                   (0,1,2,3,4,5),(0,1,3,4,5,6,7),tuple(range(8))]
    for k in range(9):
        assert abs(table[k][0]-expected_ca[k])<3e-8
        assert table[k][1]==expected_sets[k]
        assert table[k][4][0]==23

    # Crucial contrast with Toy009: hard rank is already full without added
    # force covariance, but finite-noise/source-prior cost remains large.
    assert abs(table[0][2]-0.1944054367218483)<3e-10
    assert abs(table[4][2]-0.5191318203057858)<3e-10
    assert abs(table[8][2]-0.5987070029452113)<3e-10
    assert abs(table[0][4][1]-0.0017140951050145044)<3e-12

    # Natural shared-edge covariance lower bound for the best four-by-Ca set.
    inds4=table[4][1]
    rho2=graph_rho2(inds4)
    n_cov4=GC*rho2
    delta_ca=table[0][0]-table[4][0]
    t_coh=float(np.max(TIMES))/(2.0*np.pi*F_GAP_HZ)
    t_cycle=t_coh+DEAD_S
    wall_cov4=n_cov4/P_ACCEPT*t_cycle
    r_break=delta_ca/wall_cov4
    omega_break=r_break/(P_ACCEPT*RAMSEY_RATE_COEFF)
    print('best4 graph rho^2',rho2,'N floor',n_cov4)
    print('Delta C_alpha',delta_ca,'cov wall h',wall_cov4/3600.0)
    print('source-metrology Fisher-rate break-even',r_break)
    print('zero-reset Ramsey Omega break-even',omega_break)

    assert abs(rho2-2.0)<2e-12
    assert abs(n_cov4-3798996.063442428)<5e-6
    assert abs(wall_cov4/3600.0-19.830283481773925)<3e-10
    assert abs(r_break-2.2025278726983266e-5)<3e-12
    assert abs(omega_break-0.02063941580360119)<3e-12


if __name__=='__main__':
    main()
