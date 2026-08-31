# Iteration 157 — dRGT shared-boundary quotient audit

**Date:** 2026-08-31  
**Comparator:** `C4-DRGT-001`  
**Status:** `PASS_SCOPED / MASS_DIRECTION_NEAR_DEGENERATE`

## Purpose

Iteration 156 compared the dRGT tangent only with the two implemented local C5 `R^3` columns. Iteration 157 applies a stricter nuisance/comparator quotient before interpreting those residuals.

The base span now contains:

1. the common EH nonlinear response;
2. C5 `Ricci^3`;
3. C5 `Riemann^3`;
4. a conservative common response-gain direction at the frozen dRGT reference point.

The dRGT tangent columns are still `(log m^2,alpha3)`.

## Raw quotient

Base rank: `4`.

Combined base+dRGT rank: `6`.

Residual fractions after projection:

- `log m^2`: `0.001256944940945903`;
- `alpha3`: `0.0529565926906167`.

Thus algebraic independence remains, but the mass direction is already extremely close to the shared-boundary/gain span.

## Row-normalization robustness

Three additional invertible row scalings were tested:

- normalize by the base-row L2 norm;
- normalize by `|EH|` with a floor;
- normalize by the absolute dRGT reference response with a floor.

For all four coordinate choices:

- base rank remains `4`;
- combined rank remains `6`.

Residual-fraction ranges:

`log m^2: 0.001256944940945903 ... 0.003203089011461978`,

`alpha3: 0.047221203241976296 ... 0.06942706305159267`.

So the rank result is invariant, but the conditioning is highly asymmetric.

## Retained result

### `C4-NG-003 — COMMON_BOUNDARY_GAIN_NEARLY_ABSORBS_MASS_DIRECTION`

After the common EH response and an overall response-gain nuisance are included, the frozen dRGT mass direction retains only about `0.13%–0.32%` of its tangent norm outside the base span under the tested row normalizations.

This direction is therefore **near-degenerate and not promotable as a robust discriminator** at the present numerical/model-completion level.

The `alpha3` direction retains about `4.7%–6.9%`, making it materially more robust in this scoped TT protocol, though still not a novelty certificate because full C4 and full C5 remain incomplete.

### `NG-FUNNEL-014 — ALGEBRAIC_RANK_REQUIRES_CONDITIONING_AUDIT`

A formal rank increase is not enough. Shared-boundary directions, gain nuisances and reasonable observable coordinate scalings can reveal that an algebraically independent direction is practically near-degenerate.

This gate must be applied before Fisher/resource work.

## Scope guard

The result does not include:

- helicity-0/1 dRGT response;
- Vainshtein/nonperturbative effects;
- dRGT `N2/C3sym`;
- alpha4 higher-point information;
- higher local and loop/nonanalytic C5 columns.

Therefore `alpha3` is only `SCOPED_RESIDUAL_SURVIVES`, not Candidate Gravity novelty.

## Reproducibility

- `analysis/c4_drgt_shared_boundary_quotient_iteration157.py`
- `results/c4_drgt_shared_boundary_quotient_iteration157.json`
