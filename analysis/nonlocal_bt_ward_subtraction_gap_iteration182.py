#!/usr/bin/env python3
"""Iteration 182: executable Ward-subtraction gap for nonlocal B_T.

The six-row B_T protocol was introduced schematically as

    B_T = P_T[Gamma_arr - W[K2]].

Iteration 175 validates the transverse soft-Riemann carrier but does not implement
an executable W[K2] map or a numerical P_T.  This is harmless for the local
curvature-cubic directions of Iterations 177-178 because those operators start at
O(h^3) about Minkowski and have K2_operator=0, hence W[K2_operator]=0 exactly.

It is not harmless for QG-NL-EXP-001, whose quadratic kernel is nonzero.  A raw
cubic tensor calculation cannot by itself define the transverse B_T coordinate:
any gauge-invariant soft-Riemann term may be shifted between W and B unless the
source-completed covariantization convention is explicitly frozen.

This script supplies a finite algebraic certificate of that ambiguity using the
same linearized soft-Riemann geometry as Iteration 175.
"""
from pathlib import Path
import json, math
import numpy as np


def linearized_riemann(k, eps):
    R=np.zeros((4,4,4,4),dtype=float)
    for mu in range(4):
        for nu in range(4):
            for rho in range(4):
                for sig in range(4):
                    R[mu,nu,rho,sig] = -0.5*(
                        k[rho]*k[nu]*eps[mu,sig]
                        + k[sig]*k[mu]*eps[nu,rho]
                        - k[sig]*k[nu]*eps[mu,rho]
                        - k[rho]*k[mu]*eps[nu,sig]
                    )
    return R

k=np.array([1.0,0.0,0.0,1.0])
xi=np.array([0.31,-0.27,0.19,0.41])
eps_gauge=np.outer(k,xi)+np.outer(xi,k)
eps_tt=np.zeros((4,4),dtype=float)
eps_tt[1,1]=1/math.sqrt(2.0)
eps_tt[2,2]=-1/math.sqrt(2.0)
Rg=linearized_riemann(k,eps_gauge)
Rt=linearized_riemann(k,eps_tt)

# Contract the Riemann carrier with a deterministic Riemann-symmetry-compatible
# tensor chosen only to demonstrate a nonzero physical transverse scalar.
rng=np.random.default_rng(182)
X=rng.normal(size=(4,4,4,4))
# Antisymmetrize in first and second pairs, then symmetrize pair exchange.
B0=0.25*(X-X.swapaxes(0,1)-X.swapaxes(2,3)+X.swapaxes(0,1).swapaxes(2,3))
B0=0.5*(B0+B0.transpose(2,3,0,1))
carrier_g=float(np.einsum('mnrs,mnrs',Rg,B0))
carrier_t=float(np.einsum('mnrs,mnrs',Rt,B0))

# Six scalar row illustration.  Gamma = W + carrier*B is unchanged under
# W -> W + carrier*C, B -> B-C.  Since the added term is built from Rlin,
# pure-gauge soft polarization cannot constrain C.
nrow=6
W=np.array([0.3,-0.2,0.15,0.7,-0.4,0.11])
B=np.array([0.8,-0.5,0.2,0.1,-0.3,0.6])
C=np.array([0.17,-0.09,0.04,0.12,-0.08,0.03])
Gamma=W+carrier_t*B
Wp=W+carrier_t*C
Bp=B-C
Gammap=Wp+carrier_t*Bp

out={
  'iteration':182,
  'scope':'definition audit for six-row source-completed null-soft B_T protocol before QG-NL-EXP-001 tensor projection',
  'soft_carrier':{
    'pure_gauge_riemann_norm':float(np.linalg.norm(Rg)),
    'physical_tt_riemann_norm':float(np.linalg.norm(Rt)),
    'pure_gauge_test_contraction':carrier_g,
    'physical_tt_test_contraction':carrier_t,
  },
  'decomposition_shift_certificate':{
    'max_abs_raw_vertex_change_under_W_B_shift':float(np.max(np.abs(Gammap-Gamma))),
    'shift_norm':float(np.linalg.norm(C)),
    'interpretation':'arbitrary transverse soft-Riemann shift leaves the raw vertex and Ward/gauge constraints unchanged unless W[K2] convention is fixed'
  },
  'repository_protocol_audit':{
    'iteration175_W_K2':'SCHEMATIC_NOT_EXECUTABLE',
    'iteration175_P_T':'SCHEMATIC_NOT_EXECUTABLE',
    'iteration177_178_local_R3':'SAFE_BECAUSE_OPERATOR_K2_ZERO_SO_W_ZERO_EXACTLY',
    'QG_NL_EXP_001':'NONZERO_K2_REQUIRES_EXPLICIT_SOURCE_COMPLETED_WARD_SUBTRACTION',
    'raw_full_nonlocal_cubic':'NECESSARY_BUT_NOT_SUFFICIENT_FOR_B_T'
  },
  'classification':{
    'nonlocal_B_T':'BLOCKED_EXECUTABLE_SOURCE_COMPLETED_WARD_SUBTRACTION_NOT_YET_FROZEN',
    'consistency_fail':False,
    'exact_comparator_identity':False,
    'novelty_certificate':'NONE',
    'ANSATZ_003':'NOT_CREATED',
    'Fisher_resources':'FORBIDDEN'
  },
  'retained_results':[
    'SOFT-NG-008 — TRANSVERSE_RIEMANN_SHIFT_IS_INVISIBLE_TO_WARD_CONSTRAINTS_UNTIL_W_K2_CONVENTION_IS_FIXED',
    'NL-NG-005 — FULL_NONLOCAL_RAW_CUBIC_IS_NECESSARY_BUT_NOT_SUFFICIENT_FOR_B_T_WHEN_K2_IS_NONZERO',
    'NG-FUNNEL-040 — EXECUTABLE_SOURCE_COMPLETED_WARD_SUBTRACTION_MUST_PRECEDE_NONLOCAL_OR_AS_B_T_RANK_PROMOTION'
  ],
  'model_readiness_percent':24,
  'readiness_change':'unchanged: a definition-level comparator blocker is exposed and prevented from becoming a false rank certificate'
}
Path('results/nonlocal_bt_ward_subtraction_gap_iteration182.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2,sort_keys=True))
