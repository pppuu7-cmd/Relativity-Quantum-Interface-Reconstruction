#!/usr/bin/env python3
"""Iteration 651: fail-closed audit for a same-parent Born/source term in the
closed retarded gravitational Gamma3 observable.

The reconciled Iter650 raw gate says the definition is absent.  This audit asks
whether any already-frozen Born authority can legally fill that role.  It uses
only pre-existing authority and topology/normalization metadata; no Candidate or
comparator numerical values are inspected or fitted.
"""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]

def load(p):
    return json.loads((ROOT/p).read_text())

failures=[]

# Current same-parent / closed-retarded authorities.
d627=load('candidate_gravity/results/iteration627_combined_sk_contract.json')
d629=load('candidate_gravity/results/iteration629_open_vs_1pi_normalization_gate.json')
d630=load('candidate_gravity/results/iteration630_closed_retarded_loop_keldysh_gate.json')
d636=load('candidate_gravity/results/iteration636_closed_gamma3_invariant_family_contract.json')
d647=load('candidate_gravity/results/iteration647_pre645_normalization_history_audit.json')
d642=load('results/iteration642_same_parent_vertex_authority_audit/result.json')

# Historical Born controls, intentionally different observables.
d214=load('results/c5_fivepoint_ir_subtraction_iteration214.json')
d222=load('results/scalar_source_cut_born_factorization_iteration222.json')

if d627.get('contract_id')!='MSSC001-GRAVITY-SK-MEAS-V1': failures.append('Iter627 contract drift')
if d629.get('single_common_N_native_exists') is not False: failures.append('Iter629 topology result drift')
if 'exactly one G_K' not in d630.get('exact_consequence',''): failures.append('Iter630 closed-loop causal structure drift')
if d636.get('contract',{}).get('contract_id')!='MSSC001-CLOSED-GAMMA3-INV-FAMILY-V1': failures.append('Iter636 invariant-family drift')
if d642.get('machine_recoverable') is not True: failures.append('Iter642 vertex authority missing')
if d647.get('authority_conclusion',{}).get('complete_pre_result_binding_found') is not False: failures.append('Iter647 provenance conclusion drift')

# Old Born results are controls, not the missing closed-Gamma3 Born object.
iter214_scope_ok=('Pure-Einstein five-graviton' in d214.get('protocol',''))
iter222_scope_ok=(d222.get('source_model_id')=='MSSC-001' and 'R_in = R_out = -8 * M_Born' in d222.get('common_relation',''))
if not iter214_scope_ok: failures.append('Iter214 scope drift')
if not iter222_scope_ok: failures.append('Iter222 scope drift')

# The missing authority is a committed same-parent closed-retarded Gamma3 Born
# contribution with CTP/Legendre normalization.  None of the audited objects is
# that object: Iter214 is pure-Einstein five-graviton; Iter222 is an open
# scalar+graviton source-cut with stripped overall normalization; Iter627 is an
# open scalar-probe G_R response; Iter629 proves it is not proportional to the
# closed 1PI topology; Iter630/636/642 define the closed loop but not a Born
# subtraction term; Iter647 proves the absolute pre-result normalization gap.
missing=True

classification=(
 'BLOCKED_ITER651_HISTORICAL_BORN_AUTHORITIES_TOPOLOGY_OR_OBSERVABLE_MISMATCHED__SAME_PARENT_CLOSED_RETARDED_GAMMA3_BORN_TERM_UNDEFINED__TERMINAL_PREREQUISITE_NON_RESIDUAL'
 if not failures and missing else
 'BLOCKED_ITER651_AUTHORITY_INPUT_DRIFT__NON_RESIDUAL'
)

result={
 'iteration':651,
 'date':'2026-09-09',
 'MODEL_READINESS':'24%',
 'readiness_change':'0 percentage points',
 'classification':classification,
 'scientific_gate_pass':not failures,
 'candidate_residual':False,
 'same_parent_closed_retarded_gamma3_born_defined':False,
 'audited_authorities':{
   'Iter214':{'observable':'pure-Einstein five-graviton total-s cut','born_role':'beam IR subtraction coefficient A=-2i M5','eligible_as_closed_MSSC_Gamma3_Born':False},
   'Iter222':{'observable':'connected MSSC scalar+graviton source cut','born_role':'collinear residue factorization R=-8 M_Born','overall_normalization':'stripped','eligible_as_closed_MSSC_Gamma3_Born':False},
   'Iter627':{'observable':'open retarded scalar probe G_phi^{ra}=G_R','eligible_as_closed_1PI_Born':False},
   'Iter629':{'open_family_totals':[-1,6,-6],'closed_1PI_family_totals':[1,-3,2],'open_over_closed':[-1,-2,-3],'single_common_scale_proxy':False},
   'Iter630':{'closed_retarded_loop_requires':'exactly one G_K per family','Born_term_defined':False},
   'Iter636':{'closed_Gamma3_invariant_family_defined':True,'Born_term_defined':False},
   'Iter642':{'same_parent_K1_K2_K3_vertices_machine_recoverable':True,'Born_term_defined':False},
   'Iter647':{'complete_pre_result_absolute_binding_found':False,'permanent_for_computed_absolute_branch':True}
 },
 'terminal_prerequisite_meaning':(
   'The present matched Source/Born branch cannot lawfully proceed from committed authority. '
   'A new prospective derivation must define the Born/source contribution inside the same closed retarded gravitational Gamma3 observable from the doubled MSSC001 functional itself; importing Iter214, Iter222, or the Iter627 open response would change observable/topology or normalization.'
 ),
 'source_born_subtraction':'NOT_PERFORMED',
 'native_Y_Tcut_projection':'NOT_PERFORMED',
 'comparator_quotient':'NOT_PERFORMED',
 'candidate_values_used':False,
 'normalization_fit':False,
 'zero_fill':False,
 'ANSATZ_003':'FORBIDDEN',
 'Fisher_resources':'FORBIDDEN',
 'failures':failures,
 'next_gate':(
   'Independent constructive authority only: derive prospectively, from the doubled MSSC001 CTP/Legendre functional, a same-parent closed-retarded-Gamma3 Born/source term with explicit topology, CTP component, coupling/loop normalization and pole/cut origin before subtraction. If such a term is not mathematically part of the chosen observable, version the matched observable/protocol rather than importing an open-response proxy.'
 )
}

out=ROOT/'results/iteration651_same_parent_closed_gamma3_born_authority_audit'
out.mkdir(parents=True,exist_ok=True)
(out/'result.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
if failures: raise SystemExit(2)
