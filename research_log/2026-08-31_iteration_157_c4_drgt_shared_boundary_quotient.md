# RQIR Research Log — Iteration 157

**Date:** 2026-08-31  
**Comparator:** `C4-DRGT-001`

## Starting point

Iteration 156 produced a two-dimensional dRGT TT nonlinear-response tangent and showed it was outside the currently implemented two-column C5 `R^3` span. Before treating that as a meaningful comparator-space enlargement, the frozen next gate required common-boundary and gain nuisance subtraction.

## Quotient construction

Base finite span:

`M=[EH_common,C5_Ricci3,C5_Riemann3,response_gain]`.

The gain direction is the frozen dRGT reference response itself, corresponding to an unknown common multiplicative response calibration.

Tested C4 directions:

`V4=[d/d log m^2,d/d alpha3]`.

## Raw result

Base rank `4`; combined rank `6`.

Residual fractions:

- `log m^2`: `0.001256944940945903`;
- `alpha3`: `0.0529565926906167`.

Thus both columns remain algebraically independent, but the mass direction is nearly absorbed after the physically motivated shared-boundary/gain quotient.

## Coordinate-scaling audit

Repeated the same quotient after three invertible row normalizations in addition to raw coordinates.

Across all scalings:

- base rank = `4`;
- combined rank = `6`.

Residual fraction ranges:

- `log m^2`: `0.001256944940945903` to `0.003203089011461978`;
- `alpha3`: `0.047221203241976296` to `0.06942706305159267`.

The algebraic rank is robust but the conditioning is strongly unequal.

## New retained results

### `C4-NG-003 — COMMON_BOUNDARY_GAIN_NEARLY_ABSORBS_MASS_DIRECTION`

The dRGT mass tangent retains only `~0.13%–0.32%` outside the common EH/C5/gain span in the tested coordinates. It is therefore near-degenerate and not promotable as a robust discriminator.

The `alpha3` direction retains `~4.7%–6.9%` and is materially more robust, but remains only a scoped comparator residual.

### `NG-FUNNEL-014 — ALGEBRAIC_RANK_REQUIRES_CONDITIONING_AUDIT`

Rank increase alone is insufficient. A future Candidate Gravity direction must survive shared-boundary/nuisance subtraction with a residual comfortably above numerical and modeling uncertainties under reasonable coordinate scaling before Fisher/resources.

## Scope

Still BLOCKED:

- dRGT helicity-0/1 completion;
- Vainshtein/nonperturbative sector;
- dRGT `N2/C3sym`;
- alpha4 higher-point direction;
- C5 higher local and loop/nonanalytic directions;
- C3 diffusion-dependent ordered response.

No `ANSATZ-003`; no Fisher/resources.

## Next gate — Iteration 158

Freeze one additional strong quantum-gravity comparator rather than expanding dRGT prematurely. Preferred next target: one concrete covariant nonlocal/form-factor action whose two- and three-point sectors can be evaluated on the same six-probe protocol. A fixed asymptotic-safety vertex truncation is the alternative if it provides a cleaner finite parameter map.

Before acceptance, derive its finite tangent from the action/truncation and perform the same common-EH/gain quotient. Do not use the broad labels `nonlocal gravity` or `asymptotic safety` as columns.
