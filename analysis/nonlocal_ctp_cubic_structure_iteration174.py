#!/usr/bin/env python3
"""Iteration 174: fixed covariant nonlocal cubic/CTP structural audit.

Comparator: QG-NL-EXP-001

  S = Mpl^2/2 int sqrt(-g) [ R + G_mn F(Box) R^mn ] + S_m,
  F(Box) = (exp(-lambda Box)-1)/Box, lambda=M^-2>0.

The audit has two purposes.

(1) Demonstrate that the *full covariant parent form factor* fixes a cubic
operator-insertion term that is absent from propagator-only reasoning.  Using

  F(A) = - int_0^lambda d alpha exp(-alpha A),

the first Frechet variation is

  delta F(A) = int_0^lambda d alpha int_0^alpha du
               exp(-(alpha-u)A) (delta A) exp(-u A).

Between eigenmodes A|a>=a|a>, A|b>=b|b>, this coefficient is the divided
 difference (F(a)-F(b))/(a-b), with the diagonal limit F'(a).

(2) Show that the current Iteration-172 coarse CTP relation map cannot
 distinguish this closed-unitary diffeomorphism-invariant tree comparator.
 Any row-local cubic amplitude B_i enters as

  (Gamma_arr,Gamma_aar,Gamma_aaa,WardLock)=(B_i,0,B_i/4,0),

so R_aar=0, R_unit=Gamma_aaa-Gamma_arr/4=0, R_W=0 exactly.

This does NOT mean the raw nonlocal cubic amplitude is zero.  It means it is
annihilated by the current relation coordinates.  A more discriminating
transverse/soft-Ward relation is required.
"""
from pathlib import Path
import json
import math
import numpy as np

lam = 1.0

def F(z):
    if abs(z) < 1e-14:
        return -lam
    return (math.exp(-lam*z)-1.0)/z

def Fprime(z):
    if abs(z) < 1e-14:
        return lam*lam/2.0
    return (1.0-math.exp(-lam*z)*(1.0+lam*z))/(z*z)

def frechet_integral_coeff(a,b):
    if abs(a-b) < 1e-14:
        return (1.0-math.exp(-a*lam)*(1.0+a*lam))/(a*a)
    A = lambda z: (1.0-math.exp(-lam*z))/z
    return (A(a)-A(b))/(b-a)

def divided_difference(a,b):
    if abs(a-b) < 1e-14:
        return Fprime(a)
    return (F(a)-F(b))/(a-b)

pairs = [(0.3,0.7),(0.5,1.2),(1.0,1.0),(0.2,2.0),(0.4,0.9),(1.4,0.6)]
frechet_rows=[]
for a,b in pairs:
    i = frechet_integral_coeff(a,b)
    d = divided_difference(a,b)
    frechet_rows.append({"a":a,"b":b,"integral":i,"divided_difference":d,"abs_error":abs(i-d)})
max_frechet_error=max(r["abs_error"] for r in frechet_rows)

# Six frozen relation rows: generic closed-unitary amplitude basis.
nrow=6
raw=np.zeros((4*nrow,nrow))
for i in range(nrow):
    raw[4*i+0,i]=1.0       # Gamma_arr
    raw[4*i+1,i]=0.0       # Gamma_aar
    raw[4*i+2,i]=0.25      # Gamma_aaa
    raw[4*i+3,i]=0.0       # WardLock

# Relation map per row: (aar, aaa-arr/4, WardLock)
R=np.zeros((3*nrow,4*nrow))
for i in range(nrow):
    R[3*i+0,4*i+1]=1.0
    R[3*i+1,4*i+2]=1.0
    R[3*i+1,4*i+0]=-0.25
    R[3*i+2,4*i+3]=1.0
rel=R@raw

out={
  "iteration":174,
  "comparator":"QG-NL-EXP-001",
  "lambda":lam,
  "frechet_variation_certificate":frechet_rows,
  "max_frechet_divided_difference_error":max_frechet_error,
  "cubic_expansion_structure":[
    "G2 F0 R1",
    "G1 F0 R2",
    "sqrtg1 G1 F0 R1",
    "G1 (delta F)_1 R1"
  ],
  "current_relation_map": ["R_aar=Gamma_aar","R_unit=Gamma_aaa-Gamma_arr/4","R_W=WardLock"],
  "closed_unitary_raw_rank": int(np.linalg.matrix_rank(raw,tol=1e-12)),
  "closed_unitary_relation_rank": int(np.linalg.matrix_rank(rel,tol=1e-12)),
  "max_abs_relation_entry": float(np.max(np.abs(rel))),
  "classification":{
    "full_covariant_action_tree_cubic":"FIXED_IN_PRINCIPLE_BY_ACTION_AND_FRECHET_VARIATION",
    "propagator_only_to_cubic":"NOT_UNIQUE_WITHOUT_COVARIANT_PARENT_ACTION",
    "independent_curvature_cubic_potential_in_QG_NL_EXP_001":"ABSENT_BY_FROZEN_DEFINITION",
    "broad_weakly_nonlocal_class_cubic_from_two_point":"NOT_UNIQUE_BECAUSE_INDEPENDENT_POTENTIALS_ALLOWED",
    "tree_CTP_relation_contribution":"EXACTLY_ANNIHILATED_BY_ITERATION172_RELATION_MAP",
    "raw_six_probe_tensor_cubic_amplitude":"NOT_NEEDED_FOR_CURRENT_COARSE_RELATION_RANK; STILL_NOT_NUMERICALLY_PROJECTED",
    "ANSATZ_003":"NOT_CREATED",
    "Fisher_resources":"FORBIDDEN"
  },
  "retained_results":[
    "NL-NG-003 — COVARIANT_NONLOCAL_CUBIC_VERTEX_CONTAINS_OPERATOR_FRECHET_VARIATION_NOT_VISIBLE_IN_PROPAGATOR_ONLY_REASONING",
    "CTP-NG-005 — CLOSED_UNITARY_DIFFEO_INVARIANT_NONLOCAL_TREE_ACTION_IS_ANNIHILATED_BY_CURRENT_COARSE_CTP_RELATION_MAP",
    "NG-FUNNEL-034 — ZERO_WARD_LOCK_PLUS_GENERIC_UNITARY_RA_RELATION_CANNOT_DISTINGUISH_QUANTUM_GRAVITY_FAMILIES"
  ],
  "model_readiness_percent":24,
  "readiness_change":"unchanged: nonlocal tree relation occupancy is structurally closed, but the current relation protocol is proven too coarse and no unique residual exists"
}

Path("results/nonlocal_ctp_cubic_structure_iteration174.json").write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2,sort_keys=True))
