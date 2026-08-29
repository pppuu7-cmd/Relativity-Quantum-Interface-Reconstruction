# RQIR Research Log — Iteration 019: Branch-Specific Physical Fisher Rates

**Date:** 2026-08-29

## Starting point

Iteration 018 converted timing/control priors into clock-jitter and wall-clock bookkeeping but still used a standardized single-shot sensitivity `xi`. The declared next gate was to replace this with native D1 and D2 detector information rates.

## D1 rate model

Using the Iteration-011 Toy009 harmonics, the current four-switch window re-optimizes to approximately

- `a=0.90716`;
- `|W2|=0.50150`;
- `|W4|=0.30892`;
- profiled dimensionless `S_eff=4.54477e-5`.

For mass product `M`, coherent interrogation `T`, fringe contrast `C`, accepted-event probability `p_acc`, and dead time `d`,

`R_D1 = p_acc C^2 [2 alpha G M T/(hbar L0)]^2 S_eff /(T+d)`.

This exposes a resource hidden by the old aggregate-phase benchmark.

## D1 correction/reclassification

The historical `sigma_phi=1 mrad` in Protocol 002B was aggregate phase uncertainty. With the current response the five-sigma mass-product scale at `T=1 s` is about `5.86e-29 kg^2`, but reaching `1 mrad` with binary fringe events requires

`N_acc >= 1/(C^2 sigma_phi^2)`.

Examples:

- `C=0.10`: `~1e8` accepted events;
- `C=0.66`: `~2.30e6`;
- `C=1`: `1e6`.

At `C=0.66`, `T=1 s`, `d=1 ms`, `p_acc=0.5`, this is about `53.2 days` detector wall time. The old mass scaling is not withdrawn; it is reclassified as conditional on an aggregate phase precision whose acquisition cost was previously external to the model.

Recorded as **RQIR-D1-002**: aggregate phase precision and coherent interaction time are distinct resources.

## D1 coherence optimum

For exponential contrast `C(T)=C0 exp(-T/T2)`, rate optimization gives

`T_opt=[T2-2d+sqrt((T2-2d)^2+16 d T2)]/4`.

For `d=1 ms`, `T_opt` is approximately `5.74 ms`, `50.96 ms`, and `0.501 s` for `T2=10 ms`, `100 ms`, and `1 s` respectively. With negligible dead time the limit is `T2/2`.

## D2 rate model

For equivalent-force ASD `A_F,n`,

`Delta F_n=2 alpha G M G_n/L0^2`,

`r_n=|Delta F_n|^2/A_F,n^2`,

and with live duty `eta`,

`R_D2=eta 4 r2 r4/(r2+r4)`.

Recorded as **RQIR-D2-002**: D2's native resource is force-PSD × live integration time, not arbitrary shot count.

For equal ASD in both bands and duty `0.5`, the current model gives five-sigma mass-product requirements:

- ASD `1e-18 N/sqrtHz`: `3.67e-17 kg^2` in 1 h, `7.50e-18` in 1 day, `1.37e-18` in 30 days;
- ASD `1e-21`: `3.67e-20`, `7.50e-21`, `1.37e-21`;
- ASD `1e-23`: `3.67e-22`, `7.50e-23`, `1.37e-23`.

The `1e-23` row is proposal-level, not achieved-RQIR hardware.

## External boundary check

- Pedalino et al., Nature 649, 866–870 (2026), DOI `10.1038/s41586-025-09917-9`: quantum/classical-discriminating ~172 kDa fringes reach visibility about `0.10`; heavier 400 kDa–1 MDa clusters reach `0.66 +/- 0.09`, but their current interferometer enters a regime where quantum and classical fringe predictions converge.
- Skrabulis et al., PRL 136, 233604 (2026), DOI `10.1103/9wzm-3qyb`: sub-zero-point impulsive-force resolution; not directly a stationary force ASD.
- Premawardhana et al., arXiv:2603.16487 (2026): proposal for broadband sub-`1e-23 N/sqrtHz` levitated-diamond sensing; retained only as a future-sensitivity scenario.

## New design rule

**RQIR-RESOURCE-004:** detector ranking must be Fisher-rate conditional. D1 aggregate phase uncertainty and D2 force ASD are different native resource coordinates and cannot support a universal branch ranking without contrast/coherence/throughput or PSD/duty assumptions.

## Files

- `analysis/branch_specific_fisher_rates_iteration019.py`
- `docs/BRANCH_SPECIFIC_PHYSICAL_FISHER_RATES.md`
- this log

## Next gate

Build an explicit source-preparation metrology rate and combine it with D1/D2 detector rates, corrected gravitational calibration rates and reference-control rates in a common wall-clock optimization of `F_beta|theta/T_wall`. Preserve the Iteration-015 hard-constraint correction and Iteration-016 structural-systematics priors.
