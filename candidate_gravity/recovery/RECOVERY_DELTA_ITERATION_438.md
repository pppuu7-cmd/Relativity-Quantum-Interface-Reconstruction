# RECOVERY DELTA — ITERATION 438

**Status at allocation:** prospectively frozen; result not yet consumed.  
**Authority target:** Iteration-270 `A_finite` 80/120-digit arithmetic-core closure only.  
**Prerequisites:** raw-valid Iterations 436/437 N1/Q1 precision closures.  
**MODEL_READINESS:** 24% at launch.

## Frozen object

The authoritative Iteration 438 object is the exact parent arithmetic chain

`geometry -> action_covector + gamma_tensor + R_and_dR + lie_on_tensor -> A_finite`

at every finite-amplitude node actually used by `Acoef(POS, legs, P0, h)` for all seven nonempty subsets of `LEGS=('s','a','b')`.

Frozen amplitudes are exactly those of Iteration 270:

- one-leg: `h1=1e-4`, 6 signed nodes;
- two-leg: `h2=5e-4`, 12 signed nodes;
- three-leg: `h3=1e-3`, 8 signed nodes;
- total node census: 26; subset census: 7.

Every node uses `p=P0` and exact `total_shift=ksum(POS,legs)`.

## Frozen acceptance before result

- precision levels: 80 and 120 decimal digits;
- `max_scaled(A_finite_80-A_finite_120) <= 1e-40` over all 26 nodes;
- `max_scaled(A_finite_binary64-A_finite_120) <= 1e-9` over all 26 nodes;
- all 80/120-digit and binary64 values finite;
- node census exactly 26 and subset census exactly 7.

The `1e-9` implementation-equivalence threshold is frozen before result inspection. It cannot be relaxed after the fact.

## Scope discipline

A PASS certifies only arithmetic realization of `A_finite` on the frozen node set. It does not certify `Acoef`, `Asub`, finite-difference truncation, 368/370, 379/374, 407, Iteration 424, or physical index-2 `D_s`.

No threshold weakening, no amplitude-step change, no dynamics/routing/sign/normalization change, no zero fill, no `ANSATZ003`, and no Fisher/resource claims.
