"""RQIR Iteration 064 / Toy013 search.

Search the exact nearest-neighbour Jacobi-chain manifold using the *physical*
two-band D2 metric with the relative spectral-tilt nuisance already profiled.
Cheap stage preserves both harmonics and conditioning; expensive stage audits
spectral-tilt-profiled centered NP3 calibration using Iteration 063 machinery.
No global-optimum or new-physics claim is made.
"""
from __future__ import annotations
import math
import heapq
import numpy as np
import toy011_local_nearest_neighbor_source as t11
import d2_spectral_tilt_profiled_calibration_iteration063 as i63

SEED=20260830064
N_SCAN=30000
N_SURVIVE=120
SMIN_FLOOR=7.5e-4
IMBALANCE_FLOOR=0.06


def cheap_score(r, d2_base):
    p2=abs(r['G2'])**2; p4=abs(r['G4'])**2
    if p2+p4<=0: return -math.inf
    balance=min(p2,p4)/max(p2,p4)
    if balance<IMBALANCE_FLOOR or r['smin']<SMIN_FLOOR: return -math.inf
    # Physical tilt-profiled information is exactly t11.seff(G2,G4).
    # Conditioning enters softly so it cannot compensate a collapsed band.
    phys=r['D2']/d2_base
    return math.log(max(phys,1e-300))+0.35*math.log(r['smin']/SMIN_FLOOR)+0.20*math.log(balance)


def main():
    _,_,_,d2_base=t11.baseline_009()
    rng=np.random.default_rng(SEED)
    heap=[]
    for trial in range(N_SCAN):
        q0=np.exp(rng.normal(0.0,0.85,size=t11.D)); q0/=np.linalg.norm(q0)
        y1=-rng.uniform(0.75,15.0)
        times=np.r_[0.0,rng.uniform(0.0,2.0*math.pi,6)]
        r=t11.evaluate(q0,y1,times)
        if r is None: continue
        score=cheap_score(r,d2_base)
        if not np.isfinite(score): continue
        item=(score,trial,q0.copy(),float(y1),times.copy())
        if len(heap)<N_SURVIVE: heapq.heappush(heap,item)
        elif score>heap[0][0]: heapq.heapreplace(heap,item)

    survivors=sorted(heap,reverse=True)
    assert survivors
    audited=[]
    for score,trial,q0,y1,times in survivors:
        r=t11.evaluate(q0,y1,times)
        pack,B,s,tilt,seff=i63.physical_pack(r['Q'],r['y1'],r['times'])
        gu,best=i63.optimize(pack,B,s,tilt)
        p2=abs(r['G2'])**2; p4=abs(r['G4'])**2
        balance=min(p2,p4)/max(p2,p4)
        audited.append((best[0],-seff,-r['smin'],trial,score,balance,r,best,gu))

    audited.sort(key=lambda x:(x[0],x[1],x[2]))
    for rank,a in enumerate(audited[:12],1):
        cost,negseff,negsmin,trial,score,balance,r,best,gu=a
        hp,hm,res=t11.exact_checks(r)
        Hsite=r['Q'].T@np.diag(t11.E)@r['Q']
        far=Hsite.copy()
        for i in range(t11.D):
            for j in range(t11.D):
                if i==j or abs(i-j)==1: far[i,j]=0.0
        print(rank,'trial',trial,'cost',cost,'seff',-negseff,'smin',-negsmin,
              'balance',balance,'score',score,'gm/gc',best[1:], 'uniform',gu)
        print('q0',r['q0']); print('y1',r['y1']); print('times',r['times'])
        print('state minima',hp.min(),hm.min(),'null residual',res,'far norm',np.linalg.norm(far))
        assert np.linalg.norm(far)<2e-12
        assert hp.min()>0 and hm.min()>0 and res<1e-12
        assert abs((s@s-(s@tilt)**2/(tilt@tilt))-1.0)<2e-9

if __name__=='__main__':
    main()
