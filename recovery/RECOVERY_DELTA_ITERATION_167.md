# RQIR Candidate Gravity — Recovery Delta Iteration 167

**Date:** 2026-08-31  
**Authoritative predecessor:** Iteration 166  
**MODEL_READINESS:** 24% (unchanged)

## New protocol clarification

The timelike `A_odd` introduced in Iteration 166 is the frequency-odd imaginary part of the **linear** susceptibility `chi1R`:

`A_odd=[Im chi1R(+omega)-Im chi1R(-omega)]/(2*pi)`.

It is not the post-Gaussian `chi2R_odd` coordinate.

## Linear conserved-TT source map

On the eight timelike rows use

`k=(omega,0,0,0)`

and

`T_0mu=0`, `T_ij=diag(1,-1,0)/sqrt(2)`.

All eight rows satisfy exact numerical conservation/traceless/projector tests; `T:P2:T=1` within `2.22e-16`.

Therefore the source overlap is frequency-independent and the scoped source-to-source TT response preserves the propagator spectral shape up to a common gain.

Retain:

`ABS-SHAPE-001 — CONSERVED_TT_SOURCE_MAP_PRESERVES_TIMELIKE_SPECTRAL_SHAPE`.

## Constant-log-null quotient

Let `x=s/s_max=i/8`. QR factorisation of `[1,x,...,x^7]` defines one normalized constant direction and a seven-dimensional orthonormal complement `Q_shape`.

Numerical certificate:

- `max |Q_shape^T 1| = 2.22e-16`;
- orthonormality error `4.44e-16`;
- projected norm of leading C5 massless log `3.80e-16`;
- projected norm of leading AS IR log `1.44e-16`.

The target-independent capacity family `(x,x^2,x^3)` retains rank `3/3` after projection.

Retain:

`ABS-SHAPE-002 — CONSTANT_LOG_NULL_QUOTIENT_LEAVES_SEVEN_SUBLEADING_SHAPE_DIMENSIONS`.

`NG-FUNNEL-026 — PROFILE_UNIVERSAL_IR_LOG_BEFORE_SUBLEADING_SPECTRAL_SHAPE_SEARCH`.

## AS literature refinement

`AS-LOR-SPEC-002` is updated to the journal publication:

Pawlowski, Reichert, Wessely, Physics Letters B 880 (2026) 140844, DOI `10.1016/j.physletb.2026.140844`, arXiv:2507.22169.

The published spectral continuum is not constant at finite frequency; it decreases at intermediate scales. The repository has no numerical data table for this curve and has not reproduced the spectral flow.

Therefore finite-frequency AS shape remains

`BLOCKED_NUMERICAL_SPECTRAL_DATA_OR_CONTROLLED_REPRODUCTION_REQUIRED`.

Retain:

`NG-FUNNEL-027 — PUBLISHED_SPECTRAL_CURVE_IS_NOT_A_NUMERICAL_COMPARATOR_COLUMN_WITHOUT_DATA_OR_CONTROLLED_REPRODUCTION`.

## Candidate state

No comparator-subtracted sub-leading shape is defined.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
Readiness: 24%.

## Authorities

- `analysis/absorptive_shape_quotient_iteration167.py`;
- `results/absorptive_shape_quotient_iteration167.json`;
- `candidate_gravity/ABSORPTIVE_SHAPE_QUOTIENT_ITERATION167.md`;
- updated `candidate_gravity/comparators/AS-LOR-SPEC-002.md`;
- this recovery delta.

## Exact next gate — Iteration 168

Freeze C5 loop/power-counting order in the same conserved-TT linear absorptive channel. Determine which complete one-loop massless nonanalytic two-point structures survive the constant-log quotient and classify higher-loop / higher-derivative-insertion shapes as either explicit comparator columns or controlled truncation uncertainty rather than silently ignoring them.
