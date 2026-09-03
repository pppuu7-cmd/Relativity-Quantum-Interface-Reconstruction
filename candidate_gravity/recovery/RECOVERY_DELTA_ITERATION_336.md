# Recovery Delta — Candidate Gravity Iteration 336

**Date:** 2026-09-03  
**MODEL_READINESS:** 24%  
**Status:** authoritative scoped PASS for exact geometric two-particle phase-space normalization; not yet a normalized determinant discontinuity coefficient.

## Provenance

- workflow: `rqir-iteration336-det-massless-phase-space-normalization`
- run: `33754035543`
- job: `100644020489`
- artifact: `9892688060`
- artifact digest: `sha256:eaa23f7411d63f0d66216498b750a20609fa19a478662f9fde1f1e14bce0165e`
- scientific JSON SHA-256: `5f84fd4616dcca8eb3bd5beeb396718a74caab9637f77758e4e63aa529f07e53`

## Result

For the Candidate Gravity signature `(-,+,+,+)` and a timelike rest frame `Q=(M,0)`, the standard Lorentz-invariant two-massless-particle positive-energy cut measure is frozen as

`dPhi2 = dOmega/(32*pi^2)`

and therefore

`int dPhi2 = 1/(8*pi)`.

The Iteration-333/335 cut proxies are normalized sphere means,

`mean = (1/(4*pi)) int dOmega F`,

so the exact geometric conversion is

`int dPhi2 F = mean/(8*pi)`.

The executable exact-Jacobian check closes with numerical error `0.0` at double precision.

## Authority boundary

This PASS freezes only the geometric Lorentz-invariant phase-space factor. It does **not** freeze the overall Cutkosky discontinuity sign, factors of `i`, loop prefactor, or matched-observable normalization. Those require explicit provenance from the exact effective-action/propagator convention and must not be guessed from textbook sign conventions.

Iteration 335 remains independently active on the sole unresolved `q^2=-1` triangle angular convergence. Iteration 336 does not use or recompute that result.

## Guardrails retained

No threshold weakening; no parent/numerator/routing change; no Cutkosky sign assumption; no Source/Born subtraction; no `ANSATZ-003`; no Fisher/resources; Iteration-297 finite-DR warning remains binding.

## Readiness

MODEL_READINESS: 24%

Change from Iteration 334: `0 pp`. An exact normalization prerequisite closed, but no readiness bucket is complete and no comparator-subtracted residual exists.

## Exact next gate

1. Allow Iteration 335 to finish without duplication. If it passes, freeze the complete channel-resolved absorptive vector; if it remains BLOCKED, move to analytic angular reduction without weakening the frozen `2e-5` criterion.
2. Independently audit the exact loop-measure/propagator/`i` convention that multiplies the geometric `1/(8*pi)` factor before calling any determinant quantity a normalized physical discontinuity coefficient.
