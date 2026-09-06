# RECOVERY DELTA — ITERATION 495

Date: 2026-09-06
MODEL_READINESS: 24%

## New exact estimator/provenance authority
For frozen central4 nodes `[-2,-1,+1,+2]` with `c=[1/12,-2/3,2/3,-1/12]`, exact rational moments through degree four are `M_0..M_4=[0,1,0,0,0]`.

The mixed tensor estimator therefore has factorized monomial moments `M_ab=M_a M_b`; for `0<=a,b<=4`, only `M_11=1` is nonzero. Thus every bivariate polynomial of degree <=4 in each variable is reproduced exactly at the mixed-derivative level: `D_h p(0,0)=partial_x partial_y p(0,0)` for every nonzero `h`, including exact bilinear normalization `D_h(x*y)=1`.

Because each row and column sum of `w_ij=c_i c_j` vanishes exactly, every arbitrary sampled additive field `F_ij=f_i+g_j+const` is annihilated exactly, with no polynomial assumption.

Classification: `PASS_CENTRAL4_TENSOR_NULLSPACE_POLYNOMIAL_REPRODUCTION_EXACT__NON_PROMOTING`.

This is a future BASE/HALF assembly unit contract only. Violations are implementation/provenance `BLOCKED`, not Candidate-Gravity consistency FAIL. No frozen threshold, dynamics, support order, precision convention, BASE/HALF rule or `ds=-d_base` convention changes.

Reproducible audit: `candidate_gravity/code/iteration495_central4_tensor_reproduction_audit.py`.
Machine-readable result: `candidate_gravity/results/iteration495_central4_tensor_reproduction_audit.json`.

## Active numerical gate
Canonical frozen rank17 `(u,v)=(-5e-6,+2.5e-6)`, multiplicity 1, run `34023698421`, job `101460814699`, remains `in_progress`. No duplicate heavy run was launched. Certified occurrence coverage remains `21/32 = 65.625%` pending raw consumption.

## Retained blockers
Physical/operator authority remains Iteration 411. Iteration 421 remains raw-valid `BLOCKED_CONVERGENCE` for unresolved set `[2]`. Robust comparator-subtracted residual is absent. `ANSATZ-003` and Fisher/resources remain BLOCKED.

## Readiness
MODEL_READINESS: 24%
Readiness change: 0 percentage points. The exact assembly unit contract closes a provenance subgate but no additional stable-rubric component.

## Exact next gate
Fail-closed raw-consume rank17 run `34023698421`. Only if raw PASS may the next explicit UNTESTED Iteration-455 coordinate be authorized; if BLOCKED, localize the first failing `z/phi/radial` sample without changing frozen conventions.
