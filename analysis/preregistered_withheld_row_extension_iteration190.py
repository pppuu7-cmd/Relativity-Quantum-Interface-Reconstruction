#!/usr/bin/env python3
"""Iteration 190: preregister a target-independent withheld null-soft row extension.

No candidate or residual is evaluated here.  The extension is frozen solely from
Iteration-185 baseline kinematics by scaling each hard q-vector by the fixed
factors 0.75 and 1.25.  This broadens the q^2 lever arm symmetrically around the
existing scale without using the Iteration-188 left-null vector or any target.
"""
from pathlib import Path
import json, numpy as np

ETA=np.diag([-1.,1.,1.,1.])
QS=np.array([
 [0.18,0.70,0.20,0.10],
 [0.14,0.55,-0.25,0.20],
 [0.22,0.62,0.18,-0.24],
 [0.16,0.48,0.31,0.12],
 [0.20,0.58,-0.16,-0.28],
 [0.12,0.44,0.27,-0.19]],float)
k0=np.array([1.,0.,0.,1.])
scales=[0.75,1.25]
soft_steps=[0.01,0.005,0.0025,0.00125,0.000625]

def dot(a,b): return float(a@ETA@b)
rows=[]
for scale in scales:
    for i,q0 in enumerate(QS):
        q=scale*q0
        q2=dot(q,q)
        partner=[]
        for eps in soft_steps:
            r=-q-eps*k0
            partner.append({"epsilon":eps,"r2":dot(r,r)})
        rows.append({
          "row_id":f"W{len(rows):02d}",
          "source_row":i,
          "hard_scale":scale,
          "q":q.tolist(),
          "q2":q2,
          "polarization_seed_pair":[19000+2*len(rows),19001+2*len(rows)],
          "partner_checks":partner})
q2s=np.array([r['q2'] for r in rows])
r2s=np.array([p['r2'] for r in rows for p in r['partner_checks']])
assert np.all(q2s>0)
assert np.all(r2s>0)
out={
 "iteration":190,
 "model_readiness_percent":24,
 "protocol_name":"RQIR-WITHHELD-NULLSOFT-12-v1",
 "status":"PREREGISTERED_WITHHELD_NOT_EVALUATED_ON_ANY_CANDIDATE",
 "selection_rule":"scale each of the six frozen hard q vectors by exactly 0.75 and 1.25; no use of residual/null-vector information",
 "soft_direction":k0.tolist(),
 "soft_steps":soft_steps,
 "hard_scales":scales,
 "rows":rows,
 "q2_range":[float(q2s.min()),float(q2s.max())],
 "partner_r2_range_over_all_soft_steps":[float(r2s.min()),float(r2s.max())],
 "all_hard_and_partner_legs_spacelike":True,
 "future_use_order":[
   "compute C5 local and K2-compensation columns",
   "compute fixed QG-NL-EXP-001 conditioned column",
   "apply same AS/C3 authority status or newly derived columns without retuning rows",
   "only then evaluate any future candidate residual"
 ],
 "classification":{
   "target_optimized":False,
   "candidate_evaluated":False,
   "left_null_used_for_selection":False,
   "protocol_extension":"FROZEN_PROSPECTIVELY",
   "ANSATZ_003":"NOT_CREATED",
   "Fisher_resources":"FORBIDDEN"
 },
 "retained_results":[
   "PROTO-NG-001 — WITHHELD_ROW_EXTENSION_FROZEN_BEFORE_ANY_CANDIDATE_TEST",
   "NUM-NG-005 — HARD_Q2_LEVER_ARM_EXPANDED_FROM_BASELINE_TO_0P162_0P793_WITHOUT_TARGET_OPTIMIZATION",
   "NG-FUNNEL-045 — FUTURE_RESIDUAL_MUST_SURVIVE_PROSPECTIVELY_FROZEN_ROW_EXTENSION"
 ],
 "readiness_change":"unchanged: a prospective robustness protocol is frozen, but it has not yet closed a comparator or residual rubric point"
}
Path('results/preregistered_withheld_row_extension_iteration190.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
