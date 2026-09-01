# RQIR Candidate Gravity — Iteration 225

## MSSC-001 singularity-adapted global hard remainder

Iteration 224 left the Born-subtracted connected scalar-source cut numerically BLOCKED because a global cap mask sampled by two tensor-product angular charts produced up to 13.819% chart disagreement. Iteration 225 does not modify the physics subtraction. The Iteration-222 authority

`R_in = R_out = -8 M_Born`

and the Iteration-223 local `delta^2` cap-shell result remain frozen.

The numerical change is geometric. Let `c_in=-z` and `c_out=n_out` be the two certified collinear directions. Partition the sphere into their exact spherical Voronoi cells. In a local polar chart centered on either cell generator `c`, with the other generator separated by angle `gamma`, the equidistant great-circle boundary is

`rho_max(phi) = atan2(1-cos(gamma), sin(gamma) cos(phi))`.

Thus every cell is integrated directly in `(rho,phi)` with measure `sin(rho) d rho d phi`; the singular direction is the coordinate origin and no discontinuous cap-excision indicator is sampled by a global grid.

Two independent deterministic cubatures were used on this same exact decomposition:

1. Gauss-Legendre in local radius and periodic midpoint in azimuth;
2. Gauss-Legendre in local radius and Gauss-Legendre in azimuth.

Across the frozen five scattering angles `{0.45,0.8,1.15,1.6,2.1}` and both independent external linear spin-2 polarizations, at order 32 the maximum relative difference is

`2.584334806770234e-7`.

The slowest two rows are both at `theta_ext=2.1`. Increasing both cubatures to order 40 reduces their disagreements to

- plus: `6.045121421330798e-9`;
- cross: `6.135670833005235e-9`.

A conservative frozen relative numerical acceptance envelope of `3e-7` therefore contains every order-32 row, while the explicit order-40 stress test shows that the worst rows continue converging well inside that envelope.

## Classification

- local IR completion: `PASS_FROM_ITERATION223`;
- global finite source hard remainder: `PASS_NUMERICAL_GLOBAL_COMPLETION`;
- previous `BLOCKED_NUMERICAL_BULK_HARD_REMAINDER`: resolved numerically;
- consistency FAIL: `NO`;
- exact comparator identity: `NO`;
- regime-specific non-identifiability: `NO` for this numerical gate;
- near-degeneracy: `NO`;
- Candidate Gravity novelty: `NONE`.

Retain:

- `NUM-NG-014 — SINGULARITY_ADAPTED_VORONOI_CUBATURE_REMOVES_THE_GLOBAL_CHART_ALIASING_BLOCKER`;
- `SRC-CUT-006 — MSSC001_BORN_SUBTRACTED_GLOBAL_HARD_REMAINDER_IS_NUMERICALLY_STABLE_ACROSS_TWO_INDEPENDENT_CUBATURES`;
- `NG-FUNNEL-081 — NUMERICAL_SOURCE_COMPARATOR_CLOSURE_IS_COMPARATOR_AUTHORITY_NOT_CANDIDATE_NOVELTY`.

The important guardrail is that this is comparator closure, not a Candidate Gravity residual. `ANSATZ-003` remains forbidden. AS and C3 real-time nonlinear authority remain BLOCKED and must not be zero-filled. Fisher/resources remain forbidden.

## Readiness

`MODEL_READINESS: 24%`.

Change from Iteration 224: `+1 percentage point`, assigned only to comparator foundation because an actually blocked comparator component — the finite global `MSSC-001` hard remainder — is now numerically completed. No other rubric component changes.

## Next gate

Use the now stable finite `MSSC-001` source hard remainder to extract its frozen nonanalytic regular+log structure and compare that structure with the already separate pure-graviton positive control without identifying the two observables. Then resume the missing AS/C3 authority audit. No candidate residual may be promoted unless it survives the full fixed comparator quotient.
