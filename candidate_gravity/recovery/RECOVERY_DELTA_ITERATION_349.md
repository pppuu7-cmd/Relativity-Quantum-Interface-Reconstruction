# Recovery Delta — Candidate Gravity Iteration 349

Date: 2026-09-03

## Scope

Matched-timelike re-specialization of the already frozen Iteration-342 `N/Y` inverse-routing bridge and Iteration-339 shifted graviton Green bridge on the exact Iteration-348 common metric background. The Iteration-340 sign binding `Hinv_VD=-K^-1` is retained. This is a provider gate only; no physical `Tr U2` cut is integrated here.

## Raw Actions authority

- run: `33782491809`
- job: `100739279679`
- artifact: `9904116787` (`iteration349-result`)
- artifact digest: `sha256:d5f4953609c50310214c481ad31dea379ca3d55b6ebd1c87f72917cb8015436b`
- scientific JSON SHA-256: `f0cd7fc78d9db50dfdb38ac22a32d67d817df8ee5d35b531ac0b3b20aa79e515`
- workflow head: `b752a16efeaeade69a3ea97ca2ea0aa1d1e90de6`

The raw artifact and authority-audit JSON were downloaded and inspected independently of the workflow conclusion. The audit contains exactly one Iteration-349 top-level object and `scientific_authority_pass=true`.

## Result

The exact common fixture closes with `closure_max_abs=0.0` and `q_i^2=(-1.0,-0.14,-0.34)` to `5.55e-17`.

For all three timelike legs, the matched ghost inverse routing passes the unchanged first-order identities. Largest observed errors are:

- `NY_bridge_error = 5.329070518200751e-15`;
- `block_inverse_error = 1.7763568394002505e-15`;
- `Y_inverse_error = 0.0`.

For all three timelike legs, shifted graviton inversion with the Vilkovisky sign passes. Largest observed errors are:

- flat `K0` error `6.938893903907228e-17`;
- shifted block inverse error `5.69835734791793e-15`;
- `Hinv_VD + K^-1` error `0.0`.

The deliberately wrong unshifted routing remains strongly separated, with shifted-vs-unshifted norms approximately `208.18`, `27.64`, and `19.87` for the three legs.

Authority:

`PASS_U2_NY_AND_SHIFTED_HINV_MATCHED_TIMELIKE_COMMON_BACKGROUND_PROVIDERS__12_ROUTE_PHYSICAL_SUBSTITUTION_NEXT`.

This closes the matched-timelike `N/Y` and shifted `Hinv` provider prerequisite only. It does not by itself validate reuse of the Iteration-346 null-soft 12-route survivor set on a timelike fixture.

## Immediate downstream audit

Before physical route substitution, Iteration 350 is launched to re-audit whether the Iteration-308/346 singleton-soft `A1=0` pruning survives the matched timelike rebase. If the designated soft-leg `A1` is nonzero, the 12-route set is not timelike physical authority and the route census must be rebuilt from all 30 raw placements rather than zero-filled.

Unsupported remains `BLOCKED`; no Source/Born subtraction, no `ANSATZ-003`, no Fisher/resources and no blind full-C5.

MODEL_READINESS: 24%

Change from Iteration 348: `0 pp`. A hard U2 provider prerequisite closed, but no complete readiness bucket or robust comparator-subtracted residual closed.
