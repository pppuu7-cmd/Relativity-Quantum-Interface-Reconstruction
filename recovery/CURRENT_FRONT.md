# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 083**.

> `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework but may lag the fast resource front. For current work, read this pointer and the listed recovery deltas before starting a new gate. Repository state, not chat history, is authoritative.

## Publication-track status

- **Paper I scientific scope: CLOSED at Iteration 078.** RQIR-THM-001 abstracts Toy009/Toy010 into a finite nullspace response-discriminant existence theorem.
- **Paper II scientific scope: CLOSED at Iteration 079.** RQIR-STAT-001 freezes the reference-likelihood regression certificate.
- **Paper III: ACTIVE.** Iterations 080–083 provide the inverse apparatus specification envelope, prove absolute wall-clock normalization is not identifiable from normalized Fisher geometry alone, show that a real single-resonance levitated-force ASD cannot directly normalize the two-band RQIR likelihood, and derive the correct sequential-retuning gain-profile law.

## Active architecture status

- **Toy009:** mature global/statistical reference; literal radius-basis Hamiltonian remains dense/nonlocal.
- **Toy014:** leading balanced exact-nearest-neighbour local D2 candidate after physical multi-resource co-design.
- **Toy013:** retained calibration-specialized local comparison branch.
- **Toy011/Toy012:** retained as locality/history and negative-design evidence.

## Mandatory mature gates

- **NG-005:** gravitational exact-null cannot self-calibrate hidden source amplitude.
- **NG-006/007:** low-rank controls and stability floors can kill profiled Fisher even at high exposure.
- **NG-023:** H-QND source metrology is not automatically ordered-response nondemolition.
- **NG-025/026:** locality belongs inside co-design; exact rank completion is not finite-noise resource closure.
- Detector comparisons use spectral-tilt-profiled `F_beta|theta`, centered noise derivatives, exact hard constraints, and full same-time 2x2 matrix PSD/cross-PSD Fisher blocks.

## Physical Fisher-rate closure — Iterations 067–071

`T_sci = Z^2/R_beta`,

`T_cal = gamma_mean sum_j 1/R_cal,j`,

`T_src = C_prep/R_src`.

At retained multiplicative source-amplitude fraction `r`,

`C_prep=[r/(1-r)] Z^2`.

For current `Z=5`, `r=.90`, `C_prep=225`.

## Toy014 — Iterations 074–076

Toy014 retained physical same-kernel resource vector relative to Toy009:

`(q_s,q_c,q_p)=(3.53338589945,3.48482822888,0.67054046)`.

It is slower in science/calibration than Toy009 but faster in Ramsey source metrology. Its source-specific 100-Hz timing target is `~3.97715 us`. NG-006 survives without independent control references.

## Iteration 077 — apparatus-rate certificate

Primitive per-architecture inputs are `R_beta`, seven `R_cal,j`, `R_src`, and duty `d`.

`x = gamma_mean R_beta/Z^2 sum_j 1/R_cal,j`,

`y = C_prep R_beta/(Z^2 R_src)`,

`m = 1/(1-d)`,

`T_total = m (Z^2/R_beta) (1+x+y)`.

**RQIR-RESOURCE-036:** `(R_beta,x,y,d)` is the compressed architecture-selection certificate after the physical likelihood is fixed.

**RQIR-NG-030:** require conservative `T_i^upper < T_k^lower` for robust dominance.

## Iteration 078 — Paper-I scientific closure

**RQIR-THM-001:** a one-dimensional finite calibration null with nonzero response functional admits sufficiently small positive hidden-state pairs that are calibration-indistinguishable but response-distinguishable.

Files:
- `docs/PAPER_I_SCIENTIFIC_CLOSURE_ITERATION078.md`
- `research_log/2026-08-30_iteration_078_paper_i_scientific_closure.md`
- `recovery/RECOVERY_DELTA_ITERATION_078.md`

## Iteration 079 — Paper-II reference-likelihood closure

**RQIR-STAT-001:** mature likelihoods must pass Schur/projection identity, nuisance-coordinate invariance, calibration monotonicity, NG-005, NG-006, the two-band spectral-tilt identity, and the NUM-001 weak-nuisance threshold counterexample.

Files:
- `analysis/paper12_reference_regression_iteration079.py`
- `docs/PAPER_II_REFERENCE_LIKELIHOOD_CERTIFICATE_ITERATION079.md`
- `research_log/2026-08-30_iteration_079_paper_ii_reference_likelihood_certificate.md`
- `recovery/RECOVERY_DELTA_ITERATION_079.md`

## Iteration 080 — apparatus specification envelope

`H_cal = 7 / sum_j (1/R_cal,j)`,

`T_total = m [Z^2/R_beta + 7 gamma_mean/H_cal + C_prep/R_src]`.

**RQIR-RESOURCE-037:** `H_cal` is the exact one-number calibration throughput for the current independent-layer schedule.

**RQIR-NG-031:** separate minimum-rate floors are not jointly sufficient; an explicit science/calibration/source time allocation is required.

Files:
- `analysis/apparatus_specification_envelope_iteration080.py`
- `docs/PAPER_III_APPARATUS_SPECIFICATION_ENVELOPE_ITERATION080.md`
- `research_log/2026-08-30_iteration_080_apparatus_specification_envelope.md`
- `recovery/RECOVERY_DELTA_ITERATION_080.md`

## Iteration 081 — apparatus-closure identifiability audit

**RQIR-NG-032:** normalized Fisher/resource geometry does not determine absolute seconds. A common detector PSD scale changes wall time while leaving compressed dimensionless geometry unchanged.

**RQIR-APP-001:** absolute closure requires science transfer and full PSD/cross-PSD; seven physical two-probe calibration Jacobians/rates; source-metrology acceptance/coupling/visibility/reset/coherence; low-frequency controls, duty and uncertainties.

Files:
- `analysis/apparatus_closure_identifiability_iteration081.py`
- `docs/PAPER_III_APPARATUS_CLOSURE_IDENTIFIABILITY_ITERATION081.md`
- `research_log/2026-08-30_iteration_081_apparatus_closure_identifiability.md`
- `recovery/RECOVERY_DELTA_ITERATION_081.md`

## Iteration 082 — externally anchored D2 frequency-compatibility gate

Liang et al. (*Fundamental Research* 3, 57–62 (2023), DOI `10.1016/j.fmre.2022.09.021`) provide an experimental levitated-force anchor near `193.8 kHz`, with `6.33 +/- 1.62 zN/sqrt(Hz)` force sensitivity, best run `4.34 zN/sqrt(Hz)`, Allan-optimal time `~2751 s`, and stable force resolution `166.40 +/- 55.48 yN`.

Current RQIR D2 needs both `n=2` and `n=4` because `S_eff = 4 P2 P4/(P2+P4)`.

Aligning the single resonance to one RQIR band leaves the other thousands of reported linewidth scales away.

**RQIR-NG-033:** a single narrowband on-resonance ASD cannot by itself normalize a two-band RQIR Fisher discriminator. Do not apply it to both harmonics without measured transfer/PSD at both frequencies.

Files:
- `analysis/external_d2_frequency_compatibility_iteration082.py`
- `docs/PAPER_III_EXTERNAL_D2_FREQUENCY_COMPATIBILITY_ITERATION082.md`
- `research_log/2026-08-30_iteration_082_external_d2_frequency_compatibility.md`
- `recovery/RECOVERY_DELTA_ITERATION_082.md`

## Iteration 083 — sequential-retuning likelihood

For a narrowband detector retuned between the two science bands, let `P2,P4` be raw whitened science information and `C2,C4` independent gain/relock reference Fisher for the two apparatus settings. Profiling the independent setting gains gives

`F_beta = P2 C2/(P2+C2) + P4 C4/(P4+C4)`.

**RQIR-NG-034:** if the two retuned settings have independent unconstrained gains (`C2=C4=0`), then `F_beta=0` at arbitrary science exposure. Sequentially measuring both harmonics does not reproduce the simultaneous two-band discriminator for free.

Per setting, retaining a fraction `r` requires `C_i=[r/(1-r)]P_i`; 90/95/99% retention needs gain-reference Fisher 9/19/99 times that setting's science information.

Sequential retuning must therefore pay separate gain-reference time, relock/recertification duty, timing/phase drift, calibration-transfer uncertainty and source reproducibility.

Files:
- `analysis/sequential_retuning_gain_profile_iteration083.py`
- `docs/PAPER_III_SEQUENTIAL_RETUNING_LIKELIHOOD_ITERATION083.md`
- `research_log/2026-08-30_iteration_083_sequential_retuning_likelihood.md`
- `recovery/RECOVERY_DELTA_ITERATION_083.md`

## Immediate next gate — Paper III only

Prioritize a **simultaneous dual-mode or broadband detector closure** with measured transfer plus PSD/cross-PSD at two frequencies separated by a factor of two. If no suitable published platform supplies both bands, build a parameterized two-mode apparatus envelope anchored to measured force ASD and Allan stability, then propagate it through Toy009/Toy014 source spectra.

Only after both science bands have physical rate normalization should the seven `R_cal,j`, `R_src`, duty and uncertainty intervals be combined and NG-030 robust Toy009/Toy014 dominance tested. Do not start Toy015 unless that rate map shows a source-dependent bottleneck.

## Discipline

RQIR remains separate from RTK/DSIR. No toy, Fisher, resource or detector-model result is an empirical new-physics detection or a complete theory of quantum gravity. Classical/stochastic/hybrid/full-QFT degeneracy, relativistic, gauge/conservation/causality/EFT/renormalization and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
