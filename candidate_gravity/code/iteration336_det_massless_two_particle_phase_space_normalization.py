#!/usr/bin/env python3
"""RQIR Iteration 336: exact 4D massless two-particle phase-space normalization.

Independent of Iteration 335 angular-convergence work.  This gate freezes only the
geometric phase-space normalization that converts the repository's normalized
sphere mean (1/4pi) int dOmega F into the standard Lorentz-invariant two-particle
phase-space integral.  It deliberately does NOT freeze the overall Cutkosky Disc
sign/i convention, which depends on the exact loop-measure/propagator convention
of the matched observable and must be audited separately.

Signature used by Candidate Gravity is (-,+,+,+).  In the timelike rest frame,
Q=(M,0), M=sqrt(-Q^2)>0.  For two massless positive-energy cut lines:

  dPhi_2 = [d^4 l/(2pi)^4] (2pi) delta_+(l^2)
            (2pi) delta_+((Q-l)^2)
          = dOmega/(32 pi^2),

hence int dPhi_2 = 1/(8 pi), and if sphere_mean=(1/4pi) int dOmega F,

  int dPhi_2 F = sphere_mean/(8 pi).
"""
from __future__ import annotations
import json, math
from fractions import Fraction

# Exact Jacobian bookkeeping in the Q rest frame.
# (2pi)^2/(2pi)^4 = 1/(4 pi^2).
loop_2pi_rational = Fraction(1,4)
# delta_+(l^2) -> delta(l0-r)/(2r),
# delta_+((Q-l)^2) -> delta(M-l0-r)/(2r).
# r^2 dr dl0 times both factors gives (1/4) dr; delta(M-2r) gives 1/2.
radial_delta_jacobian = Fraction(1,8)
# Therefore dPhi2/dOmega = 1/(32 pi^2).
angular_rational = loop_2pi_rational * radial_delta_jacobian
assert angular_rational == Fraction(1,32)
# Integrating 4pi solid angle gives 1/(8pi).
total_rational_over_pi = Fraction(1,8)
# A normalized sphere mean multiplies exactly by the same total phase-space factor.
mean_to_phase_space_rational_over_pi = Fraction(1,8)

numeric_dphi_per_domega = float(angular_rational) / (math.pi**2)
numeric_total = float(total_rational_over_pi) / math.pi
numeric_mean_factor = float(mean_to_phase_space_rational_over_pi) / math.pi

# Internal consistency: (1/(32pi^2))*4pi == 1/(8pi).
closure_error = abs(numeric_dphi_per_domega * 4.0 * math.pi - numeric_total)

result = {
    "iteration": 336,
    "model_readiness_percent": 24,
    "scientific_gate_pass": closure_error < 1e-15,
    "classification": "PASS_EXACT_4D_MASSLESS_TWO_PARTICLE_PHASE_SPACE_NORMALIZATION",
    "candidate_residual": False,
    "signature": "(-,+,+,+)",
    "scope": "geometric Lorentz-invariant two-massless-particle cut phase-space normalization only",
    "derivation": {
        "loop_2pi_factor": "1/(4*pi^2)",
        "radial_and_delta_jacobian": "1/8",
        "dPhi2_per_dOmega": "1/(32*pi^2)",
        "integrated_dPhi2": "1/(8*pi)",
        "normalized_sphere_mean_to_phase_space": "1/(8*pi)"
    },
    "numeric": {
        "dPhi2_per_dOmega": numeric_dphi_per_domega,
        "integrated_dPhi2": numeric_total,
        "normalized_sphere_mean_factor": numeric_mean_factor,
        "closure_error": closure_error
    },
    "authority_boundary": {
        "frozen": "geometric phase-space factor multiplying Iteration-333/335 normalized angular means",
        "not_frozen": "overall Cutkosky discontinuity sign, i factors, loop prefactor and matched-observable normalization",
        "reason": "those depend on exact propagator/effective-action convention and require explicit provenance audit"
    },
    "guardrails": [
        "NO_USE_OF_ITERATION335_RESULT",
        "NO_CHANGE_TO_PARENT_DYNAMICS_OR_NUMERATORS",
        "NO_CUTKOSKY_SIGN_ASSUMPTION",
        "NO_ANSATZ003",
        "NO_FISHER_RESOURCES",
        "ITERATION297_FINITE_DR_WARNING_REMAINS_BINDING"
    ],
    "next_gate": "audit exact loop-measure/propagator/i convention and then combine with the complete channel-resolved absorptive vector once Iteration 335 resolves or is analytically replaced"
}
print(json.dumps(result, indent=2, sort_keys=True))
if not result["scientific_gate_pass"]:
    raise SystemExit(2)
