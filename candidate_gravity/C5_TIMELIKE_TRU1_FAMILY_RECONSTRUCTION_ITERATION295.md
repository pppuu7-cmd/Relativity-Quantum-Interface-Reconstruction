# Candidate Gravity C5 — Iteration 295 direct timelike Tr U1 family reconstruction

**Date:** 2026-09-03  
**MODEL_READINESS:** **24%**

## Purpose

Close the numerator-reconstruction prerequisite for the actual weight-completed one-loop Vilkovisky insertion `[Tr U1]_{sab}` directly on the timelike cut geometry, without analytically continuing numerator coefficients from the earlier checkpoint/spacelike reconstruction.

Frozen row:

- `s=0.016`;
- `k_s^2=0`;
- `k_a^2=-0.016`;
- `k_b^2=-0.216`;
- `k_s.k_a=-0.1`.

The Iteration-292 complete trace census contains 36 primitive branches. After scaleless/null sectors are removed, eight non-scaleless denominator/numerator families remain.

## Validated numerical certificate

GitHub Actions run `33688456731`, job `100441403084`, completed successfully. Immutable artifact:

- artifact ID `9869280530`;
- name `iteration295-result`;
- digest `sha256:2c702d3aef66d052b63553590114900b2754b98e6871762ca3bda9ed8ec9ee77`;
- workflow head `634e4b00d764ed79ffb952218853b32d9641960c`.

Audited result:

- primitive branches: `36`;
- non-scaleless families: `8`;
- direct-vs-primitive absolute residual: `6.485922909860165e-13`;
- maximum held-out relative polynomial-reconstruction error: `4.842076903979733e-09`;
- maximum oracle imaginary contamination: `0.0`.

Classification:

`PASS_DIRECT_TIMELIKE_S0016_WEIGHT_COMPLETED_TRU1_ALL_FAMILY_NUMERATOR_RECONSTRUCTION`.

## Scope

This closes the direct-timelike numerator reconstruction prerequisite for the `e=1,c=2` `Tr U1` sector. It does **not** yet provide:

- the integrated dimensional-regularization result;
- a Laurent pole coefficient;
- a `+i0/-i0` discontinuity;
- source/Ward/Born-IR completion;
- the full C5 comparator coordinate;
- a comparator-subtracted Candidate Gravity residual.

The older Iteration-289 weighted-kernel proxy pole must not be imported into this calculation.

## Next gate

Iteration 296 must reduce the eight **directly timelike** families in one common DR normalization, evaluate the explicit `+i0` and `-i0` branches, inspect raw epsilon scans before fitting, perform a Laurent fit rather than naive finite-epsilon extrapolation, and extract the actual `e=1,c=2` `Tr U1` pole/discontinuity structure.

Source/Born subtraction remains downstream until the pole origin is classified in the matched observable.

`ANSATZ-003`: NOT CREATED.  
Fisher/resources: FORBIDDEN.  
MODEL_READINESS remains `24%` because no integrated comparator coordinate or robust unique residual has closed a readiness-rubric point.
