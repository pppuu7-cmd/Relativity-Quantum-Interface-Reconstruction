# RQIR Current Front Pointer

**Updated:** 2026-08-30  
**Authoritative front:** through **Iteration 084**.

> `docs/RECOVERY_GUIDE.md` and `docs/MASTER_TABLE.md` contain the mature framework but may lag the fast resource front. Read this pointer plus the listed recovery deltas before starting a new gate. Repository state, not chat history, is authoritative.

## Publication-track status

- **Paper I scientific scope: CLOSED at Iteration 078.** RQIR-THM-001 abstracts Toy009/Toy010 into a finite nullspace response-discriminant existence theorem.
- **Paper II scientific scope: CLOSED at Iteration 079.** RQIR-STAT-001 freezes the reference-likelihood regression certificate.
- **Paper III: ACTIVE.** Iterations 080–084 now provide the inverse apparatus specification envelope, absolute-rate identifiability audit, single-resonance frequency incompatibility, sequential-retuning gain-profile law, and simultaneous two-band physical Fisher-rate closure.

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
- Detector comparisons use spectral-tilt-profiled `F_beta|theta`, centered noise derivatives, exact hard constraints, and full same-time matrix PSD/cross-PSD Fisher blocks.

## Physical wall-clock backbone

Use

`T_sci = Z^2/R_beta`,

`T_cal = gamma_mean sum_j 1/R_cal,j`,

`T_src = C_prep/R_src`,

with `C_prep=[r/(1-r)] Z^2`; for `Z=5`, `r=.90`, `C_prep=225`.

Iteration 077 compresses a fully normalized apparatus to `(R_beta,x,y,d)` with

`x = gamma_mean R_beta/Z^2 sum_j 1/R_cal,j`,

`y = C_prep R_beta/(Z^2 R_src)`,

`m = 1/(1-d)`,

`T_total = m (Z^2/R_beta)(1+x+y)`.

**RQIR-NG-030:** branch dominance is retained only when conservative uncertainty intervals do not overlap: require `T_i^upper < T_k^lower`.

Iteration 080 defines

`H_cal = 7 / sum_j(1/R_cal,j)`

and

`T_total = m[Z^2/R_beta + 7 gamma_mean/H_cal + C_prep/R_src]`.

**RQIR-NG-031:** separate componentwise minimum-rate floors are not jointly sufficient; explicit science/calibration/source time allocation is required.

## Iteration 081 — absolute-rate identifiability

**RQIR-NG-032:** normalized Fisher/resource geometry does not determine absolute seconds. A common PSD or Fisher-rate scale can leave dimensionless architecture ratios unchanged while rescaling wall time.

**RQIR-APP-001:** apparatus closure requires science transfer plus full PSD/cross-PSD, seven physical calibration Jacobians/rates, source-metrology acceptance/coupling/visibility/reset/coherence, control-reference stability/duty and uncertainty intervals.

Files:
- `analysis/apparatus_closure_identifiability_iteration081.py`
- `docs/PAPER_III_APPARATUS_CLOSURE_IDENTIFIABILITY_ITERATION081.md`
- `recovery/RECOVERY_DELTA_ITERATION_081.md`

## Iteration 082 — single-resonance incompatibility

Using the externally anchored Liang et al. levitated-force sensor near `193.8 kHz`, a single quoted on-resonance ASD cannot normalize both RQIR science harmonics, which are separated by a factor two.

**RQIR-NG-033:** never apply one narrowband on-resonance ASD to both RQIR bands without measured transfer/PSD at both frequencies.

Files:
- `analysis/external_d2_frequency_compatibility_iteration082.py`
- `docs/PAPER_III_EXTERNAL_D2_FREQUENCY_COMPATIBILITY_ITERATION082.md`
- `recovery/RECOVERY_DELTA_ITERATION_082.md`

## Iteration 083 — sequential retuning

For retuned settings with raw science informations `P2,P4` and independent gain/relock reference Fisher `C2,C4`, profiling gives

`F_beta = P2 C2/(P2+C2) + P4 C4/(P4+C4)`.

**RQIR-NG-034:** if retuned settings have independent unconstrained gains (`C2=C4=0`), then `F_beta=0` at arbitrary science exposure. Sequential retuning does not reproduce a shared two-band likelihood for free.

Files:
- `analysis/sequential_retuning_gain_profile_iteration083.py`
- `docs/PAPER_III_SEQUENTIAL_RETUNING_LIKELIHOOD_ITERATION083.md`
- `recovery/RECOVERY_DELTA_ITERATION_083.md`

## Iteration 084 — simultaneous dual-band physical rate

For simultaneous whitened band Fisher rates `r2,r4`, with the mature antisymmetric spectral-tilt nuisance,

`P2=r2 T`, `P4=r4 T`,

so

`F_beta|tilt(T) = R_2band T`,

with

`boxed{R_2band = 4 r2 r4/(r2+r4)}`.

**RQIR-RESOURCE-038:** the simultaneous two-band science throughput is twice the ordinary harmonic mean of `r2,r4`.

**RQIR-NG-035:** for fixed weak-band rate `r_w`, even an arbitrarily strong partner band gives only `R_2band -> 4 r_w`. Therefore any target `R_*` requires both bands individually above `R_*/4`.

Inverse partner requirement:

`r4 >= R_* r2/(4 r2-R_*)`,

with no finite solution for `4 r2 <= R_*`.

At `Z=5`, science-only profiled-rate targets are:

- 1 day: `R_beta >= 2.8935185e-4 s^-1`;
- 7 days: `R_beta >= 4.1335979e-5 s^-1`;
- 30 days: `R_beta >= 9.6450617e-6 s^-1`.

Balanced bands each require half the corresponding profiled rate. These are specifications, not apparatus forecasts.

External literature confirms simultaneous multimode levitated readout/control is experimentally real, but no searched platform supplied a complete RQIR-ready force PSD/cross-PSD data set at two simultaneous bands in exact 2:1 ratio plus all calibration/source/control channels. Keep the apparatus model parameterized until those data exist.

Files:
- `analysis/simultaneous_dual_band_rate_iteration084.py`
- `docs/PAPER_III_SIMULTANEOUS_DUAL_BAND_RATE_ITERATION084.md`
- `research_log/2026-08-30_iteration_084_simultaneous_dual_band_rate.md`
- `recovery/RECOVERY_DELTA_ITERATION_084.md`

## Immediate next gate — Paper III only

Construct a physical two-band detector specification with measured/declared `S_F,2`, `S_F,4`, complex transfer functions/windows and cross-PSD. Convert these to nuisance-profiled `r2,r4`, then set `R_beta=4 r2 r4/(r2+r4)`.

After that, propagate the **same apparatus model** through all seven `R_cal,j`, independent `R_src`, control duty and uncertainties, and apply NG-030 to Toy009 versus Toy014. Do not start Toy015 unless that full rate map shows a genuinely source-dependent bottleneck.

## Discipline

RQIR remains separate from RTK/DSIR. No toy, Fisher, resource or detector-model result is an empirical new-physics detection or a complete theory of quantum gravity. Classical/stochastic/hybrid/full-QFT degeneracy, relativistic, gauge/conservation/causality/EFT/renormalization and experimental-measurability gates remain open unless explicitly closed elsewhere in the repository.
