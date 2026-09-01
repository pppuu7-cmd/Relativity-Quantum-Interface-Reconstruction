# RQIR Candidate Gravity — Iteration 248

**Date:** 2026-09-01  
**MODEL_READINESS: 24%**

## Question

Can the Vilkovisky `e=1` or `e=2` equation-of-motion sectors be discarded in the null-soft TT protocol merely because the soft mode satisfies the linearized Einstein equation?

## Frozen test

Use Minkowski signature `(-,+,+,+)`.

Soft mode:

- `k_s=(1,0,0,1)`, hence `k_s^2=0`;
- TT plus polarization `epsilon_s,xx=+1/sqrt(2)`, `epsilon_s,yy=-1/sqrt(2)`.

Hard mode:

- `k_h=(0.2,0.6,0.3,0.1)`, hence `k_h^2=0.42`;
- deterministic spatial TT polarization orthogonal to the hard spatial momentum.

Evaluate the exact Einstein tensor of

`g = eta + a h_s exp(i k_s.x) + b h_h exp(i k_h.x)`

at `x=0`, and extract the mixed amplitude derivative

`d^2 G/(da db)|_0`

with a symmetric four-corner finite difference.

## Result

All frozen TT/null checks pass:

- `k_s^2 = 0`;
- soft and hard transversality at machine zero;
- soft and hard traces equal zero.

The mixed nonlinear Einstein response is decisively nonzero and converges as the amplitude step shrinks:

| step | Frobenius norm | max component |
|---:|---:|---:|
| `1e-2` | `0.7318372412` | `0.4627846361` |
| `3e-3` | `0.7316734791` | `0.4626937686` |
| `1e-3` | `0.7316590851` | `0.4626857810` |
| `3e-4` | `0.7316574478` | `0.4626848725` |

Therefore

`G^(1)[h_s]=0`

does **not** imply

`G^(2)[h_s,h_h]=0`.

## Scientific classification

`PASS_SCOPED_NONLINEAR_EINSTEIN_MIXED_SOFT_HARD_NONZERO`.

Retain guardrail:

`DO_NOT_ZERO_VD_E1_E2_SECTORS_FROM_LINEAR_NULL_SOFT_EOM`.

This strengthens Iteration 247: the `e=3` EOM sector is structurally killed in the cubic null-soft partition, but `e=1` and `e=2` are not.

This is not yet a complete Vilkovisky comparator calculation. Kernel/connection insertions, source/Ward completion and the causal hard-channel cut still have to be evaluated in the same parent convention.

## Readiness

`MODEL_READINESS: 24%` — unchanged. No comparator rubric block closes and there is no Candidate Gravity residual.

## Next gate — Iteration 249

Compute the first explicit `e=1/e=2` Vilkovisky-compatible cubic contractions using the Iteration-248 nonlinear Einstein building block and determine whether the surviving terms remain nonzero after the frozen TT/source/Ward projection. Do not infer their cut/discontinuity before the causal kernel is specified.
