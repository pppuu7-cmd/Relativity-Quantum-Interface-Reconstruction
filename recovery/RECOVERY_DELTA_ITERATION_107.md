# RQIR Recovery Delta — Iteration 107

**Date:** 2026-08-30  
**Parent front:** Iteration 106.

## New front

Mandatory control/reference recertification is now represented explicitly as a scheduling constraint rather than automatically as a scalar duty multiplier.

### RESOURCE-064

Use the constrained campaign polytope

`X={x>=0, 1^T x=1, A x>=b}`

and robust detector rate

`R_D^rob=max_{x in X} min_u Phi(sum_k x_k J_k(u))`.

The problem remains convex on a fixed identifiable affine-polytope branch.

### DESIGN-013

Active recertification constraints enter the campaign KKT conditions through shadow prices; equal marginal profiled Fisher/sec applies only after those constraint multipliers are included.

### NG-063

Do not factor a reference/calibration block into a scalar duty if it also constrains a nuisance appearing in `F_beta|theta`. Such a block belongs inside the joint Fisher schedule. Scalar duty is reserved for genuinely information-free dead time.

### NG-064

If Toy009 and Toy014 have different feasible schedule sets, the two-sided Iteration-106 Loewner ratio certificate does not follow automatically. Set inclusion gives only the corresponding one-sided bound; otherwise optimize the two constrained schedules directly.

### RESOURCE-065

For pure-dead periodic reference blocks,

`L=F_*/R_live`,

`n_ref=ceil(L/tau_live)`,

`T_wall=L+n_ref t_ref`.

The asymptotic live fraction `tau_live/(tau_live+t_ref)` is only the long-campaign limit; finite campaigns have staircase overhead.

## Regression

- synthetic unconstrained detector rate `~2.56`;
- forcing a 10% slower reference fraction gives `~2.32`;
- finite pure-dead example: `L=250 s`, `tau=100 s`, `t_ref=2 s` -> three blocks and `T_wall=256 s`.

Retained Toy014 timing-reference illustration, if treated as pure dead time only:

- slow-drift cadence duty loss `~8.774e-4`;
- faster-drift cadence duty loss `~8.705e-3`.

These are not apparatus forecasts.

## Files

- `analysis/recertification_constrained_schedule_iteration107.py`
- `docs/PAPER_III_RECERTIFICATION_CONSTRAINED_SCHEDULE_ITERATION107.md`
- `research_log/2026-08-30_iteration_107_recertification_constrained_schedule.md`

## Next admissible gate

Use source-specific recertification intervals/cadences to derive robust constrained bounds on `u`, combine them with RESOURCE-063 `(v,z,delta)` intervals, and compute control/reference decision shadow prices. Do not start Toy015 yet.
