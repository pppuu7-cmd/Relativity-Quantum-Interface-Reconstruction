#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 196.

Structural row-robustness theorem for the Iteration-195 supported quotient.

Hard K2 block:
  [x,x^2,...,x^6,x^2 exp(x)].
For x>0 factor one x from every row.  The collocation functions become
  {1,x,x^2,x^3,x^4,x^5,x exp(x)}.
Their leading polynomial Wronskians are nonzero constants and the full
Wronskian is 34560*(x+6)*exp(x)>0 on x>0.  Hence this ordered family is an
extended complete Chebyshev system on the positive interval: every 7 distinct
positive nodes give a nonsingular 7x7 collocation matrix.  Thus the exact
local/nonlocal K2 identity is structurally impossible for this frozen function
family once at least seven distinct positive x rows are used.

Conditional soft2 block:
  V4 = diag(r0) [1,-x,x^2,-x^3].
For any four rows with distinct x and nonzero r0, the determinant is a nonzero
row-scale factor times a Vandermonde determinant.  Therefore every >=4-row
subset of the current protocol has rank four.
"""
from pathlib import Path
import itertools, json
import numpy as np
import sympy as sp

x=sp.symbols('x', positive=True)
funcs=[x**k for k in range(6)]+[x*sp.exp(x)]
wronskians=[sp.factor(sp.wronskian(funcs[:n],x)) for n in range(1,8)]
W7=wronskians[-1]
assert sp.simplify(W7-34560*(x+6)*sp.exp(x))==0

q2=np.array([
  0.2855249999999999,0.21678750000000005,0.23962499999999995,
  0.17735625,0.22522499999999995,0.16211250000000002,
  0.793125,0.6021875,0.665625,0.49265624999999996,0.625625,
  0.45031250000000006],float)
r0=np.array([
  0.09062678834951932,0.16803920764664712,-0.09789544062570427,
  -0.005916118520839153,-0.029039631761568437,-0.07238006200957146,
  -0.06610818516517986,0.38320932719734235,0.029971342547624725,
  0.45560116033401604,0.6591802274467985,-0.18125066515442065],float)
assert len(np.unique(q2))==12
assert np.all(q2>0)
assert np.all(r0!=0)

A7=np.column_stack([q2**k for k in range(1,7)]+[q2**2*np.exp(q2)])
V4=np.column_stack([r0,-q2*r0,q2**2*r0,-q2**3*r0])

# Exhaustive numerical regression against the structural theorem.
hard_7row_ranks=[]; hard_7row_conds=[]; hard_7row_smins=[]
for keep in itertools.combinations(range(12),7):
    M=A7[list(keep)]
    s=np.linalg.svd(M,compute_uv=False)
    hard_7row_ranks.append(int(np.linalg.matrix_rank(M,tol=1e-12)))
    hard_7row_conds.append(float(s[0]/s[-1]))
    hard_7row_smins.append(float(s[-1]))

soft_4row_ranks=[]; soft_4row_conds=[]; soft_4row_smins=[]
for keep in itertools.combinations(range(12),4):
    M=V4[list(keep)]
    s=np.linalg.svd(M,compute_uv=False)
    soft_4row_ranks.append(int(np.linalg.matrix_rank(M,tol=1e-12)))
    soft_4row_conds.append(float(s[0]/s[-1]))
    soft_4row_smins.append(float(s[-1]))

out={
  'iteration':196,
  'protocol':'RQIR-WITHHELD-NULLSOFT-12-v2',
  'hard_K2_structural_theorem':{
    'factored_functions':['1','x','x^2','x^3','x^4','x^5','x*exp(x)'],
    'leading_wronskians':[str(w) for w in wronskians],
    'full_wronskian':str(W7),
    'sign_on_x_positive':'STRICTLY_POSITIVE',
    'classification':'EXTENDED_COMPLETE_CHEBYSHEV_SYSTEM_ON_X_POSITIVE',
    'consequence':'ANY_SEVEN_DISTINCT_POSITIVE_X_NODES_GIVE_RANK7',
    'current_protocol_all_7row_subsets':len(hard_7row_ranks),
    'current_protocol_min_rank':min(hard_7row_ranks),
    'current_protocol_max_condition_number':max(hard_7row_conds),
    'current_protocol_min_smallest_singular_value':min(hard_7row_smins),
    'conditioning_note':'exact structural independence does not remove severe near-degeneracy on narrow finite x intervals'
  },
  'conditional_soft2_structural_theorem':{
    'form':'diag(r0)*[1,-x,x^2,-x^3]',
    'all_x_distinct':True,
    'all_r0_nonzero':True,
    'consequence':'ANY_FOUR_CURRENT_ROWS_GIVE_RANK4_BY_VANDERMONDE',
    'current_protocol_all_4row_subsets':len(soft_4row_ranks),
    'current_protocol_min_rank':min(soft_4row_ranks),
    'current_protocol_max_condition_number':max(soft_4row_conds),
    'current_protocol_min_smallest_singular_value':min(soft_4row_smins)
  },
  'classification':{
    'hard_rank7':'STRUCTURALLY_ROW_ROBUST_FOR_DISTINCT_POSITIVE_X',
    'soft2_rank4':'STRUCTURALLY_ROW_ROBUST_FOR_CURRENT_NONZERO_R0_DISTINCT_X_ROWS',
    'finite_noise_identifiability':'NOT_CLAIMED',
    'AS':'BLOCKED_NOT_ZERO','C3':'BLOCKED_NOT_ZERO',
    'candidate_residual':'NOT_TESTED','ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'
  },
  'retained_results':[
    'REL-NG-011 — LOCAL_POLYNOMIAL_PLUS_FIXED_EXPONENTIAL_K2_FAMILY_FORMS_AN_ECT_SYSTEM_AFTER_ROW_FACTORING_ON_X_POSITIVE',
    'NUM-NG-010 — EXACT_RANK7_IS_ROW_STRUCTURAL_BUT_CAN_REMAIN_SEVERELY_ILL_CONDITIONED',
    'C5-NG-016 — CONDITIONAL_CURVATURE_CUBIC_SOFT2_BASIS_IS_A_ROW_SCALED_VANDERMONDE_AND_ANY_FOUR_CURRENT_ROWS_HAVE_RANK4',
    'NG-FUNNEL-050 — STRUCTURAL_RANK_ROBUSTNESS_AND_OPERATIONAL_CONDITIONING_ARE_SEPARATE_GATES'
  ],
  'model_readiness_percent':24,
  'readiness_change':'unchanged: supported comparator ranks are now structurally row-robust, but AS/C3 authority blockers still prevent full comparator closure and no candidate residual exists.'
}
Path('results/withheld_v2_structural_rank_theorem_iteration196.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
