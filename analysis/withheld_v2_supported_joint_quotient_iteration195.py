#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 195.

Build the prospectively supported comparator quotient on
RQIR-WITHHELD-NULLSOFT-12-v2 without zero-filling unsupported AS/C3 rows.

Parameter block:
  theta = (c1,...,c6, lambda_NL, g0,...,g3)
where c1..c6 are the frozen local quadratic K2 Wilson directions x..x^6,
lambda_NL is the fixed QG-NL-EXP-001 K2 tangent x^2 exp(x), and g0..g3
are the zero-K2 local curvature-cubic C5 directions
Riemann3_soft2 * {1,-x,x^2,-x^3}.

The exact hard K2 matrix is [A7,0].  Because A7 has full column rank 7 on
the prospectively frozen 12 rows, its exact nullspace contains no quadratic
or nonlocal parameter variation.  Therefore the conditional soft2 nuisance
map is determined solely by the four zero-K2 curvature-cubic columns.  The
unknown/blocked AS and C3 soft2 maps are deliberately not represented as zero.
"""
from pathlib import Path
import json
import numpy as np

x=np.array([
  0.2855249999999999,0.21678750000000005,0.23962499999999995,
  0.17735625,0.22522499999999995,0.16211250000000002,
  0.793125,0.6021875,0.665625,0.49265624999999996,0.625625,
  0.45031250000000006],float)
r0=np.array([
  0.09062678834951932,0.16803920764664712,-0.09789544062570427,
  -0.005916118520839153,-0.029039631761568437,-0.07238006200957146,
  -0.06610818516517986,0.38320932719734235,0.029971342547624725,
  0.45560116033401604,0.6591802274467985,-0.18125066515442065],float)

A_local=np.column_stack([x**k for k in range(1,7)])
v_nl=x*x*np.exp(x)
A7=np.column_stack([A_local,v_nl])
A_full=np.column_stack([A7,np.zeros((12,4))])

sA=np.linalg.svd(A7,compute_uv=False)
rank_A7=int(np.linalg.matrix_rank(A7,tol=1e-12))
rank_Afull=int(np.linalg.matrix_rank(A_full,tol=1e-12))
assert rank_A7==7 and rank_Afull==7

# Exact structural nullspace: A7 full column rank and the final four columns
# are exact K2 zeros, hence only g0..g3 survive hard calibration.
N_exact=np.zeros((11,4))
N_exact[7:,:]=np.eye(4)
assert np.max(np.abs(A_full@N_exact))==0.0

V4=np.column_stack([r0,-x*r0,x*x*r0,-x**3*r0])
sV=np.linalg.svd(V4,compute_uv=False)
rank_V=int(np.linalg.matrix_rank(V4,tol=1e-12))
assert rank_V==4

# Orthonormal quotient projector in the supported soft2 block.
Q,_=np.linalg.qr(V4)
Q=Q[:,:4]
P_perp=np.eye(12)-Q@Q.T
rank_P=int(np.linalg.matrix_rank(P_perp,tol=1e-10))
assert rank_P==8

out={
  'iteration':195,
  'protocol':'RQIR-WITHHELD-NULLSOFT-12-v2',
  'scope':'prospective supported C5/C4-boundary/nonlocal quotient only; AS/C3 remain blocked and are not zero-filled',
  'parameter_order':['c1_x','c2_x2','c3_x3','c4_x4','c5_x5','c6_x6','lambda_NL','g0_Riemann3','g1_BoxRiemann3','g2_Box2Riemann3','g3_Box3Riemann3'],
  'hard_K2':{
    'rows':12,
    'A7_rank':rank_A7,
    'A7_columns':7,
    'A7_singular_values':sA.tolist(),
    'A7_condition_number':float(sA[0]/sA[-1]),
    'A_full_rank':rank_Afull,
    'parameter_count':11,
    'exact_parameter_nullity_after_K2':4,
    'exact_null_support':'ONLY_ZERO_K2_CURVATURE_CUBIC_PARAMETERS_g0_TO_g3',
    'nonlocal_lambda_survives_exact_K2':False,
    'conditioning_note':'FULL_RANK_BUT_NEAR_DEGENERATE; exact algebraic hard calibration removes lambda_NL, but finite-precision/noisy calibration would require separate conditioning treatment'
  },
  'conditional_soft2':{
    'authorized_map':'V4 = Riemann3_soft2*{1,-x,x^2,-x^3}',
    'rank':rank_V,
    'singular_values':sV.tolist(),
    'quotient_projector_rank':rank_P,
    'supported_complement_dimension_before_AS_C3':12-rank_V,
    'projector_annihilation_norm':float(np.linalg.norm(P_perp@V4))
  },
  'blocked_comparators':{
    'AS':'BLOCKED_AS_REALTIME_RELATION_COMPLETION_NOT_ZERO',
    'C3':'BLOCKED_C3_CTP_ORDERED_COMPLETION_NOT_ZERO'
  },
  'classification':{
    'supported_joint_quotient':'RESOLVED_SCOPED',
    'old_six_row_conditioned_nonlocal_soft2':'NOT_TRANSFERRED_TO_WITHHELD_V2',
    'candidate_residual':'NOT_TESTED',
    'ANSATZ_003':'NOT_CREATED',
    'Fisher_resources':'FORBIDDEN'
  },
  'retained_results':[
    'REL-NG-010 — FULL_COLUMN_RANK_WITHHELD_K2_MATRIX_ELIMINATES_ALL_SUPPORTED_QUADRATIC_AND_NONLOCAL_PARAMETER_VARIATIONS_UNDER_EXACT_HARD_CALIBRATION',
    'C5-NG-015 — AFTER_EXACT_WITHHELD_K2_CALIBRATION_THE_SUPPORTED_CONDITIONAL_SOFT2_NUISANCE_IS_THE_RANK4_ZERO_K2_CURVATURE_CUBIC_SECTOR',
    'NUM-NG-009 — WITHHELD_K2_INDEPENDENCE_IS_EXACT_ALGEBRAIC_BUT_STRONGLY_ILL_CONDITIONED_AND_MUST_NOT_BE_CONFUSED_WITH_FINITE_NOISE_IDENTIFIABILITY',
    'NG-FUNNEL-049 — BLOCKED_AS_C3_COLUMNS_MUST_REMAIN_OUTSIDE_THE_SUPPORTED_QUOTIENT_RATHER_THAN_BE_ZERO_FILLED'
  ],
  'model_readiness_percent':24,
  'readiness_change':'unchanged: the supported prospective quotient is now explicit, but the last comparator-foundation point remains blocked by unresolved AS/C3 ordered relation authority and no candidate residual exists.'
}
Path('results/withheld_v2_supported_joint_quotient_iteration195.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
