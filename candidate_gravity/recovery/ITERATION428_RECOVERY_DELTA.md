# Iteration 428 Recovery Delta

**Date:** 2026-09-04  
**MODEL_READINESS:** 24% (unchanged)  
**Authority:** conditioning / implementation audit; non-promoting  
**Raw-valid run:** 33887682539  
**Job:** 101071391720  
**Artifact:** 9942518066  
**Artifact digest:** `sha256:4cc83230f7571a08995ff2008fd9e3b0900e1908ac818019c12431e7345ccca3`  
**Raw scientific JSON SHA-256:** `d79330bb9ca0a5f8dbeffa012dde391f5e549c530db36f8a090d1477d62116a5`

## Result

The corrected Iteration-428 audit passed fail-closed. It explicitly keeps the Iteration-421 symmetric-cross geometry and the Iteration-424 high-precision fallback geometry distinct.

### Iteration 421 conditioning

For

`C(u,v) = [F(u,v)-F(u,-v)-F(-u,v)+F(-u,-v)]/(4uv)`

with `R=1e-5`, radius multipliers `{1, 0.75, 0.5, 0.25}`, and the unchanged physical tolerance `2e-5`, the allowed absolute perturbation of the complete signed four-corner numerator is

`delta_N_max = 4 |u v| * 2e-5`.

At the tightest frozen node `|u|=|v|=2.5e-6`, this is only

`delta_N_max = 5e-16`,

which is about `2.2518` binary64 machine epsilons at unit scale for the entire four-corner sum. If equally attributed to four independent corner evaluations, the nominal share is only `0.56295` machine epsilon per corner. This is an implementation-conditioning statement, not a proof that roundoff alone caused Iteration-421 BLOCKED_CONVERGENCE.

At the loosest `|u|=|v|=1e-5` node the corresponding budget is `8e-15`.

### Iteration 424 is a separate frozen geometry

The prospective Iteration-424 contract freezes mass steps

`[5e-6, 2.5e-6, 1.25e-6]`

and precision levels `[80, 120]` decimal digits, with `same_mass_nodes=True` and `no_smaller_h=True`. Its contract file does **not** by itself freeze a derivative-stencil formula. Therefore Iteration 428 does not reinterpret `h^2 * 2e-5` as an acceptance budget; those values are recorded only as conditioning scales.

## Precision-surface consequence

The complete fixed-mass `F` path used by the analytic/spectral representation calls the full stripped numerator and converts numerator samples to NumPy complex arrays. The inherited numerator path also contains nested finite-difference machinery (`first_u1`/`Asub`, `y1`). Therefore upgrading only outer analytic moments, polynomial fitting, or final mass extrapolation to `mpmath` would not justify the statement that `F` itself has been evaluated at 80/120 decimal digits.

A physical Iteration-424 implementation must either:

1. carry arbitrary precision through the complete fixed-mass `F` dependency chain; or
2. explicitly quantify each retained lower-precision sublayer strongly enough that the frozen physical and cross-precision conditions remain meaningful.

Until then, outer-only high precision is diagnostic, not physical authority.

## Current front

- Iteration 421: raw-valid `BLOCKED_CONVERGENCE`; index 2 not promoted.
- Iteration 424: now authorized by the 421 outcome, but implementation must preserve its frozen contract.
- Iteration 426: independent phi-mean 16-vs-32 diagnostic still running at this checkpoint.
- Iteration 427: exact non-promoting chain reduction remains available as an independent factorized consistency oracle.
- Iteration 412 exact15: still blocked until index 2 receives raw-valid physical authority.
- `MODEL_READINESS = 24%`.

## Next implementation gate

Build a precision-closure manifest for the full `F(u,v)` dependency chain and use it to stage the true Iteration-424 implementation from the deepest numerator primitives outward. Do not change frozen mass steps, thresholds, routing, sign, normalization, or physical numerator.
