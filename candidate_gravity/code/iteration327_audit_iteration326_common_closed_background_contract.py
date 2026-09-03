#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 327.

Fail-closed authority audit of Iteration 326 before physical determinant-trace
assembly.  Iteration 324 routes denominators on the Iteration-322 closed triad.
For Iteration 326 to certify the corresponding physical numerator layer, both
H and N insertion factories must use that same closed triad and the same
background metric modes, while only the incoming loop momentum is shifted per
route.

This audit does not change any frozen physical kernel or threshold.  It checks
source contracts exactly and narrows the interpretation of Iteration 326 if the
common-background condition is not met.
"""
from __future__ import annotations
import json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
p326=ROOT/'iteration326_det_full_cubic_topology_incoming_momentum_gate.py'
p319=ROOT/'iteration319_det_graviton_three_mode_routing.py'
p317=ROOT/'iteration317_det_ghost_three_mode_routing.py'
p322=ROOT/'iteration322_det_closed_triad_cubic_coefficient.py'
s326=p326.read_text(); s319=p319.read_text(); s317=p317.read_text(); s322=p322.read_text()

Q_CLOSED=[
 [0.27,-0.19,0.31,0.11],
 [-0.13,0.37,0.17,-0.29],
 [-0.14,-0.18,-0.48,0.18],
]

def extract_qs(src:str):
    m=re.search(r'qs\s*=\s*\[(.*?)\]\s*\np\s*=',src,re.S)
    if not m: raise RuntimeError('qs fixture not found')
    vals=[float(x) for x in re.findall(r'(?<![A-Za-z_])[-+]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+]?\d+)?',m.group(1))]
    # np.array contributes no numeric tokens; three D=4 modes => 12 values.
    if len(vals)!=12: raise RuntimeError(f'unexpected qs token count: {len(vals)}')
    return [vals[0:4],vals[4:8],vals[8:12]]

def maxdiff(a,b):
    return max(abs(a[r][mu]-b[r][mu]) for r in range(3) for mu in range(4))

q319=extract_qs(s319); q317=extract_qs(s317)
q319_match=maxdiff(q319,Q_CLOSED)==0.0
q317_match=maxdiff(q317,Q_CLOSED)==0.0

# Iteration 326 loads the two independent historical fixture files directly.
loads_319="iteration319_det_graviton_three_mode_routing.py" in s326
loads_317="iteration317_det_ghost_three_mode_routing.py" in s326
# Its loader rewrites p only.  No external-mode qs or background hs rebinding is present.
p_rebind=bool(re.search(r"re\.subn\(r'\^p=np\\\.array",s326))
qs_rebind=('failed to replace qs fixture' in s326 or "replace(old_q" in s326 or 'Q_CLOSED' in s326)
hs_rebind=('common_background' in s326 or 'shared_background' in s326 or 'iteration320_det_shared_background' in s326)

seed319=('default_rng(319)' in s319); seed317=('default_rng(317)' in s317)
scale319=('0.12*(x+x.T)/2' in s319); scale317=('0.2*(x+x.T)/2.0' in s317)
independent_background_generators=bool(seed319 and seed317 and scale319 and scale317)

# Iteration 322 is the already-authoritative precedent for the required contract:
# it explicitly replaces q3 by closure before the shared-background H/N assembly.
iter322_rebinds_closed_q3=('q3=-(q1+q2)' in s322 and 's319=s319.replace(old,new)' in s322)
iter322_uses_shared_parent=('iteration320_det_shared_background_cubic_coefficient.py' in s322)

common_closed_contract=bool(
    loads_319 and loads_317 and p_rebind and
    q319_match and q317_match and qs_rebind and hs_rebind
)
# The expected finding is that the common closed-background certificate is NOT
# established by Iteration 326.  The audit itself is successful when all source
# evidence is readable and the mismatch is explicit.
audit_execution_pass=bool(loads_319 and loads_317 and p_rebind and independent_background_generators and iter322_rebinds_closed_q3 and iter322_uses_shared_parent)
scientific_gate_pass=bool(common_closed_contract)
classification=(
 'PASS_ITERATION326_COMMON_CLOSED_TRIAD_BACKGROUND_CONTRACT'
 if scientific_gate_pass else
 'FAIL_SCOPED_GATE_DESIGN_ITERATION326_NOT_COMMON_CLOSED_TRIAD_BACKGROUND'
)

result={
 'iteration':327,
 'model_readiness_percent':24,
 'audit_execution_pass':audit_execution_pass,
 'scientific_gate_pass':scientific_gate_pass,
 'classification':classification,
 'candidate_residual':False,
 'authority_audited':{
   'denominator_routing':'ITERATION_324_CLOSED_TRIAD',
   'numerator_routing':'ITERATION_326',
   'shared_background_precedent':'ITERATION_322',
 },
 'checks':{
   'iteration326_loads_graviton319_directly':loads_319,
   'iteration326_loads_ghost317_directly':loads_317,
   'iteration326_rebinds_incoming_p':p_rebind,
   'iteration326_rebinds_external_qs_to_closed_triad':qs_rebind,
   'iteration326_rebinds_H_and_N_to_one_shared_background_hs':hs_rebind,
   'iteration319_qs_equal_iteration322_closed_triad':q319_match,
   'iteration317_qs_equal_iteration322_closed_triad':q317_match,
   'iteration317_and_319_use_independent_background_generators':independent_background_generators,
   'iteration322_explicitly_rebinds_closed_q3':iter322_rebinds_closed_q3,
   'iteration322_uses_shared_HN_parent_assembly':iter322_uses_shared_parent,
   'common_closed_background_contract_established':common_closed_contract,
 },
 'fixture_differences':{
   'closed_triad_q':Q_CLOSED,
   'iteration319_q':q319,
   'iteration317_q':q317,
   'max_abs_q_difference_iteration319_vs_closed':maxdiff(q319,Q_CLOSED),
   'max_abs_q_difference_iteration317_vs_closed':maxdiff(q317,Q_CLOSED),
   'graviton_background_generator':'rng seed 319; h scale 0.12',
   'ghost_background_generator':'rng seed 317; h scale 0.2',
 },
 'scientific_interpretation':{
   'iteration326_retained_scope':'arbitrary-incoming-p validation of the historical H and N fixture kernels, including full 1+6+6 topology coverage',
   'iteration326_not_certified_as':'common-background closed-triad physical numerator certificate compatible with Iteration-324 denominator routes',
   'physical_HN_kernel_consistency_fail':False,
   'candidate_gravity_consistency_fail':False,
   'operational_failure':False,
   'typed_result':'SCOPED_GATE_DESIGN_FAIL_AND_DEPENDENT_PHYSICAL_TRACE_BLOCKED',
 },
 'guardrails':[
   'ITERATION326_NOT_RETROACTIVELY_EDITED',
   'DO_NOT_COMBINE_DENOMINATORS_AND_NUMERATORS_FROM_DIFFERENT_BACKGROUND_FIXTURES',
   'ONE_SHARED_BACKGROUND_FOR_GRAVITON_AND_GHOST',
   'NO_THRESHOLD_WEAKENING',
   'NO_SOURCE_BORN_SUBTRACTION',
   'NO_ANSATZ003','NO_FISHER_RESOURCES','NO_BLIND_HEAVY_FULL_C5'
 ],
 'next_gate':'create a new gate version from the Iteration-322 common closed-triad background: rebind both external qs and incoming p for the graviton factory, reconstruct ghost N on exactly the same hs/qs/p parent as Iteration 320, and revalidate all 19 full-cubic routed insertion requests against same-parent exact geometry before determinant trace assembly'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not audit_execution_pass:
    raise SystemExit(3)
# The audit found a scoped certificate failure by design; preserve diagnostics
# without conflating it with an execution failure.
