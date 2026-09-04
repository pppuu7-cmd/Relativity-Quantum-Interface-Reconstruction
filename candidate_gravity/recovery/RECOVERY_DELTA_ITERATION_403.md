# Candidate Gravity Recovery Delta — Iteration 403

Date: 2026-09-04

MODEL_READINESS: 24%

## Authority

Iteration 403 freezes the exact algebraic commutation contract required for the reduced double-double angular architecture.

Classification:

`PASS_DOUBLE_DOUBLE_CENTRAL4_X_CENTRAL4_EXACTLY_COMMUTES_WITH_SPHERE_MEAN`

No new physical discontinuity value is computed.

## Exact identity

The frozen one-dimensional auxiliary-mass stencil is

`C_h[f] = (f(-2h)-8 f(-h)+8 f(+h)-f(+2h))/(12h)`.

The double-double operator used by Iterations 379/385/389 is `C_h^(u) C_h^(v)`, a finite linear combination of exactly sixteen fixed mass-node evaluations.

Therefore, by linearity of sphere integration,

`C_h^(u) C_h^(v) <G(u,v,n)> = < C_h^(u) C_h^(v) G(u,v,n) >`

**exactly**.

This is not an approximation and does not require replacing the finite stencil by a continuum derivative or invoking a delicate differentiation-under-the-integral theorem.

## Why every node is legitimate

Iteration 377 already proves the complete auxiliary-mass probe envelope is regular for all 51 repeated-cut `Tr U1^2` channels:

- `51/51 REGULAR`, `BLOCKED=0`;
- minimum analytic uncut separation `0.11857147221810005`;
- minimum Källén function `0.019594400000000005`.

Thus every frozen mass-node sphere integral exists on a uniformly regular cut surface.

## Numerical consequence

For blocked double-double channels 2, 4 and 11, the reduced method may:

1. evaluate the sphere mean of the **original fixed-mass integrand** `G(u_i,v_j,n)` at every one of the sixteen frozen mass nodes;
2. use analytic/spectral angular reduction for each mean if its structural oracle passes;
3. apply the unchanged central4×central4 coefficients only after those means are obtained.

This preserves the exact mass stencil and removes angular quadrature noise from the pointwise finite-difference operation. That directly targets the observed high-vs-halfstep instability in channels 2 and 11.

## Guardrails

- no mass-stencil change;
- no `h` or `h/2` change;
- no normalization/sign change;
- no physical threshold weakening (`2e-5` remains binding);
- each reduced fixed-mass sphere mean needs structural validation;
- final physical channel authority still requires an independent original-integrand cross-check;
- blocked values are never zero-filled or inserted into q2 sums;
- no `-i/4` folding yet;
- no source/Born subtraction;
- no `ANSATZ-003`;
- no Fisher/resources.

## Next gate

Consume Iteration 401. If its one-affine-denominator structure oracle passes, build the analytic fixed-mass sphere-mean evaluator and apply it with this exact commutation contract. Validate separately for blockers 2, 4 and 11.

MODEL_READINESS: 24%
