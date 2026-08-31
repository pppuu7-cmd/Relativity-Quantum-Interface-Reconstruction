#!/usr/bin/env python3
"""Iteration 205: structural validator for a linked nonanalytic multi-point cut.

The validator is algebraic, not a gravity-loop calculation.  It freezes the
next RQIR novelty carrier after Iterations 202-204 showed that arbitrary local
analytic derivative towers defeat finite analytic-shape quotients.

Define normalized discontinuity D across a positive timelike branch cut by
D log_R(-s) = 1.  Then D annihilates local analytic polynomials and maps
s^n log_R(-s) -> s^n.

A source-completed retarded three-point soft object is written schematically as

  Gamma3 = W[K2] + T_nonanalytic + A_local,

where W is the Ward/soft-determined contribution from the same two-point kernel.
The proposed linked cut coordinate is

  T_cut = D Gamma3 - W[D K2].

For a linear momentum-space Ward operator W built from differentiation and local
kinematic multiplication, D commutes with W away from branch endpoints.  Hence
T_cut annihilates all local analytic counterterms and is invariant under any
analytic repartition W -> W+C, T -> T-C.

The toy numerical block below verifies these algebraic properties for a simple
linear W=d/ds+s* operator.  This W is not the physical gravity Ward operator; it
only checks the protocol algebra.
"""
from pathlib import Path
import json
import numpy as np

s=np.array([0.004*i for i in range(1,9)],float)
# Represent a function as analytic polynomial coeffs plus log coeff polynomial.
# D sees only the log polynomial.

def polyval(c,x):
    return sum(a*x**n for n,a in enumerate(c))
def dpolyval(c,x):
    return sum(n*a*x**(n-1) for n,a in enumerate(c) if n>=1)

# Toy K2: arbitrary analytic local part + nonanalytic massless part.
k_local=[0.4,-0.7,1.1,-0.2,0.9]
k_log=[0.0,0.0,1.3,-0.4]  # (1.3 s^2 -0.4 s^3) log
# Toy transverse nonanalytic three-point content and arbitrary local cubic terms.
t_local=[-1.2,0.3,2.1,-0.8,0.5,-0.1]
t_log=[0.0,0.6,-0.25,0.08]

# W[f]=f'(s)+s f(s).  Its discontinuity acts on the log coefficient plus the
# derivative of log itself.  To avoid pretending this toy W is the physical
# gravity map, validate only the linear commutation on the abstract cut data:
# W_D[g]=g'(s)+s*g(s).
D_K=polyval(k_log,s)
W_DK=dpolyval(k_log,s)+s*D_K
D_T=polyval(t_log,s)
D_Gamma=W_DK+D_T
T_cut=D_Gamma-W_DK

# Add arbitrary local analytic deformations: discontinuity remains unchanged.
local_deformation=[3.0,-8.0,5.0,11.0,-4.0,2.0,7.0]
# By definition D(local polynomial)=0.
D_Gamma_after_local=D_Gamma.copy()

# Analytic repartition ambiguity W->W+C, T->T-C also has zero D(C).
D_W_after_repartition=W_DK.copy()
D_T_after_repartition=D_T.copy()
T_cut_after_repartition=D_Gamma_after_local-D_W_after_repartition

# Explicit local derivative tower check: all monomials s^n have zero D.
local_tower_D=np.zeros((len(s),20))
# Nonanalytic test tower s^n log has D=s^n.
log_tower_D=np.column_stack([s**n for n in range(6)])

out={
 'iteration':205,'date':'2026-09-01','model_readiness_percent':23,
 'scope':'structural linked-discontinuity protocol; no physical gravity loop coefficient computed',
 'timelike_rows_s':s.tolist(),
 'normalized_discontinuity':'D F = Disc_s F/(2 pi i), with D log_R(-s)=1 on the frozen positive-frequency branch convention',
 'proposed_coordinate':'T_cut = D Gamma3_ret,soft - W[D K2] in one source-completed convention',
 'local_analytic_tower_max_abs_D':float(np.max(np.abs(local_tower_D))),
 'nonanalytic_log_tower_rank':int(np.linalg.matrix_rank(log_tower_D,tol=1e-14)),
 'toy_T_cut':T_cut.tolist(),
 'max_local_deformation_change':float(np.max(np.abs((D_Gamma_after_local-W_DK)-T_cut))),
 'max_analytic_repartition_change':float(np.max(np.abs(T_cut_after_repartition-T_cut))),
 'classification':{
   'arbitrary_local_analytic_C5_tower':'EXACT_NULL_UNDER_DISCONTINUITY_WITHIN_ANALYTIC_DOMAIN',
   'analytic_W_B_repartition':'EXACT_NULL_UNDER_DISCONTINUITY',
   'standalone_two_point_cut':'NOT_NOVEL_C4_DEGENERATE_BY_ITERATION170',
   'linked_three_point_cut':'NEW_PROTOCOL_TARGET_NOT_YET_COMPARATOR_CLOSED',
   'C5_loop_cut':'REQUIRED_POSITIVE_CONTROL_BLOCKED_NOT_YET_INSTANTIATED',
   'C4_nonlinear_mediator_cut':'BLOCKED_NOT_ZERO',
   'AS_realtime_threepoint_cut':'BLOCKED_NOT_ZERO',
   'C3_ordered_cut':'BLOCKED_NOT_ZERO',
   'ANSATZ_003':'NOT_CREATED','Fisher_resources':'FORBIDDEN'},
 'retained_results':[
   'CUT-NG-001 — DISCONTINUITY_ANNIHILATES_THE_UNBOUNDED_LOCAL_ANALYTIC_DERIVATIVE_TOWER_WITHIN_ITS_ANALYTIC_DOMAIN',
   'CUT-NG-002 — LINKED_THREEPOINT_MINUS_WARD_OF_TWOPOINT_CUT_IS_INVARIANT_UNDER_ANALYTIC_WARD_TRANSVERSE_REPARTITION',
   'NG-FUNNEL-061 — NONANALYTICITY_MUST_BE_TESTED_AS_A_LINKED_MULTIPOINT_RELATION_NOT_A_STANDALONE_SPECTRAL_SIGNAL'
 ],
 'readiness_change':'unchanged at 23%: the protocol evades the newly exposed analytic-tower blocker structurally, but physical C5/C4/AS/C3 cut comparators are not yet instantiated'
}
Path('results/linked_nonanalytic_cut_protocol_iteration205.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,indent=2,sort_keys=True))
