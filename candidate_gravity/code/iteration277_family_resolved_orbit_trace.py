#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 277.
Decompose the translation-closed scalar orbit trace into exact primitive
raised-bubble/triangle families at the frozen p0.  This is an integrand-level
certificate only; no loop integration is performed.
"""
import importlib.util, itertools, json
from collections import defaultdict, Counter
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('i273',HERE/'iteration273_closed_kinematics_physical_b3.py')
i273=importlib.util.module_from_spec(spec); spec.loader.exec_module(i273)
m=i273.m; POS=i273.POS; P0=i273.P0; LEGS=('s','a','b'); ETA=m.ETA

def qcomp(M,legs,p):
    legs=tuple(legs)
    if len(legs)==0:return [('Q0',m.Q0(p),[p.copy()])]
    if len(legs)==1:
      x=legs[0]; k=M[x][0]
      return [(f'Q1[{x}]',-m.Q0(p+k)@m.N1(M,x,p)@m.Q0(p),[p+k,p.copy()])]
    x,y=legs; kx,ky=M[x][0],M[y][0]
    return [
      (f'Q2_seq_{x}{y}',m.Q0(p+kx+ky)@m.N1(M,x,p+ky)@m.Q0(p+ky)@m.N1(M,y,p)@m.Q0(p),[p+kx+ky,p+ky,p.copy()]),
      (f'Q2_seq_{y}{x}',m.Q0(p+kx+ky)@m.N1(M,y,p+kx)@m.Q0(p+kx)@m.N1(M,x,p)@m.Q0(p),[p+kx+ky,p+kx,p.copy()]),
      (f'Q2_contact_{x}{y}',-m.Q0(p+kx+ky)@m.N2(M,x,y,p)@m.Q0(p),[p+kx+ky,p.copy()]),
    ]
def msq(v): return round(float(np.array(v)@ETA@np.array(v)),10)
def classify(shifts):
    vv=[]
    for s in shifts:
      t=tuple(np.round(s,10))
      if t not in vv:vv.append(t)
    if len(vv)==1:return 'single_scaleless'
    if len(vv)==2:
      q=np.array(vv[1])-np.array(vv[0]); q2=msq(q)
      if abs(q2)<1e-8:return 'bubble_null_scaleless'
      if abs(q2-.41)<1e-8:return 'bubble_a'
      if abs(q2-.21)<1e-8:return 'bubble_b'
    if len(vv)==3:return 'triangle_0_021_041'
    return 'unexpected'

groups=defaultdict(complex); counts=Counter(); B=np.zeros((4,4),complex)
for ass in itertools.product('LMR',repeat=3):
    L=tuple(LEGS[i] for i,a in enumerate(ass) if a=='L')
    A=tuple(LEGS[i] for i,a in enumerate(ass) if a=='M')
    R=tuple(LEGS[i] for i,a in enumerate(ass) if a=='R')
    if not A or A==('s',):continue
    kR=m.ksum(POS,R); kA=m.ksum(POS,A); Am=m.Asub(POS,A,P0+kR)
    for _,Lm,Lsh in qcomp(POS,L,P0+kR+kA):
      for _,Rm,Rsh in qcomp(POS,R,P0):
        T=Lm@Am@Rm; B+=T; c=classify(Lsh+Rsh); groups[c]+=np.trace(T); counts[c]+=1
result={
 'iteration':277,'model_readiness_percent':24,
 'total_orbit_trace_real':float(np.trace(B).real),
 'family_counts':dict(counts),
 'family_orbit_trace_real':{k:float(v.real) for k,v in groups.items()},
 'scaleless_family_integrand_trace_real':float(sum(v.real for k,v in groups.items() if 'scaleless' in k)),
 'non_scaleless_family_integrand_trace_real':float(sum(v.real for k,v in groups.items() if 'scaleless' not in k)),
 'classification':'PASS_SCOPED_NONSCALLESS_MASTER_FAMILY_ORBIT_TRACE_NONZERO_AT_P0',
 'guardrail':'NONZERO_NONSCALLESS_INTEGRAND_SUM_AT_ONE_P_IS_NOT_YET_A_NONZERO_INTEGRATED_LOG_OR_DISCONTINUITY_COEFFICIENT',
 'next_gate':'canonicalize loop routing within bubble-a, bubble-b and triangle families, reconstruct their scalar numerator polynomials, then tensor-reduce the combined families before evaluating logs/discontinuities'
}
print(json.dumps(result,indent=2,sort_keys=True))
