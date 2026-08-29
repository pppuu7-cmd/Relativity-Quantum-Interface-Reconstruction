"""RQIR Iteration 062: audit Toy012 detector-norm versus physical two-band Fisher.

Toy012 Iteration 055 ranked local candidates partly with the Euclidean norm of
the four real harmonic detector components.  Iteration 019's physical D1/D2
resource model, however, profiles a relative spectral-tilt nuisance and needs
information in both n=2 and n=4 bands.  This script compares those metrics and
withdraws any wall-clock interpretation based only on the Euclidean norm.
"""
from __future__ import annotations
import math
import numpy as np

import toy011_local_nearest_neighbor_source as t11
import toy011_centered_profiled_resource_audit_iteration054 as i54
import toy012_resource_aware_local_codesign_iteration055 as i55
import branch_specific_fisher_rates_iteration019 as i19


def physical_harmonics(pack):
    delta=2.0*t11.EPS*pack['d0']
    p0=pack['p0']; g0=pack['g0']
    H2=t11.harmonic(delta,p0,p0,2)
    H4=t11.harmonic(delta,p0,p0,4)
    G2=t11.harmonic(delta,g0,p0,2)
    G4=t11.harmonic(delta,g0,p0,4)
    return H2,H4,G2,G4


def profile_two_band(z2,z4):
    p2,p4=abs(z2)**2,abs(z4)**2
    return 0.0 if p2<=0 or p4<=0 else 4.0*p2*p4/(p2+p4)


def optimize_d1_switch(h2,h4,n=120000):
    best=(-1.0,None,None,None)
    for a in np.linspace(1e-6,math.pi-1e-6,n):
        w2,w4=i19.four_switch_windows(float(a))
        score=profile_two_band(h2*w2,h4*w4)
        if score>best[0]:
            best=(score,float(a),w2,w4)
    return best


def summary(cand,base_pack):
    pack=i54.make_pack(cand['Q'],cand['y1'],cand['times'])
    H2,H4,G2,G4=physical_harmonics(pack)
    bH2,bH4,bG2,bG4=physical_harmonics(base_pack)
    norm_d1=(abs(H2)**2+abs(H4)**2)/(abs(bH2)**2+abs(bH4)**2)
    norm_d2=(abs(G2)**2+abs(G4)**2)/(abs(bG2)**2+abs(bG4)**2)
    d2_ratio=profile_two_band(G2,G4)/profile_two_band(bG2,bG4)
    d1=optimize_d1_switch(H2,H4)
    d1b=optimize_d1_switch(bH2,bH4)
    d1_ratio=d1[0]/d1b[0]
    return dict(pack=pack,H2=H2,H4=H4,G2=G2,G4=G4,
                norm_d1=norm_d1,norm_d2=norm_d2,
                d1_ratio=d1_ratio,d2_ratio=d2_ratio,
                d1_switch=d1,asd_balance=abs(G4)/abs(G2))


def main():
    base=i54.make_pack(t11.V009_SORTED,t11.Y1_BASE,t11.TIMES_BASE)
    balanced=i55.refined_candidate(1638,182)
    high=i55.refined_candidate(1638,382)
    sb=summary(balanced,base)
    sh=summary(high,base)

    for name,s in [('balanced',sb),('high-response',sh)]:
        print('\n',name)
        print('G2,G4',s['G2'],s['G4'])
        print('Euclidean D2 norm-power ratio',s['norm_d2'])
        print('profiled equal-ASD D2 ratio',s['d2_ratio'])
        print('science-time factor',1.0/s['d2_ratio'])
        print('ASD4/ASD2 for equal band Fisher',s['asd_balance'])
        print('D1 Euclidean ratio',s['norm_d1'])
        print('D1 source-optimized four-switch profiled ratio',s['d1_ratio'])

    # Balanced Toy012 regression: Iteration 055's 0.21617 number is a detector
    # vector norm ratio, not the physical spectral-profiled D2 rate ratio.
    assert abs(sb['norm_d2']-0.2161694245369)<3e-10
    assert abs(sb['d2_ratio']-1.9696285538e-8)<4e-16
    assert abs(1.0/sb['d2_ratio']-5.077099426e7)<20.0
    assert abs(sb['asd_balance']-1.50428055945e-4)<3e-13
    assert abs(sb['d1_ratio']-5.81034720e-8)<3e-14

    # The aggressive local point also suffers spectral collapse, though less
    # severely than the balanced candidate.
    assert abs(sh['norm_d2']-0.30469389709)<3e-9
    assert abs(sh['d2_ratio']-1.2139856294e-4)<3e-12
    assert abs(1.0/sh['d2_ratio']-8237.3298)<2e-3
    assert abs(sh['asd_balance']-0.00994836419)<3e-10
    assert abs(sh['d1_ratio']-2.94418634e-6)<3e-12

    # Toy009 regression agrees with Iteration 019 equal-ASD D2 source factor.
    bH2,bH4,bG2,bG4=physical_harmonics(base)
    assert abs(profile_two_band(bG2,bG4)-0.000577950719611)<3e-15
    d1b=optimize_d1_switch(bH2,bH4)
    assert abs(d1b[0]-i19.FOUR_SWITCH_SEFF)<2e-9

if __name__=='__main__':
    main()
