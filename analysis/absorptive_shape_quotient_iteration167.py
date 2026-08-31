#!/usr/bin/env python3
"""Iteration 167: conserved-TT source completion and constant-log-null shape quotient.

The Iteration-166 timelike absorptive block is a linear chi^(1)R spectral observable,
not the post-Gaussian chi^(2)R_odd coordinate.  Here we make its finite shape map
operational in a fixed conserved-TT external-stress channel and profile out the
universal leading logarithmic onset shared by perturbative C5 and Lorentzian AS.

Kinematics: k=(omega,0,0,0), s=omega^2=0.004,...,0.032.
External source/detector stress:
  T_0mu=0, T_ij=diag(1,-1,0)/sqrt(2).
It is conserved and traceless and satisfies T:P2:T=1 for every row.

The eight-row constant direction is removed before any candidate comparison.  A
stable target-independent orthonormal shape basis is constructed by a QR factorisation
of [1,x,...,x^7], x=s/s_max; the first QR column is the normalised constant and the
remaining seven columns span its exact numerical orthogonal complement.

This operation removes local-tree absorptive zero trivially and also removes any
unknown overall coefficient multiplying the leading constant massless-log onset.  It
does not remove the finite-frequency AS continuum or subleading C5 loop shapes; those
remain comparators/blockers to be instantiated.
"""
from pathlib import Path
import json
import math
import numpy as np

ETA=np.diag([-1.0,1.0,1.0,1.0])
s=0.004*np.arange(1,9,dtype=float)
omega=np.sqrt(s)
x=s/s[-1]

# Fixed conserved traceless spatial source/detector tensor.
E=np.zeros((4,4),float)
E[1,1]=1/math.sqrt(2)
E[2,2]=-1/math.sqrt(2)


def p2_projector(k):
    kc=ETA@k
    k2=float(k@ETA@k)
    theta=ETA-np.outer(kc,kc)/k2
    P=np.zeros((4,4,4,4),float)
    for m in range(4):
        for n in range(4):
            for r in range(4):
                for t in range(4):
                    P[m,n,r,t]=(0.5*(theta[m,r]*theta[n,t]+theta[m,t]*theta[n,r])
                                  -(1.0/3.0)*theta[m,n]*theta[r,t])
    return theta,P

source_rows=[]
max_conservation=max_trace=max_projector_error=0.0
overlaps=[]
for i,w in enumerate(omega):
    k=np.array([w,0.0,0.0,0.0])
    theta,P=p2_projector(k)
    PE=np.einsum('mnrs,rs->mn',P,E)
    conservation=float(np.max(np.abs(k@E)))
    trace=float(abs(np.sum(ETA*E)))
    projerr=float(np.max(np.abs(PE-E)))
    overlap=float(np.einsum('mn,mn',E,PE))
    max_conservation=max(max_conservation,conservation)
    max_trace=max(max_trace,trace)
    max_projector_error=max(max_projector_error,projerr)
    overlaps.append(overlap)
    source_rows.append({"probe":i,"s":float(s[i]),"omega":float(w),"x":float(x[i]),
                        "conservation_error":conservation,"trace_error":trace,
                        "projector_error":projerr,"source_overlap":overlap})

# Target-independent orthonormal quotient.  QR on the full Vandermonde fixes the
# constant as the first direction and gives a numerically orthonormal complement.
V=np.column_stack([x**n for n in range(8)])
Q,R=np.linalg.qr(V)
for j in range(8):
    idx=int(np.argmax(np.abs(Q[:,j])))
    if Q[idx,j]<0:
        Q[:,j]*=-1
q_const=Q[:,0]
Q_shape=Q[:,1:]

one=np.ones(8)
A_h=61.0/(60.0*np.pi)
c5_leading=one.copy()
as_leading=A_h*one
c5_shape=Q_shape.T@c5_leading
as_shape=Q_shape.T@as_leading

# Target-independent capacity audit for possible sub-leading frequency dependence.
subleading=np.column_stack([x,x**2,x**3])
subleading_q=Q_shape.T@subleading
sv_sub=np.linalg.svd(subleading_q,compute_uv=False)

# Optional finite-difference diagnostic: fourth difference annihilates any cubic
# polynomial absorptive envelope exactly, but carries significant white-noise gain.
from math import comb
c4=np.array([(-1)**(4-k)*comb(4,k) for k in range(5)],float)
D4=np.zeros((4,8),float)
for i in range(4):
    D4[i,i:i+5]=c4
poly03=np.column_stack([one,x,x**2,x**3])

out={
    "iteration":167,
    "date":"2026-08-31",
    "observable_clarification":"Iteration-166/167 A_odd is frequency-odd Im chi1R; it is distinct from post-Gaussian chi2R_odd",
    "scope":"eight timelike conserved-TT source-to-source linear-response rows; constant-leading-log profiled shape quotient",
    "source_completion":{
        "kinematics":"k=(omega,0,0,0)",
        "stress":"T_0mu=0; T_ij=diag(1,-1,0)/sqrt(2)",
        "max_conservation_error":max_conservation,
        "max_trace_error":max_trace,
        "max_projector_error":max_projector_error,
        "source_overlaps":overlaps,
        "max_overlap_deviation_from_one":float(np.max(np.abs(np.asarray(overlaps)-1))),
        "interpretation":"linear conserved-TT source overlap is frequency independent; common gravitational/source gain can be calibrated/profiled without changing spectral shape",
    },
    "constant_log_null_quotient":{
        "row_count":8,
        "profiled_dimension":1,
        "shape_dimension":7,
        "q_const":q_const.tolist(),
        "Q_shape":Q_shape.tolist(),
        "max_shape_dot_constant":float(np.max(np.abs(Q_shape.T@one))),
        "max_shape_orthonormality_error":float(np.max(np.abs(Q_shape.T@Q_shape-np.eye(7)))),
        "C5_leading_log_shape_norm_after_projection":float(np.linalg.norm(c5_shape)),
        "AS_leading_IR_log_shape_norm_after_projection":float(np.linalg.norm(as_shape)),
        "classification":"UNIVERSAL_CONSTANT_LOG_DIRECTION_EXACTLY_PROFILED_TO_MACHINE_PRECISION",
    },
    "subleading_capacity_audit":{
        "test_family":["x","x^2","x^3"],
        "quotient_rank":int(np.linalg.matrix_rank(subleading_q,tol=1e-12)),
        "singular_values":sv_sub.tolist(),
        "smin_over_smax":float(sv_sub[-1]/sv_sub[0]),
        "classification":"SHAPE_QUOTIENT_RETAINS_THREE_INDEPENDENT_LOW_ORDER_FREQUENCY_DIRECTIONS",
        "guardrail":"capacity test only; these columns are not declared Candidate Gravity or independent C5 parameters",
    },
    "optional_D4_diagnostic":{
        "coefficients":c4.tolist(),
        "max_abs_response_to_degree_0_3_polynomials":float(np.max(np.abs(D4@poly03))),
        "single_window_white_noise_amplification_l2":float(np.linalg.norm(c4)),
        "classification":"EXACT_CUBIC_ENVELOPE_NULL_BUT_NOISE_COSTLY; NOT_ADOPTED_AS_PRIMARY_PROTOCOL",
    },
    "literature_boundary":{
        "AS_publication":"Pawlowski, Reichert, Wessely, Physics Letters B 880 (2026) 140844, DOI 10.1016/j.physletb.2026.140844; arXiv:2507.22169",
        "AS_supported":"positive massless peak plus continuum; universal IR constant onset; continuum decreases at intermediate scales",
        "AS_finite_frequency_column":"BLOCKED_NUMERICAL_SPECTRAL_DATA_OR_REPRODUCTION_REQUIRED",
        "C5_subleading_loop_shape":"BLOCKED_SOURCE_COMPLETED_LOOP_ORDER_SPECIFICATION",
    },
    "comparator_logic":{
        "local_tree":"annihilated because absorptive block is zero off pole",
        "C5_leading_massless_log":"annihilated by constant profile",
        "AS_leading_IR_log":"annihilated by constant profile",
        "C3_C4_nonlocal_unsupported_loops":"BLOCKED_NOT_ZERO_FILLED",
        "full_candidate_residual":"NOT_DEFINED_UNTIL_SUBLEADING_COMPARATOR_COLUMNS_ARE_INSTANTIATED_OR_BOUNDED",
    },
    "retained_results":[
        "ABS-SHAPE-001 — CONSERVED_TT_SOURCE_MAP_PRESERVES_TIMELIKE_SPECTRAL_SHAPE",
        "ABS-SHAPE-002 — CONSTANT_LOG_NULL_QUOTIENT_LEAVES_SEVEN_SUBLEADING_SHAPE_DIMENSIONS",
        "NG-FUNNEL-026 — PROFILE_UNIVERSAL_IR_LOG_BEFORE_SUBLEADING_SPECTRAL_SHAPE_SEARCH",
        "NG-FUNNEL-027 — PUBLISHED_SPECTRAL_CURVE_IS_NOT_A_NUMERICAL_COMPARATOR_COLUMN_WITHOUT_DATA_OR_CONTROLLED_REPRODUCTION",
    ],
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN",
    "model_readiness_percent":24,
    "readiness_change":"unchanged; source/shape protocol closes a methodological ambiguity but robust comparator-subtracted subleading residual remains absent",
    "rows":source_rows,
}
Path("results/absorptive_shape_quotient_iteration167.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
print(json.dumps(out,indent=2,sort_keys=True))
