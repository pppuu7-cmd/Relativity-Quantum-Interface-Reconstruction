# RQIR Candidate Gravity Recovery Delta — Iteration 337

Date: 2026-09-03

MODEL_READINESS: 24%

## Authority

Iteration 337 closes the repository-internal conversion from the normalized angular mean used by the determinant Cutkosky gates to the repository-normalized discontinuity operator `D_s`, for ordinary two-particle cuts with two simple massless cut propagators.

Freeze:

`PASS_REPOSITORY_NORMALIZED_SIMPLE_TWO_PARTICLE_CUT_CONVERSION__DET_OUTER_EFFECTIVE_ACTION_FACTOR_REMAINS_BLOCKED`

Validated Actions provenance:

- run `33756194728`
- job `100651082826`
- head/workflow commit `456b0e94830415ec1d02573f2b9b0864b1e1bcdb`
- code commit `b6f661c75d8fe2dff11ce6260a106ae361428ae8`
- artifact `9893533178`, `iteration337-result`
- artifact digest `sha256:aaeca20e2906d240417b6c9d301639068c62076f11281694525a5263d1096161`
- scientific JSON SHA-256 `7d6ba8fd46c01ccfb9af79b21932daa49787587122c47e51af85d8d7997bad64`
- exactly one top-level JSON object, sentinel `337`, `scientific_authority_pass=true`.

## Derivation

Iteration 296 freezes, in the repository loop normalization `i*pi^(D/2)`,

`D_s F = (F_advanced - F_retarded)/(2*pi*i)`

and calibrates the ordinary massless scalar bubble to

`D_s B -> -1`.

Iteration 336 independently freezes the standard 4D massless two-particle phase-space geometry

`int dPhi2 = 1/(8*pi)`

and

`int dPhi2 F = sphere_mean(F)/(8*pi)`.

Matching these two frozen normalizations on the unit scalar bubble gives the repository-normalized ordinary simple-cut bridge

`D_s I[F] = -8*pi * int dPhi2 F = - sphere_mean(F)`.

Numerically the calibrated phase-space factor is `-25.132741228718345 = -8*pi`, the normalized-sphere-mean factor is exactly `-1`, and both closure errors are zero in the scientific artifact.

## Scope boundary

Authorized:

- ordinary two-particle cuts with two simple massless cut propagators;
- the same advanced/retarded orientation as Iteration 296;
- the same repository loop normalization;
- ordinary uncut numerator/propagator factors evaluated on the same shell.

Not authorized by this gate:

- raised cut propagators / derivative delta distributions;
- overlapping singular cuts;
- full finite DR remainder;
- source/Ward/contact completion;
- matched `K2` subtraction;
- the common outer determinant effective-action `i` factor.

The last item is intentionally left to the independent Iteration 338 same-parent prefactor audit; Iteration 337 does not synthesize the connection-sector `-i/2` coefficient into the determinant sector.

## Readiness

MODEL_READINESS remains 24%. This closes a hard normalization prerequisite but does not create a comparator-subtracted residual or close a readiness rubric bucket.

## Next gate

Use independent same-parent effective-action authority to freeze the common determinant outer factor. Once that is closed, combine it with this `sphere_mean -> D_s` bridge. Iteration 335 remains independently responsible for the unresolved `q^2=-1` triangle angular-convergence channel; do not weaken its threshold.
