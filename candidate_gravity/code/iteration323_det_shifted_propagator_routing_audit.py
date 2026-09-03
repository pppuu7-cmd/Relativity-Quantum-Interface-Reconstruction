#!/usr/bin/env python3
"""RQIR Iteration 323: audit physical momentum routing in cubic determinant trace.

A physical functional trace of log K contains free inverse operators evaluated at
successive loop momenta between Fourier insertions. This gate inspects the frozen
Iteration-320/322 cubic assembly and fail-closed classifies whether those shifted
K0^{-1}(p+Q) propagators are explicit before denominator-family reduction.
"""
from __future__ import annotations
import json, pathlib, re
root=pathlib.Path(__file__).resolve().parents[2]
s=(root/'candidate_gravity/code/iteration320_det_shared_background_cubic_coefficient.py').read_text()
checks={
 'single_K0_inverse_assignment': bool(re.search(r'K0i\s*=\s*np\.linalg\.inv\(K\[ZERO\]\)',s)),
 'A_uses_single_K0_inverse': bool(re.search(r'A\s*=\s*\{a:K0i@K\[a\]',s)),
 'explicit_shifted_K0_inverse': bool(re.search(r'(K0|H0|N0).*(p\s*\+|qsum|shift)',s,re.I)),
 'pair_trace_present': 'np.trace(A[a]@A[b])' in s,
 'triple_trace_present': 'np.trace(A[a]@A[b]@A[c0])' in s,
}
shifted=checks['explicit_shifted_K0_inverse'] and not checks['A_uses_single_K0_inverse']
# PASS means the audit itself is authoritative; the physical reduction is BLOCKED when shifted=False.
result={
 'iteration':323,'model_readiness_percent':24,'scientific_gate_pass':True,
 'classification':('PASS_SHIFTED_PROPAGATOR_ROUTING_AUDIT__PHYSICAL_DENOMINATOR_ROUTING_PRESENT' if shifted else 'PASS_SHIFTED_PROPAGATOR_ROUTING_AUDIT__ITERATION322_COEFFICIENT_REMAINS_LOCAL_ROUTING_FIXTURE'),
 'audit_checks':checks,
 'physical_denominator_routing_ready':bool(shifted),
 'iteration322_status':('PHYSICAL_TRACE_INTEGRAND_ROUTING_READY' if shifted else 'MOMENTUM_CLOSED_LOCAL_OPERATOR_ROUTING_FIXTURE_ONLY'),
 'scientific_interpretation':('The cubic assembly explicitly carries the successive shifted free propagators required by the functional trace.' if shifted else 'The current cubic assembly multiplies every insertion by one K0^{-1}(p). Momentum closure is necessary but not sufficient: pair/triple functional-trace terms require K0^{-1} at successive p+Q routings. Therefore Iteration 322 is retained as a closed-triad local operator/routing certificate but is not yet a full loop-integrand determinant coefficient.'),
 'candidate_residual':False,
 'guardrails':['PRESERVE_ITERATION322_NUMERICAL_PASS','NO_RETROACTIVE_THRESHOLD_CHANGE','NO_DENOMINATOR_FAMILY_PROMOTION_WITHOUT_SHIFTED_PROPAGATORS','NO_SOURCE_BORN_SUBTRACTION','NO_ANSATZ003','NO_FISHER_RESOURCES','UNSUPPORTED_IS_BLOCKED_NOT_ZERO_FILLED'],
 'next_gate':('implement the cubic determinant functional trace with explicit successive K0^{-1}(p+Q) propagators for every ordered pair/triple routing on the closed triad, then enumerate denominator families and validate cyclic-routing equivalence' if not shifted else 'enumerate denominator families and classify pole/cut origin')
}
print(json.dumps(result,indent=2,sort_keys=True))
