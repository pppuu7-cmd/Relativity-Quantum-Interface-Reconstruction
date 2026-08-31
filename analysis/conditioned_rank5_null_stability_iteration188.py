#!/usr/bin/env python3
"""Iteration 188: target-independent stability audit of the unique left-null
functional of the currently supported conditioned comparator span span(V4,S_NL).

This is not a Candidate Gravity residual.  It asks whether the one algebraic
complement direction on six rows is numerically/geometrically robust enough to
serve as a future witness before AS/C3 completion.
"""
from pathlib import Path
import json, math
import numpy as np

r0=np.array([-1.6411697071822275,0.06385882717014456,0.8548821188463769,
             -0.17055215671317986,-0.3261917310634991,-0.1655609264695088])
x=np.array([0.5076,0.3854,0.4260,0.3153,0.4004,0.2882])
V4=np.column_stack([r0,-x*r0,x*x*r0,-x**3*r0])
Scond=np.array([4.690072651686453,0.27893263500829546,8.50174586368455,
                -3.006275167762978,-0.7364444751435104,-0.7232162208653979])
M=np.column_stack([V4,Scond])
U,s,Vt=np.linalg.svd(M,full_matrices=True)
w=U[:,-1]
if w[1]<0: w=-w
envelope=5.2625580e-6

# Fixed-seed perturbation stress test at the inherited absolute soft2 envelope.
rng=np.random.default_rng(187188)
angles=[]
for _ in range(5000):
    Mp=M+rng.normal(scale=envelope,size=M.shape)
    Up,sp,Vtp=np.linalg.svd(Mp,full_matrices=True)
    wp=Up[:,-1]
    if np.dot(wp,w)<0: wp=-wp
    c=float(np.clip(np.dot(wp,w),-1,1))
    angles.append(math.degrees(math.acos(c)))
angles=np.array(angles)

loo=[]
for i in range(6):
    Mi=np.delete(M,i,axis=0)
    si=np.linalg.svd(Mi,compute_uv=False)
    loo.append({"removed_row":i,"smallest_singular_value":float(si[-1]),
                "condition_number":float(si[0]/si[-1])})

out={
 "iteration":188,
 "model_readiness_percent":24,
 "scope":"six frozen conditioned soft2 rows; supported comparator span V4 plus QG-NL-EXP-001 lambda direction",
 "supported_rank":int(np.linalg.matrix_rank(M,tol=1e-10)),
 "singular_values":s.tolist(),
 "smallest_nonzero_singular_over_envelope":float(s[-1]/envelope),
 "left_null_unit_vector":w.tolist(),
 "max_null_orthogonality_error":float(np.max(np.abs(M.T@w))),
 "left_null_squared_row_weights":(w*w).tolist(),
 "dominant_row":int(np.argmax(w*w)),
 "dominant_row_weight_fraction":float(np.max(w*w)),
 "perturbation_test":{
   "seed":187188,"samples":5000,"entry_sigma":envelope,
   "median_angle_deg":float(np.median(angles)),
   "p95_angle_deg":float(np.quantile(angles,0.95)),
   "max_angle_deg":float(np.max(angles))},
 "leave_one_row_out":loo,
 "classification":{
   "unique_algebraic_complement":"EXISTS_DIMENSION_1_BEFORE_AS_C3_COMPLETION",
   "candidate_residual":"NOT_ESTABLISHED",
   "null_geometry":"ROW_DOMINATED_AND_NOT_YET_ROBUST_WITNESS",
   "protocol_extension":"REQUIRED_TARGET_INDEPENDENTLY_BEFORE_ANY_RESIDUAL_PROMOTION",
   "ANSATZ_003":"NOT_CREATED","Fisher_resources":"FORBIDDEN"},
 "retained_results":[
   "NUM-NG-004 — CURRENT_RANK5_LEFT_NULL_IS_94P7_PERCENT_DOMINATED_BY_ONE_FROZEN_ROW",
   "REL-NG-006 — ONE_DIMENSIONAL_ALGEBRAIC_COMPLEMENT_IS_NOT_A_ROBUST_RESIDUAL_CERTIFICATE_BEFORE_ROW_EXTENSION_AND_BLOCKED_COMPARATOR_COMPLETION",
   "NG-FUNNEL-043 — PREREGISTER_ROW_EXTENSION_BEFORE_TESTING_ANY_MODEL_AGAINST_THE_CURRENT_LEFT_NULL"
 ],
 "readiness_change":"unchanged: a unique algebraic complement exists, but its one-row domination makes it a design diagnostic rather than a promotable residual"
}
Path('results/conditioned_rank5_null_stability_iteration188.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
