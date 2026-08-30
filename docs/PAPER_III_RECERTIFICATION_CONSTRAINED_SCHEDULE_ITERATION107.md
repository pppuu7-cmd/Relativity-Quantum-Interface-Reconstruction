# RQIR Iteration 107 — Recertification-Constrained Detector Scheduling

**Date:** 2026-08-30  
**Status:** Paper-III detector/control scheduling gate. No apparatus forecast and no new-physics claim.

## 1. Motivation

Iteration 106 established a matrix certificate for the detector-side architecture ratio

`u=R_D,14/R_D,09`,

but its clean two-sided Loewner bound assumes a common feasible campaign simplex. The mature Toy014 systematics work already shows source-specific timing/geometry/additive reference requirements, so the next gate is to put recertification into the schedule itself rather than hiding every control cost inside one scalar duty number.

There are physically different cases:

1. a reference block is pure dead time and supplies no Fisher relevant to `beta` or its nuisances;
2. a reference/calibration block consumes time **and** supplies nuisance Fisher;
3. finite periodic recertification imposes an integer/cadence constraint rather than a smooth asymptotic duty fraction.

These cases must not be conflated.

## 2. RQIR-RESOURCE-064 — constrained campaign polytope

Let `J_k(u)` be the Fisher-rate matrix of campaign `k` at apparatus uncertainty state `u`, and let `x_k` be wall-clock fractions.

Instead of the unconstrained simplex, define a physical schedule set

`X={x: x>=0, 1^T x=1, A x >= b}`,

where the linear inequalities encode mandatory minimum reference fractions, calibration quotas, mutually declared live-time ratios, or other convex scheduling requirements.

The robust detector-side rate is

`boxed{R_D^rob = max_{x in X} min_u Phi(sum_k x_k J_k(u))}`,

with `Phi` the detector-level profiled Fisher functional.

On a fixed identifiable branch with affine-polytope Fisher uncertainty, this remains a convex optimization problem: `Phi` is concave in the Fisher matrix and the pointwise uncertainty minimum remains concave in `x`.

Thus mandatory recertification does **not** destroy the Iteration-103/104 optimization framework; it changes the feasible set.

## 3. DESIGN-013 — KKT marginal values acquire schedule shadow prices

Without active scheduling constraints, Iteration 103 gave equal marginal profiled Fisher per second across all active campaigns.

With `A x>=b`, the KKT condition becomes the same marginal rule plus the shadow prices of active scheduling constraints.

Therefore a mandatory recertification campaign can remain active even when its unconstrained marginal Fisher/sec is smaller than another campaign: it is present because the physical stability/cadence constraint requires it.

This is the correct interpretation of control overhead in the unified Fisher scheduler.

## 4. RQIR-NG-063 — a scalar duty factor is conditional

The simple replacement

`Q=(1-d)R_live`

is valid only when the removed reference/control time supplies no Fisher relevant to the science/nuisance problem and does not modify the live likelihood except through lost exposure.

If a timing, gain, geometry or additive reference block also constrains nuisance parameters appearing in `F_beta|theta`, factoring it out as pure duty can either

- discard useful calibration Fisher, or
- double count that calibration if the same prior is also inserted into the Fisher matrix.

Such blocks belong inside RESOURCE-064 as explicit campaigns.

## 5. RQIR-NG-064 — architecture-specific feasible sets weaken the Loewner ratio certificate

Iteration 106 showed that a uniform matrix sandwich

`alpha J_09,k <= J_14,k <= beta J_09,k`

gives

`alpha <= R_D,14/R_D,09 <= beta`

when both architectures optimize over the same schedule set.

If the source-specific control requirements produce different sets `X_09` and `X_14`, the two-sided conclusion no longer follows automatically.

Useful one-sided statements remain:

- if `X_09 subseteq X_14`, the lower bound `R_D,14 >= alpha R_D,09` survives;
- if `X_14 subseteq X_09`, the upper bound `R_D,14 <= beta R_D,09` survives.

If neither inclusion holds, compute the two constrained optima directly or construct an explicit mapping between feasible schedules. Do not use the unconstrained scalar ratio as a robust certificate.

## 6. RQIR-RESOURCE-065 — exact finite periodic-reference staircase

Consider first a genuinely pure-dead-time reference block.

Let

- `R_live` be the fully profiled Fisher rate during informative live exposure;
- `F_*` be the target Fisher;
- `tau_live` be the maximum allowed informative exposure between recertifications;
- `t_ref` be the duration of each mandatory reference block.

Using the declared convention that one reference block is required for every at-most `tau_live` of informative exposure, including the first live interval,

`L=F_*/R_live`,

`n_ref=ceil(L/tau_live)`,

and

`boxed{T_wall=L+n_ref t_ref}`.

The effective finite-campaign rate is

`Q_finite=F_*/T_wall`.

At long exposure,

`Q_finite -> R_live tau_live/(tau_live+t_ref)`.

Thus the familiar duty factor is only the asymptotic smooth limit. Short campaigns show an exact staircase because an additional reference block enters whenever `L` crosses an integer multiple of `tau_live`.

This matters for high-rate future apparatus where control blocks are no longer negligible compared with science duration.

## 7. Synthetic Fisher regression

The reproducibility script uses a two-parameter science campaign whose beta direction is exactly degenerate with one nuisance unless calibration is available.

A fast calibration campaign supplies nuisance Fisher, while a mandatory reference campaign supplies the same nuisance information more slowly.

The unconstrained optimum has approximately

`R_D ~= 2.56`

and uses no slow reference campaign.

Imposing a mandatory 10% reference fraction moves the optimum to a lower rate of approximately

`R_D ~= 2.32`.

This is deliberately synthetic; its role is only to verify that the constrained schedule remains well behaved and that a mandatory low-marginal campaign changes the optimum rather than being silently represented as an unrelated scalar penalty.

## 8. Finite-cadence regression

For the synthetic pure-dead-time example

- `F_*=25`;
- `R_live=.1 s^-1`;
- `tau_live=100 s`;
- `t_ref=2 s`,

one needs

`L=250 s`,

`n_ref=3`,

so

`T_wall=256 s`

rather than a continuously approximated reference cost.

The long-run live-rate limit is

`0.0980392157 s^-1`.

## 9. Toy014 timing-reference regression slice

Iteration 075 retained only as transparent benchmark numbers:

- timing-reference block `~0.889 s`;
- illustrative drift cadence `~0.2812 h` for `D=100 us^2/h`;
- `~0.02812 h` for `D=1000 us^2/h`.

If these blocks were pure dead time, the corresponding asymptotic duty losses would be only

- `d_ref ~= 8.7741e-4` (`0.0877%`);
- `d_ref ~= 8.7054e-3` (`0.8705%`).

These values are not apparatus forecasts. More importantly, the actual timing-reference campaign can carry timing nuisance Fisher, so RESOURCE-064 rather than pure duty is the scientifically preferred representation once its physical likelihood is specified.

## 10. Consequence for the Toy009/Toy014 comparison

The missing robust detector ratio must now be written more precisely as

`u = R_D,14^rob(X_14)/R_D,09^rob(X_09)`.

A valid common-apparatus comparison therefore needs not only the Fisher matrices from Iteration 106 but also the source-specific schedule constraints generated by

- timing drift recertification;
- geometry references;
- additive/gain references;
- same-state transfer calibration;
- any calibration-layer minimum counts or coherence/reset restrictions.

This is still an apparatus problem, not evidence for a need to redesign the source.

## 11. Next admissible gate

Build the **threshold form** of the constrained schedule when absolute control Fisher matrices are not yet available:

1. parameterize minimum recertification fractions/cadences for Toy009 and Toy014;
2. propagate them into lower/upper bounds on `u` using schedule-set inclusion and matrix envelopes;
3. combine with RESOURCE-063 intervals for `(v,z,delta)`;
4. determine which physical control/reference measurement has the largest architecture-decision shadow price.

Only if that constrained robust analysis shows the dominant marginal cost is source-dependent should Toy015 be opened.

## 12. Reproducibility

Run

`python analysis/recertification_constrained_schedule_iteration107.py`.
