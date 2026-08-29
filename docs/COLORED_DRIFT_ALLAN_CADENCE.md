# RQIR Iteration 023 — Colored Drift / Allan-Variance Cadence

**Date:** 2026-08-29  
**Status:** experimental-resource/systematics gate; no new-physics claim.

## 1. Target

Iteration 022 showed that white independent timing-reference statistics are very cheap compared with the current D1/D2 acquisition and calibration times. The unresolved issue is low-frequency/common-mode drift over a long campaign.

This iteration therefore replaces a static timing prior by an explicit cadence model.

## 2. Minimal colored-drift model

Let a reference coordinate `x` be re-estimated in blocks. Immediately after a reference block the residual estimation variance is

\[
\sigma_{ref}^2.
\]

Between blocks, model the uncontrolled low-frequency component as a random walk

\[
\mathrm{Var}[x(t+\Delta)-x(t)] = D\Delta,
\]

where `D` is a diffusion coefficient in physical-coordinate squared per second.

Allow an irreducible Allan/flicker floor `sigma_floor`. Averaged uniformly over one recalibration interval `Delta`, the residual variance is

\[
\boxed{\overline{\sigma_x^2}
=\sigma_{floor}^2+\sigma_{ref}^2+\frac{D\Delta}{2}.}
\]

Thus the target prior `sigma_target` is feasible only if

\[
\boxed{\sigma_{floor}^2+\sigma_{ref}^2<\sigma_{target}^2.}
\]

For nonzero `D`, the maximum allowed recalibration spacing is

\[
\boxed{\Delta_{max}
=\frac{2(\sigma_{target}^2-\sigma_{floor}^2-\sigma_{ref}^2)}{D}.}
\]

This is a time-average criterion. A worst-case endpoint criterion would omit the factor 2 and is therefore twice as strict.

## 3. Reference-block cost

From Iteration 022, for independent per-event reference noise,

\[
T_{ref}=\frac{t_{cycle}}{p_{acc}}
\left(\frac{\sigma_{event}}{\sigma_{ref}}\right)^2.
\]

If `Delta_max >> T_ref`, the lost duty fraction is approximately

\[
\boxed{\epsilon_{ref}\simeq T_{ref}/\Delta_{max}.}
\]

Therefore a good reference channel can be statistically cheap while the long-run stability requirement remains hard.

## 4. Transparent timing benchmark

Use only already-declared Toy009/Iteration-018 timing quantities:

- `f_gap=100 Hz`;
- `tau_max=4.99085067`;
- coherence floor `~7.94 ms`;
- extra dead time `1 ms`;
- acceptance `0.5`;
- timing-prior targets `sigma_t=9.47 us` D1 and `8.01 us` D2.

Take an illustrative white timestamp RMS `sigma_event=10 us` and reserve one ninth of the target variance for the reference estimate, i.e.

\[
\sigma_{ref}=\sigma_{target}/3.
\]

Then a reference block costs only

- D1: `~0.1795 s`;
- D2: `~0.2509 s`.

For a random-walk diffusion expressed in `us^2/hour`, the allowed average-variance cadence is:

| D (`us^2/h`) | D1 cadence | D2 cadence |
|---:|---:|---:|
| 1 | `159.43 h` | `114.06 h` |
| 10 | `15.94 h` | `11.41 h` |
| 100 | `1.594 h` | `1.141 h` |
| 1000 | `9.57 min` | `6.84 min` |

The corresponding reference overhead remains tiny in this benchmark. At `D=100 us^2/h`, it is only about `3.1e-5` D1 and `6.1e-5` D2 of wall time. Even at `D=1000 us^2/h`, it remains below `7e-4`.

These numbers are not hardware predictions; `D` is deliberately left as an experimentally measured stability parameter.

## 5. Negative result: cadence cannot beat a floor

If

\[
\sigma_{floor}\ge\sigma_{target},
\]

no amount of repeated white-noise averaging and no finite recalibration cadence can satisfy the current first-order timing prior.

More generally, if

\[
\sigma_{floor}^2+\sigma_{ref}^2\ge\sigma_{target}^2,
\]

the target is infeasible before random-walk accumulation is even considered.

### RQIR-NG-007 — stability-floor obstruction

A reference channel with an Allan/flicker floor at or above the detector-required nuisance prior is structurally inadequate. Increasing the number of fast reference samples does not restore the required profiled detector information.

This is the colored-noise analogue of the distinction established in RQIR-NG-006 between exposure and independent systematic control.

## 6. New resource rule

### RQIR-DRIFT-003 — cadence is set by low-frequency stability, not white-event Fisher

Once the reference-block white variance is below the target, the useful control resource is characterized by the pair

\[
\boxed{(D,\sigma_{floor})}
\]

or equivalently an experimentally measured Allan-deviation curve, not by per-event timestamp precision alone.

The full wall-clock objective therefore needs a control-duty penalty

\[
\epsilon_{ctrl}=\sum_j T_{ref,j}/\Delta_{j},
\]

with each `Delta_j` constrained by the appropriate drift model.

## 7. D1/D2 implication

D2 has the tighter current timing requirement (`8.01 us` versus `9.47 us`), so the same physical random-walk diffusion forces more frequent D2 timing recertification. For the random-walk model and the same fractional reference allocation,

\[
\Delta_{D2}/\Delta_{D1}
=(8.01/9.47)^2\approx0.715.
\]

Thus D2 tolerates only about 71.5% of the D1 recalibration interval at equal timing-drift diffusion.

This difference is real at the current local Fisher baseline, but it is not a statement that D1 is globally experimentally superior.

## 8. Additive offsets

The same equations apply to the row-normalized additive mean/covariance controls from Iteration 016 after replacing `sigma_t` by the corresponding physical offset coordinate and measuring its `D_b` and Allan floor. No SI wall-time number is claimed until the row-normalized offsets are tied to a concrete readout quantity.

## 9. Consistency status

This iteration does not close gauge, conservation, relativistic, QFT-degeneracy, or experimental-readiness gates. It only sharpens G13 detector/systematics measurability.

## 10. Reproducibility

Code:

`analysis/colored_drift_allan_cadence_iteration023.py`

The script checks the formulas above, reproduces the timing cadence table, and explicitly asserts failure when the stability floor equals/exceeds the required target.

## 11. Next gate

Measure or adopt branch-specific physically justified Allan/PSD models for D1 clock/control references and D2 sampling/reference channels, then insert their actual `D`, floors and control-duty fractions into the Iteration-021 full wall-clock optimizer. In parallel, convert the additive-offset coordinates into physical detector units so their cadence costs can enter the same objective.
