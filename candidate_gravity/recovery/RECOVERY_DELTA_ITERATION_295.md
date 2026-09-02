# Recovery Delta — Iteration 295

**Date:** 2026-09-03  
**MODEL_READINESS:** **24%**  
**Authoritative classification:** `PASS_DIRECT_TIMELIKE_S0016_WEIGHT_COMPLETED_TRU1_ALL_FAMILY_NUMERATOR_RECONSTRUCTION`

## What closed

The complete weight-completed cubic `Tr U1` insertion has now been reconstructed directly at the frozen timelike row `s=0.016`, rather than by rotating denominators while retaining checkpoint/spacelike numerator coefficients.

Validated certificate:

- 36 primitive branches;
- 8 non-scaleless families;
- primitive/direct trace residual `6.485922909860165e-13`;
- maximum held-out reconstruction error `4.842076903979733e-09`;
- maximum oracle imaginary contamination `0.0`.

Actions provenance:

- run `33688456731`;
- job `100441403084`;
- artifact `9869280530` (`iteration295-result`);
- digest `sha256:2c702d3aef66d052b63553590114900b2754b98e6871762ca3bda9ed8ec9ee77`;
- workflow head `634e4b00d764ed79ffb952218853b32d9641960c`.

## Interpretation

Iteration 295 is numerator-family authority for the actual `e=1,c=2` `Tr U1` sector on the frozen timelike point. It is not an integrated cut and not a Candidate Gravity residual.

The Iteration-289 pole of the old scalar weighted-kernel proxy `tr(B3)` remains non-authoritative for `Tr U1` and must not be reused.

## Exact next gate

Iteration 296:

1. consume the direct timelike family coefficients produced by the Iteration-295 parent/oracle;
2. use one common `i*pi^(D/2)` dimensional-regularization normalization across ordinary and raised bubble/triangle sectors;
3. compute explicit `+i0` and `-i0` branches;
4. record raw epsilon scans before fitting;
5. fit Laurent structure, never naive finite-epsilon polynomial extrapolation;
6. extract the actual `e=1,c=2` `Tr U1` pole and discontinuity;
7. do not perform source/Born subtraction until the pole origin is classified in a matched source-completed observable.

After this, active C5 sectors still include connection `e=2,c<=1` and determinant `e=0,c<=3`. Generic `e=3,c=0` remains null-soft killed by Iteration 246.

## Guardrails

No robust Candidate Gravity residual exists. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. Blind heavy full-C5 remains unauthorized.

Readiness change from Iteration 294: `+0` percentage points. `MODEL_READINESS: 24%`.
