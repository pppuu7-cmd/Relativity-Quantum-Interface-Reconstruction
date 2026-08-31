# Post-Gaussian Finite RQIR Quotient Template

**Iteration:** 144  
**Status:** infrastructure / no model-specific discovery claim

## Purpose

Before freezing or optimizing a post-Gaussian Candidate Gravity model, reduce its predicted observables to a finite vector and determine whether the candidate direction lies outside the exact span of calibration, nuisance and comparator directions.

This template is the higher-order analogue of the finite hard-constraint quotient used in RQIR Paper I.

## 1. Finite observable vector

For a chosen finite source/detector protocol define

`y = (y1_mean, y2_sym, y1R, y3_sym, y2R, yWard, ...)`.

The coordinates may contain, for example:

- calibrated mean/static response;
- symmetrized two-point covariance;
- linear retarded response;
- fully symmetrized connected third cumulant;
- second-order ordered/causal response;
- one or more finite Ward/soft consistency combinations.

Every coordinate must be an actual finite smeared/renormalized observable. Formal unsmeared field components are not accepted as detector coordinates.

## 2. Exact hard constraints

Collect exact calibration/symmetry constraints as

`H y = h`.

Linearizing around the baseline gives allowed tangent vectors `v` satisfying

`H v = 0`.

Let `Q_H` be a matrix whose columns form a basis for `null(H)`. Work only in reduced coordinates

`v_red = Q_H^T v`.

Hard constraints are eliminated before any profiling or Fisher calculation.

## 3. Candidate direction

For model parameter `beta`,

`v_beta = partial y / partial beta |_(beta=0)`.

The post-Gaussian contract requires the components of `v_beta` to be derived from one parent dynamics. In particular, `y3_sym` and `y2R` may not be independently tuned merely to evade comparators.

## 4. Nuisance tangent space

Build columns for all applicable nuisance directions:

`V_nuis = [v_source, v_gain, v_phase, v_timing, v_geometry, v_detector_nonlin, v_source_C3, ...]`.

Post-Gaussian work must include detector and source higher-cumulant nuisance directions when they can mimic the candidate.

## 5. Comparator tangent blocks

Construct separate finite tangent blocks:

### C3 classical/hybrid block

`V_C3`

must include all allowed classical stochastic higher-cumulant and nonlinear-response directions of the frozen comparator realization.

Do not set its third cumulant to zero merely because the metric is classical.

### C4 quantum mediator block

`V_C4`

must include nonlinear self-interaction directions of the allowed hidden/KK/massive-spin-2 mediator EFT, not only its Gaussian propagator.

### C5 perturbative quantum-GR block

`V_C5`

must include the declared-order tree/loop/higher-dimension operator directions and the same renormalization convention as the candidate baseline.

### Other strong quantum-gravity blocks

Add `V_NL`, `V_AS`, etc. when fixed nonlocal/form-factor or asymptotic-safety comparator models are applicable.

## 6. Combined comparator matrix

After hard-constraint reduction,

`M = Q_H^T [V_nuis, V_C3, V_C4, V_C5, V_NL, V_AS, ...]`.

Candidate reduced direction:

`b = Q_H^T v_beta`.

The first operational novelty gate is

`b notin Col(M)`.

Numerically use a rank/SVD certificate with a frozen tolerance tied to the calculation error budget, not an arbitrary display tolerance.

Equivalent rank test:

`rank([M,b]) > rank(M)`.

## 7. Residual projector

When the Euclidean metric in observable space is appropriate for the algebraic gate, define

`P_perp = I - M M^+`,

where `M^+` is the Moore–Penrose pseudoinverse in the reduced coordinates.

Then

`r_beta = P_perp b`.

A necessary Paper-I condition is

`||r_beta|| > numerical/modeling error bound`.

For statistically weighted geometry replace this only **after** the exact hard-constraint and algebraic identity checks are complete.

## 8. Ward/soft locking as a constraint, not a bonus observable

If the model predicts an exact finite Ward/soft relation

`L y = 0`,

append it to `H` whenever it is an exact identity shared by the candidate parameter family.

If a comparator does not obey the same identity, do not simply remove it by hand. Its predictions must be evaluated in the same full observable space; failure of the relation can itself contribute to distinguishability.

The distinction between:

- exact model identity;
- calibration constraint;
- measured consistency test

must be explicit.

## 9. Symmetric-vs-ordered test

Define selector matrices `S_sym` and `S_ord` for symmetric cumulant and ordered nonlinear-response coordinates.

Record separately:

`r_sym = S_sym r_beta`,

`r_ord = S_ord r_beta`.

A candidate whose only residual is `r_sym` must still be tested against the full classical stochastic C3 comparator family. A genuinely useful post-Gaussian search should preferentially retain a nonzero ordered component after C3 profiling.

This is a design criterion, not a theorem that every classical/hybrid model has zero ordered operational response.

## 10. Model-free pre-screen

Before heavy detector work, reject a proposed ansatz design if its formal tangent is visibly contained in an existing comparator block by construction. Examples already established by the project:

- standard perturbative QG ansatz in C5;
- positive Gaussian KL continuum in C4/KK;
- finite-order deep-IR gapped continuum in local C5 EFT Wilson directions.

## 11. Required certificate for `ANSATZ-003`

The first version of the next model must eventually produce:

- finite observable vector definition;
- hard-constraint matrix `H`;
- candidate tangent `v_beta`;
- nuisance matrix;
- at least C3/C4/C5 comparator matrices;
- SVD/rank tolerances and numerical error bound;
- residual vector `r_beta`;
- decomposition into symmetric and ordered residual sectors;
- authority links from every vector component back to the same parent dynamics.

No `QG-008 PASS` is allowed without this package.
