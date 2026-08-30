"""RQIR Iteration 065: execute the Iteration-064 Toy013 gate and regression-check
its leading physical D2 candidate.

This script preserves the Iteration-064 deterministic search definition but uses
an algebraically identical precomputed Fisher form and scipy.linalg.solve to make
the 900-point gm / 60-step gc profiling practical.  No global optimum or
new-physics claim is made.
"""
from __future__ import annotations
import math, heapq
import numpy as np
import scipy.linalg as la
import toy011_local_nearest_neighbor_source as t11
import d2_spectral_tilt_profiled_calibration_iteration063 as i63

SEED=20260830064
N_SCAN=30000
N_SURVIVE=120
SMIN_FLOOR=7.5e-4
IMBALANCE_FLOOR=0.06
TARGET=0.90


def cheap_score(r,d2_base):
    p2,p4=abs(r['G2'])**2,abs(r['G4'])**2
    if p2+p4<=0:return -math.inf
    balance=min(p2,p4)/max(p2,p4)
    if balance<IMBALANCE_FLOOR or r['smin']<SMIN_FLOOR:return -math.inf
    return math.log(max(r['D2']/d2_base,1e-300))+0.35*math.log(r['smin']/SMIN_FLOOR)+0.20*math.log(balance)


def prep(pack,B,s,tilt):
    Zu=pack['Zu']; bu=B@Zu
    J=np.column_stack([bu,tilt]); K=J.T@J
    am=pack['pm']@Zu; ac=pack['pc']@Zu
    Mm=np.zeros_like(K); Mc=np.zeros_like(K)
    Mm[:22,:22]=am.T@am; Mc[:22,:22]=ac.T@ac
    return K,Mm,Mc,s@J,float(s@s)


def fprof(P,gm,gc):
    K,Mm,Mc,c,ss=P
    x=la.solve(K+gm*Mm+gc*Mc,c,assume_a='sym')
    return float(ss-c@x)


def optimize_fast(pack,B,s,tilt):
    P=prep(pack,B,s,tilt)
    lo,hi=1e2,1e14
    for _ in range(60):
        mid=math.sqrt(lo*hi)
        if fprof(P,mid,mid)>=TARGET:hi=mid
        else:lo=mid
    gu=hi; best=(22*gu,gu,gu)
    for gm in np.logspace(3,12,900):
        if fprof(P,float(gm),1e14)<TARGET:continue
        lo,hi=1e1,1e14
        for _ in range(60):
            mid=math.sqrt(lo*hi)
            if fprof(P,float(gm),mid)>=TARGET:hi=mid
            else:lo=mid
        cost=14*float(gm)+8*hi
        if cost<best[0]:best=(cost,float(gm),hi)
    return gu,best


def main():
    _,_,_,d2_base=t11.baseline_009()
    rng=np.random.default_rng(SEED); heap=[]; nvalid=0
    for trial in range(N_SCAN):
        q0=np.exp(rng.normal(0.0,0.85,size=t11.D)); q0/=np.linalg.norm(q0)
        y1=-rng.uniform(0.75,15.0)
        times=np.r_[0.0,rng.uniform(0.0,2.0*math.pi,6)]
        r=t11.evaluate(q0,y1,times)
        if r is None:continue
        score=cheap_score(r,d2_base)
        if not np.isfinite(score):continue
        nvalid+=1
        item=(score,trial,q0.copy(),float(y1),times.copy())
        if len(heap)<N_SURVIVE:heapq.heappush(heap,item)
        elif score>heap[0][0]:heapq.heapreplace(heap,item)
    assert nvalid==137 and len(heap)==120

    # Full physical Fisher audit of all survivors; sort by total calibration cost.
    out=[]
    for score,trial,q0,y1,times in sorted(heap,reverse=True):
        r=t11.evaluate(q0,y1,times)
        pack,B,s,tilt,seff=i63.physical_pack(r['Q'],r['y1'],r['times'])
        gu,best=optimize_fast(pack,B,s,tilt)
        p2,p4=abs(r['G2'])**2,abs(r['G4'])**2
        balance=min(p2,p4)/max(p2,p4)
        out.append((best[0],trial,seff,r['smin'],balance,r,best,gu,s,tilt))
    out.sort(key=lambda x:x[0])
    cost,trial,seff,smin,balance,r,best,gu,s,tilt=out[0]

    bp,bB,bs,bt,bse=i63.physical_pack(t11.V009_SORTED,t11.Y1_BASE,t11.TIMES_BASE)
    _,bbest=optimize_fast(bp,bB,bs,bt)
    hp,hm,res=t11.exact_checks(r)
    Hsite=r['Q'].T@np.diag(t11.E)@r['Q']; far=Hsite.copy()
    for i in range(t11.D):
        for j in range(t11.D):
            if i==j or abs(i-j)==1:far[i,j]=0.0

    print('winner trial',trial)
    print('q0',r['q0']); print('y1',r['y1']); print('times',r['times'])
    print('cost',cost,'gm/gc',best[1:], 'uniform',gu,'cost/Toy009',cost/bbest[0])
    print('seff',seff,'seff/Toy009',seff/bse,'smin',smin,'cond',r['cond'],'balance',balance)
    print('state minima',hp.min(),hm.min(),'null residual',res,'far norm',np.linalg.norm(far))
    print('tilt-only profiled Fisher',s@s-(s@tilt)**2/(tilt@tilt))

    assert trial==29100
    assert abs(cost-3.5819942712e6)/cost<5e-7
    assert abs(best[1]-1.2086865290e5)/best[1]<5e-7
    assert abs(best[2]-2.3622914132e5)/best[2]<5e-7
    assert abs(cost/bbest[0]-0.1233011369)<2e-7
    assert abs(seff-2.44381107074e-5)<2e-15
    assert abs(seff/bse-0.04228407350)<2e-10
    assert abs(smin-0.00132918812262)<3e-14
    assert abs(balance-0.90475514044)<2e-10
    assert np.linalg.norm(far)<2e-12
    assert hp.min()>0 and hm.min()>0 and res<1e-12
    assert abs((s@s-(s@tilt)**2/(tilt@tilt))-1.0)<2e-9

if __name__=='__main__':
    main()
