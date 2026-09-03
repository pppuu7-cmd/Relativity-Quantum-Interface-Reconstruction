# Recovery Delta — Candidate Gravity Iteration 361

Date: 2026-09-03

## Scope

Normalized channel-resolved ordinary-simple `Tr U2` cut integration for only the 36 Iteration-360 `REGULAR` channels, using the frozen Iteration-337 bridge `D_s I[F] = -sphere_mean(F)`. Physical ghost/graviton propagator signs remain explicit. Distinct external timelike `q^2` discontinuities are not mixed. Repeated-pole families are excluded and remain governed by Iteration 359.

## Raw Actions authority

- authoritative run: `33795340192`
- job: `100781555423`
- artifact: `9909223767` (`iteration361-result`)
- artifact digest: `sha256:8473b567e8d7188b35f3472b1e33c309b12749596fbfe00dd2490a6c8b7c4d90`
- raw scientific JSON SHA-256: `c3d6a916a42faf560ac1196cff789de5ba2384b94864c4a9284dfbd7dc96c0ec`
- workflow head: `02ae17bfe6f2a89d918e1c904373bd71dd06e12c`

The artifact authority audit reports exactly one top-level Iteration-361 object, expected sentinel `361`, and `scientific_authority_pass=true`.

## Result

Authority:

`PASS_U2_SIMPLE_NORMALIZED_CHANNEL_CUT_CLASSIFICATION__ALL_CONVERGED__Q2_RESOLVED_SIMPLE_SECTOR_CANCELS_TO_ZERO`.

Census:
- typed ordinary-simple channels: `36`;
- `CONVERGED`: `36`;
- `BLOCKED_CONVERGENCE`: `0`;
- q2 buckets: `3`;
- maximum cut-shell error: `3.1176990904323794e-16`;
- maximum scaled convergence error: `2.481513269677227e-10`, far below the frozen `2e-5` threshold;
- minimum sampled uncut denominator magnitude: `0.12097829436145643`.

The normalized ordinary-simple sector sums, kept separately by discontinuity variable, are:
- `q^2=-0.14`: `D_s TrU2_simple = 0.0`;
- `q^2=-0.34`: `D_s TrU2_simple = 0.0`;
- `q^2=-1.0`: `D_s TrU2_simple = 0.0`.

The raw channel table contains nonzero positive and negative contributions which cancel within each q2 bucket. Therefore this is a scoped ordinary-simple-sector cancellation, not evidence that each channel vanishes and not evidence that the full `Tr U2` contribution vanishes.

Strict interpretation:
- not a consistency FAIL;
- not an exact comparator identity;
- not regime-specific non-identifiability;
- not near-degeneracy;
- not a novelty certificate;
- not a Candidate residual;
- repeated-pole U2 remains unresolved and cannot be zero-filled from this cancellation.

The Iteration-308 effective-action coefficient `+(i/2) Tr U2 -(i/4) Tr U1^2` is still separate and was not folded into the stored coordinate.

## Exact next gate

Proceed only on the repeated-pole branch frozen in Iteration 359. For each of the 30 families with one unique double-pole momentum group, introduce one auxiliary `mu^2`, represent the double pole as one derivative with the same `i0`, derive the corresponding simple-massive channel cut, differentiate once and take `mu^2 -> 0`. Validate the derivative/distributional implementation against an independent smooth test-function oracle before physical repeated-pole integration.

Do not use ordinary simple-cut substitution for repeated poles. Do not perform Source/Born subtraction yet. No comparator-subtracted residual exists.

MODEL_READINESS: 24%

Change from Iteration 360: `0 pp`. The full ordinary-simple U2 cut sub-sector is now closed and cancels within each q2 bucket, but the repeated-pole U2 sector is unresolved; no full readiness-rubric bucket and no robust comparator-subtracted residual closed.
