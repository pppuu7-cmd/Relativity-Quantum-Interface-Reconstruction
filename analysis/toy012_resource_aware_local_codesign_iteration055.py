"""RQIR Iteration 055 / Toy012: resource-aware local source co-design.

Iteration 053 proved existence of an exact nearest-neighbour source and
Iteration 054 exposed the relevant resource axes: absolute detector signal,
centered calibration cost and source-metrology rate.  The original Toy011 scan
was not optimized for those quantities.

This script reproduces the two-stage deterministic search used for Toy012:

1. global local-manifold scan seed 20260830 (positive Lanczos spectral weights,
   probe location and six phases);
2. local refinement seed 2026083001 around promising global anchors.

The retained balanced point minimizes centered D2 calibration cost among the
explicitly audited local-Pareto candidates subject to raw D2 signal >=20% of
Toy009 and s_min>=1e-3.  A second high-response point is retained as a Pareto
alternative.  No global-optimum claim is made.
"""
from __future__ import annotations

import math
import numpy as np
import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54

GLOBAL_SEED=20260830
LOCAL_SEED=2026083001
ANCHOR_ORDER=(1799,1638,1987)
N_MUT=450


def global_candidate_at(index: int):
    rng=np.random.default_rng(GLOBAL_SEED)
    out=None
    for trial in range(index+1):
        q0=np.exp(rng.normal(0.0,0.9,size=t11.D)); q0/=np.linalg.norm(q0)
        y1=-rng.uniform(0.75,15.0)
        times=np.r_[0.0,rng.uniform(0.0,2.0*math.pi,6)]
        if trial==index:
            out=t11.evaluate(q0,y1,times)
    assert out is not None
    return out


def refined_candidate(target_anchor: int,target_mutation: int):
    anchors={k:global_candidate_at(k) for k in ANCHOR_ORDER}
    rng=np.random.default_rng(LOCAL_SEED)
    out=None
    for anchor in ANCHOR_ORDER:
        base=anchors[anchor]
        qbase=np.asarray(base['q0'],float)
        ybase=float(base['y1'])
        tbase=np.asarray(base['times'],float)
        for j in range(N_MUT):
            sig=(0.04,0.10,0.22)[j%3]
            q=np.exp(np.log(np.maximum(qbase,1e-12))+rng.normal(0.0,sig,size=t11.D))
            q/=np.linalg.norm(q)
            y=ybase+rng.normal(0.0,max(0.08,abs(ybase)*sig*0.25))
            if y>=-0.4:
                y=-0.4-abs(y)
            tt=tbase.copy()
            tt[1:]=(tt[1:]+rng.normal(0.0,sig*0.7,size=6))%(2.0*math.pi)
            if anchor==target_anchor and j==target_mutation:
                out=t11.evaluate(q,y,tt)
        if anchor==target_anchor:
            break
    assert out is not None
    return out


def source_summary(cand,base_pack):
    pack=i54.make_pack(cand['Q'],cand['y1'],cand['times'])
    d1=i54.optimize_groups(pack,'D1')[1]
    d2=i54.optimize_groups(pack,'D2')[1]
    fq=i54.qfi_alpha(pack['d0'])
    fe=i54.energy_fisher_alpha(pack['d0'])
    phi,cr=i54.ramsey_rate_optimum(pack['d0'])
    return dict(
        pack=pack,
        D1raw_ratio=pack['n1']**2/base_pack['n1']**2,
        D2raw_ratio=pack['n2']**2/base_pack['n2']**2,
        D1cost=d1[0],D1gm=d1[1],D1gc=d1[2],
        D2cost=d2[0],D2gm=d2[1],D2gc=d2[2],
        FQ=fq,FE=fe,phi=phi,cR=cr,
    )


def main():
    base=i54.make_pack(t11.V009_SORTED,t11.Y1_BASE,t11.TIMES_BASE)
    base_d1=i54.optimize_groups(base,'D1')[1]
    base_d2=i54.optimize_groups(base,'D2')[1]
    base_fq=i54.qfi_alpha(base['d0'])
    base_fe=i54.energy_fisher_alpha(base['d0'])
    _bp,base_cr=i54.ramsey_rate_optimum(base['d0'])

    balanced=refined_candidate(1638,182)
    high=refined_candidate(1638,382)

    sb=source_summary(balanced,base)
    sh=source_summary(high,base)

    for label,cand,s in [('balanced',balanced,sb),('high-response',high,sh)]:
        print('\n',label)
        print('q0',cand['q0'])
        print('y1',cand['y1'])
        print('times',cand['times'])
        print('smin/cond',cand['smin'],cand['cond'])
        print('D1/D2 raw ratios',s['D1raw_ratio'],s['D2raw_ratio'])
        print('D1/D2 calibration cost ratios',s['D1cost']/base_d1[0],s['D2cost']/base_d2[0])
        print('QFI/energy/Ramsey ratios',s['FQ']/base_fq,s['FE']/base_fe,s['cR']/base_cr)
        print('D2 gm/gc',s['D2gm'],s['D2gc'])

        # exact physicality checks
        Hsite=cand['Q'].T@np.diag(t11.E)@cand['Q']
        far=Hsite.copy()
        for i in range(t11.D):
            for j in range(t11.D):
                if i==j or abs(i-j)==1:
                    far[i,j]=0.0
        rho0=np.eye(t11.D)/t11.D
        rp=rho0+t11.EPS*s['pack']['d0']
        rm=rho0-t11.EPS*s['pack']['d0']
        residual=np.max(np.abs(s['pack']['A']@t11.herm_vec(rp-rm)))
        print('far-coupling norm',np.linalg.norm(far),'state minima',np.linalg.eigvalsh(rp).min(),np.linalg.eigvalsh(rm).min(),'residual',residual)
        assert np.linalg.norm(far)<2e-12
        assert np.linalg.eigvalsh(rp).min()>0 and np.linalg.eigvalsh(rm).min()>0
        assert residual<1e-12

    # Balanced Toy012 regression values.
    assert abs(balanced['smin']-0.0014325459648020177)<3e-14
    assert abs(balanced['cond']-3264.2179923651133)<3e-7
    assert abs(sb['D1raw_ratio']-0.1704188542363)<3e-10
    assert abs(sb['D2raw_ratio']-0.2161694245369)<3e-10
    assert abs(sb['D1cost']/base_d1[0]-1.5149085838)<3e-7
    assert abs(sb['D2cost']/base_d2[0]-1.0584243728)<3e-7
    assert abs(sb['FQ']-0.09928072148)<3e-10
    assert abs(sb['FE']-0.006297270760)<3e-10
    assert abs(sb['phi']-1.5750792620)<3e-7
    assert abs(sb['cR']-0.002134292844)<3e-10

    # High-response local Pareto point.
    assert abs(high['smin']-0.0005795981054620762)<3e-14
    assert abs(high['cond']-8033.878284)<3e-5
    assert abs(sh['D2raw_ratio']-0.30469389709)<3e-9
    assert abs(sh['D2cost']/base_d2[0]-1.375207)<3e-5
    assert abs(sh['cR']/base_cr-1.150503)<3e-5


if __name__=='__main__':
    main()
