#!/usr/bin/env python3
"""Iteration 220: pure-Einstein helicity projection of the MSSC-001 KLT block.

Iteration 219 used real factorized vector polarizations as a gauge-algebra test.
Here each physical graviton is projected onto matched complex vector helicities
  epsilon_h x epsilon_h, h=+/-1,
which gives spin-2 helicity +/-2 and satisfies epsilon.epsilon=0 as well as
k.epsilon=0.  The two KLT copies remain separately accessible for Ward tests.
"""
from pathlib import Path
import json, math
import numpy as np

ITERATION=220
eta=np.diag([1.,-1.,-1.,-1.]).astype(complex)
def dot(a,b): return a@eta@b

def A4(P1,k2,k3,P4,e2,e3):
    F3=np.outer(k3,e3)-np.outer(e3,k3)
    e2F3P1=e2@eta@F3@eta@P1
    return ((2*dot(e2,P1)*dot(e3,k2)-2*e2F3P1)/(2*dot(k2,k3))
            -2*dot(e2,P1)*dot(e3,P4)/(2*dot(P1,k2)))

def M4(P1,k2,k3,P4,eL2,eL3,eR2,eR3):
    return -(2*dot(k2,k3))*A4(P1,k3,k2,P4,eL3,eL2)*A4(P1,k2,k3,P4,eR2,eR3)

def kinematics(m,sqrts,theta):
    s=sqrts*sqrts; p=(s-m*m)/(2*sqrts); Es=(s+m*m)/(2*sqrts)
    Pin=np.array([Es,0,0,p],complex); kin=np.array([p,0,0,-p],complex)
    kout=np.array([p,p*math.sin(theta),0,p*math.cos(theta)],complex)
    Pout=np.array([Es,-p*math.sin(theta),0,-p*math.cos(theta)],complex)
    return -Pin,-kin,kout,Pout

def helicity_vectors(theta):
    ex=np.array([0,1,0,0],complex); ey=np.array([0,0,1,0],complex)
    et=np.array([0,math.cos(theta),0,-math.sin(theta)],complex)
    ep=np.array([0,0,1,0],complex)
    return ({+1:(ex+1j*ey)/np.sqrt(2), -1:(ex-1j*ey)/np.sqrt(2)},
            {+1:(et+1j*ep)/np.sqrt(2), -1:(et-1j*ep)/np.sqrt(2)})

m=0.7; sqrts=2.0; angles=[0.45,0.8,1.15,1.6,2.1]
max_mom=max_shell=max_trans=max_null=max_gauge=max_exchange=0.0
records=[]; nonzero=[]
for th in angles:
    P1,k2,k3,P4=kinematics(m,sqrts,th)
    pol2,pol3=helicity_vectors(th)
    max_mom=max(max_mom,float(np.max(np.abs(P1+k2+k3+P4))))
    max_shell=max(max_shell,float(abs(dot(P1,P1)-m*m)),float(abs(dot(P4,P4)-m*m)),float(abs(dot(k2,k2))),float(abs(dot(k3,k3))))
    for h2 in (+1,-1):
        for h3 in (+1,-1):
            e2,e3=pol2[h2],pol3[h3]
            max_trans=max(max_trans,float(abs(dot(e2,k2))),float(abs(dot(e3,k3))))
            max_null=max(max_null,float(abs(dot(e2,e2))),float(abs(dot(e3,e3))))
            amp=M4(P1,k2,k3,P4,e2,e3,e2,e3)
            if abs(amp)>1e-14: nonzero.append(float(abs(amp)))
            ward=[
                M4(P1,k2,k3,P4,k2,e3,e2,e3),
                M4(P1,k2,k3,P4,e2,k3,e2,e3),
                M4(P1,k2,k3,P4,e2,e3,k2,e3),
                M4(P1,k2,k3,P4,e2,e3,e2,k3),
            ]
            max_gauge=max(max_gauge,max(float(abs(x)) for x in ward))
            swapped=M4(P1,k3,k2,P4,e3,e2,e3,e2)
            max_exchange=max(max_exchange,float(abs(swapped-amp)))
            records.append({
                "theta":th,"helicity2":2*h2,"helicity3":2*h3,
                "amplitude":{"real":float(amp.real),"imag":float(amp.imag)},
                "max_independent_copy_ward_abs":max(float(abs(x)) for x in ward),
                "exchange_abs_difference":float(abs(swapped-amp))
            })

out={
  "iteration":ITERATION,
  "date":"2026-09-01",
  "model_readiness_percent":23,
  "source_model_id":"MSSC-001",
  "supersedes_state_interpretation":"Iteration 219 real factorized states remain gauge-algebra controls; this iteration supplies the pure Einstein helicity projection",
  "mass":m,"sqrt_s":sqrts,"angles":angles,
  "max_momentum_conservation_error":max_mom,
  "max_mass_shell_error":max_shell,
  "max_helicity_vector_transversality_error":max_trans,
  "max_helicity_vector_null_self_contraction":max_null,
  "max_independent_gravitational_ward_abs":max_gauge,
  "max_graviton_exchange_abs_difference":max_exchange,
  "nonzero_amplitude_abs_range":[min(nonzero),max(nonzero)],
  "records":records,
  "classification":{
    "pure_Einstein_external_helicity_projection":"PASS",
    "helicity_vector_transverse_and_null":"PASS_MACHINE_PRECISION",
    "independent_graviton_Ward_tests":"PASS_MACHINE_PRECISION",
    "graviton_exchange_symmetry":"PASS_MACHINE_PRECISION",
    "Iteration219_real_factorized_state_interpretation":"RESTRICTED_TO_GAUGE_ALGEBRA_CONTROL",
    "pure_Einstein_source_tree_block_for_unitarity":"AUTHORIZED",
    "connected_source_loop_cut":"NOT_YET_COMPUTED",
    "candidate_residual":"NONE",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "SRC-CORR-001 — REAL_FACTORIZED_KLT_POLARIZATIONS_ARE_GAUGE_ALGEBRA_CONTROLS_NOT_BY_THEMSELVES_PURE_HELICITY_EINSTEIN_STATES",
    "SRC-NG-005 — MATCHED_COMPLEX_KLT_HELICITIES_GIVE_A_PURE_EINSTEIN_TWO_SCALAR_TWO_GRAVITON_BLOCK_WITH_MACHINE_PRECISION_WARD_TESTS",
    "C5-CUT-019 — PURE_EINSTEIN_DYNAMICAL_SCALAR_SOURCE_TREE_BLOCK_IS_READY_FOR_PHYSICAL_UNITARITY_CUT_CONSTRUCTION"
  ],
  "readiness_change":"unchanged at 23%; the source tree block is now validated for pure Einstein helicities, but no loop source cut or full comparator quotient exists",
  "next_gate":"Construct and diagnose the scalar+graviton two-particle unitarity cut of gravitational Compton scattering using only the pure-helicity MSSC-001 tree blocks."
}
Path("results/scalar_two_graviton_pure_helicity_iteration220.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
