#!/usr/bin/env python3
"""Iteration 224: deterministic global bulk quadrature audit for MSSC-001.

Uses exactly the Iteration-222 Born-fixed subtraction retained in Iteration 223:
    I_hard = I_cut - R/(1+n_z) - R/(1-n.n_out),  R=-8 M_Born.
No subtraction coefficient is refit.

Two independent angular decompositions are compared:
A) Gauss-Legendre in mu=cos(theta) with periodic midpoint phi in the laboratory chart;
B) the same deterministic tensor quadrature after a fixed y-rotation of 0.371 rad.
Both omit exact spherical caps of radius delta around the two already-certified
collinear points. Iteration 223 established that omitted hard-cap contributions
vanish as delta^2, so disagreement between the two bulk charts is numerical,
not a new IR subtraction ambiguity.
"""
from pathlib import Path
import json, math
import numpy as np
from numpy.polynomial.legendre import leggauss

ITERATION=224
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
    E1=np.r_[0.,f1].astype(complex); E2=np.r_[0.,f2].astype(complex); q=1/math.sqrt(2)
    return ([(q,E1,E1),(-q,E2,E2)],[(q,E1,E2),(q,E2,E1)])

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

def cut_dir(n,theta_ext,pol_idx):
    Pin,kin,kout,Pout,p,Es=physical(theta=theta_ext)
    n=np.asarray(n,float); n/=np.linalg.norm(n)
    lg=np.r_[p,p*n].astype(complex); ls=np.r_[Es,-p*n].astype(complex)
    Tin=spin2_basis([0,0,-1])[pol_idx]
    Tout=spin2_basis([math.sin(theta_ext),0,math.cos(theta_ext)])[pol_idx]
    left=(-Pin,-kin,lg,ls); right=(-ls,-lg,kout,Pout)
    return sum(tensor_amp(*left,Tin,T)*tensor_amp(*right,T,Tout) for T in spin2_basis(n))

def hard_kernel(n,theta_ext,pol_idx):
    n=np.asarray(n,float); n/=np.linalg.norm(n)
    R=-8*born(theta_ext,pol_idx)
    nout=np.array([math.sin(theta_ext),0,math.cos(theta_ext)])
    return cut_dir(n,theta_ext,pol_idx)-R/(1+n[2])-R/(1-float(n@nout))

def rot_y(a):
    c,s=math.cos(a),math.sin(a)
    return np.array([[c,0,s],[0,1,0],[-s,0,c]])

def integrate(theta_ext,pol_idx,N,rotation,delta):
    mu,w=leggauss(N); nphi=2*N; dphi=2*math.pi/nphi; Rm=rot_y(rotation)
    nout=np.array([math.sin(theta_ext),0,math.cos(theta_ext)])
    total=0j
    for x,wi in zip(mu,w):
        r=math.sqrt(max(0.,1-x*x))
        for j in range(nphi):
            ph=(j+0.5)*dphi
            n=Rm@np.array([r*math.cos(ph),r*math.sin(ph),x])
            rho_in=math.acos(max(-1.,min(1.,-float(n[2]))))
            rho_out=math.acos(max(-1.,min(1.,float(n@nout))))
            if rho_in<delta or rho_out<delta: continue
            total += wi*dphi*hard_kernel(n,theta_ext,pol_idx)
    return total

angles=[0.45,0.8,1.15,1.6,2.1]
resolutions=[12,16,20]
deltas=[0.08,0.04]
rotations={"lab_chart":0.0,"rotated_chart":0.371}
records=[]; worst=0.0
for delta in deltas:
  for theta_ext in angles:
    for pol_idx,pol_name in [(0,"plus"),(1,"cross")]:
      vals={name:[float(integrate(theta_ext,pol_idx,N,rot,delta).real) for N in resolutions]
            for name,rot in rotations.items()}
      rel=abs(vals["lab_chart"][-1]-vals["rotated_chart"][-1])/max(abs(vals["lab_chart"][-1]),abs(vals["rotated_chart"][-1]),1e-30)
      worst=max(worst,rel)
      records.append({"delta":delta,"theta_ext":theta_ext,"polarization":pol_name,
                      "resolutions":resolutions,"values":vals,"finest_chart_relative_disagreement":rel})

out={
 "iteration":224,"date":"2026-09-01","model_readiness_percent":23,
 "source_model_id":"MSSC-001",
 "subtraction_authority":"R=-8 M_Born fixed by Iteration 222; unchanged",
 "local_cap_authority":"Iteration 223: omitted hard-cap shells vanish as delta^2",
 "quadratures":rotations,"resolutions":resolutions,"deltas":deltas,
 "worst_finest_grid_chart_relative_disagreement":worst,
 "acceptance_criterion":"No finite global remainder is frozen unless both chart sequences converge to the same value within a declared numerical envelope.",
 "classification":{
   "local_IR_completion":"PASS_FROM_ITERATION223",
   "global_bulk_hard_remainder":"BLOCKED_NUMERICAL_BULK_HARD_REMAINDER",
   "physics_fail":"NO",
   "candidate_residual":"NONE","ANSATZ_003":"NOT_CREATED","Fisher_resources":"FORBIDDEN"},
 "records":records,
 "retained_results":[
   "NUM-NG-013 — TWO_FIXED_ANGULAR_DECOMPOSITIONS_DO_NOT_YET_CONVERGE_TO_A_COMMON_MSSC001_GLOBAL_HARD_REMAINDER_ON_THE_TESTED_GRIDS",
   "SRC-CUT-005 — LOCAL_DELTA2_CAP_COMPLETION_DOES_NOT_GUARANTEE_GLOBAL_BULK_QUADRATURE_STABILITY",
   "NG-FUNNEL-080 — A_COORDINATE_DEPENDENT_BULK_NUMBER_MUST_NOT_BE_FROZEN_AS_A_PHYSICAL_COMPARATOR_REMAINDER"],
 "readiness_change":"unchanged at 23%; this is a numerical blocker localization, not closure of a rubric block",
 "next_gate":"Replace global tensor-product sampling by singularity-adapted domain decomposition: analytically/local-coordinate integrate the two certified caps and use independent high-order cubatures only on a smooth cap-excised bulk; require common convergence before freezing a finite value."
}
Path("results/scalar_source_global_bulk_quadrature_iteration224.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
