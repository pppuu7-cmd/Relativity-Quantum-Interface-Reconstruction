# RQIR Candidate Gravity — Research Log Iteration 438

## Prospective gate freeze

Iteration 438 is allocated uniquely before numerical result inspection. It targets only the Iteration-270 `A_finite` arithmetic core, after raw-valid Iterations 436/437 closed N1/Q1 at the frozen representative parent scope.

## Frozen scientific object

The gate carries the exact Iteration-270 chain used by `A_finite`:

`geometry -> action_covector + gamma_tensor + R_and_dR + lie_on_tensor -> A_finite`

with unchanged coefficients, metric convention, momenta, modes, total shifts, contraction order, signs and normalization.

It evaluates every finite-amplitude node required by `Acoef(POS, legs, P0, h)` for all nonempty subsets of `LEGS=('s','a','b')` at the unchanged Iteration-270 stencil amplitudes:

- one-leg subsets: `h1=1e-4`, 3 subsets × 2 signs = 6 nodes;
- two-leg subsets: `h2=5e-4`, 3 subsets × 4 sign combinations = 12 nodes;
- three-leg subset: `h3=1e-3`, 1 subset × 8 sign combinations = 8 nodes;
- total: 26 distinct `A_finite` evaluations.

All use `p=P0`; each node uses the exact parent `total_shift = ksum(POS, legs)`.

## Prospectively frozen acceptance

- precision levels: 80 and 120 decimal digits;
- maximum componentwise scaled `A_finite_80-A_finite_120 <= 1e-40` over all 26 nodes;
- maximum componentwise scaled binary64 `A_finite` vs 120-digit `A_finite <= 1e-9` over all nodes;
- all 80/120-digit and binary64 values finite;
- node census must equal exactly 26 and subset census exactly 7.

The `1e-9` binary64-reproduction threshold is an implementation-equivalence gate, over four orders of magnitude tighter than the unchanged downstream physical `2e-5` tolerance. It is frozen before result inspection and cannot be relaxed post hoc.

## Authority scope

A PASS certifies only the `A_finite` arithmetic realization at these frozen nodes. It does not certify the finite-difference `Acoef/Asub` derivatives, their truncation error, 368/370, 379/374, 407, Iteration 424, or any physical `D_s` coordinate.

## Readiness

`MODEL_READINESS = 24%` at launch; no readiness increase from this arithmetic-core gate alone.
