# RECOVERY DELTA — ITERATION 440

**Status:** raw-consumed PASS; parent arithmetic precision closure, non-promoting.  
**Classification:** `PASS_ITER270_ACOEF_ASUB_80_120_DIGIT_ARITHMETIC_CLOSURE__NON_PROMOTING`  
**MODEL_READINESS:** 24% (unchanged).

## Preconditions consumed

- Iteration 438 raw-valid PASS: exact `A_finite` arithmetic core closed across all 26 signed nodes.
- Iteration 439 raw-valid diagnostic PASS: signed `Acoef` assembly cancellation amplification reaches `1790391356.9083405`; diagnostic only.
- Physical index 2 remains blocked by Iteration 421.

## Frozen object

Exact Iteration-270

`Acoef = sum_sigma prod(sigma) A_finite(sigma*h)/(2h)^n`, identical to `Asub`,

at unchanged `M=POS`, `p=P0`, `h1=1e-4`, `h2=5e-4`, `h3=1e-3`, all seven nonempty subsets and 26 signed nodes.

## Raw provenance

Run `33904321843`, job `101125537041`, artifact `9948876125`, digest `sha256:244e52df6a951a21d5ea20638fdf0d15875a07f6b0b3c77355d5b336cf4b479d`; raw scientific JSON SHA-256 `36ff8634a6bafae0281e99110739416d4a8a6313a62c918a9d12bfebffb6f964`. Workflow head `c84a9991c8d11c5d863d7f8b39bd01e5eeb4d5f9`.

## Frozen acceptance and observed result

- max scaled 80-vs-120 `Acoef` discrepancy: `1.4149749985220297e-75 <= 1e-30`;
- all outputs finite;
- exact 26-node / 7-subset census;
- diagnostic-only max binary64-vs-120 `Acoef` discrepancy: `1.890704312519492e-10`, attained in the three-leg `(s,a,b)` subset.

The arithmetic precision of the frozen signed assembly is therefore closed by an enormous margin. This does **not** certify finite-difference truncation or alternate representation consistency.

## Scientific consequence

The next unresolved parent layer is now representation/truncation rather than floating-point precision. The authorized next gate is an independent derivative oracle for the same `A_finite` function at zero amplitude, compared against the unchanged frozen `Acoef/Asub` stencil without reducing `h` or retuning thresholds.

## Guardrails

No physical `D_s` promotion, no amplitude-step reduction, no physical mass-step change, no threshold weakening, no parent-dynamics/routing/sign/normalization change, no zero fill. `ANSATZ-003` remains uncreated. Fisher/resources remain forbidden. Iteration 412 exact15 remains BLOCKED until index 2 gets raw-valid physical authority.
