# Recovery Delta — RQIR Iteration 157

**Date:** 2026-08-31  
**Authoritative change:** shared-EH and gain nuisance quotient applied to the fixed dRGT comparator. Algebraic rank survives, but the dRGT mass direction is exposed as near-degenerate; `alpha3` is materially more robust in the scoped TT protocol.

## Previous front

Iteration 156 instantiated `C4-DRGT-001`. Its `(log m^2,alpha3)` TT nonlinear tangent had rank `2/2` and expanded the implemented C5 local `R^3` span from rank 2 to rank 4.

## Stricter base span

Iteration 157 uses

`M=[EH_common,C5_Ricci3,C5_Riemann3,response_gain_at_dRGT_reference]`.

Base rank: `4`.

The dRGT parameter tangent is then projected against this shared-boundary/nuisance span.

## Result

In raw coordinates:

- combined rank = `6`;
- `log m^2` residual fraction = `0.001256944940945903`;
- `alpha3` residual fraction = `0.0529565926906167`.

Three additional invertible row normalizations preserve base rank `4` and combined rank `6`.

Across all tested coordinate scalings:

- `log m^2` residual fraction range: `[0.001256944940945903,0.003203089011461978]`;
- `alpha3` residual fraction range: `[0.047221203241976296,0.06942706305159267]`.

## New retained results

### `C4-NG-003 — COMMON_BOUNDARY_GAIN_NEARLY_ABSORBS_MASS_DIRECTION`

The mass direction is algebraically independent but practically near-degenerate after common EH and gain subtraction. It is not promotable as a robust discriminator in the present scoped model/protocol.

### `NG-FUNNEL-014 — ALGEBRAIC_RANK_REQUIRES_CONDITIONING_AUDIT`

Formal rank increase is not sufficient. Residual size relative to numerical/modeling uncertainty and robustness to reasonable observable coordinate scaling must be checked before Fisher/resource work.

## Current C4 interpretation

- `log m^2`: `NEAR_DEGENERATE_NOT_PROMOTABLE`;
- `alpha3`: `SCOPED_RESIDUAL_SURVIVES`;
- `alpha4`: `BLOCKED_AT_CUBIC_TT_ORDER`;
- helicity-0/1, Vainshtein, C4 `N2/C3sym`: BLOCKED;
- full C4 quotient: BLOCKED.

## New files

- `analysis/c4_drgt_shared_boundary_quotient_iteration157.py`
- `results/c4_drgt_shared_boundary_quotient_iteration157.json`
- `candidate_gravity/C4_DRGT_SHARED_BOUNDARY_QUOTIENT_ITERATION157.md`
- `research_log/2026-08-31_iteration_157_c4_drgt_shared_boundary_quotient.md`
- `recovery/RECOVERY_DELTA_ITERATION_157.md`

## Exact restart instruction — Iteration 158

Instantiate one fixed strong QG comparator outside the existing C3/C4/C5 blocks.

Preferred path:

1. freeze one explicit covariant nonlocal/form-factor gravity action with finite parameters;
2. derive its two-/three-point response on the same six-probe protocol;
3. apply the common EH/gain quotient and compare against C4+C5 spans;
4. if a clean finite nonlocal model cannot be mapped without additional arbitrary choices, use one concrete asymptotic-safety vertex truncation instead;
5. never use the program/class label as a tangent block;
6. keep all unavailable sectors BLOCKED;
7. no `ANSATZ-003`, Fisher or resources until a residual survives the full fixed comparator quotient.
