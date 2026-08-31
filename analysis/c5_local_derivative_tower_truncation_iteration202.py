#!/usr/bin/env python3
"""Iteration 202: C5 local derivative-tower truncation audit.

This audit asks whether the rank-4 soft2 C5 nuisance on the frozen v3 protocols
is a model-independent local-EFT boundary or only a consequence of the frozen
dimension-12 cutoff.

Authority inherited from Iteration 178:

  B_T[RiemannChain Box^n] = (2/3)(-q^2)^n B_T[Riemann^3], n=1,2,3.

The same flat-background cubic operator argument extends to every integer n>=1:
at O(h^3), Box^n acts on one linearized curvature.  If it acts on the physical
null soft leg, k_soft^2=0; if it acts on either hard momentum eigenmode, it
contributes (-q^2)^n.  Four of six permutations survive, hence the factor 2/3.

Therefore on N frozen rows the local family has columns

  v_0(i)=r_i,
  v_n(i)=(2/3) r_i (-x_i)^n, n>=1.

For distinct x_i and nonzero r_i, the first N columns are diag(r) times a
Vandermonde matrix up to nonzero column scalings and therefore have exact rank N.

This is a finite-protocol saturation theorem for this declared local analytic
operator family.  It is NOT a statement that every Box^n representative is an
independent element of every nonredundant 4D EFT basis after IBP/EOM reduction;
the physics claim is that a finite residual requires an explicit EFT-order /
remainder restriction before omitted local analytic directions may be ignored.
"""
from pathlib import Path
from decimal import Decimal, getcontext
import json
import numpy as np

getcontext().prec = 100

A_PATH = Path('results/withheld_v3_local_c5_soft2_iteration197.json')
B_PATH = Path('results/withheld_v3_local_c5_soft2_iteration199.json')
A = json.loads(A_PATH.read_text())
B = json.loads(B_PATH.read_text())

xA = np.array(A['q2'], dtype=float)
xB = np.array(B['q2'], dtype=float)
rA = np.array(A['Riemann3_soft2'], dtype=float)
rB = np.array(B['Riemann3_soft2'], dtype=float)
assert np.allclose(xA, xB, rtol=0, atol=1e-13)
x = xA

def matrix(r, ncols):
    cols = [r]
    for n in range(1, ncols):
        cols.append((2.0/3.0) * r * ((-x)**n))
    return np.column_stack(cols)

def ladder(r):
    ans=[]
    for ncols in range(4,13):
        V=matrix(r,ncols)
        s=np.linalg.svd(V,compute_uv=False)
        ans.append({
            'ncols':ncols,
            'max_box_power':ncols-1,
            'operator_dimension_max':6+2*(ncols-1),
            'rank_tol_1e-12':int(np.linalg.matrix_rank(V,tol=1e-12)),
            'smax':float(s[0]),
            'smin':float(s[-1]),
            'condition_number':float(s[0]/s[-1]),
        })
    return ans

def exact_det(xvals, rvals):
    # det diag(r) * [1, (2/3)y, (2/3)y^2, ...], y=-x.
    xd=[Decimal(str(v)) for v in xvals]
    rd=[Decimal(str(v)) for v in rvals]
    y=[-v for v in xd]
    det=Decimal(1)
    for v in rd: det*=v
    for i in range(len(y)):
        for j in range(i+1,len(y)):
            det *= (y[j]-y[i])
    det *= (Decimal(2)/Decimal(3))**(len(y)-1)
    return det

out={
  'iteration':202,
  'date':'2026-09-01',
  'model_readiness_percent':23,
  'readiness_change':'24 -> 23: local-C5 comparator foundation re-opened because dimension-12 truncation lacks a model-independent remainder bound over the current x range',
  'protocols':['v3-A','v3-B'],
  'x':x.tolist(),
  'x_min':float(x.min()),
  'x_max':float(x.max()),
  'max_node_power_examples':{str(n):float(x.max()**n) for n in [1,2,3,4,6,8,11]},
  'all_x_distinct':bool(len(set(np.round(x,15)))==len(x)),
  'all_rA_nonzero':bool(np.all(rA!=0)),
  'all_rB_nonzero':bool(np.all(rB!=0)),
  'arbitrary_n_soft_identity':'v0=r; vn=(2/3) r (-x)^n for n>=1 within the declared Riemann-chain Box^n cubic family',
  'determinant_formula':'det(V_N)=prod_i r_i * (2/3)^(N-1) * prod_{i<j}[(-x_j)-(-x_i)]',
  'exact_det_12_A_100digit_decimal':str(exact_det(x,rA)),
  'exact_det_12_B_100digit_decimal':str(exact_det(x,rB)),
  'ladder_A':ladder(rA),
  'ladder_B':ladder(rB),
  'exact_rank_theorem':'For N distinct x_i and nonzero r_i, first N columns of this local analytic derivative family have exact rank N.',
  'classification':{
    'dimension12_rank4_complement':'SCOPED_TRUNCATION_RESULT_NOT_MODEL_INDEPENDENT_C5_COMPLEMENT',
    'untruncated_local_analytic_tower':'FINITE_N_ROW_SPACE_SATURABLE',
    'high_order_numeric_conditioning':'SEVERE_NEAR_DEGENERACY_DOES_NOT_NEGATE_EXACT_VANDERMONDE_RANK',
    'EFT_truncation_control':'BLOCKED_REQUIRES_POWER_COUNTING_AND_REMAINDER_BOUND',
    'AS':'BLOCKED_NOT_ZERO',
    'C3':'BLOCKED_NOT_ZERO',
    'candidate_residual':'NONE',
    'ANSATZ_003':'NOT_CREATED',
    'Fisher_resources':'FORBIDDEN'
  },
  'retained_results':[
    'C5-NG-019 — LOCAL_RIEMANN_CUBIC_DERIVATIVE_TOWER_CAN_SATURATE_ANY_FINITE_NULLSOFT_ROW_SET_WITH_DISTINCT_HARD_NODES',
    'REL-NG-015 — DIMENSION12_RANK4_COMPLEMENT_IS_NOT_A_MODEL_INDEPENDENT_C5_RESIDUAL_SPACE_WITHOUT_EFT_REMAINDER_CONTROL',
    'NG-FUNNEL-057 — FINITE_ANALYTIC_SOFT2_NOVELTY_REQUIRES_CONTROLLED_EFT_TRUNCATION_OR_A_NONINTERPOLABLE_LINKED_OBSERVABLE',
    'READINESS-CORR-001 — C5_TRUNCATION_BLOCKER_REOPENS_ONE_COMPARATOR_FOUNDATION_POINT'
  ]
}
Path('results/c5_local_derivative_tower_truncation_iteration202.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
