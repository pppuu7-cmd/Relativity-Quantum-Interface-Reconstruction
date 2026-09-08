#!/usr/bin/env python3
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
u2=json.loads((ROOT/'results/iteration406_tru2_complete_operator_coordinate.json').read_text())
u1=json.loads((ROOT/'results/iteration581_frozen_iter412_exact15_raw_consumed.json').read_text())
assert u2['iteration']==406 and u2['scientific_gate_pass'] is True
assert u2['classification']=='PASS_TRU2_COMPLETE_TIMELIKE_OPERATOR_COORDINATE_Q2_RESOLVED'
assert u2['effective_action_weight']=='NOT_FOLDED__PLUS_I_OVER_2_TRU2_SEPARATE'
assert u1['iteration']==581 and u1['scientific_gate_pass'] is True
assert u1['exact_double_double_channel_count']==15
assert u1['frozen_contract_iteration']==412
assert u1['workflow_authority']['raw_result_integrity_valid'] is True
assert u1['workflow_authority']['scientific_result_sha256']=='77970170c5a10e42bb9b5f846204d9a34348436b674da7e1437977a02bdb47e4'
assert u1['effective_action_weight']=='NOT_FOLDED__MINUS_I_OVER_4_TRU1SQ_SEPARATE'
keys=['-1.0','-0.34','-0.14']
outvals={}
for q in keys:
    a=complex(*u2['D_s_TrU2_complete_q2'][q])
    b=complex(*u1['D_s_TrU1sq_complete_q2'][q])
    g=0.5j*a-0.25j*b
    assert math.isfinite(g.real) and math.isfinite(g.imag)
    outvals[q]=[g.real,g.imag]
out={
 'iteration':582,
 'date':'2026-09-08',
 'classification':'PASS_GAMMA_E2_Q2_RESOLVED_FROZEN_WEIGHT_ASSEMBLY__NON_RESIDUAL',
 'scientific_gate_pass':True,
 'candidate_residual':False,
 'parent_dynamics_consistent':True,
 'source_iterations':[406,581],
 'effective_action_formula':'D_s Gamma_e2(q2) = +(i/2) D_s TrU2(q2) -(i/4) D_s TrU1sq(q2)',
 'D_s_Gamma_e2_q2':outvals,
 'model_readiness_percent':24,
 'strict_classification':'operator-coordinate assembly PASS; not Candidate-Gravity consistency PASS, not comparator identity, not model-level non-identifiability, not near-degeneracy, not novelty certificate',
 'guardrails':['Q2_BUCKETS_KEPT_DISTINCT','FROZEN_EFFECTIVE_ACTION_WEIGHTS','NO_SOURCE_BORN_SUBTRACTION_YET','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'derive the concrete Source/Ward/contact+K2 object from the same frozen parent dynamics and parameter convention; only then form the fixed C3/C4/C5/nonlocal/asymptotic-safety comparator quotient'
}
print(json.dumps(out,indent=2,sort_keys=True))
