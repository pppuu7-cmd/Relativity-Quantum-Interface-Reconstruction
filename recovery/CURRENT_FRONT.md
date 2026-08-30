# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 076**.

> This compact pointer exists because `docs/RECOVERY_GUIDE.md` currently lags the active research front. For recent science/resource results, follow the recovery deltas listed below rather than restarting from the older Toy012 priority.

## Active source/baseline status

- **Toy009:** mature global/statistical reference; literal radius-basis Hamiltonian is nonlocal/dense.
- **Toy014 (Iteration 074): leading balanced exact-nearest-neighbour local D2 source candidate.**
- **Toy013:** retained calibration-specialized local comparison branch.
- **Toy011:** locality existence/history; now Pareto-dominated by Toy014 in the retained physical three-axis comparison.
- **Toy012 balanced:** exact-locality existence result only; physically demoted after the two-band metric correction.
- **Toy012 high:** also Pareto-dominated by Toy014 after Iteration 074.

## Mandatory recent corrections

### Iteration 062 — physical two-band metric

`recovery/RECOVERY_DELTA_ITERATION_062.md`

Euclidean detector norm is not the spectral-tilt-profiled D2 Fisher. Balanced Toy012 physical D2 ratio is `~1.97e-8` of Toy009, not `0.21617`.

### Iteration 063 — detector nuisance inside calibration co-design

`recovery/RECOVERY_DELTA_ITERATION_063.md`

Spectral tilt must be inside the full source/calibration Fisher. Old Toy012 near-Toy009 calibration claim is withdrawn for physical D2.

### Iterations 064–066 — Toy013 and architecture dominance

Toy013 trial 29100 is calibration-efficient (`q_cal~0.1233`) but has science penalty `23.65x` and severe Ramsey source-metrology penalty. Toy013 beats Toy009 only in a calibration-dominated region.

### Iterations 067–071 — physical Fisher-rate closure

Latest general resource equations:

`T_sci = Z^2/R_beta`

`T_cal = gamma_mean sum_j 1/R_cal,j`

`T_src = C_prep/R_src`

`x = gamma_mean R_beta/Z^2 sum_j 1/R_cal,j`

`y = C_prep R_beta/(Z^2 R_src)`.

At 90% retained multiplicative beta/source-amplitude Fisher:

`y = 9 R_beta/R_src`.

Use full same-time `2x2` matrix PSD/Fisher blocks; do not sum scalar SNRs when cross spectra are present.

## Latest executed front

### Iteration 072 — Toy012 physical dominance closure

Balanced Toy012 is componentwise worse than Toy009 in the shared-kernel physical science/calibration/Ramsey resource projection and is removed from the physical Pareto front.

### Iteration 073 — local Pareto audit

Before Toy014, four local branches occupied different resource regions; this motivated true multi-resource source co-design.

### Iteration 074 — Toy014 executed

Toy014 geometry:

- `q0=(0.276628448462335,0.692706589526471,0.133811514954169,0.242173595051988,0.605871859928477)`;
- `y1=-5.776797810075849`;
- phases `(0,1.282219941742947,1.828517907056411,3.566406614507335,3.168865574324793,4.280901503306583,2.751657214339520)`.

Physical resource vector relative to Toy009:

`(q_s,q_c,q_p) = (3.5334, 3.4848, 0.6705)`

where the axes are same-kernel D2 science time, spectral-tilt-profiled calibration cost, and zero-reset Ramsey source-metrology time.

Toy014 componentwise dominates Toy011-response, Toy011-conditioning and Toy012-high on these axes. Toy013 remains non-dominated because it is much cheaper to calibrate.

### Iteration 075 — Toy014 controls

NG-006 survives: unconstrained timing/geometry/additive controls collapse final profiled Fisher even at large exposure.

Toy014 10% control bundle:

- `sigma(delta y1)=0.74131718`;
- `sigma(delta tau)=0.00249891877`;
- `sigma_t(100 Hz)=3.97715 us`;
- `sigma(b_mean)=4.19676e-5`;
- `sigma(b_cov)=6.06487e-5`.

With bundle: `F_beta|theta~0.8999686`.

### Iteration 076 — timing recertification duty

In the declared Brownian drift / white reference model:

`d_tau proportional to D_tau sigma_event^2 t_cycle / sigma_target^4`.

Toy014 reference duty is ~24.9x Toy009 under equal drift/jitter assumptions, but remains below 1% for the transparent `D=100–1000 us^2/h` examples.

Control-aware Toy014-vs-Toy009 projected boundary is approximately

- `D=100`: `y > 7.7118 + 7.5640 x`;
- `D=1000`: `y > 7.9178 + 7.7665 x`.

## Immediate next gate

Build an apparatus-requirement map for the surviving physical architectures **Toy009 / Toy014 / Toy013** using only measurable/declared ratios:

1. profiled science Fisher rate `R_beta`;
2. seven same-time dual-probe matrix calibration rates `R_cal,j`;
3. independent source-metrology rate `R_src` including reset/readout/visibility;
4. timing/control duty including drift floor.

Derive the architecture boundaries in these rates without inventing absolute detector ASD values. After that, either instantiate a repository-backed detector model or begin a broader Toy015 search only if the rate map shows a source-design bottleneck.

## Discipline

No toy/result above is an empirical quantum-gravity detection or a complete theory of quantum gravity. All gauge/conservation/causality/EFT/renormalization/classical-stochastic/full-QFT degeneracy and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
