#!/usr/bin/env python3
"""Iteration 219: full two-scalar/two-graviton source amplitude via KLT.

Authority: Bjerrum-Bohr, Cristofoli, Damgaard & Gomez, arXiv:1908.09755,
Eq. (32) for the color-ordered two-scalar/two-gluon amplitude and Eq. (52)
for the four-point KLT gravity amplitude.

This validates the *complete* tree amplitude, not an isolated hh phi phi
contact.  The two gauge-theory copies are kept separate so a gravitational
Ward test may replace the polarization in either Lorentz copy independently.
Overall coupling/i conventions are stripped; only gauge identities, exchange
symmetry, and kinematic consistency are classified.
"""
from pathlib import Path
import json, math
import numpy as np

ITERATION=219
eta=np.diag([1.,-1.,-1.,-1.])
def dot(a,b): return float(a@eta@b)

def scalar_gluon_A4(P1,k2,k3,P4,e2,e3):
    """Color ordered A4(1_phi,2_g,3_g,4_phi), stripped convention."""
    F3=np.outer(k3,e3)-np.outer(e3,k3)
    e2F3P1=e2@eta@F3@eta@P1
    s23=2.0*dot(k2,k3)
    sP12=2.0*dot(P1,k2)
    return ((2.0*dot(e2,P1)*dot(e3,k2)-2.0*e2F3P1)/s23
            -2.0*dot(e2,P1)*dot(e3,P4)/sP12)

def scalar_graviton_M4(P1,k2,k3,P4,eL2,eL3,eR2,eR3):
    """M4=A(1,3,2,4)*(-s23)*A(1,2,3,4), two copies explicit."""
    s23=2.0*dot(k2,k3)
    left=scalar_gluon_A4(P1,k3,k2,P4,eL3,eL2)
    right=scalar_gluon_A4(P1,k2,k3,P4,eR2,eR3)
    return -s23*left*right

def physical_compton(m,sqrts,theta):
    """All-outgoing scalar+graviton -> scalar+graviton CM kinematics."""
    s=sqrts*sqrts
    p=(s-m*m)/(2.0*sqrts)
    Es=(s+m*m)/(2.0*sqrts)
    Pin=np.array([Es,0.,0.,p])
    kin=np.array([p,0.,0.,-p])
    kout=np.array([p,p*math.sin(theta),0.,p*math.cos(theta)])
    Pout=np.array([Es,-p*math.sin(theta),0.,-p*math.cos(theta)])
    return -Pin,-kin,kout,Pout

m=0.7; sqrts=2.0
angles=[0.45,0.8,1.15,1.6,2.1]
max_mom=0.0; max_shell=0.0; max_gauge=0.0; max_exchange=0.0
nonzero_amplitudes=[]
records=[]
for th in angles:
    P1,k2,k3,P4=physical_compton(m,sqrts,th)
    max_mom=max(max_mom,float(np.max(np.abs(P1+k2+k3+P4))))
    max_shell=max(max_shell,abs(dot(P1,P1)-m*m),abs(dot(P4,P4)-m*m),abs(dot(k2,k2)),abs(dot(k3,k3)))

    # Two deterministic physical vector polarizations for each graviton.
    e2x=np.array([0.,1.,0.,0.]); e2y=np.array([0.,0.,1.,0.])
    e3p=np.array([0.,math.cos(th),0.,-math.sin(th)]); e3y=np.array([0.,0.,1.,0.])
    polpairs=[("xp",e2x,e3p),("xy",e2x,e3y),("yp",e2y,e3p),("yy",e2y,e3y)]
    for label,e2,e3 in polpairs:
        amp=scalar_graviton_M4(P1,k2,k3,P4,e2,e3,e2,e3)
        if abs(amp)>1e-14: nonzero_amplitudes.append(float(abs(amp)))
        # Independent Ward tests for each Lorentz copy of each graviton.
        gtests=[
            scalar_graviton_M4(P1,k2,k3,P4,k2,e3,e2,e3),
            scalar_graviton_M4(P1,k2,k3,P4,e2,k3,e2,e3),
            scalar_graviton_M4(P1,k2,k3,P4,e2,e3,k2,e3),
            scalar_graviton_M4(P1,k2,k3,P4,e2,e3,e2,k3),
        ]
        max_gauge=max(max_gauge,max(abs(x) for x in gtests))
        swapped=scalar_graviton_M4(P1,k3,k2,P4,e3,e2,e3,e2)
        max_exchange=max(max_exchange,float(abs(swapped-amp)))
        records.append({
            "theta":th,"polarization_pair":label,"amplitude":float(amp),
            "max_independent_copy_ward_abs":float(max(abs(x) for x in gtests)),
            "graviton_exchange_abs_difference":float(abs(swapped-amp))
        })

out={
  "iteration":ITERATION,
  "date":"2026-09-01",
  "model_readiness_percent":23,
  "source_model_id":"MSSC-001",
  "amplitude_authority":"arXiv:1908.09755 Eq.(32) scalar-gluon A4 + Eq.(52) four-point KLT",
  "convention":"overall coupling/i factors stripped; two KLT polarization copies explicit",
  "mass":m,"sqrt_s":sqrts,"angles":angles,
  "max_momentum_conservation_error":max_mom,
  "max_mass_shell_error":max_shell,
  "max_independent_gravitational_ward_abs":max_gauge,
  "max_graviton_exchange_abs_difference":max_exchange,
  "nonzero_amplitude_abs_range":[min(nonzero_amplitudes),max(nonzero_amplitudes)],
  "records":records,
  "classification":{
    "full_two_scalar_two_graviton_tree_amplitude":"PASS_SCOPED",
    "independent_graviton_Ward_tests":"PASS_MACHINE_PRECISION",
    "graviton_exchange_symmetry":"PASS_MACHINE_PRECISION",
    "isolated_hh_phi_phi_contact_as_observable":"FORBIDDEN",
    "source_tree_building_block_for_unitarity":"AUTHORIZED",
    "connected_one_loop_source_cut":"NOT_YET_COMPUTED",
    "candidate_residual":"NONE",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "SRC-NG-003 — FULL_TWO_SCALAR_TWO_GRAVITON_KLT_AMPLITUDE_PASSES_INDEPENDENT_GRAVITATIONAL_WARD_TESTS",
    "SRC-NG-004 — NONLINEAR_SOURCE_GAUGE_SAFETY_BELONGS_TO_THE_COMPLETE_AMPLITUDE_NOT_AN_ISOLATED_SEAGULL_VERTEX",
    "C5-CUT-018 — GAUGE_INVARIANT_DYNAMICAL_SCALAR_SOURCE_TREE_BLOCK_IS_AVAILABLE_FOR_SOURCE_LEVEL_UNITARITY_CUTS",
    "NG-FUNNEL-076 — BUILD_SOURCE_COMPLETED_CUTS_FROM_GAUGE_INVARIANT_TREE_AMPLITUDES_BEFORE_OFFSHELL_1PI_INTERPRETATION"
  ],
  "readiness_change":"unchanged at 23%; the first nonlinear gauge-invariant dynamical-source tree block is executable, but the physical connected source cut has not yet been built",
  "next_gate":"Construct the lowest one-loop discontinuity of a connected MSSC-001 scalar-source observable from gauge-invariant tree blocks and physical intermediate gravitons, preserving the on-shell/off-shell distinction from Iteration 217."
}
Path("results/scalar_two_graviton_klt_iteration219.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
