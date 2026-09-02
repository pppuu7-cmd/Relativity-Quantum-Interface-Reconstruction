#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 272.

Translation/trace closure audit for the Iteration-270/271 open cubic B3 kernel.
No loop integration is attempted.

A translationally invariant operator trace of a Fourier kernel
    <p+K|B3|p>
contains the global delta distribution delta^(4)(K), with
    K = k_s+k_a+k_b.
Therefore an open fixed-p certificate at K != 0 proves only that the parent
kernel is not identically zero off the conservation surface.  It cannot by
itself establish a physical three-point comparator coordinate.
"""
import json
import numpy as np

ETA=np.diag([-1.,1.,1.,1.])
K_S=np.array([1.,0.,0.,1.])
K_A=np.array([.25,.6,.3,.15])
K_B_270=np.array([-.15,.2,.55,-.35])
K_TOTAL_270=K_S+K_A+K_B_270
K_B_CLOSED=-(K_S+K_A)
K_TOTAL_CLOSED=K_S+K_A+K_B_CLOSED


def msq(k):
    return float(k@ETA@k)

result={
  "iteration":272,
  "model_readiness_percent":24,
  "input_authority":[
    "Iteration 270 explicit nonzero routed open B3 kernel",
    "Iteration 271 open-B3 resolvent-rank census"
  ],
  "iteration270_total_shift":K_TOTAL_270.tolist(),
  "iteration270_total_shift_minkowski_square":msq(K_TOTAL_270),
  "iteration270_is_translation_closed":bool(np.max(np.abs(K_TOTAL_270))<1e-14),
  "trace_closure_identity":"Tr B3 Fourier sector carries (2pi)^4 delta^4(k_s+k_a+k_b)",
  "classification":"PASS_EXACT_TRANSLATION_TRACE_CLOSURE_GATE",
  "status_of_iteration270_nonzero":"VALID_OFF_CONSERVATION_SURFACE_PARENT_KERNEL_NONIDENTICAL_ZERO_CERTIFICATE; NOT_YET_PHYSICAL_THREE_POINT_NONZERO",
  "closed_test_kinematics":{
    "k_s":K_S.tolist(),
    "k_a":K_A.tolist(),
    "k_b":K_B_CLOSED.tolist(),
    "sum":K_TOTAL_CLOSED.tolist(),
    "k_s_sq":msq(K_S),
    "k_a_sq":msq(K_A),
    "k_b_sq":msq(K_B_CLOSED)
  },
  "operational_status":"BLOCKED_PHYSICAL_B3_NONZERO_UNTIL_K_SUM_ZERO_RERUN",
  "guardrails":[
    "DO_NOT_CALL_K_NONZERO_OPEN_KERNEL_A_PHYSICAL_THREE_POINT_COMPARATOR",
    "DO_NOT_APPLY_LOOP_TRACE_MASTER_REDUCTION_BEFORE_GLOBAL_MOMENTUM_CLOSURE",
    "ITERATION270_REMAINS_A_VALID_NONIDENTICAL_ZERO_CERTIFICATE_FOR_THE_PARENT_KERNEL"
  ],
  "next_gate":"rerun the exact Iteration-270 routed A/Q/B3 construction with k_b=-(k_s+k_a), independent TT polarization for b, and K=0; require nonzero B3 plus permutation/endpoint checks on the conservation surface before p-dependent integrand reconstruction"
}

assert not result["iteration270_is_translation_closed"]
assert np.max(np.abs(K_TOTAL_CLOSED))<1e-14
assert abs(result["closed_test_kinematics"]["k_s_sq"])<1e-14
print(json.dumps(result,indent=2,sort_keys=True))
