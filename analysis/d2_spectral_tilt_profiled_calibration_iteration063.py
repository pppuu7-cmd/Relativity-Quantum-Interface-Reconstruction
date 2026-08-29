"""RQIR Iteration 063: put the physical two-band spectral-tilt nuisance inside
D2 source/calibration Fisher before comparing local source candidates.

For a four-real-component detector vector s=(G2_re,G2_im,G4_re,G4_im), a
relative spectral-tilt nuisance has score t=(G2_re,G2_im,-G4_re,-G4_im).
Profiling t gives exactly

    F_beta|tilt = 4 p2 p4/(p2+p4),

for unit/equal band noise.  The detector/source nuisance Jacobian is normalized
by sqrt(F_beta|tilt), so beta has unit Fisher after profiling tilt alone.  This
makes calibration cost comparable across source geometries in the same physical
D2 metric.
"""
from __future__ import annotations
import math
import numpy as np

import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54
import toy012_resource_aware_local_codesign_iteration055 as i55

TARGET=0.90


def candidate_at_trial(index):
    rng=np.random.default_rng(t11.SEED)
    out=None
    for trial in range(index+1):
        q0=np.exp(rng.normal(0.0,0.8,size=t11.D)); q0/=np.linalg.norm(q0)
        y1=-rng.uniform(1.0,12.0)
        times=np.r_[0.0,rng.uniform(0.0,2.0*math.pi,6)]
        if trial==index:
            out=t11.evaluate(q0,y1,times)
    return out


def physical_pack(Q,y1,times):
    pack=i54.make_pack(Q,y1,times)
    # i54.B2raw is the four-real-component harmonic Jacobian.
    Braw=pack['B2raw']; sraw=Braw@pack['theta0']
    p2=float(sraw[:2]@sraw[:2]); p4=float(sraw[2:]@sraw[2:])
    seff=4.0*p2*p4/(p2+p4)
    B=Braw/math.sqrt(seff)
    s=B@pack['theta0']
    tilt=np.r_[s[:2],-s[2:]]
    return pack,B,s,tilt,seff


def profiled_known(pack,B,s,tilt,gm,gc):
    Zu=pack['Zu']
    bu=B@Zu
    Jn=np.column_stack([bu,tilt])
    Fnn=Jn.T@Jn
    am=pack['pm']@Zu; ac=pack['pc']@Zu
    Fnn[:22,:22]+=gm*(am.T@am)+gc*(ac.T@ac)
    cross=s@Jn
    return float(s@s-cross@np.linalg.solve(Fnn,cross))


def required_cov(pack,B,s,tilt,gm,target=TARGET):
    lo,hi=1e1,1e14
    if profiled_known(pack,B,s,tilt,gm,hi)<target:
        return math.inf
    for _ in range(60):
        mid=math.sqrt(lo*hi)
        if profiled_known(pack,B,s,tilt,gm,mid)>=target: hi=mid
        else: lo=mid
    return hi


def uniform(pack,B,s,tilt,target=TARGET):
    lo,hi=1e2,1e14
    for _ in range(60):
        mid=math.sqrt(lo*hi)
        if profiled_known(pack,B,s,tilt,mid,mid)>=target: hi=mid
        else: lo=mid
    return hi


def optimize(pack,B,s,tilt,target=TARGET):
    gu=uniform(pack,B,s,tilt,target)
    best=(22.0*gu,gu,gu)
    for gm in np.logspace(3,12,900):
        gc=required_cov(pack,B,s,tilt,float(gm),target)
        if np.isfinite(gc):
            cost=14.0*gm+8.0*gc
            if cost<best[0]: best=(float(cost),float(gm),float(gc))
    return gu,best


def main():
    candidates={
        'Toy009': (t11.V009_SORTED,t11.Y1_BASE,t11.TIMES_BASE),
    }
    r=candidate_at_trial(6304); c=candidate_at_trial(3811)
    b=i55.refined_candidate(1638,182); h=i55.refined_candidate(1638,382)
    candidates.update({
        'Toy011-response':(r['Q'],r['y1'],r['times']),
        'Toy011-conditioning':(c['Q'],c['y1'],c['times']),
        'Toy012-balanced':(b['Q'],b['y1'],b['times']),
        'Toy012-high':(h['Q'],h['y1'],h['times']),
    })

    out={}
    for name,(Q,y,times) in candidates.items():
        pack,B,s,tilt,seff=physical_pack(Q,y,times)
        # Regression: tilt profiling alone gives unit beta Fisher.
        ftilt=float(s@s-(s@tilt)**2/(tilt@tilt))
        assert abs(ftilt-1.0)<2e-9
        gu,best=optimize(pack,B,s,tilt)
        out[name]=(seff,gu,best)
        print(name,'seff',seff,'uniform',gu,'best',best)

    base=out['Toy009'][2][0]
    ratios={name:v[2][0]/base for name,v in out.items()}
    print('physical calibration-cost ratios',ratios)

    # Stable values from the declared 900-point group scan. Small changes in
    # scan resolution can move gm/gc individually, so regression is on total
    # cost ratios at modest tolerance.
    assert abs(out['Toy009'][2][0]-2.91e7)/2.91e7<0.03
    assert abs(ratios['Toy011-response']-21.7)<0.8
    assert abs(ratios['Toy011-conditioning']-8.83)<0.35
    assert 4.4e4<ratios['Toy012-balanced']<5.0e4
    assert 490<ratios['Toy012-high']<550

if __name__=='__main__':
    main()
