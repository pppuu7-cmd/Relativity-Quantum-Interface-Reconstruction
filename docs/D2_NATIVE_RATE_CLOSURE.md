# RQIR Iteration 029 — D2 Native-Rate Closure of the Resource Phase Diagram

**Date:** 2026-08-29  
**Status:** hard-constrained Toy009/Toy010 resource closure; not an apparatus forecast and not a new-physics claim.

## 1. Question

Iteration 028 showed that D2 branch choice is controlled by

`x=K_force/K_pot`, `y=K_cov/K_pot`, `z=R_P K_pot`,

but deliberately left these quantities free because no common apparatus-level rate model had yet been imposed.

This iteration closes one layer of that problem without inventing a hardware sensitivity. Instead of assigning arbitrary hours, it rewrites `(x,y,z)` exactly in terms of four native Fisher rates that one internally consistent D2 apparatus must provide.

## 2. Native Fisher rates

Define

- `q_pot`: Fisher per second for one normalized potential-mean calibration row;
- `q_force`: Fisher per second for one normalized force-gradient calibration row;
- `q_cov`: Fisher per second for one normalized covariance/log-PSD row;
- `R_P`: independent source-preparation Fisher per second.

For the corrected D2 hard-constrained benchmark from Iteration 015,

`gamma_mean = GM = 2.414e6`,

`gamma_cov = GC = 0.929e6`,

with 14 mean rows and 8 covariance rows.

If rows inside a family share the same native rate for the purpose of a bundle-level resource closure,

`K_pot = 14 GM / q_pot`,

`K_force = 14 GM / q_force`,

`K_cov = 8 GC / q_cov`.

Therefore the Iteration-028 coordinates become exactly

`x = q_pot/q_force`,

`y = [(8 GC)/(14 GM)] q_pot/q_cov`,

`z = (14 GM) R_P/q_pot`.

Numerically,

`(8 GC)/(14 GM) = 0.219907681382...`,

`14 GM = 3.3796e7`.

Hence

`y = 0.219907681382 * q_pot/q_cov`,

`z = 3.3796e7 * R_P/q_pot`.

This is the requested apparatus-level closure: a concrete D2 design now needs native rate ratios, not arbitrary normalized wall-clock constants.

## 3. Important scale separation

The large corrected mean-calibration weight has a direct resource consequence.

The phase-coordinate boundary `z=1` occurs at

`R_P/q_pot = 1/(14 GM) ~= 2.95893e-8`.

Thus source-preparation metrology can accumulate Fisher roughly **3.38e7 times more slowly** than a single normalized potential-calibration row and still have `z~1` because the full potential bundle itself requires a very large accumulated Fisher weight.

This does **not** prove that preparation is experimentally easy. It proves a more precise conditional statement: once the corrected D2 calibration requirement is respected, independent preparation metrology need not match calibration Fisher rate per second to be resource-competitive.

This sharpens RQIR-PREP-001 and RQIR-RESOURCE-008.

## 4. Covariance bundle

The boundary `y=1` occurs when

`q_cov/q_pot ~= 0.2199077`.

Therefore if the covariance/log-PSD channel accumulates normalized Fisher even at the same per-second rate as a potential-mean row,

`q_cov=q_pot`,

then

`y~=0.2199`.

If a stationary broadband PSD channel accumulates covariance information substantially faster than a mean row, `y<<1`.

This is consistent with Iteration 022, but only under the stationary/independent-mode approximation. Colored drift, finite effective bandwidth, spectral leakage and correlated calibration errors can reduce the effective `q_cov`; Iterations 023–024 remain mandatory controls.

## 5. Force versus potential calibration

Because both mean bundles contain 14 rows with the same corrected `GM`,

`x=q_pot/q_force`.

So the force-replacement and augmented branches are cheap in the Iteration-028 phase diagram only if the **normalized force-gradient calibration Fisher rate** exceeds the normalized potential-mean rate.

This gives the physically useful interpretation:

- `q_force >> q_pot` -> `x<<1`, force-based branches can be cheap;
- `q_force ~ q_pot` -> `x~1`, branch choice depends strongly on preparation and covariance rates;
- `q_force << q_pot` -> `x>>1`, the original NP3-null branch tends to recover despite RQIR-NG-005, provided independent preparation metrology is available.

This does not identify a winner without the actual transduction model.

## 6. Representative internally consistent rate-ratio regimes

Setting `q_pot=1` only fixes a common time unit. The following are rate-ratio examples, not hardware claims.

1. `q_force/q_pot=10`, `q_cov/q_pot=10`, `R_P/q_pot=1e-8` gives

   `x=0.1`, `y~=0.02199`, `z~=0.33796`.

   This lies in the slow-preparation / cheap-force side of the phase diagram, where augmented calibration is favored in the nearby tested slices.

2. The same calibration rates but `R_P/q_pot=1e-6` gives

   `x=0.1`, `y~=0.02199`, `z~=33.796`.

   This moves to the fast-preparation regime, where native-force replacement becomes competitive or favored at low `x`.

3. `q_force/q_pot=0.1`, `q_cov/q_pot=10`, `R_P/q_pot=1e-6` gives

   `x=10`, `y~=0.02199`, `z~=33.796`.

   The large force-calibration cost moves the design toward the NP3-null + independent-preparation region.

These qualitative assignments are intentionally tied to the already computed Iteration-028 phase diagram; no new branch threshold is invented here.

## 7. Source-preparation cycle mapping

Iteration 020 gives

`F_Q(a=0.08) ~= 13.2707`

per ideal accepted copy. For preparation acceptance `p_P`, QFI efficiency `eta_P` and complete prepare+measure+reset cycle `t_P`,

`R_P = p_P eta_P F_Q/t_P`.

Combining this with the native closure,

`z = 3.3796e7 * p_P eta_P F_Q/(t_P q_pot)`.

Therefore the source side can now be connected directly to accepted-copy throughput and QFI efficiency once the same apparatus supplies `q_pot`.

## 8. New rule

### RQIR-RESOURCE-009 — native-rate closure

The D2 branch phase diagram can be parameterized directly by native measurement Fisher rates:

`(q_pot, q_force, q_cov, R_P)`

rather than abstract calibration times.

For the current corrected 14+8 row structure,

`x=q_pot/q_force`,

`y=0.219907681382 q_pot/q_cov`,

`z=3.3796e7 R_P/q_pot`.

This removes one layer of arbitrary resource normalization while preserving the requirement that all rates come from the same apparatus model.

## 9. Negative result / remaining obstruction

A unique SI-time winner is still not justified. The repository does not yet contain a physically validated common transduction model that supplies `q_pot`, `q_force` and `q_cov` for the same D2 sensor and source geometry.

In particular, one must not identify `q_pot` with `q_force` merely because both are gravitational calibration rows. Iterations 025–026 showed that they correspond to different observables and different nullspaces.

## 10. Next gate

Construct a concrete D2 transduction model that maps one equivalent-force PSD and one controlled source displacement/drive into all three native rates:

1. `q_force` from the force-template derivative and one-sided equivalent-force PSD;
2. `q_pot` from a declared physical potential-sensitive transduction or a force-integral protocol with its propagated covariance;
3. `q_cov` from the same detector bandwidth, duty cycle and effective number of independent modes;
4. `R_P` from preparation acceptance, QFI efficiency and cycle time;
5. add the timing/reference recertification duty from Iteration 023 and test branch robustness under uncertainty in all four rates.

Only after this common transduction closure should the optimizer report SI hours.

## Reproducibility

Code: `analysis/d2_native_rate_closure_iteration029.py`.
