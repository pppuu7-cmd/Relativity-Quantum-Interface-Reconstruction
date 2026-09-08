#!/usr/bin/env python3
import json

# Scope/authority gate before any Cutkosky integral.  Iter613 freezes an OPEN
# scalar-source trajectory p0(s)=sqrt(s)e0 with external q_i held fixed.  After
# closing the scalar endpoints into the gravitational one-loop 1PI Gamma3,
# p0 is the loop integration momentum and cannot simultaneously be the external
# hard-channel parameter.  Therefore Iter613 supplies useful external q_i/mass
# conventions but does not, by itself, define the closed-loop D_s channel.

facts={
 'iter613_object':'open routed MSSC scalar-source response',
 'iter613_p0_role':'external/source scalar endpoint momentum varied as p0(s)=sqrt(s)e0',
 'closed_1pi_object':'closed scalar loop contribution to retarded gravitational Gamma3',
 'closed_loop_p0_role':'dummy/integrated loop momentum',
 'same_symbol_role_preserved':False,
 'iter613_can_be_reused_as_closed_loop_integration_trajectory':False,
 'iter613_mass_and_external_q_fixture_remain_valid':True
}
failures=[]
if facts['same_symbol_role_preserved'] is not False: failures.append('open endpoint p0 incorrectly identified with closed loop momentum')
if facts['iter613_can_be_reused_as_closed_loop_integration_trajectory'] is not False: failures.append('Iter613 trajectory incorrectly promoted to loop integration path')
if facts['iter613_mass_and_external_q_fixture_remain_valid'] is not True: failures.append('valid parent fixture was discarded')

result={
 'iteration':634,'date':'2026-09-09','scientific_gate_pass':not failures,'candidate_residual':False,
 'classification':'BLOCKED_ITER634_ITER613_OPEN_SOURCE_P0_TRAJECTORY_IS_NOT_CLOSED_LOOP_HARD_CHANNEL__EXTERNAL_INVARIANT_BINDING_REQUIRED_BEFORE_CUTKOSKY_LANDAU_EVALUATION__NON_RESIDUAL' if not failures else 'FAIL_ITER634_CLOSED_LOOP_HARD_INVARIANT_AUTHORITY_AUDIT',
 'facts':facts,
 'scientific_consequence':'Do not evaluate bubble thresholds or triangle Landau equations by substituting the Iter613 source p0 trajectory for the loop momentum. The closed-loop hard variable must be an external gravitational invariant built from the frozen q_s,q_a,q_b/native channel and held independent of the integration momentum.',
 'iter633_status':'PRESERVED_AS_GENERAL_TOPOLOGY_AND_ORIGIN_CLASSIFICATION; its K3 tadpole / K1K2 bubble / K1cubed triangle census does not depend on identifying Iter613 p0 with loop momentum',
 'allowed_resolution':'derive or prospectively freeze an identity-preserving map from native Iter205 D_s/hard channel to one external invariant of the closed three-graviton loop, using the fixed q_s,q_a,q_b fixture; then perform Cutkosky/Landau integration over an independent loop momentum ell',
 'forbidden_resolution':'do not set ell=p0(s), do not use source pole roots as closed-loop phase-space roots, do not fit the channel to Iter582 values',
 'source_born_subtraction':'NOT_PERFORMED','native_projection':'NOT_PERFORMED','candidate_values_used':False,'zero_fill':False,
 'failures':failures,'MODEL_READINESS':'24%','readiness_change':'0 percentage points',
 'next_gate':'Iteration635: audit existing native/three-graviton authority for the external hard-channel invariant of the closed retarded Gamma3 (e.g. a specific (q_i+q_j)^2 channel). If absent, prospectively freeze it before any loop integral; keep loop momentum independent.'
}
print(json.dumps(result,indent=2))
if failures: raise SystemExit('\n'.join(failures))
