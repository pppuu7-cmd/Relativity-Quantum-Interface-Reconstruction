# RQIR Candidate Gravity research log — Iteration 259

**Date:** 2026-09-02  
**MODEL_READINESS: 24%**

Started from authoritative Iteration 258 after reading `candidate_gravity/recovery/CURRENT_QG_FRONT.md`, `recovery/RECOVERY_DELTA_ITERATION_258.md`, the Iteration-258 research log, recent commits, and GitHub Actions. Recent commits confirmed Iteration 258 as the actual front. Actions reported zero workflow runs, so no computation was duplicated.

## Work performed

1. Preserved the frozen Iteration-252 factorization `Nhat=W N_orb` and the Iteration-258 physical `N2`; no new ansatz was introduced.
2. Constructed the physical inverse `Q=N_orb^-1` only from the same-parent orbit metric.
3. Used exact coefficient matching of `N_orb Q=I`:
   - `Q0=N0^-1`,
   - `Q1=-Q0N1Q0`,
   - `Q2=Q0N1Q0N1Q0-Q0N2Q0`.
4. Independently formed `Q(t)=N_orb(t)^-1` on the same finite-amplitude TT background used in Iteration 258 and extracted direct finite-difference coefficients.
5. At `h=1e-4`, obtained
   - `max|Q1_direct-Q1_recursion|=3.2350440104522704e-8`,
   - `max|Q2_direct-Q2_recursion|=6.316712886089704e-8`,
   - `||Q2||_F=3.90439593779004`.
6. The mismatch decreases approximately quadratically over the tested step sequence, providing an independent direct-inverse certificate for the physical second-order resolvent coefficient.

Freeze:

`PASS_SCOPED_PHYSICAL_Q2_RECURSION_AND_DIRECT_INVERSE_VALIDATION`

and retain guardrail

`NO_INDEPENDENT_Q2_ANSATZ`.

This is a scoped comparator-authority PASS, not a complete C5 comparator coordinate, Candidate Gravity residual, exact comparator identity, regime-specific non-identifiability, near-degeneracy, consistency FAIL, or novelty certificate.

Retain

`BLOCKED_4D_EINSTEIN_VD_RESOLVENT_VERTEX_LIBRARY_TENSOR_REDUCTION_AND_SOURCE_PROJECTION`

and `BLOCKED_NOT_ZERO`.

`ANSATZ-003`: NOT CREATED. Fisher/resources: FORBIDDEN. Heavy integration: NOT RUN.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 258: **0 percentage points**. The physical `Q` sector through second order is now constructively fixed and independently validated, but no complete C5 comparator coordinate or robust nonzero residual closes a readiness-rubric category. Comparator foundation remains `24/25`; unique residual remains `0/20`.

## Exact next gate

Complete the same-parent physical `A1,A2,A3`, with `A3=K0E3+K1E2+K2E1`. Then assemble all six terms of `B3=[U1W]_3` using the now-fixed `Q0,Q1,Q2` and apply the weighted pairwise transpose/index/TT certificate before tensor reduction. Do not test ordinary `U1` symmetry, do not introduce an independent resolvent coefficient, and do not launch heavy integration, Fisher/resources, or `ANSATZ-003`.
