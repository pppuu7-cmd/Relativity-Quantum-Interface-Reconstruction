# Candidate Gravity Article / Negative-Results Matrix — Iteration 251

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

| ID | Scoped result | Classification | Article use / provenance |
|---|---|---|---|
| C5-CUT-029 | In frozen `D=4`, `Lambda=0`, `a=-1/2` convention the first TT-background variation of `N^alpha_beta = delta Box + R` is an explicit local quadratic momentum polynomial. | `PASS_SCOPED_E1_GHOST_RESOLVENT_VERTEX_FREEZE_AND_TT_VALIDATION` | Positive methods/result; code `candidate_gravity/code/iteration251_vd_e1_ghost_resolvent_vertex.py`, result JSON, primary VD operator authority Giacchini–de Paula Netto–Shapiro (2020). |
| C5-CUT-030 | Independent finite differentiation of the full covariant vector-Laplacian-plus-Ricci operator reproduces the analytic `delta N` vertex to `8.01e-11` max component error on the frozen hard TT test. | reproducibility/unit PASS | Methods validation; do not interpret as physical comparator closure. |
| C5-CUT-031 | `delta(N^-1) = -N0^-1 deltaN N0^-1` must occur on both ghost inverses of `U1` in the `E^(2)K^(1)` cubic sector. | exact resolvent identity | Algebra/reduction section. |
| C5-NG-014 | A first-order ghost-resolvent insertion raises/repeats an existing ghost segment but does not create a fourth independent loop-momentum corner. | scoped no-new-topology result | Negative/computational reduction; reinforces Iteration-250 bubble/triangle bound. |
| C5-BLOCK-006 | The explicit ghost-resolvent vertex alone is not the complete `E^(2)K^(1)` `Tr U1` numerator: `delta[R(DR)]`, `delta Y`, `E^(3)`, surviving `E^(1)K^(2)` and `e=2` remain. | operational `BLOCKED_NOT_ZERO` | Negative-results / authority boundary; prevents premature C5 or residual claims. |
| NG-FUNNEL-097 | No Candidate Gravity residual is promoted from a nonzero VD numerator subblock. | no novelty certificate | Article funnel guardrail; `ANSATZ-003` withheld, Fisher/resources forbidden. |

## Exact formula retained

For TT `h_mu_nu = epsilon_mu_nu exp(i q.x)`,

`delta N^alpha_beta = (epsilon^{mu nu} p_mu p_nu) delta^alpha_beta - (p.q) epsilon^alpha_beta - q_beta p_mu epsilon^{alpha mu} + q^alpha p_mu epsilon^mu_beta`.

The derivative-free linearized curvature pieces cancel between the vector covariant Laplacian and explicit Ricci term in the frozen TT specialization.

## Classification discipline

Iteration 251 is **not** a consistency FAIL, exact comparator identity, near-degeneracy, regime-specific non-identifiability, or novelty certificate. It is a scoped algebraic/reproducibility PASS inside a still operationally BLOCKED C5 construction.
