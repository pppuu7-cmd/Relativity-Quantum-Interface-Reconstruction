# RQIR Research Log — Iteration 107

**Date:** 2026-08-30

## Goal

Continue from Iteration 106 by removing the assumption that Toy009 and Toy014 necessarily share the same unconstrained campaign simplex. Promote timing/geometry/additive/gain recertification into explicit scheduling constraints.

## RESOURCE-064 — constrained campaign polytope

Use

`X={x>=0, 1^T x=1, A x>=b}`

for physical minimum reference/calibration fractions and other linear schedule constraints. The robust detector rate is

`R_D^rob=max_{x in X} min_u Phi(sum_k x_k J_k(u))`.

On a fixed identifiable affine-polytope branch this remains a convex optimization problem.

## DESIGN-013

Active scheduling constraints modify the Iteration-103 equal-marginal rule by KKT shadow prices. A mandatory reference campaign can be active even when its unconstrained marginal profiled Fisher/sec is smaller than another campaign.

## NG-063

A scalar duty factor is legitimate only for pure dead/reference time that supplies no Fisher relevant to beta/nuisance profiling and does not alter the live likelihood except through lost exposure. Otherwise the reference belongs inside the joint Fisher schedule; factoring it out can discard or double-count information.

## NG-064

The Iteration-106 two-sided Loewner ratio certificate assumes a common feasible schedule set. If `X_09 != X_14`, only set-inclusion one-sided bounds survive automatically:

- `X_09 subseteq X_14` preserves the lower alpha bound;
- `X_14 subseteq X_09` preserves the upper beta bound.

Without inclusion, optimize both constrained schedules directly.

## RESOURCE-065 — finite periodic recertification

For a pure-dead-time reference block, target Fisher `F_*`, live rate `R_live`, live cadence `tau_live` and block duration `t_ref`:

`L=F_*/R_live`,

`n_ref=ceil(L/tau_live)`,

`T_wall=L+n_ref t_ref`.

The asymptotic live fraction is `tau_live/(tau_live+t_ref)`, but finite campaigns have a staircase overhead.

## Regression

Synthetic joint Fisher schedule:

- unconstrained optimized detector rate about `2.56`;
- mandatory 10% slower reference fraction reduces it to about `2.32`.

Finite cadence regression:

- `F_*=25`, `R_live=.1/s`, `tau_live=100 s`, `t_ref=2 s`;
- `L=250 s`, three reference blocks, `T_wall=256 s`.

Toy014 retained timing-reference illustration from Iteration 075, if treated as pure dead time only:

- `0.889 s` block at `0.2812 h` cadence -> asymptotic duty loss `8.7741e-4`;
- at `0.02812 h` cadence -> `8.7054e-3`.

These remain transparent drift benchmarks, not apparatus forecasts.

## Files

- `analysis/recertification_constrained_schedule_iteration107.py`
- `docs/PAPER_III_RECERTIFICATION_CONSTRAINED_SCHEDULE_ITERATION107.md`
- `recovery/RECOVERY_DELTA_ITERATION_107.md`

## Next gate

Construct interval/threshold bounds on constrained `u` using source-specific minimum recertification fractions/cadences, matrix envelopes from Iteration 106 and schedule shadow prices. Combine with robust `(v,z,delta)` and identify the highest decision-value control measurement. Toy015 remains closed.
