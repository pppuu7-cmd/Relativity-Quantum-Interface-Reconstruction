"""RQIR Iteration 060: Toy012 relational-covariance/source-metrology wall-clock tradeoff.

Purpose
-------
Iteration 059 showed that Toy012 control priors must be rebuilt and that all
base relational-covariance rows cannot be treated as a free common constant.
This script enumerates relational-covariance subsets for the preferred Toy012
D2 architecture, profiles the hidden source amplitude alpha, and maps the
resource-relevant subsets into a transparent lower-bound wall-clock budget.

This is not a hardware forecast.  The normalized mean-row sensitivity xi_mu and
independent source-metrology Fisher rate R_alpha remain explicit.  Physical
force transduction / detector PSD must be attached in a later gate before xi_mu
can be interpreted as an apparatus number.
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
F_GAP_HZ=100.0
DEAD_S=1e-3

# Relational covariance endpoint graph: same row pattern as the declared
# centered covariance design, now interpreted for relational potential probes.
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


def pack_and_rows():
    Q=t11.lanczos_q(i57.Q0)
    pack=i54.make_pack(Q,i57.Y1,i57.TIMES)
    p0=i57.probe_at(Q,0.0); p1=i57.probe_at(Q,i57.Y1)
    pref=i57.probe_at(Q,i57.YREF)
    g0=i57.grad_at(Q,0.0); g1=i57.grad_at(Q,i57.Y1)
    rm,rc=i54.operator_rows([p0-pref,p1-pref],i57.TIMES)
    fm,_fc=i54.operator_rows([g0,g1],i57.TIMES)
    means=np.vstack([rm,fm])
    return pack,means,rc


def profiled(pack,means,covs,c_alpha):
    M=np.vstack([means,covs]) if len(covs) else means
    W=np.r_[np.full(len(means),i57.GM),np.full(len(covs),i57.GC)]
    s=pack['s2']; B=pack['B2']; Zu=pack['Zu']; theta0=pack['theta0']
    Jd=np.column_stack([s,s,B@Zu])
    F=Jd.T@Jd
    Jc=np.column_stack([M@theta0,M@Zu])
    F[1:,1:]+=Jc.T@(W[:,None]*Jc)
    F[1,1]+=c_alpha
    N=F[1:,1:]; c=F[0,1:]
    return float(F[0,0]-c@np.linalg.solve(N,c))


def min_calpha(pack,means,covs,target=TARGET):
    if profiled(pack,means,covs,0.0)>=target:
        return 0.0
    lo,hi=0.0,1.0
    while profiled(pack,means,covs,hi)<target and hi<1e12:
        hi*=10.0
    if hi>=1e12 and profiled(pack,means,covs,hi)<target:
        return np.inf
    for _ in range(90):
        mid=0.5*(lo+hi)
        if profiled(pack,means,covs,mid)>=target: hi=mid
        else: lo=mid
    return hi


def graph_rho2(indices):
    if not indices:
        return 0.0
    nodes=sorted({x for j in indices for x in EDGES[j]})
    ind={x:i for i,x in enumerate(nodes)}
    A=np.zeros((len(nodes),len(nodes)))
    for j in indices:
        a,b=EDGES[j]
        A[ind[a],ind[b]]=A[ind[b],ind[a]]=1.0
    ev=np.linalg.eigvalsh(A)
    return float(np.max(np.abs(ev))**2)


def covariance_wall_hours(indices):
    if not indices:
        return 0.0
    n_floor=i57.GC*graph_rho2(indices)
    cycle=float(np.max(i57.TIMES))/(2.0*math.pi*F_GAP_HZ)+DEAD_S
    return n_floor/P_ACCEPT*cycle/3600.0


def mean_wall_hours(xi_mu=1.0):
    if xi_mu<=0: raise ValueError
    # Relational and direct-force means are conservatively separate campaigns.
    # Within each family the two same-time probe rows share one phase layer.
    cycles=np.sum(i57.TIMES/(2.0*math.pi*F_GAP_HZ)+DEAD_S)
    one_family=i57.GM/P_ACCEPT*float(cycles)/(xi_mu*xi_mu)
    return 2.0*one_family/3600.0


def total_aux_hours(indices,c_alpha,R_alpha,xi_mu=3.0):
    if R_alpha<=0: return np.inf
    return mean_wall_hours(xi_mu)+covariance_wall_hours(indices)+c_alpha/R_alpha/3600.0


def main():
    pack,means,rc=pack_and_rows()
    table=[]
    for k in range(9):
        combos=[()] if k==0 else itertools.combinations(range(8),k)
        best=None
        for inds in combos:
            cov=rc[list(inds)] if inds else np.empty((0,rc.shape[1]))
            ca=min_calpha(pack,means,cov)
            item=(ca,tuple(inds),graph_rho2(inds),covariance_wall_hours(inds))
            if best is None or ca<best[0]: best=item
        table.append(best)
        print('k',k,'best-by-C_alpha',best)

    # Resource-relevant prescan branches retained from Iteration 059.
    expected={
        4: (15.061939558628682,(2,4,5,6)),
        5: (13.819478635553859,(2,3,4,5,6)),
        8: (13.669414719050629,tuple(range(8))),
    }
    for k,(ca,inds) in expected.items():
        assert table[k][1]==inds
        assert abs(table[k][0]-ca)<3e-8

    k4=table[4]; k5=table[5]; k8=table[8]
    assert abs(k4[2]-2.0)<2e-12
    assert abs(k5[2]-(5.0+math.sqrt(5.0))/2.0)<2e-12
    assert abs(k8[2]-6.0)<2e-12
    assert abs(k4[3]-19.830283481773925)<3e-10
    assert abs(k5[3]-35.873319821801836)<3e-10
    assert abs(k8[3]-59.490850445321776)<3e-10

    # Two independent seven-layer mean families at the transparent xi_mu=3
    # benchmark cost only a few hours; source metrology can dominate total time.
    m3=mean_wall_hours(3.0)
    print('two-family mean wall h xi=3',m3)
    assert abs(m3-5.782669933968786)<3e-12

    def crossing(a,b):
        ca,_,_,ha=a; cb,_,_,hb=b
        return (ca-cb)/((hb-ha)*3600.0)

    r45=crossing(k4,k5)
    r58=crossing(k5,k8)
    print('k4->k5 R_alpha crossing',r45)
    print('k5->k8 R_alpha crossing',r58)
    assert abs(r45-2.151263806130919e-5)<3e-15
    assert abs(r58-1.7649779697706861e-6)<3e-16

    for rate in (1e-4,2.2e-5,2e-5,1e-5,2e-6,1e-6):
        vals={
            'k4':total_aux_hours(k4[1],k4[0],rate,3.0),
            'k5':total_aux_hours(k5[1],k5[0],rate,3.0),
            'k8':total_aux_hours(k8[1],k8[0],rate,3.0),
        }
        print('R_alpha',rate,'total auxiliary h',vals,'winner',min(vals,key=vals.get))

if __name__=='__main__':
    main()
