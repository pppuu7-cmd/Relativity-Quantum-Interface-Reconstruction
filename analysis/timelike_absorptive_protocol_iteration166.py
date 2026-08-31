#!/usr/bin/env python3
"""Iteration 166: causal/timelike absorptive protocol outside finite spacelike-TT interpolation.

This script freezes a target-independent positive/negative-frequency TT source-response
pre-protocol and studies the odd absorptive projection

    A_odd(s) = [Im chi_R(+omega)-Im chi_R(-omega)]/(2*pi),  s=omega^2>0.

The key theorem-level distinction is analytic rather than fit-based:

* any real local Hermitian tree-level EFT contribution is analytic/meromorphic and has
  zero off-pole absorptive part;
* a massless-loop logarithm has L_R(+omega)=log(-s-i0)=log(s)-i*pi and the opposite
  branch at negative frequency, producing a non-zero odd absorptive direction.

The leading C5 inverse-kernel structure is represented schematically as

    K_R(s)=s [1 + ell*s*L_R(s)]

so at first order d chi_R/d ell = -L_R.  Only the shape is used for the quotient;
its source-completed coefficient is not assumed.

For comparison, Pawlowski-Reichert-Wessely arXiv:2507.22169 give the Lorentzian
asymptotic-safety TT propagator IR form

    G_hh^ph = z_spec^-1 [1/p^2 - A_h log(p^2) + ...],
    A_h = 61/(60*pi), z_spec ~= 1.486,

which has the same leading constant absorptive shape.  Their coefficient belongs to a
particular TT/gauge/field normalisation and is not substituted for a source-completed
RQIR observable.

No blocked comparator entry is zero-filled.  The full C3/C4/nonlocal loop sectors and
the source-completed AS/C5 finite-frequency map remain separate blockers.
"""
from pathlib import Path
import cmath
import json
import math
import numpy as np

# Target-independent benchmark rows.  They are all below the already frozen dRGT
# one-particle TT pole m^2=0.04, so the tree massive pole is not sampled.
# The numerical points are protocol coordinates only, not a candidate optimisation.
s = 0.004 * np.arange(1, 9, dtype=float)
omega = np.sqrt(s)
s_ref = float(s[-1])
x = s / s_ref
eps = 1e-14

# Retarded branch at positive frequency and the conjugate negative-frequency branch.
L_plus = np.array([cmath.log(complex(-v, -eps)) for v in s])
L_minus = np.array([cmath.log(complex(-v, +eps)) for v in s])

# First-order response tangent to a massless-loop logarithm: d chi / d ell = -L_R.
dchi_plus = -L_plus
dchi_minus = -L_minus
A_odd_log = (np.imag(dchi_plus) - np.imag(dchi_minus)) / (2 * np.pi)
A_even_leak = (np.imag(dchi_plus) + np.imag(dchi_minus)) / (2 * np.pi)

# A local real tree response is real away from isolated poles.  Use a deliberately
# overcomplete polynomial ladder to make the numerical audit explicit; the absorptive
# projection annihilates every column exactly by construction.
local_tree_real = np.column_stack([x**n for n in range(8)])
local_tree_abs = np.zeros_like(local_tree_real)
local_tree_abs_rank = int(np.linalg.matrix_rank(local_tree_abs, tol=1e-14))

# Generic logarithmic descendants illustrate how the new observable can carry shape
# information that local tree interpolation cannot reproduce.  They are a protocol
# stress-test family, not all claimed as independently present C5 operators.
log_desc = np.column_stack([(x**n) * A_odd_log for n in range(4)])
sv_log = np.linalg.svd(log_desc, compute_uv=False)
rank_log = int(np.linalg.matrix_rank(log_desc, tol=1e-12))

# Lorentzian AS IR authority (arXiv:2507.22169, Eqs. 30,33 in v1 HTML).
A_h = 61.0 / (60.0 * np.pi)
z_spec = 1.486
as_unnormalized_shape = A_h * A_odd_log
as_physical_field_shape = (A_h / z_spec) * A_odd_log
rho_tail_unnormalized_ir = 61.0 / 30.0
rho_tail_physical_ir = rho_tail_unnormalized_ir / z_spec

# Shape quotient: after allowing an overall source/field gain, AS leading IR and C5
# leading massless-log directions are exactly collinear in this finite protocol.
c5_shape = A_odd_log.copy()
coef_as_on_c5 = float(np.dot(c5_shape, as_unnormalized_shape) / np.dot(c5_shape, c5_shape))
res_as = as_unnormalized_shape - coef_as_on_c5 * c5_shape
rel_res_as = float(np.linalg.norm(res_as) / np.linalg.norm(as_unnormalized_shape))
rank_c5_as = int(np.linalg.matrix_rank(np.column_stack([c5_shape, as_unnormalized_shape]), tol=1e-12))

rows=[]
for i in range(len(s)):
    rows.append({
        "probe": i,
        "s": float(s[i]),
        "omega": float(omega[i]),
        "x=s/s_ref": float(x[i]),
        "Im_minus_log_positive_frequency": float(np.imag(dchi_plus[i])),
        "Im_minus_log_negative_frequency": float(np.imag(dchi_minus[i])),
        "A_odd_leading_log": float(A_odd_log[i]),
        "A_even_causality_leak": float(A_even_leak[i]),
        "AS_IR_unnormalized_Aodd": float(as_unnormalized_shape[i]),
        "AS_IR_physical_field_Aodd": float(as_physical_field_shape[i]),
    })

out={
    "iteration":166,
    "date":"2026-08-31",
    "scope":"eight timelike conserved-TT source-response benchmark frequencies; odd absorptive projection; comparator pre-gate",
    "protocol":{
        "s_values":s.tolist(),
        "omega_values":omega.tolist(),
        "s_ref":s_ref,
        "positive_frequency_branch":"log(-s-i0)=log(s)-i*pi",
        "negative_frequency_branch":"log(-s+i0)=log(s)+i*pi",
        "Aodd_definition":"[Im chi_R(+omega)-Im chi_R(-omega)]/(2*pi)",
        "pole_exclusion":"all s<0.04 frozen dRGT TT pole",
    },
    "analytic_local_tree":{
        "absorptive_rank":local_tree_abs_rank,
        "statement":"real local Hermitian tree contributions are off-pole absorptively zero; this is not a finite-polynomial interpolation statement",
    },
    "leading_massless_log":{
        "Aodd":A_odd_log.tolist(),
        "rank":int(np.linalg.matrix_rank(A_odd_log[:,None],tol=1e-12)),
        "max_even_causality_leak":float(np.max(np.abs(A_even_leak))),
    },
    "generic_log_descendant_stress_test":{
        "basis":"x^n Aodd_log, n=0..3",
        "rank":rank_log,
        "singular_values":sv_log.tolist(),
        "smin_over_smax":float(sv_log[-1]/sv_log[0]),
        "condition_number":float(sv_log[0]/sv_log[-1]),
        "interpretation":"illustrative nonanalytic shape capacity only; not a claim that all four are independent fixed C5 Wilson directions",
    },
    "lorentzian_AS_IR":{
        "source":"Pawlowski, Reichert, Wessely, arXiv:2507.22169 v1, Eqs. 12-15, 30-33",
        "A_h":float(A_h),
        "z_spec_approx":z_spec,
        "A_h_over_z_spec":float(A_h/z_spec),
        "rho_tail_unnormalized_IR":rho_tail_unnormalized_ir,
        "rho_tail_physical_IR":rho_tail_physical_ir,
        "shape_rank_C5_log_plus_AS_IR":rank_c5_as,
        "AS_relative_residual_after_C5_log_shape_projection":rel_res_as,
        "classification":"LEADING_IR_SHAPE_COLLINEAR_WITH_C5_MASSLESS_LOG_AFTER_GAIN",
        "guardrail":"published AS coefficient is TT/gauge/field-normalization specific and is not treated as the final source-completed RQIR coefficient",
    },
    "supported_scoped_comparator_statements":{
        "C5_local_tree":"ZERO_ABSORPTIVE_OFF_POLE",
        "C5_massless_loop_log":"NONZERO_CONSTANT_AODD_SHAPE",
        "C4_dRGT_tree":"ZERO_ABSORPTIVE_ON_CHOSEN_ROWS_BELOW_ISOLATED_TT_POLE; loops/matter completion not inferred",
        "NL_entire_tree":"NO_FORM_FACTOR_BRANCH_CUT_SCOPED; full CTP/loop completion still blocked",
        "AS_Lorentzian_IR":"NONZERO_CONTINUUM; leading log shape collinear with C5",
        "C3_tree_EH":"ZERO_ABSORPTIVE_OFF_POLE_SCOPED; diffusion/MSR ordered corrections remain blocked",
    },
    "blocked":[
        "source-completed gauge-invariant finite-frequency C5 loop coefficient in the exact RQIR detector/source convention",
        "full C3 diffusion-dependent ordered/absorptive response",
        "full C4 loop/matter/helicity absorptive completion",
        "full nonlocal CTP/loop absorptive completion",
        "finite-frequency AS source-completed RQIR map beyond the leading IR shape",
        "global cross-observable quotient tying this block to chi2R/N2/C3sym from one dynamics",
    ],
    "retained_results":[
        "C5-NG-004 — LOCAL_HERMITIAN_TREE_EFT_CANNOT_SATURATE_OFF_POLE_ABSORPTIVE_BLOCK",
        "AS-NG-004 — LORENTZIAN_AS_LEADING_IR_LOG_IS_COLLINEAR_WITH_C5_MASSLESS_LOOP_SHAPE",
        "NG-FUNNEL-024 — ABSORPTIVE_NONANALYTICITY_ESCAPES_LOCAL_TREE_INTERPOLATION_BUT_NOT_QUANTUM_COMPARATOR_SUBTRACTION",
        "NG-FUNNEL-025 — BARE_TT_SPECTRAL_COEFFICIENT_IS_NOT_YET_A_SOURCE_COMPLETED_RQIR_OBSERVABLE",
    ],
    "candidate_residual":"NOT_DEFINED_FULL_COMPARATOR_ABSORPTIVE_QUOTIENT_BLOCKED",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN",
    "model_readiness_percent":24,
    "readiness_change":"unchanged: comparator foundation narrowed but final point not awarded while source-completed absorptive C3/C4/nonlocal/AS quotient is incomplete",
    "rows":rows,
}

Path("results/timelike_absorptive_protocol_iteration166.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
