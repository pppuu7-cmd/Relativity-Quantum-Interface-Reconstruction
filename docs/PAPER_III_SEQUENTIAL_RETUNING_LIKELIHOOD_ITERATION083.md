# RQIR Iteration 083 — Sequential-Retuning Narrowband Likelihood

**Date:** 2026-08-30  
**Status:** Paper-III detector/resource gate; analytic result plus numerical regression, not an apparatus forecast and not a new-physics claim.

## 1. Motivation

Iteration 082 showed that a single narrow mechanical resonance cannot be treated as if its record force ASD applied simultaneously to both retained RQIR bands. One admissible alternative is to retune/relock the same detector sequentially: acquire the `n=2` band in one configuration and the `n=4` band in another.

That changes the nuisance geometry. In particular, the two acquisitions no longer share an automatically common detector gain.

## 2. Minimal sequential likelihood

Let the whitened science information accumulated in the two settings be

`P2`, `P4`.

Let `g2`, `g4` be independent fractional gain/relock nuisances for the two apparatus configurations. Let independent reference measurements supply gain Fisher

`C2`, `C4`.

Locally, beta and each corresponding gain enter the same band amplitude, so the Fisher matrix for parameters `(beta,g2,g4)` is

`F = [[P2+P4, P2, P4], [P2, P2+C2, 0], [P4, 0, P4+C4]]`.

Profiling `g2,g4` gives the exact closed form

`F_beta = P2 C2/(P2+C2) + P4 C4/(P4+C4)`.

This has a direct resource interpretation: every retuned band carries its own science-versus-reference harmonic bottleneck.

## 3. RQIR-NG-034 — unreferenced sequential retuning loses common-amplitude identifiability

If the two retuned configurations have independent unconstrained gains,

`C2=C4=0`,

then

`F_beta=0`

no matter how large `P2` and `P4` become.

Thus sequentially measuring both source harmonics does **not** by itself reproduce the simultaneous two-band spectral-tilt discriminator. The common interface amplitude can be absorbed independently into the two unconstrained setting gains.

More exposure cannot repair this exact degeneracy.

## 4. Finite gain-reference law

Each band retains the fraction

`r_i = C_i/(P_i+C_i)`

of its raw science information, so

`F_beta = P2 r_2 + P4 r_4`.

To retain a desired fraction `r` in one isolated band requires

`C_i = [r/(1-r)] P_i`.

Therefore:

- 90% retention needs `C_i=9 P_i` for each retuned setting;
- 95% retention needs `C_i=19 P_i`;
- 99% retention needs `C_i=99 P_i`.

This is structurally analogous to NG-005 but applies to apparatus reconfiguration gain rather than hidden source amplitude.

## 5. Resource consequence

If gain-reference information is accumulated at rates `R_g2,R_g4`, while science information is accumulated at `R_2,R_4`, sequential retuning incurs at minimum

`T = P2/R_2 + P4/R_4 + C2/R_g2 + C4/R_g4 + T_relock + T_recert`,

before source-metrology and the seven calibration layers are added.

The `T_relock/T_recert` terms must also carry low-frequency drift and stability uncertainty. A nominally fast resonance tune is not free if it changes gain, phase, geometry or PSD normalization.

## 6. Relation to the simultaneous two-band law

For one simultaneous detector configuration with one common amplitude and one antisymmetric spectral-tilt nuisance, the retained shape Fisher can be

`S_eff = 4 P2 P4/(P2+P4)`.

The sequential-retuning result is a different likelihood. It must not be substituted into or equated with that formula unless the apparatus demonstrates the corresponding shared gain/covariance structure.

A sequential experiment can recover nearly all `P2+P4` only in the strong-reference limit

`C2 >> P2`, `C4 >> P4`.

## 7. Numerical regression

The stored script verifies the Schur complement against the analytic formula. Examples:

- `P2=P4=1`, `C2=C4=0` -> `F_beta=0`;
- `P2=P4=1`, `C2=C4=1` -> `F_beta=1` versus raw `2`;
- `P2=1`, `P4=3`, `C2=C4=100` -> `F_beta~3.90272` versus raw `4`;
- strong references approach the raw `P2+P4` limit.

## 8. Consequence for the external levitated-force anchor

Iteration 082's single-resonance detector could only become an admissible RQIR architecture by sequential retuning if the experiment supplies, for **each** band:

1. measured transfer and PSD at the retuned resonance;
2. gain/relock calibration Fisher `C_i` or rate `R_gi`;
3. phase/timing reference after retuning;
4. source reproducibility across the two acquisitions;
5. relock/recertification duty and long-time stability.

The published single on-resonance force ASD and one Allan curve do not yet supply these quantities.

## 9. Design decision

A simultaneous dual-mode/broadband detector remains preferable when available because it can preserve a genuinely shared likelihood and avoid paying two independent gain-reference bottlenecks. Sequential retuning remains scientifically admissible, but only with explicit per-setting reference information.

This gives a concrete criterion for the next apparatus search: prioritize experimental platforms with either two simultaneously calibrated modes or demonstrated reproducible retuning plus gain/phase transfer calibration.

## 10. Reproducibility

Run

`python analysis/sequential_retuning_gain_profile_iteration083.py`.
