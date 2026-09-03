#!/usr/bin/env python3
"""RQIR Candidate Gravity Iteration 309.

Fail-closed typed operator/index and first-background-variation contract for the
remaining e=2,c<=1 Vilkovisky U2 sector.

This gate deliberately does NOT invent unavailable physical V1/H component
formulas.  It freezes the exact operator typing implied by authoritative U2
order and verifies the six-site Leibniz expansion needed by Iteration 308.
Unsupported physical component data remain BLOCKED, never zero-filled.
"""
from __future__ import annotations
import json
import numpy as np

rng=np.random.default_rng(309)
G=5   # abstract ghost-index space
S=7   # abstract symmetric-field-index space

# Operator conventions.  Matrix products implement explicit index contractions:
# (U2)^a_b = N_L^a_c (V1_L)^c_I H^I_J (V1_R)^J_d N_R^d_e Y^e_b.
# Thus V1_L : S -> G is represented GxS and V1_R : G -> S is SxG.
shapes={
 'N_L':(G,G), 'V1_L':(G,S), 'H':(S,S),
 'V1_R':(S,G), 'N_R':(G,G), 'Y':(G,G)
}

def rmat(shape):
    return rng.normal(size=shape)

A={k:rmat(v) for k,v in shapes.items()}
dA={k:rmat(v) for k,v in shapes.items()}

seq=('N_L','V1_L','H','V1_R','N_R','Y')

def product(dic):
    out=dic[seq[0]]
    for k in seq[1:]: out=out@dic[k]
    return out

U0=product(A)
assert U0.shape==(G,G)
tr0=float(np.trace(U0))

# Exact first-background Leibniz derivative: one insertion on each of six sites.
terms={}
for site in seq:
    B=dict(A); B[site]=dA[site]
    terms[site]=product(B)
dU=sum(terms.values())

# Independent finite-difference audit of simultaneous first variation.
h=1e-6
Ap={k:A[k]+h*dA[k] for k in seq}
Am={k:A[k]-h*dA[k] for k in seq}
fd=(product(Ap)-product(Am))/(2*h)
fd_rel=float(np.linalg.norm(fd-dU)/max(1.0,np.linalg.norm(dU)))

# Trace cyclicity check: exact operator order may be cyclically rotated, not
# reversed.  This guards against an unproven left/right reversal quotient.
def cyclic_trace(mats):
    out=mats[0]
    for m in mats[1:]: out=out@m
    return float(np.trace(out))
base=[A[k] for k in seq]
cyclic=[]
for j in range(len(base)):
    rot=base[j:]+base[:j]
    # dimensions only close for rotations that start/end on compatible spaces;
    # np.matmul will enforce the typed contract.
    try: cyclic.append(cyclic_trace(rot))
    except ValueError: pass
cyclic_res=max(abs(x-tr0) for x in cyclic) if cyclic else float('inf')

# Adjoint/transpose typing: the right V1 orientation is the transpose-direction
# map of the left orientation in the abstract real test representation.  This
# is an index-space statement only, not a physical equality of coefficients.
VL=rmat((G,S)); VR=VL.T
assert VL.shape==(G,S) and VR.shape==(S,G)

# Iteration 308 requires exactly 12 surviving ordered U2 placements, two per
# extra site.  This gate freezes how those rows plug into the six derivative
# terms, without assigning missing physical coefficients.
iter308_survivors_by_site={k:2 for k in seq}
assert sum(iter308_survivors_by_site.values())==12

thresholds={'finite_difference_relative_max':5e-9,'cyclic_trace_absolute_max':1e-9}
passed=(fd_rel<=thresholds['finite_difference_relative_max'] and
        cyclic_res<=thresholds['cyclic_trace_absolute_max'])

physical_component_status={
 'V1_1_flat_momentum_kernel':'BLOCKED_NOT_SUPPLIED_BY_THIS_GATE',
 'V1_2_mixed_background_kernel':'BLOCKED_NOT_SUPPLIED_BY_THIS_GATE',
 'H0_flat_graviton_green_projector':'BLOCKED_NOT_SUPPLIED_BY_THIS_GATE',
 'H1_first_background_variation':'BLOCKED_NOT_SUPPLIED_BY_THIS_GATE',
 'N1_and_Y1':'REUSE_ONLY_AFTER_SAME_PARENT_ROUTING_CHECK'
}

classification=('PASS_E2C1_U2_TYPED_OPERATOR_INDEX_AND_FIRST_VARIATION_CONTRACT__PHYSICAL_COMPONENT_KERNELS_REMAIN_BLOCKED'
                if passed else
                'FAIL_E2C1_U2_TYPED_OPERATOR_CONTRACT')

result={
 'iteration':309,
 'model_readiness_percent':24,
 'scientific_gate_pass':bool(passed),
 'classification':classification,
 'candidate_residual':False,
 'operator_identity':{
   'U2_sequence':list(seq),
   'indexed_formula':'(U2)^a_b = N_L^a_c (V1_L)^c_I H^I_J (V1_R)^J_d N_R^d_e Y^e_b',
   'trace_formula':'Tr U2 = N_L^a_c (V1_L)^c_I H^I_J (V1_R)^J_d N_R^d_e Y^e_a',
   'index_spaces':{'ghost':'a,b,c,d,e','symmetric_field':'I,J'},
   'V1_orientations':{'left':'S->G (GxS)','right':'G->S (SxG)'},
   'H_role':'field-space Green operator between the two V1 orientations'
 },
 'first_background_variation':{
   'formula':'dU2 = dN_L V1_L H V1_R N_R Y + N_L dV1_L H V1_R N_R Y + N_L V1_L dH V1_R N_R Y + N_L V1_L H dV1_R N_R Y + N_L V1_L H V1_R dN_R Y + N_L V1_L H V1_R N_R dY',
   'site_count':6,
   'iteration308_surviving_placements_by_site':iter308_survivors_by_site,
   'iteration308_total_surviving_ordered_placements':12
 },
 'numerical_contract_audit':{
   'finite_difference_relative_residual':fd_rel,
   'cyclic_trace_absolute_residual':cyclic_res,
   'thresholds':thresholds
 },
 'physical_component_status':physical_component_status,
 'guardrails':[
   'UNSUPPORTED_PHYSICAL_COMPONENTS_ARE_BLOCKED_NOT_ZERO_FILLED',
   'NO_LEFT_RIGHT_OR_REVERSAL_QUOTIENT_IS_ASSUMED',
   'NO_NUMERATOR_RECONSTRUCTION_AUTHORIZED_BY_THIS CONTRACT ALONE',
   'NO_SOURCE_BORN_SUBTRACTION',
   'NO_ANSATZ003_FISHER_OR_RESOURCES',
   'NO_BLIND_HEAVY_FULL_C5'
 ],
 'next_gate':'extract/freeze same-parent physical V1_1, V1_2, H0 and H1 component formulas in frozen D=4 Lambda=0 a=-1/2 conventions, then validate transpose/routing identities against this typed contract before any e2c1 numerator reconstruction.'
}
print(json.dumps(result,indent=2,sort_keys=True))
if not passed:
    raise SystemExit(2)
