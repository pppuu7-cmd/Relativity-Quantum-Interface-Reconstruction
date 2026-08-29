# RQIR Iteration 034 — Physical-Coordinate and Centered-Covariance Correction

**Date:** 2026-08-29  
**Scope:** Toy009/Iteration-011 hard-constrained Fisher/resource layer.  
**Status:** mandatory coordinate/observable correction; no new-physics claim.

## 1. Why this audit was necessary

Iteration 033 attempted to close the remaining D2 covariance resource budget. Before assigning a physical `dS/du` to the covariance rows, two coordinate questions had to be checked:

1. Is the independent source-preparation Fisher `C_a` expressed in the same amplitude coordinate as the QFI from Iteration 020?
2. Are the finite-noise `cov` rows actually the derivative of the centered symmetrized noise kernel defined by RQIR, or only derivatives of raw second moments?

Both checks exposed corrections.

## 2. Source-preparation Fisher coordinate correction

Iteration 020 correctly computed the QFI of the single-branch family

`rho(a)=I/5+a Delta0`

at the nominal physical amplitude

`a=EPS=0.08`:

`F_Q^(a) = 13.27068619`

per ideal accepted copy.

However, the later detector Fisher from Iteration 026 onward uses a **fractional hidden-amplitude nuisance** `alpha` such that

`a = EPS * alpha`,

with nominal `alpha=1`.

Fisher information transforms covariantly under a parameter change:

`F_alpha = (da/dalpha)^2 F_a`.

Therefore the source QFI in the coordinate actually used by the current detector Fisher is

`F_Q^(alpha) = EPS^2 F_Q^(a)`

and numerically

`F_Q^(alpha) ~= 0.0849323916`

per ideal accepted **single-branch** source copy.

If one metrology cycle supplies one independent `rho+` copy and one independent `rho-` copy, and both are used at the same efficiency, the pair carries twice this Fisher. That factor of two must not be assumed unless the physical protocol really supplies both measurements.

### Consequence for the historical 90% example

For detector-only Fisher normalized to `S_D=1`, 90% retention requires

`C_alpha=9`.

The QFI-limited source counts are therefore approximately

- `105.97` accepted single-branch copies, or
- `52.98` independent plus/minus pair equivalents.

For the historical detector-SNR-5 scaling `S_D=25`,

`C_alpha=225`,

which requires approximately

- `2649.17` accepted single-branch copies, or
- `1324.58` independent plus/minus pair equivalents.

The earlier Iteration-020 statement that `C_a=225` corresponds to only about `17` accepted copies compared a Fisher requirement written in the later fractional-amplitude normalization with QFI written in the physical-`a` coordinate. **That copy-count mapping is withdrawn.**

The QFI value `F_Q^(a)=13.27068619` itself remains correct.

### RQIR-NUM-002 — Fisher-coordinate Jacobian rule

> Fisher requirements, Fisher rates and QFI must be transformed into the same physical parameter coordinate before they are compared or converted into repetitions/time.

For the current hidden-amplitude nuisance,

`R_P^(alpha) = p_P eta_P EPS^2 F_Q^(a) / t_P`

per single-branch metrology cycle, not `p_P eta_P F_Q^(a)/t_P`.

This correction propagates to the physical wall-clock interpretation of Iterations 020–033, but it does **not** change their dimensionless `C_alpha(lambda)` Fisher geometry.

## 3. Centered covariance is not the raw second moment in the noisy problem

RQIR defines the symmetrized noise kernel using centered operators. For two observables `A,B`,

`N_AB(rho) = Tr[rho sym(A,B)] - <A>_rho <B>_rho`.

The current Toy009 pair is parameterized symmetrically about

`rho0=I/5`:

`rho_+ = rho0 + Delta rho/2`,

`rho_- = rho0 - Delta rho/2`.

For this symmetric pair, the difference of centered covariances is exactly linear in `Delta rho`:

`Delta N_AB = Tr[Delta rho C_AB]`,

where, on the trace-zero tangent space,

`C_AB = sym(A,B) - <A>_0 B - <B>_0 A`.

An optional identity term is irrelevant because `Tr Delta rho=0`.

The earlier noisy-Fisher scripts used only `sym(A,B)` as the `cov` derivative row. That is sufficient for the **exact-null construction** because all relevant mean differences are simultaneously zero. It is not the correct centered-noise derivative once mean directions are uncertain and profiled with finite Fisher.

### RQIR-CAL-013 — centered-noise linearization rule

> In a finite-noise source/calibration likelihood, a symmetrized covariance/noise row must be the derivative of the centered covariance statistic in the declared state coordinate. A raw second-moment row is equivalent only under exact mean conditioning or when the raw second moment itself is explicitly the measured observable.

## 4. Exact Toy009/Toy010 results survive

Replacing raw second-moment rows by centered-noise derivative rows does **not** destroy the exact finite NP3 construction.

For the current balanced calibration:

- raw rank: `24/25`;
- centered rank: `24/25`;
- absolute overlap of exact null vectors: `1.000000000000` to numerical precision.

The normalized smallest singular value changes from

`0.00199954040554`

to

`0.00210380608381`,

because row normalization changes, but the exact row span/nullspace is the same.

Thus Toy009/Toy010 exact mean/noise equality and ordered-response split remain intact. The correction is statistical/resource-level.

## 5. Recomputed hard-constrained 90% row-weight benchmark

Using exact trace+energy elimination and the same deterministic 900-point allocation scan as Iteration 015, but now with centered covariance derivatives, the normalized 90%-retention benchmarks become:

### D1

- uniform gamma: `~1.12758e6`;
- optimized `gamma_mean ~= 1.26572e6`;
- optimized `gamma_cov ~= 0.621783e6`;
- uniform/optimized cost gain: `~1.09308`.

### D2

- uniform gamma: `~1.63750e6`;
- optimized `gamma_mean ~= 1.83026e6`;
- optimized `gamma_cov ~= 0.590127e6`;
- uniform/optimized cost gain: `~1.18719`.

The older Iteration-015 values remain valid for the **raw symmetrized second-moment protocol**. Because the RQIR physical target is the centered noise kernel, the values above are now the preferred normalized covariance baseline.

This does not by itself imply fewer SI seconds: row normalization still cannot create a physical rate. Native transduction/noise must be supplied.

## 6. D2 branch consequences at the centered benchmark

The fully force-native branch (`14 force means + 8 centered force-covariance rows`) still has hard rank `22/23` and retains the same structural null geometry:

- old-hidden overlap `~0.95003346`;
- detector alignment `~0.99003961`.

At the new centered benchmark:

- `F_beta|theta(C_alpha=0,lambda=1) ~= 0.0195153`;
- 90% at `lambda=1` requires `C_alpha* ~= 7.78026`;
- with asymptotically strong source metrology, the 90% calibration threshold is `lambda ~= 0.10013`.

So RQIR-NG-010 remains intact.

For the finite-reference complementary branch at `y_ref=-4`, using relational + force means and **both centered covariance families**:

`F_beta|theta(C_alpha=0,lambda=1) ~= 0.905293`.

Thus the branch exceeds 90% at the current centered benchmark without a source-amplitude prior. Its calibration-only 90% threshold is approximately

`lambda ~= 0.94149`.

This is a local normalized Fisher result, not a wall-clock conclusion.

## 7. Centered covariance row-selection update

At `y_ref=-4`, starting from relational centered covariance only:

| added centered force-cov rows | best indices | `F_beta|theta` | `C_alpha*` at `lambda=1` |
|---:|---|---:|---:|
| 0 | `()` | `0.833432` | `4.55511` |
| 1 | `(0)` | `0.856835` | `3.38136` |
| 2 | `(0,1)` | `0.876533` | `1.85743` |
| 3 | `(0,1,3)` | `0.894465` | `0.508219` |
| 4 | `(0,1,3,7)` | `0.899477` | `0.0500614` |
| 5 | `(0,1,3,6,7)` | `0.903527` | `0` |
| 8 | all | `0.905293` | `0` |

The high-value four-row set `(0,1,3,7)` is unchanged, but a fifth row now suffices to remove the source-amplitude prior at `lambda=1` in the centered normalized benchmark.

Using the centered `gamma_cov`, the equal-row local preparation-substitution thresholds become approximately

- first four rows: `q_cov/R_P^(alpha) > 5.24e5`;
- fifth row after the best four: `q_cov/R_P^(alpha) > 1.18e7`.

Rows beyond the fifth provide no additional `C_alpha` saving at `lambda=1`; their value, if any, must come from reducing calibration exposure, robustness or other nuisances.

## 8. What is now withdrawn or requires revalidation

Withdrawn as a current physical mapping:

- Iteration-020 `~17 copies for C_a=225` for the fractional-amplitude Fisher used downstream;
- any later conversion that used `R_P = p eta F_Q^(a)/t_P` directly against `C_alpha`.

Requires revalidation on the centered covariance likelihood:

- Iteration-016 timing/additive control-prior numbers;
- Iterations 018/021 wall-clock allocations that used those priors;
- raw-covariance D2 branch resource numbers from Iterations 026–033;
- stationary covariance-rate examples until the actual temporal covariance measurement model is declared.

Retained:

- all exact Toy009/Toy010 null/response results;
- RQIR-NG-005/006/010/011/012/013 as structural statements, subject to their declared protocols;
- the need for independent source metrology when an exact detector-relevant null remains;
- the physical necessity of native row-specific rates.

## 9. Reproducibility

Code:

`analysis/physical_coordinate_centered_covariance_audit_iteration034.py`

The script checks the raw/centered exact-null equivalence, recomputes D1/D2 centered row weights, applies the source-QFI parameter Jacobian, recomputes current D2 centered branches and row-selection results, and records regression guards.

## 10. Next gate

Before assigning SI `q_cov` values, determine the actual temporal measurement class of the centered covariance rows. The current Toy009 hidden states need not be stationary, so a stationary scalar PSD formula may not be the correct likelihood. The next audit must decide between:

1. stationary PSD,
2. cyclostationary/phase-referenced spectral estimation, or
3. repeated two-time covariance measurements,

and include detector backaction/ordering where the two source operators do not commute.
