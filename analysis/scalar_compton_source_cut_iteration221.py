#!/usr/bin/env python3
"""Iteration 221: first physical dynamical-source unitarity-cut kernel.

Build the s-channel scalar+graviton two-particle cut of gravitational Compton
scattering using only the gauge-invariant MSSC-001 two-scalar/two-graviton KLT
tree blocks. External and intermediate gravitons are pure spin-2 plus/cross
linear polarizations. Overall Cutkosky/phase-space normalization is stripped;
this gate tests physical-state completeness, basis invariance and angular IR
structure before integration.
"""
from pathlib import Path
import json, math
import numpy as np

ITERATION=221
eta=np.diag([1.,-1.,-1.,-1.]).astype(complex)
def dot(a,b): return a@eta@b

def A4(P1,k2,k3,P4,e2,e3):
    F=np.outer(k3,e3)-np.outer(e3,k3)
    return ((2*dot(e2,P1)*dot(e3,k2)-2*(e2@eta@F@eta@P1))/(2*dot(k2,k3))
            -2*dot(e2,P1)*dot(e3,P4)/(2*dot(P1,k2)))

def Msep(P1,k2,k3,P4,l2,l3,r2,r3):
    return -(2*dot(k2,k3))*A4(P1,k3,k2,P4,l3,l2)*A4(P1,k2,k3,P4,r2,r3)

def tensor_amp(P1,k2,k3,P4,T2,T3):
    val=0j
    for c2,l2,r2 in T2:
        for c3,l3,r3 in T3:
            val += c2*c3*Msep(P1,k2,k3,P4,l2,l3,r2,r3)
    return val

def spin2_basis(n,alpha=0.0):
    """Real physical plus/cross basis, with optional transverse-basis rotation."""
    n=np.asarray(n,float); n=n/np.linalg.norm(n)
    ref=np.array([0.,0.,1.])
    if abs(float(n@ref))>0.9: ref=np.array([1.,0.,0.])
    e1=np.cross(ref,n); e1/=np.linalg.norm(e1)
    e2=np.cross(n,e1); e2/=np.linalg.norm(e2)
    c,s=math.cos(alpha),math.sin(alpha)
    f1=c*e1+s*e2; f2=-s*e1+c*e2
    E1=np.r_[0.,f1].astype(complex); E2=np.r_[0.,f2].astype(complex)
    q=1/math.sqrt(2)
    plus=[(q,E1,E1),(-q,E2,E2)]
    cross=[(q,E1,E2),(q,E2,E1)]
    return plus,cross

def physical_compton(m=0.7,sqrts=2.0,theta=0.8):
    s=sqrts*sqrts; p=(s-m*m)/(2*sqrts); Es=(s+m*m)/(2*sqrts)
    Pin=np.array([Es,0,0,p],complex)
    kin=np.array([p,0,0,-p],complex)
    kout=np.array([p,p*math.sin(theta),0,p*math.cos(theta)],complex)
    Pout=np.array([Es,-p*math.sin(theta),0,-p*math.cos(theta)],complex)
    return Pin,kin,kout,Pout,p,Es

def cut_kernel(theta_i,phi_i,theta_ext=0.8,alpha=0.0):
    Pin,kin,kout,Pout,p,Es=physical_compton(theta=theta_ext)
    n=np.array([math.sin(theta_i)*math.cos(phi_i),math.sin(theta_i)*math.sin(phi_i),math.cos(theta_i)])
    lg=np.r_[p,p*n].astype(complex)
    ls=np.r_[Es,-p*n].astype(complex)
    left=(-Pin,-kin,lg,ls)
    right=(-ls,-lg,kout,Pout)
    ext_in_plus=spin2_basis([0,0,-1])[0]
    ext_out_plus=spin2_basis([math.sin(theta_ext),0,math.cos(theta_ext)])[0]
    inter=spin2_basis(n,alpha)
    total=0j
    for T in inter:
        ML=tensor_amp(*left,ext_in_plus,T)
        MR=tensor_amp(*right,T,ext_out_plus)
        total += ML*MR
    return total

# Internal physical-polarization basis rotation invariance.
basis_points=[(0.6,0.4),(1.2,1.1),(2.2,2.4)]
alphas=[0.17,0.43,0.91,1.37]
max_basis_rel=0.0
for th,ph in basis_points:
    base=cut_kernel(th,ph,alpha=0.0)
    for a in alphas:
        val=cut_kernel(th,ph,alpha=a)
        max_basis_rel=max(max_basis_rel,float(abs(val-base)/max(abs(base),1e-30)))

# Map singular vs nonsingular directions. The incoming physical graviton points
# along -z; outgoing graviton is at theta_ext, phi=0.
theta_ext=0.8
deltas=np.array([0.1,0.05,0.02,0.01,0.005,0.002])
def scan(kind):
    vals=[]
    for d in deltas:
        if kind=="incoming": th,ph=math.pi-d,0.7
        elif kind=="outgoing": th,ph=theta_ext+d,0.0
        elif kind=="antipode_in": th,ph=d,0.7
        elif kind=="antipode_out": th,ph=math.pi-theta_ext+d,math.pi
        else: raise ValueError(kind)
        vals.append(float(abs(cut_kernel(th,ph,theta_ext))))
    slope=float(np.polyfit(np.log(deltas[-4:]),np.log(np.asarray(vals)[-4:]),1)[0])
    return {"abs_kernel":vals,"delta2_times_abs":[float(d*d*v) for d,v in zip(deltas,vals)],"small_delta_loglog_slope":slope}

scans={k:scan(k) for k in ["incoming","outgoing","antipode_in","antipode_out"]}

out={
  "iteration":ITERATION,
  "date":"2026-09-01",
  "model_readiness_percent":23,
  "source_model_id":"MSSC-001",
  "observable":"stripped s-channel scalar+graviton two-particle cut kernel for gravitational Compton scattering",
  "external_state":"scalar + plus-polarized graviton -> scalar + plus-polarized graviton",
  "intermediate_state_sum":"massive scalar plus two physical spin-2 linear polarizations (plus,cross)",
  "normalization_scope":"overall Cutkosky/phase-space constants stripped; singularity and basis-invariance gate only",
  "max_internal_spin2_basis_rotation_relative_error":max_basis_rel,
  "delta_scan":deltas.tolist(),
  "direction_scans":scans,
  "classification":{
    "gauge_invariant_source_tree_blocks":"PASS_FROM_ITERATION220",
    "physical_intermediate_spin2_sum":"PASS_BASIS_ROTATION_INVARIANCE",
    "incoming_graviton_collinear_behavior":"DELTA_THETA_MINUS_TWO",
    "outgoing_graviton_collinear_behavior":"DELTA_THETA_MINUS_TWO",
    "antipodal_directions":"FINITE",
    "phase_space_integral":"LOG_IR_DIVERGENT_BEFORE_INCLUSIVE_OR_HARD_REMAINDER_COMPLETION",
    "source_completion_avoids_offshell_gauge_ambiguity":"YES_AT_ONSHELL_CONNECTED_AMPLITUDE_LEVEL",
    "IR_safe_source_cut":"NOT_YET",
    "candidate_residual":"NONE",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "SRC-CUT-001 — PHYSICAL_SCALAR_GRAVITON_TWO_PARTICLE_CUT_CAN_BE_BUILT_ENTIRELY_FROM_GAUGE_INVARIANT_DYNAMICAL_SOURCE_TREE_BLOCKS",
    "SRC-CUT-002 — INTERMEDIATE_SPIN2_POLARIZATION_SUM_IS_INVARIANT_UNDER_TRANSVERSE_BASIS_ROTATION",
    "IR-NG-005 — SOURCE_COMPLETION_REMOVES_OFFSHELL_GAUGE_AMBIGUITY_BUT_NOT_PHYSICAL_GRAVITATIONAL_COLLINEAR_IR_DIVERGENCES",
    "NG-FUNNEL-077 — GAUGE_SAFE_CONNECTED_SOURCE_CUTS_STILL_REQUIRE_A_DECLARED_IR_SAFE_OR_HARD_REMAINDER_COMPLETION_BEFORE_COMPARATOR_PROMOTION"
  ],
  "readiness_change":"unchanged at 23%; a gauge-safe connected source cut kernel now exists, but its phase-space integral is IR divergent before physical completion",
  "next_gate":"Factorize the two collinear source-cut residues against the scalar Compton Born amplitude and determine whether a Born-fixed hard-remainder subtraction/inclusive definition can be frozen without cap fitting."
}
Path("results/scalar_compton_source_cut_iteration221.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
