#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 347.

Fail-closed compatibility/rebase gate between the frozen U2 component authorities
(Iterations 339, 341, 342, 345, 346) and the direct-timelike closed triad frozen
by Iteration 332.

This gate does NOT manufacture physical Tr U2 numerators. It establishes the
exact matched-fixture specialization that the next physical substitution gate
must use, and refuses promotion if any binding source convention has drifted.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path
import numpy as np

ITERATION=347
ROOT=Path(__file__).resolve().parent
files={
 'green339':ROOT/'iteration339_e2c1_u2_graviton_green_bridge.py',
 'A341':ROOT/'iteration341_u2_v1_a12_same_parent_geometry.py',
 'NY342':ROOT/'iteration342_u2_ny_inverse_routing_bridge.py',
 'route346':ROOT/'iteration346_u2_complete_12_route_operator_assembly.py',
}
missing=[k for k,p in files.items() if not p.exists()]
texts={k:p.read_text() for k,p in files.items() if p.exists()}
sha={k:hashlib.sha256(t.encode()).hexdigest() for k,t in texts.items()}

# Exact closed timelike triad frozen by Iteration 332 in signature (-,+,+,+).
eta=np.diag([-1.,1.,1.,1.])
q={
 'q1':np.array([1.0,0.0,0.0,0.0]),
 'q2':np.array([-0.4,0.1,0.1,0.0]),
 'q3':np.array([-0.6,-0.1,-0.1,0.0]),
}
closure=q['q1']+q['q2']+q['q3']
q2={k:float(v@eta@v) for k,v in q.items()}
closure_err=float(np.max(np.abs(closure)))
all_timelike=all(v < 0.0 for v in q2.values())
expected_q2={'q1':-1.0,'q2':-0.14,'q3':-0.34}
q2_err=max(abs(q2[k]-expected_q2[k]) for k in expected_q2)

required={
 'green339':[
   'G1 = -G0_out @ K1 @ G0_in',
   'iteration319_det_graviton_three_mode_routing.py',
 ],
 'A341':[
   "primary_authority':'Giacchini-de Paula Netto-Shapiro 2020 arXiv:2006.04217v4 Eqs.54-55'",
   "'A':'field x ghost (10x4)'",
   "'V1_L':'A.T (4x10)'",
   "'V1_R':'A (10x4)'",
 ],
 'NY342':[
   'Q1=-Q0pq@N1@Q0p',
   'Yup0=-eta',
   'Ylow0=-eta',
   'Nupper_from_QY=Q_direct@Yup',
 ],
 'route346':[
   "ORDER=('NL','AT','H','AR','NR','Y')",
   'return AR(key,-np.asarray(k)-Q).T',
   "assert len(brute_survivors)==12 and len(brute_killed)==18",
 ],
}
source_checks={k:{needle:(needle in texts.get(k,'')) for needle in needles}
               for k,needles in required.items()}
source_ok=(not missing and all(all(v.values()) for v in source_checks.values()))

# Binding specialization inherited by every physical provider.
contract={
 'D':4,
 'Lambda':0,
 'a':'-1/2',
 'metric_signature':'(-,+,+,+)',
 'metric_split':'g=eta+h',
 'u2_order':['NL','AT','Hinv_VD','AR','NR','Y'],
 'Hinv_VD':'-K^-1',
 'functional_transpose':'AT(Q;k)=AR(Q;-k-Q)^T',
 'incoming_momentum_rule':'each factor evaluated at cumulative loop momentum p+Q_before_factor',
 'external_fixture':{k:v.tolist() for k,v in q.items()},
 'external_invariants':q2,
 'route_count':12,
 'singleton_soft_kills':18,
}

# Critical scientific point: the old executable component tests are authority
# for formulas/conventions, not permission to copy numerical matrices from their
# historical random fixtures. The physical substitution must re-specialize the
# same frozen formulas on this timelike triad.
provider_rebase={
 'A1_A2':'REEVALUATE_FROZEN_ITERATION341_FORMULA_ON_ITERATION332_TIMELIKE_MODES',
 'NY':'REEVALUATE_FROZEN_ITERATION342_PARENT_GHOST_GREEN_AND_Y_ON_SAME_MODES',
 'Hinv':'REEVALUATE_FROZEN_ITERATION339_SHIFTED_GREEN_ON_SAME_MODES_AND_ROUTE_MOMENTA',
 'routes':'USE_EXACT_ITERATION346_12_ROUTE_PLACEMENT_AND_ITERATION345_FUNCTIONAL_TRANSPOSE',
 'copy_historical_fixture_matrices':'FORBIDDEN',
}

thresholds={'closure_abs_max':1e-15,'q2_abs_max':1e-14}
passed=bool(source_ok and closure_err<=thresholds['closure_abs_max'] and
            q2_err<=thresholds['q2_abs_max'] and all_timelike)
classification=(
 'PASS_U2_MATCHED_TIMELIKE_PHYSICAL_COMPONENT_REBASE_CONTRACT__12_ROUTE_SUBSTITUTION_AUTHORIZED_NEXT'
 if passed else
 'BLOCKED_U2_MATCHED_TIMELIKE_REBASE_CONTRACT_SOURCE_OR_FIXTURE_DRIFT'
)
result={
 'iteration':ITERATION,
 'model_readiness_percent':24,
 'scientific_gate_pass':passed,
 'classification':classification,
 'candidate_residual':False,
 'scope':'MATCHED_TIMELIKE_REBASE_CONTRACT_ONLY__NO_PHYSICAL_TRU2_NUMERATOR_YET',
 'source_files_sha256':sha,
 'missing_sources':missing,
 'source_convention_checks':source_checks,
 'timelike_fixture':{'closure_error':closure_err,'q2_error':q2_err,'all_timelike':all_timelike},
 'binding_contract':contract,
 'physical_provider_rebase':provider_rebase,
 'thresholds':thresholds,
 'status':{
   'matched_fixture_contract':'FROZEN' if passed else 'BLOCKED',
   'physical_12_route_substitution':'AUTHORIZED_NEXT' if passed else 'BLOCKED',
   'TrU2_cut_integration':'FORBIDDEN_UNTIL_PHYSICAL_FAMILY_REDUCTION_PASS',
 },
 'guardrails':[
   'UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED',
   'NO_COPY_OF_HISTORICAL_RANDOM_FIXTURE_MATRICES',
   'NO_CUT_INTEGRATION_FROM_OPERATOR_ROUTE_PASS_ALONE',
   'NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_FULL_C5'],
 'next_gate':(
   're-specialize frozen A1/A2, N/Y and shifted Hinv providers on the exact Iteration-332 timelike triad; substitute route-by-route into all 12 Iteration-346 survivors and canonicalize physical numerator/denominator families before any cut integration'
   if passed else
   'preserve BLOCKED and repair only the detected source/fixture drift without weakening frozen conventions')
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed:
    raise SystemExit(2)
