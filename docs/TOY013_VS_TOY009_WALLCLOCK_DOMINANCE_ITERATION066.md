# RQIR Iteration 066 — Toy013 vs Toy009 wall-clock dominance gate

**Date:** 2026-08-30  
**Status:** architecture-level resource lower bound; no hardware or new-physics claim.

## 1. Purpose

Iteration 065 established three physically relevant Toy013/Toy009 ratios after the same spectral-tilt-profiled D2 treatment:

- `S_eff,013/S_eff,009 = 0.04228407350`;
- calibration cost ratio `C_cal,013/C_cal,009 = 0.1233011369`;
- zero-reset Ramsey Fisher-rate coefficient ratio `R_R,013/R_R,009 = 0.003022`.

The first ratio means equal-noise D2 science exposure scales as `1/S_eff`; the third means source-metrology time scales as inverse Fisher rate when all protocol-external factors are held fixed.

This note asks a deliberately narrow question: **can Toy013 ever beat Toy009 in total wall clock before choosing an absolute detector ASD, mass, separation or coupling?**

## 2. Dimensionless total-time model

Normalize all times to the Toy009 D2 science exposure `T_sci,009`. Define

`x = T_cal,009 / T_sci,009`,

`y = T_src,009 / T_sci,009`.

For costs that are common to both architectures, write `z=T_common/T_sci,009`. Then

`T_009/T_sci,009 = 1 + x + y + z`,

while the retained Iteration-065 ratios imply

`T_013/T_sci,009 = 23.64956631 + 0.1233011369 x + 330.9066843 y + z`.

Here the source factor assumes the same Ramsey acceptance, coupling normalization, reset regime and visibility. It is therefore an optimistic comparison for Toy013, not a complete SI apparatus model.

## 3. Exact dominance inequality

Toy013 is faster only if

`23.64956631 + 0.1233011369 x + 330.9066843 y < 1 + x + y`.

Solving for the required Toy009 calibration burden gives

`x > 25.83505838 + 376.3055916 y`.

This is the main result of Iteration 066.

### Consequences

Even in the unphysical best case `y=0`, Toy013 can beat Toy009 only if Toy009 calibration already costs more than

`25.835 x T_sci,009`.

Once source metrology is non-negligible, the threshold rises extremely rapidly:

| `y=T_src,009/T_sci,009` | minimum `x=T_cal,009/T_sci,009` for Toy013 win |
|---:|---:|
| 0 | 25.8351 |
| 0.01 | 29.5981 |
| 0.1 | 63.4656 |
| 1 | 402.1407 |

Therefore the `~8.11x` Toy013 calibration saving is not, by itself, enough to compensate its `~23.65x` science penalty unless Toy009 calibration is overwhelmingly dominant. Any appreciable Ramsey source-metrology cost makes Toy013 still harder to justify.

## 4. Retained result — RQIR-RESOURCE-029

**Calibration-optimality is insufficient for architecture promotion.** For Toy013 trial 29100, the spectral-tilt-profiled calibration saving can overcome the science and Ramsey penalties only in a restricted region of resource space satisfying

`T_cal,009/T_sci,009 > 25.8351 + 376.306 (T_src,009/T_sci,009)`

under the optimistic equal-protocol assumptions above.

This gives a useful architecture-independent pruning gate before an absolute SI detector model is available.

## 5. What remains open

This result does **not** yet close the total physical budget because:

- detector equivalent-force/displacement ASD and transfer Jacobians are still needed to set `T_sci,009` in seconds;
- direct-force and relational mean calibration require physical shot-noise/transduction rates;
- Ramsey acceptance, coupling, visibility, fresh-copy reset and state-preparation throughput can differ between Toy009 and Toy013;
- control/timing/additive-reference costs need source-specific revalidation;
- coherence constraints can turn a nominal Fisher-rate advantage into an infeasible sequence.

NG-005, NG-006, NG-023, NG-026 and all relativistic/full-QFT consistency gates remain active.

## 6. Reproducibility

Code:

`analysis/toy013_vs_toy009_wallclock_dominance_iteration066.py`

The script reconstructs the inverse-rate factors, evaluates the exact crossover and regression-checks the boundary.

## 7. Next gate

The next highest-value step is to replace `x` and `y` by physical rates for the mature Toy009 baseline: first attach a declared detector ASD/transduction model to D2 science and direct-force mean calibration, then propagate the same apparatus assumptions to Toy013. This will decide whether the resource-space region required by the inequality is physically reachable rather than merely algebraically possible.
