# RQIR Iteration 048 — Explicit Energy-Metrology D2 Resource Phase Diagram

**Date:** 2026-08-29  
**Scope:** centered `y_ref=-4`, `lambda=1` D2 branch choice using the concrete energy-basis source-metrology channel from Iteration 047.  
**Status:** local branch-selection/resource result; common mean/control costs omitted; no hardware forecast and no new-physics claim.

## 1. Why this changes the branch comparison

Earlier D2 branch comparisons treated independent source metrology through an abstract rate `R_P^(alpha)` or the full-QFI bound.

Iteration 047 supplied a concrete, simpler channel:

`F_E^(alpha) ~= 0.009391884`

per accepted plus-branch energy-basis population measurement.

That is only about 11% of the full QFI, but the current best4 residual `C_alpha` is so small that even this modest metrology channel can be extremely cheap compared with millions of covariance trajectories.

Iteration 048 therefore recomputes the local D2 phase diagram with this explicit source-metrology information rate.

## 2. Three compared centered branches

At `y_ref=-4`, `lambda=1`:

### Branch 0 — no added force-covariance rows

- relational + force means;
- relational centered covariance only;
- required source prior `C_alpha*=4.55511`;
- energy-basis metrology cost `~485.00` accepted plus-branch copies.

### Branch 4 — best four force-covariance rows `(0,1,3,7)`

- covariance trajectory lower bound `N4=1.180254e6`;
- residual source prior `C_alpha*=0.05006144`;
- only `~5.33` accepted plus-branch energy-metrology copies.

### Branch 5 — best five force-covariance rows `(0,1,3,6,7)`

- covariance trajectory lower bound `N5~=2.135100e6`;
- `C_alpha*=0`.

Common force-mean calibration and timing/control resources are intentionally omitted because they are shared by the three local alternatives being compared.

## 3. Physical phase coordinate

Define

`x_E = (p_C eta_C)/(p_E eta_E) * t_E/t_C`,

where

- `t_E` is one energy/population metrology cycle;
- `t_C` is one covariance trajectory cycle;
- `p` and `eta` are acceptance/information efficiencies.

In units of `t_C/(p_C eta_C)`, the branch wall times are

`tau0 = N_E0 x_E`,

`tau4 = N4 + N_E4 x_E`,

`tau5 = N5`,

with

`N_E0~=485.005`,

`N_E4~=5.33029`.

## 4. RQIR-RESOURCE-021 — explicit source-metrology branch phase diagram

The lower-envelope branch sequence is:

### Fast energy metrology

For

`boxed: x_E < 2460.53`,

**Branch 0 wins**: it is cheaper to skip all added force-covariance rows and simply measure the larger hidden-amplitude prior independently in the energy basis.

### Intermediate energy metrology

For

`boxed: 2460.53 < x_E < 1.79136e5`,

**Branch 4 wins**: the best four covariance rows are worth acquiring, but the tiny remaining source prior should still be measured independently.

### Extremely slow energy metrology

For

`boxed: x_E > 1.79136e5`,

**Branch 5 wins**: only when independent energy-basis source verification is extraordinarily slow does eliminating the residual source prior through the fifth covariance row become cheaper.

The direct Branch-0/Branch-5 crossing is at `x_E~4402.22`, but it never controls the global lower envelope because Branch 4 is already cheaper in that region.

## 5. Transparent 100-Hz thresholds

For equal acceptance/efficiency and current maximum phase, the covariance trajectory coherence floor is about

`t_C=7.943 ms`

before readout/dead time.

### Zero additional dead/readout time

- Branch 0 ↔ Branch 4 crossover:
  `t_E ~= 19.54 s`;
- Branch 4 ↔ Branch 5 crossover:
  `t_E ~= 1423 s ~= 23.7 min`.

### With 1 ms detector dead/readout time

`t_C~=8.943 ms`, giving

- Branch 0 ↔ Branch 4:
  `boxed: t_E ~= 22.0 s`;
- Branch 4 ↔ Branch 5:
  `boxed: t_E ~= 1602 s ~= 26.7 min`.

Thus, under this transparent benchmark:

- if one accepted energy/population metrology cycle is faster than about **22 s**, adding the best four force-covariance rows is not wall-clock optimal;
- if it takes roughly **22 s to 27 min**, best4 + tiny source metrology is optimal;
- only if it takes longer than roughly **27 min** does best5 with no source metrology become preferable.

Efficiency/acceptance ratios shift these thresholds through `x_E` exactly.

## 6. Scientific consequence

This substantially changes the current D2 design intuition.

Covariance complementarity remains geometrically powerful, but once a concrete independent source-metrology channel is admitted, **the optimal experiment may need fewer covariance observables, not more**.

The experimentally relevant question is no longer simply

> how many covariance rows maximize `F_beta|theta`?

but

> which combination minimizes wall time after comparing covariance trajectories against the actual source-metrology rate?

### RQIR-RESOURCE-021 — explicit metrology-rate closure

> Branch selection must use a physically realizable source-metrology Fisher rate. In the current Toy009 benchmark, a modest energy-basis measurement can make the no-extra-force-covariance branch cheaper than best4 by many orders of measurement count unless one source-metrology cycle is tens of seconds or slower relative to an ~ms covariance trajectory.

## 7. Important scope

The phase diagram is local and omits costs common to the compared branches:

- force-mean calibration;
- timing/additive controls;
- science detector integration;
- source preparation/reset overhead if distinct from `t_E`;
- detector backaction on shared copies;
- apparatus-specific SI transduction.

It therefore selects between **source-amplitude closure strategies**, not the total D2 experiment architecture.

Still, the ordering is robust enough to change the next priority: a physical estimate of `t_E`, `p_E`, and `eta_E` is now more valuable than adding more covariance geometry.

## 8. Reproducibility

Code:

`analysis/d2_energy_metrology_phase_diagram_iteration048.py`

The script derives the three normalized branch times, solves all pairwise crossovers and verifies the lower-envelope ordering and 100-Hz thresholds.

## 9. Next gate

Build a minimally physical energy/population source-metrology protocol and estimate

`R_E^(alpha)=p_E eta_E F_E^(alpha)/t_E`.

The immediate experimental question is whether `t_E` plausibly lies below or above the ~20-second branch-0/best4 threshold for the type of five-mode coherent massive source envisioned by Toy009. Until that is specified, branch 0 and best4 should both remain active candidates.