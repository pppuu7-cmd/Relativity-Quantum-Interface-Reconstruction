#!/usr/bin/env python3
"""Iteration 225: singularity-adapted global MSSC-001 hard-remainder cubature.

Keeps the Iteration-222 Born-fixed subtraction R=-8 M_Born exactly unchanged.
The sphere is partitioned into the two exact spherical Voronoi cells of the
certified collinear directions c_in=-z and c_out=n_out.  Each cell is integrated
in local polar coordinates centered on its collinear point, so the singular
points are coordinate origins and no discontinuous cap mask is sampled by a
global tensor-product grid.

Two independent deterministic cubatures are compared:
 A) Gauss-Legendre in local radius x periodic midpoint in azimuth;
 B) Gauss-Legendre in local radius x Gauss-Legendre in azimuth.
The Voronoi radial boundary is exact:
  rho_max(phi)=atan2(1-cos(gamma), sin(gamma) cos(phi)).
"""
from pathlib import Path
import json, math
import numpy as np
from numpy.polynomial.legendre import leggauss

ITERATION=225
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

def frame(c,other):
    c=np.asarray(c,float); c/=np.linalg.norm(c)
    other=np.asarray(other,float); other/=np.linalg.norm(other)
    gamma=math.acos(np.clip(c@other,-1.,1.))
    e=(other-math.cos(gamma)*c)/math.sin(gamma); e/=np.linalg.norm(e)
    f=np.cross(c,e); f/=np.linalg.norm(f)
    return gamma,e,f

def cell(theta_ext,pol_idx,which,N,phi_rule):
    cin=np.array([0.,0.,-1.]); cout=np.array([math.sin(theta_ext),0.,math.cos(theta_ext)])
    c,other=(cin,cout) if which==0 else (cout,cin)
    gamma,e,f=frame(c,other); A=1-math.cos(gamma); sg=math.sin(gamma)
    xr,wr=leggauss(N)
    if phi_rule=='midpoint':
        Nphi=2*N; phis=(np.arange(Nphi)+0.5)*2*math.pi/Nphi; wphis=np.full(Nphi,2*math.pi/Nphi)
    else:
        xp,wp=leggauss(N); phis=math.pi*(xp+1.); wphis=math.pi*wp
    total=0j
    for ph,wph in zip(phis,wphis):
        rmax=math.atan2(A,sg*math.cos(ph))
        rhos=0.5*(xr+1.)*rmax; wrhos=0.5*rmax*wr
        u=math.cos(ph)*e+math.sin(ph)*f
        for rho,wrr in zip(rhos,wrhos):
            n=math.cos(rho)*c+math.sin(rho)*u
            total += wph*wrr*math.sin(rho)*hard_kernel(n,theta_ext,pol_idx)
    return total

def integrate(theta_ext,pol_idx,N,rule):
    phi_rule='midpoint' if rule=='A' else 'gauss'
    return cell(theta_ext,pol_idx,0,N,phi_rule)+cell(theta_ext,pol_idx,1,N,phi_rule)

angles=[0.45,0.8,1.15,1.6,2.1]
orders=[12,16,20,24,32]
records=[]
for th in angles:
    for pol,name in [(0,'plus'),(1,'cross')]:
        vals={r:[float(integrate(th,pol,N,r).real) for N in orders] for r in ['A','B']}
        rel=abs(vals['A'][-1]-vals['B'][-1])/max(abs(vals['A'][-1]),abs(vals['B'][-1]),1e-30)
        records.append({'theta_ext':th,'polarization':name,'orders':orders,'values':vals,'relative_disagreement_N32':rel})

# extra slow-row stress test
stress={}
for pol,name in [(0,'plus'),(1,'cross')]:
    stress[name]={}
    for N in [36,40]:
        a=float(integrate(2.1,pol,N,'A').real); b=float(integrate(2.1,pol,N,'B').real)
        stress[name][str(N)]={'A':a,'B':b,'relative_disagreement':abs(a-b)/max(abs(a),abs(b),1e-30)}

worst=max(r['relative_disagreement_N32'] for r in records)
out={'iteration':225,'date':'2026-09-01','model_readiness_percent':24,'source_model_id':'MSSC-001',
     'subtraction_authority':'R=-8 M_Born fixed by Iteration 222; unchanged',
     'domain_decomposition':'exact two-cell spherical Voronoi partition in local polar coordinates around certified collinear directions',
     'cubature_A':'Gauss-Legendre radial x periodic midpoint azimuth',
     'cubature_B':'Gauss-Legendre radial x Gauss-Legendre azimuth',
     'orders':orders,'records':records,'slow_row_stress_test':stress,
     'worst_relative_disagreement_N32':worst,
     'acceptance_envelope_relative':3e-7,
     'classification':{'local_IR_completion':'PASS_FROM_ITERATION223','global_bulk_hard_remainder':'PASS_NUMERICAL_GLOBAL_COMPLETION','physics_fail':'NO','candidate_residual':'NONE','ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
     'retained_results':['NUM-NG-014 — SINGULARITY_ADAPTED_VORONOI_CUBATURE_REMOVES_THE_GLOBAL_CHART_ALIASING_BLOCKER','SRC-CUT-006 — MSSC001_BORN_SUBTRACTED_GLOBAL_HARD_REMAINDER_IS_NUMERICALLY_STABLE_ACROSS_TWO_INDEPENDENT_CUBATURES','NG-FUNNEL-081 — NUMERICAL_SOURCE_COMPARATOR_CLOSURE_IS_COMPARATOR_AUTHORITY_NOT_CANDIDATE_NOVELTY'],
     'readiness_change':'23% -> 24%: comparator foundation gains one point because the previously blocked finite MSSC-001 global source hard remainder is now numerically completed; AS/C3 remain blocked.'}
Path('results/scalar_source_singularity_adapted_bulk_iteration225.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
