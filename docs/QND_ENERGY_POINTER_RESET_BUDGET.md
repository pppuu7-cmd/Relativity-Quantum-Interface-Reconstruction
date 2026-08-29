# RQIR Iteration 050 — Reset-Aware QND Energy-Metrology Budget

**Date:** 2026-08-29  
**Scope:** independent Toy009 source metrology after finite-strength QND pointer closure.  
**Status:** resource/branch-selection result; no hardware forecast and no new-physics claim.

## 1. Motivation

Iteration 049 found that, with negligible source reset overhead, a finite-strength QND energy pointer maximizes Fisher/sec at a sub-projective separation `r*=0.86775`.

A real source-metrology cycle must also prepare/reset a fresh source copy. If that overhead is non-negligible, very weak measurements waste expensive copies and the optimum should move toward stronger, more projective energy discrimination.

## 2. Reset-aware rate

For the finite energy pointer

`r = 2 sqrt(eta_E kappa_E T_E)`,

define the dimensionless reset cost

`delta = 4 eta_E kappa_E t_reset`.

The accepted Fisher rate becomes

`R_E(r)=4 p_E eta_E kappa_E F_alpha(r)/(r^2+delta)`.

The physical optimization is therefore over

`F_alpha(r)/(r^2+delta)`.

This cleanly separates:

- measurement rate `kappa_E`;
- detector efficiency `eta_E`;
- source acceptance `p_E`;
- fresh-copy preparation/reset overhead `t_reset`.

## 3. Optimal strength shifts with reset cost

| `delta` | optimal `r*` | projective-Fisher fraction per accepted copy | `R_E/(p_E eta_E kappa_E)` |
|---:|---:|---:|---:|
| 0 | 0.868 | 16.6% | `8.2701e-3` |
| 0.1 | 0.986 | 21.2% | `7.4084e-3` |
| 0.5 | 1.265 | 32.0% | `5.7228e-3` |
| 1 | 1.471 | 39.8% | `4.7250e-3` |
| 2 | 1.726 | 48.8% | `3.6853e-3` |
| 5 | 2.170 | 62.5% | `2.4204e-3` |
| 10 | 2.587 | 73.1% | `1.6452e-3` |
| 20 | 3.037 | 82.0% | `1.0544e-3` |
| 50 | 3.656 | 90.4% | `5.3619e-4` |

Thus expensive reset/preparation shifts the optimum toward projective measurement, but total Fisher throughput falls because each copy carries a fixed overhead.

### RQIR-RESOURCE-023 — source-reset/measurement-strength tradeoff

> The optimal source-metrology measurement strength depends on the cost of producing a fresh source copy. Cheap reset favors many sub-projective QND measurements; expensive reset favors stronger near-projective readout. Projective Fisher per copy is not by itself a wall-clock optimum.

## 4. Rate-space D2 branch phase diagram

At the current transparent D2 benchmark (`100 Hz`, `p_C=0.5`, `1 ms` detector overhead):

- best4 covariance wall time `T4 ~= 5.86402 h`;
- best5 covariance wall time `T5 ~= 10.60811 h`.

The source-amplitude requirements remain

`C0=4.55511`,

`C4=0.05006144`,

`C5=0`.

The branch boundaries can now be written directly in the measurable source Fisher rate `R_E^(alpha)`:

### Branch 0 beats best4 if

`boxed: R_E^(alpha) > 2.13404e-4 s^-1`.

### best4 beats best5 if

`boxed: R_E^(alpha) > 2.93122e-6 s^-1`.

Therefore the lower envelope is:

- **Branch 0** for `R_E > 2.134e-4 s^-1`;
- **best4 + residual energy metrology** for `2.93e-6 < R_E < 2.134e-4 s^-1`;
- **best5** only for `R_E < 2.93e-6 s^-1`.

This is a cleaner physical statement than the old abstract `R_P` coordinate because `R_E` is tied to an explicit measurement model.

## 5. Mapping back to detector parameters

For any reset cost `delta`, define

`c(delta)=max_r 4 F_alpha(r)/(r^2+delta)`.

Then

`R_E,max = p_E eta_E kappa_E c(delta)`.

For zero reset,

`c(0)=0.00827010`,

so the Branch0/best4 boundary is

`p_E eta_E kappa_E > 0.025804 s^-1`.

As reset grows, `c(delta)` decreases. For example:

- `delta=1`: boundary `p_E eta_E kappa_E > 0.0452 s^-1`;
- `delta=5`: `>0.0882 s^-1`;
- `delta=10`: `>0.1297 s^-1`;
- `delta=20`: `>0.2024 s^-1`;
- `delta=50`: `>0.3980 s^-1`.

These numbers are not hardware predictions because `delta` itself contains `eta_E kappa_E t_reset`. They are a compact design map for any proposed source-readout implementation.

## 6. Scientific interpretation

The current D2 decision problem has become more concrete:

1. covariance geometry alone is not enough;
2. source metrology is not characterized by projective copy count alone;
3. a weak QND energy monitor is suppressed by the exact equal-energy constraint;
4. a finite measurement strength maximizes Fisher/sec;
5. fresh-copy preparation/reset can dominate and shift the optimum;
6. the only apparatus quantity needed for the current branch decision is the actual achieved `R_E^(alpha)`.

This means a future physical source model can be inserted without redoing the entire Fisher geometry: measure or calculate its energy-metrology rate and compare it with the two rate thresholds above.

## 7. Reproducibility

Code:

`analysis/qnd_energy_pointer_reset_budget_iteration050.py`

It optimizes the finite pointer at fixed dimensionless reset cost and reproduces the current Branch0/best4/best5 rate boundaries.

## 8. Next gate

The largest remaining ambiguity is now the **source realization**, not the abstract Fisher conversion. Build a minimal physical five-mode source implementation class (oscillator/atomic/internal-mode proxy) and determine whether its fresh-copy preparation and dispersive energy-readout parameters can plausibly produce

`R_E^(alpha) > 2.13e-4 s^-1`.

In parallel, the conservative experiment architecture should retain Branch0 and best4 until a physical `R_E` is supplied.
