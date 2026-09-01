# RQIR Research Log — Iteration 244

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Goal

Recover the exact Vilkovisky reduced insertion series through the `O(E^3)` sector required by Iteration 243, without extrapolating cubic coefficients from the UV-truncated 4D expression.

## Result

Primary Cho–Kantowski general gauge-theory authority gives the reduced unique-action series in `U1,U2` through `O(E^5)`. The published sequence is exactly reproduced, under cyclic trace equivalence and without commuting `U1,U2`, by

`-1/2 Tr log(1 - U1 + U2)`.

Mapping to the sign convention of Giacchini–de Paula Netto–Shapiro Eq. (14) gives

`Gamma_conn = +(i/2) Tr log(1 - U1 + U2)`

and therefore the required cubic sector

`Gamma_conn^(3) = +(i/2) Tr(U1 U2) - (i/6) Tr(U1^3)`.

The Iteration-243 primitive `U3` placeholder is superseded: the reduced series closes on `U1,U2` at cubic EOM degree.

## Classification

`PASS_EXACT_VD_OEPS3_INSERTION_SERIES_IDENTITY`.

Previous blocker is narrowed to

`BLOCKED_COMPOSITE_U1_U2_TRACES_TO_FINITE_CPT3_MASTER_MAP_AND_PURE_GRAVITY_PROJECTION`.

## Heavy compute

Full finite-CPT3 heavy calculation remains not authorized. The composite trace map must be frozen first.

## Readiness

`MODEL_READINESS: 24%` — unchanged from Iteration 243. A real C5 authority gap was closed, but the physical finite cubic comparator column is still not computed.

## Next

Iteration 245: freeze the explicit inverse-operator content of `U1,U2`, classify the required trace sectors, and determine whether standard CPT3 directly applies or a mixed-resolvent/flat-kernel reduction is required.
