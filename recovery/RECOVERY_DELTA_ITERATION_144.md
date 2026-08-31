# Recovery Delta — Candidate Gravity Iteration 144

**Date:** 2026-08-31  
**Authoritative front:** Iteration 144

## Current registry state

No promotable ansatz is active.

Permanent branches:

1. `ANSATZ-PQG-EFT-001` — C5 reference, novelty-degenerate (`CG-NG-003`).
2. `ANSATZ-RQIR-CTP-001` v0.1 — rejected on Lorentzian consistency (`CG-NG-004`).
3. `ANSATZ-RQIR-KL-002` v0.1 — positive-spectral Gaussian control, QG-007 failed by exact C4/KK mediator equivalence (`CG-NG-006`); also deep-IR C5 EFT degeneracy (`CG-NG-005`).

## New Iteration-142 result

Existing nonlinear theories show that nonlinearity itself is not enough:

- covariant nonlocal gravity generates nonlinear momentum-dependent vertices;
- asymptotic-safety vertex expansions compute `Gamma^(2/3/4)`;
- dRGT massive gravity has constrained nonlinear spin-2 interactions;
- postquantum classical gravity has nonlinear stochastic CQ path-integral dynamics.

Exported lesson:

`nonzero C3 / nonlinear vertex != gravity-specific novelty`.

Authority:

`candidate_gravity/landscape/RQIR_NONLINEAR_COMPARATOR_AUDIT_ITERATION142.md`.

## New Iteration-143 contract

Future post-Gaussian candidates must derive, from one parent dynamics:

- Gaussian layer `J,N,chi^(1)R`;
- fully symmetrized connected third cumulant `C3_sym`;
- causal second-order susceptibility built from nested commutators / equivalent ordered CTP components;
- Ward/soft/constraint identity tying higher response to the same gravitational coupling.

Authority:

`candidate_gravity/POST_GAUSSIAN_MODEL_TO_RQIR_CONTRACT.md`.

## New Iteration-144 finite quotient

For finite observable vector `y`, hard constraints `H y=h` are eliminated first using a nullspace basis `Q_H`.

Candidate reduced tangent:

`b=Q_H^T v_beta`.

Combined reduced nuisance/comparator matrix:

`M=Q_H^T[V_nuis,V_C3,V_C4,V_C5,V_NL,V_AS,...]`.

Necessary algebraic novelty condition:

`rank([M,b]) > rank(M)`

with residual

`r_beta=(I-MM^+)b`

above the numerical/modeling error bound.

Symmetric and ordered residual sectors must be reported separately.

Authorities:

- `candidate_gravity/POST_GAUSSIAN_FINITE_QUOTIENT_TEMPLATE.md`;
- `analysis/post_gaussian_quotient_validator_iteration144.py`.

## Article scaffolds

- `docs/CANDIDATE_GRAVITY_ARTICLE_FUNNEL_SECTION_ITERATION137.md`;
- `docs/CANDIDATE_GRAVITY_ARTICLE_NEGATIVE_RESULTS_MATRIX_ITERATION143.md`.

These are suitable as a basis for describing failed/non-identifying controls in the eventual model paper, with the strict rule that RQIR promotion failure is not automatically global falsification.

## Exact restart instruction — Iteration 145

Do not invent the next action first.

Instead:

1. freeze a finite post-Gaussian observable protocol;
2. instantiate comparator tangent spaces for at least C3/C4/C5;
3. identify a residual ordered Ward/soft-locked direction outside the combined span;
4. only then construct the minimal covariant parent dynamics (`ANSATZ-003`) that generates this residual while returning exactly to the chosen C5 baseline at `beta=0`;
5. immediately test whether fixed nonlocal/asymptotic-safety/massive-spin-2 comparators already contain that direction.

If no residual direction exists, record that negative result and enlarge the observable hierarchy before constructing another model.
