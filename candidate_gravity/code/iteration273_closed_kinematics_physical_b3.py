#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 273 executable gate.

Re-use the exact Iteration-270 same-parent routed implementation, but impose
physical translation closure k_s+k_a+k_b=0 before evaluating B3.

This script deliberately does not assume the result is nonzero.  It reports a
nonzero, near-zero, or numerical-instability classification after step scans and
endpoint/permutation checks.
"""
import importlib.util
import itertools
import json
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
SRC=HERE/'iteration270_vd_physical_b3_nonzero.py'
spec=importlib.util.spec_from_file_location('iter270',SRC)
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

# Freeze s and a exactly as Iteration 270; close the third leg.
K_S=m.K_S.copy()
K_A=m.K_A.copy()
K_B=-(K_S+K_A)
E_S=m.E_S.copy()
E_A=m.E_A.copy()
E_B=m.tt_pol(K_B,[.8,.1,.3])
POS={'s':(K_S,E_S),'a':(K_A,E_A),'b':(K_B,E_B)}
NEG={x:(-k,e) for x,(k,e) in POS.items()}
LEGS=('s','a','b')
P0=m.P0.copy()
KT=m.ksum(POS,LEGS)


def build_B(M,p,h1=1e-4,h2=5e-4,h3=1e-3):
    B=np.zeros((4,4),complex)
    rows=[]
    for assign in itertools.product('LMR',repeat=3):
        L=tuple(LEGS[i] for i,a in enumerate(assign) if a=='L')
        Md=tuple(LEGS[i] for i,a in enumerate(assign) if a=='M')
        R=tuple(LEGS[i] for i,a in enumerate(assign) if a=='R')
        if not Md or Md==('s',):
            continue
        T=m.term(M,L,Md,R,p,h1,h2,h3)
        B+=T
        rows.append({'L':L,'A':Md,'R':R,'norm':float(np.linalg.norm(T))})
    return B,rows

B,rows=build_B(POS,P0)
Bneg,_=build_B(NEG,P0+KT)

A3=m.Asub(POS,LEGS,P0)
A3perm=max(np.max(np.abs(m.Asub(POS,p,P0)-A3)) for p in itertools.permutations(LEGS))
A1s=float(np.linalg.norm(m.Asub(POS,('s',),P0)))

stability=[]
for h2,h3 in [(1e-3,2e-3),(7e-4,1.5e-3),(5e-4,1e-3),(3e-4,8e-4)]:
    X,_=build_B(POS,P0,1e-4,h2,h3)
    stability.append({'h_A2':h2,'h_A3':h3,'B15_fro':float(np.linalg.norm(X)),'B15_max':float(np.max(np.abs(X)))})

fro=float(np.linalg.norm(B))
mx=float(np.max(np.abs(B)))
transpose=float(np.max(np.abs(B.T-Bneg)))
scan=np.array([r['B15_fro'] for r in stability])
spread=float(np.max(scan)-np.min(scan))
scale=max(float(np.max(scan)),1.0)
rel_spread=spread/scale

# Conservative classification only.  A genuinely nonzero value must dominate
# finite-difference/transpose envelopes; otherwise keep the gate unresolved.
envelope=max(transpose, spread, 1e-7)
if fro > 100.0*envelope and mx > 100.0*envelope and rel_spread < 1e-4:
    cls='PASS_SCOPED_TRANSLATION_CLOSED_NULLSOFT_B3_EXPLICIT_NONZERO'
elif fro < 10.0*envelope:
    cls='REGIME_SPECIFIC_NEAR_ZERO_OR_UNRESOLVED_ON_TRANSLATION_CLOSED_KINEMATICS'
else:
    cls='BLOCKED_NUMERICAL_STABILITY_TRANSLATION_CLOSED_B3'

result={
 'iteration':273,
 'model_readiness_percent':24,
 'translation_closed':bool(np.max(np.abs(KT))<1e-14),
 'kinematics':{'k_s':K_S.tolist(),'k_a':K_A.tolist(),'k_b':K_B.tolist(),'sum':KT.tolist()},
 'A1_soft_norm':A1s,
 'A3_permutation_residual':float(A3perm),
 'surviving_partition_count':len(rows),
 'B15_fro':fro,
 'B15_max':mx,
 'B15_endpoint_transpose_residual':transpose,
 'step_stability':stability,
 'step_scan_absolute_spread':spread,
 'step_scan_relative_spread':rel_spread,
 'numerical_envelope':envelope,
 'classification':cls,
 'candidate_residual':False,
 'guardrail':'THIS_TESTS_C5_PARENT_B3_ON_THE_MOMENTUM_CONSERVATION_SURFACE; IT_IS_NOT_YET_THE_LINKED_T_CUT_COMPARATOR',
 'next_gate':('if PASS: sample/reconstruct full p-dependent closed B3 numerator and denominator families; '
              'if unresolved: improve derivative stencil/precision before any master reduction')
}

assert result['translation_closed']
assert len(rows)==15
assert A1s < 2e-7
print(json.dumps(result,indent=2,sort_keys=True))
