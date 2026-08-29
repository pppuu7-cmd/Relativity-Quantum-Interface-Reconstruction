# RQIR Branch-Specific Physical Fisher Rates — Iteration 019

**Date:** 2026-08-29  
**Status:** physical resource/rate layer for the Iteration-011 Toy009 baseline; not an experimental forecast and not a new-physics claim.

## 1. Why this iteration is needed

Iteration 018 still used a standardized single-shot sensitivity `xi`. That was useful for bookkeeping but prevented a physically meaningful comparison of D1 and D2 because the two branches acquire information in fundamentally different ways.

This iteration replaces that final common `xi` layer by branch-specific parametric Fisher rates:

- D1: accepted matter-wave fringe events with finite contrast, four-switch response window, coherent interrogation time, acceptance probability, and dead time;
- D2: continuous equivalent-force PSD in the two response bands and detector duty cycle.

The source and calibration geometry remain the accepted Iteration-011 Toy009 baseline.

Accepted response harmonics (rounded stored values):

`H2 = +0.00245460 - i 0.01049981`

`H4 = -0.00395383 - i 0.01338211`

`G2 = +0.00285553 - i 0.01750306`

`G4 = -0.00463232 - i 0.01567853`.

## 2. D1 — physical phase-shot Fisher rate

For the pi-periodic four-switch sequence, with positive interval `a` in each half period,

`|W2| = 2 |sin(a)| / pi`,

`|W4| = |sin(2a)| / pi`.

Optimizing the current Iteration-011 harmonics gives approximately

`a = 0.90716`,

`|W2| = 0.50150`,

`|W4| = 0.30892`,

and the dimensionless profiled two-band response

`S_eff,4sw ~= 4.54477e-5`.

The common physical phase scale for mass product `M=m_s m_p` and coherent interrogation time `T` is

`A_phi = 2 alpha G M T / (hbar L0)`.

At quadrature, an ideal binary fringe event with visibility/contrast `C` carries phase Fisher of order `C^2`. Therefore the local detector information per accepted event is modeled as

`I_D1,event = C^2 A_phi^2 S_eff,4sw`.

With accepted-event probability `p_acc` and extra dead time `t_dead`,

`R_D1 = p_acc I_D1,event / (T+t_dead)`.

This makes the missing physical dependence explicit:

`R_D1 proportional to p_acc C^2 M^2 T^2/(T+t_dead)`

before decoherence is included.

## 3. Correction/reclassification of the old 1-mrad benchmark

The historical Protocol-002B assumption `sigma_phi=1 mrad` was an **aggregate phase uncertainty**, not a demonstrated one-event phase noise.

For the current Iteration-011 response and four-switch window, the corresponding five-sigma mass-product scaling at `T=1 s`, `alpha=0.1`, `L0=10 um` is

`M ~= 5.86e-29 kg^2`.

The mass scaling itself is retained. The new point is that obtaining the assumed aggregate `1 mrad` precision costs events.

Using the binary-fringe Cramer-Rao scaling

`sigma_phi^2 >= 1/(N_acc C^2)`,

one needs

`N_acc >= 1/(C^2 sigma_phi^2)`.

For `sigma_phi=1 mrad`:

- `C=0.10` -> about `1.0e8` accepted events;
- `C=0.66` -> about `2.30e6` accepted events;
- `C=1` -> `1.0e6` accepted events.

For the illustrative `C=0.66`, `T=1 s`, `t_dead=1 ms`, `p_acc=0.5`, the detector-only wall time for those events is about `53.2 days`.

Thus the old mass-product benchmark must not be read as a one-second experiment. It assumed a one-second coherent interaction time **per effective phase estimate** while leaving the acquisition cost of the 1-mrad phase precision outside the model.

### RQIR-D1-002 — aggregate phase precision and coherent interaction are distinct resources

A phase-scaling benchmark written with an aggregate `sigma_phi` hides the number of accepted fringe events needed to achieve that phase precision. D1 resource accounting must therefore track at least

`(mass product, contrast, coherent interrogation time, accepted-event rate, dead time)`

rather than only `(mass product, T, sigma_phi)`.

## 4. D1 coherence/throughput tradeoff

If contrast decays approximately as

`C(T)=C0 exp(-T/T2)`,

then, with constant acceptance probability, the detector Fisher rate scales as

`R_D1 proportional to exp(-2T/T2) T^2/(T+t_dead)`.

The positive stationary point is

`T_opt = [T2 - 2 d + sqrt((T2-2d)^2 + 16 d T2)]/4`,

where `d=t_dead`.

For `d=1 ms`:

- `T2=10 ms` -> `T_opt ~= 5.74 ms`;
- `T2=100 ms` -> `T_opt ~= 50.96 ms`;
- `T2=1 s` -> `T_opt ~= 0.501 s`.

With negligible dead time, `T_opt -> T2/2`.

This replaces the implicit assumption that longer coherent interrogation is always better.

## 5. D2 — physical force-PSD Fisher rate

For D2 the physical force harmonics are

`Delta F_n = 2 alpha G M G_n / L0^2`.

Let the one-sided equivalent-force amplitude spectral densities in the two bands be `A_F,2` and `A_F,4`, so

`S_F,n = A_F,n^2`.

Define information rates

`r_n = |Delta F_n|^2 / S_F,n`.

After profiling the same relative spectral-tilt nuisance, the continuous two-band detector rate is

`R_D2 = eta_duty * 4 r2 r4/(r2+r4)`.

This is already Fisher per unit wall-clock time in the stationary-PSD approximation. Mechanical susceptibility is not an extra free gain if the PSD has already been converted to equivalent force noise.

### RQIR-D2-002 — D2 resource is PSD-time, not shot count

D2's natural detector resource is equivalent-force noise spectral density times live integration time. Converting it into arbitrary `shots` obscures the actual physics and can double-count resonant susceptibility.

## 6. D2 scaling examples

For equal ASD in both bands and duty cycle `0.5`, the five-sigma mass product required by the current Toy009 gradient response is approximately:

| force ASD | 1 hour | 1 day | 30 days |
|---|---:|---:|---:|
| `1e-18 N/sqrtHz` | `3.67e-17 kg^2` | `7.50e-18 kg^2` | `1.37e-18 kg^2` |
| `1e-21 N/sqrtHz` | `3.67e-20 kg^2` | `7.50e-21 kg^2` | `1.37e-21 kg^2` |
| `1e-23 N/sqrtHz` | `3.67e-22 kg^2` | `7.50e-23 kg^2` | `1.37e-23 kg^2` |

These rows are declared sensitivity scenarios, not claims that those continuous two-band ASDs have been achieved in an RQIR-compatible apparatus.

The `1e-23 N/sqrtHz` scale is especially important to label as proposal-level: a 2026 levitated-diamond proposal reports projected sub-zeptonewton broadband sensitivity, whereas a 2026 levitated-nanoparticle experiment demonstrated sub-zero-point **impulse** resolution, which is not the same observable as a stationary continuous force ASD.

## 7. Current experimental anchors

Pedalino et al., *Nature* 649, 866–870 (2026), DOI `10.1038/s41586-025-09917-9`, report matter-wave interference of sodium clusters around 172 kDa with quantum/classical discrimination and fringe visibility up to about `0.10`; for heavier 400 kDa–1 MDa clusters they report visibility `0.66 +/- 0.09`, but in that high-mass configuration the quantum and classical predictions converge. Therefore `C=0.66` is useful only as an empirical high-contrast anchor, not as direct evidence that an RQIR-scale coherent probe is available.

Skrabulis et al., *PRL* 136, 233604 (2026), DOI `10.1103/9wzm-3qyb`, demonstrate impulsive-force resolution below the sensor zero-point momentum scale. This validates advanced levitated mechanical sensing but must not be inserted as a continuous `N/sqrtHz` force floor without a transfer/noise model.

Premawardhana et al., arXiv:2603.16487 (2026), propose broadband levitated-diamond force sensitivity below `1e-23 N/sqrtHz` around `10^4 Hz`; this is retained only as a proposal-level future sensitivity scenario.

## 8. Consequence for D1 versus D2

The two branches now have physically different rate laws:

`R_D1 proportional to C(T)^2 M^2 T^2/(T+t_dead)`

versus

`R_D2 proportional to eta_duty M^2 / S_F`.

So the earlier statement "D1 is stronger than D2" is not a detector-independent fact. It was true under the earlier declared aggregate phase-noise and force-ASD benchmarks. Once physical rates are explicit:

- D1 can win through long coherent interrogation, high contrast and high accepted-event throughput;
- D2 can win through low continuous equivalent-force PSD, large classical detector mass and high duty cycle;
- neither branch can be ranked without its actual coherence/throughput or PSD/duty parameters.

### RQIR-RESOURCE-004 — detector ranking must be Fisher-rate conditional

A detector branch should be ranked only after its native physical information rate is specified. Aggregate phase uncertainty and force ASD are not interchangeable resource coordinates.

## 9. What is still missing

This iteration closes the detector-rate parameterization but not the full experiment optimization. Still required:

1. explicit source-preparation Fisher rate rather than `C_a` alone;
2. calibration/reference-channel rates for the corrected Iteration-015/016 nuisance model;
3. a common source mass/gap/separation/coherence budget;
4. joint optimization of detector, preparation, calibration and controls in `F_beta|theta/T_wall`;
5. mandatory G1/G2/G3/G4a/G8/G9/G10/G12/G13 consistency gates before fundamental interpretation.

## Reproducibility

Code: `analysis/branch_specific_fisher_rates_iteration019.py`.
