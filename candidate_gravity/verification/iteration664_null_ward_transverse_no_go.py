#!/usr/bin/env python3
"""Iter664 exact linear-algebra no-go: diffeo Ward data do not determine null transverse quotient."""
from fractions import Fraction as F
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
fail=[]
for name in ['candidate_gravity/results/iteration658_plus_tt_null_quotient_invariance.json','candidate_gravity/results/iteration663_transverse_soft_ward_authority.json']:
 p=ROOT/name
 if not p.exists(): fail.append('missing:'+name)
 elif json.loads(p.read_text()).get('scientific_gate_pass') is not True: fail.append('nonpass:'+name)
pairs=[(i,j) for i in range(4) for j in range(i,4)]
q=[F(1),F(0),F(0),F(1)]
D=[[F(0) for _ in range(10)] for _ in range(4)]
for nu in range(4):
 for a,(mu,rho) in enumerate(pairs):
  if rho==nu: D[nu][a]+=q[mu]
  if mu==nu and rho!=mu: D[nu][a]+=q[rho]
def rank(A):
 A=[r[:] for r in A]; m=len(A); n=len(A[0]) if m else 0; i=j=r=0
 while i<m and j<n:
  k=next((k for k in range(i,m) if A[k][j]),None)
  if k is None: j+=1; continue
  A[i],A[k]=A[k],A[i]; p=A[i][j]; A[i]=[x/p for x in A[i]]
  for k in range(m):
   if k!=i and A[k][j]:
    c=A[k][j]; A[k]=[A[k][l]-c*A[i][l] for l in range(n)]
  r+=1; i+=1; j+=1
 return r
rD=rank(D); ker_dim=10-rD
# Exact Iter657 authority established dim(Im Lq cap Ker Dq)=3; reproduce L and D L rank relation.
qL=[F(1),0,0,F(-1)]
L=[[F(0) for _ in range(4)] for _ in range(10)]
for a,(mu,nu) in enumerate(pairs):
 for k in range(4): L[a][k]=(qL[mu] if nu==k else 0)+(qL[nu] if mu==k else 0)
DL=[[sum(D[i][a]*L[a][k] for a in range(10)) for k in range(4)] for i in range(4)]
rL=rank(L); rDL=rank(DL); overlap_dim=rL-rDL; quotient_dim=ker_dim-overlap_dim
if (rD,rL,rDL,ker_dim,overlap_dim,quotient_dim)!=(4,4,1,6,3,3): fail.append('rank tuple drift')
# Ward equation D Gamma = RHS fixes only an affine coset modulo Ker(D), hence cannot fix quotient components.
no_go=(quotient_dim>0)
if not no_go: fail.append('transverse quotient unexpectedly trivial')
out={'iteration':664,'date':'2026-09-09','MODEL_READINESS':'24%','classification':('BLOCKED_ITER664_EXACT_NULL_WARD_LINEAR_ALGEBRA_LEAVES_THREE_DIMENSIONAL_TRANSVERSE_GAUGE_QUOTIENT_UNDETERMINED__ADDITIONAL_PHYSICAL_SOFT_INPUT_REQUIRED__NON_RESIDUAL' if not fail else 'FAIL_ITER664_NULL_WARD_NO_GO_AUDIT'),'scientific_gate_pass':not fail,'failures':fail,'blocked':not fail,'checks':{'rank_Dq':rD,'dim_Ker_Dq':ker_dim,'rank_Lq':rL,'rank_DqLq':rDL,'dim_ImLq_intersect_KerDq':overlap_dim,'dim_transverse_gauge_quotient':quotient_dim},'theorem':'At null q, the diffeomorphism Ward equation D_q Gamma=RHS determines Gamma only modulo Ker(D_q). Modding pure-gauge overlap still leaves a three-dimensional physical transverse quotient. Therefore longitudinal Ward data alone cannot determine the frozen plus-TT component; an additional physical soft theorem/asymptotic or observable definition is required.','source_born_subtraction':'NOT_PERFORMED','native_soft_Tcut':'BLOCKED_ADDITIONAL_TRANSVERSE_SOFT_INPUT_REQUIRED','zero_fill':False,'candidate_values_used':False,'ANSATZ_003':'FORBIDDEN','Fisher_resources':'FORBIDDEN','exact_next_gate':'Iteration665: prospective observable redesign audit. Search committed authority for a physical transverse soft theorem/asymptotic identity. If absent, freeze a non-collinear or mixed-tensor closed-SK soft observable that avoids the Iter662 odd-spin selection zero while retaining Iter655 cut-before-soft-limit and same-parent normalization; do not invent W.'}
p=ROOT/'candidate_gravity/results/iteration664_null_ward_transverse_no_go.json'; p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n'); print(json.dumps(out,indent=2,sort_keys=True))
if fail: raise SystemExit(2)
