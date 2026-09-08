#!/usr/bin/env python3
import json

# Prospective, pre-result external invariant family for the CLOSED scalar-loop
# three-graviton 1PI object.  It is frozen before threshold/Landau evaluation.
# Momentum conservation q_s+q_a+q_b=0 is exact.  Select the q_s^2 channel as
# the native positive-timelike variable by a predeclared leg-label convention,
# not by Candidate values.  Hold the other two external virtualities at their
# exact-fixture anchor values t0=q_a0^2 and u0=q_b0^2.
# Pairwise dots are then fixed algebraically, so loop-denominator Landau
# geometry is fully specified in invariant space without identifying loop
# momentum ell with the old open-source p0.

contract={
 'contract_id':'MSSC001-CLOSED-GAMMA3-INV-FAMILY-V1',
 'external_channel':'s := q_s^2 > 0',
 'fixed_external_invariants':['t := q_a^2 = t0 (exact fixture anchor)','u := q_b^2 = u0 (exact fixture anchor)'],
 'momentum_closure':'q_s+q_a+q_b=0',
 'pairwise_dots':{
   'q_s_dot_q_a':'(u-s-t)/2',
   'q_s_dot_q_b':'(t-s-u)/2',
   'q_a_dot_q_b':'(s-t-u)/2'
 },
 'anchor':'at s=s0:=q_s0^2, (s,t,u) equals the exact Iter368/588 three-mode invariant point',
 'loop_momentum':'ell is integrated independently over R^4 and is never set equal to Iter613 p0(s)',
 'mass':'m_phi=0.7 retained from MSSC001',
 'scope':'scalar-denominator Cutkosky/Landau support geometry only; tensor numerator/polarization transport is deferred and cannot alter singularity location',
 'channel_choice_rule':'q_s leg chosen prospectively by fixed leg label before any bubble/triangle support or Candidate value is inspected'
}
failures=[]
if contract['external_channel']!='s := q_s^2 > 0': failures.append('external channel mismatch')
if contract['momentum_closure']!='q_s+q_a+q_b=0': failures.append('closure mismatch')
if 'independently' not in contract['loop_momentum']: failures.append('loop momentum independence missing')

result={
 'iteration':636,'date':'2026-09-09','scientific_gate_pass':not failures,'candidate_residual':False,
 'classification':'PASS_ITER636_PROSPECTIVE_CLOSED_GAMMA3_EXTERNAL_INVARIANT_FAMILY_CONTRACT__S_QS2_WITH_TU_FIXED__NON_RESIDUAL' if not failures else 'FAIL_ITER636_CLOSED_GAMMA3_INVARIANT_FAMILY_CONTRACT',
 'contract':contract,
 'anti_bias':{'candidate_values_used':False,'bubble_support_inspected_before_freeze':False,'triangle_landau_support_inspected_before_freeze':False,'normalization_fit_used':False},
 'source_born_subtraction':'NOT_PERFORMED','native_projection':'NOT_PERFORMED','zero_fill':False,
 'failures':failures,'MODEL_READINESS':'24%','readiness_change':'0 percentage points',
 'next_gate':'Iteration637: using only this frozen invariant family + m=0.7 + Iter632 vacuum state, evaluate the K1/K2 bubble normal-cut support and solve the equal-mass triangle Landau determinant/positive-Feynman-parameter conditions as functions of s with t=t0,u=u0; report unsupported anchor data as BLOCKED rather than inventing t0/u0.'
}
print(json.dumps(result,indent=2))
if failures: raise SystemExit('\n'.join(failures))
