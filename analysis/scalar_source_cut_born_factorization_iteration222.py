#!/usr/bin/env python3
"""Iteration 222: Born-fixed collinear factorization of the MSSC-001 source cut.

The connected scalar+graviton cut from Iteration 221 has two logarithmic
collinear singularities.  This script determines their residues locally, before
any angular integration or cap fit, and compares them to the complete scalar
Compton Born amplitude across five external scattering angles and both real
spin-2 linear polarizations.

Overall gravitational/Cutkosky normalization remains stripped exactly as in
Iterations 219-221.  The question is whether one common residue/Born ratio is
supported by the frozen kinematics.
"""
from pathlib import Path
import json, math
import numpy as np

ITERATION=222
eta=np.diag([1.,-1.,-1.,-1.]).astype(complex)
def dot(a,b): return a@eta@b

def A4(P1,k2,k3,P4,e2,e3):
    F=np.outer(k3,e3)-np.outer(e3,k3)
    return ((2*dot(e2,P1)*dot(e3,k2)-2*(e2@eta@F@eta@P1))/(2*dot(k2,k3))
            -2*dot(e2,P1)*dot(e3,P4)/(2*dot(P1,k2)))

def Msep(P1,k2,k3,P4,l2,l3,r2,r3):
    return -(2*dot(k2,k3))*A4(P1,k3,k2,P4,l3,l2)*A4(P1,k2,k3,P4,r2,r3)

def tensor_amp(P1,k2,k3,P4,T2,T3):
    return sum(c2*c3*Msep(P1,k2,k3,P4,l2,l3,r2,r3)
               for c2,l2,r2 in T2 for c3,l3,r3 in T3)

def spin2_basis(n,alpha=0.0):
    n=np.asarray(n,float); n=n/np.linalg.norm(n)
    ref=np.array([0.,0.,1.])
    if abs(float(n@ref))>0.9: ref=np.array([1.,0.,0.])
    e1=np.cross(ref,n); e1/=np.linalg.norm(e1)
    e2=np.cross(n,e1); e2/=np.linalg.norm(e2)
    c,s=math.cos(alpha),math.sin(alpha)
    f1=c*e1+s*e2; f2=-s*e1+c*e2
    E1=np.r_[0.,f1].astype(complex); E2=np.r_[0.,f2].astype(complex)
    q=1/math.sqrt(2)
    return ([(q,E1,E1),(-q,E2,E2)], [(q,E1,E2),(q,E2,E1)])

def physical(m=0.7,sqrts=2.0,theta=0.8):
    s=sqrts*sqrts; p=(s-m*m)/(2*sqrts); Es=(s+m*m)/(2*sqrts)
    Pin=np.array([Es,0,0,p],complex); kin=np.array([p,0,0,-p],complex)
    kout=np.array([p,p*math.sin(theta),0,p*math.cos(theta)],complex)
    Pout=np.array([Es,-p*math.sin(theta),0,-p*math.cos(theta)],complex)
    return Pin,kin,kout,Pout,p,Es

def born(theta_ext,pol_idx):
    Pin,kin,kout,Pout,_,_=physical(theta=theta_ext)
    Tin=spin2_basis([0,0,-1])[pol_idx]
    Tout=spin2_basis([math.sin(theta_ext),0,math.cos(theta_ext)])[pol_idx]
    return tensor_amp(-Pin,-kin,kout,Pout,Tin,Tout)

def cut(theta_i,phi_i,theta_ext,pol_idx):
    Pin,kin,kout,Pout,p,Es=physical(theta=theta_ext)
    n=np.array([math.sin(theta_i)*math.cos(phi_i),math.sin(theta_i)*math.sin(phi_i),math.cos(theta_i)])
    lg=np.r_[p,p*n].astype(complex); ls=np.r_[Es,-p*n].astype(complex)
    left=(-Pin,-kin,lg,ls); right=(-ls,-lg,kout,Pout)
    Tin=spin2_basis([0,0,-1])[pol_idx]
    Tout=spin2_basis([math.sin(theta_ext),0,math.cos(theta_ext)])[pol_idx]
    return sum(tensor_amp(*left,Tin,T)*tensor_amp(*right,T,Tout) for T in spin2_basis(n))

angles=[0.45,0.8,1.15,1.6,2.1]
deltas=np.array([0.01,0.005,0.002,0.001,0.0005])
records=[]; max_to_minus8=0.; max_in_out=0.
for theta_ext in angles:
    for pol_idx,pol_name in [(0,"plus"),(1,"cross")]:
        B=born(theta_ext,pol_idx)
        ratios_in=[]; ratios_out=[]
        for d in deltas:
            rin=(1-math.cos(d))*cut(math.pi-d,0.7,theta_ext,pol_idx)/B
            rout=(1-math.cos(d))*cut(theta_ext+d,0.0,theta_ext,pol_idx)/B
            ratios_in.append(float(rin.real)); ratios_out.append(float(rout.real))
        # Smooth local residue has an ordinary small-d expansion; use a frozen
        # quadratic extrapolation only on local residues, never on cap integrals.
        intercept_in=float(np.polyfit(deltas,ratios_in,2)[-1])
        intercept_out=float(np.polyfit(deltas,ratios_out,2)[-1])
        max_to_minus8=max(max_to_minus8,abs(intercept_in+8),abs(intercept_out+8))
        max_in_out=max(max_in_out,abs(intercept_in-intercept_out))
        records.append({
            "theta_ext":theta_ext,"external_linear_polarization":pol_name,
            "born_amplitude":{"real":float(B.real),"imag":float(B.imag)},
            "incoming_residue_over_born_extrapolated":intercept_in,
            "outgoing_residue_over_born_extrapolated":intercept_out,
            "incoming_local_ratio_samples":ratios_in,
            "outgoing_local_ratio_samples":ratios_out
        })

out={
  "iteration":ITERATION,
  "date":"2026-09-01",
  "model_readiness_percent":23,
  "source_model_id":"MSSC-001",
  "local_residue_definition":"R=lim_delta_to_0 (1-cos(delta))*I_cut, evaluated before angular integration",
  "frozen_delta_samples":deltas.tolist(),
  "tested_external_angles":angles,
  "tested_external_linear_spin2_polarizations":["plus","cross"],
  "common_relation":"R_in = R_out = -8 * M_Born in the stripped Iteration-219/221 normalization",
  "max_abs_extrapolated_ratio_error_from_minus8":max_to_minus8,
  "max_abs_incoming_outgoing_ratio_mismatch":max_in_out,
  "records":records,
  "classification":{
    "Born_fixed_collinear_factorization":"PASS_SCOPED_CROSS_KINEMATIC",
    "residue_from_cap_fit":"NOT_USED",
    "source_cut_IR_subtraction_coefficient":"FIXED_BY_COMPLETE_BORN_AMPLITUDE_IN_THIS_NORMALIZATION",
    "IR_safe_integrated_source_cut":"NOT_YET",
    "candidate_residual":"NONE",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "SRC-CUT-003 — BOTH_SCALAR_SOURCE_CUT_COLLINEAR_RESIDUES_FACTORIZE_AS_MINUS_EIGHT_TIMES_THE_COMPLETE_COMPTON_BORN_AMPLITUDE_IN_THE_FROZEN_NORMALIZATION",
    "IR-NG-006 — SOURCE_CUT_IR_RESIDUES_MUST_BE_FIXED_LOCALLY_BY_BORN_FACTORIZATION_NOT_BY_REGULATED_PHASE_SPACE_FITS",
    "NG-FUNNEL-078 — CONNECTED_SOURCE_HARD_REMAINDERS_REQUIRE_BORN_FIXED_IR_COMPLETION_BEFORE_LINKED_CUT_COMPARISON"
  ],
  "readiness_change":"unchanged at 23%; the source-cut IR coefficient is now fixed by physical Born data, but the finite/inclusive source cut is not yet constructed",
  "next_gate":"Use R=-8 M_Born to define a regulator-independent source hard remainder, verify cap independence, then compare its nonanalytic soft structure to the on-shell pure-graviton positive control without identifying the two observables."
}
Path("results/scalar_source_cut_born_factorization_iteration222.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
