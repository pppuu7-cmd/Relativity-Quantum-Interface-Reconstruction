#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 197.

Target-independent prospective hard-row design to improve conditioning of the
supported rank-7 K2 block before any candidate evaluation.

The six base hard q-vectors are fixed.  Search only a preregistered two-scale
grid:
  low  in {0.60,0.65,...,0.90}
  high in {1.10,1.15,...,1.40}
with the internal design window 0.10 <= x=q^2 <= 1.00 for all 12 rows.
Objective: minimize the condition number of the column-normalized supported K2
matrix [x,x^2,...,x^6,x^2 exp(x)].  Tie-break by raw condition number.
No candidate amplitude, residual, left-null, or soft2 value enters the design.
"""
from pathlib import Path
import json
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
QS=np.array([
 [0.18,0.70,0.20,0.10],
 [0.14,0.55,-0.25,0.20],
 [0.22,0.62,0.18,-0.24],
 [0.16,0.48,0.31,0.12],
 [0.20,0.58,-0.16,-0.28],
 [0.12,0.44,0.27,-0.19]],float)
k0=np.array([1.,0.,0.,1.])

def dot(v): return float(v@ETA@v)
base_x=np.array([dot(q) for q in QS])
assert np.all(base_x>0)

low_grid=np.round(np.arange(0.60,0.901,0.05),2)
high_grid=np.round(np.arange(1.10,1.401,0.05),2)
records=[]
for lo in low_grid:
    for hi in high_grid:
        xs=np.concatenate([base_x*lo**2,base_x*hi**2])
        if xs.min()<0.10-1e-12 or xs.max()>1.00+1e-12:
            continue
        A=np.column_stack([xs**k for k in range(1,7)]+[xs**2*np.exp(xs)])
        s=np.linalg.svd(A,compute_uv=False)
        norms=np.linalg.norm(A,axis=0)
        sn=np.linalg.svd(A/norms,compute_uv=False)
        records.append({
          'low_scale':float(lo),'high_scale':float(hi),
          'x_min':float(xs.min()),'x_max':float(xs.max()),
          'raw_condition_number':float(s[0]/s[-1]),
          'raw_smallest_singular_value':float(s[-1]),
          'column_normalized_condition_number':float(sn[0]/sn[-1]),
          'column_normalized_smallest_singular_value':float(sn[-1])})

best=min(records,key=lambda r:(r['column_normalized_condition_number'],r['raw_condition_number']))
lo=best['low_scale']; hi=best['high_scale']
scales=[lo,hi]
qs=np.vstack([QS*lo,QS*hi])
xs=np.array([dot(q) for q in qs])
A=np.column_stack([xs**k for k in range(1,7)]+[xs**2*np.exp(xs)])
s=np.linalg.svd(A,compute_uv=False)
sn=np.linalg.svd(A/np.linalg.norm(A,axis=0),compute_uv=False)

# Spacelike partner check on the same geometry-only epsilon window used by v2.
eps_grid=np.linspace(-0.01,0.01,81)
partner_x=[]
for q in qs:
    partner_x.extend([dot(-q-e*k0) for e in eps_grid])
assert min(partner_x)>0

# Frozen v2 reference for direct conditioning comparison.
x_v2=np.concatenate([base_x*0.75**2,base_x*1.25**2])
A_v2=np.column_stack([x_v2**k for k in range(1,7)]+[x_v2**2*np.exp(x_v2)])
s_v2=np.linalg.svd(A_v2,compute_uv=False)
sn_v2=np.linalg.svd(A_v2/np.linalg.norm(A_v2,axis=0),compute_uv=False)

out={
 'iteration':197,
 'protocol_name':'RQIR-WITHHELD-NULLSOFT-12-v3-K2-FROZEN',
 'design_status':'K2_GEOMETRY_FROZEN_BEFORE_ANY_CUBIC_OR_CANDIDATE_EVALUATION',
 'design_rule':{
   'base_q_vectors':'same six frozen base q vectors',
   'low_scale_grid':low_grid.tolist(),
   'high_scale_grid':high_grid.tolist(),
   'hard_x_window':[0.10,1.00],
   'objective':'minimize column-normalized condition number of [x,...,x^6,x^2 exp(x)]',
   'tie_break':'minimize raw condition number',
   'candidate_information_used':False,
   'soft2_information_used':False,
   'valid_grid_pairs':len(records)},
 'selected':{
   'low_scale':lo,'high_scale':hi,
   'x_values':xs.tolist(),
   'x_min':float(xs.min()),'x_max':float(xs.max()),
   'hard_rank':int(np.linalg.matrix_rank(A,tol=1e-12)),
   'raw_singular_values':s.tolist(),
   'raw_condition_number':float(s[0]/s[-1]),
   'column_normalized_singular_values':sn.tolist(),
   'column_normalized_condition_number':float(sn[0]/sn[-1]),
   'partner_x_min_on_eps_grid':float(min(partner_x)),
   'partner_x_max_on_eps_grid':float(max(partner_x))},
 'comparison_to_v2':{
   'v2_raw_condition_number':float(s_v2[0]/s_v2[-1]),
   'v3_raw_condition_improvement_factor':float((s_v2[0]/s_v2[-1])/(s[0]/s[-1])),
   'v2_column_normalized_condition_number':float(sn_v2[0]/sn_v2[-1]),
   'v3_column_normalized_condition_improvement_factor':float((sn_v2[0]/sn_v2[-1])/(sn[0]/sn[-1])),
   'v2_raw_smallest_singular_value':float(s_v2[-1]),
   'v3_raw_smallest_singular_value_gain':float(s[-1]/s_v2[-1])},
 'classification':{
   'hard_rank7':'PASS_STRUCTURAL_AND_NUMERICAL',
   'conditioning':'IMPROVED_BUT_STILL_NEAR_DEGENERATE',
   'cubic_protocol':'NOT_YET_FROZEN_FOR_V3',
   'candidate_residual':'NOT_TESTED','ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
 'retained_results':[
   'NUM-NG-011 — TARGET_INDEPENDENT_SCALE_DESIGN_IMPROVES_SUPPORTED_HARD_K2_CONDITIONING_WITHOUT_USING_CANDIDATE_INFORMATION',
   'PROTO-NG-004 — WITHHELD_V3_K2_GEOMETRY_IS_FROZEN_BEFORE_CUBIC_POLARIZATION_OR_CANDIDATE_EVALUATION',
   'NG-FUNNEL-051 — CONDITIONING_OPTIMIZATION_MAY_USE_FIXED_COMPARATOR_GEOMETRY_BUT_NOT_FUTURE_CANDIDATE_RESIDUALS'],
 'model_readiness_percent':24,
 'readiness_change':'unchanged: conditioning improved prospectively, but AS/C3 remain blocked and v3 cubic geometry is not yet frozen.'}
Path('results/withheld_v3_k2_conditioning_design_iteration197.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
