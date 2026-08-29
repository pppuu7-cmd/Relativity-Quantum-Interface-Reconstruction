# RQIR Recovery Delta — Iteration 019

**Date:** 2026-08-29  
**Applies after:** `docs/RECOVERY_GUIDE.md` v1.6

## New closed layer

Iteration 019 replaces the standardized detector sensitivity `xi` by native branch-specific parametric Fisher rates for the current Iteration-011 Toy009 baseline.

### D1

Current four-switch optimum for the stored rounded harmonics:

- `a ~= 0.90716`;
- `|W2| ~= 0.50150`;
- `|W4| ~= 0.30892`;
- `S_eff,4sw ~= 4.54477e-5`.

Physical rate:

`R_D1 = p_acc C^2 [2 alpha G M T/(hbar L0)]^2 S_eff /(T+t_dead)`.

**RQIR-D1-002:** aggregate phase precision and coherent interaction time are separate resources. The old `sigma_phi=1 mrad` mass-product benchmark did not include the number of fringe events required to achieve 1 mrad.

At `T=1 s`, current five-sigma aggregate-1-mrad mass-product scaling is `~5.86e-29 kg^2`. Event requirement is `N_acc>=1/(C^2 sigma_phi^2)`. For `C=0.66`, `sigma_phi=1 mrad`, this is `~2.30e6` accepted events; with `p_acc=0.5` and `1 ms` dead time, about `53.2 days` wall time.

For exponential contrast `C(T)=C0 exp(-T/T2)`,

`T_opt=[T2-2d+sqrt((T2-2d)^2+16dT2)]/4`,

approaching `T2/2` for negligible dead time.

### D2

Physical force-domain rate:

`Delta F_n=2 alpha G M G_n/L0^2`,

`r_n=|Delta F_n|^2/S_F,n`,

`R_D2=eta_duty 4 r2 r4/(r2+r4)`.

**RQIR-D2-002:** D2's native resource is equivalent-force PSD times live integration time; do not translate continuous force sensing into arbitrary shot equivalents when ranking the detector branch.

### Cross-branch rule

**RQIR-RESOURCE-004:** detector ranking is conditional on native physical Fisher rate. D1 requires contrast/coherence/accepted-event/dead-time assumptions; D2 requires force PSD and duty-cycle assumptions. The earlier D1>D2 ranking is retained only under the previously declared aggregate phase-noise and force-ASD benchmarks, not as a universal statement.

## External empirical boundary retained

- Pedalino et al., Nature 649, 866–870 (2026), DOI `10.1038/s41586-025-09917-9`: ~172 kDa quantum/classical-discriminating fringes with visibility up to about `0.10`; heavier 400 kDa–1 MDa fringes reach `0.66 +/- 0.09`, but current quantum/classical predictions converge in that heavy configuration.
- Skrabulis et al., PRL 136, 233604 (2026), DOI `10.1103/9wzm-3qyb`: sub-zero-point impulse resolution, not directly a continuous force ASD.
- Premawardhana et al., arXiv:2603.16487 (2026): proposed sub-`1e-23 N/sqrtHz` broadband levitated-diamond force sensitivity; proposal-level only.

## Continuation target

Next iteration should assign an explicit independent source-preparation metrology rate and combine detector + preparation + corrected gravitational calibration + reference/control resources in one wall-clock `F_beta|theta/T_wall` optimization. Preserve:

- RQIR-NG-005 hidden-amplitude obstruction;
- RQIR-NUM-001 hard elimination of exact trace/energy constraints;
- RQIR-NG-006 low-rank systematic degeneracy;
- Iteration-016 finite control priors;
- Iteration-017 product-like gain-state bias.

Do not interpret Iteration-019 rate examples as experimental readiness or new physics.
