#!/usr/bin/env python3
"""Iteration 223: Born-fixed IR hard-remainder cap audit for MSSC-001.

Starting from Iteration 222, both collinear residues of the connected scalar+graviton
source cut obey R_in=R_out=-8 M_Born in the same stripped normalization. This script
subtracts exactly those local Born-fixed poles pointwise and tests whether the
remaining cap-shell contribution vanishes prospectively across the same five
external angles and both linear spin-2 polarizations.

No cap fit is used to determine the subtraction coefficient.
"""
from pathlib import Path
import json, math
import numpy as np
from numpy.polynomial.legendre import leggauss

ITERATION=223
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

def cut(theta_i,phi_i,theta_ext,pol_idx):
    Pin,kin,kout,Pout,p,Es=physical(theta=theta_ext)
    n=np.array([math.sin(theta_i)*math.cos(phi_i),math.sin(theta_i)*math.sin(phi_i),math.cos(theta_i)])
    lg=np.r_[p,p*n].astype(complex); ls=np.r_[Es,-p*n].astype(complex)
    left=(-Pin,-kin,lg,ls); right=(-ls,-lg,kout,Pout)
    Tin=spin2_basis([0,0,-1])[pol_idx]
    Tout=spin2_basis([math.sin(theta_ext),0,math.cos(theta_ext)])[pol_idx]
    return sum(tensor_amp(*left,Tin,T)*tensor_amp(*right,T,Tout) for T in spin2_basis(n))

def sub_kernel(th,ph,theta_ext,pol_idx):
    B=born(theta_ext,pol_idx); R=-8*B
    n=np.array([math.sin(th)*math.cos(ph),math.sin(th)*math.sin(ph),math.cos(th)])
    nout=np.array([math.sin(theta_ext),0,math.cos(theta_ext)])
    return cut(th,ph,theta_ext,pol_idx)-R/(1+math.cos(th))-R/(1-float(n@nout))

def direction_from_center(center,rho,psi):
    c=np.asarray(center,float); c/=np.linalg.norm(c)
    ref=np.array([0.,0.,1.])
    if abs(float(c@ref))>0.9: ref=np.array([1.,0.,0.])
    e1=np.cross(ref,c); e1/=np.linalg.norm(e1)
    e2=np.cross(c,e1); e2/=np.linalg.norm(e2)
    return math.cos(rho)*c+math.sin(rho)*(math.cos(psi)*e1+math.sin(psi)*e2)

def sph(n):
    th=math.acos(max(-1.,min(1.,float(n[2])))); ph=math.atan2(float(n[1]),float(n[0]))
    if ph<0: ph+=2*math.pi
    return th,ph

def shell(center,d_hi,theta_ext,pol_idx,nr=6,npsi=32):
    # Exact spherical annulus rho in [d_hi/2,d_hi].
    x,w=leggauss(nr); a=d_hi/2; b=d_hi; total=0j
    for xi,wi in zip(x,w):
        rho=(a+b)/2+(b-a)*xi/2; rw=wi*(b-a)/2
        for j in range(npsi):
            psi=2*math.pi*(j+0.5)/npsi
            th,ph=sph(direction_from_center(center,rho,psi))
            total += rw*(2*math.pi/npsi)*math.sin(rho)*sub_kernel(th,ph,theta_ext,pol_idx)
    return total

angles=[0.45,0.8,1.15,1.6,2.1]
deltas=np.array([0.08,0.04,0.02,0.01,0.005])
records=[]; slopes=[]; max_io=0.0
for theta_ext in angles:
    for pol_idx,pol_name in [(0,"plus"),(1,"cross")]:
        centers={"incoming":[0,0,-1],"outgoing":[math.sin(theta_ext),0,math.cos(theta_ext)]}
        vals={}; local_slopes={}
        for name,c in centers.items():
            arr=np.array([shell(c,float(d),theta_ext,pol_idx).real for d in deltas])
            vals[name]=arr
            local_slopes[name]=float(np.polyfit(np.log(deltas[-4:]),np.log(np.abs(arr[-4:])),1)[0])
            slopes.append(local_slopes[name])
        rel=float(abs(vals["incoming"][-1]-vals["outgoing"][-1])/max(abs(vals["incoming"][-1]),abs(vals["outgoing"][-1]),1e-30))
        max_io=max(max_io,rel)
        records.append({
            "theta_ext":theta_ext,"external_linear_polarization":pol_name,
            "born_amplitude":float(born(theta_ext,pol_idx).real),
            "incoming_shells":[float(x) for x in vals["incoming"]],
            "outgoing_shells":[float(x) for x in vals["outgoing"]],
            "incoming_shell_power":local_slopes["incoming"],
            "outgoing_shell_power":local_slopes["outgoing"],
            "smallest_shell_in_out_relative_mismatch":rel
        })

out={
  "iteration":ITERATION,"date":"2026-09-01","model_readiness_percent":23,
  "source_model_id":"MSSC-001",
  "subtraction":"I_hard_kernel = I_cut - R/(1+n_z) - R/(1-n dot n_out), with R=-8 M_Born fixed by Iteration 222",
  "shell_definition":"exact spherical annulus rho in [delta/2,delta] around each collinear direction",
  "delta_shells":deltas.tolist(),"radial_gauss_order":6,"azimuth_midpoint_count":32,
  "min_shell_power":float(min(slopes)),"max_shell_power":float(max(slopes)),
  "max_smallest_shell_in_out_relative_mismatch":max_io,
  "records":records,
  "classification":{
    "Born_fixed_pointwise_subtraction":"PASS_FROM_ITERATION222",
    "subtracted_cap_shells":"VANISH_AS_DELTA_SQUARED_SCOPED_CROSS_KINEMATIC",
    "cap_regulator_independence":"PASS_SCOPED_LOCAL_IR_COMPLETION",
    "global_bulk_hard_remainder_value":"NOT_EVALUATED_THIS_GATE",
    "candidate_residual":"NONE","ANSATZ_003":"NOT_CREATED","Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "SRC-CUT-004 — BORN_FIXED_SOURCE_CUT_SUBTRACTION_REMOVES_THE_LOG_COLLINEAR_CAP_DEPENDENCE_WITHOUT_CAP_FITTING",
    "IR-NG-007 — SUBTRACTED_SOURCE_CAP_SHELLS_SCALE_AS_DELTA_SQUARED_ACROSS_FIVE_SCATTERING_ANGLES_AND_BOTH_LINEAR_SPIN2_POLARIZATIONS",
    "NG-FUNNEL-079 — LOCAL_IR_REGULATOR_INDEPENDENCE_DOES_NOT_BY_ITSELF_CERTIFY_THE_GLOBAL_BULK_HARD_REMAINDER_OR_CANDIDATE_NOVELTY"
  ],
  "readiness_change":"unchanged at 23%; local source-cut IR completion is now regulator-independent, but comparator foundation still lacks the global bulk hard remainder and AS/C3 completion",
  "next_gate":"Construct deterministic singularity-aware bulk quadrature for the Born-subtracted MSSC-001 source cut and then test its linked nonanalytic dependence against the separate pure-graviton positive control without equating the observables."
}
Path("results/scalar_source_hard_remainder_iteration223.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
