# RQIR Research Log — Iteration 109

**Date:** 2026-08-30

Continued from authoritative Iteration 108. Paper I/II remain closed; Paper III only.

## Goal

Convert source-specific control tolerances into a physical recertification Fisher-rate envelope without inventing SI control rates, and identify which open control cuts can already enter RESOURCE-064.

## Main result

For a scalar physical nuisance coordinate with allowed variance budget

`S=sigma_*^2-sigma_floor^2`, Brownian drift convention `Var=D t/2`, reference Fisher rate `R_ref`, and pure-dead reference integration, minimizing reference overhead gives

`sigma_ref^2=S/2`,

`t_ref^*=2/(R_ref S)`,

`tau_live^*=S/D`,

`r_min=2D/(R_ref S^2)`.

Registered as **RESOURCE-067**.

For a maximum allowed overhead/live ratio `r_max`, the required Fisher rate is

`R_ref >= 2D/[r_max (sigma_*^2-sigma_floor^2)^2]`.

Registered as **RESOURCE-068**.

## New guardrails

- **NG-065:** a nuisance tolerance alone is not a control-time budget; drift/floor and physical reference Fisher rate are also required.
- **NG-066:** normalized additive tolerances are not cross-source SI control coordinates; a physical transduction and stability/reference likelihood are required before comparing Toy009/Toy014 additive costs.

## Toy009/Toy014 timing result

The retained physical timing tolerances are

- Toy009 D2: `9.19001083 us`;
- Toy014: `3.97715 us`.

Under equal timing diffusion, equal target overhead and equal reference Fisher normalization,

`R_ref,14/R_ref,09=(sigma09/sigma14)^4~=28.5086209`.

This is a same-model Fisher-rate requirement, not a statement that Toy014 necessarily spends 28.5x more timing wall time. Iteration 108 fixed-block benchmarks still yield sub-percent timing-only detector-rate correction for `D=100–1000 us^2/h`.

## Conditional additive regressions

If normalized additive coordinates were physical and common (they are not yet), same-model rate ratios would be roughly

- additive mean: `9.62310`;
- additive covariance: `21.22378`.

These are explicitly not apparatus claims.

## Control-cut status

- timing: parameterized/partial in physical seconds;
- geometry: open physical coordinate/transduction/drift/reference Fisher;
- additive mean/covariance: open physical output transduction/drift/reference Fisher;
- gain/phase: injected-transfer Fisher exists, campaign drift/recertification process remains open.

## Architecture shadow price

For a binding quota `b_ij` with `lambda_ij=-dR_D,i/db_ij`, and RESOURCE-061 detector elasticity

`E_u=u^-1/2/[u^-1/2+(v z)^-1/2]`,

the local decision effects are

`d ln G/db_14,j = -E_u lambda_14,j/R_D,14`,

`d ln G/db_09,j = +E_u lambda_09,j/R_D,09`.

Registered as **DESIGN-014**: rank physical control measurements by architecture-decision shadow price, not raw tolerance.

## Files

- `analysis/control_recertification_fisher_envelope_iteration109.py`
- `docs/PAPER_III_CONTROL_RECERTIFICATION_FISHER_ENVELOPE_ITERATION109.md`
- `research_log/2026-08-30_iteration_109_control_recertification_fisher_envelope.md`
- `recovery/RECOVERY_DELTA_ITERATION_109.md`

## Next gate

Construct the parameterized control-threshold surface for `u` in terms of measurable `(R_ref,D,sigma_floor)` for timing/geometry/additive/gain, convert them into RESOURCE-064 quotas, and derive NG-030 break-even surfaces without inventing missing SI rates.
