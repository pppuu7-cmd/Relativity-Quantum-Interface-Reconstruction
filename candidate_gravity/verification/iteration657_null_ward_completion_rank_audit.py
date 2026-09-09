#!/usr/bin/env python3
"""Iteration657 exact linear-algebra audit for the null-soft Ward completion.

No Candidate cut values are read.  We test the action-level gauge map
L_q(xi)_{mu nu}=q_mu xi_nu+q_nu xi_mu at the frozen Iter655 null direction
q proportional to n=(1,0,0,1), and the divergence D_q h=q^mu h_{mu nu}.
Overall signs/i factors do not affect the subspaces or ranks tested here.
"""
from fractions import Fraction as F
import json
from pathlib import Path

pairs=[(i,j) for i in range(4) for j in range(i,4)]
qU=[F(1),F(0),F(0),F(1)]
qL=[F(1),F(0),F(0),F(-1)]

def rank(A):
    A=[row[:] for row in A]; m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]; z=A[r][c]; A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
    return r

L=[[F(0) for _ in range(4)] for _ in range(10)]
for a,(mu,nu) in enumerate(pairs):
    for k in range(4):
        L[a][k]=(qL[mu] if nu==k else 0)+(qL[nu] if mu==k else 0)
D=[[F(0) for _ in range(10)] for _ in range(4)]
for nu in range(4):
    for a,(mu,rho) in enumerate(pairs):
        if rho==nu: D[nu][a]+=qU[mu]
        if mu==nu and rho!=mu: D[nu][a]+=qU[rho]
DL=[[sum(D[i][a]*L[a][j] for a in range(10)) for j in range(4)] for i in range(4)]

hplus=[F(0) for _ in range(10)]
hplus[pairs.index((1,1))]=F(1); hplus[pairs.index((2,2))]=F(-1)
dh=[sum(D[i][a]*hplus[a] for a in range(10)) for i in range(4)]
aug=[L[a]+[hplus[a]] for a in range(10)]
eta_x=[F(0),F(1),F(0),F(0)]
gauge_x=[sum(L[a][j]*eta_x[j] for j in range(4)) for a in range(10)]
dg=[sum(D[i][a]*gauge_x[a] for a in range(10)) for i in range(4)]

rL,rD,rDL=rank(L),rank(D),rank(DL)
intersection_dim=rL-rDL
failures=[]
checks={
 "q_squared": qU[0]**2-qU[1]**2-qU[2]**2-qU[3]**2,
 "rank_Lq": rL, "rank_Dq": rD, "rank_DqLq": rDL,
 "dim_image_Lq_intersect_kernel_Dq": intersection_dim,
 "plus_TT_transverse": all(x==0 for x in dh),
 "plus_TT_in_image_Lq": rank(aug)==rL,
 "explicit_nonzero_gauge_tensor_is_transverse": any(gauge_x) and all(x==0 for x in dg),
}
expected={"q_squared":0,"rank_Lq":4,"rank_Dq":4,"rank_DqLq":1,
          "dim_image_Lq_intersect_kernel_Dq":3,"plus_TT_transverse":True,
          "plus_TT_in_image_Lq":False,"explicit_nonzero_gauge_tensor_is_transverse":True}
for k,v in expected.items():
    if checks[k]!=v: failures.append(f"CHECK_FAILED:{k}:{checks[k]}!={v}")

classification=("BLOCKED_ITER657_NULL_WARD_COMPLETION_NONUNIQUE"
                "__IMAGE_LQ_INTERSECTS_TRANSVERSE_SUBSPACE_DIM3"
                "__AUXILIARY_COMPLEMENT_REQUIRED__NON_RESIDUAL")
result={
 "iteration":657,
 "scope":"MSSC001-CLOSED-SK-SOFT-TCUT-KIN-V1 null Ward completion rank audit",
 "checks":{k:(int(v) if isinstance(v,F) else v) for k,v in checks.items()},
 "algebraic_consequence":(
   "For null q, D_q L_q(xi)=q_lower*(q^upper.xi); hence every xi with q.xi=0 "
   "generates a nonzero pure-gauge tensor that is simultaneously transverse. "
   "The transverse/longitudinal split is therefore not canonical from q and the metric alone."),
 "explicit_two_decompositions":(
   "h_plus = L_q(0)+h_plus = L_q(eta_x)+(h_plus-L_q(eta_x)); both remainder tensors are transverse."),
 "auxiliary_vector_or_off_null_regulator_selected":False,
 "candidate_cut_values_read":False,
 "zero_fill_allowed":False,
 "classification":classification,
 "failures":failures,
 "MODEL_READINESS":"24%",
 "readiness_delta_percentage_points":0,
 "exact_next_gate":(
   "Determine whether the frozen plus-TT soft T_cut contraction is defined directly on the quotient "
   "Ker(D_q)/(Im(L_q) intersect Ker(D_q)) and is invariant under the three-dimensional null gauge overlap. "
   "If yes, derive it without choosing a complement; if no, preserve the observable as BLOCKED or prospectively version a complement before any cut inspection."),
}
out=Path("candidate_gravity/results/iteration657_null_ward_completion_rank_audit.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(1)
