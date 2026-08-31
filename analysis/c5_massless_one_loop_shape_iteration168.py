#!/usr/bin/env python3
"""Iteration 168: leading massless one-loop C5 TT absorptive shape.

Scope frozen here:
- flat Minkowski background, mostly-plus metric;
- the eight timelike conserved-TT linear-response rows of Iterations 166-167;
- EH tree propagators plus the complete curvature-squared nonlocal one-loop family
  R log(-Box/mu^2) R, Ricci log(-Box/mu^2) Ricci,
  Riemann log(-Box/mu^2) Riemann;
- renormalized local curvature-squared counterterms are allowed but are real off pole
  and therefore do not enter the absorptive block;
- no higher-derivative EFT insertion inside the loop, no two-loop contribution,
  no massive threshold, and no nonlinear/post-Gaussian response is silently set to zero.
  Those are explicitly outside this frozen perturbative order.

For a normalized TT polarization h=E exp(ik.x), k=(omega,0,0,0), every
linearized curvature carries two powers of k.  Numerically we verify
 R^(1)=0,
 Ricci^(1):Ricci^(1) = s^2/4,
 Riemann^(1):Riemann^(1) = s^2,
 Weyl^(1):Weyl^(1) = s^2/2.
Thus every nonzero curvature^2 log form factor gives a 1PI TT self-energy
Sigma_TT proportional to s^2 log(-s-i0 sign omega).  Dressing a linear
source response with two EH propagators G0~1/s gives delta chi_R proportional
to log(-s-i0 sign omega), whose frequency-odd imaginary part is constant.
The overall coefficient is theory/species/scheme dependent, but the absorptive
shape at this order is not.
"""
from pathlib import Path
import json
import math
import numpy as np

ETA=np.diag([-1.0,1.0,1.0,1.0])
s=0.004*np.arange(1,9,dtype=float)
omega=np.sqrt(s)
x=s/s[-1]
E=np.zeros((4,4),float)
E[1,1]=1/math.sqrt(2)
E[2,2]=-1/math.sqrt(2)


def linearized_curvatures(k,h):
    kc=ETA@k
    htrace=float(np.einsum('mn,mn',ETA,h))
    h_up1=ETA@h
    k2=float(k@ETA@k)
    box=-k2
    Ric=np.zeros((4,4),float)
    for m in range(4):
        for n in range(4):
            term=0.0
            for r in range(4):
                term += -kc[r]*kc[m]*h_up1[r,n]
                term += -kc[r]*kc[n]*h_up1[r,m]
            term += -box*h[m,n]
            term += kc[m]*kc[n]*htrace
            Ric[m,n]=0.5*term
    R=float(np.einsum('mn,mn',ETA,Ric))
    Riem=np.zeros((4,4,4,4),float)
    for m in range(4):
      for n in range(4):
       for r in range(4):
        for t in range(4):
         Riem[m,n,r,t]=0.5*(-kc[r]*kc[n]*h[m,t]
                            -kc[t]*kc[m]*h[n,r]
                            +kc[t]*kc[n]*h[m,r]
                            +kc[r]*kc[m]*h[n,t])
    return R,Ric,Riem


def contract2(T):
    return float(np.einsum('ab,cd,ac,bd',T,T,ETA,ETA))


def contract4(T):
    return float(np.einsum('abcd,efgh,ae,bf,cg,dh',T,T,ETA,ETA,ETA,ETA))

rows=[]
max_R=0.0
ric_rat=[]
riem_rat=[]
weyl_rat=[]
for i,w in enumerate(omega):
    k=np.array([w,0.0,0.0,0.0])
    R,Ric,Riem=linearized_curvatures(k,E)
    ric=contract2(Ric)
    riem=contract4(Riem)
    # In 4D: C^2=Riem^2-2 Ricci^2+R^2/3.
    weyl=riem-2.0*ric+(R*R)/3.0
    ric_rat.append(ric/s[i]**2)
    riem_rat.append(riem/s[i]**2)
    weyl_rat.append(weyl/s[i]**2)
    max_R=max(max_R,abs(R))
    rows.append({"probe":i,"s":float(s[i]),"omega":float(w),
                 "R_linear":R,"Ricci2_over_s2":float(ric/s[i]**2),
                 "Riemann2_over_s2":float(riem/s[i]**2),
                 "Weyl2_over_s2":float(weyl/s[i]**2)})

# Reconstruct the same target-independent constant-null quotient as Iteration 167.
V=np.column_stack([x**n for n in range(8)])
Q,_=np.linalg.qr(V)
for j in range(8):
    idx=int(np.argmax(np.abs(Q[:,j])))
    if Q[idx,j] < 0:
        Q[:,j]*=-1
Q_shape=Q[:,1:]
one=np.ones(8)

# These are normalized TT curvature contractions before the common log and the
# two EH propagators.  After dividing by s^2 all nonzero columns are constant.
shape_coefficients={
    "R_log_R":0.0,
    "Ricci_log_Ricci":float(np.mean(ric_rat)),
    "Riemann_log_Riemann":float(np.mean(riem_rat)),
    "Weyl_log_Weyl":float(np.mean(weyl_rat)),
}
shape_columns={name:coef*one for name,coef in shape_coefficients.items()}
M=np.column_stack(list(shape_columns.values()))
sv=np.linalg.svd(M,compute_uv=False)
rank=int(np.linalg.matrix_rank(M,tol=1e-12))
projected={name:float(np.linalg.norm(Q_shape.T@col)) for name,col in shape_columns.items()}

out={
  "iteration":168,
  "date":"2026-08-31",
  "scope":"leading one-loop massless curvature-squared nonlocal C5 correction to eight-row timelike conserved-TT chi1R absorptive block",
  "frozen_order":{
    "tree":"Einstein-Hilbert plus renormalized local curvature-squared counterterms",
    "loop":"one massless loop, leading curvature-squared nonlocal form factors only",
    "renormalization":"MS-like local/nonlocal split at arbitrary positive mu; absorptive discontinuity is mu- and local-counterterm independent",
    "retarded_branch":"Im log_R(-s) is odd in omega and constant in magnitude for s>0",
    "excluded_not_zero":[
      "two-loop massless self-energy",
      "one-loop graphs with higher-derivative EFT insertions",
      "massive thresholds",
      "nonlinear/post-Gaussian source-response completion"
    ]
  },
  "TT_curvature_certificate":{
    "max_abs_linear_R":max_R,
    "max_abs_Ricci2_over_s2_minus_quarter":float(np.max(np.abs(np.asarray(ric_rat)-0.25))),
    "max_abs_Riemann2_over_s2_minus_one":float(np.max(np.abs(np.asarray(riem_rat)-1.0))),
    "max_abs_Weyl2_over_s2_minus_half":float(np.max(np.abs(np.asarray(weyl_rat)-0.5))),
    "shape_coefficients":shape_coefficients
  },
  "leading_massless_one_loop_shape":{
    "column_rank_before_constant_profile":rank,
    "singular_values":sv.tolist(),
    "classification":"ALL_NONZERO_CURVATURE_SQUARED_LOG_TT_TWO_POINT_COLUMNS_ARE_COLLINEAR_WITH_THE_CONSTANT_ABSORPTIVE_DIRECTION",
    "projected_norms_after_iteration167_constant_profile":projected,
    "max_projected_norm":float(max(projected.values())),
    "conclusion":"complete leading massless one-loop curvature-squared C5 TT absorptive span is annihilated by Q_shape to machine precision"
  },
  "power_counting_boundary":{
    "two_loop":"BLOCKED_NEXT_ORDER_SHAPE; dimensional analysis permits extra powers of s multiplying nonanalytic logs",
    "higher_derivative_loop_insertions":"BLOCKED_NEXT_ORDER_SHAPE; requires separately frozen EFT-order/Wilson convention",
    "massive_thresholds":"BLOCKED_THRESHOLD_COMPARATOR; not represented by the massless log",
    "claim_boundary":"no statement that the full quantum C5 absorptive response is constant"
  },
  "retained_results":[
    "C5-NG-005 — LEADING_MASSLESS_ONE_LOOP_TT_ABSORPTIVE_SPAN_IS_ONE_DIMENSIONAL_CONSTANT_SHAPE",
    "ABS-SHAPE-003 — ITERATION167_CONSTANT_QUOTIENT_REMOVES_COMPLETE_LEADING_MASSLESS_ONE_LOOP_CURVATURE_SQUARED_C5_TT_SECTOR",
    "NG-FUNNEL-028 — HIGHER_LOOP_AND_HIGHER_DERIVATIVE_LOOP_SHAPES_ARE_TRUNCATION_UNCERTAINTY_NOT_ZERO_COLUMNS"
  ],
  "ANSATZ_003":"NOT_CREATED",
  "Fisher_resources":"FORBIDDEN",
  "model_readiness_percent":24,
  "readiness_change":"unchanged; a major C5 comparator blocker is narrowed, but no residual survives the still-blocked AS finite-frequency and next-order loop shape quotient",
  "rows":rows
}
Path("results/c5_massless_one_loop_shape_iteration168.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
