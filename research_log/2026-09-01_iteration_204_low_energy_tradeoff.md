# RQIR Research Log — Iteration 204

**Date:** 2026-09-01  
**MODEL_READINESS: 23%**

## Question

Can the newly exposed all-orders local-C5 truncation problem be controlled simply by moving the analytic protocol into deep IR?

## Target-independent diagnostic

Freeze a K2-only low-energy design with `x_max=0.1` and a second scale `0.65` times the high scale. No candidate or residual is used.

Twelve hard nodes span `x=[0.0239883,0.1]`.

## Conditional EFT remainder

Under the explicit illustrative coefficient envelope `|c_n|<=C`:

- omitted cubic Riemann-chain tail after dimension 12 (`n>=4`) is bounded by `7.4074e-5 C` relative to the base carrier;
- omitted K2 monomial tail after x^6 is bounded by `1.1111e-7 C`.

These are conditional bounds, not a hidden naturalness assumption.

## Analytic distinguishability collapse

On the same low-energy nodes, compare `x^2 exp(x)` with `[x,...,x^6]`.

- augmented rank remains 7 algebraically;
- raw condition number `5.55e12`;
- normalized condition `8.95e11`;
- relative nonlocal-minus-local residual `3.90e-12`;
- max absolute residual `4.05e-14`.

Thus the low-energy design improves possible EFT remainder control only while making an analytic nonlocal tangent effectively indistinguishable from local Wilson freedom.

## Retained results

- `EFT-NG-001`;
- `REL-NG-017`;
- `NG-FUNNEL-059`;
- `NG-FUNNEL-060`.

## Direction change

Prioritize linked nonanalytic/causal multi-point relations. Local analytic towers cannot reproduce branch-cut discontinuities, but Iteration 170 forbids treating a standalone positive two-point spectrum as gravity-specific. The new witness must therefore couple a higher-point retarded discontinuity to the same two-point spectral kernel/parameters.

## Readiness

`MODEL_READINESS: 23%`, unchanged.

## Next gate

Iteration 205: freeze a linked nonanalytic multi-point protocol based on discontinuity of an amputated retarded three-point object conditioned on the same two-point kernel. Local analytic EFT must be an exact null direction of the discontinuity map; C4/C5/AS/C3 loop/real-time comparators remain explicit.
