#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 457.

Audit the four exact BASE/HALF coordinate overlaps in the frozen Iteration-407
central4 x central4 mixed-mass derivative. Precision certificates may be shared
for identical F(u,v) coordinates, but derivative occurrences must retain their
level-specific stencil weights.
"""
from fractions import Fraction
import json

BASE_H = Fraction(5, 10**6)
HALF_H = Fraction(25, 10**7)  # 2.5e-6 = BASE_H/2
C = [Fraction(1,12), Fraction(-8,12), Fraction(8,12), Fraction(-1,12)]
BASE_NODE_INDEX = {-1: 1, +1: 2}
HALF_NODE_INDEX = {-1: 0, +1: 3}
rows=[]
for su in (-1,+1):
    for sv in (-1,+1):
        ib, jb = BASE_NODE_INDEX[su], BASE_NODE_INDEX[sv]
        ih, jh = HALF_NODE_INDEX[su], HALF_NODE_INDEX[sv]
        wb = C[ib]*C[jb]/(BASE_H*BASE_H)
        wh = C[ih]*C[jh]/(HALF_H*HALF_H)
        rows.append({
            'coordinate_in_base_h_units':[su,sv],
            'base_indices':[ib,jb], 'half_indices':[ih,jh],
            'base_weight_times_base_h2':str(C[ib]*C[jb]),
            'half_weight_times_base_h2':str(4*C[ih]*C[jh]),
            'base_over_half_weight_ratio':str(wb/wh),
            'same_sign': (wb>0)==(wh>0),
        })
passed=all(r['base_over_half_weight_ratio']=='16' and r['same_sign'] for r in rows)
out={
 'iteration':457,
 'classification':'PASS_OVERLAP_PRECISION_SHARE_BUT_STENCIL_WEIGHT_COLLAPSE_FORBIDDEN__NON_PROMOTING' if passed else 'FAIL_OVERLAP_STENCIL_WEIGHT_AUDIT',
 'scientific_gate_pass':passed,
 'promotes_physical_coordinate':False,
 'MODEL_READINESS':'24%', 'readiness_change_pp':0,
 'frozen':{'central4_coefficients':['1/12','-2/3','2/3','-1/12'],'base_h':'5e-6','half_h':'2.5e-6','half_over_base_h':'1/2'},
 'observed':{'overlap_count':4,'rows':rows,'exact_weight_ratio_base_over_half':16},
 'claim':'Exact BASE/HALF coordinate overlaps may share one F(u,v) precision certificate, but BASE and HALF mixed-derivative occurrences cannot be merged because their central4xcentral4 weights differ by an exact factor 16.',
 'guardrails':['NO_FUV_EVALUATION','NO_ACTIVE_RUN_DUPLICATION','NO_THRESHOLD_CHANGE','NO_OCCURRENCE_DENOMINATOR_COLLAPSE','NO_PHYSICAL_DS_PROMOTION','NO_ANSATZ003','NO_FISHER_RESOURCES'],
 'next_gate':'raw-consume active run 33946347229 fail-closed; if PASS advance only to the next Iteration-455 manifest coordinate'
}
print(json.dumps(out,indent=2,sort_keys=True))
if not passed: raise SystemExit(2)
