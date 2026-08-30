# RQIR Iteration 124 — Manuscript-Ready Paper III Skeleton

**Date:** 2026-08-31  
**Status:** manuscript architecture / scientific-gap audit. No apparatus forecast and no new-physics claim.

## 1. Purpose

Iteration 123 separated standard Fisher/OED/gravity-test ingredients from the candidate RQIR integration-level contribution. The next admissible gate is to arrange the mature Paper-III results into a claim-by-claim manuscript structure and expose any remaining scientific link that would prevent writing.

The central editorial rule is inherited from CAL-024: theorem/derivation, deterministic toy regression, experimental precedent, parametric specification, open gate and candidate novelty must not be mixed.

## 2. Proposed central manuscript claim

**Paper III claim:** a gravity-interface discriminator is experimentally meaningful only after its source-preparation, detector nuisance, transfer, calibration, control and scheduling uncertainties are propagated into one nuisance-profiled Fisher-rate / wall-clock certificate. RQIR supplies this end-to-end specialization for the Toy009/Toy014 detector architecture and identifies the exact measurements still required for an apparatus-specific numerical verdict.

This is an integration-level claim, not a claim to have invented Fisher profiling, optimal design, cross-spectral sensing or gravity-test resource accounting in isolation.

## 3. Section map

### Section I — From theoretical discriminant to detector identifiability

**Claim.** Exact source-level distinguishability does not imply detector-level identifiability.

**Core equation**

`F_beta|theta = F_bb - F_btheta F_thetatheta^-1 F_thetab`.

**Repository support.** Statistical Identifiability chain; exact hard-constraint correction NUM-001; centered covariance CAL-013; D1/D2 detector-level profiling.

**Figure/table target.** One schematic showing `source discriminant -> calibration/null geometry -> detector likelihood -> F_beta|theta` and one table separating exact rank from finite Fisher closure.

**Literature comparator.** Standard nuisance-profiled Fisher / optimal-design literature must be cited as prior machinery.

**Limitation.** The equation is standard; the RQIR-specific content is the physical gravity-interface score/nuisance construction.

### Section II — RQIR-NG-005 and physical source-preparation metrology

**Claim.** A gravitational null experiment cannot self-calibrate the hidden source amplitude when detector response is locally collinear in `beta` and source amplitude.

**Core equations**

`F_beta|alpha = S C_prep/(S+C_prep)`

and for retained fraction `r` at target significance `Z`,

`C_prep=[r/(1-r)] Z^2`.

At the retained `r=0.9`, `Z=5` benchmark, `C_prep=225`.

**Physical bridge.** For per-copy source-metrology Fisher `I_alpha,copy`,

`N_acc=C_prep/I_alpha,copy`,

`R_alpha=p I_alpha,copy/tau_copy`,

`T_src=C_prep/R_alpha`.

**Regression targets.** Toy009 full QFI `0.0849323916`; energy-population Fisher `0.0093918844`; source-copy/reset bounds already stored in the resource chain.

**Figure/table target.** Source-metrology branch table: QFI ceiling, projective energy, pointer, Ramsey; accepted copies and reset-limited rate.

**Limitation.** Strong source metrology is placed on independent/sacrificial copies unless a same-copy nondemolition likelihood is explicitly proved (NG-023).

### Section III — Calibration Fisher as shots, detector SNR, coherence and wall time

**Claim.** The abstract calibration target `gamma` becomes a physical resource only after a declared detector likelihood supplies per-cycle Fisher rates.

**Core equations**

`I_j = 4 int |d htilde_j/du_j|^2/S_out,j(f) df`,

`R_cal,j=p_j I_j/tau_j`,

and for independent layers

`T_cal=gamma sum_j 1/R_cal,j`.

For a full correlated two-row layer, use

`R_cal,j=lambda_min(F_j)`.

**Coherence accounting.** Independent time layers pay their own evolution/reset/readout durations; cross-time noncommuting rows cannot be credited to one disturbance-free trajectory without an explicit backaction model.

**Regression target.** Toy009 seven-layer mean campaign and Toy014/Toy009 rate-ratio regressions from Iterations 068–088 and 118–121.

**Figure/table target.** Seven-layer time/resource Sankey or stacked budget; separate strong-measurement and shared-output envelopes.

**Limitation.** A numerical wall-clock forecast requires a same-apparatus transduction/PSD/cross-PSD dataset.

### Section IV — Transfer gain/phase and control recertification inside the likelihood

**Claim.** Transfer uncertainty cannot be treated as an external tolerance independent of the science likelihood.

**Core equations**

After profiling non-transfer nuisances,

`F_beta(C)=F0-b^T(G+C)^-1 b`.

For the two-band common-gain reference, with `nu=(d,phi2,phi4)`,

`R_c=k_cc-k_cnu K_nunu^-1 k_nuc`.

Science plus separate common-gain reference has

`R_DT=1/[1/sqrt(R_s)+1/sqrt(R_c)]^2`.

**Control extension.** Matrix recertification obeys

`(t_ref F_ref)^-1 + tau Q/2 <= S`.

**Figure/table target.** A block-matrix diagram showing common gain, differential gain/spectral tilt and phase nuisance profiling; one control-cadence panel.

**Limitation.** Same hardware does not imply identical transfer Fisher rate between source architectures (NG-072); physical drift/floor remains apparatus-specific.

### Section V — Non-double-counted campaign scheduling and reference-span gates

**Claim.** Shared calibration blocks must be credited once and must span every required nuisance direction; more exposure cannot repair missing score directions.

**Core equations**

For one joint reference:

`T_ref,* = lambda_max(K_ref^-1/2 H_* K_ref^-1/2)`.

For multiple campaigns:

`min sum_k t_k` subject to `sum_k t_k K_k >= H_*`.

Finite quota feasibility requires

`range(H_*) subseteq range(K_tot)`.

**Exact Toy009/Toy014 regression.** After hard constraints the source nuisance space has dimension 22. Seven mean dual-probe layers supply rank 14; centered covariance rows add the missing rank 8. Repetition of an unchanged four-real dual-tone setting cannot create missing directions.

**Figure/table target.** Rank-accumulation plot `0 -> 14 -> 22` and calibration-setting coverage matrix.

**Limitation.** Covariance matching-block credit remains subject to source-observable backaction compatibility.

### Section VI — Detector-side Toy009/Toy014 resource interval

**Claim.** The detector architecture comparison can be expressed as a robust Fisher-rate interval without inventing detector ASD values.

Define

`u=R_D14/R_D09`.

The mature detector chain propagates uncertainty in science, transfer, mean and covariance rates into a lower/upper interval for `u`.

**Key result.** Iterations 120–121 distinguish conservative strong-measurement, intermediate matching-block and optimistic shared-output calibration branches. The resulting interval algebra is exact for the declared rate boxes.

**Figure/table target.** `u` interval versus calibration-sharing assumption; apparatus-input table showing which rates are measured, parameterized or missing.

**Limitation / principal open gate.** No public same-apparatus dataset currently supplies the complete force-calibrated `f,2f` PSD/cross-PSD, transfer Fisher, seven calibration rates, covariance/backaction and control drift needed for a numerical apparatus-specific `u`. Therefore Paper III must not state a measured Toy009/Toy014 winner.

### Section VII — Final-significance architecture certificate

**Claim.** Source design can be compared only after detector information, source metrology and control duty are combined at the final significance level.

Use

`u=R_D14/R_D09`,

`v=R_A14/R_A09`,

`z=R_A09/R_D09`,

`delta=(1-d14)/(1-d09)`.

Then

`Q14/Q09 = delta[(1+z^-1/2)/(u^-1/2+(v z)^-1/2)]^2`.

**Figure/table target.** Architecture phase diagram in `(u,v,z,delta)` showing robust win/loss/unresolved regions; no apparatus point unless independently justified.

**Limitation.** NG-030 requires interval separation for a robust winner; overlapping bounds remain unresolved.

### Section VIII — Experimental precedent and what remains to measure

**Claim.** Published experiments establish component feasibility, not a complete RQIR apparatus forecast.

Iteration 122 found external demonstrations of calibrated transfer-function force sensing, cross-spectral/multimode readout, gain/phase control and exact simultaneous fundamental/second-harmonic operation. These support feasibility of individual ingredients.

**Table target.** Rows = required RQIR apparatus inputs; columns = demonstrated externally / available in one same-state likelihood / still missing.

**Limitation.** No found publication supplies the full compatible input vector required by RESOURCE-094-style apparatus closure.

## 4. Candidate figures/tables in minimum viable manuscript

1. End-to-end RQIR Paper-III resource pipeline.
2. NG-005 source-amplitude degeneracy and independent-metrology repair.
3. Seven-layer calibration/resource schedule with coherence/reset accounting.
4. Common-gain/phase transfer profile and recertification block.
5. Rank/span coverage and no-double-counting diagram.
6. Toy009/Toy014 robust detector-rate interval / final architecture phase diagram.
7. Experimental input-gap table.

These are figure targets, not generated experimental plots.

## 5. Final scientific gap exposed by the skeleton

The manuscript chain is algebraically connected from source discrimination through final significance. The remaining unresolved object is **not another abstract Fisher parameter**. It is the physical same-apparatus data vector needed for a numerical detector architecture verdict:

- same-state two-band science PSD/cross-PSD and transduction;
- full complex transfer-reference Fisher/covariance;
- seven calibration-layer Fisher-rate matrices;
- covariance/backaction compatibility if shared blocks are used;
- geometry/additive SI reference rates;
- drift/floor/recertification inputs;
- source-metrology rate and duty in the same architecture accounting.

Therefore Paper III can be written as a rigorous **resource-certificate / design-theory paper with parametric apparatus closure**, while any specific experimental runtime/winner must remain conditional until those inputs exist.

### RQIR-NG-082 — manuscript closure is not apparatus closure

A complete symbolic/parametric end-to-end resource theorem must not be worded as a completed experimental forecast. Conversely, lack of a full public same-apparatus dataset does not invalidate the resource-certificate result; it limits only the numerical apparatus verdict.

### RQIR-DESIGN-020 — measure the closure vector, not isolated headline sensitivities

The highest-value experimental characterization is the smallest common set of same-state Fisher-rate/covariance/control measurements sufficient to instantiate the final `(u,v,z,delta)` certificate. Improving an isolated ASD or calibration SNR is lower value if another missing nuisance block still keeps NG-030 unresolved.

## 6. Readiness snapshot — Iteration 124

Project-management estimates, not statistical confidence measures:

- **Paper III scientific-content readiness:** **96%**.
- **Paper III submission readiness:** **86%**.
- **Repository readiness to begin a concrete Candidate-Gravity model:** **85%**.
- **Concrete Candidate-Gravity model itself:** **~10%**.

The scientific score rises modestly because the skeleton confirms the full inferential/resource chain and isolates one physical-data closure gap rather than a missing theoretical link. Submission readiness rises more because the claim/equation/figure/comparator/limitation structure is now explicit.

## 7. Next admissible gate

Perform the final manuscript-facing **notation and dependency audit**:

1. build a canonical symbol table for `beta`, source amplitude, `gamma`, `R_s`, `R_c`, `R_cal`, `R_A`, `u,v,z,delta`, duty and significance;
2. map every Paper-III claim to its exact repository theorem/regression file;
3. detect stale/contradictory numbering and duplicate resource/no-go labels;
4. create a minimum reproducibility command list for all manuscript figures/tables;
5. update `CURRENT_FRONT.md` so continuity no longer points to Iteration 117.

After that, prose drafting is admissible. A numerical apparatus winner remains conditional on the closure vector above.

## 8. Reproducibility

Run

`python analysis/paper3_manuscript_skeleton_iteration124.py`.

The checker verifies eight manuscript sections, theorem-bearing closure tags and the explicit rule that the detector architecture section remains non-apparatus-closed.
