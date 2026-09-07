# Recovery Delta — Iteration 561

## Authority added

Iteration 561 freezes an exact assembly-integrity contract for the future Iteration-424 QUARTER central4 mixed derivative.

Classification:

`PASS_ITER424_QUARTER_THREE_WAY_ASSEMBLY_IDENTITY_EXACT__DIAGNOSTIC_ONLY_NON_PROMOTING`

Files:

- `candidate_gravity/code/iteration561_iter424_quarter_three_way_assembly_identity_exact.py`
- `candidate_gravity/results/iteration561_iter424_quarter_three_way_assembly_identity_exact.json`
- `candidate_gravity/research_log/2026-09-08_iteration_561.md`

## Exact retained identity

With frozen scaled nodes `[-2,-1,+1,+2]`, central4 integer weights `w=[1,-8,+8,-1]`, and mixed normalization `1/(144 h^2)`, the coefficient tensor is the outer product `w_i w_j`.

On the same complete matched 4x4 raw-valid grid, all of the following are algebraically identical:

1. direct 16-coordinate tensor sum;
2. sequential central4 `u` then `v`;
3. sequential central4 `v` then `u`;
4. 10 exchange-orbit compressed sum using the Iteration559 orbit coefficient ledger.

The equality is coefficient-level exact, independent of physical raw values.

## Synthetic unit-test contract

Exact-rational audit passes for every monomial `u^a v^b` with `0<=a,b<=4`. The tensor stencil reproduces the exact mixed derivative at the origin; only the `uv` basis member returns `1`, all other basis members return `0`.

Every row and column coefficient sum is zero, so the stencil annihilates any additive separable sector `A(u)+B(v)+constant` exactly.

## Fail-closed consequence for future QUARTER assembly

When all QUARTER support is raw-closed, the assembler must compute the same mixed derivative through independent routes. Any route disagreement beyond explicitly declared arithmetic-rounding bounds is an implementation/index/orientation failure and blocks physical promotion until localized. It must never be interpreted as a model residual.

## Guardrails unchanged

- Diagnostic only; non-promoting.
- No support substitution under `u<->v`.
- No rank skipping/reordering.
- No zero fill.
- No change to frozen Iteration-424 thresholds.
- No smaller `h`.
- No `ANSATZ-003`.
- No Fisher/resources.

## Heavy authority state at Iteration561 freeze

Rank9 remains the sole canonical heavy computation:

- run `34160111095`
- job `101859912600`
- coordinate `(+1.25e-6,+1.25e-6)`
- full-z MP80/MP120 stage was in progress at the pre-freeze check
- raw audit/upload pending

No duplicate heavy run was launched.

## Progress retained

- QUARTER new coordinates raw-closed: `8/12 = 66.6666666667%`.
- Full QUARTER coordinate coverage including HALF overlaps: `12/16 = 75%`.
- Physical index2 unresolved.
- `MODEL_READINESS: 24%`.
