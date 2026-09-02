#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 280.

Scalar one-loop retarded cut-support map for the three non-scaleless master
kinematic families surviving Iterations 275/279.  This is not a tensor
coefficient computation.

On the controlled linked slice:
  s=-k_a^2 > 0,
  t=-k_b^2=s+Delta, Delta=0.2,
  k_s^2=0.

Massless raised bubbles reduce to bubble masters/derivatives whose finite
nonanalytic part contains log_R(-s)/s or log_R(-t)/t.  The two-mass massless
triangle master with one null external leg has the standard dimensionally
regulated structure proportional to
  [(-s-i0)^(-eps)-(-t-i0)^(-eps)]/[eps^2 (s-t)].
Along fixed Delta the common 1/eps discontinuity cancels, while the finite
cut-support direction is proportional to log(s/t)/(s-t).  Raised triangle
powers reduce by one-loop IBP to this triangle plus bubble families.
"""
import json, numpy as np
S=np.arange(.004,.033,.004); DELTA=.2
X=[]; rows=[]
for s in S:
    t=s+DELTA
    ba=1./s
    bb=1./t
    tri=np.log(s/t)/(s-t)
    rows.append({'s':float(s),'t':float(t),'bubble_a_cut_shape':float(ba),
                 'bubble_b_cut_shape':float(bb),'triangle_cut_shape':float(tri)})
    X.append([ba,bb,tri])
X=np.array(X)
sv=np.linalg.svd(X,compute_uv=False)
Xn=X/np.linalg.norm(X,axis=0)
svn=np.linalg.svd(Xn,compute_uv=False)
result={
 'iteration':280,'model_readiness_percent':24,
 'linked_slice':'s=-ka^2>0; t=-kb^2=s+0.2; ks^2=0',
 'normalized_discontinuity_convention':'D_s log_R(-s)=1 (Iteration 205)',
 'scalar_cut_support_basis':['1/s','1/(s+0.2)','log(s/(s+0.2))/(s-(s+0.2))'],
 'rows':rows,
 'raw_singular_values':[float(x) for x in sv],
 'raw_condition_number':float(sv[0]/sv[-1]),
 'unit_column_singular_values':[float(x) for x in svn],
 'unit_column_condition_number':float(svn[0]/svn[-1]),
 'rank':int(np.linalg.matrix_rank(X)),
 'classification':'PASS_SCOPED_THREE_DIMENSIONAL_SCALAR_MASTER_CUT_SUPPORT_BASIS_ON_TIMELIKE_SLICE',
 'guardrails':[
   'THIS_IS_MASTER_FUNCTION_SUPPORT_NOT_THE_C5_TENSOR_COEFFICIENT_VECTOR',
   'THE_LINKED_FIXED_DELTA_SLICE_IS_A_CONTROLLED_INTERNAL_CONTINUATION_UNTIL_THE_FINAL_SOURCE_COMPLETED_MULTIVARIABLE_D_s_PROTOCOL_IS_FROZEN',
   'DO_NOT_INTERPRET_THIS_SHAPE_RANK_AS_FISHER_OR_AS_A_CANDIDATE_RESIDUAL'
 ],
 'next_gate':'canonicalize and reconstruct the combined scalar orbit-trace numerators for bubble-a, bubble-b and triangle families; perform one-loop tensor/IBP reduction to obtain their actual coefficients multiplying this cut-support basis'
}
assert result['rank']==3
assert all(r['triangle_cut_shape']>0 for r in rows)
print(json.dumps(result,indent=2,sort_keys=True))
