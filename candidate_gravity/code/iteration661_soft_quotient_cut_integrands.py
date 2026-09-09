#!/usr/bin/env python3
"""Iter661: quotient-safe +TT numerator-weighted fixed-epsilon D_s integrands."""
from __future__ import annotations
import json, math, runpy
from pathlib import Path
import numpy as np
I=661; ROOT=Path(__file__).resolve().parents[2]; m=.7; m2=m*m; thr=4*m2
SAMPLES=(2.25,3.0,4.0); EPS=(.05,.02); NMU=48; NPHI=64
P=runpy.run_path(str(ROOT/'analysis'/'source_full_cubic_routed_assembly_iteration594.py'))
K1,K2,mdot=P['K1'],P['K2'],P['mdot']
H=np.zeros((4,4)); H[1,1]=1/math.sqrt(2); H[2,2]=-1/math.sqrt(2)

def qs(s,e):
 q1=np.array([math.sqrt(s),0.,0.,0.]); q3=np.array([e,0.,0.,e]); return q1,-q1-q3,q3

def boost(v,p):
 v=np.asarray(v); p=np.asarray(p); v2=float(v@v)
 if v2<1e-30:return p.copy()
 g=1/math.sqrt(1-v2); vp=float(v@p[1:]); o=np.empty(4); o[0]=g*(p[0]+vp); o[1:]=p[1:]+(((g-1)*vp/v2)+g*p[0])*v; return o

def pair(Q,n):
 Q=np.asarray(Q); z=float(mdot(Q));
 if z<=thr: raise ValueError(('below threshold',z))
 sig=1 if Q[0]>=0 else -1; F=sig*Q; M=math.sqrt(z); E=M/2; k=math.sqrt(E*E-m2)
 a=boost(F[1:]/F[0],np.array([-E,*(k*n)])); b=boost(F[1:]/F[0],np.array([E,*(k*n)]))
 return (a,b) if sig>0 else (b,a)

def avg(fn):
 mu,w=np.polynomial.legendre.leggauss(NMU); acc=None
 for x,wx in zip(mu,w):
  r=math.sqrt(max(0,1-x*x))
  for j in range(NPHI):
   ph=2*math.pi*(j+.5)/NPHI; n=np.array([r*math.cos(ph),r*math.sin(ph),x]); y=np.asarray(fn(n),complex)
   if acc is None: acc=np.zeros_like(y)
   acc+=wx*y/NPHI
 return acc/2

def bubble(Q,hs,hl,hr):
 z=float(mdot(Q)); beta=math.sqrt(1-thr/z); phase=beta/(16*math.pi**2)
 def f(n):
  a,b=pair(Q,n); return [K1(hs,b,a)*K2(hl,hr,a,b),max(abs(m2-mdot(a)),abs(m2-mdot(b)))]
 a=avg(f); return complex(phase*a[0]),float(abs(a[1])),beta

def triangle(q1,q2,q3,ori,lab):
 Q={'q1':q1,'q2':q2}[lab]; z=float(mdot(Q)); beta=math.sqrt(1-thr/z); phase=beta/(16*math.pi**2)
 stat={'min':1e300,'sign':set(),'shell':0.}
 def f(n):
  a,b=pair(Q,n)
  if ori=='A' and lab=='q1': r1,r2=a,b; r0=r1-q3; u=r0
  elif ori=='A' and lab=='q2': r2,r0=a,b; r1=r0+q3; u=r1
  elif ori=='B' and lab=='q2': r1,r2=a,b; r0=r1-q3; u=r0
  else: r2,r0=a,b; r1=r0+q3; u=r1
  den=m2-mdot(u); stat['min']=min(stat['min'],abs(float(den))); stat['shell']=max(stat['shell'],abs(m2-mdot(a)),abs(m2-mdot(b)))
  if den>1e-12: stat['sign'].add(1)
  elif den<-1e-12: stat['sign'].add(-1)
  return [K1(H,r1,r0)*K1(H,r2,r1)*K1(H,r0,r2)/den]
 a=avg(f); return complex(phase*a[0]),stat,beta

def cj(z): return {'re':float(np.real(z)),'im':float(np.imag(z))}

def main():
 req=[ROOT/'candidate_gravity/results/iteration655_soft_tcut_kinematic_contract.json',ROOT/'candidate_gravity/results/iteration658_plus_tt_null_quotient_invariance.json',ROOT/'candidate_gravity/results/iteration659_soft_gamma3_cut_topology_census.json',ROOT/'candidate_gravity/results/iteration660_soft_family_routing_threshold_landau.json']
 fail=[f'missing authority file {p.relative_to(ROOT)}' for p in req if not p.exists()]; blocked=[]; rows=[]
 if not fail:
  for p in req:
   d=json.loads(p.read_text())
   if d.get('scientific_gate_pass') is not True: fail.append(f'authority not PASS: {p.name}')
 if not fail:
  for s in SAMPLES:
   for e in EPS:
    q1,q2,q3=qs(s,e); q2sq=float(mdot(q2))
    if q2sq<=thr: fail.append(f'grid below q2 threshold {s}/{e}'); continue
    b1,e1,be1=bubble(q1,H,H,H); b2,e2,be2=bubble(q2,H,H,H); tr={}
    for o in ('A','B'):
     for lab in ('q1','q2'):
      v,st,be=triangle(q1,q2,q3,o,lab); tr[o+'_'+lab]={'density':cj(v),'max_cut_shell_error':st['shell'],'min_abs_uncut_denominator':st['min'],'uncut_denominator_signs':sorted(st['sign']),'beta':be}
      if st['shell']>2e-11: fail.append(f'triangle shell drift {o}/{lab}/{s}/{e}')
      if len(st['sign'])>1 or st['min']<1e-9: blocked.append(f'uncut triangle pole prescription required {o}/{lab}/s={s}/eps={e}')
    if max(e1,e2)>2e-11: fail.append(f'bubble shell drift {s}/{e}')
    rows.append({'s':s,'epsilon':e,'q2_squared':q2sq,'bubble_q1_density':cj(b1),'bubble_q2_density':cj(b2),'bubble_q1_beta':be1,'bubble_q2_beta':be2,'triangles':tr})
 gate=not fail and not blocked
 cls='PASS_ITER661_QUOTIENT_SAFE_PLUS_TT_NUMERATOR_WEIGHTED_DS_INTEGRANDS_FIXED_EPS__NON_RESIDUAL' if gate else ('BLOCKED_ITER661_TRIANGLE_UNCUT_POLE_CAUSAL_PRESCRIPTION_REQUIRED__BUBBLE_INTEGRANDS_RETAINED__NON_RESIDUAL' if not fail else 'FAIL_ITER661_SOFT_CUT_INTEGRAND_CONSTRUCTION')
 out={'iteration':I,'date':'2026-09-09','MODEL_READINESS':'24%','classification':cls,'scientific_gate_pass':gate,'failures':fail,'blocked':sorted(set(blocked)),
 'contract':{'soft_kinematics':'MSSC001-CLOSED-SK-SOFT-TCUT-KIN-V1','measurement':'Iter658 quotient-safe plus-TT; same frozen e_plus on all external legs','vertices':'exact Iter594 K1/K2','parent_normalization':'Iter653 common i/2 retained symbolically; reported values are cut-measure numerator densities before the common i/2','topology_signs':'Iter659 K1K2=-1, K1^3=+1','Ds':'Disc_s/(2*pi*i) at fixed epsilon>0 before epsilon->0+','two_body_cut_measure':'beta/(16*pi^2) times sphere average'},
 'support':{'q1_bubble':'ordinary cut','q2_bubble':'ordinary cut','q3_bubble':'NO_MASSIVE_ORDINARY_CUT_TOPOLOGY_RETAINED_NOT_ZERO_FILLED','triangles':'q1 and q2 hard two-line branches retained'},'samples':rows,'candidate_values_used':False,'zero_fill':False,'source_born_subtraction':'NOT_PERFORMED','native_soft_Tcut':'NOT_YET_FORMED','ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','next_gate':('Bind same-parent retarded/CTP prescription for the encountered uncut triangle denominator, then consume retained integrands without fitting.' if blocked else 'Extract the prescribed epsilon-leading coefficient away from thresholds, then build matched W[D_s K2] before subtraction.')}
 p=ROOT/'candidate_gravity/results/iteration661_soft_quotient_cut_integrands.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
 if fail: raise SystemExit(2)
if __name__=='__main__':main()
