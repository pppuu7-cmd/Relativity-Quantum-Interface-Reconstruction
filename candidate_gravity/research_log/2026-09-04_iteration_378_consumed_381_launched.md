# Candidate Gravity Research Log — Iteration 378 consumed / Iteration 381 launched

**Date:** 2026-09-04  
**MODEL_READINESS:** 24%

Iteration 378 was consumed from the raw Actions artifact, not from workflow colour. The authority audit and an independent SHA-256 recomputation agree on `637756f51e7ee0338a8d531edc5f1d2d58541ad803aa7c5dfd2026e2f9d33355`.

The prospectively first frozen simple-double `Tr U1^2` channel (`class_id=2`, `q^2=-0.34`, multiplicities `2x1`) is `CONVERGED`: normalized `D_s Tr U1^2=-2.5401676390398016e-05`, scaled convergence error `2.3732431469379806e-11` under the unchanged `2e-5` threshold, maximum shell error `1.726049858596923e-16`, minimum sampled uncut denominator `0.2609889252677208`, and runtime `1312.8183083709998 s`.

This result validates only the pipeline/runtime. It does not authorize the remaining 35 channels by inference.

Using that measured runtime, Iteration 381 prospectively freezes a 12-job architecture with exactly three frozen channels per job and 90-minute timeout. Every channel uses the same Iteration-378 physical numerator, auxiliary-mass derivative, mass nodes, radial extrapolation, low/high/shifted angular grids, signs and thresholds. Full-sector authority requires all 12 raw artifacts plus an exact 36-index no-gap/no-overlap assembly.

- Iteration 381 evaluator commit: `54b9529feea1826a4382ef9141a3750957a4ee88`
- Iteration 381 workflow commit: `5ecb485240ffc39f4bd7b8950ec8963e7b06f92f`
- run: `33816213900`

Concurrent nonduplicated work at launch: Iteration 379 double-double pilot and Iteration 380 determinant `q^2=-1` analytic-azimuth reduction remained in progress. Iteration 376 recovery run `33813179996` had already ended `cancelled`, so it has no scientific PASS/FAIL authority and must not be counted as an active computation.

No readiness rubric point closes here. `ANSATZ-003` remains uncreated; Fisher/resources and source/Born subtraction remain forbidden.
