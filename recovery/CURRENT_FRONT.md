# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 082**.

> `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework but may lag the fast resource front. For current work, read this pointer and the listed recovery deltas before starting a new gate. Repository state, not chat history, is authoritative.

## Publication-track status

- **Paper I scientific scope: CLOSED at Iteration 078.** RQIR-THM-001 abstracts Toy009/Toy010 into a finite nullspace response-discriminant existence theorem. Remaining work is manuscript/literature/novelty/reproduction work, not a missing Paper-I scientific gate.
- **Paper II scientific scope: CLOSED at Iteration 079.** RQIR-STAT-001 freezes the reference-likelihood regression certificate: Schur/projection identity, nuisance-coordinate invariance, calibration monotonicity, NG-005, NG-006 exposure obstruction, spectral-tilt identity and NUM-001 threshold counterexample.
- **Paper III: ACTIVE.** Iterations 080–082 provide the inverse apparatus specification envelope, prove absolute wall-clock normalization is not identifiable from normalized Fisher geometry alone, and show with a real levitated-force apparatus that a record single-resonance ASD cannot directly normalize the two-band RQIR likelihood.

## Active architecture status

- **Toy009:** mature global/statistical reference; literal radius-basis Hamiltonian remains dense/nonlocal.
- **Toy014:** leading balanced exact-nearest-neighbour local D2 candidate after physical multi-resource co-design.
- **Toy013:** retained calibration-specialized local comparison branch; non-dominated only in sufficiently calibration-heavy regimes.
- **Toy011/Toy012:** retained as locality/history and negative-design evidence; no longer leading physical resource branches after the two-band/spectral-tilt corrections and Toy014 search.

## Mandatory mature gates

- **NG-005:** gravitational exact-null cannot self-calibrate hidden source amplitude; independent source metrology is mandatory.
- **NG-006/007:** low-rank controls and stability floors can kill profiled Fisher even at high exposure.
- **NG-023:** H-QND source metrology is not automatically ordered-response nondemolition; strong source metrology belongs on independent/sacrificial copies unless a full same-copy likelihood proves otherwise.
- **NG-025/026:** locality belongs inside co-design; exact rank completion is not finite-noise resource closure.
- Detector comparisons use spectral-tilt-profiled `F_beta|theta`, centered noise derivatives, exact hard constraints, and full same-time 2x2 matrix PSD/cross-PSD Fisher blocks.

## Physical Fisher-rate closure — Iterations 067–071

Use

`T_sci = Z^2/R_beta`,

`T_cal = gamma_mean sum_j 1/R_cal,j`,

`T_src = C_prep/R_src`.

At retained multiplicative source-amplitude fraction `r`,

`C_prep=[r/(1-r)] Z^2`.

For current `Z=5`, `r=.90`, `C_prep=225`.

## Toy014 — Iterations 074–076

Toy014 retained physical same-kernel resource vector relative to Toy009:

`(q_s,q_c,q_p)=(3.53338589945,3.48482822888,0.67054046)`.

It is slower in science/calibration than Toy009 but faster in Ramsey source metrology; it componentwise dominates the previously retained physical Toy011/Toy012 local branches on the audited axes.

Toy014 controls remain source-specific. Its 100-Hz timing target is `~3.97715 us`; unconstrained low-rank timing/geometry/additive controls still collapse final profiled Fisher (NG-006 survives).

Under the declared Brownian timing-reference benchmark, recertification duty carries a fourth-power tolerance penalty but stays below 1% for the illustrative `D=100–1000 us^2/h` cases. This is not an apparatus prediction.

## Iteration 077 — apparatus-rate certificate

Primitive per-architecture inputs:

1. nuisance-profiled detector science Fisher rate `R_beta`;
2. seven same-time dual-probe matrix calibration rates `R_cal,j`;
3. independent source-metrology rate `R_src` including preparation/reset/readout/acceptance/visibility;
4. timing/reference duty `d`.

Compress them to

`x = gamma_mean R_beta/Z^2 sum_j 1/R_cal,j`,

`y = C_prep R_beta/(Z^2 R_src)`,

`m = 1/(1-d)`.

Then

`T_total = m (Z^2/R_beta) (1+x+y)`.

**RQIR-RESOURCE-036:** after the physical likelihood/profile are fixed, the sufficient architecture-selection certificate is `(R_beta,x,y,d)` per branch. Keep all seven `R_cal,j` as audit inputs even though they compress to `x` in total wall clock.

**RQIR-NG-030:** a nominal branch crossing is not retained when rate/duty uncertainty intervals overlap. Require conservative `T_i^upper < T_k^lower` for robust architecture dominance.

## Iteration 078 — Paper-I scientific closure

**RQIR-THM-001:** in a finite reduced physical tangent space, if a finite linear calibration map has one-dimensional null `n`, an interior nominal density state exists, and a linear response functional obeys `c(n)!=0`, then sufficiently small positive/negative perturbations along `n` are both physical, calibration-indistinguishable, and response-distinguishable.

This formalizes Toy009/Toy010. It does not assert that gravity transmits `D/chi^R` or that spacetime is quantum.

Files:
- `docs/PAPER_I_SCIENTIFIC_CLOSURE_ITERATION078.md`
- `research_log/2026-08-30_iteration_078_paper_i_scientific_closure.md`
- `recovery/RECOVERY_DELTA_ITERATION_078.md`

## Iteration 079 — Paper-II reference-likelihood closure

**RQIR-STAT-001** requires mature likelihoods to pass Schur/projection identity, nuisance-coordinate invariance, calibration monotonicity, NG-005 finite-preparation law, NG-006 exact-alignment exposure obstruction, the two-band spectral-tilt identity, and the NUM-001 weak-nuisance threshold counterexample.

Files:
- `analysis/paper12_reference_regression_iteration079.py`
- `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md`
- `research_log/2026-08-30_iteration_079_paper_ii_reference_likelihood_certificate.md`
- `recovery/RECOVERY_DELTA_ITERATION_079.md`

## Iteration 080 — apparatus specification envelope

Define

`H_cal = 7 / sum_j (1/R_cal,j)`.

Then

`T_total = m [Z^2/R_beta + 7 gamma_mean/H_cal + C_prep/R_src]`.

**RQIR-RESOURCE-037:** `H_cal` is the exact one-number calibration throughput for the current independent-layer scheduling model.

**RQIR-NG-031:** the three individual minimum-rate floors are not jointly sufficient; setting science, calibration and source rates exactly at their separate floors gives `T_total=3*T_cap`. Use an explicit time allocation `f_sci+f_cal+f_src=1` for sufficient target specifications.

Files:
- `analysis/apparatus_specification_envelope_iteration080.py`
- `docs/PAPER_III_APPARATUS_SPECIFICATION_ENVELOPE_ITERATION080.md`
- `research_log/2026-08-30_iteration_080_apparatus_specification_envelope.md`
- `recovery/RECOVERY_DELTA_ITERATION_080.md`

## Iteration 081 — apparatus-closure identifiability audit

**RQIR-NG-032:** normalized Fisher/resource geometry does not determine absolute seconds. A common detector PSD rescaling changes absolute detector/calibration wall time while leaving the compressed dimensionless geometry unchanged. Independent source metrology retains its own absolute-rate freedom until acceptance, visibility, coupling and reset/readout are fixed.

**RQIR-APP-001:** minimum apparatus closure requires science transfer and full PSD/cross-PSD; seven physical two-probe calibration Jacobians and matrix rates; source-metrology acceptance/coupling/visibility/reset/coherence; low-frequency control/reference stability, duty and uncertainties.

Files:
- `analysis/apparatus_closure_identifiability_iteration081.py`
- `docs/PAPER_III_APPARATUS_CLOSURE_IDENTIFIABILITY_ITERATION081.md`
- `research_log/2026-08-30_iteration_081_apparatus_closure_identifiability.md`
- `recovery/RECOVERY_DELTA_ITERATION_081.md`

## Iteration 082 — externally anchored D2 frequency-compatibility gate

A real levitated silica-nanosphere force sensor (Liang et al., *Fundamental Research* 3, 57–62 (2023), DOI `10.1016/j.fmre.2022.09.021`) supplies an experimental anchor near a `193.8 kHz` mechanical resonance, with reported `6.33 +/- 1.62 zN/sqrt(Hz)` force sensitivity, best run `4.34 zN/sqrt(Hz)`, Allan-optimal time `~2751 s`, and stable force resolution `166.40 +/- 55.48 yN`.

The current RQIR D2 discriminator requires both `n=2` and `n=4` bands because

`S_eff = 4 P2 P4/(P2+P4)`.

If the `193.8 kHz` resonance is aligned to `n=2`, the other band lies at `387.6 kHz`, about `9888` reported-linewidth scales away. If aligned to `n=4`, the other band lies at `96.9 kHz`, about `4944` linewidth scales away.

**RQIR-NG-033:** a single narrowband detector sensitivity measured at one mechanical resonance cannot by itself normalize a two-band RQIR Fisher discriminator whose identifiability requires finite whitened information in both bands. Do not apply a record on-resonance ASD to both RQIR harmonics without measured transfer/PSD at both frequencies.

The external Allan data also reinforce the separation between short-time matched-filter PSD and long-time stability/recertification duty; do not extrapolate the best ASD indefinitely as `1/sqrt(T)`.

Files:
- `analysis/external_d2_frequency_compatibility_iteration082.py`
- `docs/PAPER_III_EXTERNAL_D2_FREQUENCY_COMPATIBILITY_ITERATION082.md`
- `research_log/2026-08-30_iteration_082_external_d2_frequency_compatibility.md`
- `recovery/RECOVERY_DELTA_ITERATION_082.md`

## Immediate next gate — Paper III only

Find or construct an admissible **two-band detector closure** for Toy009 and Toy014. Priority order:

1. published dual-mode or broadband levitated detector with calibrated transfer plus PSD/cross-PSD at two frequencies separated by a factor of two;
2. otherwise a parameterized two-mode apparatus envelope anchored to measured force/noise and Allan-stability data;
3. alternatively derive a sequential-retuning joint likelihood with explicit relock duty, inter-setting gain/timing drift, calibration uncertainty and source reproducibility.

Only after both science bands have physical rate normalization should the seven `R_cal,j`, `R_src`, duty and uncertainty intervals be combined and NG-030 robust Toy009/Toy014 dominance tested. Do not start Toy015 unless the resulting rate map shows a source-dependent bottleneck.

## Discipline

RQIR remains separate from RTK/DSIR. No toy, Fisher, resource or detector-model result is an empirical new-physics detection or a complete theory of quantum gravity. Classical/stochastic/hybrid/full-QFT degeneracy, relativistic, gauge/conservation/causality/EFT/renormalization and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
