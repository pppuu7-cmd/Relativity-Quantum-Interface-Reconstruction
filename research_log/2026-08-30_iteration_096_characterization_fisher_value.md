# RQIR Research Log — Iteration 096

**Date:** 2026-08-30

## Goal

Continue from authoritative Iteration 095 without reopening Paper I/II or starting Toy015. Convert apparatus uncertainty value-of-information into a physical characterization-time priority.

## Reproducibility correction

A code audit found that `analysis/crossover_value_of_information_iteration094.py` selected the wrong symbolic endpoint names for `R_src` inside `contraction_derivative()`. The robust formulas and published Iteration-094 leverage numbers were already based on the correct monotonic endpoints, so the scientific result is unchanged. The code now explicitly uses `R_lo` on the upper-time architecture branch and `R_hi` on the lower-time branch.

Registered as **RQIR-NUM-005**.

## New result

For one scalar apparatus coordinate with current information `I0` and physical characterization Fisher rate `R_char`, define

`nu = R_char/I0 = R_char sigma^2`.

Then interval half-width contracts exactly as

`eta(t)=[1+nu t]^-1/2`,

and

`t_char(eta)=(eta^-2-1)/nu`.

In particular `t_50=3/nu`.

Combining this with Iteration-094 local decision leverage `Lambda=(1/W)dW/deta` gives the initial robust decision-band shrink rate

`Gamma=(1/2)Lambda nu`.

This yields **RQIR-RESOURCE-048** and **RQIR-DESIGN-010**: rank proposed characterization measurements by `Lambda nu`, not by raw VOI, raw uncertainty, or Fisher rate separately.

## Correlated extension

For primitive covariance `C`, characterization Fisher-rate matrix `J`, and smooth decision gradient `g`,

`Cdot=-CJC`,

so

`-d ln sigma_B/dt = (g^T C J C g)/(2 g^T C g)`.

This is **RQIR-RESOURCE-049**: useful characterization Fisher is directional in the covariance-weighted decision direction.

New guardrails:

- **RQIR-NG-049:** raw VOI is not a measurement schedule; measurement time can reverse the ranking.
- **RQIR-NG-050:** under correlated primitive uncertainty, total Fisher such as `tr J` is not decision Fisher; use the full matrix projection and finite robust contraction at nonsmooth points.

## Numerical regression

The corrected Iteration-094 synthetic leverage ordering is reproduced:

Toy014 `R_src`, Toy009 `R_src`, Toy014 `A`, Toy014 duty, Toy009 duty, Toy009 `A`.

Useful break-even normalized characterization-rate ratios in that regression geometry:

- Toy014 `A` overtakes Toy014 `R_src` for `nu_A/nu_R > 2.86650504416`;
- Toy009 `R_src` overtakes Toy014 `R_src` for `nu_09R/nu_14R > 1.21465868002`;
- Toy014 duty overtakes Toy014 `R_src` for `nu_d/nu_R > 3.26491671391`.

An equal-trace correlated-Fisher regression gives decision-uncertainty shrink rates `1.0` versus `0.25`, proving that total Fisher alone cannot rank measurement designs.

## Files

- corrected `analysis/crossover_value_of_information_iteration094.py`
- `analysis/characterization_fisher_value_iteration096.py`
- `docs/PAPER_III_CHARACTERIZATION_FISHER_VALUE_ITERATION096.md`
- `recovery/RECOVERY_DELTA_ITERATION_096.md`

## Next gate

Build physical characterization likelihoods and Fisher rates for the Iteration-095 primitive coordinates: `(a2,a4,rho)`, seven `2x2` calibration blocks, Ramsey `(p_E,Omega_E,t_reset,V)`, and control/duty/drift. Then evaluate `Lambda nu` or the correlated matrix projection on the active robust Toy009/Toy014 branches. Do not open Toy015 unless that physical characterization-rate analysis identifies a genuinely source-dependent bottleneck.
